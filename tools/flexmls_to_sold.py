#!/usr/bin/env python3
"""Convert a Flexmls Generic Text Export of Tara's closed sales into _data/sold.json.
Usage: python3 tools/flexmls_to_sold.py <export.csv>
Re-run whenever a new export is pulled (saved search: "Tara - Career Closed Sales")."""
import csv, json, re, sys, os

ZIP_SLUG = {  # Knoxville-city zips -> area page slug
    '37931':'karns','37932':'hardin-valley','37934':'farragut','37922':'farragut',
    '37938':'halls','37918':'halls','37849':'powell','37920':'south-knoxville',
    '37912':'north-knoxville','37917':'north-knoxville','37919':'bearden',
    '37909':'west-knoxville','37921':'west-knoxville','37923':'west-knoxville',
    '37902':'knoxville','37914':'knoxville','37915':'knoxville','37916':'knoxville','37924':'knoxville',
}
CITY_SLUG = {
    'Lenoir City':'lenoir-city','Loudon':'lenoir-city','Oak Ridge':'oak-ridge','Clinton':'clinton',
    'Maryville':'maryville','Alcoa':'maryville','Powell':'powell','Jefferson City':'jefferson-city',
    'Madisonville':'madisonville','Sweetwater':'sweetwater','Sevierville':'sevierville',
    'Morristown':'morristown','Louisville':'louisville','Seymour':'seymour','Townsend':'townsend',
    'Greenback':'greenback','Dandridge':'dandridge','Athens':'athens','Decatur':'decatur',
    'Maynardville':'maynardville','Pigeon Forge':'pigeon-forge',
}

def tara(s): return 'hayes' in (s or '').lower() and 'tara' in (s or '').lower()

def price_range(p):
    if p < 100000: return "Under $100K"
    lo = int(p // 50000) * 50000
    if lo >= 1000000:
        fmt = lambda v: f"${v/1_000_000:g}M"
        return f"{fmt(lo)}–{fmt(lo+50000)}"
    return f"${lo//1000}K–${(lo+50000)//1000}K"

# Closed deals verified in brokerage records but absent from the ETR export
# (e.g. co-op sales recorded in another MLS board). Kept across regenerations.
MANUAL_EXTRA = [
    {"mls": "1317890", "addr": "226 Deer Run Point", "city": "LaFollette", "zip": "37766",
     "slug": None, "date": "2026-03-31", "year": "2026", "range": "$1.05M–$1.1M",
     "role": "Represented buyer", "beds": "4", "baths": "4", "sqft": None,
     "sub": "Deerfield Resort", "ptype": "home", "acres": None, "photo": None, "img": False},
]

def main(src):
    rows = list(csv.DictReader(open(src, newline='', encoding='utf-8', errors='replace')))
    out = []
    for r in rows:
        lister, sel = tara(r['Listing Agent']) or tara(r['Co-Listing Agent']), tara(r['Selling Agent']) or tara(r['Co-Selling Agent'])
        if not (lister or sel):  # not hers; skip defensively
            continue
        role = "Both sides" if (lister and sel) else ("Represented seller" if lister else "Represented buyer")
        price = float(re.sub(r'[^\d.]', '', r['Sold Price'] or '0') or 0)
        if price <= 0: continue
        addr = ' '.join(x.strip() for x in [r['House #'], r['St Dir'], r['Street Name'], r['St Suffix']] if (x or '').strip())
        if (r['Unit #'] or '').strip(): addr += ' #' + r['Unit #'].strip()
        city, zc = (r['City'] or '').strip(), (r['Zip Code'] or '').strip()[:5]
        slug = ZIP_SLUG.get(zc) if city == 'Knoxville' else CITY_SLUG.get(city)
        street = (r['Street Name'] or '').lower()
        if 'taliluna' in street or 'sequoyah' in ((r['Subdivision'] or '').lower() + street): slug = 'sequoyah-hills'
        date = (r['Sold Date'] or '').strip()
        sub = (r['Subdivision'] or '').strip()
        sub = '' if sub.lower() in ('', 'none', 'n/a', 'na', 'no', 'other') else re.sub(r'\s+lot\s+\S+$', '', sub, flags=re.I).strip()
        try: sqft = int(float(r['SqFt - Total (Aprox)'] or 0))
        except ValueError: sqft = 0
        try: acres = float(r.get('Acres') or 0)
        except ValueError: acres = 0.0
        PT = {'Residential':'home','Land':'land','MultiFamily':'multi','Commercial':'commercial'}
        ptype = PT.get((r.get('Property Type') or 'Residential').strip(), 'home')
        out.append({
            'mls': (r['List Number'] or '').strip(),
            'addr': addr.title().replace("'S", "'s"),
            'city': city, 'zip': zc, 'slug': slug,
            'date': date, 'year': date[:4],
            'range': price_range(price), 'role': role,
            'beds': (r['# Bedrooms'] or '').strip() or None,
            'baths': (r['Baths - Full'] or '').strip() or None,
            'sqft': sqft or None, 'sub': sub or None,
            'ptype': ptype, 'acres': round(acres, 2) if acres else None,
            'photo': (r['Photo URL'] or '').strip() or None,
        })
    have = {x['mls'] for x in out}
    out.extend(x for x in MANUAL_EXTRA if x['mls'] not in have)
    out.sort(key=lambda x: x['date'], reverse=True)
    dst = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '_data', 'sold.json')
    json.dump(out, open(dst, 'w'), indent=1)
    import collections
    slugs = collections.Counter(x['slug'] for x in out)
    print(f"wrote {len(out)} sales -> {dst}")
    print("by area page:", dict(slugs.most_common()))

if __name__ == '__main__': main(sys.argv[1])

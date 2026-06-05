#!/usr/bin/env python3
"""
Tag Fortune 1000 companies in all/* apis.yml files.

Matches the Fortune 1000 list (rank-ordered) against slugs in all/*
using normalized name matching, then inserts or updates the top-level
tags: block with Fortune 100 / Fortune 500 / Fortune 1000 as appropriate.

Usage:
    python3 tag-fortune1000.py          # dry run
    python3 tag-fortune1000.py --write  # apply changes
"""
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ALL = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(HERE))), "all")

DRY_RUN = "--write" not in sys.argv

# ---------------------------------------------------------------------------
# Fortune 1000 list — rank order, position = rank (1-based)
# ---------------------------------------------------------------------------
FORTUNE_1000 = [
    "Walmart", "Exxon Mobil", "Chevron", "Berkshire Hathaway", "Apple",
    "General Motors", "Phillips 66", "General Electric", "Ford Motor", "CVS Health",
    "McKesson", "AT&T", "Valero Energy", "UnitedHealth Group", "Verizon",
    "AmerisourceBergen", "Fannie Mae", "Costco", "HP", "Kroger",
    "JP Morgan Chase", "Express Scripts Holding", "Bank of America", "IBM",
    "Marathon Petroleum", "Cardinal Health", "Boeing", "Citigroup", "Amazon",
    "Wells Fargo", "Microsoft", "Procter & Gamble", "Home Depot",
    "Archer Daniels Midland", "Walgreens", "Target", "Johnson & Johnson",
    "Anthem", "MetLife", "Alphabet", "State Farm Insurance", "Freddie Mac",
    "Comcast", "PepsiCo", "United Technologies", "AIG", "UPS", "Dow Chemical",
    "Aetna", "Lowe's", "ConocoPhillips", "Intel", "Energy Transfer",
    "Caterpillar", "Prudential Financial", "Pfizer", "Walt Disney", "Humana",
    "Enterprise Products Partners", "Cisco Systems", "Sysco", "Ingram Micro",
    "Coca-Cola", "Lockheed Martin", "FedEx", "Johnson Controls",
    "Plains GP Holdings", "World Fuel Services", "CHS", "American Airlines",
    "Merck", "Best Buy", "Delta Air Lines", "Honeywell", "HCA Holdings",
    "Goldman Sachs", "Tesoro", "Liberty Mutual Insurance", "United Airlines",
    "New York Life Insurance", "Oracle", "Morgan Stanley", "Tyson Foods",
    "Safeway", "Nationwide", "Deere", "DuPont", "American Express",
    "Allstate", "Cigna", "Mondelez International", "TIAA", "INTL FCStone",
    "Massachusetts Mutual Life Insurance", "DirecTV", "Halliburton",
    "Twenty-First Century Fox", "3M", "Sears Holdings", "General Dynamics",
    "Publix Super Markets", "Philip Morris International", "TJX",
    "Time Warner", "Macy's", "Nike", "Tech Data", "Avnet",
    "Northwestern Mutual", "McDonald's", "Exelon", "Travelers",
    "Qualcomm", "International Paper", "Occidental Petroleum", "Duke Energy",
    "Rite Aid", "Gilead Sciences", "Baker Hughes", "Emerson Electric", "EMC",
    "USAA", "Union Pacific", "Northrop Grumman", "Alcoa", "Capital One",
    "National Oilwell Varco", "US Foods", "Raytheon", "Time Warner Cable",
    "Arrow Electronics", "Aflac", "Staples", "Abbott Laboratories",
    "Community Health Systems", "Fluor", "Freeport-McMoRan", "US Bancorp",
    "Nucor", "Kimberly-Clark", "Hess", "Chesapeake Energy", "Xerox",
    "ManpowerGroup", "Amgen", "AbbVie", "Danaher", "Whirlpool",
    "PBF Energy", "HollyFrontier", "Eli Lilly", "Devon Energy", "Progressive",
    "Cummins", "Icahn Enterprises", "AutoNation", "Kohl's", "Paccar",
    "Dollar General", "Hartford Financial Services", "Southwest Airlines",
    "Anadarko Petroleum", "Southern Company", "Supervalu", "Kraft Foods",
    "Goodyear Tire & Rubber", "EOG Resources", "CenturyLink", "Altria Group",
    "Tenet Healthcare", "General Mills", "eBay", "ConAgra Foods", "Lear",
    "TRW Automotive", "United States Steel", "Penske Automotive Group",
    "AES", "Colgate-Palmolive", "Global Partners", "Thermo Fisher Scientific",
    "PG&E", "NextEra Energy", "American Electric Power", "Baxter International",
    "Centene", "Starbucks", "Gap", "Bank of New York Mellon",
    "Micron Technology", "Jabil", "PNC Financial Services", "Kinder Morgan",
    "Office Depot", "Bristol-Myers Squibb", "NRG Energy", "Monsanto",
    "PPG Industries", "Genuine Parts", "Omnicom Group", "Illinois Tool Works",
    "Murphy USA", "Land O'Lakes", "Western Refining", "Western Digital",
    "FirstEnergy", "Aramark", "DISH Network", "Las Vegas Sands", "Kellogg",
    "Loews", "CBS", "Ecolab", "Whole Foods Market", "Chubb",
    "Health Net", "Waste Management", "Apache", "Textron", "Synnex",
    "Marriott International", "Viacom", "Lincoln National", "Nordstrom",
    "C.H. Robinson", "Edison International", "Marathon Oil", "Yum Brands",
    "Computer Sciences", "Parker-Hannifin", "DaVita", "CarMax",
    "Texas Instruments", "WellCare Health Plans", "Marsh & McLennan",
    "Consolidated Edison", "Oneok", "Visa", "Jacobs Engineering",
    "CSX", "Entergy", "Facebook", "Dominion Resources", "Leucadia National",
    "Toys R Us", "DTE Energy", "Ameriprise Financial", "VF Corporation",
    "Praxair", "JC Penney", "Automatic Data Processing", "L-3 Communications",
    "CDW", "Guardian Life Insurance", "Xcel Energy", "Norfolk Southern",
    "PPL", "RR Donnelley", "Huntsman", "Bed Bath & Beyond",
    "Stanley Black & Decker", "L Brands", "Liberty Interactive",
    "Farmers Insurance", "First Data", "Sherwin-Williams", "BlackRock",
    "Voya Financial", "Ross Stores", "Sempra Energy", "Estee Lauder",
    "HJ Heinz", "Reinsurance Group of America", "Public Service Enterprise Group",
    "Cameron International", "Navistar International", "State Street",
    "Unum Group", "Hilton Hotels", "Family Dollar", "Principal Financial",
    "Reliance Steel & Aluminum", "Air Products & Chemicals", "Assurant",
    "Peter Kiewit Sons", "Henry Schein", "Cognizant Technology Solutions",
    "MGM Resorts International", "WW Grainger", "Group 1 Automotive",
    "BB&T", "WestRock", "Advance Auto Parts", "Ally Financial", "AGCO",
    "Corning", "Biogen", "NGL Energy Partners", "Stryker",
    "Molina Healthcare", "Precision Castparts", "Discover Financial Services",
    "Genworth Financial", "Eastman Chemical", "Dean Foods", "AutoZone",
    "Mastercard", "Owens & Minor", "Hormel Foods", "GameStop", "Autoliv",
    "CenterPoint Energy", "Fidelity National Financial", "Sonic Automotive",
    "HD Supply", "Charter Communications", "Crown Holdings",
    "Applied Materials", "Mosaic", "CBRE Group", "Avon Products",
    "Republic Services", "Universal Health Services", "Darden Restaurants",
    "Steel Dynamics", "SunTrust Banks", "Caesars Entertainment",
    "Targa Resources", "Dollar Tree", "News Corp", "Ball Corporation",
    "Thrivent Financial", "Masco", "Franklin Resources", "Avis Budget",
    "Reynolds American", "Becton Dickinson", "Priceline", "Broadcom",
    "Tenneco", "Campbell Soup", "AECOM", "Visteon", "Delek US Holdings",
    "Dover", "BorgWarner", "Jarden", "UGI", "Murphy Oil", "PVH",
    "Core-Mark", "Calpine", "DR Horton", "Weyerhaeuser", "KKR",
    "FMC Technologies", "American Family Insurance", "SpartanNash",
    "WESCO International", "Quanta Services", "Mohawk Industries",
    "Motorola Solutions", "Lennar", "TravelCenters of America",
    "Sealed Air", "Eversource Energy", "Coca-Cola Enterprises", "Celgene",
    "Williams Companies", "Ashland", "Interpublic Group", "Blackstone Group",
    "Ralph Lauren", "Quest Diagnostics", "Hershey", "Terex",
    "Boston Scientific", "Newmont Mining", "Allergan", "O'Reilly Automotive",
    "Casey's General Stores", "CMS Energy", "Foot Locker", "WR Berkley",
    "PetSmart", "Pacific Life", "Commercial Metals", "Agilent Technologies",
    "Huntington Ingalls Industries", "Mutual of Omaha", "Live Nation",
    "Dick's Sporting Goods", "Oshkosh", "Celanese", "Spirit AeroSystems",
    "United Natural Foods", "Peabody Energy", "Owens-Illinois", "Dillard's",
    "Level 3 Communications", "LKQ", "Symantec", "Ryder System",
    "SanDisk", "Rockwell Automation", "Dana Holding", "NCR",
    "Expeditors International", "AK Steel", "Fifth Third Bancorp",
    "Seaboard", "NiSource", "Cablevision Systems", "Anixter",
    "EMCOR Group", "Fidelity National Information Services",
    "Barnes & Noble", "KBR", "Avery Dennison", "NetApp",
    "iHeartMedia", "Discovery Communications", "Harley-Davidson", "Sanmina",
    "Trinity Industries", "JB Hunt Transport", "Charles Schwab",
    "Erie Insurance", "Dr Pepper Snapple", "Ameren", "Mattel",
    "Laboratory Corp of America", "TEGNA", "Starwood Hotels & Resorts",
    "General Cable", "Graybar Electric", "MRC Global", "Spectra Energy",
    "Asbury Automotive", "Packaging Corp of America", "Windstream Holdings",
    "PulteGroup", "JetBlue Airways", "Newell Rubbermaid", "Expedia",
    "American Financial Group", "Tractor Supply", "United Rentals",
    "Ingredion", "Navient", "AGL Resources", "St Jude Medical",
    "JM Smucker", "Western Union", "Clorox", "Domtar", "Kelly Services",
    "Old Republic International", "Advanced Micro Devices", "Netflix",
    "Booz Allen Hamilton", "Quintiles Transnational", "Wynn Resorts",
    "Jones Lang LaSalle", "Regions Financial", "Western & Southern Financial",
    "Lithia Motors", "Salesforce", "Alaska Air Group", "Host Hotels",
    "Harman International", "Amphenol", "Realogy Holdings",
    "Hanesbrands", "Kindred Healthcare", "Insight Enterprises",
    "Alliance Data Systems", "LifePoint Health", "Pioneer Natural Resources",
    "Wyndham Hotels", "Owens Corning", "Alleghany", "McGraw Hill Financial",
    "Big Lots", "Markel", "Noble Energy", "Leidos Holdings",
    "Rockwell Collins", "Airgas", "YRC Worldwide", "Hanover Insurance",
    "Fiserv", "ABM Industries", "Sonoco Products", "Harris Corporation",
    "Telephone & Data Systems", "WEC Energy", "Raymond James Financial",
    "Berry Plastics", "SCANA", "Cincinnati Financial", "Atmos Energy",
    "Flowserve", "Simon Property Group", "Constellation Brands",
    "Burlington Stores", "Neiman Marcus", "Levi Strauss", "SPX",
    "CF Industries", "Michaels", "M&T Bank", "Rush Enterprises",
    "Williams-Sonoma", "Robert Half International", "Nvidia",
    "First American Financial", "Zimmer Biomet", "MDU Resources",
    "Juniper Networks", "Arthur J Gallagher", "Lam Research",
    "Intercontinental Exchange", "Cintas", "Coty", "CA Technologies",
    "Valspar", "Northern Trust", "Intuit", "Polaris Industries",
    "Hyatt Hotels", "Activision Blizzard", "Fortune Brands",
    "RPM International", "KeyCorp", "Swift Transportation",
    "Alpha Natural Resources", "Hasbro", "Tiffany", "McCormick",
    "Graphic Packaging", "Greif", "Allegheny Technologies",
    "Securian Financial", "Adobe Systems", "Molson Coors",
    "Chipotle Mexican Grill", "American Tower", "FMC Corporation",
    "AmTrust Financial", "Brunswick", "Southwestern Energy", "Ametek",
    "T Rowe Price", "Torchmark", "Darling Ingredients",
    "Leggett & Platt", "Watsco", "Xylem", "Silgan Holdings",
    "Toll Brothers", "Manitowoc", "Science Applications International",
    "Carlyle Group", "Timken", "Pitney Bowes", "Ingles Markets",
    "Brookdale Senior Living", "CommScope", "Meritor",
    "Triumph Group", "Sally Beauty", "Flowers Foods",
    "Abercrombie & Fitch", "New Jersey Resources", "Fastenal",
    "Consol Energy", "USG", "Brink's", "Helmerich & Payne",
    "Lexmark International", "American Axle", "Crown Castle",
    "Oceaneering International", "Cabot", "CIT Group",
    "Cabela's", "QEP Resources", "Thor Industries",
    "Graham Holdings", "Electronic Arts", "Boise Cascade",
    "Hub Group", "CACI International", "Roper Technologies",
    "Fossil Group", "Nasdaq", "Snap-on", "Pinnacle West Capital",
    "Cerner", "Clean Harbors", "First Solar", "Lennox International",
    "Hubbell", "Unisys", "Alliant Energy", "Welltower",
    "Moody's", "CR Bard", "Urban Outfitters", "Church & Dwight",
    "American Eagle Outfitters", "Oaktree Capital",
    "Cooper Tire & Rubber", "ADT", "Ulta Beauty",
    "Hawaiian Electric", "SkyWest", "Green Plains", "NBTY",
    "Carlisle Companies", "Tesla Motors", "Groupon",
    "Landstar System", "Patterson-UTI Energy", "EP Energy",
    "ON Semiconductor", "Rent-A-Center", "SunGard Data Systems",
    "Citrix Systems", "Amkor Technology", "TD Ameritrade",
    "Worthington Industries", "Valmont Industries", "Iron Mountain",
    "CME Group", "International Flavors & Fragrances",
    "Whiting Petroleum", "Under Armour", "Ventas",
    "NuStar Energy", "Select Medical", "Diebold",
    "American National Insurance", "Varian Medical Systems",
    "Westinghouse Air Brake", "American Water Works",
    "H&R Block", "Mercury General", "TECO Energy",
    "Service Corp International", "Vulcan Materials", "Brown-Forman",
    "Regal Entertainment", "Tempur Sealy", "Steelcase",
    "Martin Marietta Materials", "Huntington Bancshares",
    "TreeHouse Foods", "KLA-Tencor", "Crane",
    "Dentsply Sirona", "Tribune Media", "ScanSource",
    "Brinker International", "Carter's", "Analog Devices",
    "Genesco", "Scotts Miracle-Gro", "WABCO Holdings",
    "Kennametal", "Amerco", "Team Health",
    "Regeneron Pharmaceuticals", "OneMain Holdings",
    "Lincoln Electric", "West Corporation", "Benchmark Electronics",
    "Old Dominion Freight Line", "MSC Industrial Direct",
    "Sentry Insurance", "WGL Holdings", "Weis Markets",
    "Sanderson Farms", "Wolverine World Wide", "Legg Mason",
    "Teradata", "Aaron's", "Range Resources",
    "Vornado Realty Trust", "Boyd Gaming",
    "Armstrong World Industries", "Cracker Barrel",
    "Chico's FAS", "Scripps Networks Interactive",
    "Universal Forest Products", "Concho Resources",
    "ITT", "Moog", "Cinemark Holdings", "Comerica",
    "Equity Residential", "GNC Holdings",
    "Curtiss-Wright", "Tupperware Brands", "Westar Energy",
    "Albemarle", "AptarGroup", "Pinnacle Foods",
    "Penn National Gaming", "Vantiv", "Kansas City Southern",
    "Nu Skin Enterprises", "Great Plains Energy", "Kirby Corporation",
    "General Growth Properties", "Broadridge Financial",
    "Stericycle", "Global Payments", "Nortek",
    "Schnitzer Steel", "Universal Corporation",
    "Hologic", "Panera Bread", "AOL", "SM Energy",
    "Paychex", "Autodesk", "Affiliated Managers Group",
    "Dynegy", "Vishay Intertechnology", "Mettler-Toledo",
    "SunEdison", "Tetra Tech", "EnerSys", "Donaldson",
    "EQT", "Monster Beverage", "Total System Services",
    "ServiceMaster", "Applied Industrial Technologies",
    "Maxim Integrated", "OGE Energy", "Equinix",
    "Mednax", "Equifax", "Denbury Resources", "Cimarex Energy",
    "Post Holdings", "HealthSouth", "KB Home",
    "Boston Properties", "Trimble Navigation",
    "Teledyne Technologies", "Acuity Brands",
    "Skechers", "Xilinx", "Plexus",
    "Newfield Exploration", "TransDigm Group",
    "Kar Auction Services", "Mueller Industries",
    "Zions Bancorp", "Insperity", "XPO Logistics",
    "A.O. Smith", "Take-Two Interactive",
    "RPC Inc", "NewMarket", "Beacon Roofing Supply",
    "Edwards Lifesciences", "Hawaiian Holdings",
    "Heartland Payment Systems", "Belden",
    "Magellan Midstream Partners", "KapStone Paper & Packaging",
    "Alliance Holdings", "Skyworks Solutions", "Ciena",
    "Granite Construction", "HCP Inc",
    "Parexel International", "Pinnacle Entertainment",
    "Stifel Financial", "Pool Corporation", "Olin",
    "PerkinElmer", "Alexion Pharmaceuticals",
    "Oil States International", "HNI Corporation",
    "LinkedIn", "Diplomat Pharmacy",
    "Brocade Communications", "Greenbrier",
    "AMC Networks", "Kemper", "Public Storage",
    "TriNet Group", "Chemtura", "Symetra Financial",
    "Tower International", "Meritage Homes",
    "Bio-Rad Laboratories", "TrueBlue",
    "Cabot Oil & Gas", "Carpenter Technology",
    "Toro Company", "American Equity Investment Life",
    "Express Inc", "Hain Celestial Group",
    "Nationstar Mortgage", "IDEX Corporation",
    "Popular Inc", "Werner Enterprises",
    "Esterline Technologies", "Intuitive Surgical",
    "Allison Transmission", "SemGroup",
    "Southwest Gas", "G-III Apparel",
    "National Fuel Gas", "HB Fuller",
    "Columbia Sportswear", "Primoris Services",
    "Energen", "Rexnord", "Waste Connections",
    "Wendy's", "International Game Technology",
    "Synopsys", "AAR Corp", "Selective Insurance",
    "Gartner", "E*Trade Financial",
]


# ---------------------------------------------------------------------------
# Name normalisation helpers
# ---------------------------------------------------------------------------

CORP_SUFFIXES = re.compile(
    r'\b(corp\.?|corporation|incorporated|inc\.?|llc|ltd\.?|limited|'
    r'co\.?|company|group|holding|holdings|plc|sa|ag|nv|bv|gmbh|'
    r'international|global|worldwide|enterprises|solutions|services|'
    r'systems|technologies|technology|communications|financial|'
    r'partners|associates|ventures|industries|manufacturing)\b',
    re.IGNORECASE,
)

def norm(s):
    """Normalize a name for fuzzy matching."""
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = s.lower()
    s = re.sub(r'[&/,\.\'\"]+', ' ', s)
    s = CORP_SUFFIXES.sub('', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def fortune_tier(rank):
    if rank <= 100:
        return "Fortune 100"
    if rank <= 500:
        return "Fortune 500"
    return "Fortune 1000"


# ---------------------------------------------------------------------------
# Build lookup: norm(name) -> (rank, tier) from Fortune list
# ---------------------------------------------------------------------------

fortune_lookup = {}
for rank, name in enumerate(FORTUNE_1000, start=1):
    fortune_lookup[norm(name)] = (rank, fortune_tier(rank))


# ---------------------------------------------------------------------------
# Scan all/* and match
# ---------------------------------------------------------------------------

NAME_RE = re.compile(r'^name:\s*(.+?)\s*$', re.MULTILINE)

def slug_to_names(slug):
    """Return a list of candidate normalised names for a slug."""
    candidates = [norm(slug.replace('-', ' '))]
    yml = os.path.join(ALL, slug, 'apis.yml')
    if os.path.isfile(yml):
        try:
            content = open(yml, encoding='utf-8', errors='ignore').read(2048)
            m = NAME_RE.search(content)
            if m:
                candidates.append(norm(m.group(1).strip().strip("'\"")))
        except OSError:
            pass
    return candidates


def find_match(slug):
    """Return (rank, tier) if this slug matches a Fortune 1000 entry."""
    for candidate in slug_to_names(slug):
        if candidate in fortune_lookup:
            return fortune_lookup[candidate]
        # try prefix match (first 2+ tokens)
        tokens = candidate.split()
        if len(tokens) >= 2:
            prefix = ' '.join(tokens[:2])
            if prefix in fortune_lookup:
                return fortune_lookup[prefix]
    return None


# ---------------------------------------------------------------------------
# Update apis.yml — insert or extend top-level tags: block
# ---------------------------------------------------------------------------

TAGS_BLOCK_RE = re.compile(r'^(tags:\s*\n(?:[ \t]+-[^\n]*\n)*)', re.MULTILINE)

def already_tagged(content):
    m = TAGS_BLOCK_RE.search(content)
    if not m:
        return False
    return bool(re.search(r'Fortune', m.group(1)))

def add_fortune_tag(content, tier):
    """Add tier to the existing tags: block, or create one after the first line."""
    tag_line = '  - %s\n' % tier
    m = TAGS_BLOCK_RE.search(content)
    if m:
        # Append to existing block
        block = m.group(1)
        new_block = block + tag_line
        return content[:m.start()] + new_block + content[m.end():]
    else:
        # Insert a new tags: block after the first non-empty line
        lines = content.split('\n')
        insert_after = 0
        for i, line in enumerate(lines):
            if line.strip():
                insert_after = i
                break
        lines.insert(insert_after + 1, 'tags:\n%s' % tag_line.rstrip())
        return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

matched = []
unmatched_sample = []

for slug in sorted(os.listdir(ALL)):
    yml = os.path.join(ALL, slug, 'apis.yml')
    if not os.path.isfile(yml):
        continue
    result = find_match(slug)
    if result:
        rank, tier = result
        try:
            content = open(yml, encoding='utf-8', errors='ignore').read()
        except OSError:
            continue
        if already_tagged(content):
            matched.append((slug, rank, tier, 'already-tagged'))
        else:
            matched.append((slug, rank, tier, 'to-tag'))
            if not DRY_RUN:
                new_content = add_fortune_tag(content, tier)
                with open(yml, 'w', encoding='utf-8') as fh:
                    fh.write(new_content)

matched.sort(key=lambda x: x[1])

to_tag = [(s, r, t) for s, r, t, st in matched if st == 'to-tag']
already = [(s, r, t) for s, r, t, st in matched if st == 'already-tagged']

print('Total matches:  %d' % len(matched))
print('Already tagged: %d' % len(already))
print('To tag:         %d' % len(to_tag))
print()

if DRY_RUN:
    print('DRY RUN — pass --write to apply changes')
    print()
    print('Sample matches to be tagged (first 30):')
    for slug, rank, tier in to_tag[:30]:
        print('  [%3d] %-12s  %s' % (rank, tier, slug))
else:
    print('Tagged %d apis.yml files.' % len(to_tag))
    for slug, rank, tier in to_tag[:30]:
        print('  [%3d] %-12s  %s' % (rank, tier, slug))

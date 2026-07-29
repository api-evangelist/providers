#!/usr/bin/env python3
"""
Build the Industries, Countries, and Australian Banks sections of the
API Evangelist Providers site.

Sources:
  - ../../signals-jobs/_data/industries.yml              : industry taxonomy
                                                           (companies per industry)
  - ../../all/*/apis.yml                                 : top-level tags
                                                           (country + Banks matching)
  - ../../api-search/providers/_providers/<slug>.md      : enriched provider data
                                                           (score.composite, score.band)

Output:
  - _data/sections-industries.json          : card data for /industries/
  - _data/sections-countries.json           : card data for /countries/
  - _data/providers-industry-<slug>.json    : provider list per industry
  - _data/providers-country-<slug>.json     : provider list per country
  - _data/providers-australian-banks.json   : AU banks sorted by rating score
  - industries/index.html + industries/<slug>/index.html
  - countries/index.html + countries/<slug>/index.html
  - australian-banks/index.html

Listings deliberately carry no per-provider links yet — provider detail
pages and apis.io links come later.
"""
import json
import os
import re

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(SITE))
ALL = os.path.join(ROOT, "all")
PROVIDERS = os.path.join(ROOT, "api-search", "providers", "_providers")
INDUSTRIES_YML = os.path.join(ROOT, "signals-jobs", "_data", "industries.yml")
SCORING_YML = os.path.join(ROOT, "api-search", "signals", "_data", "scoring.yml")
DELISTED_YML = os.path.join(ROOT, "api-search", "network", "_data", "delisted.yml")

NAME_RE = re.compile(r"^name:\s*(.+?)\s*$")
DESC_RE = re.compile(r"^description:\s*(.*?)\s*$")
TAGS_RE = re.compile(r"^tags:\n((?:\s*- .+\n)+)", re.MULTILINE)

# Top industrial countries, roughly ordered by manufacturing output. Each maps
# to the tag aliases used across all/* apis.yml files. A provider is filed
# under a country when one of its top-level tags matches an alias exactly.
COUNTRIES = [
    ("china",          "China",          "🇨🇳", ["China"]),
    ("united-states",  "United States",  "🇺🇸", ["United States", "USA", "U.S.", "United States of America"]),
    ("japan",          "Japan",          "🇯🇵", ["Japan"]),
    ("germany",        "Germany",        "🇩🇪", ["Germany"]),
    ("india",          "India",          "🇮🇳", ["India"]),
    ("south-korea",    "South Korea",    "🇰🇷", ["South Korea", "Korea"]),
    ("italy",          "Italy",          "🇮🇹", ["Italy"]),
    ("france",         "France",         "🇫🇷", ["France"]),
    ("united-kingdom", "United Kingdom", "🇬🇧", ["United Kingdom", "UK", "Great Britain", "Britain"]),
    ("brazil",         "Brazil",         "🇧🇷", ["Brazil"]),
    ("mexico",         "Mexico",         "🇲🇽", ["Mexico"]),
    ("indonesia",      "Indonesia",      "🇮🇩", ["Indonesia"]),
    ("canada",         "Canada",         "🇨🇦", ["Canada"]),
    ("russia",         "Russia",         "🇷🇺", ["Russia", "Russian Federation"]),
    ("spain",          "Spain",          "🇪🇸", ["Spain"]),
    ("turkey",         "Turkey",         "🇹🇷", ["Turkey", "Türkiye"]),
    ("taiwan",         "Taiwan",         "🇹🇼", ["Taiwan"]),
    ("switzerland",    "Switzerland",    "🇨🇭", ["Switzerland"]),
    ("netherlands",    "Netherlands",    "🇳🇱", ["Netherlands"]),
    ("australia",      "Australia",      "🇦🇺", ["Australia"]),
    ("saudi-arabia",   "Saudi Arabia",   "🇸🇦", ["Saudi Arabia"]),
    ("poland",         "Poland",         "🇵🇱", ["Poland"]),
    ("sweden",         "Sweden",         "🇸🇪", ["Sweden"]),
    ("ireland",        "Ireland",        "🇮🇪", ["Ireland"]),
    ("singapore",      "Singapore",      "🇸🇬", ["Singapore"]),
    ("finland",        "Finland",        "🇫🇮", ["Finland"]),
    ("norway",         "Norway",         "🇳🇴", ["Norway"]),
]

# Material symbol per industry slug; anything unlisted gets `domain`.
INDUSTRY_ICONS = {
    "aerospace": "flight", "agriculture": "agriculture", "automotive": "directions_car",
    "cannabis": "spa", "cloud-data-platform": "cloud", "cpaas": "forum",
    "communications-platform-as-a-service-cpaas": "forum", "construction": "construction",
    "consumer-goods": "shopping_basket", "cruise-lines": "directions_boat",
    "customer-relationship-management-crm": "support_agent", "cybersecurity": "security",
    "defense": "shield", "e-commerce-platform": "shopping_cart", "energy": "bolt",
    "enterprise-software": "business_center", "entertainment": "theaters",
    "environmental-services": "recycling", "event-management-software": "event",
    "financial-services": "account_balance", "financial-technology": "payments",
    "fitness-wellness": "fitness_center", "food-delivery": "delivery_dining",
    "food-service": "restaurant", "gaming": "sports_esports", "healthcare": "medical_services",
    "hospitality": "hotel", "human-capital-management": "groups", "industrial": "factory",
    "insurance": "verified_user", "life-sciences": "biotech", "logistics": "local_shipping",
    "maritime": "anchor", "media": "newspaper", "mining": "landslide", "pet-care": "pets",
    "pharmaceutical": "medication", "productivity-software": "task_alt",
    "professional-services": "work", "rail": "train", "real-estate": "home_work",
    "retail": "storefront", "sports": "sports_soccer", "tax-compliance-software": "receipt_long",
    "technology": "memory", "telecommunications": "cell_tower", "transportation": "commute",
    "travel-technology": "travel", "utilities": "water_drop", "video-streaming": "smart_display",
    "waste-management": "delete",
}

# Industries derived from the catalog itself rather than from the jobs taxonomy
# in industries.yml. A provider joins one of these when any of its top-level
# apis.yml tags matches an alias below (case-insensitive, exact match on the
# whole tag). Providers can belong to several — these are lenses, not buckets.
#
# Where a slug already exists in the jobs taxonomy the two memberships are
# unioned and the definition here wins for name/description/icon, which is how
# thin taxonomy pages (Cybersecurity had 9 companies against 1,500+ security
# providers in the catalog) get filled out.
TAG_INDUSTRIES = [
    # --- Tier 1 -----------------------------------------------------------
    {
        "slug": "artificial-intelligence",
        "name": "Artificial Intelligence",
        "icon": "smart_toy",
        "description": "Model providers, agent frameworks, inference platforms, and the applied AI companies putting them to work behind an API.",
        "tags": [
            "artificial intelligence", "ai", "ai ml", "machine learning", "deep learning",
            "reinforcement learning", "ai agents", "agents", "agentic ai", "agentic commerce",
            "agent commerce", "llm", "large language models", "generative ai", "foundation models",
            "computer vision", "natural language processing", "nlp", "conversational ai",
            "voice ai", "speech recognition", "text to speech", "image generation",
            "video generation", "multimodal", "embeddings", "rag", "inference", "mlops",
            "ai infrastructure", "enterprise ai", "ai apps", "edge ai", "physical ai",
            "ai governance", "ai security", "chatbots", "code generation", "data science",
            # Deliberately not `mcp` / `model context protocol`: shipping an MCP
            # server is an agent-readiness signal on any provider, not evidence
            # that AI is the business.
        ],
    },
    {
        "slug": "developer-tools",
        "name": "Developer Tools & DevOps",
        "icon": "terminal",
        "description": "The companies developers build on — SDKs and CLIs, CI/CD, containers, observability, API gateways, and the platforms that run it all.",
        "tags": [
            "developer tools", "developer platform", "developer experience", "devops", "devsecops",
            "ci/cd", "kubernetes", "containers", "cloud native", "observability", "monitoring",
            "aiops", "telemetry", "incident management", "incident response", "serverless",
            "microservices", "infrastructure as code", "orchestration", "deployment",
            "edge computing", "api gateway", "api management", "api design", "api testing",
            "api security", "sdk", "sdks", "cli", "software development", "testing",
            "quality assurance", "low-code", "no-code", "version control", "repository",
            "distributed systems", "multi-cloud",
        ],
    },
    {
        "slug": "data-analytics",
        "name": "Data & Analytics",
        "icon": "insights",
        "description": "Warehouses, catalogs, pipelines, and the analytics and business-intelligence layers companies expose as APIs.",
        "tags": [
            "analytics", "data analytics", "big data", "business intelligence",
            "data catalog", "data integration", "data aggregation", "data engineering",
            "data pipelines", "data platform", "data warehouse", "data management",
            "data governance", "data quality", "data enrichment", "data extraction",
            "data visualization", "data science", "database", "sql", "etl", "dashboards",
            "reporting", "predictive analytics", "market intelligence", "metadata", "datasets",
            "time series", "real-time data", "knowledge graph", "web scraping", "statistics",
        ],
    },
    {
        "slug": "cybersecurity",
        "name": "Cybersecurity & Identity",
        "icon": "security",
        "description": "Security and identity providers — authentication and authorization, threat detection, application and cloud security, fraud, and privacy.",
        "tags": [
            "security", "cybersecurity", "application security", "cloud security",
            "network security", "endpoint security", "data security", "api security",
            "zero trust", "threat detection", "threat intelligence", "vulnerability management",
            "security operations", "siem", "incident response", "identity",
            "identity verification", "authentication", "authorization", "access control",
            "openid connect", "oauth", "sso", "scim", "biometrics", "encryption",
            "cryptography", "privacy", "data protection", "fraud detection",
            "fraud prevention", "kyc", "kyb", "aml",
        ],
    },
    {
        "slug": "digital-health",
        "name": "Digital Health & Telehealth",
        "icon": "monitor_heart",
        "description": "Care delivered and coordinated through software — telehealth, EHR interoperability, patient engagement, remote monitoring, and behavioral health.",
        "tags": [
            "digital health", "health tech", "healthtech", "telehealth", "telemedicine",
            "virtual care", "remote patient monitoring", "patient engagement",
            "care coordination", "value-based care", "primary care", "mental health",
            "behavioral health", "consumer health", "women's health", "health data",
            "health it", "ehr", "ehr integration", "electronic health records", "fhir", "hl7",
            "interoperability", "hipaa", "medical imaging", "diagnostics", "medical devices",
            "medtech", "practice management", "revenue cycle management", "wearables",
            "pharmacy", "dental", "veterinary", "nutrition",
        ],
    },
    {
        "slug": "blockchain-crypto",
        "name": "Blockchain, Crypto & Web3",
        "icon": "currency_bitcoin",
        "description": "Chains, exchanges, wallets, and the on-chain data and settlement infrastructure the digital-asset economy runs on.",
        "tags": [
            "blockchain", "web3", "crypto web3", "cryptocurrency", "crypto", "defi", "bitcoin",
            "ethereum", "solana", "evm", "smart contracts", "nft", "digital assets", "tokens",
            "tokenization", "stablecoins", "stablecoin", "staking", "wallet", "wallets",
            "digital wallet", "decentralized", "exchange", "liquidity",
        ],
    },
    # --- Tier 2 -----------------------------------------------------------
    {
        "slug": "government",
        "name": "Government & Public Sector",
        "icon": "account_balance",
        "description": "Federal, state, and municipal agencies plus the open-data portals, GovTech vendors, and public-safety systems serving them.",
        "tags": [
            "government", "federal government", "state government", "local government",
            "municipal", "public sector", "govtech", "civic", "government data",
            "open data portal", "ckan", "dcat", "public safety", "national security",
            "census", "smart city",
            # Not bare `open data`: it tags open datasets of every kind
            # (Wikidata, OpenStreetMap, card games), not public-sector data.
        ],
    },
    {
        "slug": "creator-economy",
        "name": "Music, Audio & Creator Economy",
        "icon": "graphic_eq",
        "description": "Music and audio platforms, podcasting, publishing, social, and the tools creators use to make and monetize what they publish.",
        "tags": [
            "music", "audio", "podcast", "podcasts", "creator economy", "creators",
            "content creation", "publishing", "books", "social media",
            "influencer marketing", "live streaming", "broadcasting", "photography",
            # Not `content` / `community` / `social` / `video` / `monetization`:
            # each is generic platform vocabulary that pulls in CPaaS, CRM, and
            # market-data providers that have nothing to do with creators.
        ],
    },
    {
        "slug": "venture-capital",
        "name": "Venture Capital & Investing",
        "icon": "trending_up",
        "description": "The firms allocating capital and the platforms moving it — venture and private equity, brokerages, trading, market data, and wealth management.",
        "tags": [
            "venture capital", "private equity", "growth equity", "investing", "investment",
            "investment management", "asset management", "wealth management",
            "portfolio management", "trading", "brokerage", "broker", "stocks", "options",
            "derivatives", "capital markets", "market data", "financial data", "hedge fund",
            "family office", "crowdfunding", "startups", "venture backed",
        ],
    },
    {
        "slug": "telecommunications",
        "name": "Telecommunications & Connectivity",
        "icon": "cell_tower",
        "description": "Carriers, network operators, and the messaging, voice, and connectivity platforms built on top of them.",
        "tags": [
            "telecommunications", "telecom", "telephony", "networking", "connectivity",
            "wireless", "broadband", "5g", "isp", "network apis", "cpaas", "sms", "messaging",
            "whatsapp", "voice", "communications", "contact center", "video conferencing",
            "webrtc", "chat", "satellite communications", "dns", "cdn",
        ],
    },
    {
        "slug": "education",
        "name": "Education & EdTech",
        "icon": "school",
        "description": "Universities, school systems, and the learning platforms, credentialing, and research infrastructure around them.",
        "tags": [
            "education", "edtech", "higher education", "university", "universities", "k-12",
            "e-learning", "online learning", "learning", "lms", "students", "academic",
            "research", "research data", "institutional repository", "open access", "library",
            "libraries", "training", "coaching", "curriculum", "credentials",
        ],
    },
    {
        "slug": "legal-compliance",
        "name": "Legal & Compliance Tech",
        "icon": "gavel",
        "description": "Legal software and the compliance, RegTech, and risk platforms companies use to stay inside the rules.",
        "tags": [
            "legal", "legal tech", "legaltech", "law", "contracts", "contract management",
            "compliance", "regtech", "risk management",
            "document automation", "document management", "e-signature", "esignature",
            # Not `governance` / `audit` / `risk`: in this catalog those mostly
            # mean API governance and security posture, not legal work.
            "intellectual property", "patents", "litigation",
        ],
    },
    {
        "slug": "supply-chain",
        "name": "Supply Chain & Procurement",
        "icon": "inventory_2",
        "description": "Sourcing, procurement, freight, warehousing, and the inventory and fulfillment systems that move goods.",
        "tags": [
            "supply chain", "procurement", "sourcing", "wholesale", "distribution", "freight",
            "trucking", "shipping", "fulfillment", "warehousing", "inventory",
            "inventory management", "order management", "orders", "edi", "customs",
            "cross-border", "tracking", "3pl",
        ],
    },
    {
        "slug": "biotechnology",
        "name": "Biotechnology & Drug Discovery",
        "icon": "biotech",
        "description": "Drug discovery and development, genomics, clinical research, and the computational biology behind modern therapeutics.",
        "tags": [
            "biotechnology", "biotech", "biopharmaceutical", "drug discovery",
            "drug development", "therapeutics", "clinical trials", "clinical research",
            "clinical stage", "genomics", "bioinformatics", "proteomics", "synthetic biology",
            "cell therapy", "gene therapy", "immunotherapy", "immunology", "oncology",
            "neuroscience", "precision medicine", "molecular biology", "crispr",
        ],
    },
    {
        "slug": "robotics",
        "name": "Robotics & Autonomous Systems",
        "icon": "precision_manufacturing",
        "description": "Robots, drones, autonomous vehicles, and the perception and control stacks that let machines act on their own.",
        "tags": [
            "robotics", "robots", "autonomous systems", "autonomous vehicles", "autonomy",
            "self-driving", "drones", "uav", "industrial automation", "automation",
            "warehouse automation", "simulation", "teleoperation", "humanoid",
        ],
    },
    {
        "slug": "marketing-advertising",
        "name": "Marketing & Advertising",
        "icon": "campaign",
        "description": "AdTech and MarTech — campaigns, attribution, customer data, personalization, and the demand-generation stack.",
        "tags": [
            "marketing", "marketing automation", "martech", "advertising", "adtech",
            "programmatic", "attribution", "campaigns", "email marketing", "seo",
            "lead generation", "personalization", "customer data platform",
            "customer engagement", "customer experience", "loyalty", "rewards", "surveys",
            "sales enablement", "sales intelligence", "growth",
        ],
    },
    # --- Tier 3 -----------------------------------------------------------
    {
        "slug": "semiconductors-hardware",
        "name": "Semiconductors & Hardware",
        "icon": "memory",
        "description": "Chips, compute, consumer electronics, and the data-center hardware everything else is built on.",
        "tags": [
            "semiconductors", "semiconductor", "chips", "hardware", "consumer hardware",
            "consumer electronics", "electronics", "compute", "gpu", "quantum computing",
            "data center", "data centers", "cloud computing", "storage", "3d printing",
            "cad", "materials science",
        ],
    },
    {
        "slug": "climate-sustainability",
        "name": "Climate & Sustainability",
        "icon": "eco",
        "description": "Climate tech, clean energy, carbon accounting, and the ESG and circular-economy data companies now report against.",
        "tags": [
            "climate", "climate tech", "cleantech", "clean energy", "renewable energy", "solar",
            "wind", "energy storage", "carbon", "carbon accounting", "decarbonization",
            "emissions", "esg", "sustainability", "circular economy", "recycling",
            "environment", "climate data", "earth observation", "remote sensing",
        ],
    },
    {
        "slug": "banking",
        "name": "Banking & Open Banking",
        "icon": "savings",
        "description": "Banks, credit unions, neobanks, and the open-banking and banking-as-a-service rails that connect to them.",
        "tags": [
            "banking", "banks", "bank", "consumer banking", "commercial banking",
            "open banking", "open finance", "banking as a service", "neobank",
            "core banking", "credit union", "account information", "psd2", "obie", "cdr",
            "savings", "credit", "deposits", "treasury",
        ],
    },
    {
        "slug": "human-capital-management",
        "name": "Human Resources & Payroll",
        "icon": "groups",
        "description": "Hiring, payroll, benefits, and the workforce systems of record companies run their people on.",
        "tags": [
            "human resources", "hr", "hr tech", "hris", "human capital management", "payroll",
            "benefits", "employee benefits", "recruiting", "recruitment", "hiring",
            "talent", "talent acquisition", "staffing", "jobs", "workforce",
            "workforce management", "time tracking", "gig economy", "employer of record",
        ],
    },
    {
        "slug": "iot",
        "name": "IoT & Connected Devices",
        "icon": "sensors",
        "description": "Sensors, telematics, smart home and industrial IoT — the physical world reporting in over an API.",
        "tags": [
            "iot", "internet of things", "industrial iot", "sensors", "telematics",
            "smart home", "connected devices", "device management", "embedded",
            "wearables", "edge computing", "asset tracking", "smart building",
        ],
    },
    {
        "slug": "gaming",
        "name": "Gaming & Interactive",
        "icon": "sports_esports",
        "description": "Game studios and the engines, multiplayer backends, and immersive platforms behind interactive entertainment.",
        "tags": [
            "gaming", "games", "video games", "mobile games", "game development",
            "game studio", "esports", "multiplayer", "virtual reality", "augmented reality",
            "metaverse", "3d", "games and comics", "game engine",
        ],
    },
    {
        "slug": "weather-geospatial",
        "name": "Weather & Geospatial",
        "icon": "public",
        "description": "Weather, mapping, geocoding, and the satellite and location data feeding everything from logistics to insurance.",
        "tags": [
            "weather", "geospatial", "gis", "mapping", "maps", "geocoding", "location",
            "satellite imagery", "remote sensing", "earth observation", "navigation",
            "cartography", "elevation", "air quality",
        ],
    },
    {
        "slug": "mobility",
        "name": "Mobility & Fleet",
        "icon": "directions_car",
        "description": "Ride-hailing, micromobility, fleet management, EV charging, and the telematics layer under moving vehicles.",
        "tags": [
            "mobility", "fleet management", "fleet", "electric vehicles", "ev charging",
            "ride sharing", "ridesharing", "micromobility", "car sharing", "parking",
            "last mile", "delivery", "on-demand", "telematics",
        ],
    },
    {
        "slug": "space",
        "name": "Space & Satellite",
        "icon": "rocket_launch",
        "description": "Launch, satellites, ground segment, and the earth-observation and aviation data coming down from above.",
        "tags": [
            "space", "space technology", "satellite", "satellites", "launch", "spacecraft",
            "earth observation", "remote sensing", "aviation", "orbital", "ground station",
            "space situational awareness",
        ],
    },
]

RAW_BASE = "https://raw.githubusercontent.com/api-evangelist/%s/refs/heads/main/screenshots/%s"

BAND_LABELS = {
    "exemplar": "Exemplar", "strong": "Strong", "developing": "Developing",
    "thin": "Thin", "emerging": "Emerging", "minimal": "Minimal",
}

# Most providers a rated listing renders. Each row carries a full Kin Score panel
# (every facet, every agent-readiness dimension), which costs ~12KB of HTML — fine
# at 137 providers, not at 4,910: the Artificial Intelligence page shipped at 62MB
# before this cap. Band headers keep their true counts; only the rendered rows are
# cut, top-down by Kin Score, and both listing and band say so.
LISTING_LIMIT = 1000


def delisted_slugs():
    """Slugs a company has asked us to remove — never list these, ever.

    See network/_data/delisted.yml, the network-wide takedown registry. A
    delisted provider keeps a bare repo under all/<slug>/, so any scan of
    all/* must exclude it explicitly rather than rely on which artifacts the
    takedown happened to delete.
    """
    if not os.path.isfile(DELISTED_YML):
        print("WARNING: %s not found — delisting guard is INACTIVE" % DELISTED_YML)
        return set()
    with open(DELISTED_YML, "r", encoding="utf-8") as fh:
        doc = yaml.safe_load(fh) or []
    rows = doc if isinstance(doc, list) else doc.get("delisted", doc.get("providers", []))
    return {r["slug"] for r in rows if isinstance(r, dict) and r.get("slug")}


def slugify(name):
    s = name.lower()
    s = re.sub(r"\(([^)]*)\)", r" \1 ", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


_SCREENSHOTS = {}


def newest_screenshot(slug):
    if slug in _SCREENSHOTS:
        return _SCREENSHOTS[slug]
    _SCREENSHOTS[slug] = None
    shots = os.path.join(ALL, slug, "screenshots")
    if not os.path.isdir(shots):
        return None
    fname = None
    idx = os.path.join(shots, "index.json")
    if os.path.isfile(idx):
        try:
            with open(idx, "r", encoding="utf-8", errors="ignore") as fh:
                entries = json.load(fh)
            files = [e.get("file") for e in entries if e.get("file")]
            if files:
                fname = sorted(files)[-1]
        except (OSError, ValueError):
            fname = None
    if not fname:
        pngs = [f for f in os.listdir(shots) if f.lower().endswith(".png")]
        if pngs:
            fname = sorted(pngs)[-1]
    if not fname:
        return None
    _SCREENSHOTS[slug] = RAW_BASE % (slug, fname)
    return _SCREENSHOTS[slug]


def titleize(slug):
    parts = slug.replace("_", "-").split("-")
    return " ".join(p[:1].upper() + p[1:] if p else p for p in parts)


def _top_level_scalar(content, key):
    """Value of a top-level scalar key in a YAML document, parsed properly.

    apis.yml files are large and there are ~25k of them, so full-document
    yaml.safe_load per provider is too slow for this build. Instead slice out
    just this key's block — its own line plus every indented/blank line that
    follows — and hand that snippet to the YAML parser. That gets every scalar
    style right: plain, single/double quoted (including quoted text that wraps
    over several lines), folded `>-`, and literal `|`.

    The old hand-rolled reader took only the first physical line, which turned
    every re-serialized quoted description into a fragment with a dangling
    quote — 8,849 of them across the catalog.
    """
    lines = content.splitlines(keepends=True)
    start = None
    for i, line in enumerate(lines):
        if line.startswith(key + ":"):
            start = i
            break
    if start is None:
        return None
    block = [lines[start]]
    for line in lines[start + 1:]:
        if line.strip() and line[0] not in " \t":
            break
        block.append(line)
    try:
        parsed = yaml.safe_load("".join(block))
    except yaml.YAMLError:
        return None
    if not isinstance(parsed, dict):
        return None
    val = parsed.get(key)
    if val is None or isinstance(val, (dict, list)):
        return None
    return str(val).strip()


def read_apis_yml(slug):
    """Return (name, description, tags) from the top-level of all/<slug>/apis.yml,
    or None if the repo has no apis.yml."""
    apis_yml = os.path.join(ALL, slug, "apis.yml")
    if not os.path.isfile(apis_yml):
        return None
    try:
        with open(apis_yml, "r", encoding="utf-8", errors="ignore") as fh:
            content = fh.read()
    except OSError:
        return None
    tags = []
    m = TAGS_RE.search(content)
    if m:
        tags = [t.strip() for t in re.findall(r"-\s*(.+)", m.group(1))]
    name = _top_level_scalar(content, "name") or titleize(slug)
    if name.lower() in ("null", "~"):
        name = titleize(slug)
    description = " ".join((_top_level_scalar(content, "description") or "").split())
    return name, description, tags


def read_scores():
    """Read {slug: {composite, band}} from enriched provider frontmatter."""
    scores = {}
    if not os.path.isdir(PROVIDERS):
        return scores
    sc_re = re.compile(r"^score:\n\s{2}composite:\s*([\d.]+)\n\s{2}band:\s*(\S+)", re.MULTILINE)
    for fname in os.listdir(PROVIDERS):
        if not fname.endswith(".md"):
            continue
        try:
            with open(os.path.join(PROVIDERS, fname), "r", encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
        except OSError:
            continue
        m = sc_re.search(content)
        if m:
            scores[fname[:-3]] = {"composite": float(m.group(1)), "band": m.group(2)}
    return scores


# Matches a top-level frontmatter block (`score:` / `agent_readiness:`) plus
# all following indented lines — same shape signals/score.rb writes.
def _fm_block(content, key):
    m = re.search(r"^%s:\n((?:[ \t]+.*\n|\n)*)" % key, content, re.MULTILINE)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(0)).get(key)
    except yaml.YAMLError:
        return None


_SCORE_DETAILS = {}


def read_score_details(slug):
    """Full score + agent_readiness blocks for one provider, or None.

    Cached: providers now appear on several industry listings each, and this
    parses YAML out of a file on every call.
    """
    if slug in _SCORE_DETAILS:
        return _SCORE_DETAILS[slug]
    _SCORE_DETAILS[slug] = None
    path = os.path.join(PROVIDERS, slug + ".md")
    if not os.path.isfile(path):
        return None
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            content = fh.read()
    except OSError:
        return None
    _SCORE_DETAILS[slug] = {
        "score": _fm_block(content, "score"),
        "agent": _fm_block(content, "agent_readiness"),
    }
    return _SCORE_DETAILS[slug]


def entry_for(slug, meta, scores):
    name, description, _tags = meta
    entry = {"name": name, "slug": slug}
    if description:
        entry["description"] = description
    shot = newest_screenshot(slug)
    if shot:
        entry["screenshot"] = shot
    sc = scores.get(slug)
    if sc:
        entry["score"] = sc["composite"]
        entry["band"] = sc["band"]
        entry["band_label"] = BAND_LABELS.get(sc["band"], sc["band"].title())
    return entry


# ---------------------------------------------------------------------------
# Page templates
# ---------------------------------------------------------------------------

def cards_page(title, summary, cards_key, base_path, intro):
    return "\n".join([
        "---",
        "layout: default",
        "section: Providers",
        'title: "%s"' % title,
        'summary: "%s"' % summary,
        "nav: Providers",
        'cards_key: "%s"' % cards_key,
        'cards_base: "%s"' % base_path,
        'intro: "%s"' % intro,
        "---",
        "{% include section-cards.html %}",
        "",
    ])


def listing_page(title, summary, data_key, rated=False, paper=None):
    include = "company-listing-rated.html" if rated else "company-listing-plain.html"
    lines = [
        "---",
        "layout: default",
        "section: Providers",
        'title: "%s"' % title,
        'summary: "%s"' % summary,
        "nav: Providers",
        'data_key: "%s"' % data_key,
    ]
    body = []
    # Optional sector-report promo band (see _includes/paper-promo.html). Emitted
    # here so it survives every rebuild rather than being hand-added to the page.
    if paper:
        lines += [
            "paper:",
            "  slug: %s" % paper["slug"],
            '  title: "%s"' % paper["title"],
            '  blurb: "%s"' % paper["blurb"].replace('"', "'"),
            '  price: "%s"' % paper.get("price", "500"),
        ]
        body.append("{% include paper-promo.html %}")
    lines.append("---")
    body.append("{%% include %s %%}" % include)
    return "\n".join(lines + body + [""])


def write_page(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)


def esc(text):
    return text.replace('"', "'")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    data_dir = os.path.join(SITE, "_data")
    os.makedirs(data_dir, exist_ok=True)
    scores = read_scores()

    # Mirror the rating rubric so the listing's rating panels can render the
    # exact same facet/dimension layout as apis.io provider detail pages.
    if os.path.isfile(SCORING_YML):
        with open(SCORING_YML, "r", encoding="utf-8") as fh:
            rubric_raw = fh.read()
        with open(os.path.join(data_dir, "scoring.yml"), "w", encoding="utf-8") as fh:
            fh.write("# Mirrored from api-search/signals/_data/scoring.yml by build-sections.py — do not edit here.\n")
            fh.write(rubric_raw)

    apis_cache = {}

    delisted = delisted_slugs()

    def meta_of(slug):
        if slug in delisted:
            return None
        if slug not in apis_cache:
            apis_cache[slug] = read_apis_yml(slug)
        return apis_cache[slug]

    # --- Rated entry + band grouping --------------------------------------
    # Shared by every listing (industries, countries, banks, market data) so
    # they all render the same Kin Score band-grouped layout via
    # _includes/company-listing-rated.html.

    def rated_entry(slug, meta):
        entry = entry_for(slug, meta, scores)
        details = read_score_details(slug)
        if details:
            sc = details.get("score") or {}
            if sc.get("facets"):
                entry["facets"] = sc["facets"]
            if sc.get("scored_at"):
                entry["scored_at"] = str(sc["scored_at"])
            if sc.get("schema_version") is not None:
                entry["schema_version"] = sc["schema_version"]
            if sc.get("regulatory"):
                entry["regulatory"] = sc["regulatory"]
            ag = details.get("agent") or {}
            if ag.get("score") is not None:
                entry["agent_score"] = ag["score"]
                entry["agent_band"] = ag.get("band", "")
                entry["agent_dims"] = ag.get("dimensions", {})
        return entry

    def band_grouped(entries):
        # Rating sort: scored providers by composite descending; unscored last,
        # alphabetically (unscored is "not yet rated", not a zero).
        entries.sort(key=lambda e: (-e.get("score", -1), e["name"].lower()))
        for rank, e in enumerate(entries, 1):
            e["rank"] = rank
        # Group by composite band, same ladder as apis.io/providers/. Only bands
        # with at least one member are emitted; the top two present open by default.
        band_ladder = [
            ("exemplar",   "Exemplar",   "70+",     "Reference-quality API operations across every facet."),
            ("strong",     "Strong",     "60–69.9", "Solid contracts, transparent operations, and an easy start."),
            ("developing", "Developing", "45–59.9", "Real signal across most facets with visible, nameable gaps."),
            ("thin",       "Thin",       "30–44.9", "Limited machine-readable signal beyond documentation a human can read."),
            ("emerging",   "Emerging",   "15–29.9", "More than an index entry but still mostly links rather than artifacts."),
            ("minimal",    "Minimal",    "0–14.9",  "Index entry only; little beyond a description and a link."),
            ("unrated",    "Not Yet Rated", "",     "Providers we have not scored yet — unknown, not zero."),
        ]
        groups = []
        for band, label, band_range, blurb in band_ladder:
            members = [e for e in entries if e.get("band", "unrated") == band or (band == "unrated" and "band" not in e)]
            if not members:
                continue
            # `count` is what the band really holds; `companies` is what the page
            # renders. They differ only past LISTING_LIMIT, and the band says so.
            shown = [e for e in members if e["rank"] <= LISTING_LIMIT]
            groups.append({
                "band": band, "label": label, "range": band_range, "blurb": blurb,
                "count": len(members), "shown": len(shown), "providers": shown,
            })
        for g in groups[:2]:
            g["open"] = True
        return {
            "total": len(entries),
            "shown": min(len(entries), LISTING_LIMIT),
            "limit": LISTING_LIMIT,
            "bands": groups,
        }

    # --- Industries -------------------------------------------------------
    # Two sources, unioned by slug: the jobs taxonomy in industries.yml (which
    # only knows the ~2k companies with job-posting signal) and the tag clusters
    # in TAG_INDUSTRIES, matched against every all/* repo's top-level tags.
    with open(INDUSTRIES_YML, "r", encoding="utf-8") as fh:
        taxonomy = yaml.safe_load(fh)

    industries = {}   # slug -> {name, description, icon, providers:set}
    order = []        # slug order of first definition

    def industry(slug, name, description, icon):
        if slug not in industries:
            industries[slug] = {
                "name": name, "description": description,
                "icon": icon, "providers": set(),
            }
            order.append(slug)
        return industries[slug]

    for ind in taxonomy:
        ind_slug = slugify(ind["name"])
        rec = industry(
            ind_slug, ind["name"], ind.get("description", ""),
            INDUSTRY_ICONS.get(ind_slug, "domain"),
        )
        for sub in ind.get("industries") or []:
            rec["providers"].update(sub.get("companies") or [])

    # Tag clusters. A definition here overrides the taxonomy's name, blurb, and
    # icon for a shared slug — the catalog-derived framing is the better one —
    # while the membership sets are unioned.
    # Published so apis.io's network/scripts/build_industries.py can file its
    # catalog under the exact same industries from the exact same tag aliases.
    # The two sites are meant to list identical industries — this file is the
    # one place the definitions live.
    with open(os.path.join(data_dir, "tag-industries.yml"), "w", encoding="utf-8") as fh:
        fh.write(
            "# Auto-generated by scripts/build-sections.py — do not hand-edit.\n"
            "# Edit TAG_INDUSTRIES in that script; this is the published copy that\n"
            "# apis.io (api-search/network/scripts/build_industries.py) reads so both\n"
            "# sites derive the same industries from the same provider tags.\n"
        )
        yaml.safe_dump(TAG_INDUSTRIES, fh, sort_keys=False, allow_unicode=True, width=10000)

    tag_to_slugs = {}
    for spec in TAG_INDUSTRIES:
        rec = industry(spec["slug"], spec["name"], spec["description"], spec["icon"])
        rec.update({"name": spec["name"], "description": spec["description"], "icon": spec["icon"]})
        for tag in spec["tags"]:
            tag_to_slugs.setdefault(tag, set()).add(spec["slug"])

    for repo in sorted(os.listdir(ALL), key=str.lower):
        if not os.path.isdir(os.path.join(ALL, repo)):
            continue
        meta = meta_of(repo)
        if meta is None:
            continue
        for t in meta[2]:
            for slug in tag_to_slugs.get(t.strip().lower(), ()):
                industries[slug]["providers"].add(repo)

    industry_cards = []
    for ind_slug in order:
        rec = industries[ind_slug]
        entries = []
        for c in sorted(rec["providers"]):
            meta = meta_of(c)
            if meta is None:
                continue
            entries.append(rated_entry(c, meta))
        grouped = band_grouped(entries)
        with open(os.path.join(data_dir, "providers-industry-%s.json" % ind_slug), "w", encoding="utf-8") as fh:
            json.dump(grouped, fh, ensure_ascii=False, indent=1)
        industry_cards.append({
            "slug": ind_slug,
            "name": rec["name"],
            "description": rec["description"],
            "icon": rec["icon"],
            "count": len(entries),
        })
        write_page(
            os.path.join(SITE, "industries", ind_slug, "index.html"),
            listing_page(
                esc(rec["name"]),
                esc("%s providers in the %s industry, ranked by their Kin Score." % (len(entries), rec["name"])),
                "providers-industry-%s" % ind_slug,
                rated=True,
            ),
        )
    industry_cards.sort(key=lambda c: c["name"].lower())
    with open(os.path.join(data_dir, "sections-industries.json"), "w", encoding="utf-8") as fh:
        json.dump(industry_cards, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "industries", "index.html"),
        cards_page(
            "Industries",
            "Browse API providers by the industries they operate in.",
            "sections-industries",
            "/industries/",
            "Providers across the API Evangelist network organized by the %d industries tracked as part of ongoing industry research." % len(industry_cards),
        ),
    )

    # --- Countries --------------------------------------------------------
    alias_to_country = {}
    for slug, name, flag, aliases in COUNTRIES:
        for a in aliases:
            alias_to_country[a] = slug
    country_entries = {slug: [] for slug, _, _, _ in COUNTRIES}

    for repo in sorted(os.listdir(ALL), key=str.lower):
        if not os.path.isdir(os.path.join(ALL, repo)):
            continue
        meta = meta_of(repo)
        if meta is None:
            continue
        hit = set()
        for t in meta[2]:
            c = alias_to_country.get(t)
            if c and c not in hit:
                hit.add(c)
                country_entries[c].append(rated_entry(repo, meta))

    country_cards = []
    for slug, name, flag, _aliases in COUNTRIES:
        entries = country_entries[slug]
        grouped = band_grouped(entries)
        with open(os.path.join(data_dir, "providers-country-%s.json" % slug), "w", encoding="utf-8") as fh:
            json.dump(grouped, fh, ensure_ascii=False, indent=1)
        country_cards.append({
            "slug": slug,
            "name": name,
            "flag": flag,
            "count": len(entries),
        })
        write_page(
            os.path.join(SITE, "countries", slug, "index.html"),
            listing_page(
                name,
                esc("%s providers operating in %s, ranked by their Kin Score." % (len(entries), name)),
                "providers-country-%s" % slug,
                rated=True,
            ),
        )
    country_cards.sort(key=lambda c: -c["count"])
    with open(os.path.join(data_dir, "sections-countries.json"), "w", encoding="utf-8") as fh:
        json.dump(country_cards, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "countries", "index.html"),
        cards_page(
            "Countries",
            "Browse API providers across the top industrial countries in the world.",
            "sections-countries",
            "/countries/",
            "Providers across the API Evangelist network organized by the top industrial countries, matched using the country tags providers carry.",
        ),
    )

    # --- Rated listings (Australian Banks, Market Data) -------------------

    # --- Australian Banks -------------------------------------------------
    au_banks = []
    for repo in sorted(os.listdir(ALL), key=str.lower):
        meta = meta_of(repo)
        if meta is None:
            continue
        tags = set(meta[2])
        if "Australia" in tags and "Banks" in tags:
            au_banks.append(rated_entry(repo, meta))
    au_banks_grouped = band_grouped(au_banks)
    with open(os.path.join(data_dir, "providers-australian-banks.json"), "w", encoding="utf-8") as fh:
        json.dump(au_banks_grouped, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "australian-banks", "index.html"),
        listing_page(
            "Australian Banks",
            "Australian banks ranked by their Kin Score.",
            "providers-australian-banks",
            rated=True,
            paper={
                "slug": "state-of-australian-banking-apis",
                "title": "The State of Australian Banking APIs",
                "blurb": "Fifty Consumer Data Right banks scored — and not one breaks 51. The anatomy of a mandated-but-mediocre ecosystem: uniform resources, the Kin Score facet-by-facet, the agent-readiness paradox, the FAPI/consent posture, provider-by-provider intelligence, and the investable thesis.",
                "price": "500",
            },
        ),
    )

    # --- Market Data ------------------------------------------------------
    # Roster-driven (not tag-matched): the curated market data vendor list
    # lives in all/0-working/market-data-roster.json with a tier per provider.
    MD_TIER_LABELS = {
        "enterprise-platform":  "Enterprise Platform",
        "exchange-data":        "Exchange Data Arm",
        "feed-infrastructure":  "Feed & Infrastructure",
        "developer-first":      "Developer-First",
        "crypto":               "Crypto Market Data",
    }
    market_data = []
    roster_path = os.path.join(ALL, "0-working", "market-data-roster.json")
    with open(roster_path, "r", encoding="utf-8") as fh:
        roster = json.load(fh)
    for p in roster["providers"]:
        meta = meta_of(p["slug"])
        if meta is None:
            continue
        entry = rated_entry(p["slug"], meta)
        tier = p.get("tier", "")
        if tier:
            entry["tier"] = MD_TIER_LABELS.get(tier, titleize(tier))
        market_data.append(entry)
    market_data_grouped = band_grouped(market_data)
    with open(os.path.join(data_dir, "providers-market-data.json"), "w", encoding="utf-8") as fh:
        json.dump(market_data_grouped, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "market-data", "index.html"),
        listing_page(
            "Market Data",
            "Financial market data providers ranked by their Kin Score, from terminal and feed incumbents to API-first challengers.",
            "providers-market-data",
            rated=True,
            paper={
                "slug": "state-of-market-data-apis",
                "title": "The State of Market Data APIs",
                "blurb": "Fifty-eight providers scored. The feed is the commodity, the operation is the moat — the resource taxonomy, the Kin Score facet-by-facet, agent-readiness, security posture, provider-by-provider intelligence, and the investable thesis for operators and investors.",
                "price": "500",
            },
        ),
    )

    # --- UK Banking -------------------------------------------------------
    # Roster-driven (like Market Data): the curated UK banking list lives in
    # all/0-working/uk-banks-roster.json with a tier per provider.
    UK_TIER_LABELS = {
        "cma9":              "CMA9 (Mandated Open Banking)",
        "high-street":       "High-Street & Retail",
        "challenger":        "Challenger & Neobank",
        "baas-clearing":     "BaaS & Clearing",
        "building-society":  "Building Society",
        "sme":               "SME & Business",
        "specialist-lender": "Specialist & Mid-Tier Lender",
        "private-bank":      "Private Bank",
        "payments":          "Payments",
        "savings":           "Savings",
    }
    uk_banks = []
    uk_roster_path = os.path.join(ALL, "0-working", "uk-banks-roster.json")
    with open(uk_roster_path, "r", encoding="utf-8") as fh:
        uk_roster = json.load(fh)
    for p in uk_roster["providers"]:
        meta = meta_of(p["slug"])
        if meta is None:
            continue
        entry = rated_entry(p["slug"], meta)
        tier = p.get("tier", "")
        if tier:
            entry["tier"] = UK_TIER_LABELS.get(tier, titleize(tier))
        uk_banks.append(entry)
    uk_banks_grouped = band_grouped(uk_banks)
    with open(os.path.join(data_dir, "providers-uk-banks.json"), "w", encoding="utf-8") as fh:
        json.dump(uk_banks_grouped, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "uk-banks", "index.html"),
        listing_page(
            "UK Banking",
            "UK banks and building societies ranked by their Kin Score, from the CMA9 Open Banking mandate to challengers, building societies, and private banks.",
            "providers-uk-banks",
            rated=True,
        ),
    )

    # --- US Banking -------------------------------------------------------
    # Roster-driven (like Market Data / UK): the curated US banking list lives
    # in all/0-working/us-banks-roster.json with a tier per provider.
    US_TIER_LABELS = {
        "money-center":    "Money-Center & Custody",
        "super-regional":  "Super-Regional",
        "regional":        "Regional",
        "digital":         "Digital & Neobank",
        "baas":            "Banking-as-a-Service",
        "credit-union":    "Credit Union",
        "aggregator":      "Aggregator & FDX",
    }
    us_banks = []
    us_roster_path = os.path.join(ALL, "0-working", "us-banks-roster.json")
    with open(us_roster_path, "r", encoding="utf-8") as fh:
        us_roster = json.load(fh)
    for p in us_roster["providers"]:
        meta = meta_of(p["slug"])
        if meta is None:
            continue
        entry = rated_entry(p["slug"], meta)
        tier = p.get("tier", "")
        if tier:
            entry["tier"] = US_TIER_LABELS.get(tier, titleize(tier))
        us_banks.append(entry)
    us_banks_grouped = band_grouped(us_banks)
    with open(os.path.join(data_dir, "providers-us-banks.json"), "w", encoding="utf-8") as fh:
        json.dump(us_banks_grouped, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "us-banks", "index.html"),
        listing_page(
            "US Banking",
            "US banks, credit unions, neobanks, and banking-as-a-service providers ranked by their Kin Score — from the money-center banks and the BaaS layer to the aggregators wiring the CFPB 1033 / FDX open-finance era.",
            "providers-us-banks",
            rated=True,
        ),
    )

    # --- Canadian Banking -------------------------------------------------
    # Roster-driven (like US/UK): all/0-working/canadian-banks-roster.json.
    CA_TIER_LABELS = {
        "big-six":          "Big Six",
        "schedule-i":       "Schedule I (Domestic)",
        "schedule-ii":      "Schedule II (Foreign-Owned)",
        "digital-arm":      "Digital Arm",
        "provincial-crown": "Provincial / Crown",
        "credit-union":     "Credit Union & Caisse",
        "fintech":          "Fintech & Challenger",
        "infrastructure":   "Payments & Infrastructure",
    }
    ca_banks = []
    ca_roster_path = os.path.join(ALL, "0-working", "canadian-banks-roster.json")
    with open(ca_roster_path, "r", encoding="utf-8") as fh:
        ca_roster = json.load(fh)
    for p in ca_roster["providers"]:
        meta = meta_of(p["slug"])
        if meta is None:
            continue
        entry = rated_entry(p["slug"], meta)
        tier = p.get("tier", "")
        if tier:
            entry["tier"] = CA_TIER_LABELS.get(tier, titleize(tier))
        ca_banks.append(entry)
    ca_banks_grouped = band_grouped(ca_banks)
    with open(os.path.join(data_dir, "providers-canadian-banks.json"), "w", encoding="utf-8") as fh:
        json.dump(ca_banks_grouped, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "canadian-banks", "index.html"),
        listing_page(
            "Canadian Banking",
            "Canadian banks, credit unions and caisses, and fintechs ranked by their Kin Score — the Big Six, the digital arms, and the challengers, ahead of Canada's Consumer-Driven Banking framework.",
            "providers-canadian-banks",
            rated=True,
        ),
    )

    # --- Payments (US / UK / AU / CA) -------------------------------------
    # Roster-driven, HQ/origin model: each payment company appears on its home
    # market's page (plus that country's domestic rails). Rosters live in
    # all/0-working/<cc>-payments-roster.json. Tier vocabulary is shared across
    # all four so the pages read consistently.
    PAY_TIER_LABELS = {
        "card-network":      "Card Networks",
        "acquirer-processor":"Acquirers & Processors",
        "gateway-psp":       "Gateways & PSPs",
        "issuer-processor":  "Issuer-Processors",
        "embedded-baas":     "Embedded Finance & BaaS",
        "money-movement":    "Cross-Border & Money Movement",
        "open-banking":      "Open Banking & A2A Payments",
        "billing":           "Billing & Subscriptions",
        "bnpl":              "Buy Now, Pay Later",
        "spend-ap-ar":       "Spend, AP & AR",
        "crypto":            "Crypto & Stablecoin Rails",
        "fraud-identity":    "Fraud, Risk & Identity",
        "data-aggregation":  "Financial Data & Aggregation",
        "rails-scheme":      "Domestic Rails & Schemes",
    }
    PAY_SECTIONS = [
        ("us-payments", "us-payments-roster.json", "US Payments",
         "US payment companies ranked by their Kin Score — the four card networks, the acquirer/processor layer, and the API-native frontier of PSPs, issuer-processors, embedded-finance/BaaS, spend, crypto, and the ACH / RTP / FedNow rails, in the world's deepest and most fragmented payments market.",
         {"slug": "state-of-us-payments-apis", "title": "The State of US Payments APIs",
          "blurb": "68 US payment companies scored — the deepest, most agent-instrumented payments estate on earth, and the market with no mandate and no floor. Four Exemplars, the card networks trailing the fintechs, the rails absent as self-serve APIs, and no FAPI/mTLS anywhere.", "price": "500"}),
        ("uk-payments", "uk-payments-roster.json", "UK Payments",
         "UK payment companies ranked by their Kin Score — the open-banking payment-initiation frontier (TrueLayer, Yapily, Volt, GoCardless), card acquirers and PSPs (SumUp, Dojo, Primer), issuer-processors and BaaS, cross-border money movement, and the Pay.UK Faster Payments rails.",
         {"slug": "state-of-uk-payments-apis", "title": "The State of UK Payments APIs",
          "blurb": "32 UK payment companies scored — the open-banking payment-initiation heartland, and the market that hides its own crown jewels: the FAPI/mTLS security spine invisible in the contracts, scope-consent unpublished by the marquee PIS players, and the brand names that don't lead.", "price": "500"}),
        ("au-payments", "au-payments-roster.json", "Australian Payments",
         "Australian payment companies ranked by their Kin Score — ASX-listed merchant acquirers (Tyro, Zeller), NPP-connected money movement (Monoova, Zepto, Azupay), the Melbourne-born global breakout Airwallex, the aggregation layer, and the New Payments Platform / PayTo rails.",
         {"slug": "state-of-australian-payments-apis", "title": "The State of Australian Payments APIs",
          "blurb": "20 Australian payment companies scored — the NPP-native market where the signature resource is PayID, not the card charge. Highest discoverability in the series, one real hosted MCP in the whole country, and one honest push from the most agent-native payments market in the world.", "price": "500"}),
        ("canadian-payments", "canadian-payments-roster.json", "Canadian Payments",
         "Canadian payment companies ranked by their Kin Score — the global-scale exception Nuvei, incumbent acquirer Moneris, the SMB money-movement fintechs (VoPay, Plooto, Rotessa, Helcim), the aggregation layer, and the Interac / Payments Canada Real-Time Rail infrastructure.",
         {"slug": "state-of-canadian-payments-apis", "title": "The State of Canadian Payments APIs",
          "blurb": "14 Canadian payment companies scored — the thinnest, most concentrated market, where the API-native fintechs out-API the incumbents and the rails. VoPay's 404-operation rail abstraction is the deepest surface in the country, and the top score is an identity company that overstates its own agent surface.", "price": "500"}),
    ]
    def build_roster_sections(sections, tier_labels, counts):
        for slug_page, roster_file, title, summary, paper in sections:
            roster_path = os.path.join(ALL, "0-working", roster_file)
            with open(roster_path, "r", encoding="utf-8") as fh:
                roster = json.load(fh)
            entries = []
            for p in roster["providers"]:
                meta = meta_of(p["slug"])
                if meta is None:
                    continue
                entry = rated_entry(p["slug"], meta)
                tier = p.get("tier", "")
                if tier:
                    entry["tier"] = tier_labels.get(tier, titleize(tier))
                entries.append(entry)
            grouped = band_grouped(entries)
            data_key = "providers-%s" % slug_page
            with open(os.path.join(data_dir, "%s.json" % data_key), "w", encoding="utf-8") as fh:
                json.dump(grouped, fh, ensure_ascii=False, indent=1)
            write_page(
                os.path.join(SITE, slug_page, "index.html"),
                listing_page(title, summary, data_key, rated=True, paper=paper),
            )
            counts[slug_page] = (len(entries), sum(1 for e in entries if "score" in e))

    pay_counts = {}
    build_roster_sections(PAY_SECTIONS, PAY_TIER_LABELS, pay_counts)

    # --- Healthcare (US / UK / AU / CA) -----------------------------------
    # Roster-driven, HQ/origin model (mirrors Payments): each healthcare
    # company appears on its home market's page plus that country's national
    # health system. Rosters live in all/0-working/<cc>-healthcare-roster.json.
    HEALTH_TIER_LABELS = {
        "ehr-emr":               "EHR / EMR Systems",
        "interoperability":      "Interoperability & Health Data Networks",
        "payer-claims":          "Payer, Claims & Eligibility",
        "clinical-ai":           "Clinical AI & Documentation",
        "telehealth":            "Telehealth & Virtual Care",
        "patient-engagement":    "Patient Engagement & Scheduling",
        "pharmacy":              "Pharmacy & e-Prescribing",
        "life-sciences":         "Life Sciences & Clinical Trials",
        "genomics":              "Genomics & Diagnostics",
        "devices-wearables":     "Devices & Wearables",
        "rcm-billing":           "Revenue Cycle & Billing",
        "health-data-analytics": "Health Data & Analytics",
        "national-health":       "National Health System",
        "practice-management":   "Practice Management",
    }
    HEALTH_SECTIONS = [
        ("us-healthcare", "us-healthcare-roster.json", "US Healthcare",
         "US healthcare companies ranked by their Kin Score — the EHR duopoly and its challengers, the HL7 FHIR interoperability and health-data networks, payer/claims/eligibility rails, the clinical-AI wave, telehealth, pharmacy and e-prescribing, life sciences, and the CMS national infrastructure behind the 21st Century Cures Act.",
         {"slug": "state-of-us-healthcare-apis", "title": "The State of US Healthcare APIs",
          "blurb": "77 US healthcare companies scored — the lowest-scoring sector in the series (avg 36.8), where the Cures Act FHIR mandate produced compliance, not product: the incumbent EHRs publish gated CapabilityStatements while API-native challengers ship larger self-serve FHIR, and consent is invisible despite HIPAA.", "price": "500"}),
        ("uk-healthcare", "uk-healthcare-roster.json", "UK Healthcare",
         "UK healthcare organizations ranked by their Kin Score — NHS England's national FHIR API platform (PDS, GP Connect, e-Referrals, EPS), the GP clinical-system duopoly (EMIS, TPP SystmOne), and the commercial health-tech integrating around the single national system.",
         {"slug": "state-of-uk-healthcare-apis", "title": "The State of UK Healthcare APIs",
          "blurb": "13 UK healthcare organizations scored — the mirror image of the US inversion: one national payer, so the incumbent (NHS England) is the strongest contract publisher and the challengers orbit it. Governance is 0.0 across all 13; consent is legible at exactly one provider.", "price": "500"}),
        ("au-healthcare", "au-healthcare-roster.json", "Australian Healthcare",
         "Australian healthcare organizations ranked by their Kin Score — the Australian Digital Health Agency's My Health Record and national infrastructure, the GP-software duopoly (Best Practice, MedicalDirector), and the compact commercial cohort (Cliniko, HotDoc, HealthEngine, Coviu, Heidi Health).",
         {"slug": "state-of-australian-healthcare-apis", "title": "The State of Australian Healthcare APIs",
          "blurb": "12 Australian healthcare organizations scored — where a small API-first challenger layer out-executes the national agency and the GP duopoly, and one challenger literally built the incumbents' FHIR facade. Highest-averaging healthcare market; the national clinical record isn't openly contracted at all.", "price": "500"}),
        ("canadian-healthcare", "canadian-healthcare-roster.json", "Canadian Healthcare",
         "Canadian healthcare organizations ranked by their Kin Score — Canada Health Infoway's pan-Canadian FHIR stewardship, the consolidating commercial layer (WELL Health, TELUS Health), and the practice-management and telehealth players (Jane, OSCAR EMR, Dialogue, Maple) across a province-fragmented system.",
         {"slug": "state-of-canadian-healthcare-apis", "title": "The State of Canadian Healthcare APIs",
          "blurb": "10 Canadian healthcare organizations scored — the lowest-scoring market in the series, and a triple inversion: no API-native FHIR challenger class exists, so a niche practice-management SaaS (Jane) tops the field. Zero live clinical-data FHIR endpoints nationwide; governance 0.0.", "price": "500"}),
    ]
    health_counts = {}
    build_roster_sections(HEALTH_SECTIONS, HEALTH_TIER_LABELS, health_counts)

    # --- Insurance (US / UK / AU / CA) ------------------------------------
    # Roster-driven, HQ/origin model (mirrors Payments + Healthcare). Unlike
    # both, insurance has NO mandate in any of the four markets, so the tiers
    # separate the vendors and market bodies from the carriers themselves.
    # Rosters live in all/0-working/<cc>-insurance-roster.json.
    INS_TIER_LABELS = {
        "carrier-pc":            "P&C / General Insurers",
        "carrier-life-health":   "Life, Health & Benefits Insurers",
        "reinsurance":           "Reinsurance",
        "insurtech-dtc":         "Insurtech & Digital-Native Insurers",
        "embedded-insurance":    "Embedded Insurance & Distribution APIs",
        "core-systems":          "Core Systems & Policy Administration",
        "agency-brokerage-tech": "Agency & Brokerage Technology",
        "broker-intermediary":   "Brokers & Intermediaries",
        "risk-data-analytics":   "Risk Data & Analytics",
        "claims-tech":           "Claims Technology",
        "underwriting-ai":       "Underwriting AI & Submission Ingestion",
        "specialty-cyber":       "Cyber & Specialty Risk",
        "benefits-admin":        "Employee Benefits Administration",
        "market-infrastructure": "Market Bodies, Standards & Regulators",
    }
    INS_SECTIONS = [
        ("us-insurance", "us-insurance-roster.json", "US Insurance",
         "US insurance companies ranked by their Kin Score — the national P&C and life carriers, the digital-native insurtechs, embedded distribution, the core policy-administration vendors (Guidewire, Duck Creek, Socotra), agency and brokerage technology, the risk-data layer (Verisk, LexisNexis Risk, CoreLogic), claims technology, cyber specialty, benefits administration, and the ACORD/NAIC market bodies — in a market with fifty state regulators and no open-insurance mandate at all.",
         {"slug": "state-of-us-insurance-apis", "title": "The State of US Insurance APIs",
          "blurb": "79 US insurance companies scored (avg 29.2) — the market where ACORD wrote the standard and almost nobody implements it as an API. The vendors and risk-data monopolies out-publish every carrier they sell to, the insurtechs score no better than the incumbents they were founded to disrupt, and not one company in the sector reaches Exemplar.", "price": "500"}),
        ("uk-insurance", "uk-insurance-roster.json", "UK Insurance",
         "UK insurance organizations ranked by their Kin Score — the composite and specialty carriers (Aviva, Admiral, Direct Line, Hiscox, Beazley), the London Market and its modernization infrastructure (Lloyd's, PPL, Whitespace, Ki), the underwriting-AI cluster (Send, Artificial Labs, Cytora), the densest insurtech cohort in the series, brokers and agency technology, and the FCA.",
         {"slug": "state-of-uk-insurance-apis", "title": "The State of UK Insurance APIs",
          "blurb": "35 UK insurance organizations scored (avg 28.2) — and the one genuine surprise in the series: a 337-year-old subscription market, not a regulator, produced the only working data standard and public APIs in global insurance. A Lloyd's syndicate out-publishes every US software vendor, and ACORD lives in London rather than the country that wrote it.", "price": "500"}),
        ("au-insurance", "au-insurance-roster.json", "Australian Insurance",
         "Australian insurance organizations ranked by their Kin Score — the general-insurance oligopoly (IAG, Suncorp, QBE, Youi), the separately regulated private health funds (Medibank, nib, HCF, Bupa), the insurtech and embedded cohort including the global breakout Cover Genius, listed broker networks, claims and core-systems vendors, and the APRA / Insurance Council market layer.",
         {"slug": "state-of-australian-insurance-apis", "title": "The State of Australian Insurance APIs",
          "blurb": "20 Australian insurance organizations scored (avg 31.7) — the highest-scoring insurance market in the series, and the one that shows what a missing mandate costs: the CDR opened banking and energy, then stopped before insurance. The country has the legal machinery for open insurance and no live obligation, so a core-systems startup tops a market of national carriers.", "price": "500"}),
        ("canadian-insurance", "canadian-insurance-roster.json", "Canadian Insurance",
         "Canadian insurance organizations ranked by their Kin Score — the P&C oligopoly (Intact, Definity, Co-operators, Desjardins, Wawanesa), the life trio (Manulife, Sun Life, Great-West), digital-native brokers and insurtechs (Zensurance, APOLLO, Goose, Onlia), core systems, and OSFI — under the most fragmented supervision of the four markets.",
         {"slug": "state-of-canadian-insurance-apis", "title": "The State of Canadian Insurance APIs",
          "blurb": "20 Canadian insurance organizations scored (avg 26.9) — the lowest-scoring market in the quartet, where Consumer-Driven Banking pointedly excludes insurance and the federal regulator publishes a better API than any insurer it supervises. A digital broker tops the field; the Big-Few carriers sit beneath their own watchdog.", "price": "500"}),
    ]
    ins_counts = {}
    build_roster_sections(INS_SECTIONS, INS_TIER_LABELS, ins_counts)

    # --- Telecommunications (single GLOBAL cohort) ------------------------
    # Deliberately NOT a country quartet: telecom's developer surface is owned
    # by a globally-consolidated aggregator layer (CPaaS/IoT/identity) that is
    # overwhelmingly US/EU-headquartered, so an HQ split would leave every
    # non-US page carrier-only. The unit of analysis is the global network-API
    # market and the CAMARA / GSMA Open Gateway programme spanning it.
    TELECOM_TIER_LABELS = {
        "mno-carrier":          "Mobile Network Operators",
        "cpaas-aggregator":     "CPaaS & Messaging Aggregators",
        "network-api-exposure": "Network-API Exposure (CAMARA / Open Gateway)",
        "standards-body":       "Standards Bodies",
        "wholesale-messaging":  "Wholesale & Interconnect",
        "iot-esim":             "IoT Connectivity & eSIM",
        "ucaas-voice":          "UCaaS & Cloud Voice",
        "fixed-broadband":      "Fixed & Broadband",
        "satellite-ntn":        "Satellite & Non-Terrestrial",
        "identity-antifraud":   "Identity & Anti-Fraud",
        "network-vendor-bss":   "Network Vendors & BSS/OSS",
        "regulator":            "Regulators",
    }
    TELECOM_SECTIONS = [
        ("telecom", "telecom-roster.json", "Telecommunications",
         "The global telecom landscape ranked by Kin Score — mobile network operators across every major market, the CPaaS and messaging aggregators that resell their connectivity, the CAMARA / GSMA Open Gateway network-API exposure layer (Aduna, Nokia Network as Code), the standards bodies that write the specs (CAMARA, GSMA, 3GPP, ETSI, MEF, TM Forum), IoT and eSIM connectivity, UCaaS, wholesale interconnect, satellite and non-terrestrial networks, identity and anti-fraud, network vendors and BSS/OSS, and the regulators.",
         {"slug": "state-of-telecom-apis", "title": "The State of Telecom APIs",
          "blurb": "83 telecom organizations scored — the only sector with a real, industry-built API standard, and the widest gap in the series between signing it and shipping it. The aggregators that resell carrier connectivity out-publish their own suppliers by 19 points, and the standards bodies out-publish the carriers that wrote the standards.", "price": "500"}),
    ]
    telecom_counts = {}
    build_roster_sections(TELECOM_SECTIONS, TELECOM_TIER_LABELS, telecom_counts)

    # --- Real Estate (US / UK / AU / CA) ----------------------------------
    # Roster-driven, HQ/origin model. Real estate is the ONLY sector in the
    # series with a genuinely mandated machine-readable contract — RESO, whose
    # Web API and Data Dictionary NAR requires association-owned MLSs to
    # certify against (Policy Statement 7.90). The mandate comes from an
    # industry body, not a regulator, and it exists only in the US: 57 of the
    # 67 organizations bootstrapped for this study have no RESO reference at
    # all, mostly because outside the US there is no MLS to certify against.
    # The tiers therefore separate the listing-data infrastructure that holds
    # the certifications from the portals, brokerages and registries around it.
    # Rosters live in all/0-working/<cc>-real-estate-roster.json.
    RE_TIER_LABELS = {
        "portal-marketplace":      "Portals & Marketplaces",
        "mls-data-infrastructure": "Listing Data Infrastructure",
        "brokerage":               "Brokerages & Agencies",
        "crm-transaction-tech":    "Agency CRM & Transaction Technology",
        "valuation-avm":           "Valuation & AVM",
        "title-escrow-closing":    "Title, Escrow & Closing",
        "property-management":     "Property Management",
        "commercial-cre":          "Commercial Real Estate",
        "ibuyer":                  "iBuyers & Instant Offers",
        "land-registry-govt":      "Land Registries & Government",
        "rental-listings":         "Rentals & Listings",
        "mortgage-proptech":       "Mortgage Proptech",
        "proptech-data":           "Property Data & Analytics",
        "industry-body":           "Industry Bodies & Standards",
    }
    RE_SECTIONS = [
        ("us-real-estate", "us-real-estate-roster.json", "US Real Estate",
         "US real estate organizations ranked by their Kin Score — the portals (Zillow, Realtor.com, Redfin, Homes.com), the listing-data infrastructure that federates roughly 500 local MLSs (Trestle, MLS Grid, Spark, Bridge), the national brokerages, agency CRM and transaction technology, valuation and AVM, title and closing, property management, commercial CRE, iBuyers, the property-data layer, and the two bodies that make this market unique — RESO, which writes the only mandated machine-readable contract in the series, and NAR, which requires MLSs to certify against it.",
         {"slug": "state-of-us-real-estate-apis", "title": "The State of US Real Estate APIs",
          "blurb": "45 US real estate organizations scored (avg 31.2) — the only market in the series with a mandated machine-readable contract, and the mandate is worth about two points. RESO-certified providers average 38.0 against 36.0 for everyone else, every certified party is a reseller whose metadata document returns 401, and the portal NAR itself is affiliated with scores 7.9. Property-management software tops the market; nothing in it reaches Exemplar.", "price": "500"}),
        ("uk-real-estate", "uk-real-estate-roster.json", "UK Real Estate",
         "UK real estate organizations ranked by their Kin Score — the portal duopoly (Rightmove, Zoopla) and its challenger OnTheMarket, the agency CRM layer that actually feeds them (Reapit, Alto, Street, Apex27), the national brokerages, the property-data and analytics cluster, property management, the professional bodies (RICS, Propertymark), and the open-government layer that has no counterpart in the US — HM Land Registry and Ordnance Survey.",
         {"slug": "state-of-uk-real-estate-apis", "title": "The State of UK Real Estate APIs",
          "blurb": "24 UK real estate organizations scored (avg 42.8) — the highest-scoring real estate market in the series, and the one with no MLS, no industry standard and no mandate of any kind. What it has instead is a state that publishes: Ordnance Survey (68.5) and HM Land Registry (59.5) are the open layer, and the private portal duopoly that controls the listings is nowhere near them.", "price": "500"}),
        ("au-real-estate", "au-real-estate-roster.json", "Australian Real Estate",
         "Australian real estate organizations ranked by their Kin Score — the portal duopoly (REA Group's realestate.com.au and Domain) and challenger View, the valuation concentration in PropTrack and CoreLogic, the national brokerage networks, agency CRM and property-management software, the progressively privatised state land registries, and PEXA — the electronic conveyancing network that settles the overwhelming majority of Australian property transactions and is the closest thing in this study to a required national machine-readable property rail.",
         {"slug": "state-of-australian-real-estate-apis", "title": "The State of Australian Real Estate APIs",
          "blurb": "18 Australian real estate organizations scored (avg 33.5) — topped by PEXA (60.1), the electronic conveyancing rail that state law effectively requires, not by the portals that own the audience. REA and Domain finish nine tenths of a point apart and neither reaches Strong, REA's entire published surface belongs to its PropTrack subsidiary, and the state land registries out-publish the brokerages.", "price": "500"}),
        ("canadian-real-estate", "canadian-real-estate-roster.json", "Canadian Real Estate",
         "Canadian real estate organizations ranked by their Kin Score — CREA and REALTOR.ca with the Data Distribution Facility that syndicates member boards' listings in place of the US's ~500 MLSs, the challenger portals that have historically fought CREA for access to that data (HouseSigma, Wahi, Zolo, Properly), the national brokerage brands, rentals and property management, mortgage proptech, and the privatised provincial land registries including Teranet — where the public record itself is a commercial product.",
         {"slug": "state-of-canadian-real-estate-apis", "title": "The State of Canadian Real Estate APIs",
          "blurb": "14 Canadian real estate organizations scored (avg 28.9) — the lowest-scoring market in the quartet, and the fifth consecutive sector in which Canada finishes last. The top score belongs to a US vendor's Canadian arm rather than to any Canadian institution; the national cooperative that runs REALTOR.ca is the best-performing domestic body at 41.9, and the privatised provincial land registry that sells the public record scores 32.0.", "price": "500"}),
    ]
    re_counts = {}
    build_roster_sections(RE_SECTIONS, RE_TIER_LABELS, re_counts)

    # --- Energy & Utilities (US / UK / AU / CA) ---------------------------
    # Roster-driven, HQ/origin model. Energy is the sector that tests whether a
    # data mandate is REPLICABLE: Australia extended the same Consumer Data Right
    # that produced its byte-for-byte fifty-bank banking contract to ENERGY, and
    # Ontario mandated Green Button by regulation — against a US where Green Button
    # is a real standard nobody is compelled to adopt, and a UK that mandated smart-
    # meter INFRASTRUCTURE rather than a consumer data right. The sector also runs
    # at two speeds the tiers deliberately separate: consumer data (mandated, gated
    # by accreditation and consent) and market/grid data (frequently wide open).
    # Rosters live in all/0-working/<cc>-energy-roster.json.
    ENERGY_TIER_LABELS = {
        "utility-retailer":          "Utilities & Retailers",
        "network-distributor":       "Network Distributors",
        "system-operator":           "System & Market Operators",
        "regulator":                 "Regulators & Government Data",
        "energy-data-platform":      "Energy Data Platforms",
        "grid-tech-derms":           "Grid Tech & DERMS",
        "metering":                  "Metering",
        "solar-der":                 "Solar & Distributed Energy",
        "ev-charging":               "EV Charging",
        "energy-trading-markets":    "Energy Trading & Markets",
        "carbon-climate-accounting": "Carbon & Climate Accounting",
        "storage-flexibility":       "Storage & Flexibility",
        "industry-body-standards":   "Industry Bodies & Standards",
    }
    ENERGY_SECTIONS = [
        ("us-energy", "us-energy-roster.json", "US Energy",
         "US energy and utilities organizations ranked by their Kin Score — the investor-owned utilities, the seven ISOs and RTOs that run the wholesale markets and publish genuine open market data, the federal data agencies (EIA publishes one of the best government APIs anywhere), the energy-data platforms that resell utility billing and usage data, DERMS and demand response, metering, solar and distributed energy, EV charging, energy trading, carbon accounting, and the standards bodies behind Green Button and OpenADR — in the one market where Green Button is a real standard with no mandate compelling anyone to adopt it.",
         {"slug": "state-of-us-energy-apis", "title": "The State of US Energy APIs",
          "blurb": "60 US energy organizations scored (avg 32.8) — the market with a real standard and nothing compelling anyone to use it, and the lowest-scoring of the four despite holding the sector's single highest score. The seven wholesale market operators and the federal data agencies publish genuinely open grid data; the investor-owned utilities that bill 150 million Americans average under 30. Green Button is voluntary, and it shows.", "price": "500"}),
        ("uk-energy", "uk-energy-roster.json", "UK Energy",
         "UK energy organizations ranked by their Kin Score — the suppliers (including Octopus, whose Kraken platform is licensed to utilities worldwide), the distribution network operators and their open-data programmes, NESO and Elexon running the system and the balancing market, the licensed Smart DCC monopoly carrying smart-meter traffic, Ofgem, the consumer-data intermediaries, EV charging and flexibility — in the market that mandated the infrastructure rather than the data right.",
         {"slug": "state-of-uk-energy-apis", "title": "The State of UK Energy APIs",
          "blurb": "26 UK energy organizations scored (avg 40.9) — the market that mandated the infrastructure instead of the data right, and got exactly that. Britain has more live mandates than Australia and a fraction of the consumer APIs. What it has instead is the best-published distribution networks in the world (UK Power Networks and Northern Powergrid both hit 94.2 on agent-readiness) and Octopus, whose Kraken platform tops the market and is licensed to utilities on three continents.", "price": "500"}),
        ("au-energy", "au-energy-roster.json", "Australian Energy",
         "Australian energy organizations ranked by their Kin Score — the retailers bound by the Consumer Data Right, the distribution networks and their open data, AEMO acting as both the national market operator and the CDR energy gateway, the AER and AEMC, storage and flexibility, EV charging and the consumer-data platforms — in the only market anywhere that took a data mandate proven in banking and transplanted it into a second industry.",
         {"slug": "state-of-australian-energy-apis", "title": "The State of Australian Energy APIs",
          "blurb": "24 Australian energy organizations scored (avg 41.6) — the highest-scoring market in the sector, and the proof that a data mandate is replicable. Australia took the Consumer Data Right that produced its byte-for-byte banking contract and transplanted it into energy: every retailer is live, agent-readiness averages 57.3 against the US's 30.2, and AEMO runs both the open market data and the mandated consumer gateway. The mandate arrived intact; the architecture did not.", "price": "500"}),
        ("canadian-energy", "canadian-energy-roster.json", "Canadian Energy",
         "Canadian energy organizations ranked by their Kin Score — the provincial Crown corporations and investor-owned utilities, the Ontario utilities bound by the province's Green Button regulation, IESO and AESO running the two competitive markets, the Ontario Energy Board and the Canada Energy Regulator, and EV charging — in a federation where electricity is provincial and the only data mandate is one province's.",
         {"slug": "state-of-canadian-energy-apis", "title": "The State of Canadian Energy APIs",
          "blurb": "18 Canadian energy organizations scored (avg 32.8) — where one province mandated Green Button and the rest of the federation did not, and the difference is smaller than the mandate's advocates would like. Ontario's bound utilities cluster in the Thin band; the top score belongs to a Quebec Crown corporation under no data mandate at all. For once Canada does not finish last — it ties.", "price": "500"}),
    ]
    energy_counts = {}
    build_roster_sections(ENERGY_SECTIONS, ENERGY_TIER_LABELS, energy_counts)

    # --- Travel & Aviation (US / UK / AU / CA) ----------------------------
    # Roster-driven, HQ/origin model. Travel is the sector where SWITCHING COST
    # is the commercial structure rather than a side effect: three GDS companies
    # have intermediated airline distribution for decades, IATA's NDC is a
    # standard mid-rollout intended to route around them, and channel managers
    # hold the same position in hotels. The bootstrap recorded interface shape,
    # second-source availability, exit path and identifier portability as
    # research metadata — the Kin Score cannot read any of it yet, and that
    # evidence is what will specify the switchability lens on the roadmap.
    #
    # Genuinely global infrastructure with no home market in the quartet —
    # Amadeus (Spain), Mews (NL/CZ), Ryanair (IE), Accor (FR) — is recorded in
    # each roster's `excluded` block and discussed in the reports as shared
    # context rather than forced onto a country page.
    # Rosters live in all/0-working/<cc>-travel-roster.json.
    TRAVEL_TIER_LABELS = {
        "gds-distribution":        "GDS & Distribution",
        "airline":                 "Airlines",
        "ota-metasearch":          "OTAs & Metasearch",
        "hotel-group":             "Hotel Groups",
        "hospitality-tech":        "Hospitality Technology",
        "booking-api-aggregator":  "Booking API Aggregators",
        "corporate-travel":        "Corporate Travel",
        "rail-ground":             "Rail & Ground",
        "car-rental":              "Car Rental",
        "airport-infrastructure":  "Airports & Infrastructure",
        "industry-body-standards": "Industry Bodies & Standards",
        "regulator":               "Regulators",
    }
    TRAVEL_SECTIONS = [
        ("us-travel", "us-travel-roster.json", "US Travel & Aviation",
         "US travel and aviation organizations ranked by their Kin Score — Sabre, one of the three GDS companies whose intermediation of airline inventory is the sector's defining commercial structure, the major carriers, the OTA duopoly that owns consumer demand (Expedia, Booking Holdings) plus Airbnb, the hotel groups whose direct-booking strategies are an explicit fight against that intermediation, hospitality technology, corporate travel, car rental, rail, the standards bodies (OpenTravel, HEDNA) and the federal regulators.",
         {"slug": "state-of-us-travel-apis", "title": "The State of US Travel APIs",
          "blurb": "30 US travel organizations scored (avg 33.0) — the strongest of the four travel markets, and still a sector where the companies that own the customer publish worst. Hertz scores 2.6 and Expedia 18.8, while Oracle Hospitality tops the market at 55.9 and the volunteer OpenTravel Alliance takes second at 55.1. Idempotency is zero of 30 at full credit, in an industry that books, pays, changes and cancels.", "price": "500"}),
        ("uk-travel", "uk-travel-roster.json", "UK Travel & Aviation",
         "UK travel and aviation organizations ranked by their Kin Score — Travelport, the third GDS, alongside Duffel, an API-first booking layer built explicitly to route around GDS intermediation using IATA's NDC; British Airways, an early and aggressive NDC adopter that surcharged GDS bookings; easyJet and Jet2, direct-distribution carriers that never used a GDS at all; Skyscanner in metasearch, Trainline in rail, IHG in hotels, and the Civil Aviation Authority.",
         {"slug": "state-of-uk-travel-apis", "title": "The State of UK Travel APIs",
          "blurb": "14 UK travel organizations scored (avg 27.7) — the market building the alternative to GDS intermediation, and scoring below the market it is trying to replace. Duffel, the API-first booking layer built on NDC, reaches 34.9; Travelport, the GDS it exists to route around, scores 26.2 — twenty-seven points behind Sabre. Skyscanner, the country’s best-known travel brand, scores 5.7, last in its own table.", "price": "500"}),
        ("au-travel", "au-travel-roster.json", "Australian Travel & Aviation",
         "Australian travel and aviation organizations ranked by their Kin Score — SiteMinder, a genuinely global channel manager built in Sydney that holds the same intermediary position in hotels that the GDS holds in aviation; the Qantas and Virgin Australia duopoly and its long history of distribution disputes; Jetstar as the low-cost direct-distribution arm; the unusually large agency groups (Webjet, Flight Centre, Corporate Travel Management, Helloworld); Sydney Airport and CASA.",
         {"slug": "state-of-australian-travel-apis", "title": "The State of Australian Travel APIs",
          "blurb": "11 Australian travel organizations scored (avg 24.8) — the thinnest published surface in the entire sector series. Contract quality averages 5.8 with nine of eleven organizations at zero, one organization in eleven publishes a machine-readable spec, and agent-readiness averages 11.2 with no agent-native organization at all. SiteMinder, a channel manager used by hotels worldwide, scores 18.7 with zero agent-readiness.", "price": "500"}),
        ("canadian-travel", "canadian-travel-roster.json", "Canadian Travel & Aviation",
         "Canadian travel and aviation organizations ranked by their Kin Score — IATA, headquartered in Montreal, which writes the NDC standard intended to restructure airline distribution worldwide; the Air Canada and WestJet duopoly with Porter as challenger; Hopper as an unusually API-native OTA; Transat and Flight Network; VIA Rail; and Transport Canada.",
         {"slug": "state-of-canadian-travel-apis", "title": "The State of Canadian Travel APIs",
          "blurb": "9 Canadian travel organizations scored (avg 26.9) — and the finding is IATA, headquartered in Montreal, scoring 21.5 in the Emerging band, tied with a tour operator and below a Crown-corporation railway. The body that writes NDC publishes 33.6 points less than the volunteer non-profit OpenTravel Alliance. Air Canada alone clears 45; the other eight sit between 14.9 and 40.7.", "price": "500"}),
    ]
    travel_counts = {}
    build_roster_sections(TRAVEL_SECTIONS, TRAVEL_TIER_LABELS, travel_counts)

    # --- Headless (single GLOBAL cohort) ----------------------------------
    # Not a sector in the usual sense: "headless" is a delivery architecture,
    # so it sells into three unrelated markets that share a word and little
    # else — content (CMS), commerce (cart/catalog/checkout), and rendering
    # (a browser as an API). A fourth tier tracks the monoliths and suites
    # that bolted a headless API onto an existing platform, which is where the
    # gap between the marketing and the contract is widest. The cohort is
    # curated in all/0-working/headless-roster.json from providers already in
    # all/*, with duplicate company repos resolved to the richer survivor
    # (see the roster's retired_duplicates map) so this counts companies.
    HEADLESS_TIER_LABELS = {
        "cms":      "Headless CMS & Content Platforms",
        "commerce": "Headless & Composable Commerce",
        "browser":  "Headless Browser & Rendering Infrastructure",
        "platform": "Platforms & Suites Going Headless",
    }
    HEADLESS_SECTIONS = [
        ("headless", "headless-roster.json", "Headless",
         "The headless landscape ranked by Kin Score — the headless CMS and content platforms that sell content as an API (Contentful, Storyblok, Sanity, Contentstack, Strapi), the headless and composable commerce platforms that sell cart, catalog and checkout as an API (commercetools, Commerce Layer, Salla, Swell, Elastic Path, Saleor, Medusa), the headless browser and rendering infrastructure that sells a rendered page as an API to scrapers and AI agents (Bright Data, Apify, Browserless, Browserbase, Hyperbrowser, Firecrawl), and the monoliths and suites that bolted a headless API onto an existing platform (WordPress, Shopify, Drupal, Magento, Sitecore, Adobe Experience Manager, Salesforce Commerce Cloud). One architecture, three unrelated markets, and a very uneven willingness to publish the contract the architecture depends on.",
         {"slug": "state-of-headless-apis", "title": "The State of Headless APIs",
          "blurb": "108 headless providers scored — the architecture whose whole promise is that the API is the product, tested against the evidence. The tier that invented the word finishes last: headless CMS averages 39.1 against 49.4 for the monoliths it was funded to disrupt, and WordPress out-publishes 33 of the 34 headless CMS vendors in the study. Not one provider in 108 signals idempotency, in a cohort selling checkout as an API.", "price": "500"}),
    ]
    headless_counts = {}
    build_roster_sections(HEADLESS_SECTIONS, HEADLESS_TIER_LABELS, headless_counts)

    print("industries:       %d (providers matched: %d)" % (
        len(industry_cards), sum(c["count"] for c in industry_cards)))
    print("countries:        %d (providers matched: %d)" % (
        len(country_cards), sum(c["count"] for c in country_cards)))
    print("australian banks: %d (scored: %d)" % (
        len(au_banks), sum(1 for b in au_banks if "score" in b)))
    print("market data:      %d (scored: %d)" % (
        len(market_data), sum(1 for e in market_data if "score" in e)))
    print("uk banks:         %d (scored: %d)" % (
        len(uk_banks), sum(1 for e in uk_banks if "score" in e)))
    print("us banks:         %d (scored: %d)" % (
        len(us_banks), sum(1 for e in us_banks if "score" in e)))
    for slug_page, _r, _t, _s, _p in PAY_SECTIONS:
        n, sc = pay_counts.get(slug_page, (0, 0))
        print("%-19s %d (scored: %d)" % (slug_page + ":", n, sc))
    for slug_page, _r, _t, _s, _p in HEALTH_SECTIONS:
        n, sc = health_counts.get(slug_page, (0, 0))
        print("%-19s %d (scored: %d)" % (slug_page + ":", n, sc))
    for slug_page, _r, _t, _s, _p in INS_SECTIONS:
        n, sc = ins_counts.get(slug_page, (0, 0))
        print("%-19s %d (scored: %d)" % (slug_page + ":", n, sc))
    for slug_page, _r, _t, _s, _p in TELECOM_SECTIONS:
        n, sc = telecom_counts.get(slug_page, (0, 0))
        print("%-19s %d (scored: %d)" % (slug_page + ":", n, sc))
    for slug_page, _r, _t, _s, _p in RE_SECTIONS:
        n, sc = re_counts.get(slug_page, (0, 0))
        print("%-19s %d (scored: %d)" % (slug_page + ":", n, sc))
    for slug_page, _r, _t, _s, _p in ENERGY_SECTIONS:
        n, sc = energy_counts.get(slug_page, (0, 0))
        print("%-19s %d (scored: %d)" % (slug_page + ":", n, sc))
    for slug_page, _r, _t, _s, _p in TRAVEL_SECTIONS:
        n, sc = travel_counts.get(slug_page, (0, 0))
        print("%-19s %d (scored: %d)" % (slug_page + ":", n, sc))
    for slug_page, _r, _t, _s, _p in HEADLESS_SECTIONS:
        n, sc = headless_counts.get(slug_page, (0, 0))
        print("%-19s %d (scored: %d)" % (slug_page + ":", n, sc))


if __name__ == "__main__":
    main()

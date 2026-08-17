#!/usr/bin/env python3
"""
Build the Industries, Countries, and Australian Banks sections of the
API Evangelist Providers site.

Sources:
  - ../../insights-work/_data/industries.yml             : industry taxonomy
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
import glob
import json
import os
import re
import subprocess
import sys

import yaml

import lib_bands

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(SITE))
ALL = os.path.join(ROOT, "all")
PROVIDERS = os.path.join(ROOT, "api-search", "providers", "_providers")
INDUSTRIES_YML = os.path.join(ROOT, "insights-work", "_data", "industries.yml")
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
# Industry Reports that have shipped, keyed by industry slug. Rendered as the
# paper-promo band above the listing on that industry's page (see
# _includes/paper-promo.html). Emitted by the generator so the promo survives a
# rebuild instead of being hand-added to a generated page and then wiped.
# The Spectral report has no listing page of its own: its cohort is 1,005 real
# public CI pipelines, not providers, so there is no roster to rank. It is
# promoted as a SECOND paper on the two markets it actually speaks to —
# governance tooling sits between API management and API testing.
SPECTRAL_PAPER = {
    "slug": "the-state-of-spectral-in-api-pipelines",
    "title": "The State of Spectral in API Pipelines",
    "blurb": "What 1,005 real public pipelines reveal about how teams actually "
             "govern their APIs — and the blueprint almost none of them have reached.",
    "price": "500",
    "kind": "API Evangelist Trend Report",
}


INDUSTRY_PAPERS = {
    "artificial-intelligence": {
        "slug": "state-of-artificial-intelligence-apis",
        "title": "The State of Artificial Intelligence APIs",
        "blurb": "All 4,904 of these companies scored. The industry selling agents has a median "
                 "agent-readiness of zero, and its score distribution matches the whole catalog "
                 "within a rounding error.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "developer-tools": {
        "slug": "state-of-developer-tools-apis",
        "title": "The State of Developer Tools APIs",
        "blurb": "The best-scoring industry in the catalog, first of twenty-five \u2014 and it publishes "
                 "idempotency at the same 2.8% rate as the worst. The gap was never competence.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "cybersecurity": {
        "slug": "state-of-cybersecurity-apis",
        "title": "The State of Cybersecurity APIs",
        "blurb": "Second-best-scoring market in the catalog \u2014 and 72% of it will not tell you how "
                 "to report a vulnerability, now that the EU Cyber Resilience Act requires exactly that.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "semiconductors-hardware": {
        "slug": "state-of-compute-hardware-apis",
        "title": "The State of Compute & Hardware APIs",
        "blurb": "The companies that rent the chips score 36.5. The companies that make them score "
                 "10.7. NVIDIA scores 31.1 and NVIDIA NIM scores 75.7.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "robotics": {
        "slug": "state-of-robotics-apis",
        "title": "The State of Robotics & Autonomous Systems APIs",
        "blurb": "Not short of APIs \u2014 short of PUBLIC ones. 5.8% publish a contract, and the "
                 "likely reason is security posture rather than absence.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "legal-compliance": {
        "slug": "state-of-legal-compliance-apis",
        "title": "The State of Legal & Compliance APIs",
        "blurb": "The contract lifecycle management segment publishes the fewest contracts in its "
                 "own market \u2014 18.2%, against e-signature's 55.0%.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "education": {
        "slug": "state-of-education-apis",
        "title": "The State of Education & EdTech APIs",
        "blurb": "The library out-publishes the classroom \u2014 scholarly infrastructure publishes a "
                 "contract 70.8% of the time, corporate learning 0%.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "blockchain-crypto": {
        "slug": "state-of-blockchain-crypto-apis",
        "title": "The State of Blockchain & Crypto APIs",
        "blurb": "The highest-publishing market in the catalog, and the one that says least about "
                 "who is allowed to move the money \u2014 scopes at 10.2% of its leaders.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "marketing-advertising": {
        "slug": "state-of-marketing-advertising-apis",
        "title": "The State of Marketing & Advertising APIs",
        "blurb": "The industry whose tracking wrote the world\u2019s consent laws describes consent in "
                 "its own APIs at 3.1% \u2014 below the whole-catalog rate.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "data-analytics": {
        "slug": "state-of-data-analytics-apis",
        "title": "The State of Data & Analytics APIs",
        "blurb": "One of the best-scoring markets in the catalog \u2014 and the segment selling "
                 "\u201cknow your data\u201d is the worst-scoring segment inside it.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "digital-health": {
        "slug": "state-of-digital-health-apis",
        "title": "The State of Digital Health APIs",
        "blurb": "The market with the best standard and the most mandates publishes consent as a "
                 "machine-readable surface at 3.4% \u2014 the same rate as the rest of the catalog.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "supply-chain": {
        "slug": "state-of-supply-chain-apis",
        "title": "The State of Supply Chain APIs",
        "blurb": "Thirteen companies out of 1,124 publish idempotency — in the one industry where "
                 "a retried request dispatches a second truck. No company here reaches 70.",
        "price": "500",
        "kind": "API Evangelist Market Report",
    },
    "biotechnology": {
        "slug": "state-of-biotechnology-apis",
        "title": "The State of Biotechnology APIs",
        "blurb": "An industry that built three workflow languages and published zero "
                 "workflow contracts. Biotechnology solved sequencing, orchestration and "
                 "reproducibility for compute pipelines over twenty years, and never once "
                 "pointed that machinery at its own interfaces.",
        "price": "500",
    },
    "climate-sustainability": {
        "slug": "state-of-climate-sustainability-apis",
        "title": "The State of Climate, Energy and Sustainability APIs",
        "blurb": "98% of the upper band publishes a contract — the highest rate measured "
                 "anywhere — and it is mostly weather APIs. The software that climate "
                 "regulation created is seventeen companies.",
        "price": "500",
    },
    "creator-economy": {
        "slug": "state-of-creator-economy-apis",
        "title": "The State of Creator Economy APIs",
        "blurb": "The market everyone describes as dependent on platforms turns out to be "
                 "the one best equipped to survive them.",
        "price": "500",
    },
    "gaming": {
        "slug": "state-of-gaming-apis",
        "title": "The State of Gaming APIs",
        "blurb": "The product is deliberately closed and the supply chain is wide open. "
                 "Heroic Labs scores 78.8; Take-Two scores 7.1.",
        "price": "500",
    },
    "government": {
        "slug": "state-of-government-apis",
        "title": "The State of Government APIs",
        "blurb": "The most consistently contract-publishing market measured anywhere in this "
                 "research is also one of the least operable. Government did the part the "
                 "policy named and stopped precisely there.",
        "price": "500",
    },
    "human-capital-management": {
        "slug": "state-of-human-capital-management-apis",
        "title": "The State of HR and Workforce APIs",
        "blurb": "This market proved it will adopt an API standard when one exists at the "
                 "right layer. It has done that exactly once, for the narrowest problem in "
                 "the stack.",
        "price": "500",
    },
    "iot": {
        "slug": "state-of-iot-apis",
        "title": "The State of IoT APIs",
        "blurb": "This market solved interoperability where devices meet networks and left "
                 "it unsolved where customers and agents meet platforms. The best contracts "
                 "in the research series; the lowest MCP adoption.",
        "price": "500",
    },
    "mobility": {
        "slug": "state-of-mobility-apis",
        "title": "The State of Mobility APIs",
        "blurb": "The best-documented market in this research is the least agent-ready one. "
                 "Mobility built excellent interfaces for a world of scheduled integrations "
                 "and webhooks, and that is precisely the investment that does not carry "
                 "forward.",
        "price": "500",
    },
    "space": {
        "slug": "state-of-space-apis",
        "title": "The State of Space and Aerospace APIs",
        "blurb": "Forty years of machine-to-machine standards produced spacecraft that talk "
                 "to each other across agencies and almost nothing a customer's agent can "
                 "operate.",
        "price": "500",
    },
    "telecommunications": {
        "slug": "state-of-telecom-apis",
        "title": "The State of Telecom APIs",
        "blurb": "What eighty-three telecom organizations worldwide actually publish, scored "
                 "— the industry that built a real open standard and then published 351 "
                 "specifications with no hosts in them.",
        "price": "500",
    },
    "weather-geospatial": {
        "slug": "state-of-weather-geospatial-apis",
        "title": "The State of Weather and Geospatial APIs",
        "blurb": "The best-governed market in this research scores badly on an instrument "
                 "built for agents that write. That is a finding about the instrument as "
                 "much as the market.",
        "price": "500",
    },
}

# Providers a tag rule cannot keep out of an industry, removed by hand.
#
# Some industries have a vocabulary they share with the rest of the economy, and no
# set of tags draws their edge correctly. Supply chain is the worst case in the
# catalog: even after the polysemous terms came out of TAG_INDUSTRIES, an iPaaS, a
# document-AI vendor, two headless commerce platforms and a container registry still
# land in it on a single legitimate tag. This list is the editorial boundary the tag
# rule cannot express, and it is the same boundary The State of Supply Chain APIs is
# scored against, so the section page and the report agree on who is in the market.
#
# Published into tag-industries.yml as an `exclude:` key so apis.io can honour the
# same boundary from the same source of truth.
TAG_INDUSTRY_EXCLUDE = {
    "supply-chain": {
        # horizontal software carrying one supply chain tag
        "boomi", "affinda", "dun-and-bradstreet", "tonkean", "postalcodes-info",
        # software supply chain - a different meaning of the phrase
        "google-cloud-artifact-registry", "openssf",
        # commerce platforms and consumer marketplaces
        "commerce-layer", "swell-io", "swell", "etsy", "depop", "wallapop",
        "back-market", "wish", "trendyol", "spreadshirt", "mirakl", "canal",
        "channable", "stockx", "bjs-wholesale-club", "kurly", "cratejoy", "snipcart",
        "spree", "opencart", "elastic-path", "demandware", "fabric-com", "bigcommerce",
        "shopify-admin", "woocommerce", "avify", "snackmagic",
        # trading, crypto, payments
        "bloomberg-aim", "bloomberg-emsx", "bitstamp", "montonio", "fenbeitong",
        # ride-hailing, food delivery, on-demand consumer
        "uber", "uber-eats", "cabify", "deliveroo", "getir", "goget", "also",
        "dispatch", "wolt",
        # restaurant and hospitality back office
        "plateiq", "qubiqle", "cloudkitchens", "deliverart", "otter", "erply",
        "restaurant365", "marginedge", "wisk", "itsacheckmate", "lunchbox", "slice",
        "fudo", "toast-tab", "flipdish",
        # fleet telematics and mapping - vehicles, not goods
        "samsara", "loconav", "automile", "revvo", "openrouteservice", "hivemapper",
        "travelcenters-of-america",
        # other verticals
        "kpn", "syniverse", "benchling", "stedi", "ease", "codafication", "buildxact",
        "zuper", "beamable", "steam", "partnerize", "n2yo", "looksrare",
        # public-sector sales intelligence - the sell side, not the buy side
        "govly", "starbridge", "nationgraph",
        # general-purpose ERP and enterprise planning suites; a NAMED supply chain
        # product from the same vendor (SAP Ariba, Oracle Transportation Management)
        # stays in
        "sap-s4hana", "sap-bydesign", "erpnext", "apache-ofbiz", "infor", "aptean",
        "workday-financials", "anaplan", "softwareone", "sap-fieldglass",
    },
    # `recipes` and `cooking` are the leaky ones here: they land on media
    # companies that publish a recipe section, on appliance and robotics
    # makers, and on drinks databases that carry no nutrition data at all.
    "nutrition": {
        # cooking hardware and kitchen robotics — an appliance, not nutrition
        "brava-home", "posha", "hamptons-lane",
        # media and marketplaces that happen to publish recipes
        "new-york-times-company", "everytv", "spoon-university", "rakuten",
        # drinks databases — recipes with no nutrition in them
        "punkapi", "thecocktaildb", "free-cocktail-api",
        # confectionery and packaged-goods brands carrying a `recipes` tag
        "jelly-belly",
        # restaurant and kitchen back office — costing and rostering, filed
        # under Food Service
        "apicbase", "gronda",
        # horizontal software carrying one `animal nutrition` tag
        "datacor",
        # consumer-brand aggregator, not a nutrition business
        "boosted-commerce",
    },
    "semiconductors-hardware": {
        # software sold TO hardware companies, not hardware
        "telemetron-ai", "first-resonance", "cofactr", "violetlabs",
        # hyperscaler platform and managed-service entries
        "google-distributed-cloud", "impossible-cloud",
        # not a compute or device business
        "upsie", "also", "ace-hardware", "coldsnap", "clover", "printnode",
        "stanley-black-and-decker", "wahoo", "hyperice",
    },
}

# The mirror image: real members of an industry that no tag rule can reach.
# e2open, Manhattan Associates and Blue Yonder are among the largest supply chain
# software vendors in the world and carry NO tags at all in the catalog. The rest
# are wholesale and IT distributors filed only under the ambiguous `distribution`
# tag that was removed from TAG_INDUSTRIES above.
TAG_INDUSTRY_INCLUDE = {
    "supply-chain": {
        "e2open", "manhattan-associates", "blue-yonder", "1worldsync",
        "tech-data", "pax8", "protonai", "scansource", "synnex",
        "sap-sales-and-distribution-sd",
    },
    # Food-composition APIs filed only under the generic `food and drink` tag,
    # plus Open Food Facts — the largest open food-product database in the
    # world, which carries no tags at all.
    "nutrition": {
        "chomp", "recipeapi", "edamam-nutrition", "open-food-facts",
        "fruityvice", "tasty",
    },
    # The silicon layer is invisible to tag matching. Intel is tagged only
    # `fortune 100`, Qualcomm only `fortune 500`, Synopsys is filed as a
    # software-security company, and KLA, Microchip and Qorvo carry no tags at all.
    "semiconductors-hardware": {
        "intel", "qualcomm", "broadcom", "micron-technology", "marvell-technology",
        "on-semiconductor", "microchip-technology", "skyworks-solutions", "qorvo",
        "silabs", "vishay-intertechnology", "western-digital",
        "synopsys", "cadence", "risc-v", "kla",
        "groq", "tenstorrent", "sima", "positron", "etched", "rebellions",
        "birentech", "mythic", "hp", "hpe",
    },
}

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
        # Five terms were removed here in Aug 2026 because they are polysemous and
        # were filing whole other industries under supply chain: `sourcing` matched
        # recruiting (an ATS ranked #1 in this section), `orders` matched brokerages
        # and ad ops, `distribution` matched electricity networks and travel
        # wholesalers, `tracking` matched web analytics, `cross-border` matched
        # payments. `inventory` went too - it matches game, lab and cloud-resource
        # inventory. A third of the section's upper band was not a supply chain
        # company. The logistics vocabulary that replaced them was missing entirely:
        # `logistics` alone matches 571 providers and was not in this list.
        "tags": [
            "supply chain", "supply-chain", "supply chain visibility", "supply chain risk",
            "procurement", "e-procurement", "eprocurement", "procure-to-pay", "source-to-pay",
            "strategic sourcing", "supplier management", "purchase orders",
            "logistics", "third-party logistics", "3pl", "reverse logistics",
            "freight", "freight forwarding", "freight brokerage", "load board",
            "trucking", "transportation management", "ocean freight", "air freight",
            "container tracking", "shipping",
            "last mile", "last mile delivery", "last-mile delivery", "last-mile-delivery",
            "courier", "couriers", "parcel delivery", "parcel tracking", "package tracking",
            "shipment tracking",
            "fulfillment", "warehousing", "warehouse management", "dropshipping", "dropship",
            "inventory management", "order management",
            "wholesale", "edi", "customs", "trade compliance", "global trade", "traceability",
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
        # `cloud computing`, `compute`, `storage`, `data center` and `data centers`
        # were removed in Aug 2026: they describe cloud infrastructure, not hardware,
        # and they made Google Cloud Platform the #1 "semiconductor" provider, with
        # Amazon EC2, Lambda, EBS, Azure, Databricks, Workday and Google Workspace
        # filling most of the top twenty. `cad` and `3d printing` went with them -
        # design software is a different market. See The State of Compute & Hardware
        # APIs, which had to rebuild this cohort by hand to say anything true.
        "tags": [
            "semiconductors", "semiconductor", "chips", "gpu", "quantum computing",
            "hardware", "consumer hardware", "consumer electronics", "electronics",
            "materials science",
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
    # Drawn deliberately NARROW — what a food is made of and what a person eats,
    # not the food business. Agriculture, Food Delivery and Food Service are
    # already their own industries, so the broad `food` / `food and beverage` /
    # `grocery` / `restaurant` tags stay out; a Fortune 500 packaged-foods
    # manufacturer is a consumer-goods company, not a nutrition provider.
    {
        "slug": "nutrition",
        "name": "Nutrition",
        "icon": "nutrition",
        "description": "Food composition databases, recipe and meal-planning platforms, food logging and diet tracking, supplements, and the dietitian and weight-management services built on top of them.",
        "tags": [
            "nutrition", "personalized nutrition", "sports nutrition", "infant nutrition",
            "medical nutrition", "medical nutrition therapy", "enteral nutrition",
            "telenutrition", "animal nutrition", "pet nutrition", "food and nutrition",
            "nutritional supplements", "supplements", "dietary supplements", "vitamins",
            "diet", "diets", "dietitian", "dietitians", "dietetics",
            "calories", "food diary", "weight tracking", "weight loss", "weight management",
            "recipes", "recipe search", "cooking", "meal planning", "meal plans",
            "meal kit", "meal kits", "meal replacement", "meal subscription",
            "food labeling", "branded foods", "baby food",
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
LISTING_LIMIT = int(os.environ.get("LISTING_LIMIT", "1000"))  # override to emit uncapped cohorts for bundling


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


AID_RE = re.compile(r"^aid:\s*['\"]?([\w.-]+)", re.M)


def resolve_conflicts(content, slug):
    """Collapse an unresolved git merge conflict in an apis.yml down to one side.

    A handful of all/*/apis.yml still carry `<<<<<<<` markers, so the file holds
    two documents' worth of top-level keys and any reader silently mixes them.
    Neither "first side" nor "last side" is right on its own: for most of them
    the enriched profile is the first side and a portfolio stub is the second,
    but in at least one the first side is a wholly different provider that got
    spliced in. So drop a side whose `aid:` names some OTHER provider, and
    otherwise keep the first — which is the enriched one in every case seen.

    This is damage control, not a repair: the files themselves need fixing.
    """
    if "<<<<<<< " not in content:
        return content
    head, ours, theirs, tail = [], [], [], []
    bucket = head
    for line in content.splitlines(keepends=True):
        if line.startswith("<<<<<<< "):
            bucket = ours
        elif line.startswith("=======") and bucket is ours:
            bucket = theirs
        elif line.startswith(">>>>>>> "):
            bucket = tail
        else:
            bucket.append(line)

    def disowns(block):
        # True only when the side positively claims a DIFFERENT provider; a side
        # with no aid at all is not evidence either way.
        m = AID_RE.search("".join(block))
        return bool(m) and m.group(1) != slug

    if disowns(ours) and not disowns(theirs):
        chosen = theirs
    else:
        chosen = ours
    return "".join(head + chosen + tail)


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
    content = resolve_conflicts(content, slug)
    tags = []
    m = TAGS_RE.search(content)
    if m:
        tags = [t.strip() for t in re.findall(r"-\s*(.+)", m.group(1))]
    name = _top_level_scalar(content, "name") or titleize(slug)
    if name.lower() in ("null", "~"):
        name = titleize(slug)
    description = " ".join((_top_level_scalar(content, "description") or "").split())
    return name, description, tags


def _kin_score_file(slug):
    """Newest all/<slug>/kin/score-*.yml — the authoritative Kin Score source.

    The provider frontmatter under PROVIDERS is a MIRROR of this, and the
    mirror goes stale: a provider can be freshly scored in all/* and still
    carry no `score:` block on its page, which sends it to "Not Yet Rated" on
    every listing even though we hold a real score for it. Used only to fill
    that gap — the mirror still wins wherever it has a value.
    """
    files = sorted(glob.glob(os.path.join(ALL, slug, "kin", "score-*.yml")))
    return files[-1] if files else None


def _kin_score_blocks(slug):
    """{'score': {...}, 'agent': {...}} straight from all/<slug>/kin, or None."""
    path = _kin_score_file(slug)
    if not path:
        return None
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            doc = yaml.safe_load(fh) or {}
    except (OSError, yaml.YAMLError):
        return None
    ks = doc.get("kin_score")
    if not isinstance(ks, dict) or ks.get("composite") is None:
        return None
    score = {
        "composite": ks.get("composite"),
        "band": ks.get("band"),
        "facets": ks.get("facets") or {},
        "scored_at": ks.get("scored_at"),
        "schema_version": ks.get("schema_version"),
    }
    if ks.get("regulatory"):
        score["regulatory"] = ks["regulatory"]
    return {"score": score, "agent": ks.get("agent_readiness")}


def read_scores():
    """Read {slug: {composite, band}} from enriched provider frontmatter."""
    scores = {}
    if not os.path.isdir(PROVIDERS):
        return scores
    # Parse the whole `score:` block rather than matching a fixed key order.
    # score.rb has emitted both `composite`-first and alphabetical (`band`-first)
    # blocks; the old two-line regex silently dropped the alphabetical ones,
    # which sent an otherwise-scored provider to "Not Yet Rated" on every listing.
    for fname in os.listdir(PROVIDERS):
        if not fname.endswith(".md"):
            continue
        try:
            with open(os.path.join(PROVIDERS, fname), "r", encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
        except OSError:
            continue
        block = _fm_block(content, "score")
        if not isinstance(block, dict):
            continue
        composite, band = block.get("composite"), block.get("band")
        if composite is None or not band:
            continue
        scores[fname[:-3]] = {"composite": float(composite), "band": str(band)}
    # Gap-fill from the authoritative score files for any provider the mirror
    # has not caught up with yet. Never overwrites a value the mirror holds.
    for path in glob.glob(os.path.join(ALL, "*", "kin")):
        slug = os.path.basename(os.path.dirname(path))
        if slug in scores:
            continue
        blocks = _kin_score_blocks(slug)
        if not blocks or not blocks["score"].get("band"):
            continue
        scores[slug] = {"composite": float(blocks["score"]["composite"]),
                        "band": str(blocks["score"]["band"])}
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
    content = ""
    if os.path.isfile(path):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as fh:
                content = fh.read()
        except OSError:
            content = ""
    details = {
        "score": _fm_block(content, "score") if content else None,
        "agent": _fm_block(content, "agent_readiness") if content else None,
    }
    # Same gap-fill as read_scores: the facets and the twelve agent dimensions
    # are what every report's tables are built from, so a stale mirror would
    # silently drop a scored provider out of the analysis rather than the
    # listing. Each block falls back independently.
    if not isinstance(details["score"], dict) or not isinstance(details["agent"], dict):
        blocks = _kin_score_blocks(slug)
        if blocks:
            if not isinstance(details["score"], dict):
                details["score"] = blocks["score"]
            if not isinstance(details["agent"], dict) and blocks["agent"]:
                details["agent"] = blocks["agent"]
    if details["score"] or details["agent"]:
        _SCORE_DETAILS[slug] = details
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
# Rated entry + band grouping
# ---------------------------------------------------------------------------
# Shared by every rated listing (industries, countries, banks, sectors, market
# data, secondary market) so they all render the same Kin Score band-grouped
# layout via _includes/company-listing-rated.html. Module level rather than
# nested in main() so one section can be rebuilt on its own — main() is a
# single pass that rewrites every section it knows about, which is the wrong
# tool when only one listing needs refreshing.

def build_rated_entry(slug, meta, scores):
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


# The band a provider sits in comes from score.rb, which reads its thresholds from
# api-search/network/_data/scoring.yml. The RANGE LABEL printed beside each band on
# every rated listing used to be a second, hand-maintained copy of those thresholds
# here — and it drifted: the rubric was recalibrated (Exemplar 66+, Strong 56–65.9,
# Developing 42–55.9, Thin 28–41.9, Emerging 13–27.9) while this file kept printing
# the pre-calibration ladder (70+, 60–69.9, 45–59.9, 30–44.9, 15–29.9). Grouping was
# always right; the label under it was wrong on every section page. Read the ranges
# from the same file score.rb does so the two cannot disagree again.
SCORING_YML = os.path.join(ROOT, "api-search", "network", "_data", "scoring.yml")

# Bands (ids, labels, ranges) come from lib_bands, which reads the rubric — see that
# module for why no list of bands is retyped anywhere in this repo any more.
BAND_BLURBS = lib_bands.BAND_BLURBS


def band_ladder_from_scoring():
    """[(id, label, range, blurb), …] with ranges read from scoring.yml."""
    return lib_bands.band_ladder()


def band_grouped(entries):
    # Rating sort: scored providers by composite descending; unscored last,
    # alphabetically (unscored is "not yet rated", not a zero).
    entries.sort(key=lambda e: (-e.get("score", -1), e["name"].lower()))
    for rank, e in enumerate(entries, 1):
        e["rank"] = rank
    # Group by composite band, same ladder as apis.io/providers/. Only bands
    # with at least one member are emitted; the top two present open by default.
    band_ladder = band_ladder_from_scoring()
    groups = []
    for band, label, band_range, blurb in band_ladder:
        members = [e for e in entries if e.get("band", "unrated") == band or (band == "unrated" and "band" not in e)]
        if not members:
            continue
        # `count` is what the band really holds; `providers` is what the page
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


# ---------------------------------------------------------------------------
# Page templates
# ---------------------------------------------------------------------------
# (build_secondary_market / build_vcs are defined after these, since they use
# listing_page and write_page.)

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


# Tiers that are pulled OUT of the ranked Kin Score bands and listed as their
# own groups below them, keyed by the tier label the section builds. These are
# organizations that do not sell an API — they write the specification, run the
# rail, or supervise the market — so ranking them on a composite that measures
# a service is a category error. The order here is the order they render in.
#
# A section opts in by simply CONTAINING one of these tiers; nothing per-page
# needs to be declared. That matters because these pages are generated: the
# first pass of this treatment was hand-added to the front matter of 17 built
# pages, where the next rebuild would have silently reverted every one.
SEPARATED_TIER_BLURBS = [
    ("Standards Bodies",
     "They write the specifications, they do not sell an API — scored on a service rubric they were never built for."),
    ("Industry Bodies & Standards",
     "Trade bodies and standards organizations — they define how the sector exchanges data rather than selling an API."),
    ("Market Bodies & Standards",
     "Market bodies and standards organizations — they set the rules the banks clear through rather than selling an API."),
    ("Market Bodies, Standards & Regulators",
     "Market bodies, standards organizations and supervisors — not carriers, vendors or brokers."),
    ("Domestic Rails & Schemes",
     "The national payment rails and the bodies that write their rules — you join them as a participant, you do not call them as an API."),
    ("Regulators",
     "Supervisory and safety authorities, not commercial providers in this market."),
    ("Regulators & Government Data",
     "Supervisory bodies and government data publishers, not commercial providers in this market."),
]


def separated_tiers(entries, overrides=None):
    """(labels, blurbs) for the separable tiers this section actually holds."""
    present = {e["tier"] for e in entries if e.get("tier")}
    blurbs = dict(SEPARATED_TIER_BLURBS)
    blurbs.update(overrides or {})
    labels = [label for label, _ in SEPARATED_TIER_BLURBS if label in present]
    return labels, {label: blurbs[label] for label in labels}


# ---------------------------------------------------------------------------
# The interactive tools that sit above a ranked listing — "Pick your priorities"
# for buyers and "Find your opening" for providers — are NOT declared here. They
# are generated for every listing that sells a report by scripts/build-section-tools.py,
# which runs as a post-pass at the end of main(). Their card notes are computed
# from the cohort and the rubric, so a market with nothing unclaimed does not get
# sold one, and a truncated listing says it is truncated.
#
# TWO SIDES, DELIBERATELY EQUAL. A market report has a buy side and a sell side
# and both arrive on the same page. The listing include renders these as
# same-size cards rather than a primary button and a secondary link, so whoever
# lands here finds one addressed to them and neither reads as the afterthought.
# ---------------------------------------------------------------------------


def listing_page(title, summary, data_key, rated=False, paper=None,
                 papers=None, entries=None, tier_blurbs=None, tools=None):
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

    # Standards bodies, market bodies and regulators out of the ranked bands.
    if entries:
        labels, blurbs = separated_tiers(entries, tier_blurbs)
        if labels:
            lines.append("separate_tiers:")
            lines += ['  - "%s"' % label for label in labels]
            lines.append("tier_blurbs:")
            lines += ['  %s: "%s"' % (label, blurbs[label]) for label in labels]

    body = []
    # Optional sector-report promo band (see _includes/paper-promo.html). Emitted
    # here so it survives every rebuild rather than being hand-added to the page.
    # `papers` (several) wins over `paper` (one) — the include accepts either.
    promo = papers if papers else ([paper] if paper else [])
    if promo:
        if papers:
            lines.append("papers:")
            for p in papers:
                lines += [
                    "  - slug: %s" % p["slug"],
                    '    title: "%s"' % p["title"],
                    '    blurb: "%s"' % p["blurb"].replace('"', "'"),
                    '    price: "%s"' % p.get("price", "500"),
                ]
                if p.get("kind"):
                    lines.append('    kind: "%s"' % p["kind"])
        else:
            lines += [
                "paper:",
                "  slug: %s" % paper["slug"],
                '  title: "%s"' % paper["title"],
                '  blurb: "%s"' % paper["blurb"].replace('"', "'"),
                '  price: "%s"' % paper.get("price", "500"),
            ]
            if paper.get("kind"):
                lines.append('  kind: "%s"' % paper["kind"])
        body.append("{% include paper-promo.html %}")

    # Interactive tools band. Only build-section-tools.py passes these; see the
    # note above listing_page() for why they are generated as a post-pass.
    if tools:
        lines.append("tools:")
        for t in tools:
            lines.append('  - side: "%s"' % esc(t["side"]))
            lines.append('    label: "%s"' % esc(t["label"]))
            for key in ("icon", "blurb", "note", "url", "report"):
                if t.get(key):
                    lines.append('    %s: "%s"' % (key, esc(t[key])))

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
# Roster-driven sections
# ---------------------------------------------------------------------------
# Every sector page (banking, payments, healthcare, insurance, real estate,
# energy, travel, telecom, headless, market data) is a curated roster in
# all/0-working/<name>-roster.json with a tier per provider. Module level so a
# single sector can be rebuilt without running the whole file.
#
# A section spec is (slug_page, roster_file, title, summary, paper) with an
# optional 6th element carrying extras:
#   tier_labels : per-section tier vocabulary, when the group's shared one
#                 does not apply (banking has three different taxonomies)
#   papers      : several promo papers instead of one
#   tier_blurbs : override a separated tier's blurb for this section

def build_roster_section_group(data_dir, meta_of, scores, sections,
                               tier_labels, counts=None):
    counts = {} if counts is None else counts
    for spec in sections:
        slug_page, roster_file, title, summary, paper = spec[:5]
        extras = spec[5] if len(spec) > 5 else {}
        labels = extras.get("tier_labels") or tier_labels

        with open(os.path.join(ALL, "0-working", roster_file), "r", encoding="utf-8") as fh:
            roster = json.load(fh)

        entries = []
        for p in roster["providers"]:
            meta = meta_of(p["slug"])
            if meta is None:
                continue
            entry = build_rated_entry(p["slug"], meta, scores)
            tier = p.get("tier", "")
            if tier:
                entry["tier"] = labels.get(tier, titleize(tier))
            entries.append(entry)

        data_key = "providers-%s" % slug_page
        with open(os.path.join(data_dir, "%s.json" % data_key), "w", encoding="utf-8") as fh:
            json.dump(band_grouped(entries), fh, ensure_ascii=False, indent=1)

        write_page(
            os.path.join(SITE, slug_page, "index.html"),
            listing_page(title, summary, data_key, rated=True, paper=paper,
                         papers=extras.get("papers"), entries=entries,
                         tier_blurbs=extras.get("tier_blurbs")),
        )
        counts[slug_page] = (len(entries), sum(1 for e in entries if "score" in e))
    return counts


# ---------------------------------------------------------------------------
# Capital-market collections
# ---------------------------------------------------------------------------
# Two rosters that file providers by how their EQUITY trades rather than by
# what they sell: the private-market venues that list their shares, and the
# venture firms that own them. Both are maintained for the apis.io sibling
# sites (secondary-market.apis.io, vcs.apis.io) and mirrored onto the
# providers site so the same cohorts carry a Kin Score reading.

def build_secondary_market(data_dir, meta_of, scores):
    """Providers whose private shares are listed on the secondary venues.

    Forge Global, Hiive, EquityZen, Nasdaq Private Market, Augment. Every
    entry in the roster is already an all/* provider, so this is an ordinary
    Kin Score listing, with the number of venues a company is listed on
    carried as the row's tier badge. A pre-IPO company answering diligence
    questions about its API is exactly the cohort the score describes.

    Returns the entry list so the caller can report on it.
    """
    path = os.path.join(ROOT, "api-search", "secondary-market", "_data", "secondary_market.yml")
    with open(path, "r", encoding="utf-8") as fh:
        roster = yaml.safe_load(fh) or {}

    entries = []
    for c in roster.get("companies") or []:
        meta = meta_of(c["slug"])
        if meta is None:
            continue
        entry = build_rated_entry(c["slug"], meta, scores)
        venues = c.get("venue_count") or len(c.get("venues") or [])
        if venues:
            entry["tier"] = "%d venue%s" % (venues, "" if venues == 1 else "s")
        entries.append(entry)

    with open(os.path.join(data_dir, "providers-secondary-market.json"), "w", encoding="utf-8") as fh:
        json.dump(band_grouped(entries), fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "secondary-market", "index.html"),
        listing_page(
            "Secondary Market",
            esc("%d providers whose private shares are listed on the %d secondary venues — Forge Global, Hiive, EquityZen, Nasdaq Private Market and Augment — ranked by their Kin Score."
                % (len(entries), len(roster.get("venues") or {}))),
            "providers-secondary-market",
            rated=True,
        ),
    )
    return entries


def build_vcs(data_dir, delisted):
    """Venture and growth firms ranked by portfolio strength.

    A venture firm has no API and therefore no Kin Score of its own, so this
    listing deliberately does NOT use the rated provider include. Firms are
    ranked by portfolio strength — the same tier-weighted rollup vcs.apis.io
    ranks by — and the band on each row is the firm's PORTFOLIO rating band,
    not a score for the firm. Source is api-search/vcs/_data/vcs.yml, which
    the VC pipeline rebuilds whenever portfolios are re-matched against the
    network.

    Returns the entry list so the caller can report on it.
    """
    path = os.path.join(ROOT, "api-search", "vcs", "_data", "vcs.yml")
    with open(path, "r", encoding="utf-8") as fh:
        roster = yaml.safe_load(fh) or {}

    entries = []
    for v in roster.get("vcs") or []:
        slug = v["slug"]
        if slug in delisted:
            continue
        band = v.get("rating_band") or "unrated"
        entry = {
            "slug": slug,
            "name": v.get("name") or titleize(slug),
            "description": " ".join((v.get("description") or "").split()),
            "strength": v.get("strength") or 0,
            "rating": v.get("rating"),
            "band": band,
            "band_label": BAND_LABELS.get(band, band.title()),
            "portfolio_total": v.get("portfolio_total") or 0,
            "portfolio_on_network": v.get("portfolio_on_network") or 0,
            "top_tier": (v.get("rating_exemplar") or 0) + (v.get("rating_strong") or 0),
            "agent_tier": (v.get("rating_agent_native") or 0) + (v.get("rating_agent_ready") or 0),
        }
        shot = newest_screenshot(slug)
        if shot:
            entry["screenshot"] = shot
        entries.append(entry)

    entries.sort(key=lambda e: (-e["strength"], e["name"].lower()))
    for rank, e in enumerate(entries, 1):
        e["rank"] = rank

    with open(os.path.join(data_dir, "providers-vcs.json"), "w", encoding="utf-8") as fh:
        json.dump({
            "total": len(entries),
            "portfolio_companies": roster.get("portfolio_companies") or 0,
            "on_network": roster.get("on_network") or 0,
            "vcs": entries,
        }, fh, ensure_ascii=False, indent=1)

    write_page(
        os.path.join(SITE, "vcs", "index.html"),
        "\n".join([
            "---",
            "layout: default",
            "section: Providers",
            'title: "Venture Capital"',
            'summary: "%d venture capital firms ranked by portfolio strength — how many of the companies they backed publish APIs that score well on the Kin Score."' % len(entries),
            "nav: Providers",
            'data_key: "providers-vcs"',
            # Promoted here rather than by build-section-tools.py: that pass only
            # handles listings whose data is band-grouped, and this page is a
            # portfolio roll-up with no Kin Score of its own. It gets the promo
            # band, and deliberately no buyer/provider tools — there is no cohort
            # under it for them to read.
            "papers:",
            "  - slug: agentic-readiness-of-venture",
            '    title: "The Agentic Readiness of Venture"',
            '    blurb: "The twenty-five most important venture funds, ranked on one axis '
            '— whether their portfolios are ready for agents that act."',
            '    price: "1,500"',
            '    kind: "API Evangelist Trend Report"',
            "---",
            "{% include paper-promo.html %}",
            "{% include vc-listing.html %}",
            "",
        ]),
    )
    return entries


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
    # Both live at module level (see rated_entry/band_grouped above) so a
    # single section can be rebuilt on its own without running the whole file.
    # Bound here to this run's score table.

    def rated_entry(slug, meta):
        return build_rated_entry(slug, meta, scores)

    def build_roster_sections(sections, tier_labels, counts):
        build_roster_section_group(data_dir, meta_of, scores, sections, tier_labels, counts)

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
        published = []
        for spec in TAG_INDUSTRIES:
            rec = dict(spec)
            if TAG_INDUSTRY_EXCLUDE.get(spec["slug"]):
                rec["exclude"] = sorted(TAG_INDUSTRY_EXCLUDE[spec["slug"]])
            if TAG_INDUSTRY_INCLUDE.get(spec["slug"]):
                rec["include"] = sorted(TAG_INDUSTRY_INCLUDE[spec["slug"]])
            published.append(rec)
        yaml.safe_dump(published, fh, sort_keys=False, allow_unicode=True, width=10000)

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
                if repo in TAG_INDUSTRY_EXCLUDE.get(slug, ()):
                    continue
                industries[slug]["providers"].add(repo)

    for slug, extra in TAG_INDUSTRY_INCLUDE.items():
        if slug not in industries:
            continue
        for repo in extra:
            if os.path.isdir(os.path.join(ALL, repo)) and meta_of(repo) is not None:
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
                paper=INDUSTRY_PAPERS.get(ind_slug),
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

    # --- Banking (UK / US / CA) -------------------------------------------
    # Roster-driven, one taxonomy per market: British banking is organized by
    # the CMA9 mandate, American banking by charter class and the BaaS layer,
    # Canadian banking by the Bank Act schedules. Each market therefore carries
    # its own tier vocabulary rather than a shared one.
    #
    # Australian banking is deliberately absent: that page is tag-derived
    # (Australia + Banks) rather than roster-curated, and is built above.
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
    US_TIER_LABELS = {
        "money-center":    "Money-Center & Custody",
        "super-regional":  "Super-Regional",
        "regional":        "Regional",
        "digital":         "Digital & Neobank",
        "baas":            "Banking-as-a-Service",
        "credit-union":    "Credit Union",
        # FDX used to sit inside this tier, which is why it read "Aggregator &
        # FDX". It is a standards body, not an aggregator: it publishes the FDX
        # API specification the aggregators implement, and it sells nothing.
        "aggregator":      "Aggregators & Open Finance",
        "standards-body":  "Industry Bodies & Standards",
    }
    CA_TIER_LABELS = {
        "big-six":          "Big Six",
        "schedule-i":       "Schedule I (Domestic)",
        "schedule-ii":      "Schedule II (Foreign-Owned)",
        "digital-arm":      "Digital Arm",
        "provincial-crown": "Provincial / Crown",
        "credit-union":     "Credit Union & Caisse",
        "fintech":          "Fintech & Challenger",
        # Interac and Moneris sell services; Payments Canada is the statutory
        # body that operates Lynx and the Real-Time Rail and writes the ISO
        # 20022 rules the banks clear through. Different thing, different tier.
        "infrastructure":   "Payments & Infrastructure",
        "market-body":      "Market Bodies & Standards",
    }
    BANK_SECTIONS = [
        ("uk-banks", "uk-banks-roster.json", "UK Banking",
         "UK banks and building societies ranked by their Kin Score, from the CMA9 Open Banking mandate to challengers, building societies, and private banks.",
         {"slug": "state-of-uk-banking-apis", "title": "The State of UK Banking APIs",
          "blurb":
          "What sixty UK banks and building societies actually publish, scored — "
          "from the CMA9 Open Banking mandate to the challengers, building "
          "societies, and private banks around it.", "price": "500"},
         {"tier_labels": UK_TIER_LABELS}),
        ("us-banks", "us-banks-roster.json", "US Banking",
         "US banks, credit unions, neobanks, and banking-as-a-service providers ranked by their Kin Score — from the money-center banks and the BaaS layer to the aggregators wiring the CFPB 1033 / FDX open-finance era.",
         {"slug": "state-of-us-banking-apis", "title": "The State of US Banking APIs",
          "blurb":
          "What 113 US banks, credit unions, neobanks, and banking-rails providers "
          "actually publish, scored — the one open-finance market with no mandate, "
          "and the widest split in banking.", "price": "500"},
         {"tier_labels": US_TIER_LABELS}),
        ("canadian-banks", "canadian-banks-roster.json", "Canadian Banking",
         "Canadian banks, credit unions and caisses, and fintechs ranked by their Kin Score — the Big Six, the digital arms, and the challengers, ahead of Canada's Consumer-Driven Banking framework.",
         {"slug": "state-of-canadian-banking-apis", "title": "The State of Canadian Banking APIs",
          "blurb":
          "What 42 Canadian banks, credit unions, caisses, and fintechs actually "
          "publish, scored — the emptiest banking market measured, where the rails "
          "outrank the banks.", "price": "500"},
         {"tier_labels": CA_TIER_LABELS}),
    ]
    bank_counts = {}
    build_roster_sections(BANK_SECTIONS, {}, bank_counts)

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
         None,
         # Two papers, and a regulator blurb specific to this sector: telecom's
         # supervisors are the ones who conspicuously do NOT require the network
         # capability that CAMARA standardizes to be exposed at all.
         {"papers": [
             {"slug": "state-of-telecom-apis", "title": "The State of Telecom APIs",
              "blurb": "83 telecom organizations scored — the only sector with a real, industry-built API standard, and the widest gap in the series between signing it and shipping it. The aggregators that resell carrier connectivity out-publish their own suppliers by 19 points, and the standards bodies out-publish the carriers that wrote the standards.", "price": "500"},
             {"slug": "the-camara-standard", "title": "The CAMARA Standard",
              "kind": "API Evangelist Standard Report",
              "blurb": "The standard itself, taken apart: 93 repositories in which 57 are Sandbox, 15 Incubating and none Graduated; 1,369 named participants across 487 organizations mapped for the first time; and exactly one operator on earth publishing a contract a developer can download, price and call self-serve.", "price": "500"},
          ],
          "tier_blurbs": {
             "Regulators": "Supervisory bodies. None of them requires an operator to expose network capability as an API.",
          }}),
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

    # --- Management (single GLOBAL cohort, the first AREA cut) ------------
    # The first section anchored to an API Evangelist AREA rather than an
    # industry or a country: management.apievangelist.com, read as a market.
    # An industry says who a company sells to; an area says what the API does.
    #
    # COHORT IS HAND-NAMED. API management is a fuzzy category and no
    # automated rule draws its edge correctly — tag matching returns 6
    # providers for this area and 14 for gateway, because Kong and Apigee
    # carry the category in API-level tags the provider roll-up never reads,
    # while a looser read pulls in half a dozen adjacent markets. So the 36
    # in all/0-working/management-roster.json are named by hand and the
    # boundary is stated as editorial.
    #
    # 36 vendors. Two tiers, both factual rather than editorial: does the
    # vendor sell the whole lifecycle as a product, or is it the data plane
    # you put in front of an API. Portals and docs, metering and billing, analytics and
    # observability, API security and service mesh are REAL adjacent markets
    # and are covered in their own areas, not folded in here.
    MANAGEMENT_TIER_LABELS = {
        "platform": "Full-Stack API Management Platforms",
        "gateway":  "Gateways, Ingress and the Data Plane",
    }

    # --- Programmable Revenue + Programmable Marketing -------------------
    # Roster-driven from the planning cohorts, which are built on four axes
    # (domain / confidence / liveness / vertical) with a two-tier tag boundary —
    # a filter no tag match can express. Rebuild with:
    #   python3 planning/<cohort>/pipeline/area_spine.py
    #   python3 planning/build_rosters.py
    # The roll-up pages tier by function area so a reader sees immediately that
    # each is many markets; the marketing area pages tier by buy/sell side.
    PROGRAMMABLE_TIER_LABELS = {
        "buy-side": "Sold to the advertiser (buy side)",
        "sell-side": "Sold to the publisher (sell side)",
        "both-sides": "Sold to both sides",
    }
    PROGRAMMABLE_SECTIONS = [
        ("programmable-revenue", "state-of-revenue-apis-roster.json", "Programmable Revenue",
         "Programmable Revenue providers ranked by their Kin Score. 517 companies, 300 (58%) publishing a machine-readable contract, 238 (46%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-revenue-apis", "title": "The State of Revenue APIs",
          "blurb": "517 companies scored, every one named and banded. Kin Score median 53.8, Agent Readiness median 48.0. This market has made itself readable by machines and has not made itself operable by them. Fifty-eight percent publish a contract and forty-six percent run their own MCP server, both high figures by any standard in the catalog. Zero describe a workflow. The distance between those two facts is the whole opportunity.", "price": "500"}),
        ("data-prospecting", "state-of-data-prospecting-apis-roster.json", "Data & Prospecting",
         "Data & Prospecting providers ranked by their Kin Score. 234 companies, 142 (61%) publishing a machine-readable contract, 118 (50%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-data-prospecting-apis", "title": "The State of Data and Prospecting APIs",
          "blurb": "234 companies scored, every one named and banded. Kin Score median 55.5, Agent Readiness median 49.1. This area publishes contracts at a higher rate than the market around it and still fails every delegation dimension. The data moves; the permission to act on it does not.", "price": "500"}),
        ("engagement-outreach", "state-of-engagement-outreach-apis-roster.json", "Engagement & Outreach",
         "Engagement & Outreach providers ranked by their Kin Score. 221 companies, 148 (67%) publishing a machine-readable contract, 104 (47%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-engagement-outreach-apis", "title": "The State of Engagement and Outreach APIs",
          "blurb": "221 companies scored, every one named and banded. Kin Score median 59.8, Agent Readiness median 50.9. Sixty-seven percent publish a contract — the highest of any large area in this report. Ninety percent cannot tell an agent whether a call was already made.", "price": "500"}),
        ("pipeline-forecast", "state-of-pipeline-forecast-apis-roster.json", "Pipeline & Forecast",
         "Pipeline & Forecast providers ranked by their Kin Score. 178 companies, 93 (52%) publishing a machine-readable contract, 77 (43%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-pipeline-forecast-apis", "title": "The State of Pipeline and Forecast APIs",
          "blurb": "178 companies scored, every one named and banded. Kin Score median 51.6, Agent Readiness median 46.8. This is the most connected software in go-to-market and it sits 1.2 points below the market median on Agent Readiness. Being integrated by everyone is not the same as being operable by anything.", "price": "500"}),
        ("conversation-coaching", "state-of-conversation-coaching-apis-roster.json", "Conversation & Coaching",
         "Conversation & Coaching providers ranked by their Kin Score. 122 companies, 56 (46%) publishing a machine-readable contract, 58 (48%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-conversation-coaching-apis", "title": "The State of Conversation and Coaching APIs",
          "blurb": "122 companies scored, every one named and banded. Kin Score median 45.7, Agent Readiness median 38.0. The weakest area in revenue software, and it holds at full coverage. Governance averages 18.1 in the market that holds recordings of every customer conversation.", "price": "500"}),
        ("revenue-plumbing", "state-of-plumbing-apis-roster.json", "Revenue Plumbing",
         "Revenue Plumbing providers ranked by their Kin Score. 66 companies, 46 (70%) publishing a machine-readable contract, 35 (53%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-plumbing-apis", "title": "The State of Revenue Plumbing APIs",
          "blurb": "66 companies scored, every one named and banded. Kin Score median 60.5, Agent Readiness median 52.7. The best-scoring area in revenue software on every artifact measure, and it fails consent and idempotency at 91% each. Even the market's integration specialists have not built for a caller that acts on someone else's behalf.", "price": "500"}),
        ("quote-to-cash", "state-of-quote-to-cash-apis-roster.json", "Quote-to-Cash",
         "Quote-to-Cash providers ranked by their Kin Score. 23 companies, 15 (65%) publishing a machine-readable contract, 10 (43%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-quote-to-cash-apis", "title": "The State of Quote-to-Cash APIs",
          "blurb": "23 companies scored, every one named and banded. Kin Score median 57.0, Agent Readiness median 52.7. Twenty-three companies, scoring above the market on every artifact measure and failing consent at 96%. The step immediately before money moves is the step least prepared to be delegated.", "price": "500"}),
        ("retention-expansion", "state-of-retention-expansion-apis-roster.json", "Retention & Expansion",
         "Retention & Expansion providers ranked by their Kin Score. 20 companies, 10 (50%) publishing a machine-readable contract, 7 (35%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-retention-expansion-apis", "title": "The State of Retention and Expansion APIs",
          "blurb": "20 companies scored, every one named and banded. Kin Score median 49.4, Agent Readiness median 40.3. Twenty companies, and four of the market's own core terms carry no company at all. This is the one area in the report where coverage is a live question.", "price": "500"}),
        ("programmable-marketing", "state-of-marketing-apis-roster.json", "Programmable Marketing",
         "Programmable Marketing providers ranked by their Kin Score. 814 companies, 419 (51%) publishing a machine-readable contract, 301 (37%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-marketing-apis", "title": "The State of Marketing APIs",
          "blurb": "814 companies scored, every one named and banded. Kin Score median 49.1, Agent Readiness median 42.7. The strongest divide in marketing software is not category, it is customer. Software sold to the advertiser scores 53.3; software sold to the publisher scores 39.0. Both sides run the same real-time auctions against each other. One of them documents how.", "price": "500"}),
        ("marketing-orchestration", "state-of-orchestration-apis-roster.json", "Marketing Orchestration",
         "Marketing Orchestration providers ranked by their Kin Score. 551 companies, 278 (50%) publishing a machine-readable contract, 191 (35%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-orchestration-apis", "title": "The State of Marketing Orchestration APIs",
          "blurb": "551 companies scored, every one named and banded. Kin Score median 48.9, Agent Readiness median 41.9. The area that automates marketing scores at the marketing average. Orchestration software that cannot itself be orchestrated is the clearest irony in this research.", "price": "500"}),
        ("audience-measurement", "state-of-audience-measurement-apis-roster.json", "Audience & Measurement",
         "Audience & Measurement providers ranked by their Kin Score. 263 companies, 157 (60%) publishing a machine-readable contract, 115 (44%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-audience-measurement-apis", "title": "The State of Audience and Measurement APIs",
          "blurb": "263 companies scored, every one named and banded. Kin Score median 54.8, Agent Readiness median 48.2. One of marketing's strongest areas, with an eleven-point buy/sell split inside a single function. The same capability, measured differently depending on who pays for it.", "price": "500"}),
        ("paid-media-buy-side", "state-of-paid-media-buy-side-apis-roster.json", "Paid Media — Buy Side",
         "Paid Media — Buy Side providers ranked by their Kin Score. 252 companies, 100 (40%) publishing a machine-readable contract, 76 (30%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-paid-media-buy-side-apis", "title": "The State of Paid Media APIs — The Buy Side",
          "blurb": "252 companies scored, every one named and banded. Kin Score median 35.7, Agent Readiness median 30.1. This market transacts entirely by machine and describes itself to the outside world less than almost any other. The bid stream is a specification. The platform is not.", "price": "500"}),
        ("sales-handoff", "state-of-the-sales-handoff-apis-roster.json", "The Sales Handoff",
         "The Sales Handoff providers ranked by their Kin Score. 156 companies, 86 (55%) publishing a machine-readable contract, 69 (44%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-the-sales-handoff-apis", "title": "The State of the Sales Handoff APIs",
          "blurb": "156 companies scored, every one named and banded. Kin Score median 53.6, Agent Readiness median 48.6. The area that connects the two cohorts in this research scores like the stronger one. Software defined by a handoff gets good at handing off.", "price": "500"}),
        ("where-the-spend-lands", "state-of-where-the-spend-lands-apis-roster.json", "Where the Spend Lands",
         "Where the Spend Lands providers ranked by their Kin Score. 146 companies, 79 (54%) publishing a machine-readable contract, 50 (34%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-where-the-spend-lands-apis", "title": "The State of Where the Spend Lands",
          "blurb": "146 companies scored, every one named and banded. Kin Score median 48.8, Agent Readiness median 44.2. The newest money in marketing arrives on the least described surfaces. Retail media grew into a major channel without building a public interface layer.", "price": "500"}),
        ("owned-channels", "state-of-owned-channels-apis-roster.json", "Owned Channels",
         "Owned Channels providers ranked by their Kin Score. 135 companies, 90 (67%) publishing a machine-readable contract, 60 (44%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-owned-channels-apis", "title": "The State of Owned Channel APIs",
          "blurb": "135 companies scored, every one named and banded. Kin Score median 60.2, Agent Readiness median 50.9. The strongest area in marketing, built by companies whose product was always an interface. Even here, delegation is missing at over eighty percent.", "price": "500"}),
        ("earned-social", "state-of-earned-social-apis-roster.json", "Earned & Social",
         "Earned & Social providers ranked by their Kin Score. 116 companies, 52 (45%) publishing a machine-readable contract, 41 (35%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-earned-social-apis", "title": "The State of Earned and Social APIs",
          "blurb": "116 companies scored, every one named and banded. Kin Score median 44.9, Agent Readiness median 35.8. The one area in this report where a low score is partly not the company's fault — and one of only two where the sell side outscores the buy side.", "price": "500"}),
        ("content-brand", "state-of-content-brand-apis-roster.json", "Content & Brand",
         "Content & Brand providers ranked by their Kin Score. 115 companies, 49 (43%) publishing a machine-readable contract, 42 (37%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-content-brand-apis", "title": "The State of Content and Brand APIs",
          "blurb": "115 companies scored, every one named and banded. Kin Score median 44.5, Agent Readiness median 34.7. The lowest governance figure in marketing, in the area whose entire product is an asset other systems depend on retrieving.", "price": "500"}),
        ("demand-capture", "state-of-demand-capture-apis-roster.json", "Demand Capture",
         "Demand Capture providers ranked by their Kin Score. 115 companies, 67 (58%) publishing a machine-readable contract, 51 (44%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-demand-capture-apis", "title": "The State of Demand Capture APIs",
          "blurb": "115 companies scored, every one named and banded. Kin Score median 57.2, Agent Readiness median 47.7. The second-strongest area in marketing, and the one where the product only works if the handoff works. Programmability here is not a virtue, it is the business model.", "price": "500"}),
        ("paid-media-sell-side", "state-of-paid-media-sell-side-apis-roster.json", "Paid Media — Sell Side",
         "Paid Media — Sell Side providers ranked by their Kin Score. 104 companies, 40 (38%) publishing a machine-readable contract, 25 (24%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-paid-media-sell-side-apis", "title": "The State of Paid Media APIs — The Sell Side",
          "blurb": "104 companies scored, every one named and banded. Kin Score median 34.0, Agent Readiness median 26.6. The lowest scores in either cohort, and the clearest single finding in this research: the side of the transaction with no customer demanding transparency did not build any.", "price": "500"}),
        ("retention-advocacy", "state-of-retention-advocacy-apis-roster.json", "Retention & Advocacy",
         "Retention & Advocacy providers ranked by their Kin Score. 56 companies, 32 (57%) publishing a machine-readable contract, 18 (32%) running their own MCP server, and 0 describing a multi-step workflow.",
         {"slug": "state-of-retention-advocacy-apis", "title": "The State of Retention and Advocacy APIs",
          "blurb": "56 companies scored, every one named and banded. Kin Score median 49.1, Agent Readiness median 47.1. The tightest Kin-to-Agent-Readiness gap in either cohort. What these companies publish, an agent can mostly use — there is simply not very much of it.", "price": "500"}),
    ]
    programmable_counts = {}
    build_roster_sections(PROGRAMMABLE_SECTIONS, PROGRAMMABLE_TIER_LABELS, programmable_counts)

    MANAGEMENT_SECTIONS = [
        ("management", "management-roster.json", "API Management",
         "The API management market ranked by Kin Score — the 21 full-stack platforms that sell the whole lifecycle as one product (Apigee, Boomi, Kong, MuleSoft, IBM API Connect, Axway, Azure API Management, WSO2, Tyk, Gravitee, Zuplo, Red Hat 3scale, SAP, TIBCO, Software AG, Broadcom, APIwiz, APIIDA, APIPark, Apiman, Apidog) and the 15 gateways, ingress controllers and data planes you put in front of an API (Amazon API Gateway, Google Cloud API Gateway, NGINX, Traefik, Envoy, Envoy Gateway, Apache APISIX, KrakenD, Higress, Solo.io, Emissary-Ingress, Spring Cloud Gateway, Netflix Zuul, Apinizer, Bifrost). API management is a fuzzy category, so this cohort is named by hand rather than matched — developer portals, documentation, metering, analytics, API security and service mesh are real adjacent markets and are covered in their own areas.",
         {"slug": "state-of-management-apis", "title": "The State of API Management",
          "blurb": "36 API management vendors scored — the market that sells other people their API practice, measured on its own rubric. The cohort averages 53.9 against a whole-catalog average of 22.6, and 33.1 on agent readiness. Solo.io leads at 80.8 on the composite and 59.5 on agents; Apigee scores 74.0 and 30.6. Not one vendor of 36 signals idempotency, in the market that sells you the gateway where you would implement it.", "price": "500"},
         {"papers": [{"slug": "state-of-management-apis", "title": "The State of API Management",
          "blurb": "36 API management vendors scored — the market that sells other people their API practice, measured on its own rubric. The cohort averages 53.9 against a whole-catalog average of 22.6, and 33.1 on agent readiness. Solo.io leads at 80.8 on the composite and 59.5 on agents; Apigee scores 74.0 and 30.6. Not one vendor of 36 signals idempotency, in the market that sells you the gateway where you would implement it.", "price": "500"}, SPECTRAL_PAPER]}),
    ]
    management_counts = {}
    build_roster_sections(MANAGEMENT_SECTIONS, MANAGEMENT_TIER_LABELS, management_counts)

    # --- Documentation (single GLOBAL cohort, the second AREA cut) --------
    # The second section anchored to an API Evangelist AREA rather than an
    # industry or a country: documentation.apievangelist.com, read as a market.
    #
    # COHORT IS HAND-NAMED, same as management. The tag roll-up reports 87
    # providers for this area, which is a looser and different set than the
    # market. The 29 in all/0-working/documentation-roster.json are named by
    # hand from the 41 curated slugs on the area subsite, and the boundary is
    # stated as editorial in the report.
    #
    # Three tiers, and they are commercial rather than editorial — what a
    # buyer actually procures: a hosted platform you buy, a reference renderer
    # you embed, or a static site generator you build with. The ladder runs
    # monotonically down both the composite and agent-readiness axes.
    #
    # Four adjacent markets are deliberately OUT, each covered in its own
    # area: SDK-generation platforms that also ship docs sites (Fern,
    # Speakeasy, Stainless, Sideko, APIMatic, liblab, Konfig) belong to the
    # SDK area; API clients that render documentation (Postman, Apidog,
    # Insomnia, Bruno, Hoppscotch) sell a client, on the same reasoning that
    # kept Postman out of the management cohort; linting and governance
    # (Spectral, vacuum, Optic, TypeSpec) belong to design and governance; and
    # internal developer portals (Backstage, Cortex, Port) catalog services
    # rather than document APIs. Duplicate company repos are resolved to the
    # richer survivor (readmeio -> readme) so this counts companies.
    DOCUMENTATION_TIER_LABELS = {
        "platform": "Hosted Documentation Platforms",
        "renderer": "API Reference Renderers",
        "ssg":      "Docs-as-Code Static Site Generators",
    }
    DOCUMENTATION_SECTIONS = [
        ("documentation", "documentation-roster.json", "API Documentation",
         "The API documentation market ranked by Kin Score — the 15 hosted platforms you buy (SwaggerHub, ReadMe, Mintlify, Document360, Theneo, Bump.sh, Archbee, Redocly, GitBook, Stoplight, Doctave, DeveloperHub, ApiNotes, Apiary, zeroheight), the 8 reference renderers you embed (Scalar, Stoplight Elements, Zudoku, RapiDoc, ReDoc, Slate, Swagger UI, DapperDox), and the 6 docs-as-code static site generators you build with (Fumadocs, Nextra, VitePress, Docusaurus, MkDocs, Docsify). Documentation is a fuzzy category, so this cohort is named by hand rather than matched — SDK generators, API clients, linting and governance tooling, and internal developer portals are real adjacent markets and are covered in their own areas.",
         {"slug": "state-of-documentation-apis", "title": "The State of API Documentation",
          "blurb": "29 API documentation vendors and projects scored — the market whose entire job is making APIs legible, measured on whether its own products are. Developer ergonomics is the cohort's weakest facet at 25.6, in the market that sells developer experience. Four vendors sell MCP servers and AI search to their customers; none of the 29 runs one. One provider in 29 clears the Exemplar line, by three tenths of a point.", "price": "500"}),
    ]
    documentation_counts = {}
    build_roster_sections(DOCUMENTATION_SECTIONS, DOCUMENTATION_TIER_LABELS, documentation_counts)

    # --- Testing (single GLOBAL cohort, the third AREA cut) --------------
    # testing.apievangelist.com read as a market, and the FUZZIEST area cut
    # attempted — the curated index names seven sub-markets, so the tiers are
    # drawn by WHAT THE TOOL DOES rather than by who sells it.
    #
    # COHORT IS HAND-NAMED. Security scanners and browser/E2E frameworks are
    # IN: the area's own description explicitly names security testing
    # scanners, and E2E frameworks test the system an API serves. API CLIENTS
    # ARE OUT — Postman, Insomnia, Bruno, Hoppscotch and HTTPie sell a client,
    # on the same reasoning that kept Postman out of the management and
    # documentation cohorts. That is a scope call, not a delisting.
    #
    # Three catalog problems were resolved before any figure was computed and
    # they are worth recording here because each would have been invisible in
    # the output: (1) `cypress` is CYPRESS SEMICONDUCTOR, the San Jose chip
    # company acquired by Infineon, not the testing framework — the framework
    # is `cypressio`, and using the obvious slug would have dropped a defunct
    # semiconductor manufacturer into an API testing report; (2) `jmeter`
    # (20.4) and `apache-jmeter` (50.3) are one project, a 30-point spread and
    # the widest duplicate found in the series; (3) ReadyAPI is a SmartBear
    # PRODUCT with an empty record, not a company, and folds into SmartBear.
    # StormForge was dropped on inspection — it is Kubernetes cost rightsizing,
    # not testing. Roster: all/0-working/testing-roster.json.
    TESTING_TIER_LABELS = {
        "commercial": "Commercial Testing & Quality Platforms",
        "mock":       "Mocking & Service Virtualization",
        "load":       "Load & Performance Testing",
        "contract":   "Contract Testing & Test Frameworks",
        "security":   "Security Testing Scanners",
        "e2e":        "Browser & End-to-End Frameworks",
    }
    TESTING_SECTIONS = [
        ("testing", "testing-roster.json", "API Testing",
         "The API testing market ranked by Kin Score — the commercial testing and quality platforms (Tricentis, SmartBear, APIToolkit, Checkly, Assertible, Speedscale), the mocking and service-virtualization layer (WireMock, Beeceptor, Microcks, Mockoon, MockAPI, MockServer, Mock Service Worker, Hoverfly, Prism), load and performance testing (Apache JMeter, k6, Vegeta, Artillery, GoReplay, Gatling, Locust), contract testing and test frameworks (REST Assured, Pact, SuperTest, Schemathesis, Step CI, Optic, Dredd, Portman, Karate, Newman), the security scanners (Nuclei, OWASP ZAP) and the browser and end-to-end frameworks (Cypress.io, Selenium, Playwright). Testing is the fuzziest category in the series, so this cohort is named by hand rather than matched — API clients, chaos engineering, observability and APM are real adjacent markets covered in their own areas.",
         {"slug": "state-of-testing-apis", "title": "The State of API Testing",
          "blurb": "37 API testing tools and platforms scored — and the first market in this series that is actually building for agents. Four vendors ship a real MCP server after three consecutive cohorts shipped none, and Tricentis posts a 1.1-point gap between its composite and its agent readiness where every previous market leader posted thirty or more. It is also the weakest-scoring cohort measured: no Exemplar, and governance at 20.9 with 24 of 37 at zero.", "price": "500"},
         {"papers": [{"slug": "state-of-testing-apis", "title": "The State of API Testing",
          "blurb": "37 API testing tools and platforms scored — and the first market in this series that is actually building for agents. Four vendors ship a real MCP server after three consecutive cohorts shipped none, and Tricentis posts a 1.1-point gap between its composite and its agent readiness where every previous market leader posted thirty or more. It is also the weakest-scoring cohort measured: no Exemplar, and governance at 20.9 with 24 of 37 at zero.", "price": "500"}, SPECTRAL_PAPER]}),
    ]
    testing_counts = {}
    build_roster_sections(TESTING_SECTIONS, TESTING_TIER_LABELS, testing_counts)

    # --- API Clients (single GLOBAL cohort, the fourth AREA cut) ----------
    # api-clients.apievangelist.com read as a market, and the cut where the
    # INSTRUMENT stops fitting the category — which is itself the finding.
    #
    # Only 3 of 35 candidates publish an OpenAPI (Postman 35 specs, Insomnia
    # 4, HTTPie 3) and 30 sit at the agent-readiness floor. That is not a
    # harvesting gap: an API client is a CONSUMER of APIs, and a large and
    # growing share of this market is deliberately built with NO service
    # surface — Yaak advertises "no telemetry and no cloud lock-in", Bruno
    # and Voiden are "offline-first, Git-native", Restfox is "offline-first".
    # So the REPORT scores only the platform tier and presents the rest as the
    # counter-movement they are. This SECTION is a catalog directory and still
    # lists everyone; the directory and the report's analysis are different
    # things and do not conflict.
    #
    # Cross-cohort: Apidog is a client platform by the same test but is already
    # scored in the PUBLISHED management cohort — one provider, one cohort.
    # RapidAPI is a marketplace, not a client (Paw is "now RapidAPI for Mac").
    # Scalar and Stoplight are scored in documentation; Microcks, REST Assured
    # and Step CI in testing. `curlie` is CURLIE.ORG, the DMOZ-successor web
    # directory, NOT the CLI tool — the fourth slug collision in four area cuts.
    # Roster: all/0-working/api-clients-roster.json.
    API_CLIENTS_TIER_LABELS = {
        "platform":    "Client Platforms",
        "local-first": "Local-First & Offline-First Clients",
        "cli-library": "CLI Clients & HTTP Libraries",
    }
    API_CLIENTS_SECTIONS = [
        ("api-clients", "api-clients-roster.json", "API Clients",
         "The API client market ranked by Kin Score — the client platforms that operate a hosted service (Postman, Insomnia, Hoppscotch, HTTPie, Thunder Client, Firecamp), the local-first and offline-first clients that deliberately ship no cloud at all (Bruno, Yaak, Voiden, Restfox, Paw, Kreya, Milkman, Nightingale, API Dash, Ezy, ReqBin, the JetBrains and VS Code editor clients, and the debugging proxies Charles, Fiddler and mitmproxy), and the command-line clients and HTTP libraries the whole industry runs on (cURL, Wget, xh, Hurl, grpcurl, Axios, Got, HTTPX, Requests, node-fetch, OkHttp, Retrofit, RestSharp). Only three of these publish an API of their own, because an API client is a consumer of APIs rather than a provider of one — which is why the accompanying report scores the platform tier and reads the rest as a market movement rather than a ranking.",
         {"slug": "state-of-api-clients", "title": "The State of API Clients",
          "blurb": "The API client market, and the one cut in this series where the measuring instrument stops fitting the category. Only 3 of 35 publish an API of their own. That is not a gap in the research \u2014 it is a market deliberately building without a service surface, and Postman is the reason. Scores the six platforms that do operate a service, and reads the other twenty-nine as the offline-first counter-movement they advertise themselves to be.", "price": "500"}),
    ]
    api_clients_counts = {}
    build_roster_sections(API_CLIENTS_SECTIONS, API_CLIENTS_TIER_LABELS, api_clients_counts)

    # --- Authentication (single GLOBAL cohort, the fifth AREA cut) --------
    # authentication.apievangelist.com read as a market, and the STRONGEST
    # area cohort measured: composite 50.4, agent readiness 36.3, seven
    # Exemplars, and spec presence at 97.5% — this market publishes contracts
    # because its product IS an API.
    #
    # COHORT IS HAND-NAMED and nearly DOUBLE the curated index of 21, because
    # the developer-first CIAM wave (Clerk, Stytch, Kinde, PropelAuth,
    # Descope, Frontegg, Corbado, Hanko) and the fine-grained authorization
    # wave (Cerbos, OpenFGA, AuthZed, Oso, Permit.io, Aserto) are both largely
    # missing from it.
    #
    # INDUSTRY/AREA OVERLAP IS DELIBERATE. All 20 curated members also sit in
    # the published 2,031-provider cybersecurity INDUSTRY cohort, exactly as 29
    # of the 35 API-management providers sit in developer-tools. An industry
    # says who a company sells to; an area says what the API does. The
    # one-provider-one-cohort rule applies WITHIN a lens, not across lenses.
    #
    # Secrets management (HashiCorp Vault and the KMS layer) is OUT — it
    # belongs to the encryption area. LoginRadius and MojoAuth are excluded as
    # THIN PROFILES: their 7.8 and 6.2 composites sit on 35- and 54-character
    # descriptions and are an API Evangelist harvesting gap, not a market
    # signal. Curity, Passage, Authgear, miniOrange, Duende and WSO2 Identity
    # Server are absent from the catalog entirely — a real coverage gap.
    # Roster: all/0-working/authentication-roster.json.
    AUTHENTICATION_TIER_LABELS = {
        "enterprise": "Enterprise IAM & Workforce Identity",
        "cloud":      "Cloud Platform Identity",
        "ciam":       "Developer-First CIAM",
        "opensource": "Open Source Identity Servers",
        "authz":      "Authorization & Policy Engines",
    }
    AUTHENTICATION_SECTIONS = [
        ("authentication", "authentication-roster.json", "Authentication & Identity",
         "The API authentication and identity market ranked by Kin Score — the enterprise IAM and workforce identity platforms (Okta, Ping Identity, ForgeRock, SailPoint, CyberArk, OneLogin, Duo Security, JumpCloud), the cloud platform identity services (Amazon Cognito, Microsoft Entra ID), the developer-first CIAM providers (Auth0, WorkOS, Stytch, Kinde, PropelAuth, Clerk, Descope, Frontegg, FusionAuth, Beyond Identity, Transmit Security, Corbado, Hanko, Magic, Nevis), the open source identity servers (Keycloak, Ory, Zitadel, Authentik, Authelia, Casdoor, SuperTokens, Logto, Gluu) and the authorization and policy engines (Cerbos, OpenFGA, AuthZed, Oso, Permit.io, Aserto). The strongest-publishing area in the catalog — 97.5% ship a machine-readable contract — and the one where the single scarcest artifact is the one the market sells.",
         {"slug": "state-of-authentication-apis", "title": "The State of API Authentication",
          "blurb": "40 authentication, identity and authorization providers scored — the strongest-publishing market in this series. Composite 50.4 against a catalog average of 22.8, seven Exemplars, and 97.5% ship a machine-readable contract. Six run a public MCP server, the most of any area measured. And then the sharpest finding in the series: delegated identity and consent signal appears once in forty, in the market whose entire product is letting one party act on another\u2019s behalf.", "price": "500"}),
    ]
    authentication_counts = {}
    build_roster_sections(AUTHENTICATION_SECTIONS, AUTHENTICATION_TIER_LABELS, authentication_counts)

    # --- Logistics & Supply Chain (four cohorts, split by MODE) -----------
    # The first sector in the series NOT split by country. A container, a
    # parcel and an air waybill cross borders by definition, so an HQ model
    # would file Maersk under Denmark and tell you nothing; each organization
    # is filed by the mode it operates in instead.
    #
    # Logistics is also the sector that tests INTEROPERABILITY rather than
    # mandate: no one party owns the transaction, so a shipment only moves if
    # the next party can read what the last one published. That makes the
    # standards bodies the variable to watch, and the four modes disagree
    # about them completely — DCSA publishes conformant OpenAPI for ocean,
    # IATA authors ONE Record for air cargo (and scored 21.5 on its own
    # surface in the travel study), GS1 and the WCO sit horizontally across
    # freight and customs, and road has no dominant body at all.
    #
    # Rosters live in all/0-working/<cohort>-roster.json.
    LOGISTICS_TIER_LABELS = {
        # air cargo & parcel
        "air-cargo-carrier":         "Air Cargo Carriers",
        "air-cargo-marketplace":     "Air Cargo Marketplaces",
        "parcel-integrator":         "Parcel Integrators",
        "postal-operator":           "Postal Operators",
        "shipping-api-aggregator":   "Shipping API Aggregators",
        "tracking-aggregator":       "Tracking Aggregators",
        # freight platforms
        "freight-forwarder":         "Freight Forwarders",
        "visibility-platform":       "Visibility Platforms",
        "supply-chain-software":     "Supply Chain Software",
        "customs-trade-tech":        "Customs & Trade Tech",
        "edi-integration":           "EDI & Integration",
        "fulfilment-warehousing":    "Fulfilment & Warehousing",
        # road & fleet
        "telematics-fleet":          "Telematics & Fleet",
        "digital-freight-marketplace": "Digital Freight Marketplaces",
        "load-board":                "Load Boards",
        "last-mile-delivery":        "Last-Mile Delivery",
        "road-tms":                  "Transportation Management",
        "road-carrier-3pl":          "Road Carriers & 3PLs",
        # ocean & ports
        "ocean-carrier":             "Ocean Carriers",
        "port-terminal-operator":    "Ports & Terminal Operators",
        "port-community-system":     "Port Community Systems",
        "ocean-visibility":          "Ocean Visibility",
        # shared
        "industry-body-standards":   "Industry Bodies & Standards",
        "regulator":                 "Regulators",
    }
    LOGISTICS_SECTIONS = [
        ("air-cargo-parcel", "air-cargo-parcel-roster.json", "Air Cargo & Parcel Logistics",
         "Air cargo and parcel organizations ranked by their Kin Score — the freighter carriers, the air cargo marketplaces selling capacity as an API, the parcel integrators whose developer portals are among the most mature in logistics, the national postal operators, and the shipping-API aggregators that resell all of them behind one contract. This is the mode IATA's ONE Record was written for, and the tier that actually publishes is the aggregator layer that exists because the carriers do not.",
         None),
        ("freight-platforms", "freight-platforms-roster.json", "Freight Platforms, Forwarders & Customs",
         "Freight platforms, forwarders and customs technology ranked by their Kin Score — the global forwarders that sit between shippers and carriers exactly as a GDS sits between agencies and airlines, the visibility platforms that exist because neither end publishes reachable data, supply chain software, the customs and trade-compliance vendors selling duty and classification as an API, EDI integration, fulfilment and warehousing, and the two horizontal standards bodies whose identifiers and data models the whole sector borrows: GS1 and the World Customs Organization.",
         None),
        ("road-fleet", "road-fleet-roster.json", "Road, Fleet & Telematics Logistics",
         "Road, fleet and telematics organizations ranked by their Kin Score — the telematics vendors that sell an API as the product because vehicle data has no other route to the customer, the digital freight marketplaces built API-first to disintermediate the broker, the load boards, last-mile delivery, transportation management systems and the road carriers and 3PLs. The one mode in logistics with no dominant standards body, which makes it the control group for whether a standards body helps or hinders what gets published.",
         None),
        ("ocean-ports", "ocean-ports-roster.json", "Ocean & Ports Logistics",
         "Ocean shipping and port organizations ranked by their Kin Score — the container lines, the terminal operators, the port community systems built specifically to be the neutral integration point between hundreds of parties in one port, the ocean visibility platforms, the IMO, and DCSA: the association the largest carriers founded to publish common OpenAPI standards for booking, track-and-trace and the electronic bill of lading. The direct structural counterpart to IATA and NDC in aviation — same governance shape, very different publication posture.",
         None),
    ]
    logistics_counts = {}
    build_roster_sections(LOGISTICS_SECTIONS, LOGISTICS_TIER_LABELS, logistics_counts)

    secondary_entries = build_secondary_market(data_dir, meta_of, scores)
    vc_entries = build_vcs(data_dir, delisted)

    print("industries:       %d (providers matched: %d)" % (
        len(industry_cards), sum(c["count"] for c in industry_cards)))
    print("countries:        %d (providers matched: %d)" % (
        len(country_cards), sum(c["count"] for c in country_cards)))
    print("australian banks: %d (scored: %d)" % (
        len(au_banks), sum(1 for b in au_banks if "score" in b)))
    print("market data:      %d (scored: %d)" % (
        len(market_data), sum(1 for e in market_data if "score" in e)))
    for spec in BANK_SECTIONS:
        n, sc = bank_counts.get(spec[0], (0, 0))
        print("%-19s %d (scored: %d)" % (spec[0] + ":", n, sc))
    for spec in PAY_SECTIONS:
        n, sc = pay_counts.get(spec[0], (0, 0))
        print("%-19s %d (scored: %d)" % (spec[0] + ":", n, sc))
    for spec in HEALTH_SECTIONS:
        n, sc = health_counts.get(spec[0], (0, 0))
        print("%-19s %d (scored: %d)" % (spec[0] + ":", n, sc))
    for spec in INS_SECTIONS:
        n, sc = ins_counts.get(spec[0], (0, 0))
        print("%-19s %d (scored: %d)" % (spec[0] + ":", n, sc))
    for spec in TELECOM_SECTIONS:
        n, sc = telecom_counts.get(spec[0], (0, 0))
        print("%-19s %d (scored: %d)" % (spec[0] + ":", n, sc))
    for spec in RE_SECTIONS:
        n, sc = re_counts.get(spec[0], (0, 0))
        print("%-19s %d (scored: %d)" % (spec[0] + ":", n, sc))
    for spec in ENERGY_SECTIONS:
        n, sc = energy_counts.get(spec[0], (0, 0))
        print("%-19s %d (scored: %d)" % (spec[0] + ":", n, sc))
    for spec in TRAVEL_SECTIONS:
        n, sc = travel_counts.get(spec[0], (0, 0))
        print("%-19s %d (scored: %d)" % (spec[0] + ":", n, sc))
    for spec in HEADLESS_SECTIONS:
        n, sc = headless_counts.get(spec[0], (0, 0))
        print("%-19s %d (scored: %d)" % (spec[0] + ":", n, sc))
    for spec in MANAGEMENT_SECTIONS:
        n, sc = management_counts.get(spec[0], (0, 0))
        print("%-19s %d (scored: %d)" % (spec[0] + ":", n, sc))
    for spec in LOGISTICS_SECTIONS:
        n, sc = logistics_counts.get(spec[0], (0, 0))
        print("%-19s %d (scored: %d)" % (spec[0] + ":", n, sc))
    print("secondary market: %d (scored: %d)" % (
        len(secondary_entries), sum(1 for e in secondary_entries if "score" in e)))
    print("venture capital:  %d (portfolio companies: %d)" % (
        len(vc_entries), sum(e["portfolio_total"] for e in vc_entries)))

    # The two interactive market tools, for every listing that sells a report.
    # A POST-PASS, because its notes are computed from the data files written
    # above and from the rubric, and because the `tools:` block has to land in
    # pages built by five different call sites here. See the module docstring in
    # build-section-tools.py for why it is generated rather than hand-added.
    subprocess.run(
        [sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      "build-section-tools.py")],
        check=True,
    )


if __name__ == "__main__":
    main()

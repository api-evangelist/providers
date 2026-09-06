---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Beautiful Soup 4 is a Python library providing a parse tree API for HTML and XML documents. It exposes Tag, NavigableString, BeautifulSoup, and Comment objects with navigation methods (find, find_all,
  name: Beautiful Soup
  slug: beautiful-soup
artifact_total: 23
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beautiful-soup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crummy.com/software/BeautifulSoup/
- group: docs
  title: ''
  type: Documentation
  url: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- group: build
  title: PyPI Package
  type: SDKs
  url: https://pypi.org/project/beautifulsoup4/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://bazaar.launchpad.net/~leonardr/beautifulsoup/bs4
- group: operate
  title: ''
  type: ChangeLog
  url: https://bazaar.launchpad.net/~leonardr/beautifulsoup/bs4/view/head:/CHANGELOG
created: '2026-03-29'
description: Beautiful Soup is a Python library for pulling data out of HTML and XML files, widely used for web scraping and screen scraping tasks. It provides a parse tree API with simple methods for navigating, searching, and modifying parsed HTML/XML documents. Beautiful Soup automatically handles encoding, supports multiple parsers (html.parser, lxml, html5lib), and integrates with CSS selectors via the Soup Sieve library. Current stable version is 4.14.3.
features:
- description: Supports html.parser (built-in), lxml (fast), and html5lib (browser-like) parsers for flexible HTML/XML parsing.
  name: Multi-Parser Support
- description: Full CSS4 selector support via the Soup Sieve library for familiar CSS-based element selection.
  name: CSS Selector Support
- description: Rich API for navigating the parse tree upward, downward, and sideways including find(), find_all(), parents, children, and siblings.
  name: Tree Navigation API
- description: Automatically detects and handles document encoding using Unicode, Dammit, ensuring correct text extraction.
  name: Automatic Encoding Detection
- description: Full tree modification support including append, insert, extract, decompose, replace_with, wrap, and unwrap operations.
  name: Tree Modification
- description: Multiple output formatters including prettify(), get_text(), and custom formatters for controlled serialization.
  name: Output Formatting
finops:
- name: Beautiful Soup Finops
  service_category: API
  slug: beautiful-soup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beautiful-soup.png
integrations:
- description: Python HTTP library used in combination with Beautiful Soup to fetch and parse web pages.
  name: Requests
- description: Python web crawling framework that can use Beautiful Soup selectors for content extraction.
  name: Scrapy
- description: Fast XML and HTML parsing library used as an alternate parser backend for Beautiful Soup.
  name: lxml
- description: Pure-Python HTML5 parser used with Beautiful Soup for browser-compatible HTML parsing.
  name: html5lib
- description: DataFrame library commonly used with Beautiful Soup to convert scraped HTML tables into structured data.
  name: Pandas
- description: Browser automation tool used with Beautiful Soup to scrape JavaScript-rendered pages.
  name: Selenium
layout: provider
modified: '2026-04-19'
name: Beautiful Soup
nav: Providers
network: true
overview: 'Beautiful Soup publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Extraction, HTML Parsing, Python, Scraping, and Web Scraping.


  Beautiful Soup''s developer surface includes documentation, changelog, and 4 more developer resources.'
plans:
- name: Beautiful Soup Plans Pricing
  plan_count: 3
  slug: beautiful-soup-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Beautiful Soup Rate Limits
  slug: beautiful-soup-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beautiful-soup/refs/heads/main/screenshots/beautiful-soup-2026-06-20T173111.png
security:
- kind: domain-security
  name: Beautiful Soup Domain Security
  slug: beautiful-soup-domain-security
  summary_line: TLSv1.2 · DMARC
slug: beautiful-soup
tags:
- Data Extraction
- HTML Parsing
- Python
- Scraping
- Web Scraping
- XML Parsing
use_cases:
- description: Extract data from websites by parsing HTML pages with Beautiful Soup and navigating the DOM tree to find target elements.
  name: Web Scraping
- description: Mine structured data from HTML tables, lists, and other markup patterns across large numbers of web pages.
  name: Data Mining
- description: Extract article text, product information, or other content from web pages for NLP pipelines and data analysis.
  name: Content Extraction
- description: Automate data extraction from legacy HTML web interfaces that lack modern APIs.
  name: Screen Scraping Legacy Systems
- description: Parse and clean HTML documents by removing unwanted tags, scripts, and formatting.
  name: HTML Sanitization
- description: Parse and query XML documents using Beautiful Soup's tree navigation and search capabilities.
  name: XML Processing
website: https://www.crummy.com/software/BeautifulSoup/
---

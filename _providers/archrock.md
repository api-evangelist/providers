---
access_model:
  confidence: high
  label: No public API program
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - https://www.archrock.com/sitemap.xml
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Machine-readable filing data for Archrock is available from the U.S. Securities and Exchange Commission, not from the company. The SEC EDGAR submissions API returns the full filing history for CIK 000
  name: SEC EDGAR Filings (Archrock, Inc., CIK 1389050)
  slug: sec-edgar-filings
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.archrock.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/security/archrock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archrock-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/archrock
- group: start
  title: ''
  type: Portal
  url: https://www.archrock.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.archrock.com/aroc-investor-relations/
- group: company
  title: ''
  type: Blog
  url: https://www.archrock.com/news-media/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.archrock.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.archrock.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.archrock.com/contact/
coverage:
  checked: '2026-09-04'
  detail: 'Archrock (NYSE: AROC) sells natural gas compression as a physical service — contract compression, field and shop aftermarket work, and compressor parts — and its complete 42-page sitemap contains no developer, API, docs, signup or pricing page; the api.archrock.com host named by the OpenAPI files in this repo has no DNS record at all.'
  evidence:
  - status: 200
    url: https://www.archrock.com/sitemap.xml
  - status: 0
    url: https://api.archrock.com/openapi.json
  - status: 404
    url: https://www.archrock.com/.well-known/api-catalog
  - status: 404
    url: https://www.archrock.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/archrock
  reason: not-a-software-company
  state: none
created: '2026-03-23'
description: 'Archrock (NYSE: AROC) is the premier provider of natural gas compression services and equipment to customers in the oil and natural gas industry throughout the United States. The company operates a large fleet of compression equipment and provides contract operations and aftermarket services.'
features:
- description: Contract operations and maintenance of natural gas compression equipment across the US.
  name: Natural Gas Compression
- description: Management of one of the largest compression fleets in North America with diverse horsepower ratings.
  name: Fleet Management
- description: Parts, service, and maintenance for third-party compression equipment.
  name: Aftermarket Services
- description: Financial performance, fleet statistics, and operational metrics for investors and analysts.
  name: Investor Relations Data
- description: Annual reports, 10-K, 10-Q, and 8-K filings available through SEC EDGAR.
  name: SEC Filings
finops:
- name: Archrock Finops
  service_category: API
  slug: archrock-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/archrock.png
integrations:
- description: All SEC filings available through the EDGAR electronic filing system.
  name: SEC EDGAR
- description: Financial and operational data integrated with Bloomberg terminal.
  name: Bloomberg
- description: Production and financial data available through Refinitiv data services.
  name: Refinitiv
layout: provider
modified: '2026-09-04'
name: Archrock
nav: Providers
network: true
overview: 'Archrock publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Natural Gas, Compression Services, Oil and Gas, Energy, and Industrial.


  Archrock''s developer surface includes developer portal, engineering blog, support, and 6 more developer resources.'
plans:
- name: Archrock Plans Pricing
  plan_count: 0
  slug: archrock-plans-pricing
press:
- date: ''
  title: Archrock, Inc.
  url: https://www.facebook.com/Archrock/posts/yesterday-archrock-inc-reported-its-q2-2025-earnings-and-the-results-were-outsta/1359602162836702/
- date: ''
  title: Rising LNG Exports & AI-Driven Power Demand Drive ...
  url: https://finance.yahoo.com/news/rising-lng-exports-ai-driven-191500994.html
- date: ''
  title: Archrock Surges on Record Earnings, Eyes LNG and AI Growth ...
  url: https://briefglance.com/articles/archrock-surges-on-record-earnings-eyes-lng-and-ai-growth-boom
- date: ''
  title: Archrock Stock Fuels Breakout On Demand From AI Data ...
  url: https://www.investors.com/research/breakout-stocks-technical-analysis/archrock-stock-aroc-cng-ai-data-centers/
- date: ''
  title: AI Power, LNG Growth Sparking Natural Gas Compression ...
  url: https://naturalgasintel.com/news/ai-power-lng-growth-sparking-natural-gas-compression-boom-for-archrock/
random_paper: 9
rate_limits:
- limit_count: 0
  name: Archrock Rate Limits
  slug: archrock-rate-limits
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -15.4
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 33.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/archrock/refs/heads/main/screenshots/archrock-2026-06-20T172409.png
security:
- kind: domain-security
  name: Archrock Domain Security
  slug: archrock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: archrock
tags:
- Natural Gas
- Compression Services
- Oil and Gas
- Energy
- Industrial
- 'NYSE: AROC'
use_cases:
- description: Analyze Archrock financial performance and fleet utilization for investment decisions.
  name: Investment Research
- description: Track natural gas compression services market trends and operational data.
  name: Energy Sector Analysis
- description: Access environmental and safety performance data for ESG analysis.
  name: ESG Reporting
- description: Operators use Archrock fleet data for compression capacity planning.
  name: Supply Chain Planning
website: https://www.archrock.com/
---

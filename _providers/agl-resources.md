---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 10
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/southern-company/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agl-resources-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agl-resources
- group: company
  title: ''
  type: Website
  url: https://www.southerncompanygas.com/
- group: company
  title: ''
  type: Website
  url: https://www.atlantagaslight.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.southerncompany.com/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.southerncompany.com/privacy-statement.html
- group: company
  title: ''
  type: Blog
  url: https://www.southerncompanygas.com/news.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agl-resources-llms.txt
coverage:
  checked: '2026-08-30'
  detail: AGL Resources ceased to exist as an operating brand when Southern Company acquired it in 2016 and renamed it Southern Company Gas — the legacy corporate domain www.aglresources.com now redirects to www.southerncompanygas.com, and that successor site is a consumer/corporate information site whose full sitemap contains no developer, API or documentation section, with /developers returning 404 and every /.well-known/ path on southerncompanygas.com, atlantagaslight.com and the parent southerncompany.com returning 404.
  evidence:
  - status: 200
    url: https://www.aglresources.com/
  - status: 404
    url: https://www.southerncompanygas.com/developers
  - status: 404
    url: https://www.southerncompanygas.com/.well-known/api-catalog
  - status: 404
    url: https://www.southerncompanygas.com/openapi.json
  - status: 404
    url: https://www.atlantagaslight.com/.well-known/agent-card.json
  - status: 200
    url: https://www.southerncompanygas.com/sitemap.xml
  reason: defunct
  state: none
created: '2026-04-19'
description: AGL Resources was an energy services holding company headquartered in Atlanta, Georgia, whose principal business was the distribution of natural gas to residential, commercial, and industrial customers. In 2016, AGL Resources was acquired by Southern Company and renamed Southern Company Gas, becoming the nation's largest natural gas-only distribution company. The company distributes natural gas through subsidiaries including Atlanta Gas Light, Chattanooga Gas, Nicor Gas, and Virginia Natural Gas. AGL Resources / Southern Company Gas does not offer a public developer API; utility data access is available through third-party data aggregators and community-built integrations.
features:
- description: Distribution of natural gas to over 1.6 million residential, commercial, and industrial customers in Georgia and other states.
  name: Natural Gas Distribution
- description: Competitive retail natural gas services through brands including SouthStar Energy Services and Georgia Natural Gas.
  name: Energy Marketing Services
- description: Midstream pipeline investments and operations supporting natural gas transport and delivery.
  name: Pipeline Infrastructure
- description: Clean energy initiatives and net-zero goals including hydrogen blending and renewable natural gas programs.
  name: Sustainability Programs
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agl-resources.png
integrations:
- description: Third-party utility data aggregation platform enabling programmatic access to AGL/Southern Company Gas usage data with customer consent.
  name: UtilityAPI
- description: Customer account portal for usage monitoring, billing, and payment management.
  name: Southern Company Online Account
layout: provider
modified: '2026-08-30'
name: AGL Resources
nav: Providers
network: true
overview: 'AGL Resources is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Natural Gas, Utilities, Energy Distribution, and Georgia.


  AGL Resources'' developer surface includes engineering blog and 8 more developer resources.'
press:
- date: '2026-05-25'
  title: Southern Company (SO) and the New Energy Tsunami
  url: https://markets.financialcontent.com/stocks/article/finterra-2026-2-19-the-ai-utility-southern-company-so-and-the-new-energy-tsunami
- date: '2026-05-25'
  title: 'Forbes Earnings Preview: AGL Resources Inc.'
  url: https://www.forbes.com/sites/narrativescience/2013/02/03/forbes-earnings-preview-agl-resources-inc/
- date: '2026-05-25'
  title: Southern Company and AGL Resources complete merger, ...
  url: https://www.prnewswire.com/news-releases/southern-company-and-agl-resources-complete-merger-create-a-leading-us-energy-company-300293200.html
- date: '2026-05-25'
  title: Power demand is skyrocketing from AI, electrification and ...
  url: https://www.facebook.com/WilliamsEnergyCo/posts/power-demand-is-skyrocketing-from-ai-electrification-and-industrial-reshoring-bu/904918505241219/
- date: '2026-05-25'
  title: Southern Company--AGL Resources combination ...
  url: https://www.prnewswire.com/news-releases/southern-company--agl-resources-combination-enhances-customer-focused-business-model-300132249.html
random_paper: 17
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agl-resources/refs/heads/main/screenshots/agl-resources-2026-06-20T170314.png
security:
- kind: domain-security
  name: Agl Resources Domain Security
  slug: agl-resources-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agl-resources
tags:
- Energy
- Natural Gas
- Utilities
- Energy Distribution
- Georgia
- Fortune 500
use_cases:
- description: Customers manage natural gas accounts, usage, and billing through online portals and mobile apps.
  name: Residential Energy Management
- description: Large commercial and industrial customers access competitive natural gas supply and usage reporting.
  name: Commercial and Industrial Supply
- description: Utility data aggregators (such as UtilityAPI) can provide programmatic access to usage data with customer consent.
  name: Third-Party Data Aggregation
website: https://www.southerncompanygas.com/
---

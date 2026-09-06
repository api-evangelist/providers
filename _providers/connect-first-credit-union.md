---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - '{''url'': ''https://www.connectfirstcu.com/'', ''status'': 301, ''note'': ''declared website redirects to https://servus.ca/?utm_source=cfcu&utm_medium=redirect — a different registrable domain (connectfirstcu.com -> servus.ca), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/connect-first-credit-union-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/connect-first-credit-union-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/connect-first-credit-union-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/connect-first-credit-union-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/connect-first-credit-union-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/connect-first-credit-union-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.connectfirstcu.com/
- group: company
  title: ''
  type: Blog
  url: https://connectfirstcu.com/en/news/news-and-announcments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/connect-first-credit-union
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://servus.ca/privacy
created: '2026-07-23'
description: 'connectFirst Credit Union is a member-owned, cooperative (Schedule-equivalent provincial credit union) financial institution headquartered in Calgary, Alberta, formed on May 3, 2021 by amalgamating four Alberta credit unions (First Calgary Financial, Chinook Financial, Mountain View Financial, and Legacy Financial). At its peak it held over CAD $6 billion in assets under administration and served more than 128,000 members across 41 branches in Central and Southern Alberta, offering retail, commercial, agricultural, and dealer-services banking. Members voted in November 2023 to merge with Servus Credit Union; the legal amalgamation closed May 1, 2024 as "Connect First and Servus Credit Union Ltd." (~CAD $29.3B assets, 600,000+ members), and the unified brand realigned to Servus Credit Union in January 2025 — the connectfirstcu.com domain now 301-redirects to servus.ca. Its open-finance posture is honest and typical of a Canadian credit union: no first-party public developer
  portal or downloadable OpenAPI, digital banking delivered via the Celero Xpress platform (powered by ebankIT) with core/banking-tech through the Central 1 / Celero cooperative ecosystem, and third-party consumer data access available only through aggregators (Plaid coverage confirmed). Canada''s federal Consumer-Driven Banking framework (Budget 2024 / FCAC-overseen) is legislated but not yet operational, so no mandated open-banking API exists.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: connectFirst Credit Union
nav: Providers
network: true
overview: 'connectFirst Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Credit Union, and Alberta.


  connectFirst Credit Union''s developer surface includes authentication, engineering blog, and 8 more developer resources.'
random_paper: 17
scopes:
- name: Connect First Credit Union Scopes
  scope_count: 0
  slug: connect-first-credit-union-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 55.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/connect-first-credit-union/refs/heads/main/screenshots/connect-first-credit-union-2026-07-25T210259.png
security:
- kind: authentication
  name: Connect First Credit Union Authentication
  slug: connect-first-credit-union-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Connect First Credit Union Domain Security
  slug: connect-first-credit-union-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: connect-first-credit-union
tags:
- Financial-Services
- Banking
- Canada
- Credit Union
- Alberta
- Cooperative
- Data Aggregation
website: https://www.connectfirstcu.com/
---

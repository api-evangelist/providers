---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides public data services for property and business records via the Maryland DAT portal.
  name: Maryland Department of Assessments and Taxation API
  slug: maryland-department-of-assessments-and-taxation-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/maryland-department-of-assessments-and-taxation/llms/maryland-department-of-assessments-and-taxation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/maryland-department-of-assessments-and-taxation-llms.txt
- group: other
  href: https://artifacts.apis.io/maryland-department-of-assessments-and-taxation/hosts/maryland-department-of-assessments-and-taxation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/maryland-department-of-assessments-and-taxation-hosts.yml
- group: other
  href: https://artifacts.apis.io/maryland-department-of-assessments-and-taxation/vendors/maryland-department-of-assessments-and-taxation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/maryland-department-of-assessments-and-taxation-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://www.maryland.gov/pages/privacy_security.aspx
- group: company
  title: ''
  type: Newsroom
  url: https://dat.maryland.gov/newsroom
- group: auth
  href: https://artifacts.apis.io/maryland-department-of-assessments-and-taxation/security/maryland-department-of-assessments-and-taxation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maryland-department-of-assessments-and-taxation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dat.maryland.gov/Pages/default.aspx
coverage:
  checked: '2026-10-26'
  detail: The provider's documentation returns HTML pages for spec URLs (e.g., /openapi.json) with no machine‑readable OpenAPI definition.
  evidence:
  - status: 200
    url: https://dat.maryland.gov/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: The Maryland Department of Assessments and Taxation (MDAT) is the state agency responsible for maintaining property and business records, assessing real‑property values, and providing a range of online services to Maryland residents, businesses, and government entities. It offers searchable databases for business entities, real‑property assessments, tax credits, and more, accessible through its public web portals and data services.
image: https://dat.maryland.gov/Style Library/egov/img/logo.png
layout: provider
modified: '2026-10-26'
name: Maryland Department of Assessments and Taxation
nav: Providers
network: true
overview: Maryland Department of Assessments and Taxation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Real Estate, Business Services, Data, and Maryland.
random_paper: 6
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/maryland-department-of-assessments-and-taxation/maryland-department-of-assessments-and-taxation-2026-11-03T135344.png
security:
- kind: domain-security
  name: Maryland Department Of Assessments And Taxation Domain Security
  slug: maryland-department-of-assessments-and-taxation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: maryland-department-of-assessments-and-taxation
tags:
- Government
- Real Estate
- Business Services
- Data
- Maryland
website: https://dat.maryland.gov/Pages/default.aspx
---

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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-west-credit-union-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/first-west-credit-union-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/first-west-credit-union-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.trucooperativebank.ca/
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/firstwestcu
- group: other
  title: ''
  type: X
  url: https://x.com/firstwestcu
created: '2026-07-23'
description: First West Credit Union — rebranded Tru Cooperative Bank in 2026 — is a member-owned Canadian cooperative financial institution headquartered in Langley, British Columbia. Formed in 2010 by the merger of Envision Credit Union and Valley First, and later joined by Island Savings and Enderby & District Financial, it operates those four regional brands over a shared branch network with roughly 291,000 members, about $20.8 billion in total assets, 45 branches, and around 1,300 employees. After members voted in 2021 for federal continuance, it received a federal charter under Canada's Bank Act and became a federal credit union / cooperative bank (CDIC-insured) as of April 1, 2026. On the open-finance front First West / Tru runs no first-party public developer portal and publishes no downloadable OpenAPI or partner API; both developer.firstwestcu.ca and developer.trucooperativebank.ca resolve to nothing (NXDOMAIN). Third-party access to member account data today is aggregator-based
  (screen-scraping via providers such as Plaid and Flinks), the fragmented and voluntary Canadian norm while the federal Consumer-Driven Banking framework (Budget 2024 / Fall Economic Statement 2024, overseen by the FCAC) remains legislated but not yet operational.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: First West Credit Union
nav: Providers
network: true
overview: First West Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Credit Union, and Cooperative Bank.
random_paper: 16
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/first-west-credit-union/refs/heads/main/screenshots/first-west-credit-union-2026-07-25T214610.png
security:
- kind: domain-security
  name: First West Credit Union Domain Security
  slug: first-west-credit-union-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: first-west-credit-union
tags:
- Financial-Services
- Banking
- Canada
- Credit Union
- Cooperative Bank
- British Columbia
- Consumer-Driven Banking
- Data Aggregation
website: https://www.trucooperativebank.ca/
---

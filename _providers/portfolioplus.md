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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Portfolio+ offers open banking and core banking APIs as described on their website.
  name: Portfolio API
  slug: portfolio-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/portfolioplus/well-known/portfolioplus-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/portfolioplus-well-known.yml
- group: agent
  href: https://artifacts.apis.io/portfolioplus/llms/portfolioplus-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/portfolioplus-llms.txt
- group: other
  href: https://artifacts.apis.io/portfolioplus/hosts/portfolioplus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/portfolioplus-hosts.yml
- group: other
  href: https://artifacts.apis.io/portfolioplus/vendors/portfolioplus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/portfolioplus-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://portfolioplus.com/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://portfolioplus.com/leadership/
- group: company
  title: ''
  type: Blog
  url: https://portfolioplus.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.portfolioplus.com/
- group: auth
  href: https://artifacts.apis.io/portfolioplus/security/portfolioplus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/portfolioplus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://portfolioplus.com/
coverage:
  checked: '2026-10-21'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on any discovered host.
  evidence:
  - status: 0
    url: https://api.portfolioplus.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Portfolio+ provides a scalable Open Banking and Core Banking platform for banks, credit unions, trust companies, and other financial institutions. Their cloud‑based services include open finance APIs, core banking core‑ops, term deposit and GIC software, lending, investment management, retail banking solutions, and managed services. Portfolio+ also offers consulting, premier support, and business continuity planning, targeting both traditional banks and fintech partners.
image: https://portfolioplus.com/wp-content/uploads/2019/04/Main-hero-Backgorund.jpg
layout: provider
modified: '2026-10-21'
name: Portfolio
nav: Providers
network: true
overview: 'Portfolio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Open Finance, Cloud Services, and Consulting.


  Portfolio''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 65.2
    operational_transparency: 0.0
  previous_composite: 9.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 11.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/portfolioplus/portfolioplus-2026-11-03T141416.png
security:
- kind: domain-security
  name: Portfolioplus Domain Security
  slug: portfolioplus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: portfolioplus
tags:
- Company
- Banking
- Open Finance
- Cloud Services
- Consulting
website: https://portfolioplus.com/
---

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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public finance learning resources and glossary
  name: Learn API
  slug: learn-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/alokbarnwal-com/llms/alokbarnwal-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alokbarnwal-com-llms.txt
- group: other
  href: https://artifacts.apis.io/alokbarnwal-com/hosts/alokbarnwal-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alokbarnwal-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/alokbarnwal-com/security/alokbarnwal-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alokbarnwal-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alokbarnwal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://alokbarnwal.com/learn/
- group: other
  title: ''
  type: Glossary
  url: https://alokbarnwal.com/glossary/
- group: company
  title: ''
  type: About
  url: https://alokbarnwal.com/about/
coverage:
  checked: '2026-11-01'
  detail: No machine‑readable API contract (OpenAPI/GraphQL/etc.) was found on the provider's documentation site.
  evidence:
  - status: 200
    url: https://alokbarnwal.com/learn/
  - status: 0
    url: https://api.alokbarnwal.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Alok Barnwal is a public finance consultant based in Raipur, India, offering expertise in government budgeting, public finance management systems (PFMS), debt and cash management, and fiscal policy. Through his website alokbarnwal.com, he provides interactive lessons, a glossary, and detailed explanations to make public finance understandable for professionals, students, and officials.
image: https://alokbarnwal.com/og-default.svg
layout: provider
modified: '2026-11-01'
name: Alok Barnwal
nav: Providers
network: true
overview: 'Alok Barnwal is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Education, Consulting, and India.


  Alok Barnwal''s developer surface includes documentation and 6 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 5.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alokbarnwal Com Domain Security
  slug: alokbarnwal-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alokbarnwal-com
tags:
- Company
- Finance
- Education
- Consulting
- India
- Public Finance
website: https://alokbarnwal.com/
---

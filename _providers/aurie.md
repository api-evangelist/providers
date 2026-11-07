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
- description: API information not publicly available; no developer program or documentation found.
  name: Aurie API
  slug: aurie-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/aurie/hosts/aurie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aurie-hosts.yml
- group: other
  href: https://artifacts.apis.io/aurie/vendors/aurie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aurie-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.livewithaurie.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.livewithaurie.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/aurie/security/aurie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aurie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.livewithaurie.com/
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract discovered at api.livewithaurie.com.
  evidence:
  - status: 0
    url: https://api.livewithaurie.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Aurie is a medical device company developing the world’s first automatically reusable no‑touch catheter system. Founded in 2018 in Syracuse, New York, Aurie aims to improve independence for individuals requiring intermittent urinary catheterization by reducing infections and eliminating the need for disposable catheters. The company has received FDA De Novo clearance and is expanding internationally, targeting over 600,000 potential users in the United States.
image: https://cdn.sanity.io/images/p65scf09/production/0385cb644a17a52d976fbf03d019f7ecba170cbf-3000x2000.jpg?rect=0,213,3000,1575&w=1200&h=630
layout: provider
modified: '2026-09-26'
name: Aurie
nav: Providers
network: true
overview: Aurie is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Health Tech, Catheter, Reusable, and FDA.
random_paper: 6
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 9.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aurie/aurie-2026-10-11T100850.png
security:
- kind: domain-security
  name: Aurie Domain Security
  slug: aurie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aurie
tags:
- Medical Devices
- Health Tech
- Catheter
- Reusable
- FDA
website: https://www.livewithaurie.com/
---

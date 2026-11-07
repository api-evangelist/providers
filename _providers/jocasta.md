---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Jocasta is pioneering cognitive health with science‑backed solutions to support memory, focus, and resilience as you age.
  name: Jocasta API
  slug: jocasta-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/jocasta/hosts/jocasta-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jocasta-hosts.yml
- group: other
  href: https://artifacts.apis.io/jocasta/vendors/jocasta-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jocasta-vendors.yml
- group: auth
  href: https://artifacts.apis.io/jocasta/security/jocasta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jocasta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jocastaneuro.com
- group: company
  title: ''
  type: Blog
  url: https://www.jocastaneuro.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.jocastaneuro.com/contact
coverage:
  checked: '2026-10-29'
  detail: No machine-readable OpenAPI, AsyncAPI, GraphQL, or other spec found despite public documentation.
  evidence:
  - status: 404
    url: https://www.jocastaneuro.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Jocasta is a neurotechnology company focused on cognitive health, developing science‑backed solutions such as the α‑Klotho‑based supplement JN‑0413 to support memory, focus, and resilience as people age. The company combines clinical research, biotechnology, and wellness to deliver patented, IND‑ready treatments aimed at mitigating age‑related cognitive decline.
image: https://cdn.prod.website-files.com/681e7909aa00a14304829abb/681e7909aa00a14304829c58_webclip.jpg
layout: provider
modified: '2026-10-29'
name: Jocasta
nav: Providers
network: true
overview: 'Jocasta is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Neurotechnology, Cognitive Health, Biotechnology, Wellness, and Medical Research.


  Jocasta''s developer surface includes engineering blog, support, and 4 more developer resources.'
plans:
- name: Jocasta Plans Pricing
  plan_count: 0
  slug: jocasta-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Jocasta Rate Limits
  slug: jocasta-rate-limits
scopes:
- name: Jocasta Scopes
  scope_count: 0
  slug: jocasta-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/jocasta/jocasta-2026-11-03T134158.png
security:
- kind: authentication
  name: Jocasta Authentication
  slug: jocasta-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Jocasta Domain Security
  slug: jocasta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jocasta
tags:
- Neurotechnology
- Cognitive Health
- Biotechnology
- Wellness
- Medical Research
website: https://www.jocastaneuro.com
---

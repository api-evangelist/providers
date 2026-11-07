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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 16.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Human Mind API enables developers to create hands‑free, voice‑free applications by translating brain signals into actionable data.
  name: Nubrain API
  slug: nubrain-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/nubrain/well-known/nubrain-calendly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nubrain-calendly-security.txt
- group: auth
  href: https://artifacts.apis.io/nubrain/well-known/nubrain-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nubrain-api-security.txt
- group: agent
  href: https://artifacts.apis.io/nubrain/well-known/nubrain-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nubrain-well-known.yml
- group: other
  href: https://artifacts.apis.io/nubrain/hosts/nubrain-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nubrain-hosts.yml
- group: other
  href: https://artifacts.apis.io/nubrain/vendors/nubrain-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nubrain-vendors.yml
- group: auth
  href: https://artifacts.apis.io/nubrain/security/nubrain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nubrain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nubrain.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nubrain.com/early-access
- group: operate
  title: ''
  type: Support
  url: https://calendly.com/priyanka-nubrain/meet-the-team
- group: start
  title: ''
  type: SignUp
  url: https://www.nubrain.com/early-access
coverage:
  checked: '2026-10-29'
  detail: The provider's website presents static HTML docs with no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.nubrain.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Nubrain builds the world’s largest dataset of human brain activity, collecting over 500,000 EEG recordings to train foundation models that decode thoughts into text, speech, and images. Their Human Mind API enables developers to create hands‑free, voice‑free applications by translating brain signals into actionable data. Based in Berlin and New York, Nubrain offers early‑access headsets and API access for researchers and developers, backed by investors such as Vercel’s CTO and former AI leaders.
image: https://nubrain.com/nubrain-banner.png
layout: provider
modified: '2026-10-29'
name: Nubrain
nav: Providers
network: true
overview: 'Nubrain is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Neuroscience, Brain-Computer Interface, Artificial Intelligence, and EEG.


  Nubrain''s developer surface includes getting-started guide, support, signup flow, and 7 more developer resources.'
plans:
- name: Nubrain Plans Pricing
  plan_count: 0
  slug: nubrain-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Nubrain Rate Limits
  slug: nubrain-rate-limits
scopes:
- name: Nubrain Scopes
  scope_count: 0
  slug: nubrain-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 57.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nubrain/nubrain-2026-11-03T140342.png
security:
- kind: authentication
  name: Nubrain Authentication
  slug: nubrain-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nubrain Domain Security
  slug: nubrain-domain-security
  summary_line: TLSv1.3 · HSTS
slug: nubrain
tags:
- Company
- Neuroscience
- Brain-Computer Interface
- Artificial Intelligence
- EEG
website: https://nubrain.com
---

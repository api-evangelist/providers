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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Electronic invoicing API for Kema Invoice, as described in the documentation.
  name: Kema Invoice API
  slug: kema-invoice-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/kema-studio-com/llms/kema-studio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kema-studio-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/kema-studio-com/well-known/kema-studio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kema-studio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/kema-studio-com/hosts/kema-studio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kema-studio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/kema-studio-com/vendors/kema-studio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kema-studio-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/kema-studio-com/security/kema-studio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kema-studio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kema-studio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kema-studio.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kema-studio.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://kema-studio.com/en#produits
- group: operate
  title: ''
  type: Support
  url: https://kema-studio.com/en#contact
- group: commercial
  title: ''
  type: Legal
  url: https://docs.kema-studio.com/aspects-legaux/mentions-legales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.kema-studio.com/aspects-legaux/politique-de-confidentialite
coverage:
  checked: '2026-10-30'
  detail: Documentation is served as a JavaScript‑rendered site with no machine‑readable OpenAPI or GraphQL spec.
  evidence:
  - status: 200
    url: https://docs.kema-studio.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Kema Studio is a Lisbon‑based software studio that builds its own management applications—such as Olia for law firms and Kema Invoice for automated billing—and also develops custom solutions for other businesses. Its tools are used daily by teams, and the company highlights that AI agents can now pilot these applications, positioning itself at the intersection of SaaS and AI‑enabled automation.
image: https://kema-studio.com/logo.png
layout: provider
modified: '2026-10-30'
name: kema-studio-com
nav: Providers
network: true
overview: 'kema-studio-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Software, Management, Artificial Intelligence, Portugal, and Software-as-a-Service.


  kema-studio-com''s developer surface includes documentation, API reference, getting-started guide, support, legal docs, and 7 more developer resources.'
plans:
- name: Kema Studio Com Plans Pricing
  plan_count: 0
  slug: kema-studio-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Kema Studio Com Rate Limits
  slug: kema-studio-com-rate-limits
scopes:
- name: Kema Studio Com Scopes
  scope_count: 0
  slug: kema-studio-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 73.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - portugal
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kema-studio-com/kema-studio-com-2026-11-03T134348.png
security:
- kind: authentication
  name: Kema Studio Com Authentication
  slug: kema-studio-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kema Studio Com Domain Security
  slug: kema-studio-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kema-studio-com
tags:
- Software
- Management
- Artificial Intelligence
- Portugal
- Software-as-a-Service
website: https://kema-studio.com/
---

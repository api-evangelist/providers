---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://app.super.mx
  baseurl_source: declared
  description: The Quotes API from Super Seguros — 1 operation(s) for quotes.
  name: Super Seguros Quotes API
  slug: super-seguros-quotes-api
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Super Seguros Quotes API
  slug: open-super-seguros-quotes-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/super-seguros-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/super-seguros-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/super-seguros-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.super.mx/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.super.mx/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.super.mx/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.super.mx/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.super.mx/reference/bobbywebapiv2quotecontrollerindex
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/super-seguros-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/super-seguros-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/super-seguros-openapi-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/super-seguros-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/super-seguros-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/super-seguros-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/super-seguros-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/super-seguros-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/super-seguros-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Super Seguros (super.mx) is a Mexican insurtech that lets people quote, buy, and manage insurance entirely online. Its developer product, Super Studio, is a set of REST APIs partners use to generate insurance quotes and sell policies — covering life insurance (12-month term and 5-year plans with savings), home, renters, and landlord products. Quoting endpoints are broadly available and return prefilled purchase links to super.mx; purchase endpoints let approved partners sell insurance directly via API. Authentication is via an X-Api-Key header, with separate sandbox and production hosts. Super Seguros is backed by Anthemis.
image: https://www.super.mx/src/assets/super_midoconline_fav.ico
layout: provider
modified: '2026-07-21'
name: Super Seguros
nav: Providers
network: true
overview: 'Super Seguros publishes 1 API on the [APIs.io](https://apis.io/) network: Quotes API. Tagged areas include Company, Insurance, Insurtech, Life Insurance, and Quotes.


  Super Seguros'' developer surface includes authentication, documentation, getting-started guide, API reference, sandbox, and 13 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 55.1
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 29.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/super-seguros/refs/heads/main/screenshots/super-seguros-2026-09-02T161203.png
security:
- kind: authentication
  name: Super Seguros Authentication
  slug: super-seguros-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Super Seguros Domain Security
  slug: super-seguros-domain-security
  summary_line: TLSv1.3 · HSTS
slug: super-seguros
tags:
- Company
- Insurance
- Insurtech
- Life Insurance
- Quotes
- Mexico
- Financial-Services
- Super Studio
website: https://www.super.mx/
---

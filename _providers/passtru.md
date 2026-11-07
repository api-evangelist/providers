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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/passtru/llms/passtru-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/passtru-llms.txt
- group: other
  href: https://artifacts.apis.io/passtru/hosts/passtru-hosts.yml
  title: ''
  type: Hosts
  url: hosts/passtru-hosts.yml
- group: other
  href: https://artifacts.apis.io/passtru/vendors/passtru-vendors.yml
  title: ''
  type: Vendors
  url: vendors/passtru-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://passtru.io/en/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://passtru.io/en/auth/login
- group: start
  title: ''
  type: GettingStarted
  url: https://passtru.io/en/developers/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://passtru.io/llms.txt
- group: auth
  href: https://artifacts.apis.io/passtru/security/passtru-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/passtru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://passtru.io
- group: docs
  title: ''
  type: Documentation
  url: https://passtru.io/en/developers
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://passtru.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Passtru provides identity verification services that enable users to prove who they are once and share only the necessary proof with services. It supports age verification, KYC, document verification, and sanctions screening through standard OIDC flows, public APIs, SDK helpers, signed webhooks, and receipt-aware verification flows. The platform offers developer documentation, integration guides, and resources for businesses and agents to implement secure identity proofing.
image: https://passtru.io/og-image.png
layout: provider
modified: '2026-10-21'
name: Passtru
nav: Providers
network: true
overview: 'Passtru is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Identity Verification, Age Verification, KYC, Document Verification, and Sanctions Screening.


  Passtru''s developer surface includes getting-started guide, API reference, documentation, and 7 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 15.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/passtru/passtru-2026-11-03T140948.png
security:
- kind: domain-security
  name: Passtru Domain Security
  slug: passtru-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: passtru
tags:
- Identity Verification
- Age Verification
- KYC
- Document Verification
- Sanctions Screening
website: https://passtru.io
---

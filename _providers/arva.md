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
    dynamic_client_registration: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Arva AI platform API for banking decision automation
  name: Arva API
  slug: arva-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/arva/well-known/arva-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arva-well-known.yml
- group: other
  href: https://artifacts.apis.io/arva/hosts/arva-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arva-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://arva.ai/trust
- group: company
  title: ''
  type: Newsroom
  url: https://arva.ai/press
- group: start
  title: ''
  type: Login
  url: https://arva.ai/login
- group: auth
  href: https://artifacts.apis.io/arva/security/arva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arva-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arva.ai/
- group: company
  title: ''
  type: Blog
  url: https://arva.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://arva.ai/platform/agentstudio
- group: docs
  title: ''
  type: APIReference
  url: https://arva.ai/platform/agentcore
- group: start
  title: ''
  type: GettingStarted
  url: https://arva.ai/book-a-demo
- group: operate
  title: ''
  type: Support
  url: https://arva.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arva.ai/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arva.ai/legal/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: API documentation redirects to a login page requiring partner credentials
  evidence:
  - status: 200
    url: https://docs.arva.ai/login?redirect=%2F
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Arva AI provides advanced artificial intelligence solutions for banking decisions, offering research-driven models that automate high‑risk financial processes such as fraud detection, compliance, and lending. Their platform delivers accurate, scalable AI agents that integrate into banking operations, trusted by regulated institutions worldwide. Arva’s technology aims to move critical decisions beyond human‑in‑the‑loop, enhancing efficiency and security across the financial sector.
image: https://framerusercontent.com/images/Vw8hmk7y9elurzUNj3IRstU8.jpg
layout: provider
modified: '2026-10-29'
name: Arva
nav: Providers
network: true
overview: 'Arva is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Banking, Fintech, and Machine Learning.


  Arva''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 58.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/arva/arva-2026-11-03T121141.png
security:
- kind: domain-security
  name: Arva Domain Security
  slug: arva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arva
tags:
- Company
- Artificial Intelligence
- Banking
- Fintech
- Machine Learning
website: https://www.arva.ai/
---

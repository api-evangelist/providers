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
    agent_card: near-conformant
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-09-19'
api_count: 1
apis:
- description: Real-time AI news, model pricing, service status, and agent activity feeds
  name: TensorFeed
  slug: tensorfeed
artifact_total: 3
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tensorfeed/refs/heads/main/a2a/tensorfeed-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tensorfeed-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tensorfeed/refs/heads/main/security/tensorfeed-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tensorfeed-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tensorfeed/refs/heads/main/security/tensorfeed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tensorfeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tensorfeed.ai/developers
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: operate
  title: ''
  type: Support
  url: mailto:contact@tensorfeed.ai
created: '2026-05-28'
description: Real-time AI news, model pricing, service status, and agent activity feeds
layout: provider
modified: '2026-05-28'
name: TensorFeed
nav: Providers
network: true
overview: 'TensorFeed publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Machine-Learning and Public APIs.


  TensorFeed''s developer surface includes support and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 53.7
    operational_transparency: 0.0
  previous_composite: 8.2
  provenance:
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/tensorfeed/refs/heads/main/screenshots/tensorfeed-2026-06-20T195119.png
security:
- kind: domain-security
  name: Tensorfeed Domain Security
  slug: tensorfeed-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Tensorfeed Vulnerability Disclosure
  slug: tensorfeed-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tensorfeed
tags:
- Machine-Learning
- Public APIs
website: https://tensorfeed.ai/developers
---

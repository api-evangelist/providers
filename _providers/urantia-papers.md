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
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-09-18'
api_count: 1
apis:
- description: Full-text + semantic search across the Urantia Papers, with audio narration, entities, translations
  name: Urantia Papers
  slug: urantia-papers
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/urantia-papers/refs/heads/main/a2a/urantia-papers-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/urantia-papers-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/urantia-papers/refs/heads/main/security/urantia-papers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/urantia-papers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://urantia.dev
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: operate
  title: ''
  type: Support
  url: https://urantia.dev/support
created: '2026-05-28'
description: Full-text + semantic search across the Urantia Papers, with audio narration, entities, translations
layout: provider
modified: '2026-05-28'
name: Urantia Papers
nav: Providers
network: true
overview: 'Urantia Papers publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Books and Public APIs.


  Urantia Papers'' developer surface includes support and 4 more developer resources.'
random_paper: 0
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
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/urantia-papers/refs/heads/main/screenshots/urantia-papers-2026-06-20T200543.png
security:
- kind: domain-security
  name: Urantia Papers Domain Security
  slug: urantia-papers-domain-security
  summary_line: TLSv1.3 · HSTS
slug: urantia-papers
tags:
- Books
- Public APIs
website: https://urantia.dev
---

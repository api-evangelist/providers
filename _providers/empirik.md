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
- description: Empirik API – no public machine‑readable contract discovered.
  name: Empirik API
  slug: empirik-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/empirik/hosts/empirik-hosts.yml
  title: ''
  type: Hosts
  url: hosts/empirik-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://empirik.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://empirik.ai/privacy-policy
- group: auth
  href: https://artifacts.apis.io/empirik/security/empirik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/empirik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://empirik.ai/
- group: company
  title: ''
  type: Blog
  url: https://empirik.ai/blog
coverage:
  checked: '2026-10-29'
  detail: Empirik's website provides product information but no public OpenAPI, AsyncAPI, GraphQL, or other machine‑readable API specification.
  evidence:
  - status: 0
    url: https://empirik.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Empirik provides a change observability platform that gives AI agents operational context to understand dependencies, ownership, changes, and risk. Trusted by platform and engineering teams, it enables system‑aware AI coding, risk assessment, and improved developer productivity across modern software ecosystems.
image: https://empirik.ai/empirik_og1.jpg
layout: provider
modified: '2026-10-28'
name: Empirik
nav: Providers
network: true
overview: 'Empirik is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Observability, Change Management, and Platform Engineering.


  Empirik''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/empirik/empirik-2026-11-03T131500.png
security:
- kind: domain-security
  name: Empirik Domain Security
  slug: empirik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: empirik
tags:
- Company
- Artificial Intelligence
- Observability
- Change Management
- Platform Engineering
website: https://empirik.ai/
---

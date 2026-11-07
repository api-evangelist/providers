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
- description: Keen provides an Event Streaming API for collecting, storing, and querying event data.
  name: Keen Event Streaming API
  slug: keen-event-streaming-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/keen-technologies/hosts/keen-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/keen-technologies-hosts.yml
- group: other
  href: https://artifacts.apis.io/keen-technologies/vendors/keen-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/keen-technologies-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://keenagi.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://keenagi.com/privacy/
- group: auth
  href: https://artifacts.apis.io/keen-technologies/security/keen-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keen-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keenagi.com/
coverage:
  checked: '2026-10-23'
  detail: API documentation pages are rendered via JavaScript and no OpenAPI spec is publicly accessible.
  evidence:
  - status: 200
    url: https://keen.io/docs/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Keen Technologies is an AI research and development company focused on building artificial general intelligence (AGI). The firm runs a public website keenagi.com that showcases its research projects, team, and mission to advance AI capabilities responsibly. It is backed by Sequoia Capital and listed in the API Evangelist harvest backlog.
image: https://keenagi.com/icons/keen-logo.svg
layout: provider
modified: '2026-10-23'
name: Keen Technologies
nav: Providers
network: true
overview: Keen Technologies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Research, AGI, and Technology.
random_paper: 20
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.6
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
screenshot: https://apis.io/screenshots/keen-technologies/keen-technologies-2026-11-03T134338.png
security:
- kind: domain-security
  name: Keen Technologies Domain Security
  slug: keen-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: keen-technologies
tags:
- Company
- Artificial Intelligence
- Research
- AGI
- Technology
website: https://keenagi.com/
---

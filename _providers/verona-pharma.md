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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/verona-pharma/hosts/verona-pharma-hosts.yml
  title: ''
  type: Hosts
  url: hosts/verona-pharma-hosts.yml
- group: auth
  href: https://artifacts.apis.io/verona-pharma/security/verona-pharma-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/verona-pharma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.veronapharma.com
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the API host.
  evidence:
  - status: 0
    url: https://api.veronapharma.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Verona Pharma is a biopharmaceutical company focused on developing innovative therapies for rare diseases. The company leverages advanced drug discovery platforms and collaborates with academic institutions to bring novel treatments to market. Founded with a mission to address unmet medical needs, Verona Pharma aims to improve patient outcomes through rigorous research, clinical development, and strategic partnerships across the healthcare ecosystem.
layout: provider
modified: '2026-10-26'
name: Verona Pharma
nav: Providers
network: true
overview: Verona Pharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 9
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 2.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/verona-pharma/verona-pharma-2026-11-03T145725.png
security:
- kind: domain-security
  name: Verona Pharma Domain Security
  slug: verona-pharma-domain-security
  summary_line: DMARC
slug: verona-pharma
tags:
- Company
website: https://www.veronapharma.com
---

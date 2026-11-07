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
- description: API for AIEGIS identity, governance, and visibility platform as described in the developer docs.
  name: AIEGIS API
  slug: aiegis-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/aiegis-ie/hosts/aiegis-ie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiegis-ie-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiegis-ie/vendors/aiegis-ie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiegis-ie-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://aiegis.ie/status
- group: start
  title: ''
  type: GettingStarted
  url: https://aiegis.ie/get-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aiegis.ie/developer
- group: company
  title: ''
  type: Blog
  url: https://aiegis.ie/blog
- group: auth
  href: https://artifacts.apis.io/aiegis-ie/security/aiegis-ie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiegis-ie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiegis.ie/
coverage:
  checked: '2026-10-30'
  detail: Developer documentation provides HTML pages but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://aiegis.ie/developer
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: AIEGIS provides universal identity, governance, and visibility solutions for autonomous AI agents. It enables businesses to assign verifiable identities to AI agents, enforce real‑time policy compliance, and record tamper‑evident evidence of actions. The platform offers a single /api/protect endpoint that evaluates requests across fifteen security layers, including identity verification, instruction integrity, data protection, and human‑review routing, helping organizations trust and control AI‑driven operations.
image: https://aiegis.ie/logo-512.png
layout: provider
modified: '2026-10-29'
name: aiegis-ie
nav: Providers
network: true
overview: 'aiegis-ie is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Identity, Governance, and Security.


  aiegis-ie''s developer surface includes getting-started guide, engineering blog, and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aiegis-ie/aiegis-ie-2026-11-03T120457.png
security:
- kind: domain-security
  name: Aiegis Ie Domain Security
  slug: aiegis-ie-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aiegis-ie
tags:
- Company
- Artificial Intelligence
- Identity
- Governance
- Security
website: https://aiegis.ie/
---

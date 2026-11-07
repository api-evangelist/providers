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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Matterworks platform API (no public machine‑readable specification found).
  name: Matterworks API
  slug: matterworks-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/matterworksbio-com/hosts/matterworksbio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/matterworksbio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/matterworksbio-com/vendors/matterworksbio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/matterworksbio-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/matterworksbio
- group: auth
  href: https://artifacts.apis.io/matterworksbio-com/security/matterworksbio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/matterworksbio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.matterworksbio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.matterworksbio.com/news-insights
coverage:
  checked: '2026-10-29'
  detail: No public OpenAPI, AsyncAPI, GraphQL, or other machine‑readable API specification was found on the provider's website or documented hosts.
  evidence:
  - status: 404
    url: https://www.matterworks.ai/openapi.json
  - status: 404
    url: https://www.matterworks.ai/.well-known/agent-card.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Matterworks is an AI-driven platform that transforms biology by applying predictive omics and frontier AI to accelerate drug discovery, safety, and manufacturing. Their platform aims to make biological outcomes foreseeable, reducing the high failure rates and costs of drug development. By integrating large-scale omics data with machine learning, Matterworks provides insights that guide research and development across the life sciences pipeline.
image: https://framerusercontent.com/images/EzzcVsOCX5scOlfonoIaR499SWw.png?width=2008&height=381
layout: provider
modified: '2026-10-29'
name: Matterworks
nav: Providers
network: true
overview: 'Matterworks is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Biology, Life Sciences, and Predictive Omics.


  Matterworks'' developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Matterworksbio Com Plans Pricing
  plan_count: 0
  slug: matterworksbio-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Matterworksbio Com Rate Limits
  slug: matterworksbio-com-rate-limits
scopes:
- name: Matterworksbio Com Scopes
  scope_count: 0
  slug: matterworksbio-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.6
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/matterworksbio-com/matterworksbio-com-2026-11-03T135352.png
security:
- kind: authentication
  name: Matterworksbio Com Authentication
  slug: matterworksbio-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Matterworksbio Com Domain Security
  slug: matterworksbio-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: matterworksbio-com
tags:
- Company
- Artificial Intelligence
- Biology
- Life Sciences
- Predictive Omics
- Drug Discovery
website: https://www.matterworksbio.com/
---

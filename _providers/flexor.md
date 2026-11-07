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
- group: agent
  href: https://artifacts.apis.io/flexor/llms/flexor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flexor-llms.txt
- group: other
  href: https://artifacts.apis.io/flexor/hosts/flexor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flexor-hosts.yml
- group: other
  href: https://artifacts.apis.io/flexor/vendors/flexor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flexor-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://flexor.ai/news/flexor-snowflake-integration/
- group: auth
  href: https://artifacts.apis.io/flexor/security/flexor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flexor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flexor.ai/
- group: company
  title: ''
  type: Blog
  url: https://flexor.ai/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flexor.ai/privacy-policy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://flexor.ai/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Flexor AI provides an enterprise data platform that transforms unstructured data into AI‑ready context. Their solution automates data preparation, structuring, and retrieval, delivering higher accuracy, lower token costs, and sub‑second latency for AI agents across industries such as finance, healthcare, and manufacturing.
image: https://flexor.ai/wp-content/uploads/2026/05/Flexor-Open-Graph-Image.jpg
layout: provider
modified: '2026-10-20'
name: Flexor
nav: Providers
network: true
overview: 'Flexor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Data Platform, Enterprise, and Unstructured Data.


  Flexor''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 56.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Flexor Domain Security
  slug: flexor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: flexor
tags:
- Company
- Artificial Intelligence
- Data Platform
- Enterprise
- Unstructured Data
website: https://flexor.ai/
---

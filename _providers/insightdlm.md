---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/insightdlm/hosts/insightdlm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/insightdlm-hosts.yml
- group: other
  href: https://artifacts.apis.io/insightdlm/vendors/insightdlm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/insightdlm-vendors.yml
- group: auth
  href: https://artifacts.apis.io/insightdlm/security/insightdlm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/insightdlm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://insightdlm.com/
- group: operate
  title: ''
  type: Contact
  url: https://insightdlm.com/contact.html
- group: company
  title: ''
  type: About
  url: https://insightdlm.com/about.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insightdlm.com/privacy-policy.html
coverage:
  checked: '2026-10-18'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found after probing known API host endpoints.
  evidence:
  - status: 0
    url: https://api.insightdlm.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: Insightprompts, operating as InsightDLM, provides an end‑to‑end framework for building domain‑specific fine‑tuned language models across verticals such as insurance, retail, banking, healthcare, legal, manufacturing and more. The platform curates enterprise data, generates high‑quality training sets, fine‑tunes both small and large models, evaluates them rigorously, and deploys them securely within an organization. It offers connectors to common data sources, robust data processing, and tools for monitoring model drift and cost.
layout: provider
modified: '2026-10-17'
name: Insightprompts
nav: Providers
network: true
overview: Insightprompts is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, Data Processing, and Vertical Solutions.
random_paper: 19
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 5.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Insightdlm Domain Security
  slug: insightdlm-domain-security
  summary_line: TLSv1.3
slug: insightdlm
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Data Processing
- Vertical Solutions
- Enterprise
website: https://insightdlm.com/
---

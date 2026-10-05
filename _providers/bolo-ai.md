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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bolo-ai/refs/heads/main/hosts/bolo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bolo-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bolo-ai/refs/heads/main/vendors/bolo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bolo-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.bolo.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bolo-ai/refs/heads/main/security/bolo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bolo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bolo.ai
- group: company
  title: ''
  type: Blog
  url: https://bolo.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://bolo.ai/about-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bolo.ai/privacy-policy
coverage:
  checked: '2026-10-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found at api.bolo.ai or bolo.ai.
  evidence:
  - status: 0
    url: https://api.bolo.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Bolo.ai provides a context layer that enables agentic AI to work effectively in heavy industry. By embedding directly into existing industrial software and workflows, Bolo captures operational data and institutional knowledge, ensuring AI models have reliable, domain‑specific context. This platform helps preserve expertise, improve safety, and accelerate decision‑making across sectors such as energy, manufacturing, and infrastructure.
layout: provider
modified: '2026-10-02'
name: Bolo.ai
nav: Providers
network: true
overview: 'Bolo.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Industrial, Data, and Context.


  Bolo.ai''s developer surface includes engineering blog, documentation, and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bolo Ai Domain Security
  slug: bolo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bolo-ai
tags:
- Company
- Artificial Intelligence
- Industrial
- Data
- Context
website: https://bolo.ai
---

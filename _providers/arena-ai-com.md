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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/arena-ai-com/hosts/arena-ai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arena-ai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arena-ai-com/vendors/arena-ai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arena-ai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arenaphysica.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arenaphysica.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.arenaphysica.com/news
- group: auth
  href: https://artifacts.apis.io/arena-ai-com/security/arena-ai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arena-ai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arenaphysica.com/
coverage:
  checked: '2026-10-22'
  detail: No OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL files were found on the website.
  evidence:
  - status: 404
    url: https://www.arenaphysica.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Arena AI is a venture‑backed startup focused on building AI‑driven platforms for enterprise decision‑making and data integration. The company aims to provide modular, scalable AI services that can be embedded into existing workflows, offering APIs for model inference, data enrichment, and analytics. Backed by Initialized Capital, Arena AI targets sectors such as finance, healthcare, and logistics, emphasizing privacy‑preserving machine learning and robust API security.
image: https://cdn.sanity.io/images/dxvtl5a1/production/46fbcaa3d2825b856822096129abdf518dd37347-2400x1260.png?w=1200&h=630
layout: provider
modified: '2026-10-22'
name: Arena AI
nav: Providers
network: true
overview: Arena AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Enterprise, Data, and Analytics.
random_paper: 2
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arena Ai Com Domain Security
  slug: arena-ai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arena-ai-com
tags:
- Company
- AI
- Enterprise
- Data
- Analytics
website: https://www.arenaphysica.com/
---

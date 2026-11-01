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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Machine‑readable catalog API providing dataset listings and package metadata.
  name: DataForge API
  slug: dataforge-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/zalize-com/llms/zalize-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zalize-com-llms.txt
- group: other
  href: https://artifacts.apis.io/zalize-com/hosts/zalize-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zalize-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/zalize-com/vendors/zalize-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zalize-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/zalize-com/security/zalize-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zalize-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zalize.com/
- group: company
  title: ''
  type: Blog
  url: https://zalize.com/posts/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zalize.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zalize.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://zalize.com/join/
coverage:
  checked: '2026-10-30'
  detail: Provider's docs list JSON endpoints (e.g., /catalog.json) but no OpenAPI or other machine-readable spec is published.
  evidence:
  - status: 200
    url: https://data.zalize.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Zalize is an independent studio that showcases selected AI platforms, full‑stack products, games, and open-source engineering. It focuses on curating AI tools, building open-source projects, and providing resources for developers and creators. The studio emphasizes honesty, transparency, and community‑driven values, as outlined in its purpose and values pages.
image: https://zalize.com/static/brand/og.png?v=5
layout: provider
modified: '2026-10-30'
name: zalize-com
nav: Providers
network: true
overview: 'zalize-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Studio, Open-Source, Engineering, and Products.


  zalize-com''s developer surface includes engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Zalize Com Plans Pricing
  plan_count: 0
  slug: zalize-com-plans-pricing
random_paper: 11
scopes:
- name: Zalize Com Scopes
  scope_count: 0
  slug: zalize-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zalize Com Authentication
  slug: zalize-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Zalize Com Domain Security
  slug: zalize-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: zalize-com
tags:
- AI
- Studio
- Open-Source
- Engineering
- Products
- Games
website: https://zalize.com/
---

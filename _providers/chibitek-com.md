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
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Explore AI-driven managed IT solutions with Chibitek.
  name: ChibiTek API
  slug: chibitek-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/chibitek-com/llms/chibitek-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chibitek-com-llms.txt
- group: other
  href: https://artifacts.apis.io/chibitek-com/hosts/chibitek-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chibitek-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/chibitek-com/vendors/chibitek-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chibitek-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chibitek
- group: auth
  href: https://artifacts.apis.io/chibitek-com/security/chibitek-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chibitek-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chibitek.com/
- group: company
  title: ''
  type: Blog
  url: https://www.chibitek.com/blog
- group: company
  title: ''
  type: BlogFeed
  url: https://www.chibitek.com/blog-feed.xml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chibitek.com
- group: docs
  title: ''
  type: APIReference
  url: https://api.chibitek.com
coverage:
  checked: '2026-10-30'
  detail: Documentation pages redirect to a login portal, preventing access to API specifications.
  evidence:
  - status: 200
    url: https://docs.chibitek.com/admin/documentation
  reason: customer-only-docs
  state: gated
created: '2026-10-29'
description: Chibitek is an AI‑first managed intelligence provider delivering AI‑driven managed IT solutions across the United States. It offers scalable, automated IT support, infrastructure monitoring, and custom MSP packages designed to help businesses grow efficiently and securely.
image: https://static.wixstatic.com/media/0a47c7_29235adee93d4b7b818cf0c5835b609d%7Emv2.png
layout: provider
modified: '2026-10-29'
name: chibitek-com
nav: Providers
network: true
overview: 'chibitek-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Managed Service, IT Support, and Cloud.


  chibitek-com''s developer surface includes engineering blog, documentation, API reference, and 7 more developer resources.'
plans:
- name: Chibitek Com Plans Pricing
  plan_count: 0
  slug: chibitek-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Chibitek Com Rate Limits
  slug: chibitek-com-rate-limits
scopes:
- name: Chibitek Com Scopes
  scope_count: 0
  slug: chibitek-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/chibitek-com/chibitek-com-2026-11-03T124012.png
security:
- kind: authentication
  name: Chibitek Com Authentication
  slug: chibitek-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Chibitek Com Domain Security
  slug: chibitek-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chibitek-com
tags:
- Company
- Artificial Intelligence
- Managed Service
- IT Support
- Cloud
website: https://chibitek.com/
---

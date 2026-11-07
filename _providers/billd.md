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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/billd/llms/billd-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billd-llms.txt
- group: other
  href: https://artifacts.apis.io/billd/hosts/billd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billd-hosts.yml
- group: other
  href: https://artifacts.apis.io/billd/vendors/billd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billd-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.billd.com/
- group: company
  title: ''
  type: Newsroom
  url: https://billd.com/press/
- group: start
  title: ''
  type: Login
  url: https://billd.com/login/
- group: other
  title: ''
  type: Leadership
  url: https://billd.com/team/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.billd.com/topic/get-started/
- group: auth
  href: https://artifacts.apis.io/billd/security/billd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://billd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://billd.com/about/
- group: company
  title: ''
  type: Blog
  url: https://billd.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://billd.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://billd.com/privacy/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: error
    url: https://api.billd.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Billd provides construction financing solutions for subcontractors, offering flexible lines of credit and pay‑app advances to help contractors manage cash flow, purchase materials, and grow their businesses. The platform connects subcontractors with lenders, delivering predictable payments and working‑capital tools tailored to the construction industry.
image: https://billd.com/images/og-default.jpg
layout: provider
modified: '2026-10-28'
name: Billd
nav: Providers
network: true
overview: 'Billd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Financing, Subcontractors, Working Capital, and Billd.


  Billd''s developer surface includes support, getting-started guide, documentation, engineering blog, and 10 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 18.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/billd/billd-2026-11-03T121720.png
security:
- kind: domain-security
  name: Billd Domain Security
  slug: billd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: billd
tags:
- Construction
- Financing
- Subcontractors
- Working Capital
- Billd
website: https://billd.com/
---

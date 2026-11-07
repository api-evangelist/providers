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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/6ix-com/llms/6ix-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/6ix-com-llms.txt
- group: other
  href: https://artifacts.apis.io/6ix-com/hosts/6ix-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/6ix-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/6ix-com/vendors/6ix-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/6ix-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://6ix.com/news
- group: auth
  href: https://artifacts.apis.io/6ix-com/security/6ix-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/6ix-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://6ix.com/
- group: company
  title: ''
  type: Blog
  url: https://6ix.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://6ix.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://6ix.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://6ix.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://6ix.com/contact
- group: docs
  title: ''
  type: APIReference
  url: https://6ix.com/api
coverage:
  checked: '2026-10-31'
  detail: API reference endpoint returns only a welcome JSON with no OpenAPI or other contract discovered.
  evidence:
  - status: 200
    url: https://6ix.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: 6ix is a global library of public companies, providing news releases, earnings calls, decks and charts for over 54,000 companies. Founded in 2016 and operated by 6ix Inc. in Miami and Toronto, the platform offers AI-driven alerts, email notifications, and tools for investors and companies to share information. The service is free for investors and offers paid solutions for companies to manage their investor relations.
image: https://6ix.com/images/social-banner.png?v=2
layout: provider
modified: '2026-10-31'
name: 6ix
nav: Providers
network: true
overview: '6ix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Data, Investor Relations, and News.


  6ix''s developer surface includes engineering blog, pricing, support, API reference, and 8 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 49.1
    operational_transparency: 0.0
  previous_composite: 14.0
  provenance:
    mcp: unknown
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
security:
- kind: domain-security
  name: 6Ix Com Domain Security
  slug: 6ix-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 6ix-com
tags:
- Company
- Finance
- Data
- Investor Relations
- News
website: https://6ix.com/
---

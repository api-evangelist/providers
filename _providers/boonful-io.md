---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
  score: 0.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP API providing tool list and other studio functions.
  name: Boonful Studio API
  slug: boonful-studio-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/boonful-io/plans/boonful-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boonful-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/boonful-io/llms/boonful-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boonful-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/boonful-io/mcp/boonful-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/boonful-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/boonful-io/hosts/boonful-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boonful-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/boonful-io/vendors/boonful-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boonful-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://boonful.io/login
- group: auth
  href: https://artifacts.apis.io/boonful-io/security/boonful-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boonful-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boonful.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://boonful.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boonful.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boonful.io/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://boonful.io/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://boonful.io/guides
created: '2026-11-02'
description: Boonful is a publishing platform that enables creators to build, sell, and manage digital products such as books, courses, videos, podcasts, newsletters, and apps. It offers tools for product creation, audience discovery, payment processing via Stripe, and automated marketing features. The service emphasizes a no‑code approach, AI‑assisted content generation, and integrated scheduling across social channels, aiming to help creators monetize their work without technical barriers.
image: https://boonful.io/demo/og-home.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at api.boonful.io.
  name: Boonful MCP Server
  slug: boonful-io-mcp-yml
modified: '2026-11-02'
name: Boonful
nav: Providers
network: true
overview: 'Boonful is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Publishing, Software-as-a-Service, E-Commerce, Content Creation, and No-Code.


  Boonful''s developer surface includes pricing, documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Boonful Io Plans Pricing
  plan_count: 4
  slug: boonful-io-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 65.0
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boonful Io Domain Security
  slug: boonful-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boonful-io
tags:
- Publishing
- Software-as-a-Service
- E-Commerce
- Content Creation
- No-Code
website: https://boonful.io/
---

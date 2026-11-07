---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 18.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Machine Control Protocol (MCP) providing tool list for AI generation.
  name: BananaBanana MCP
  slug: bananabanana-mcp
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/bananabanana-pro/plans/bananabanana-pro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bananabanana-pro-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bananabanana-pro/llms/bananabanana-pro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bananabanana-pro-llms.txt
- group: agent
  href: https://artifacts.apis.io/bananabanana-pro/mcp/bananabanana-pro-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bananabanana-pro-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bananabanana-pro/well-known/bananabanana-pro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bananabanana-pro-well-known.yml
- group: other
  href: https://artifacts.apis.io/bananabanana-pro/hosts/bananabanana-pro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bananabanana-pro-hosts.yml
- group: other
  href: https://artifacts.apis.io/bananabanana-pro/vendors/bananabanana-pro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bananabanana-pro-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bananabanana-pro/security/bananabanana-pro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bananabanana-pro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bananabanana.pro/
- group: company
  title: ''
  type: Blog
  url: https://bananabanana.pro/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bananabanana.pro/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bananabanana.pro/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bananabanana.pro/privacy
- group: start
  title: ''
  type: SignUp
  url: https://bananabanana.pro/register
- group: start
  title: ''
  type: Login
  url: https://bananabanana.pro/
created: '2026-11-02'
description: BananaBanana, operated by Rari LTD in Tbilisi, Georgia, offers metered access to AI image, video, and speech generation models from Google, OpenAI, Alibaba, and xAI. Users top up a balance; each generation deducts its price (images from $0.03, video from $0.10, speech from $1.00) with no subscription and balances never expire. The service is independent, not affiliated with Google, and supports crypto and card payments.
image: https://bananabanana.pro/logo-email.png
layout: provider
mcp_servers:
- description: Remote MCP server at bananabanana.pro.
  name: BananaBanana MCP Server
  slug: bananabanana-pro-mcp-yml
modified: '2026-11-02'
name: BananaBanana
nav: Providers
network: true
overview: 'BananaBanana is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Image Generation, Video Generation, Speech, and Crypto Payments.


  BananaBanana''s developer surface includes engineering blog, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Bananabanana Pro Plans Pricing
  plan_count: 1
  slug: bananabanana-pro-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 19.7
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 13.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bananabanana Pro Domain Security
  slug: bananabanana-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bananabanana-pro
tags:
- Artificial Intelligence
- Image Generation
- Video Generation
- Speech
- Crypto Payments
website: https://bananabanana.pro/
---

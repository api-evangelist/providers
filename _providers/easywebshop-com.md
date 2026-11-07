---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Machine-readable MCP tool list for EasyWebshop, providing website creation and related operations.
  name: EasyWebshop MCP
  slug: easywebshop-mcp
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/easywebshop-com/plans/easywebshop-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/easywebshop-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/easywebshop-com/llms/easywebshop-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easywebshop-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/easywebshop-com/mcp/easywebshop-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/easywebshop-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/easywebshop-com/hosts/easywebshop-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easywebshop-com-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://easywebshop.com/software/signup
- group: auth
  href: https://artifacts.apis.io/easywebshop-com/security/easywebshop-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easywebshop-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easywebshop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://easywebshop.com/create-online-store
- group: commercial
  title: ''
  type: Pricing
  url: https://easywebshop.com/price
- group: company
  title: ''
  type: Blog
  url: https://easywebshop.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easywebshop.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://easywebshop.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://easywebshop.com/software/contact
created: '2026-11-06'
description: EasyWebshop provides user‑friendly, affordable software to create professional websites and webshops. Their platform offers a range of templates, e‑commerce tools, and a privacy‑first approach with no ads or trackers. Customers can start with a free plan or choose paid tiers for advanced features, and the service includes support, POS integration, and reservation tools, making it a comprehensive solution for small businesses and entrepreneurs.
layout: provider
mcp_servers:
- description: Remote MCP server at easywebshop.com.
  name: EasyWebshop MCP Server
  slug: easywebshop-com-mcp-yml
modified: '2026-11-06'
name: EasyWebshop
nav: Providers
network: true
overview: 'EasyWebshop is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Website Builder, Software-as-a-Service, Small Business, and Point-of-Sale.


  EasyWebshop''s developer surface includes signup flow, documentation, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Easywebshop Com Plans Pricing
  plan_count: 4
  slug: easywebshop-com-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Easywebshop Com Domain Security
  slug: easywebshop-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: easywebshop-com
tags:
- E-Commerce
- Website Builder
- Software-as-a-Service
- Small Business
- Point-of-Sale
- Reservations
website: https://easywebshop.com/
---

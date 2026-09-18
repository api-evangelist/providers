---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-09-17'
api_count: 1
apis:
- baseURL: https://api.nexscope.ai
  baseurl_source: declared
  description: Proprietary REST skill API (OpenAPI 3.1) with 225 POST operations at /api/skill-api/v1/skills/{skill}/run, bearer API-key auth, a credit-based usage model, and a matching remote MCP server.
  name: Nexscope Ecommerce Data and Creative APIs
  slug: nexscope-ecommerce-data-and-creative-apis
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nexscope/refs/heads/main/security/nexscope-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nexscope-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nexscope/refs/heads/main/authentication/nexscope-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nexscope-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nexscope/refs/heads/main/packages/nexscope-packages.yml
  title: ''
  type: Packages
  url: packages/nexscope-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nexscope/refs/heads/main/packages/nexscope-packages.yml
  title: ''
  type: SDKs
  url: packages/nexscope-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nexscope/refs/heads/main/llms/nexscope-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nexscope-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nexscope/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.nexscope.ai/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.nexscope.ai/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nexscope.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.nexscope.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nexscope-ai
- group: start
  title: ''
  type: SignUp
  url: https://www.nexscope.ai/seller/api-access
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nexscope.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nexscope.ai/privacy
- group: company
  title: ''
  type: Website
  url: https://www.nexscope.ai
created: '2026-09-16'
description: Nexscope is an ecommerce data and creative-AI platform for marketplace sellers. Its public REST + MCP surface exposes 225 skill operations spanning Amazon marketplace intelligence, keyword and search-demand research, TikTok/social commerce, Temu, Shopify, Etsy, Ozon, eBay, Shopee and 1688 data, patent/IP risk, and creative generation (studio product images, background removal, virtual try-on, and short-form product video) across model families such as Seedream, Seedance, Kling, Wan and GPT-Image. Authentication is a bearer Nexscope API key and usage is credit-based; data skills return synchronously while creative skills run as pollable async tasks. The same catalog is exposed to AI agents over a remote MCP endpoint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: Official remote MCP server exposing Nexscope's ecommerce data and creative skills to AI agents (Claude, ChatGPT, others). Implements JSON-RPC 2.0 (initialize, tools/list, tools/call) over HTTPS. The t
  name: Nexscope MCP Server
  slug: nexscope-mcp-server
modified: '2026-09-16'
name: Nexscope Ecommerce Data and Creative APIs
nav: Providers
network: true
overview: 'Nexscope Ecommerce Data and Creative APIs publishes 1 API on the [APIs.io](https://apis.io/) network: Nexscope Ecommerce Data and Creative APIs. Tagged areas include E-Commerce, Data, Creative, Artificial Intelligence, and Marketplace Intelligence.


  Nexscope Ecommerce Data and Creative APIs'' developer surface includes authentication, documentation, pricing, engineering blog, signup flow, and 10 more developer resources.'
plans:
- name: Nexscope Plans Pricing
  plan_count: 4
  slug: nexscope-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Nexscope Rate Limits
  slug: nexscope-rate-limits
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 59.9
    developer_ergonomics: 49.4
    discoverability: 75.9
    operational_transparency: 26.3
  previous_composite: 54.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 38.9
security:
- kind: authentication
  name: Nexscope Authentication
  slug: nexscope-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nexscope Domain Security
  slug: nexscope-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nexscope
tags:
- E-Commerce
- Data
- Creative
- Artificial Intelligence
- Marketplace Intelligence
- Amazon
- TikTok
- Keyword Research
- Image-Generation
- Video Generation
- MCP
website: https://www.nexscope.ai
---

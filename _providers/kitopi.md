---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: 'The Model Context Protocol endpoint that Kitopi''s Wix-hosted website exposes for agentic AI access. It is a platform-provided (Wix) site assistant server rather than a Kitopi product API: it lets an a'
  name: Kitopi Site MCP
  slug: site-mcp
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kitopi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kitopi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.wix.com/docs/develop-websites/articles/get-started/about-the-wix-site-mcp
- group: company
  title: ''
  type: Blog
  url: https://www.kitopi.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.kitopi.com/blog-feed.xml
- group: company
  title: ''
  type: Newsroom
  url: https://www.kitopi.com/newsroom
- group: company
  title: ''
  type: About
  url: https://www.kitopi.com/our-story
- group: other
  title: ''
  type: Technology
  url: https://www.kitopi.com/tech
- group: company
  title: ''
  type: Careers
  url: https://www.kitopi.com/careers
- group: other
  title: ''
  type: JobBoard
  url: https://jobs.lever.co/kitopi/
- group: company
  title: ''
  type: Partners
  url: https://www.kitopi.com/franchise
- group: other
  title: ''
  type: Products
  url: https://www.kitopi.com/brands
- group: other
  title: ''
  type: Leadership
  url: https://www.kitopi.com/leadership
- group: operate
  title: ''
  type: Support
  url: mailto:info@kitopi.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kitopi.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kitopi.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kitopi/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/kitopihq
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/thisiskitopi/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kitopi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kitopi-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kitopi-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kitopi-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kitopi-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kitopi-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kitopi-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Kitopi is a Dubai-headquartered, tech-powered multi-brand restaurant and cloud kitchen platform that discovers, creates and curates homegrown F&B brands for the MENA region. It operates over 200 restaurant and delivery-only outlets across the UAE, Saudi Arabia, Bahrain, Qatar and Kuwait with more than 6,000 employees, and runs a Global Customer Experience center in Dubai plus a 100-plus person technology hub in Krakow, Poland. Kitopi's differentiator is its in-house Smart Kitchen Operating System (SKOS), a suite of applications that optimizes every aspect of cloud-kitchen operations in real time to maximize throughput and utilization for its restaurant partners, letting a brand scale into a new market in roughly 14 days. Kitopi is a SoftBank Vision Fund portfolio company. It publishes no public product or partner developer API; its only machine-readable surface is a Wix-provided site MCP endpoint and an llms.txt agent-access declaration on www.kitopi.com.
image: https://static.wixstatic.com/media/eef487_23715ab360904fa2b3be013b50cad3d3%7Emv2.jpg/v1/fit/w_2500,h_1330,al_c/eef487_23715ab360904fa2b3be013b50cad3d3%7Emv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: kitopi-mcp.yml
  slug: kitopi-mcpyml
modified: '2026-07-19'
name: Kitopi
nav: Providers
network: true
overview: 'Kitopi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Food and Beverage, Cloud Kitchens, and Restaurants.


  Kitopi''s developer surface includes documentation, engineering blog, support, authentication, and 23 more developer resources.'
random_paper: 86
score:
  band: emerging
  composite: 21.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 36.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 21.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kitopi/refs/heads/main/screenshots/kitopi-2026-07-25T223911.png
security:
- kind: authentication
  name: Kitopi Authentication
  slug: kitopi-authentication
  summary_line: none/bearer-visitor-token · 2 schemes
- kind: domain-security
  name: Kitopi Domain Security
  slug: kitopi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kitopi
tags:
- Company
- Consumer
- Food and Beverage
- Cloud Kitchens
- Restaurants
- Food Delivery
- Hospitality
- Middle East
- Logistics
website: https://www.kitopi.com/
---

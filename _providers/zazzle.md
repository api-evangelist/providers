---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Zazzle Agentic Access
  operation_count: 3
  slug: zazzle-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: Build a purchasable Zazzle product from a template plus partner-supplied images and text.
  name: Zazzle Create a Product API
  slug: zazzle-create-a-product-api
- description: Dynamic product mockup image rendering.
  name: Zazzle Real View API
  slug: zazzle-realview-api
- description: Maker order retrieval, acknowledgement, packing sheets and shipping labels.
  name: Zazzle Vendor API
  slug: zazzle-vendor-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zazzle Create-a-Product Create a Product API
  slug: open-zazzle-create-a-product-api
- collection_type: open
  name: Zazzle Product Image Real View API
  slug: open-zazzle-realview-api
- collection_type: open
  name: Zazzle (Maker) API v100 Vendor API
  slug: open-zazzle-vendor-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zazzle-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zazzle-create-a-product-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.zazzle.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zazzle.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.zazzle.com/sell/developers
- group: docs
  title: ''
  type: APIReference
  url: https://asset.zcache.com/assets/graphics/z4/uniquePages/zAPI/ZazzleApiGuide.v3.pdf
- group: start
  title: ''
  type: GettingStarted
  url: https://help.zazzle.com/hc/en-us/sections/360005063194-Create-A-Product-API
- group: operate
  title: ''
  type: Support
  url: https://www.zazzle.com/about/ask
- group: operate
  title: ''
  type: HelpCenter
  url: https://makerhelp.zazzle.com/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://community.zazzle.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.zazzle.com/lgn/registration
- group: start
  title: ''
  type: Login
  url: https://www.zazzle.com/lgn/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zazzle.com/sell/affiliates
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zazzle.com/terms/user_agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zazzle.com/terms/privacy_notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zazzle
- group: auth
  title: ''
  type: Security
  url: https://www.zazzle.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zazzle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zazzle-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zazzle-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zazzle-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zazzle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zazzle-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zazzle-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zazzle-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zazzle-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/zazzle-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zazzle-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zazzle-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zazzle-agentic-access.yml
created: '2026-08-05'
description: 'Zazzle is an online marketplace and on-demand manufacturing platform where independent designers, brands and shoppers create and buy customized physical products — invitations, cards, apparel, mugs, signage, business products and hundreds of other made-to-order goods. Zazzle exposes three distinct public integration surfaces rather than one general-purpose REST API: the Create-a-Product API, a URL "linkover" contract that injects a partner site''s images and text into a Zazzle product template and returns a purchasable product (or a whole "Templates Buffet" of them); the RealView image service, which renders a dynamic product mockup of that same template for preview on the partner''s own page; and the partner-gated Vendor (Maker) API, an XML RPC endpoint that Zazzle manufacturing partners use to pull new orders, acknowledge them, fetch packing sheets and print files, and buy or void Zazzle-issued shipping labels. The Create-a-Product surface is monetized through the Zazzle
  Associates/Ambassador program, with partners setting their own royalty and earning a referral share on each sale.'
image: https://asset.zcache.com/assets/graphics/z5/global/zazzle_white.svg
layout: provider
mcp_servers:
- description: ''
  name: zazzle-mcp.yml
  slug: zazzle-mcpyml
modified: '2026-08-05'
name: Zazzle
nav: Providers
network: true
overview: 'Zazzle publishes 3 APIs on the [APIs.io](https://apis.io/) network: Create a Product API, Real View API, and Vendor API. Tagged areas include Company, E-Commerce, Marketplace, Print On Demand, and Manufacturing.


  Zazzle''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, pricing, authentication, and 24 more developer resources.'
random_paper: 76
score:
  band: thin
  composite: 40.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 30.2
    developer_ergonomics: 60.3
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Zazzle Authentication
  slug: zazzle-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Zazzle Domain Security
  slug: zazzle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zazzle Vulnerability Disclosure
  slug: zazzle-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: zazzle
tags:
- Company
- E-Commerce
- Marketplace
- Print On Demand
- Manufacturing
- Retail
- Affiliate
- Custom Products
- Order Management
- Shipping
website: https://www.zazzle.com/
---

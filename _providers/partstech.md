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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Partner-facing REST API for the PartsTech parts and tire ordering platform. Covers authentication (JWT bearer via /oauth/access), parts search and part detail, brands, ACES/PCdb/VCdb taxonomy (categor
  name: PartsTech External API
  slug: partstech-external-api
artifact_total: 7
asyncapis:
- description: ''
  name: Partstech Webhooks
  slug: partstech-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://partstech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.partstech.com/openapi.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.partstech.com/openapi.yaml
- group: operate
  title: ''
  type: Support
  url: https://partstech.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://partstech.my.site.com/help/s/
- group: start
  title: ''
  type: GettingStarted
  url: https://partstech.my.site.com/help/s/article/Getting-Started-With-Partstech
- group: company
  title: ''
  type: Blog
  url: https://partstech.com/resource/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/partstech
- group: commercial
  title: ''
  type: Pricing
  url: https://partstech.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.partstech.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.partstech.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://partstech.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://partstech.com/privacy-policy/
- group: commercial
  title: ''
  type: Plans
  url: plans/partstech-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/partstech-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/partstech-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/partstech-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/partstech-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/partstech-sandbox.yml
created: '2026-08-26'
description: PartsTech is a web-based automotive parts and tire procurement platform for repair shops, tire shops and dealers, connecting more than 30,000 shops to 300+ aftermarket parts and tire suppliers across 30,000+ distribution locations through a single search, quote and ordering workflow. Founded by Greg Kirber and Erik St. Pierre and acquired by OEConnection (OEC) in 2025, PartsTech pairs its shop-facing web application with a partner-facing REST API — the PartsTech External API — used by 35+ shop management systems (SMS), point-of-sale and estimating vendors to embed parts search, VIN and license plate decoding, ACES/PCdb/VCdb taxonomy lookups, live wholesale pricing and availability, punchout carts, quoting, tire search, MOTOR and Mitchell 1 labor/maintenance content, order history and local inventory into their own software.
image: https://partstech.com/wp-content/uploads/2024/04/partstech-fb-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: PartsTech MCP Server
  slug: partstech-mcp-server
modified: '2026-08-26'
name: PartsTech
nav: Providers
network: true
overview: 'PartsTech publishes 1 API on the [APIs.io](https://apis.io/) network: External API. Tagged areas include Company, Automotive, Auto Parts, Parts Procurement, and Tires.


  The PartsTech catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PartsTech''s developer surface includes documentation, API reference, support, getting-started guide, engineering blog, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Partstech Plans Pricing
  plan_count: 3
  slug: partstech-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Partstech Rate Limits
  slug: partstech-rate-limits
score:
  band: strong
  composite: 54.4
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 16.7
    contract_quality: 59.5
    developer_ergonomics: 56.5
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 42.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Partstech Authentication
  slug: partstech-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Partstech Domain Security
  slug: partstech-domain-security
  summary_line: TLSv1.3 · DMARC
slug: partstech
tags:
- Company
- Automotive
- Auto Parts
- Parts Procurement
- Tires
- E-Commerce
- Ordering
- Catalog
- Vehicle Data
- VIN Decoding
- Shop Management
- Punchout
- Marketplace
- Supply Chain
website: https://partstech.com/
---

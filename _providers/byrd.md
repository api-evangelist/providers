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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API to create and manage products, deliveries (inbound stock), shipments (outbound orders), and returns across byrd's European fulfillment network. JWT bearer auth; JSON over HTTPS (TLS 1.2+); re
  name: byrd Fulfillment API
  slug: byrd-fulfillment-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/byrd-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/byrd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.getbyrd.com/en/vulnerability-disclosure-program
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.getbyrd.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.getbyrd.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.getbyrd.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.getbyrd.com/docs/integration-overview
- group: auth
  title: ''
  type: Authentication
  url: authentication/byrd-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.getbyrd.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.getbyrd.com/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://blog.getbyrd.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getbyrd.com/preise
- group: start
  title: ''
  type: SignUp
  url: https://www.getbyrd.com/kontakt
- group: start
  title: ''
  type: Login
  url: https://developers.getbyrd.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getbyrd.com/agbs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getbyrd.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.getbyrd.com/en/security-startpage
- group: company
  title: ''
  type: Website
  url: https://www.getbyrd.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/byrd-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: byrd is a European e-commerce fulfillment and third-party logistics (3PL) provider operating a network of 25+ fulfillment warehouses across Europe and the UK. It offers multichannel order fulfillment with integrations to the major shop and marketplace platforms (Shopify, Amazon, eBay, WooCommerce, Shopware, PlentyONE, Mirakl and more), inventory and warehouse management, carrier shipping, returns handling, and analytics. byrd exposes a developer REST API (developers.getbyrd.com) for programmatically managing products, deliveries, shipments, and returns, secured with JWT bearer authentication. byrd is a Speedinvest portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/byrd.png
layout: provider
mcp_servers:
- description: ''
  name: byrd-mcp.yml
  slug: byrd-mcpyml
modified: '2026-07-18'
name: Byrd
nav: Providers
network: true
overview: 'Byrd publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Fulfillment, Logistics, and 3PL.


  Byrd''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 13 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 0
  name: Byrd Rate Limits
  slug: byrd-rate-limits
score:
  band: thin
  composite: 33.8
  delta: -1.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 53.8
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 26.3
  previous_composite: 34.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/byrd/refs/heads/main/screenshots/byrd-2026-07-25T204138.png
security:
- kind: authentication
  name: Byrd Authentication
  slug: byrd-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Byrd Domain Security
  slug: byrd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Byrd Vulnerability Disclosure
  slug: byrd-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Byrd Trust Center
  slug: byrd-trust-center
  summary_line: trust center published
slug: byrd
tags:
- Company
- E-Commerce
- Fulfillment
- Logistics
- 3PL
- Shipping
- Warehousing
- Order Management
- Inventory
- Returns
- Supply Chain
website: https://www.getbyrd.com
---

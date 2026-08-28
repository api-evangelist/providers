---
access_model:
  confidence: high
  label: Partner
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.bevz.com/pricing
  - https://docs.bevz.com/#tag/faq
  trial: true
  try_now: false
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
  score: 31.3
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Bevz Integrator Service is a partner REST API that lets POS vendors and third-party integrators provision and manage stores on the Bevz platform programmatically. It covers store creation, provisi
  name: Bevz Integrator Service
  slug: bevz-integrator-service
artifact_total: 7
asyncapis:
- description: ''
  name: Bevz Webhooks
  slug: bevz-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bevz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bevz.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bevz.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bevz.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bevz.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bevz.com/#tag/Getting-Started
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bevz-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bevz-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bevz-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bevz-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bevz-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bevz.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://join.bevz.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bevz.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.bevz.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://22677957.hs-sites.com/en/bevz-help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bevz.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bevz.com/privacy-policy
created: '2026-07-17'
description: 'Bevz is a delivery-management platform built for liquor stores and convenience retailers that consolidates multiple third-party delivery apps (DoorDash, Uber Eats, GrubHub) into a single dashboard. Its products cover menu management across platforms (Connect), AI-powered marketing and local promotion on Yelp, Google, and Facebook (Reach), cross-platform performance analytics (Reporting+), and a white-label direct-delivery storefront for restricted items (Shop.Bevz). Bevz bundles an iPad plus software, access to a 215,000+ product catalog, barcode scanning, onboarding, and training. Behind the merchant product Bevz operates a real partner API: the Bevz Integrator Service, a REST API documented with a published OpenAPI 3.0.3 contract covering 30 operations across store provisioning, menu upload and sync, product catalog maintenance, order lifecycle management, order adjustments and delivery-service onboarding for DoorDash, Grubhub and Uber Eats, plus three outbound webhooks.
  It is aimed at POS vendors and third-party integrators, is credentialed by Bevz rather than self-serve, and runs a separate sandbox environment with a formal certification path to production. Bevz is a Techstars-backed company.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bevz.png
layout: provider
mcp_servers:
- description: ''
  name: Bevz MCP Server
  slug: bevz-mcp-server
modified: '2026-08-13'
name: Bevz
nav: Providers
network: true
overview: 'Bevz publishes 1 API on the [APIs.io](https://apis.io/) network: Integrator Service. Tagged areas include Company, Delivery Management, Liquor Retail, Convenience Store, and Point-of-Sale.


  The Bevz catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bevz''s developer surface includes documentation, API reference, getting-started guide, changelog, pricing, signup flow, engineering blog, and 12 more developer resources.'
plans:
- name: Bevz Plans Pricing
  plan_count: 3
  slug: bevz-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Bevz Rate Limits
  slug: bevz-rate-limits
score:
  band: strong
  composite: 57.1
  delta: 4.8
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 63.9
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 52.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bevz/refs/heads/main/screenshots/bevz-2026-07-25T202827.png
security:
- kind: authentication
  name: Bevz Authentication
  slug: bevz-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bevz Domain Security
  slug: bevz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bevz
tags:
- Company
- Delivery Management
- Liquor Retail
- Convenience Store
- Point-of-Sale
- Food Delivery
- Retail Technology
- Marketing
- Menu Management
- Order Management
- Webhook
- Integrator API
website: https://bevz.com/
---

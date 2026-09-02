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
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The Integrator Users API allows you to manage user accounts and access permissions for your integrator account.
  name: Bevz Integrator Users API
  slug: bevz-integrator-users-api
- description: The Integrators API from Bevz — 2 operation(s) for integrators.
  name: Bevz Integrators API
  slug: bevz-integrators-api
- description: '## Lotto Scratcher Games Retrieve lottery scratch-off game data from supported state lotteries. This endpoint provides game catalogs that can be used to display lotto ticket information in POS systems'
  name: Bevz Lotto Scratcher Games API
  slug: bevz-lotto-scratcher-games-api
- description: The Order API from Bevz — 3 operation(s) for order.
  name: Bevz Order API
  slug: bevz-order-api
- description: This document outlines the integration flow for onboarding new DoorDash and Grubhub stores through the [Delivery Services Onboarding API](#tag/Pick-a-Delivery-Service-for-Onboarding-API/operation/onbo
  name: Bevz Pick a Delivery Service for Onboarding API
  slug: bevz-pick-a-delivery-service-for-onboarding-api-api
- description: Store Products refer to inventory items that are available in a specific store. These products can be managed, updated, and retrieved through the Store Products API.
  name: Bevz Store Products API
  slug: bevz-store-products-api
- description: The Stores API from Bevz — 9 operation(s) for stores.
  name: Bevz Stores API
  slug: bevz-stores-api
- description: 'The Uber Eats API allows you to onboard your store to Uber Eats and manage related operations. Uber Eats onboarding is a three-step process: 1. **Generate OAuth URL:** Obtain an authorization link for'
  name: Bevz Uber Eats Onboarding API Workflow API
  slug: bevz-uber-eats-onboarding-api-workflow-api
- description: The Webhooks API from Bevz — 0 operation(s) for webhooks.
  name: Bevz Webhooks API
  slug: bevz-webhooks-api
artifact_total: 15
asyncapis:
- description: ''
  name: Bevz Webhooks
  slug: bevz-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bevz-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bevz-integrator-service-overlay.yaml
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
overview: 'Bevz publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Integrator Users API, Integrators API, Lotto Scratcher Games API, and 6 more. Tagged areas include Company, Delivery Management, Liquor Retail, Convenience Store, and Point-of-Sale.


  The Bevz catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bevz''s developer surface includes documentation, API reference, getting-started guide, changelog, pricing, signup flow, engineering blog, and 14 more developer resources.'
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
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 58.8
    developer_ergonomics: 60.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 53.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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

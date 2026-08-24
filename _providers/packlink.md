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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Packlink Agentic Access
  operation_count: 24
  slug: packlink-agentic-access
  summary_line: 24 operations · 9 acting
api_count: 6
apis:
- description: Client account, warehouses, and API keys.
  name: Packlink Clients API
  slug: packlink-clients-api
- description: Customs invoices and customs-union lookups.
  name: Packlink Customs API
  slug: packlink-customs-api
- description: Register and manage platform integrations.
  name: Packlink Integrations API
  slug: packlink-integrations-api
- description: Postal code, postal zone, and drop-off lookups.
  name: Packlink Locations API
  slug: packlink-locations-api
- description: Compare and query available shipping services.
  name: Packlink Services API
  slug: packlink-services-api
- description: Create shipments, print labels, and track parcels.
  name: Packlink Shipments API
  slug: packlink-shipments-api
artifact_total: 18
asyncapis:
- description: ''
  name: Packlink Webhooks
  slug: packlink-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Packlink PRO Shipping Clients API
  slug: open-packlink-clients-api
- collection_type: open
  name: Packlink PRO Shipping Clients Customs API
  slug: open-packlink-customs-api
- collection_type: open
  name: Packlink PRO Shipping Clients Integrations API
  slug: open-packlink-integrations-api
- collection_type: open
  name: Packlink PRO Shipping Clients Locations API
  slug: open-packlink-locations-api
- collection_type: open
  name: Packlink PRO Shipping Clients Services API
  slug: open-packlink-services-api
- collection_type: open
  name: Packlink PRO Shipping Clients Shipments API
  slug: open-packlink-shipments-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/packlink-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: http://www.packlink.com
- group: start
  title: ''
  type: Portal
  url: https://pro.packlink.com
- group: operate
  title: ''
  type: Support
  url: https://support.packlink.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://packlink.com/en-GB/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/packlink-dev
- group: start
  title: ''
  type: SignUp
  url: https://auth.packlink.com/register/?platform=PRO
- group: commercial
  title: ''
  type: TermsOfService
  url: https://packlink.com/en-GB/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://packlink.com/en-GB/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/packlink-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/packlink-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/packlink-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/packlink-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/packlink-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/packlink-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/packlink-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/packlink-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/packlink-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/packlink-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/packlink-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/packlink-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/packlink-domain-security.yml
created: '2026-07-17'
description: Packlink is a multi-carrier shipping comparison and management platform for e-commerce, founded in Spain and backed by Accel. It lets individuals and businesses compare courier services (UPS, DPD, DHL, Evri, Royal Mail and more) and send parcels nationally and internationally at negotiated rates. Its Packlink PRO product adds a business shipping dashboard with marketplace and e-commerce integrations (Shopify, WooCommerce, Magento, PrestaShop, Amazon, eBay). The Packlink PRO Shipping API (api.packlink.com) exposes service comparison, shipment creation, label printing, parcel tracking, warehouse management, customs invoicing, and integration management, and Packlink maintains open-source e-commerce integration modules on GitHub.
image: http://www.packlink.com
layout: provider
mcp_servers:
- description: ''
  name: Packlink MCP Server
  slug: packlink-mcp-server
modified: '2026-07-20'
name: Packlink
nav: Providers
network: true
overview: 'Packlink publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Customs API, Integrations API, and 3 more. Tagged areas include Company, E-Commerce, Shipping, Logistics, and Parcel Delivery.


  The Packlink catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Packlink''s developer surface includes developer portal, support, engineering blog, signup flow, authentication, and 18 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 39.4
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 61.5
    developer_ergonomics: 37.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/screenshots/packlink-2026-08-07T191246.png
security:
- kind: authentication
  name: Packlink Authentication
  slug: packlink-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Packlink Domain Security
  slug: packlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: packlink
tags:
- Company
- E-Commerce
- Shipping
- Logistics
- Parcel Delivery
- Carriers
- Fulfillment
website: http://www.packlink.com
---

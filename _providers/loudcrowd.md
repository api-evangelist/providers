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
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: Read-only, account-scoped REST API for pulling orders attributed to members of a LoudCrowd program. Each result identifies the program member and includes attribution methods, financial values and pla
  name: LoudCrowd Brand API
  slug: loudcrowd-brand-api
- description: Single-endpoint event intake for custom and headless commerce stacks. POST /event/ecomm accepts the complete order payload for ORDER_CREATE, ORDER_UPDATE and ORDER_CANCEL topics selected by the X-LC-T
  name: LoudCrowd Attribution Events API
  slug: loudcrowd-attribution-events-api
- description: Data API to be used in place of the hosted creator storefront web components, leaving the caller responsible for rendering. Five read operations return ambassador information, an ambassador's collecti
  name: LoudCrowd Creator Storefronts API
  slug: loudcrowd-creator-storefronts-api
artifact_total: 8
asyncapis:
- description: ''
  name: Loudcrowd Attribution Events
  slug: loudcrowd-attribution-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loudcrowd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loudcrowd-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://loudcrowd.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.loudcrowd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.loudcrowd.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.loudcrowd.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.loudcrowd.com/docs/implementation-overview-custom-ecommerce
- group: operate
  title: ''
  type: Support
  url: https://help.loudcrowd.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.loudcrowd.com/en/
- group: company
  title: ''
  type: Blog
  url: https://loudcrowd.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://loudcrowd.com/feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://loudcrowd.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://loudcrowd.com/demo/
- group: start
  title: ''
  type: Login
  url: https://app.loudcrowd.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loudcrowd.com/legal/platform-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loudcrowd.com/legal/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://loudcrowd.com/legal/dpa/
- group: build
  title: ''
  type: Packages
  url: packages/loudcrowd-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/loudcrowd-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loudcrowd-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/loudcrowd-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/loudcrowd-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loudcrowd-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loudcrowd-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loudcrowd-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loudcrowd-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/loudcrowd-components.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/loudcrowd-tool-crosswalk.yml
- group: other
  title: ''
  type: EventCatalog
  url: asyncapi/loudcrowd-attribution-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/loudcrowd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loudcrowd-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/loudcrowd-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/loudcrowd-creator-storefronts-overlay.yaml
- group: agent
  title: ''
  type: WellKnown-Probe
  url: well-known/loudcrowd-well-known.yml
- group: agent
  title: ''
  type: MCPServer-Candidate
  url: mcp/loudcrowd-mcp.yml
created: '2026-08-25'
description: 'LoudCrowd is a creator-commerce platform for consumer brands, combining an influencer/ambassador and affiliate marketing platform, on-domain Creator Storefronts, a ShopWith AI shopping concierge for product detail pages, AI Influencer Agents for discovery, outreach and moderation, and Creator GEO for turning earned creator content into AI-recommendable assets. For developers it publishes a small, purpose-built OpenAPI 3.0 surface across three services: a read-only account-scoped Brand API for pulling program-attributed orders, an HMAC-SHA256-signed Attribution Events API for pushing order create/update/cancel and refund events plus product-catalog batches from custom and headless commerce stacks, and a Creator Storefronts data API used in place of the hosted storefront web components. A browser SDK loaded from pub.loudcrowd.com renders storefront and influencer-list app blocks and performs first-party affiliate attribution on Shopify, Salesforce Commerce Cloud and custom sites.'
image: https://loudcrowd.com/og-default.png
layout: provider
modified: '2026-08-25'
name: LoudCrowd
nav: Providers
network: true
overview: 'LoudCrowd publishes 3 APIs on the [APIs.io](https://apis.io/) network: Brand API, Attribution Events API, and Creator Storefronts API. Tagged areas include Creator Marketing, Influencer Marketing, Affiliate Marketing, Ecommerce, and Creator Commerce.


  The LoudCrowd catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LoudCrowd''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Loudcrowd Plans Pricing
  plan_count: 5
  slug: loudcrowd-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Loudcrowd Rate Limits
  slug: loudcrowd-rate-limits
score:
  band: developing
  composite: 53.8
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 30.3
    contract_quality: 58.8
    developer_ergonomics: 47.0
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Loudcrowd Authentication
  slug: loudcrowd-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Loudcrowd Domain Security
  slug: loudcrowd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: loudcrowd
tags:
- Creator Marketing
- Influencer Marketing
- Affiliate Marketing
- Ecommerce
- Creator Commerce
- Attribution
- Social Commerce
- Shopify
- User Generated Content
- Commissions
- Retail
- Marketing
website: https://loudcrowd.com/
---

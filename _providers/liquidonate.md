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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Liquidonate Agentic Access
  operation_count: 9
  slug: liquidonate-agentic-access
  summary_line: 9 operations · 9 acting
api_count: 2
apis:
- description: Bulky, multi-package and pickup-scheduled donations.
  name: LiquiDonate Donate API
  slug: liquidonate-donate-api
- description: Match items to nonprofits.
  name: LiquiDonate Match API
  slug: liquidonate-match-api
- description: Push order data into ReturnsDirect.
  name: LiquiDonate Orders API
  slug: liquidonate-orders-api
- description: Retailer account setup and lookup.
  name: LiquiDonate Retailer API
  slug: liquidonate-retailer-api
- description: Purchase donation shipping labels.
  name: LiquiDonate Ship API
  slug: liquidonate-ship-api
- description: The ReturnsDirect By LiquiDonate (Beta) API from LiquiDonate — 0 operation(s) for returnsdirect by liquidonate (beta).
  name: LiquiDonate ReturnsDirect By LiquiDonate (Beta) API
  slug: liquidonate-returnsdirect-by-liquidonate-beta-api
artifact_total: 17
asyncapis:
- description: Outbound webhook event surface for ReturnsDirect by LiquiDonate. LiquiDonate POSTs return and refund status events to the webhook URL a retailer registers, so the retailer can update its own order man
  name: ReturnsDirect by LiquiDonate - Return and Refund Events
  slug: liquidonate-returnsdirect-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MagicMatch by LiquiDonate Donate API
  slug: open-liquidonate-donate-api
- collection_type: open
  name: MagicMatch by LiquiDonate Donate Match API
  slug: open-liquidonate-match-api
- collection_type: open
  name: MagicMatch by LiquiDonate Donate Orders API
  slug: open-liquidonate-orders-api
- collection_type: open
  name: MagicMatch by LiquiDonate Donate Retailer API
  slug: open-liquidonate-retailer-api
- collection_type: open
  name: MagicMatch by LiquiDonate Donate Ship API
  slug: open-liquidonate-ship-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/liquidonate-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/liquidonate-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/liquidonate-magicmatch-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/liquidonate-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.liquidonate.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.liquidonate.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.liquidonate.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.liquidonate.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.liquidonate.com/integrations
- group: operate
  title: ''
  type: Support
  url: https://help.liquidonate.com
- group: company
  title: ''
  type: Blog
  url: https://www.liquidonate.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.liquidonate.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.liquidonate.com/login
- group: start
  title: ''
  type: Login
  url: https://app.liquidonate.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liquidonate.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liquidonate.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.liquidonate.com/contact-us
- group: company
  title: ''
  type: About
  url: https://www.liquidonate.com/about
- group: company
  title: ''
  type: Press
  url: https://www.liquidonate.com/press
- group: other
  title: ''
  type: CaseStudies
  url: https://www.liquidonate.com/case-studies
- group: other
  title: ''
  type: Marketplace
  url: https://apps.shopify.com/liquidonate
- group: company
  title: ''
  type: Careers
  url: https://jobs.gusto.com/boards/liquidonate-inc-6984f107-b115-40e9-8c73-432c4902cff4
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liquidonate
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/liquidonate
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@LiquiDonate
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/liquidonate
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/liquidonate
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/21205794/2sA3QteBZu
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/liquidonate-category-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liquidonate-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/liquidonate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/liquidonate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liquidonate-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.liquidonate.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/liquidonate-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/liquidonate-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/liquidonate-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/liquidonate-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/liquidonate-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liquidonate-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/liquidonate-returnsdirect-asyncapi.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liquidonate-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'LiquiDonate is a San Francisco based reverse-logistics and donation-disposition platform that turns retail returns, excess inventory and unsellable goods into local nonprofit donations instead of landfill or liquidation. Its matching engine pairs items with nearby nonprofits that want them, buys the shipping label, routes the parcel and generates the donation receipt, so retailers recover tax value and meet extended-producer-responsibility and sustainability obligations. The company sells three product lines - ReturnsDirect (customer-direct returns), WarehouseDirect (warehouse and 3PL excess inventory) and BoxDrop (donation boxes) - and exposes two public developer APIs: MagicMatch, a donation-as-a-service API that accepts parcel and item details and returns a nonprofit match plus a donation shipping label, and ReturnsDirect, a beta returns-management integration for non-Shopify ecommerce platforms built on pushed order data plus HMAC-signed return and refund webhooks. LiquiDonate
  integrates with Shopify, Loop, EasyPost, FedEx, Bungii, SendGrid and Rise AI, and has been recognized on TIME Best Inventions 2025 and Fast Company World Changing Ideas.'
image: https://cdn.prod.website-files.com/672dc2792e95c584b8beaaca/6739416b527eda8f246a7686_Liquidonate%20%20Webclip.png
layout: provider
mcp_servers:
- description: ''
  name: LiquiDonate MCP Server
  slug: liquidonate-mcp-server
modified: '2026-07-19'
name: LiquiDonate
nav: Providers
network: true
overview: 'LiquiDonate publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Donate API, Match API, Orders API, and 3 more. Tagged areas include Reverse Logistics, Returns Management, Donations, Non-Profit, and Retail.


  The LiquiDonate catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  LiquiDonate''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 22
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 19.7
    contract_quality: 64.7
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 19.7
    operational_transparency: 23.7
  previous_composite: 52.5
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liquidonate/refs/heads/main/screenshots/liquidonate-2026-07-25T225320.png
security:
- kind: authentication
  name: Liquidonate Authentication
  slug: liquidonate-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Liquidonate Domain Security
  slug: liquidonate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: liquidonate
tags:
- Reverse Logistics
- Returns Management
- Donations
- Non-Profit
- Retail
- E-Commerce
- Sustainability
- Circular Economy
- Shipping
- Supply Chain
- Excess Inventory
- Company
website: https://www.liquidonate.com
---

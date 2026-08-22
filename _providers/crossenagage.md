---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.5
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: Asynchronous customer profile API — create, update and delete single users, batch up to 1,000 users per call, look a user up by id or by email plus business unit, and poll a tracking id for terminal s
  name: CrossEngage User Management API v2
  slug: user-management-v2
- description: 'Synchronous predecessor to v2, still fully documented and still monitored as its own status-page component. Broader in surface than v2: user attribute definitions (create/list/fetch/delete), lead capt'
  name: CrossEngage User Management API v1
  slug: user-management-v1
- description: Real-time product catalogue API backing message personalization — page through products, fetch, upsert and delete by SKU. The only CrossEngage API published as a native Swagger 2.0 document rather tha
  name: CrossEngage Product Feed API
  slug: product-feed
- description: Asynchronous bulk data-out API for user and event data. List and inspect the (S)FTP export destinations and CALLBACK webhook destinations configured on the account, list event classes, request an expo
  name: CrossEngage Raw Export API
  slug: raw-export
- description: Synchronous reporting API for story, campaign and message performance. Discover the KPI catalogue configured on the account, then request detailed per-entity or overall roll-up statistics for up to 30
  name: CrossEngage Statistics API
  slug: statistics
- description: 'Single-operation API for uploading files to be attached to messages sent through stories or campaigns. A paid add-on enabled per account through a customer success representative. Published as an API '
  name: CrossEngage File Attachments API
  slug: file-attachments
artifact_total: 20
asyncapis:
- description: ''
  name: Crossenagage Webhooks
  slug: crossenagage-webhooks
collections:
- collection_type: open
  name: File Attachment API
  slug: open-crossenagage-file-attachments-v1
- collection_type: open
  name: Product Feed API
  slug: open-crossenagage-product-feed
- collection_type: open
  name: Raw Export API
  slug: open-crossenagage-raw-export-v1
- collection_type: open
  name: Statistics API
  slug: open-crossenagage-statistics-v1
- collection_type: open
  name: User Management API v1
  slug: open-crossenagage-user-management-v1
- collection_type: open
  name: User Management API v2
  slug: open-crossenagage-user-management-v2
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/crossenagage-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crossenagage-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.documentation.crossengage.io/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.crossengage.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.documentation.crossengage.io/
- group: start
  title: ''
  type: Login
  url: https://app.crossengage.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://spotler.com/en-de/pricing
- group: company
  title: ''
  type: Blog
  url: https://spotler.com/en-de/resources
- group: operate
  title: ''
  type: Support
  url: https://documentation.crossengage.io/data-and-engagement-platform/help-and-support/reach-out-to-customer-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://spotler.com/en-de/help-centers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trust.spotler.com/privacy-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crossengage.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.spotler.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.spotler.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crossenagage-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.spotler.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/crossenagage-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crossenagage-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crossenagage-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crossenagage-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/crossenagage-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/crossenagage-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crossenagage-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crossenagage-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/crossenagage-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crossenagage-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/crossenagage-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/crossenagage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crossenagage-rate-limits.yml
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/7f6c14ba49835c19dbd7
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CrossEngage
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.crossengage.io/documentation-guide
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trust.spotler.com/general-terms-and-conditions-de
created: '2026-07-17'
description: CrossEngage is a Berlin-based customer data and cross-channel marketing platform (a Customer Data Platform / CDP) founded in 2015 and backed by Earlybird Venture Capital. It unifies first-party customer data into 360-degree profiles, builds no-code predictive AI/ML models for customer lifetime value and behavior, manages audiences with drag-and-drop segmentation, and orchestrates real-time cross-channel customer journeys across email, push, SMS, WhatsApp and webhooks. Following its acquisition by Spotler, the product is sold as Spotler Activate Pro. CrossEngage exposes six REST APIs on api.crossengage.io — User Management v1 and v2, Product Feed, Raw Export, Statistics and File Attachments — totalling 37 operations. Five are published as API Blueprint documents and one (Product Feed) as Swagger 2.0, all served from Apiary and embedded in the reference site at api.documentation.crossengage.io. Authentication is a static X-XNG-AuthToken header paired with a required X-XNG-ApiVersion
  header; there is no OAuth surface. Product documentation is published at documentation.crossengage.io, which serves a first-party llms.txt index of all 219 pages.
image: https://api.documentation.crossengage.io/wp-content/uploads/cropped-favicon-96x96-1-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: crossenagage-mcp.yml
  slug: crossenagage-mcpyml
modified: '2026-08-13'
name: CrossEngage
nav: Providers
network: true
overview: 'CrossEngage publishes 6 APIs on the [APIs.io](https://apis.io/) network, including User Management API v2, User Management API v1, Product Feed API, and 3 more. Tagged areas include Company, Customer Data Platform, Marketing, Customer Engagement, and Marketing Automation.


  The CrossEngage catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CrossEngage''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, getting-started guide, and 27 more developer resources.'
plans:
- name: Crossenagage Plans Pricing
  plan_count: 0
  slug: crossenagage-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Crossenagage Rate Limits
  slug: crossenagage-rate-limits
score:
  band: strong
  composite: 56.4
  delta: -2.1
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 30.3
    contract_quality: 59.6
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 36.8
  previous_composite: 58.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crossenagage/refs/heads/main/screenshots/crossenagage-2026-07-25T210755.png
security:
- kind: authentication
  name: Crossenagage Authentication
  slug: crossenagage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Crossenagage Domain Security
  slug: crossenagage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crossenagage Vulnerability Disclosure
  slug: crossenagage-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Crossenagage Trust Center
  slug: crossenagage-trust-center
  summary_line: ISO/IEC 27001:2022, CSA STAR Certification, GDPR
slug: crossenagage
tags:
- Company
- Customer Data Platform
- Marketing
- Customer Engagement
- Marketing Automation
- Cross-Channel
- Personalization
- Predictive Analytics
- Segmentation
- Campaign Management
- Product Feed
- Data Export
- Webhooks
- Web Tracking
- Germany
website: https://api.documentation.crossengage.io/
---

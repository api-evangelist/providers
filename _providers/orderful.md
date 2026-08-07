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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 12
  name: Orderful Agentic Access
  operation_count: 21
  slug: orderful-agentic-access
  summary_line: 21 operations · 12 acting · 12 human-in-the-loop
api_count: 9
apis:
- description: Convert data between EDI X12 and JSON formats.
  name: Orderful Conversion API
  slug: orderful-conversion-api
- description: Approve or fail transaction deliveries.
  name: Orderful Delivery API
  slug: orderful-delivery-api
- description: Retrieve transactions from inboxes.
  name: Orderful Inbox API
  slug: orderful-inbox-api
- description: Generate UCC-128 shipping labels.
  name: Orderful Label API
  slug: orderful-label-api
- description: Retrieve organization information.
  name: Orderful Organization API
  slug: orderful-organization-api
- description: Retrieve and confirm transactions from polling buckets.
  name: Orderful Poller API
  slug: orderful-poller-api
- description: Manage trading partner relationships.
  name: Orderful Relationship API
  slug: orderful-relationship-api
- description: Create and manage EDI transactions.
  name: Orderful Transaction API
  slug: orderful-transaction-api
- description: Create and manage EDI transactions using the v3 API.
  name: Orderful Transaction (v3) API
  slug: orderful-transaction-v3-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Receive a Purchase Order from an inbox, approve delivery, acknowledge it, and send back the acknowledgment.
  name: Orderful Order-to-Cash
  slug: orderful-order-to-cash
artifact_total: 18
asyncapis:
- description: ''
  name: Orderful Webhooks
  slug: orderful-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.orderful.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orderful.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.orderful.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.orderful.com/reference/welcome-to-mosaic
- group: operate
  title: ''
  type: Support
  url: https://support.orderful.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.orderful.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.orderful.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.orderful.com/book-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orderful.com/terms/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orderful.com/terms/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orderful
- group: operate
  title: ''
  type: StatusPage
  url: https://status.orderful.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/orderful-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orderful-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/orderful-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orderful-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/orderful-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orderful-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orderful-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/orderful-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/orderful-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orderful-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/orderful-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/orderful-order-to-cash.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orderful-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orderful-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/orderful-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/orderful-security.txt
- group: auth
  title: ''
  type: Security
  url: security/orderful-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orderful-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/orderful-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orderful-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.orderful.com/
created: '2026-07-17'
description: Orderful is a modern B2B trading and EDI platform that lets companies connect once to transact with any partner in their supply chain without building custom integrations. Its Mosaic API turns X12 and EDIFACT electronic data interchange into simple JSON, handling mapping, validation, testing, and compliance so suppliers, retailers, 3PLs, and carriers can exchange purchase orders (850), acknowledgments (855), ship notices (856), invoices (810), inventory advices (846), warehouse (940-series) and other transaction sets over a REST API, HTTP webhooks, AS2, SFTP, and VAN. The platform advertises 10,000+ trading partners, 50M+ transactions, and 99.99% network uptime, with US and EU regional data residency, Web EDI (Pixel), and GS1 UCC-128 shipping labels.
image: https://www.orderful.com/cms/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: orderful-mcp.yml
  slug: orderful-mcpyml
modified: '2026-07-20'
name: Orderful
nav: Providers
network: true
overview: 'Orderful publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Conversion API, Delivery API, Inbox API, and 6 more. Tagged areas include Company, EDI, Electronic Data Interchange, Supply Chain, and B2B.


  The Orderful catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Orderful''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
random_paper: 76
score:
  band: strong
  composite: 58.4
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 65.9
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 63.2
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Orderful Authentication
  slug: orderful-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Orderful Domain Security
  slug: orderful-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Orderful Vulnerability Disclosure
  slug: orderful-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Orderful Trust Center
  slug: orderful-trust-center
  summary_line: trust center published
slug: orderful
tags:
- Company
- EDI
- Electronic Data Interchange
- Supply Chain
- B2B
- Logistics
- Retail
- Transactions
- Integration
website: https://www.orderful.com/
---

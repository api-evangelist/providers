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
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Fairmarkit Agentic Access
  operation_count: 5
  slug: fairmarkit-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 18
apis:
- description: The Business Units API from Fairmarkit — 2 operation(s) for business units.
  name: Fairmarkit Business Units API
  slug: fairmarkit-business-units-api
- description: The Categories API from Fairmarkit — 1 operation(s) for categories.
  name: Fairmarkit Categories API
  slug: fairmarkit-categories-api
- description: The Data Exports API from Fairmarkit — 3 operation(s) for data exports.
  name: Fairmarkit Data Exports API
  slug: fairmarkit-data-exports-api
- description: The Data Fields API from Fairmarkit — 6 operation(s) for data fields.
  name: Fairmarkit Data Fields API
  slug: fairmarkit-data-fields-api
- description: The ERP Systems API from Fairmarkit — 1 operation(s) for erp systems.
  name: Fairmarkit ERP Systems API
  slug: fairmarkit-erp-systems-api
- description: The Event API from Fairmarkit — 3 operation(s) for event.
  name: Fairmarkit Event API
  slug: fairmarkit-event-api
- description: The File attachments API from Fairmarkit — 4 operation(s) for file attachments.
  name: Fairmarkit File attachments API
  slug: fairmarkit-file-attachments-api
- description: The Identity API from Fairmarkit — 2 operation(s) for identity.
  name: Fairmarkit Identity API
  slug: fairmarkit-identity-api
- description: The Price Books API from Fairmarkit — 8 operation(s) for price books.
  name: Fairmarkit Price Books API
  slug: fairmarkit-price-books-api
- description: The Purchase Orders API from Fairmarkit — 3 operation(s) for purchase orders.
  name: Fairmarkit Purchase Orders API
  slug: fairmarkit-purchase-orders-api
- description: The Requests API from Fairmarkit — 23 operation(s) for requests.
  name: Fairmarkit Requests API
  slug: fairmarkit-requests-api
- description: The Responses API from Fairmarkit — 4 operation(s) for responses.
  name: Fairmarkit Responses API
  slug: fairmarkit-responses-api
- description: The RFP API from Fairmarkit — 5 operation(s) for rfp.
  name: Fairmarkit RFP API
  slug: fairmarkit-rfp-api
- description: The RFQ API from Fairmarkit — 11 operation(s) for rfq.
  name: Fairmarkit RFQ API
  slug: fairmarkit-rfq-api
- description: The Schema API from Fairmarkit — 2 operation(s) for schema.
  name: Fairmarkit Schema API
  slug: fairmarkit-schema-api
- description: The Supplier API from Fairmarkit — 6 operation(s) for supplier.
  name: Fairmarkit Supplier API
  slug: fairmarkit-supplier-api
- description: The UOM API from Fairmarkit — 1 operation(s) for uom.
  name: Fairmarkit UOM API
  slug: fairmarkit-uom-api
- description: The User Profiles API from Fairmarkit — 1 operation(s) for user profiles.
  name: Fairmarkit User Profiles API
  slug: fairmarkit-user-profiles-api
artifact_total: 42
asyncapis:
- description: ''
  name: Fairmarkit Webhooks
  slug: fairmarkit-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BUYER PUBLIC Business Units API
  slug: open-fairmarkit-business-units-api
- collection_type: open
  name: BUYER PUBLIC Business Units Categories API
  slug: open-fairmarkit-categories-api
- collection_type: open
  name: BUYER PUBLIC Business Units Data Exports API
  slug: open-fairmarkit-data-exports-api
- collection_type: open
  name: BUYER PUBLIC Business Units Data Fields API
  slug: open-fairmarkit-data-fields-api
- collection_type: open
  name: BUYER PUBLIC Business Units ERP Systems API
  slug: open-fairmarkit-erp-systems-api
- collection_type: open
  name: BUYER PUBLIC Business Units Event API
  slug: open-fairmarkit-event-api
- collection_type: open
  name: BUYER PUBLIC Business Units File attachments API
  slug: open-fairmarkit-file-attachments-api
- collection_type: open
  name: BUYER PUBLIC Business Units Identity API
  slug: open-fairmarkit-identity-api
- collection_type: open
  name: BUYER PUBLIC Business Units Price Books API
  slug: open-fairmarkit-price-books-api
- collection_type: open
  name: BUYER PUBLIC Business Units Purchase Orders API
  slug: open-fairmarkit-purchase-orders-api
- collection_type: open
  name: BUYER PUBLIC Business Units Requests API
  slug: open-fairmarkit-requests-api
- collection_type: open
  name: BUYER PUBLIC Business Units Responses API
  slug: open-fairmarkit-responses-api
- collection_type: open
  name: BUYER PUBLIC Business Units RFP API
  slug: open-fairmarkit-rfp-api
- collection_type: open
  name: BUYER PUBLIC Business Units RFQ API
  slug: open-fairmarkit-rfq-api
- collection_type: open
  name: BUYER PUBLIC Business Units Schema API
  slug: open-fairmarkit-schema-api
- collection_type: open
  name: BUYER PUBLIC Business Units Supplier API
  slug: open-fairmarkit-supplier-api
- collection_type: open
  name: BUYER PUBLIC Business Units UOM API
  slug: open-fairmarkit-uom-api
- collection_type: open
  name: BUYER PUBLIC Business Units User Profiles API
  slug: open-fairmarkit-user-profiles-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/fairmarkit-buyer-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fairmarkit-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fairmarkit-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.fairmarkit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.fairmarkit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fairmarkit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.fairmarkit.com/reference/getting-started-with-fairmarkit-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.fairmarkit.com/reference/getting-started-with-fairmarkit-api
- group: auth
  title: ''
  type: Authentication
  url: authentication/fairmarkit-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://fmkt.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.fairmarkit.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fairmarkit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fairmarkit.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fairmarkit.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.fairmarkit.com/security-statement
- group: auth
  title: ''
  type: Compliance
  url: https://www.fairmarkit.com/security-compliance
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fairmarkit-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.fairmarkit.com/release-notes
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fairmarkit-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fairmarkit-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fairmarkit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fairmarkit-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fairmarkit-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/fairmarkit-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fairmarkit-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fairmarkit-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fairmarkit-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Fairmarkit is an autonomous sourcing and strategic procurement platform that uses AI agents to automate the full sourcing lifecycle — from intake and request creation through RFQ/RFP/RFI events, supplier bidding, award, and purchase-order handoff to ERP and P2P systems. Fairmarkit publishes a public, OpenAPI 3.1-described Buyer Self-Service REST API (v3 and v4) and a Supplier Public API, secured with an X-FM-API-KEY header, covering RFQ/RFP events, requests and request items, suppliers, purchase orders, price books, datasets/data fields, business units, categories, identities, permission sets, data exports, and file attachments, plus a rich webhook notification catalog for procurement events. The company is backed by GGV Capital and Insight Partners.
image: https://cdn.prod.website-files.com/6974c3dfc9de89aed672a42c/69df9b1468ca1d50addc7ada_aac4c2022c593d27762cac87054f89ec_Opengraph_Homepage.png
layout: provider
mcp_servers:
- description: ''
  name: fairmarkit-mcp.yml
  slug: fairmarkit-mcpyml
modified: '2026-07-19'
name: Fairmarkit
nav: Providers
network: true
overview: 'Fairmarkit publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Business Units API, Categories API, Data Exports API, and 15 more. Tagged areas include Company, Procurement, Sourcing, Supply Chain, and Purchasing.


  The Fairmarkit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fairmarkit''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, changelog, and 21 more developer resources.'
random_paper: 23
score:
  band: developing
  composite: 49.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 65.9
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fairmarkit/refs/heads/main/screenshots/fairmarkit-2026-07-25T214156.png
security:
- kind: authentication
  name: Fairmarkit Authentication
  slug: fairmarkit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fairmarkit Domain Security
  slug: fairmarkit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fairmarkit
tags:
- Company
- Procurement
- Sourcing
- Supply Chain
- Purchasing
- Suppliers
- RFQ
- RFP
- Spend Management
- Webhooks
website: https://www.fairmarkit.com/
---

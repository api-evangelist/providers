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
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Wetravel Agentic Access
  operation_count: 77
  slug: wetravel-agentic-access
  summary_line: 77 operations · 46 acting
api_count: 1
apis:
- description: The Access token API from WeTravel — 1 operation(s) for access token.
  name: WeTravel Access token API
  slug: wetravel-access-token-api
- description: The Add-ons API from WeTravel — 2 operation(s) for add-ons.
  name: WeTravel Add-ons API
  slug: wetravel-add-ons-api
- description: The Discounts API from WeTravel — 2 operation(s) for discounts.
  name: WeTravel Discounts API
  slug: wetravel-discounts-api
- description: The Images API from WeTravel — 2 operation(s) for images.
  name: WeTravel Images API
  slug: wetravel-images-api
- description: The Included items API from WeTravel — 2 operation(s) for included items.
  name: WeTravel Included items API
  slug: wetravel-included-items-api
- description: The Leads API from WeTravel — 2 operation(s) for leads.
  name: WeTravel Leads API
  slug: wetravel-leads-api
- description: The Not Included items API from WeTravel — 2 operation(s) for not included items.
  name: WeTravel Not Included items API
  slug: wetravel-not-included-items-api
- description: The Orders API from WeTravel — 7 operation(s) for orders.
  name: WeTravel Orders API
  slug: wetravel-orders-api
- description: The Packages API from WeTravel — 2 operation(s) for packages.
  name: WeTravel Packages API
  slug: wetravel-packages-api
- description: The Paragraphs API from WeTravel — 2 operation(s) for paragraphs.
  name: WeTravel Paragraphs API
  slug: wetravel-paragraphs-api
- description: The Participant Information API from WeTravel — 2 operation(s) for participant information.
  name: WeTravel Participant Information API
  slug: wetravel-participant-information-api
- description: The Payment Links API from WeTravel — 3 operation(s) for payment links.
  name: WeTravel Payment Links API
  slug: wetravel-payment-links-api
- description: The Payment Plans API from WeTravel — 2 operation(s) for payment plans.
  name: WeTravel Payment Plans API
  slug: wetravel-payment-plans-api
- description: The Suppliers API from WeTravel — 2 operation(s) for suppliers.
  name: WeTravel Suppliers API
  slug: wetravel-suppliers-api
- description: The Transactions API from WeTravel — 2 operation(s) for transactions.
  name: WeTravel Transactions API
  slug: wetravel-transactions-api
- description: The Trip Overview API from WeTravel — 2 operation(s) for trip overview.
  name: WeTravel Trip Overview API
  slug: wetravel-trip-overview-api
- description: The Trips API from WeTravel — 3 operation(s) for trips.
  name: WeTravel Trips API
  slug: wetravel-trips-api
artifact_total: 42
asyncapis:
- description: ''
  name: Wetravel Webhooks
  slug: wetravel-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WeTravel Partner Access token API
  slug: open-wetravel-access-token-api
- collection_type: open
  name: WeTravel Partner Access token Add-ons API
  slug: open-wetravel-add-ons-api
- collection_type: open
  name: WeTravel Partner Access token Discounts API
  slug: open-wetravel-discounts-api
- collection_type: open
  name: WeTravel Partner Access token Images API
  slug: open-wetravel-images-api
- collection_type: open
  name: WeTravel Partner Access token Included items API
  slug: open-wetravel-included-items-api
- collection_type: open
  name: WeTravel Partner Access token Leads API
  slug: open-wetravel-leads-api
- collection_type: open
  name: WeTravel Partner Access token Not Included items API
  slug: open-wetravel-not-included-items-api
- collection_type: open
  name: WeTravel Partner Access token Orders API
  slug: open-wetravel-orders-api
- collection_type: open
  name: WeTravel Partner Access token Packages API
  slug: open-wetravel-packages-api
- collection_type: open
  name: WeTravel Partner Access token Paragraphs API
  slug: open-wetravel-paragraphs-api
- collection_type: open
  name: WeTravel Partner Access token Participant Information API
  slug: open-wetravel-participant-information-api
- collection_type: open
  name: WeTravel Partner Access token Payment Links API
  slug: open-wetravel-payment-links-api
- collection_type: open
  name: WeTravel Partner Access token Payment Plans API
  slug: open-wetravel-payment-plans-api
- collection_type: open
  name: WeTravel Partner Access token Suppliers API
  slug: open-wetravel-suppliers-api
- collection_type: open
  name: WeTravel Partner Access token Transactions API
  slug: open-wetravel-transactions-api
- collection_type: open
  name: WeTravel Partner Access token Trip Overview API
  slug: open-wetravel-trip-overview-api
- collection_type: open
  name: WeTravel Partner Access token Trips API
  slug: open-wetravel-trips-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/wetravel-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/wetravel-partner-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wetravel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wetravel.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.wetravel.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.wetravel.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.wetravel.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wetravel.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wetravel-com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wetravel-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.wetravel.com/reference/migration-v2-to-v3
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wetravel-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wetravel-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wetravel-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wetravel-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wetravel-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wetravel-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wetravel-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wetravel-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wetravel-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wetravel-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wetravel-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wetravel-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://www.wetravel.com/disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wetravel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wetravel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wetravel.com/
created: '2026-07-17'
description: WeTravel is a booking and payments platform for the multi-day and group travel industry - tour operators, retreat and adventure-travel organizers, and travel agencies. Its Partner API (Trip Builder, Bookings, Payments/Payment Links, Transactions, Suppliers and Leads) lets travel companies programmatically create WeTravel trip and booking pages from their own IT systems and sync customer, order, payment and transaction data, while WeTravel handles the customer-facing booking experience, automated payment plans and low-cost payment processing. A Zapier integration extends the same data to 8000+ services, and a documented webhook catalog streams booking, payment, transaction, trip and lead events. Backed by Index Ventures and Sapphire Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wetravel.png
layout: provider
mcp_servers:
- description: ''
  name: WeTravel MCP Server
  slug: wetravel-mcp-server
modified: '2026-07-21'
name: WeTravel
nav: Providers
network: true
overview: 'WeTravel publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Access token API, Add-ons API, Discounts API, and 14 more. Tagged areas include Company, Business Applications, Travel, Booking, and Payments.


  The WeTravel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WeTravel''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, sandbox, and 21 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 1
  name: Wetravel Rate Limits
  slug: wetravel-rate-limits
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 62.4
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 77.6
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 17
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wetravel/refs/heads/main/screenshots/wetravel-2026-08-17T082914.png
security:
- kind: authentication
  name: Wetravel Authentication
  slug: wetravel-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wetravel Domain Security
  slug: wetravel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Wetravel Vulnerability Disclosure
  slug: wetravel-vulnerability-disclosure
  summary_line: disclosure policy published
slug: wetravel
tags:
- Company
- Business Applications
- Travel
- Booking
- Payments
- Trip Management
- Tour Operators
- Travel Technology
website: https://www.wetravel.com/
---

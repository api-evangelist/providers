---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developer.onerail.io/hc/en-us/articles/50724541394971-Getting-Started-with-Delivery-API
  - https://developer.onerail.io/hc/en-us/articles/53169025821339-CapacityConnect-API-Quickstart-Guide
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 284
  human_in_the_loop: 22
  name: Onerail Agentic Access
  operation_count: 469
  slug: onerail-agentic-access
  summary_line: 469 operations · 284 acting · 22 human-in-the-loop
api_count: 2
apis:
- description: The OmniPoint Delivery API lets authorized shippers request, price, update, and track deliveries through the OneRail carrier network. It covers rate shopping across qualified carriers, order and deliv
  name: OneRail Delivery API
  slug: onerail-delivery-api
- description: 'The OmniPoint Operations (Operation Dashboard) API administers the shipper account behind the Delivery API: organizations and their preferences, pickup and drop-off locations with service hours and cu'
  name: OneRail Operations API
  slug: onerail-operations-api
artifact_total: 9
asyncapis:
- description: ''
  name: Onerail Delivery Events Webhooks
  slug: onerail-delivery-events-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onerail-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.onerail.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.onerail.io/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://developer.onerail.io/hc/en-us/categories/50712147847067-Developer-Hub
- group: docs
  title: ''
  type: APIReference
  url: https://developer.onerail.io/hc/en-us/articles/50724541394971-Getting-Started-with-Delivery-API
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.onerail.io/hc/en-us/articles/50724541394971-Getting-Started-with-Delivery-API
- group: operate
  title: ''
  type: Support
  url: https://knowledge.onerail.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.onerail.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.onerail.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onerail.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onerail.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.onerail.com/ai/data-privacy-security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/onerail-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://onerail.cronitorstatus.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/onerail-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/onerail-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onerail-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/onerail-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/onerail-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/onerail-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/onerail-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onerail-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onerail-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/onerail-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/onerail-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/onerail-delivery-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onerail-llms.txt
created: '2026-08-02'
description: OneRail is an Orlando, Florida based last-mile delivery orchestration company whose OmniPoint platform unifies fragmented delivery ecosystems into a single decisioning and execution layer for enterprise shippers. The platform rate-shops and dispatches orders across a courier marketplace of 1,000+ connected carriers and 12M+ drivers, optimizes multi-stop routes for internal fleets under vehicle-capacity, market-hours and appointment-window constraints, and streams delivery events back to the shipper for end-to-end visibility and proof of delivery. Developers integrate through two documented REST surfaces published from the OneRail Developer Hub - the Delivery API (order creation, rate shopping, partial updates, cancellation, shipping labels, routes, and visibility-only tracking for shipments fulfilled outside the OneRail network) and the Operations API (organizations, locations, users, markets, fleet assets, contracts, SLAs, and API credentials). Both are authenticated with an
  organization App ID / API Key header pair, and delivery status changes are pushed to shipper-configured webhook endpoints. OneRail is embedded in the IBM Sterling Order Management and Fulfillment Suite and in SAP environments, and serves wholesale, retail, automotive, pharma, industrial, grocery, furniture, and food and beverage shippers.
image: https://www.onerail.com/wp-content/themes/customtheme/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: onerail-mcp.yml
  slug: onerail-mcpyml
modified: '2026-08-02'
name: OneRail
nav: Providers
network: true
overview: 'OneRail publishes 2 APIs on the [APIs.io](https://apis.io/) network: Delivery API and Operations API. Tagged areas include last-mile-delivery, delivery-orchestration, logistics, supply-chain, and route-optimization.


  The OneRail catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OneRail''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 21 more developer resources.'
random_paper: 81
scopes:
- name: Onerail Scopes
  scope_count: 0
  slug: onerail-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.8
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Onerail Authentication
  slug: onerail-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Onerail Domain Security
  slug: onerail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Onerail Trust Center
  slug: onerail-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, GDPR
slug: onerail
tags:
- last-mile-delivery
- delivery-orchestration
- logistics
- supply-chain
- route-optimization
- courier-network
- shipping
- fleet-management
- transportation
- order-management
- webhooks
- final-mile
website: https://www.onerail.com/
---

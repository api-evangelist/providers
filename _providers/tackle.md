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
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Tackle Agentic Access
  operation_count: 78
  slug: tackle-agentic-access
  summary_line: 78 operations · 35 acting
api_count: 25
apis:
- description: Operations for API Authentication
  name: Tackle Authentication API
  slug: tackle-authentication-api
- description: The Contracts API from Tackle — 2 operation(s) for contracts.
  name: Tackle Contracts API
  slug: tackle-contracts-api
- description: Microsoft marketplace currency and conversion helpers.
  name: Tackle Currencies API
  slug: tackle-currencies-api
- description: The Disbursements API from Tackle — 1 operation(s) for disbursements.
  name: Tackle Disbursements API
  slug: tackle-disbursements-api
- description: Legacy entitlements endpoint - returns flat role objects
  name: Tackle Entitlements API
  slug: tackle-entitlements-api
- description: SCIM 2.0 Groups endpoint - returns full Group resources (RFC 7643 §4.2)
  name: Tackle Groups API
  slug: tackle-groups-api
- description: Create (test-environment-only), read, update, and list co-sell invitations — AWS-led requests to partner with you on a specific opportunity. Use the update operation to accept or reject an invitation,
  name: Tackle Invitations API
  slug: tackle-invitations-api
- description: The Invoices API from Tackle — 1 operation(s) for invoices.
  name: Tackle Invoices API
  slug: tackle-invoices-api
- description: AWS Marketplace context endpoints used to assemble offers and amendments.
  name: Tackle Marketplace API
  slug: tackle-marketplace-api
- description: The Metering API from Tackle — 2 operation(s) for metering.
  name: Tackle Metering API
  slug: tackle-metering-api
- description: Buyer instruction notification operations.
  name: Tackle Notifications API
  slug: tackle-notifications-api
- description: 'Create, read, update, and list co-sell opportunities — the partner- originated (Outbound / Partner Referral) and AWS-originated (Inbound / AWS Referral) deals tracked in AWS Partner Central. Includes '
  name: Tackle Opportunities API
  slug: tackle-opportunities-api
- description: AWS Marketplace partner (reseller) reference data.
  name: Tackle Partners API
  slug: tackle-partners-api
- description: Private offer lifecycle actions such as archive, cancel, and sync.
  name: Tackle Private Offer Actions API
  slug: tackle-private-offer-actions-api
- description: AWS private-offer lifecycle (create, read, update, cancel, push to marketplace).
  name: Tackle Private Offers API
  slug: tackle-private-offers-api
- description: Operations for Products
  name: Tackle Products API
  slug: tackle-products-api
- description: The public API from Tackle — 7 operation(s) for public.
  name: Tackle public API
  slug: tackle-public-api
- description: Operations for Order Registrations
  name: Tackle Registrations API
  slug: tackle-registrations-api
- description: Score domains and search scored accounts.
  name: Tackle Scores API
  slug: tackle-scores-api
- description: Service provider configuration and capabilities
  name: Tackle Service Provider API
  slug: tackle-service-provider-api
- description: List the co-sell solutions registered with AWS Partner Central for your account. Solution identifiers are referenced by `solutions` on opportunities.
  name: Tackle Solutions API
  slug: tackle-solutions-api
- description: Operations for Subscriptions
  name: Tackle Subscriptions API
  slug: tackle-subscriptions-api
- description: User management operations
  name: Tackle Users API
  slug: tackle-users-api
- description: Operations for API Versions
  name: Tackle Version API
  slug: tackle-version-api
- description: Operations for Webhooks
  name: Tackle Webhooks API
  slug: tackle-webhooks-api
artifact_total: 32
asyncapis:
- description: ''
  name: Tackle Webhooks
  slug: tackle-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.tackle.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tackle.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.tackle.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.tackle.io/docs/getting-an-access-token
- group: operate
  title: ''
  type: Support
  url: https://help.tackle.io/en
- group: company
  title: ''
  type: Blog
  url: https://tackle.io/resources/blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://tackle.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://downstream.tackle.io/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tackle.io/privacy-policy-tackle-platform/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tackle.io
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tackle.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/tackle-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tackle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tackle-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tackle-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tackle-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tackle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tackle-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tackle-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tackle-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tackle-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tackle-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tackle-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tackle-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tackle-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tackle-llms.txt
created: '2026-07-17'
description: 'Tackle is a Cloud Go-To-Market (Cloud GTM) platform that helps software companies sell through the AWS, Microsoft Azure, and Google Cloud marketplaces. Its developer APIs (developers.tackle.io) automate the full marketplace workflow: creating and managing private offers on AWS and Microsoft, AWS Partner Central co-sell opportunities and invitations, public contracts, metered usage reporting, disbursements and invoices, buyer prospecting (propensity-to-buy domain scoring), and SCIM 2.0 user provisioning. Authentication is machine-to-machine JWT (client_id/client_secret exchanged for a Bearer token), and vendors receive marketplace lifecycle events via registered, authenticated webhooks. Tackle is backed by a16z and publishes a SafeBase trust center (SOC 2 Type II, GDPR).'
image: https://tackle.io/wp-content/uploads/2024/02/cropped-cropped-favicon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: tackle-mcp.yml
  slug: tackle-mcpyml
modified: '2026-07-21'
name: Tackle
nav: Providers
network: true
overview: 'Tackle publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contracts API, Currencies API, and 22 more. Tagged areas include Company, Cloud Marketplace, Cloud GTM, Go-To-Market, and Private Offers.


  The Tackle catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tackle''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 58
scopes:
- name: Tackle Scopes
  scope_count: 0
  slug: tackle-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 55.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.5
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Tackle Authentication
  slug: tackle-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Tackle Domain Security
  slug: tackle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tackle Trust Center
  slug: tackle-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: tackle
tags:
- Company
- Cloud Marketplace
- Cloud GTM
- Go-To-Market
- Private Offers
- Co-Sell
- Metering
- SCIM
- AWS Marketplace
- Azure Marketplace
website: https://developers.tackle.io
---

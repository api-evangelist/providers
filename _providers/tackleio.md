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
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.5
  scored_at: '2026-07-28'
api_count: 28
apis:
- description: Operations for API Authentication
  name: Tackle.io Authentication API
  slug: tackleio-authentication-api
- description: The Contracts API from Tackle.io — 2 operation(s) for contracts.
  name: Tackle.io Contracts API
  slug: tackleio-contracts-api
- description: Microsoft marketplace currency and conversion helpers.
  name: Tackle.io Currencies API
  slug: tackleio-currencies-api
- description: 'Look up customer accounts in Microsoft Partner Center before creating a referral. Use these endpoints to determine `customerProfile.ids` and the `dealSensitivity` value (`USFed` vs `None`) you should '
  name: Tackle.io Customers API
  slug: tackleio-customers-api
- description: The Disbursements API from Tackle.io — 1 operation(s) for disbursements.
  name: Tackle.io Disbursements API
  slug: tackleio-disbursements-api
- description: Legacy entitlements endpoint - returns flat role objects
  name: Tackle.io Entitlements API
  slug: tackleio-entitlements-api
- description: SCIM 2.0 Groups endpoint - returns full Group resources (RFC 7643 §4.2)
  name: Tackle.io Groups API
  slug: tackleio-groups-api
- description: Create (test-environment-only), read, update, and list co-sell invitations — AWS-led requests to partner with you on a specific opportunity. Use the update operation to accept or reject an invitation,
  name: Tackle.io Invitations API
  slug: tackleio-invitations-api
- description: The Invoices API from Tackle.io — 1 operation(s) for invoices.
  name: Tackle.io Invoices API
  slug: tackleio-invoices-api
- description: AWS Marketplace context endpoints used to assemble offers and amendments.
  name: Tackle.io Marketplace API
  slug: tackleio-marketplace-api
- description: The Metering API from Tackle.io — 2 operation(s) for metering.
  name: Tackle.io Metering API
  slug: tackleio-metering-api
- description: Buyer instruction notification operations.
  name: Tackle.io Notifications API
  slug: tackleio-notifications-api
- description: 'Create, read, update, and list co-sell opportunities — the partner- originated (Outbound / Partner Referral) and AWS-originated (Inbound / AWS Referral) deals tracked in AWS Partner Central. Includes '
  name: Tackle.io Opportunities API
  slug: tackleio-opportunities-api
- description: Look up partner organizations in Microsoft Partner Center. Use the returned `organizationId` when adding a non-Microsoft partner via `inviteContexts`.
  name: Tackle.io Partners API
  slug: tackleio-partners-api
- description: Private offer lifecycle actions such as archive, cancel, and sync.
  name: Tackle.io Private Offer Actions API
  slug: tackleio-private-offer-actions-api
- description: AWS private-offer lifecycle (create, read, update, cancel, push to marketplace).
  name: Tackle.io Private Offers API
  slug: tackleio-private-offers-api
- description: Microsoft product and plan detail lookup.
  name: Tackle.io Products API
  slug: tackleio-products-api
- description: The public API from Tackle.io — 7 operation(s) for public.
  name: Tackle.io public API
  slug: tackleio-public-api
- description: Create, read, update, and list events on Microsoft Partner Center co-sell referrals (both outbound and inbound).
  name: Tackle.io Referrals API
  slug: tackleio-referrals-api
- description: Operations for Order Registrations
  name: Tackle.io Registrations API
  slug: tackleio-registrations-api
- description: Score domains and search scored accounts.
  name: Tackle.io Scores API
  slug: tackleio-scores-api
- description: Service provider configuration and capabilities
  name: Tackle.io Service Provider API
  slug: tackleio-service-provider-api
- description: Vendor-level reference data, including the picklist endpoint that supplies the acceptable values for opportunity fields.
  name: Tackle.io Settings API
  slug: tackleio-settings-api
- description: List the co-sell solutions registered with AWS Partner Central for your account. Solution identifiers are referenced by `solutions` on opportunities.
  name: Tackle.io Solutions API
  slug: tackleio-solutions-api
- description: Operations for Subscriptions
  name: Tackle.io Subscriptions API
  slug: tackleio-subscriptions-api
- description: User management operations
  name: Tackle.io Users API
  slug: tackleio-users-api
- description: Operations for API Versions
  name: Tackle.io Version API
  slug: tackleio-version-api
- description: Operations for Webhooks
  name: Tackle.io Webhooks API
  slug: tackleio-webhooks-api
artifact_total: 34
asyncapis:
- description: ''
  name: Tackleio Webhooks
  slug: tackleio-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.tackle.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tackle.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.tackle.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.tackle.io/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/tackleio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tackleio-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tackleio-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tackleio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tackleio-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tackleio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tackleio-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tackleio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/tackleio-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tackleio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tackleio-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tackleio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tackleio-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tackle.io
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tackleio-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tackleio-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tackleio-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tackleio-webhooks.yml
- group: operate
  title: ''
  type: Support
  url: https://help.tackle.io/
- group: company
  title: ''
  type: Blog
  url: https://tackle.io/resources-category/blogs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tackle.io/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tackle.io/privacy-policy-tackle-platform/
- group: company
  title: ''
  type: Website
  url: https://tackle.io
created: '2026-07-17'
description: 'Tackle.io is the Cloud Marketplace and Co-Sell platform that helps software vendors list, sell, co-sell, and meter through the AWS, Microsoft Azure, and Google Cloud marketplaces. The Tackle developer surface spans nine services: a core Platform API (authentication, webhooks, metering/usage records, products, subscriptions, disbursements, invoices, registrations), a Prospect buyer-signal scoring API, Co-Sell APIs for AWS Partner Central, Microsoft Partner Center, and Google Cloud, Private Offer APIs for the AWS and Microsoft marketplaces, a public Contracts API, and a SCIM 2.0 user-provisioning API. Authentication is OAuth 2.0 client-credentials (machine-to-machine) issuing short-lived JWT bearer tokens gated by fine-grained RBAC permissions.'
image: https://files.readme.io/f0c77fe-tackle-logo-light_1.png
layout: provider
mcp_servers:
- description: ''
  name: tackleio-mcp.yml
  slug: tackleio-mcpyml
modified: '2026-07-21'
name: Tackle.io
nav: Providers
network: true
overview: 'Tackle.io publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Contracts API, Currencies API, and 25 more. Tagged areas include Company, Cloud, Cloud Marketplace, Co-Sell, and AWS Marketplace.


  The Tackle.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tackle.io''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, support, and 21 more developer resources.'
random_paper: 54
scopes:
- name: Tackleio Scopes
  scope_count: 0
  slug: tackleio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.5
  delta: 0.4
  facets:
    commercial_clarity: 36.8
    contract_quality: 67.6
    developer_ergonomics: 69.0
    discoverability: 68.5
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 52.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tackleio Authentication
  slug: tackleio-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Tackleio Domain Security
  slug: tackleio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tackleio Trust Center
  slug: tackleio-trust-center
  summary_line: SOC 2
slug: tackleio
tags:
- Company
- Cloud
- Cloud Marketplace
- Co-Sell
- AWS Marketplace
- Azure Marketplace
- Google Cloud Marketplace
- Private Offers
- Metering
- SCIM
- Webhooks
- B2B SaaS
website: https://tackle.io
---

---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 72.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 108
  human_in_the_loop: 0
  name: Decisiv Agentic Access
  operation_count: 272
  slug: decisiv-agentic-access
  summary_line: 272 operations · 108 acting
api_count: 7
apis:
- description: 'Accounts, ecosystem users, account users and roles, and the webhook subscription surface for the Decisiv SRM Gateway. This is the module that manages webhook endpoints (URL, subscribed events, custom '
  name: Decisiv SRM Gateway - Account Management
  slug: decisiv-srm-gateway-account-management
- description: The fleet / asset-owner view of the SRM Gateway. Registered assets and components, depots, extended asset attributes, contacts, service requests to service providers, cases and case summaries, case no
  name: Decisiv SRM Gateway - Asset Management
  slug: decisiv-srm-gateway-asset-management
- description: The service-provider view of the SRM Gateway and the largest module. Cases and case actions, customers and customer assets, customer requests, line items with parts, additional charges, technician sto
  name: Decisiv SRM Gateway - Service Management
  slug: decisiv-srm-gateway-service-management
- description: 'Ingest and read connected-asset telematics inside SRM: diagnostic readings and fault codes for registered assets, so a fault on a vehicle can open or enrich a service case at the point of service.'
  name: Decisiv SRM Gateway - Telematics
  slug: decisiv-srm-gateway-telematics
- description: Global store of reference for all assets within the Decisiv ecosystem — asset lookup by id or VIN, plus campaigns, recalls, warranties, service history and OEM build information where authorized and a
  name: Decisiv Global Assets API
  slug: decisiv-global-assets-api
- description: Base API allowing dealers and service providers to interact with their customers and those customers' assets, including group customers and group assets. Swagger 2.0, secured with OAuth 2.0 plus the t
  name: Decisiv Service Provider API
  slug: decisiv-service-provider-api
- description: The original XML Platform API for service providers and dealer systems, covering the lifecycle of a service case — assets, cases, estimates and line items, parts, VMRS, notes, attachments and estimate
  name: Decisiv Platform API
  slug: decisiv-platform-api
artifact_total: 21
asyncapis:
- description: ''
  name: Decisiv Srm Gateway Webhooks
  slug: decisiv-srm-gateway-webhooks
collections:
- collection_type: open
  name: Account Management
  slug: open-decisiv-account-management
- collection_type: open
  name: Asset Management
  slug: open-decisiv-asset-management
- collection_type: open
  name: Global Assets API
  slug: open-decisiv-global-assets
- collection_type: open
  name: Service Management
  slug: open-decisiv-service-management
- collection_type: open
  name: Service Provider API
  slug: open-decisiv-service-provider
- collection_type: open
  name: Telematics
  slug: open-decisiv-telematics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/decisiv-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/decisiv-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.decisiv.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.decisiv.net/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.decisiv.net/
- group: docs
  title: ''
  type: APIReference
  url: https://srm-api.decisivapps.com/api-docs/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://www.decisivmarketplace.com/solutions-center/
- group: operate
  title: ''
  type: Support
  url: https://www.decisiv.com/resources/
- group: company
  title: ''
  type: Blog
  url: https://www.decisiv.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Decisiv
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.decisiv.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.decisiv.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.decisivmarketplace.com/product/srm-gateway-for-partners/
- group: start
  title: ''
  type: Login
  url: https://login.decisiv.net/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.decisiv.com/trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://www.decisiv.com/trust-center/
- group: other
  title: ''
  type: Marketplace
  url: https://www.decisivmarketplace.com/solutions-center/
- group: auth
  title: ''
  type: Authentication
  url: authentication/decisiv-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/decisiv-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/decisiv-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/decisiv-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/decisiv-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/decisiv-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/decisiv-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/decisiv-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/decisiv-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/decisiv-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/decisiv-srm-gateway-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/decisiv-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/decisiv-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/decisiv-packages.yml
- group: design
  title: ''
  type: Components
  url: components/decisiv-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/decisiv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/decisiv-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/decisiv-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/decisiv-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: 'Decisiv is the Reston, Virginia company behind the commercial vehicle industry''s Service Relationship Management (SRM) platform — a cloud service that connects fleets, asset owners, OEMs, dealers, independent service providers and component suppliers around a single service event. The platform orchestrates the whole repair lifecycle: asset registration and VIN-based identification, service requests, case creation, estimates and line items with VMRS coding, parts, labor and additional charges, technician time tasks, notes, attachments, approvals, sublet work between shops, and telematics-driven fault codes and diagnostic readings. Decisiv exposes this through the SRM Gateway APIs — four JSON:API-shaped OpenAPI 3.1 modules (Account Management, Asset Management, Service Management, Telematics) — plus the older Global Assets and Service Provider Swagger 2.0 APIs and the XML Platform API. Access is OAuth 2.0 and provisioned per account; documentation is public but credentials come
  through sales.'
image: https://www.decisiv.com/wp-content/uploads/2019/08/cropped-decisiv-favicon-1.png
layout: provider
modified: '2026-08-12'
name: Decisiv
nav: Providers
network: true
overview: 'Decisiv publishes 6 APIs on the [APIs.io](https://apis.io/) network, including SRM Gateway - Account Management, SRM Gateway - Asset Management, SRM Gateway - Service Management, and 3 more. Tagged areas include Company, commercial-vehicle, fleet-management, service-relationship-management, and telematics.


  The Decisiv catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Decisiv''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 30 more developer resources.'
plans:
- name: Decisiv Plans Pricing
  plan_count: 0
  slug: decisiv-plans-pricing
random_paper: 147
rate_limits:
- limit_count: 0
  name: Decisiv Rate Limits
  slug: decisiv-rate-limits
scopes:
- name: Decisiv Scopes
  scope_count: 5
  slug: decisiv-scopes
  summary_line: 5 scopes · authorizationCode/password
score:
  band: developing
  composite: 53.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 59.5
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 53.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Decisiv Authentication
  slug: decisiv-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Decisiv Domain Security
  slug: decisiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Decisiv Trust Center
  slug: decisiv-trust-center
  summary_line: ISO 27001, GDPR
slug: decisiv
tags:
- Company
- commercial-vehicle
- fleet-management
- service-relationship-management
- telematics
- asset-management
- maintenance-and-repair
- heavy-duty-trucking
- transportation
- dealer-management
- json-api
- webhooks
website: https://www.decisiv.com/
---

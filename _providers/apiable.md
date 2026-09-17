---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.5
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Apiable Agentic Access
  operation_count: 66
  slug: apiable-agentic-access
  summary_line: 66 operations · 36 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Apiable provides a self-service API portal platform for API product managers and developers. It offers single-tenant dedicated portals with custom domains, automated API documentation with try-out fun
  name: Apiable API Portal Platform
  slug: api-portal-platform
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: Companies, similar to teams are a way to group users together. Companies are a way to manage multiple teams and users together. An example being a company that has teams for different departments, suc
  name: Apiable Companies API
  slug: apiable-companies-api
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: Custom properties are additional fields that can be used to store extra information about the subscription.
  name: Apiable Custom Properties API
  slug: apiable-custom-properties-api
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: Docs are a way to store documentation in the system. The documentation can be used to store API and Plan level API documentations in the system.A documentation entry is always associated with either p
  name: Apiable Docs API
  slug: apiable-docs-api
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: Files are a way to store files in the system. All uploaded files are stored in an S3 bucket.
  name: Apiable Files API
  slug: apiable-files-api
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: Invitations are a way to invite new users to join the platform and team of the inviter. Invitations are typically sent by team members to new users, and can be accepted or ignored by the invitee.
  name: Apiable Invitations API
  slug: apiable-invitations-api
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: Plans are a way to group APIs and their documentation.
  name: Apiable Plans API
  slug: apiable-plans-api
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: Products are a high-level abstraction of your API products, they are used to group plans together and to provide a high level overview of the product.
  name: Apiable Products API
  slug: apiable-products-api
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: 'Operations related to managing subscriptions, including retrieval, update, approval, rejection, and refreshing the status of connected monetization. For security reasons, API keys, secrets, and other '
  name: Apiable Subscriptions API
  slug: apiable-subscriptions-api
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: Teams are a way to group users together. Teams are used to manage team-based access to subscriptions on the platform with internal roles and permissions. Teams typically consist of one to a handful of
  name: Apiable Teams API
  slug: apiable-teams-api
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: Users are the people who use the platform. Users can be invited to join the platform by an admin or they can sign up themselves. Users can be assigned to teams and have roles and permissions within th
  name: Apiable Users API
  slug: apiable-users-api
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: '# How Webhooks Work Webhooks are a way for services to communicate with each other in real time. When an event occurs, the Webhook sends an HTTP POST request to the URL that you''ve configured. The Web'
  name: Apiable Webhooks API
  slug: apiable-webhooks-api
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: Serverinfo is a way to get information about the server.
  name: Apiable Server Info API
  slug: apiable-server-info-api
artifact_total: 33
asyncapis:
- description: ''
  name: Apiable Webhooks
  slug: apiable-webhooks
common:
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/openapi/_original/apiable-platform-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/apiable-platform-api-openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://www.apiable.io/docs/api-reference/
- group: docs
  title: ''
  type: Documentation
  url: https://www.apiable.io/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.apiable.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.apiable.io/docs/get-started/onboarding/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apiable
- group: operate
  title: ''
  type: Support
  url: https://www.apiable.io/terms/support-policy/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.apiable.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apiable.io/terms/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apiable.io/terms/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apiable.io/
- group: auth
  title: ''
  type: Security
  url: https://www.apiable.io/security/
- group: auth
  title: ''
  type: Compliance
  url: https://www.apiable.io/security/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/lifecycle/apiable-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apiable-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/conventions/apiable-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apiable-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/errors/apiable-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apiable-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/conformance/apiable-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apiable-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/data-model/apiable-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apiable-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/asyncapi/apiable-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/apiable-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/mcp/apiable-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/apiable-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/llms/apiable-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiable-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/overlays/apiable-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apiable-platform-api-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/packages/apiable-packages.yml
  title: ''
  type: Packages
  url: packages/apiable-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/rate-limits/apiable-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apiable-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/plans/apiable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apiable-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/agentic-access/apiable-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apiable-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/scopes/apiable-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/apiable-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/authentication/apiable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apiable-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/security/apiable-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/apiable-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/security/apiable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apiable.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.apiable.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.apiable.io/resources/
created: '2025-01-08'
description: Apiable is an API portal platform that enables businesses to create single-tenant, white-label developer portals with custom domains, branding, and API product management. It supports API monetization, developer self-service onboarding, usage metrics, subscription lifecycle management, and integrates with API gateways including Amazon API Gateway and Kong.
features:
- description: Single-tenant dedicated portals with custom domains, branding, logos, and CSS whitelabeling.
  name: API Portal Generation
- description: Bundle APIs into products and plans with monetization options and subscription lifecycle management.
  name: API Product Management
- description: Automatically generate API documentation from specs with interactive try-out functionality and code samples.
  name: Auto-Generated API Documentation
- description: Self-service account creation, API subscription, and credential generation for developers.
  name: Developer Self-Service Onboarding
- description: Real-time API consumption tracking and usage dashboards for developers and administrators.
  name: Usage Metrics and Dashboards
- description: Team access control with role-based permissions and shared API credential management.
  name: Role-Based Access Control
- description: Deploy analytics and tracking tags via Google Tag Manager integration in developer portals.
  name: Google Tag Manager Integration
finops:
- name: Apiable Finops
  service_category: API
  slug: apiable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apiable.png
layout: provider
modified: '2026-09-16'
name: Apiable
nav: Providers
network: true
overview: 'Apiable publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Custom Properties API, Docs API, and 9 more. Tagged areas include Amazon API Gateway, API Gateway, API Monetization, API Portal, and Developer Experience.


  The Apiable catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Apiable''s developer surface includes API reference, documentation, getting-started guide, support, signup flow, authentication, pricing, and 27 more developer resources.'
plans:
- name: Apiable Plans Pricing
  plan_count: 0
  slug: apiable-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Apiable Rate Limits
  slug: apiable-rate-limits
scopes:
- name: Apiable Scopes
  scope_count: 3
  slug: apiable-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 67.8
    developer_ergonomics: 58.9
    discoverability: 66.7
    operational_transparency: 28.9
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/apiable/refs/heads/main/screenshots/apiable-2026-06-20T172223.png
security:
- kind: authentication
  name: Apiable Authentication
  slug: apiable-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Apiable Domain Security
  slug: apiable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Apiable Trust Center
  slug: apiable-trust-center
  summary_line: AWS Well-Architected Framework Review, ISO 27001, GDPR
slug: apiable
tags:
- Amazon API Gateway
- API Gateway
- API Monetization
- API Portal
- Developer Experience
- Developer Portal
- Developer Tools
- Kong
- Platform
- Self-Service
use_cases:
- description: Streamline partner API access with self-service portals and automated credential provisioning.
  name: Partner API Onboarding
- description: Implement usage-based billing and subscription plans for API product revenue generation.
  name: API Product Monetization
- description: Create branded developer portals where consumers can discover, subscribe to, and manage API access independently.
  name: Developer Self-Service Portals
- description: Scale API adoption by reducing onboarding friction through self-service workflows and automated access management.
  name: API Adoption Scaling
website: https://www.apiable.io/
---

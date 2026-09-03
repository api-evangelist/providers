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
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Apiable Agentic Access
  operation_count: 66
  slug: apiable-agentic-access
  summary_line: 66 operations · 36 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://developer.apiable.io
  baseurl_source: declared
  description: 'The Apiable Platform API (v2) is the REST API Apiable publishes for managing an API program programmatically: products, plans, subscriptions, teams, users, companies, invitations, documentation entrie'
  name: Apiable Platform API
  slug: platform-api
- description: Apiable provides a self-service API portal platform for API product managers and developers. It offers single-tenant dedicated portals with custom domains, automated API documentation with try-out fun
  name: Apiable API Portal Platform
  slug: api-portal-platform
artifact_total: 23
asyncapis:
- description: ''
  name: Apiable Webhooks
  slug: apiable-webhooks
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/apiable-platform-api-openapi.json
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
  title: ''
  type: Lifecycle
  url: lifecycle/apiable-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apiable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apiable-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apiable-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apiable-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/apiable-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apiable-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apiable-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/apiable-platform-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/apiable-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apiable-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/apiable-plans-pricing.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apiable-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/apiable-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apiable-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/apiable-trust-center.yml
- group: auth
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
mcp_servers:
- description: ''
  name: Apiable MCP Server
  slug: apiable-mcp-server
modified: '2026-09-02'
name: Apiable
nav: Providers
network: true
overview: 'Apiable publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include Amazon API Gateway, API Gateway, API Monetization, API Portal, and Developer Experience.


  The Apiable catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Apiable''s developer surface includes API reference, documentation, getting-started guide, support, signup flow, authentication, pricing, and 27 more developer resources.'
plans:
- name: Apiable Plans Pricing
  plan_count: 0
  slug: apiable-plans-pricing
random_paper: 4
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
  band: strong
  composite: 55.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 39.5
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 67.8
    developer_ergonomics: 58.9
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 16.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: rising
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

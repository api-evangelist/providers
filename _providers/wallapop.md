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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.1
  scored_at: '2026-08-12'
api_count: 6
apis:
- description: A category is a classification for product listings, with specific attributes and constraints that products within the category must adhere to.
  name: Wallapop Categories API
  slug: wallapop-categories-api
- description: The Delivery API from Wallapop — 1 operation(s) for delivery.
  name: Wallapop Delivery API
  slug: wallapop-delivery-api
- description: The Disputes API from Wallapop — 1 operation(s) for disputes.
  name: Wallapop Disputes API
  slug: wallapop-disputes-api
- description: An item refers to a listing created by a user on the Wallapop marketplace, indicating their intent to sell. These items can include a diverse range of products.
  name: Wallapop Items API
  slug: wallapop-items-api
- description: A shipping transaction is initiated when a seller accepts a shipping request.
  name: Wallapop Transactions API
  slug: wallapop-transactions-api
- description: Webhooks allow you to receive event notifications.
  name: Wallapop Webhooks API
  slug: wallapop-webhooks-api
artifact_total: 12
asyncapis:
- description: ''
  name: Wallapop Webhooks Catalog
  slug: wallapop-webhooks-catalog
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/wallapop-items-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.wallapop.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.wallapop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.wallapop.com/intro
- group: docs
  title: ''
  type: APIReference
  url: https://developers.wallapop.com/apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.wallapop.com/pages/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://ayuda.wallapop.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Wallapop
- group: commercial
  title: ''
  type: Pricing
  url: https://es.wallapop.com/wallapop-pro
- group: start
  title: ''
  type: SignUp
  url: https://es.wallapop.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://es.wallapop.com/toc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://es.wallapop.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wallapop-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wallapop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wallapop-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wallapop-domain-security.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wallapop-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wallapop-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wallapop-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wallapop-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wallapop-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wallapop-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wallapop-webhooks-catalog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wallapop-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/wallapop-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wallapop-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wallapop-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Wallapop is a Barcelona-based consumer marketplace for buying and selling second-hand items across Spain, Italy, and Portugal, backed by Accel, Insight Partners, and Northzone. Its Wallapop Connect API lets professional sellers and third-party integrators programmatically publish and manage listings (Items Connect API), accept shipping requests and track transactions through delivery (Transactions Connect API), and subscribe to signed event notifications (Webhooks Connect API), all secured with OAuth 2.0 Authorization Code + PKCE via its Keycloak-based identity service.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wallapop.png
layout: provider
mcp_servers:
- description: ''
  name: wallapop-mcp.yml
  slug: wallapop-mcpyml
modified: '2026-07-21'
name: Wallapop
nav: Providers
network: true
overview: 'Wallapop publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Delivery API, Disputes API, and 3 more. Tagged areas include Company, Consumer, Marketplace, Ecommerce, and Second-Hand.


  The Wallapop catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wallapop''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 21 more developer resources.'
random_paper: 24
rate_limits:
- limit_count: 3
  name: Wallapop Rate Limits
  slug: wallapop-rate-limits
scopes:
- name: Wallapop Scopes
  scope_count: 1
  slug: wallapop-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 55.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.5
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 60.5
  previous_composite: 55.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Wallapop Authentication
  slug: wallapop-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Wallapop Domain Security
  slug: wallapop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wallapop
tags:
- Company
- Consumer
- Marketplace
- Ecommerce
- Second-Hand
- Classifieds
- Shipping
- Webhooks
website: https://www.wallapop.com
---

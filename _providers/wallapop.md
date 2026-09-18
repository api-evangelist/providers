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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.9
  scored_at: '2026-09-17'
api_count: 3
apis:
- baseURL: https://connect.wallapop.com
  baseurl_source: declared
  description: A category is a classification for product listings, with specific attributes and constraints that products within the category must adhere to.
  name: Wallapop Categories API
  slug: wallapop-categories-api
- baseURL: https://connect.wallapop.com
  baseurl_source: declared
  description: The Delivery API from Wallapop — 1 operation(s) for delivery.
  name: Wallapop Delivery API
  slug: wallapop-delivery-api
- baseURL: https://connect.wallapop.com
  baseurl_source: declared
  description: The Disputes API from Wallapop — 1 operation(s) for disputes.
  name: Wallapop Disputes API
  slug: wallapop-disputes-api
- baseURL: https://connect.wallapop.com
  baseurl_source: declared
  description: An item refers to a listing created by a user on the Wallapop marketplace, indicating their intent to sell. These items can include a diverse range of products.
  name: Wallapop Items API
  slug: wallapop-items-api
- baseURL: https://connect.wallapop.com
  baseurl_source: declared
  description: A shipping transaction is initiated when a seller accepts a shipping request.
  name: Wallapop Transactions API
  slug: wallapop-transactions-api
- baseURL: https://connect.wallapop.com
  baseurl_source: declared
  description: Webhooks allow you to receive event notifications.
  name: Wallapop Webhooks API
  slug: wallapop-webhooks-api
artifact_total: 19
asyncapis:
- description: ''
  name: Wallapop Webhooks Catalog
  slug: wallapop-webhooks-catalog
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Items Connect Categories API
  slug: open-wallapop-categories-api
- collection_type: open
  name: Items Connect Categories Delivery API
  slug: open-wallapop-delivery-api
- collection_type: open
  name: Items Connect Categories Disputes API
  slug: open-wallapop-disputes-api
- collection_type: open
  name: Connect Categories Items API
  slug: open-wallapop-items-api
- collection_type: open
  name: Items Connect Categories Transactions API
  slug: open-wallapop-transactions-api
- collection_type: open
  name: Items Connect Categories Webhooks API
  slug: open-wallapop-webhooks-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/overlays/wallapop-items-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/changelog/wallapop-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/wallapop-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/authentication/wallapop-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wallapop-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/scopes/wallapop-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/wallapop-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/security/wallapop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wallapop-domain-security.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/rate-limits/wallapop-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wallapop-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/conventions/wallapop-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wallapop-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/errors/wallapop-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wallapop-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/lifecycle/wallapop-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wallapop-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/conformance/wallapop-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wallapop-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/data-model/wallapop-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wallapop-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/asyncapi/wallapop-webhooks-catalog.yml
  title: ''
  type: Webhooks
  url: asyncapi/wallapop-webhooks-catalog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/mcp/wallapop-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wallapop-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/packages/wallapop-packages.yml
  title: ''
  type: Packages
  url: packages/wallapop-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/well-known/wallapop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wallapop-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/llms/wallapop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wallapop-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Wallapop is a Barcelona-based consumer marketplace for buying and selling second-hand items across Spain, Italy, and Portugal, backed by Accel, Insight Partners, and Northzone. Its Wallapop Connect API lets professional sellers and third-party integrators programmatically publish and manage listings (Items Connect API), accept shipping requests and track transactions through delivery (Transactions Connect API), and subscribe to signed event notifications (Webhooks Connect API), all secured with OAuth 2.0 Authorization Code + PKCE via its Keycloak-based identity service.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wallapop.png
layout: provider
mcp_servers:
- description: ''
  name: Wallapop MCP Server
  slug: wallapop-mcp-server
modified: '2026-07-21'
name: Wallapop
nav: Providers
network: true
overview: 'Wallapop publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Delivery API, Disputes API, and 3 more. Tagged areas include Company, Consumer, Marketplace, E-Commerce, and Secondhand.


  The Wallapop catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wallapop''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 21 more developer resources.'
random_paper: 6
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
  composite: 51.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 63.1
    developer_ergonomics: 56.5
    discoverability: 81.5
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 51.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/wallapop/refs/heads/main/screenshots/wallapop-2026-08-17T082833.png
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
- E-Commerce
- Secondhand
- Classifieds
- Shipping
- Webhook
website: https://www.wallapop.com
---

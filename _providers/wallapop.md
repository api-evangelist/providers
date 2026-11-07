---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.4
  scored_at: '2026-11-06'
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
artifact_total: 25
asyncapis:
- description: ''
  name: Wallapop Webhooks Catalog
  slug: wallapop-webhooks-catalog
collections:
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
  href: https://artifacts.apis.io/wallapop/capabilities/wallapop-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/wallapop-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/wallapop/plans/wallapop-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wallapop-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/wallapop/overlays/wallapop-items-overlay.yaml
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
  href: https://artifacts.apis.io/wallapop/changelog/wallapop-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/wallapop-changelog.yml
- group: auth
  href: https://artifacts.apis.io/wallapop/authentication/wallapop-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wallapop-authentication.yml
- group: auth
  href: https://artifacts.apis.io/wallapop/scopes/wallapop-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/wallapop-scopes.yml
- group: auth
  href: https://artifacts.apis.io/wallapop/security/wallapop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wallapop-domain-security.yml
- group: operate
  href: https://artifacts.apis.io/wallapop/rate-limits/wallapop-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/wallapop-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/wallapop/conventions/wallapop-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wallapop-conventions.yml
- group: design
  href: https://artifacts.apis.io/wallapop/errors/wallapop-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wallapop-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wallapop/lifecycle/wallapop-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wallapop-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wallapop/conformance/wallapop-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wallapop-conformance.yml
- group: design
  href: https://artifacts.apis.io/wallapop/data-model/wallapop-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wallapop-data-model.yml
- group: design
  href: https://artifacts.apis.io/wallapop/asyncapi/wallapop-webhooks-catalog.yml
  title: ''
  type: Webhooks
  url: asyncapi/wallapop-webhooks-catalog.yml
- group: agent
  href: https://artifacts.apis.io/wallapop/mcp/wallapop-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wallapop-mcp.yml
- group: build
  href: https://artifacts.apis.io/wallapop/packages/wallapop-packages.yml
  title: ''
  type: Packages
  url: packages/wallapop-packages.yml
- group: agent
  href: https://artifacts.apis.io/wallapop/well-known/wallapop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wallapop-well-known.yml
- group: agent
  href: https://artifacts.apis.io/wallapop/llms/wallapop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wallapop-llms.txt
- group: agent
  href: https://artifacts.apis.io/wallapop/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Wallapop is a Barcelona-based consumer marketplace for buying and selling second-hand items across Spain, Italy, and Portugal, backed by Accel, Insight Partners, and Northzone. Its Wallapop Connect API lets professional sellers and third-party integrators programmatically publish and manage listings (Items Connect API), accept shipping requests and track transactions through delivery (Transactions Connect API), and subscribe to signed event notifications (Webhooks Connect API), all secured with OAuth 2.0 Authorization Code + PKCE via its Keycloak-based identity service.
finops:
- has_sources: true
  method: derived
  name: Wallapop Finops
  primary_unit: subscription
  service_category: ''
  slug: wallapop-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wallapop.png
layout: provider
mcp_servers:
- description: Remote MCP server at developers.wallapop.com over HTTP; 6 tools listed.
  name: Wallapop MCP Server
  slug: wallapop-connect-docs
modified: '2026-07-21'
name: Wallapop
nav: Providers
network: true
overview: 'Wallapop publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Categories API, Delivery API, Disputes API, and 3 more. Tagged areas include Company, Consumer, Marketplace, E-Commerce, and Secondhand.


  The Wallapop catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Wallapop''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 23 more developer resources.'
plans:
- name: Wallapop Plans Pricing
  plan_count: 3
  slug: wallapop-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Wallapop Rate Limits
  slug: wallapop-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Wallapop API Rules
  rule_count: 65
  severity_counts:
    error: 54
    hint: 0
    info: 5
    warn: 6
  slug: wallapop-rules
scopes:
- name: Wallapop Scopes
  scope_count: 1
  slug: wallapop-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 29
    catalog_earned: 71.5
    catalog_earned_first_party: 24.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 58.0
    developer_ergonomics: 56.5
    discoverability: 80.0
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 62.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wallapop/wallapop-2026-08-17T082833.png
security:
- kind: authentication
  name: Wallapop Authentication
  slug: wallapop-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Wallapop Domain Security
  slug: wallapop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: Fulfill a Wallapop sale
  slug: wallapop-fulfill-sale
- name: Manage Wallapop webhooks
  slug: wallapop-manage-webhooks
- name: Publish an item on Wallapop
  slug: wallapop-publish-item
- name: Rotate Wallapop inventory within listing limits
  slug: wallapop-rotate-inventory
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

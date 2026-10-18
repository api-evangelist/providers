---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Dynamic Yield Agentic Access
  operation_count: 23
  slug: dynamic-yield-agentic-access
  summary_line: 23 operations · 19 acting
api_count: 3
apis:
- description: Server-side Experience APIs and related product APIs for personalization, recommendations, event collection, product catalog sync, search, and the Shopping Muse AI assistant. Authenticated with a DY-A
  name: Dynamic Yield Experience OS API
  slug: dynamic-yield-experience-os-api
- baseURL: https://dy-api.com
  baseurl_source: declared
  description: API-only mode endpoints, for users who want to use the Experience APIs without using the full Experience OS features. In API-only mode, you are responsible for generating user and session IDs, and for
  name: Dynamic Yield API only API
  slug: dynamic-yield-api-only-api
- baseURL: https://dy-api.com
  baseurl_source: declared
  description: Serve user experience and track user interactions.
  name: Dynamic Yield Experience APIs API
  slug: dynamic-yield-experience-apis-api
- baseURL: https://dy-api.com
  baseurl_source: declared
  description: Update and monitor product data.
  name: Dynamic Yield Product Data API
  slug: dynamic-yield-product-data-api
- baseURL: https://dy-api.com
  baseurl_source: declared
  description: Retrieve user affinity data.
  name: Dynamic Yield Profile Anywhere API
  slug: dynamic-yield-profile-anywhere-api
- baseURL: https://dy-api.com
  baseurl_source: declared
  description: Update user data.
  name: Dynamic Yield User Data API
  slug: dynamic-yield-user-data-api-api
artifact_total: 12
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/agentic-access/dynamic-yield-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dynamic-yield-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/rules/dynamic-yield-rules.yml
  title: ''
  type: Spectral
  url: rules/dynamic-yield-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/json-ld/dynamic-yield-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dynamic-yield-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/vocabulary/dynamic-yield-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dynamic-yield-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/data-model/dynamic-yield-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dynamic-yield-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/errors/dynamic-yield-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dynamic-yield-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/mcp/dynamic-yield-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dynamic-yield-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/hosts/dynamic-yield-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dynamic-yield-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/vendors/dynamic-yield-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dynamic-yield-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/security/dynamic-yield-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynamic-yield-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dynamicyield.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dy.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://dy.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dy.dev/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dy.dev/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://dy.dev/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.dynamicyield.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.dynamicyield.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DynamicYield
- group: start
  title: ''
  type: Login
  url: https://marketing.dynamicyield.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dynamicyield.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dynamicyield.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/authentication/dynamic-yield-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dynamic-yield-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/packages/dynamic-yield-packages.yml
  title: ''
  type: Packages
  url: packages/dynamic-yield-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/packages/dynamic-yield-packages.yml
  title: ''
  type: SDKs
  url: packages/dynamic-yield-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/conventions/dynamic-yield-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dynamic-yield-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/lifecycle/dynamic-yield-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dynamic-yield-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/changelog/dynamic-yield-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dynamic-yield-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/conformance/dynamic-yield-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dynamic-yield-conformance.yml
created: '2026-07-17'
description: Dynamic Yield (a Mastercard company) is an experience optimization and personalization platform — branded "Experience OS" — used by retail, eCommerce, media, travel, and financial-services brands to individualize content, product recommendations, offers, search, and messaging across web, mobile app, email, and kiosk channels. The platform is MACH Alliance certified (microservices-based, API-first, cloud-native, headless) and exposes server-side Experience APIs (choose/collect for personalization and event tracking), a Product Feed / catalog API, a User Event API, Recommendation APIs, a Search API (query, pagination, filtering, sorting, autosuggest), and the Shopping Muse AI shopping-assistant API, alongside client-side script snippets and native mobile SDKs for iOS (Swift), Android (Kotlin), and React Native. Developer documentation, API reference, and a quarterly technical changelog are published at dy.dev. This profile was surfaced as a Bessemer Venture Partners portfolio
  company and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dynamic-yield.png
jsonld:
- class_count: 120
  name: Dynamic Yield Context
  property_count: 101
  slug: dynamic-yield-context
layout: provider
mcp_servers:
- description: Remote MCP server at dy.dev over HTTP.
  name: Dynamic Yield MCP Server
  slug: dynamic-yield
modified: '2026-07-18'
name: Dynamic Yield
nav: Providers
network: true
overview: 'Dynamic Yield publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including API only API, Experience APIs API, Product Data API, and 3 more. Tagged areas include Company, Cloud, Personalization, Experience Optimization, and Recommendations.


  The Dynamic Yield catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dynamic Yield''s developer surface includes documentation, API reference, getting-started guide, changelog, support, engineering blog, authentication, and 22 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Dynamic Yield API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 2
  slug: dynamic-yield-rules
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 15.7
  facets:
    access_clarity: 6.6
    contract_governance: 35.6
    contract_quality: 57.8
    developer_ergonomics: 61.9
    discoverability: 73.3
    operational_transparency: 18.4
  previous_composite: 25.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/dynamic-yield/refs/heads/main/screenshots/dynamic-yield-2026-07-25T212557.png
security:
- kind: authentication
  name: Dynamic Yield Authentication
  slug: dynamic-yield-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dynamic Yield Domain Security
  slug: dynamic-yield-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dynamic-yield
tags:
- Company
- Cloud
- Personalization
- Experience Optimization
- Recommendations
- A/B Testing
- Search
- E-Commerce
- Retail
- Machine Learning
- MACH
- Mastercard
website: https://www.dynamicyield.com/
---

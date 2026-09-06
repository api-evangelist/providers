---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-09-05'
api_count: 6
apis:
- baseURL: https://api.monetate.net/api/data/v1/{retailerShortname}/production
  baseurl_source: declared
  description: Create and manage data schemas and send customer, product and catalog data into Monetate in real time for use by the decision engine. Covers schema CRUD, schema types, upload history, row-level data P
  name: Monetate Data API
  slug: monetate-data-api
- baseURL: https://api.monetate.net/api/metadata/v1/{retailerShortname}/production
  baseurl_source: declared
  description: Read-only API returning metadata about a Monetate account so that experience, page-event and custom-target identifiers seen in engine responses and analytics exports can be resolved to human-interpret
  name: Monetate Metadata API
  slug: monetate-metadata-api
- description: Hosted Model Context Protocol server published on the monetate.com marketing site, advertised through RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-resource metadata. Provided by
  name: Monetate Website MCP Server
  slug: monetate-website-mcp-server
- baseURL: https://engine.monetate.net/api/engine/v1
  baseurl_source: declared
  description: The Decision API from Monetate — 1 operation(s) for decision.
  name: Monetate Decision API
  slug: monetate-decision-api
- baseURL: https://engine.monetate.net/api/engine/v1
  baseurl_source: declared
  description: Product Catalog related endpoints.
  name: Monetate Product Catalog API
  slug: monetate-product-catalog-api
- baseURL: https://engine.monetate.net/api/engine/v1
  baseurl_source: declared
  description: Schema related endpoints.
  name: Monetate Schema API
  slug: monetate-schema-api
- baseURL: https://engine.monetate.net/api/engine/v1
  baseurl_source: declared
  description: API methods for manipulating tokens.
  name: Monetate Token API
  slug: monetate-token-api
- baseURL: https://engine.monetate.net/api/engine/v1
  baseurl_source: declared
  description: File upload related endpoints.
  name: Monetate Upload API
  slug: monetate-upload-api
artifact_total: 20
collections:
- collection_type: open
  name: Monetate Auth API
  slug: open-monetate-auth-api
- collection_type: open
  name: Monetate Data API
  slug: open-monetate-data-api
- collection_type: open
  name: Monetate Engine API
  slug: open-monetate-engine-api
- collection_type: open
  name: Monetate Metadata API
  slug: open-monetate-metadata-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/monetate-engine-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/monetate-auth-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://monetate.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.monetate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.monetate.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.monetate.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.monetate.com/engine-api/engine-api-startup-guide
- group: operate
  title: ''
  type: Support
  url: https://monetate.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.monetate.com/docs
- group: company
  title: ''
  type: Blog
  url: https://monetate.com/media-type/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/monetate
- group: commercial
  title: ''
  type: Pricing
  url: https://monetate.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/monetate-plans-pricing.yml
- group: start
  title: ''
  type: Login
  url: https://marketer.monetate.net/auth/login/
- group: start
  title: ''
  type: SignUp
  url: https://monetate.com/demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monetate.com/website-privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://monetate.com/terms-of-use/
- group: operate
  title: ''
  type: StatusPage
  url: https://monetate.statuspage.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.monetate.com/docs/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/monetate-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.monetate.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/monetate-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/monetate-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/monetate-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/monetate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/monetate-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/monetate-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/monetate-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/monetate-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monetate-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/monetate-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monetate-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/monetate-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/monetate-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: Monetate is an enterprise experience-optimization and personalization platform for ecommerce and digital businesses, delivering A/B and multivariate testing, automated 1:1 personalization, product and content recommendations, personalized search, dynamic bundles, social proof and product badging across web, mobile, email and in-store channels. Its decision engine is exposed to developers through four public REST APIs — the Engine API (real-time decision requests), the Data API (schema definition, customer/product data ingestion and default catalog management), the Metadata API (accounts, experiences, page events and custom targets) and the Auth API (bearer-token issue and refresh) — plus a browser JavaScript API and native SDKs for iOS, Android, React Web and React Native. Monetate operates as part of Kibo Commerce.
image: https://images.archbee.com/ceIfEvQHzQk1IVxoRWUh7/48dIncdY24xPwZLOvfSEr_horizontal-pink-blue-800px.png
layout: provider
mcp_servers:
- description: ''
  name: Monetate MCP Server
  slug: monetate-mcp-server
- description: ''
  name: Monetate MCP Server
  slug: monetate-mcp-server-2
modified: '2026-08-12'
name: Monetate
nav: Providers
network: true
overview: 'Monetate publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Data API, Metadata API, Decision API, and 4 more. Tagged areas include Company, Personalization, Experience Optimization, A/B Testing, and E-Commerce.


  Monetate''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Monetate Plans Pricing
  plan_count: 0
  slug: monetate-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Monetate Rate Limits
  slug: monetate-rate-limits
score:
  band: developing
  composite: 50.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 53.1
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 50.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monetate/refs/heads/main/screenshots/monetate-2026-08-17T081059.png
security:
- kind: authentication
  name: Monetate Authentication
  slug: monetate-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Monetate Domain Security
  slug: monetate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Monetate Vulnerability Disclosure
  slug: monetate-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Monetate Trust Center
  slug: monetate-trust-center
  summary_line: trust center published
slug: monetate
tags:
- Company
- Personalization
- Experience Optimization
- A/B Testing
- E-Commerce
- Product Recommendations
- Personalized Search
- Marketing
- Customer Data
- Retail
- Decision Engine
website: https://monetate.com/
---

---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-08-17'
api_count: 5
apis:
- description: RESTful entry point to the Monetate decision engine. A client POSTs a batch of context events, page events and record events for a session and receives back the actions (experiences) the engine decide
  name: Monetate Engine API
  slug: monetate-engine-api
- description: Create and manage data schemas and send customer, product and catalog data into Monetate in real time for use by the decision engine. Covers schema CRUD, schema types, upload history, row-level data P
  name: Monetate Data API
  slug: monetate-data-api
- description: Read-only API returning metadata about a Monetate account so that experience, page-event and custom-target identifiers seen in engine responses and analytics exports can be resolved to human-interpret
  name: Monetate Metadata API
  slug: monetate-metadata-api
- description: 'Issues and refreshes the bearer tokens used by the Data API and Metadata API. A signed JWT user key is exchanged for a token with a caller-specified TTL; the token is then sent as an `Authorization: T'
  name: Monetate Auth API
  slug: monetate-auth-api
- description: Hosted Model Context Protocol server published on the monetate.com marketing site, advertised through RFC 8414 OAuth authorization-server metadata and RFC 9728 protected-resource metadata. Provided by
  name: Monetate Website MCP Server
  slug: monetate-website-mcp-server
artifact_total: 17
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
  name: monetate-mcp.yml
  slug: monetate-mcpyml
- description: ''
  name: http
  slug: http
modified: '2026-08-12'
name: Monetate
nav: Providers
network: true
overview: 'Monetate publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Engine API, Data API, Metadata API, and 1 more. Tagged areas include Company, Personalization, Experience Optimization, A/B Testing, and Ecommerce.


  Monetate''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Monetate Plans Pricing
  plan_count: 0
  slug: monetate-plans-pricing
random_paper: 116
rate_limits:
- limit_count: 0
  name: Monetate Rate Limits
  slug: monetate-rate-limits
score:
  band: developing
  composite: 53.1
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 52.0
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 53.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
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
- Ecommerce
- Product Recommendations
- Personalized Search
- Marketing
- Customer Data
- Retail
- Decision Engine
website: https://monetate.com/
---

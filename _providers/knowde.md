---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: The GraphQL API is Knowde's recommended primary programmatic interface to the platform — anything possible in the REST API is intended to also be possible in GraphQL. The reference is generated from t
  name: Knowde GraphQL API
  slug: knowde-graphql-api
- description: The Knowde REST API is organized around RESTful resources with predictable resource-oriented URLs, JSON-encoded payloads and responses, and standard HTTP verbs and status codes. Resources include prod
  name: Knowde REST API
  slug: knowde-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/knowde-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/knowde-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.knowde.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.knowde.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.knowde.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://developer.knowde.com/documentation/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.knowde.com/documentation/api_clients
- group: auth
  title: ''
  type: Authentication
  url: authentication/knowde-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/knowde-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/knowde-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/knowde-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/knowde-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/knowde-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/knowde-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.knowde.com/documentation/rate_limits
- group: start
  title: ''
  type: SignUp
  url: https://www.knowde.com/sign-in
- group: start
  title: ''
  type: Login
  url: https://www.knowde.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://privacy.knowde.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.knowde.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://help.knowde.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blog.knowde.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knowde
- group: operate
  title: ''
  type: StatusPage
  url: https://status.knowde.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.knowde.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/knowde-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.knowde.com/resources/whats-new
- group: other
  title: ''
  type: Marketplace
  url: https://www.knowde.com/marketplace
- group: company
  title: ''
  type: Partners
  url: https://www.knowde.com/partners
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/knowde/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/knowde
created: '2026-08-01'
description: Knowde is an AI platform for industrial operations, built for the chemicals and ingredients industry. Knowde AI extracts, structures, harmonizes and enriches product data out of legacy systems and offline documents; Knowde MDM is the master data repository that data lands in; Knowde CXP launches supplier storefronts natively integrated with MDM; and the Knowde Marketplace is a network of 8,000+ chemical company storefronts. The Knowde API gives customers programmatic access to that platform through a GraphQL API (the recommended primary interface) and a RESTful JSON API, both served from developer-api.knowde.com behind OAuth 2.0 client credentials, with API Clients provisioned in the Developer Portal and a documented PIMS filter grammar for querying product, category and attribute data.
image: https://cdn.cxp.knowde.com/store/15d89a6e-1b0d-4b12-9ae9-06ae9d224a7b/knowde-logo_0b24070d06cb.svg
layout: provider
modified: '2026-08-01'
name: Knowde
nav: Providers
network: true
overview: 'Knowde publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chemicals, Ingredients, Marketplace, and Master Data Management.


  Knowde''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, signup flow, support, and 23 more developer resources.'
random_paper: 68
score:
  band: thin
  composite: 36.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 36.7
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/knowde/refs/heads/main/screenshots/knowde-2026-08-07T171300.png
security:
- kind: authentication
  name: Knowde Authentication
  slug: knowde-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Knowde Domain Security
  slug: knowde-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Knowde Trust Center
  slug: knowde-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27701:2019
slug: knowde
tags:
- Company
- Chemicals
- Ingredients
- Marketplace
- Master Data Management
- Product Information Management
- Manufacturing
- Distribution
- B2B Commerce
- GraphQL
- Artificial Intelligence
website: https://www.knowde.com/
---

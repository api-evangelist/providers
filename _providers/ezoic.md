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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ezoic Agentic Access
  operation_count: 3
  slug: ezoic-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: The Access API from ezoic — 1 operation(s) for access.
  name: ezoic Access API
  slug: ezoic-access-api
- description: The Products API from ezoic — 1 operation(s) for products.
  name: ezoic Products API
  slug: ezoic-products-api
- description: The Purchases API from ezoic — 1 operation(s) for purchases.
  name: ezoic Purchases API
  slug: ezoic-purchases-api
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ezoic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ezoic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ezoic.com/docs/subscriptions/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ezoic.com/docs/ezoicads/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://support.ezoic.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.ezoic.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ezoic.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ezoic
- group: operate
  title: ''
  type: StatusPage
  url: https://ezoicstatus.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ezoic.com/docs/ezoic-legacy-features/legacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ezoic.com/pricing
- group: start
  title: ''
  type: Login
  url: https://pubdash.ezoic.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ezoic.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ezoic.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ezoic-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ezoic-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/ezoic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ezoic-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ezoic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ezoic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ezoic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ezoic-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ezoic-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ezoic-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/ezoic-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ezoic-agentic-access.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ezoic.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ezoic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ezoic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ezoic.com/
created: '2026-07-17'
description: Ezoic is a website monetization and audience-growth platform for publishers, and a performance advertising marketplace for brands. Publishers integrate EzoicAds (via JavaScript, mobile SDKs for Android/iOS/Flutter/React Native/Unity, or framework SDKs for Angular/React/Vue) to run native, sticky, video, anchor, rewarded, and interstitial ad formats across 5,000+ premium sites. Beyond ads, Ezoic offers first-party Identity (ezID), Visitor Accounts (ezAuth), Ezoic Subscriptions (paywalls, donations, and a server-to-server REST API for verifying reader access), a Web Games ad SDK, Custom Events into its Big Data Analytics platform, and an official hosted Analytics MCP server that exposes read-only pageview, ad-impression, rewarded, and video analytics to AI assistants over OAuth.
image: https://www.ezoic.com/wp-content/uploads/2021/03/ezoic-logo.png
layout: provider
mcp_servers:
- description: ''
  name: ezoic-mcp.yml
  slug: ezoic-mcpyml
modified: '2026-07-19'
name: ezoic
nav: Providers
network: true
overview: 'ezoic publishes 3 APIs on the [APIs.io](https://apis.io/) network: Access API, Products API, and Purchases API. Tagged areas include Company, Advertising, AdTech, Publisher Monetization, and Analytics.


  ezoic''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 24 more developer resources.'
random_paper: 58
score:
  band: developing
  composite: 54.5
  delta: -0.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 64.1
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ezoic/refs/heads/main/screenshots/ezoic-2026-07-25T214052.png
security:
- kind: authentication
  name: Ezoic Authentication
  slug: ezoic-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Ezoic Domain Security
  slug: ezoic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ezoic Vulnerability Disclosure
  slug: ezoic-vulnerability-disclosure
  summary_line: disclosure policy published
slug: ezoic
tags:
- Company
- Advertising
- AdTech
- Publisher Monetization
- Analytics
- Subscriptions
- Identity
- MCP
website: https://www.ezoic.com/
---

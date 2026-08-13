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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: REST API for brands/advertisers to manage campaigns, partner recruitment and contracts, catalogs, reporting, and payouts across affiliate and partnership programs. Current version v13.
  name: impact.com Brand API
  slug: impactcom-brand-api
- description: REST API for media partners/publishers to access content and tracking links, retrieve actions and commissions, and report on performance. Current version v15.
  name: impact.com Partner API
  slug: impactcom-partner-api
- description: REST API for agencies managing multiple client accounts, consolidated reporting, and cross-client workflows. Current version v3.
  name: impact.com Agency API
  slug: impactcom-agency-api
artifact_total: 8
asyncapis:
- description: ''
  name: Impact Radius Advocate Webhooks
  slug: impact-radius-advocate-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://impact.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://integrations.impact.com/
- group: docs
  title: ''
  type: Documentation
  url: https://integrations.impact.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://integrations.impact.com/rest-apis/api-quick-start.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/impact-radius-authentication.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.impact.com/en/support/home
- group: operate
  title: ''
  type: Support
  url: https://help.impact.com/en/support/home
- group: company
  title: ''
  type: Blog
  url: https://impact.com/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://impact.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.impact.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.impact.com/login.user
- group: commercial
  title: ''
  type: TermsOfService
  url: https://impact.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://impact.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.impact.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/impact-radius-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/impact-radius-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/impact-radius-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/impact-radius-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/impact-radius-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://impact.responsibledisclosure.com/hc/en-us
- group: auth
  title: ''
  type: DomainSecurity
  url: security/impact-radius-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/impact-radius-advocate-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/impact-radius-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/impact-radius-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/impact-radius-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/impact-radius-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/impact-radius-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/impact-radius-conventions.yml
created: '2026-07-17'
description: Impact Radius, now operating as impact.com, is a partnership management platform for managing affiliate programs, influencer and creator partnerships, and customer referral (advocate) initiatives at scale. Brands, agencies, and publishers use it to discover and recruit partners, contract and pay them against business outcomes, track partner-driven traffic and conversions with privacy-first attribution across devices, protect programs from fraud, and optimize performance with predictive analytics. The platform exposes REST APIs for Brands, Partners (media partners), and Agencies, plus Advocate program APIs with webhooks, GraphQL, mobile SDKs, an official hosted MCP server, and machine-readable docs (llms.txt and OpenAPI) for agent and AI-assisted integration.
image: https://impact.com/wp-content/uploads/2022/04/impact-logo-square.jpg
layout: provider
mcp_servers:
- description: ''
  name: impact-radius-mcp.yml
  slug: impact-radius-mcpyml
modified: '2026-07-19'
name: Impact Radius
nav: Providers
network: true
overview: 'Impact Radius publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Partnership Management, Affiliate Marketing, Influencer Marketing, and Referral Marketing.


  The Impact Radius catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Impact Radius'' developer surface includes documentation, getting-started guide, authentication, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 50.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 92.6
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 50.8
  provenance:
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/impact-radius/refs/heads/main/screenshots/impact-radius-2026-07-25T222140.png
security:
- kind: authentication
  name: Impact Radius Authentication
  slug: impact-radius-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Impact Radius Domain Security
  slug: impact-radius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Impact Radius Vulnerability Disclosure
  slug: impact-radius-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: impact-radius
tags:
- Company
- Partnership Management
- Affiliate Marketing
- Influencer Marketing
- Referral Marketing
- Attribution
- Martech
- Advocate
- Creator Economy
- E-Commerce
website: https://impact.com/
---

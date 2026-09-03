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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Hosted Model Context Protocol server that doubles as Polar's HTTP API surface; invoke tools at POST https://api.polaranalytics.com/mcp/tool/<tool_name> with a Bearer API key. Exposes 8 tools for gener
  name: Polar Headless MCP
  slug: polar-headless-mcp
- description: First-party, server-side tracking pixel that captures the ecommerce customer journey from the merchant's own domain and builds a graph-based Lifetime ID. Client events are reported via the @polar-anal
  name: Polar Pixel
  slug: polar-pixel
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.polaranalytics.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/polar-analytics-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/polar-analytics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polar-analytics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/polar-analytics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/polar-analytics-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.polaranalytics.com/policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polar-analytics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polar-analytics-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/polar-analytics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/polar-analytics-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/polar-analytics-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://polaranalytics.statuspage.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/polar-analytics
- group: docs
  title: ''
  type: Documentation
  url: https://intercom.help/polar-app/en/
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/polar-app/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.polaranalytics.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.polaranalytics.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.polaranalytics.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.polaranalytics.com/policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.polaranalytics.com/policy
created: '2026-07-17'
description: Polar Analytics is an all-in-one data analytics and AI platform purpose-built for Shopify-based ecommerce and DTC brands. It consolidates data from 45+ sources into a dedicated Snowflake warehouse, ships 400+ pre-built ecommerce metrics with a semantic layer, and adds a first-party pixel with lifetime ID, incrementality testing, Klaviyo audience enrichment, and advertising conversion signals for Meta and Google. Its AI layer includes agents for data analysis, media buying, email marketing, and inventory planning, all exposed to LLM clients through the hosted Polar Headless MCP server at api.polaranalytics.com/mcp with Bearer API-key and OAuth 2.0 access. Backed by point-nine.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/polar-analytics.png
layout: provider
mcp_servers:
- description: ''
  name: Polar Headless MCP
  slug: polar-headless-mcp
modified: '2026-07-20'
name: Polar Analytics
nav: Providers
network: true
overview: 'Polar Analytics publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, E-Commerce, Shopify, and Business Intelligence.


  Polar Analytics'' developer surface includes authentication, documentation, support, pricing, engineering blog, and 17 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 30.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polar-analytics/refs/heads/main/screenshots/polar-analytics-2026-09-02T151642.png
security:
- kind: authentication
  name: Polar Analytics Authentication
  slug: polar-analytics-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Polar Analytics Domain Security
  slug: polar-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: polar-analytics
tags:
- Company
- Analytics
- E-Commerce
- Shopify
- Business Intelligence
- MCP
- AI Agents
- Data
website: https://www.polaranalytics.com
---

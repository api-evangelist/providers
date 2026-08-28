---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: 'REST API over Daloopa''s fundamental dataset — company discovery, fundamental series and values, calendar/fiscal period handling, taxonomy metrics and industry templates, SEC document lookup, document '
  name: Daloopa API v3
  slug: daloopa-api-v3
- description: Hosted remote MCP server (Streamable HTTP) exposing nine tools over the same fundamental dataset — discover_companies, discover_company_series, discover_company_documents, get_company_fundamentals, ge
  name: Daloopa MCP Server
  slug: daloopa-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Daloopa Webhooks
  slug: daloopa-webhooks
collections:
- collection_type: open
  name: Daloopa API
  slug: open-daloopa-api
- collection_type: open
  name: Daloopa MCP Service
  slug: open-daloopa-mcp-service
common:
- group: company
  title: ''
  type: Website
  url: https://daloopa.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.daloopa.com/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.daloopa.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.daloopa.com/reference/companies_list_v3
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.daloopa.com/docs/api-authentication
- group: operate
  title: ''
  type: Support
  url: https://docs.daloopa.com/docs/contact-us
- group: company
  title: ''
  type: Blog
  url: https://daloopa.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://daloopa.com/blog/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/daloopa
- group: start
  title: ''
  type: SignUp
  url: https://daloopa.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daloopa.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daloopa.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.daloopa.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/daloopa-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/daloopa-lifecycle.yml
- group: agent
  title: ''
  type: LLMSTxt
  url: llms/daloopa-llms.txt
- group: agent
  title: ''
  type: LLMSTxt
  url: https://docs.daloopa.com/llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/daloopa-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/daloopa-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/daloopa-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/daloopa-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.daloopa.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/daloopa-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/daloopa-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/daloopa-components.yml
created: '2026-08-11'
description: Daloopa is an AI-powered fundamental financial data platform for institutional investors, providing analyst-verified, source-linked financial data extracted from SEC filings, earnings transcripts, investor presentations and press releases. Coverage spans 6,000+ global public companies with roughly 14 years of history, and every datapoint is hyperlinked back to the exact location in the original source document for auditability. The company sells to hedge funds, mutual funds, investment banks, equity research and private equity teams, and delivers the same dataset across a REST API, a hosted remote MCP server, an Excel add-in, prebuilt Data Sheets, the Scout AI modeling agent, and native cloud-warehouse shares via Snowflake, Databricks and AWS S3.
image: https://avatars.githubusercontent.com/u/42851514?v=4
layout: provider
mcp_servers:
- description: ''
  name: Daloopa MCP Server
  slug: daloopa-mcp-server
- description: ''
  name: Daloopa MCP Server
  slug: daloopa-mcp-server-2
modified: '2026-08-11'
name: Daloopa
nav: Providers
network: true
overview: 'Daloopa publishes 2 APIs on the [APIs.io](https://apis.io/) network: API v3 and MCP Server. Tagged areas include Financial Data, Fundamental Data, Market Data, Investment Research, and Equity Research.


  The Daloopa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Daloopa''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 20 more developer resources.'
plans:
- name: Daloopa Plans Pricing
  plan_count: 0
  slug: daloopa-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Daloopa Rate Limits
  slug: daloopa-rate-limits
score:
  band: strong
  composite: 54.6
  delta: 7.2
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 16.7
    contract_quality: 64.5
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 55.3
  previous_composite: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 60.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/daloopa/refs/heads/main/screenshots/daloopa-2026-08-17T080848.png
security:
- kind: authentication
  name: Daloopa Authentication
  slug: daloopa-authentication
  summary_line: http/oauth2/apiKey · 4 schemes
- kind: domain-security
  name: Daloopa Domain Security
  slug: daloopa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Daloopa Trust Center
  slug: daloopa-trust-center
  summary_line: trust center published
slug: daloopa
tags:
- Financial Data
- Fundamental Data
- Market Data
- Investment Research
- Equity Research
- SEC Filings
- Earnings
- Fintech
- MCP
- agent-native
- Agent Skills
- Webhook
- Data Warehouse
website: https://daloopa.com/
---

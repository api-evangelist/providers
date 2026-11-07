---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 64.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Auth API from Daloopa — 10 operation(s) for auth.
  name: Daloopa Auth API
  slug: daloopa-auth-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: Company Data and Metadata
  name: Daloopa Companies API
  slug: daloopa-companies-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Consumption API from Daloopa — 6 operation(s) for consumption.
  name: Daloopa Consumption API
  slug: daloopa-consumption-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Daloopa MCP Service API from Daloopa — 1 operation(s) for daloopa mcp service.
  name: Daloopa MCP Service API
  slug: daloopa-daloopa-mcp-service-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Data Warehouse API from Daloopa — 1 operation(s) for data warehouse.
  name: Daloopa Data Warehouse API
  slug: daloopa-data-warehouse-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Databricks API from Daloopa — 1 operation(s) for databricks.
  name: Daloopa Databricks API
  slug: daloopa-databricks-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Documents API from Daloopa — 5 operation(s) for documents.
  name: Daloopa Documents API
  slug: daloopa-documents-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Download API from Daloopa — 2 operation(s) for download.
  name: Daloopa Download API
  slug: daloopa-download-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Export API from Daloopa — 1 operation(s) for export.
  name: Daloopa Export API
  slug: daloopa-export-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: Financial Fundamentals Data
  name: Daloopa Fundamentals API
  slug: daloopa-fundamentals-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Health API from Daloopa — 1 operation(s) for health.
  name: Daloopa Health API
  slug: daloopa-health-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Industry Models API from Daloopa — 1 operation(s) for industry models.
  name: Daloopa Industry Models API
  slug: daloopa-industry-models-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Investing Skills API from Daloopa — 2 operation(s) for investing skills.
  name: Daloopa Investing Skills API
  slug: daloopa-investing-skills-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Market Data API from Daloopa — 2 operation(s) for market data.
  name: Daloopa Market Data API
  slug: daloopa-market-data-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Partnership API from Daloopa — 1 operation(s) for partnership.
  name: Daloopa Partnership API
  slug: daloopa-partnership-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Series API from Daloopa — 1 operation(s) for series.
  name: Daloopa Series API
  slug: daloopa-series-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Snowflake API from Daloopa — 1 operation(s) for snowflake.
  name: Daloopa Snowflake API
  slug: daloopa-snowflake-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Taxonomy API from Daloopa — 5 operation(s) for taxonomy.
  name: Daloopa Taxonomy API
  slug: daloopa-taxonomy-api
- baseURL: https://app.daloopa.com/api/v3
  baseurl_source: declared
  description: The Webhooks API from Daloopa — 6 operation(s) for webhooks.
  name: Daloopa Webhooks API
  slug: daloopa-webhooks-api
artifact_total: 51
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
- group: other
  href: https://artifacts.apis.io/daloopa/capabilities/daloopa-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/daloopa-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/daloopa/overlays/daloopa-api-security-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/daloopa-api-security-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/daloopa/mcp/daloopa-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/daloopa-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.daloopa.com/server/mcp
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
  href: https://artifacts.apis.io/daloopa/lifecycle/daloopa-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/daloopa-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/daloopa/lifecycle/daloopa-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/daloopa-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/daloopa/llms/daloopa-llms.txt
  title: ''
  type: LLMSTxt
  url: llms/daloopa-llms.txt
- group: agent
  title: ''
  type: LLMSTxt
  url: https://docs.daloopa.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/daloopa/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/daloopa/packages/daloopa-packages.yml
  title: ''
  type: Packages
  url: packages/daloopa-packages.yml
- group: design
  href: https://artifacts.apis.io/daloopa/conformance/daloopa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/daloopa-conformance.yml
- group: auth
  href: https://artifacts.apis.io/daloopa/security/daloopa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daloopa-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/daloopa/security/daloopa-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/daloopa-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.daloopa.com/
- group: commercial
  href: https://artifacts.apis.io/daloopa/plans/daloopa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/daloopa-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/daloopa/rate-limits/daloopa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/daloopa-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/daloopa/components/daloopa-components.yml
  title: ''
  type: Components
  url: components/daloopa-components.yml
created: '2026-08-11'
description: Daloopa is an AI-powered fundamental financial data platform for institutional investors, providing analyst-verified, source-linked financial data extracted from SEC filings, earnings transcripts, investor presentations and press releases. Coverage spans 6,000+ global public companies with roughly 14 years of history, and every datapoint is hyperlinked back to the exact location in the original source document for auditability. The company sells to hedge funds, mutual funds, investment banks, equity research and private equity teams, and delivers the same dataset across a REST API, a hosted remote MCP server, an Excel add-in, prebuilt Data Sheets, the Scout AI modeling agent, and native cloud-warehouse shares via Snowflake, Databricks and AWS S3.
finops:
- has_sources: true
  method: derived
  name: Daloopa Finops
  primary_unit: ''
  service_category: ''
  slug: daloopa-finops
  template: true
image: https://avatars.githubusercontent.com/u/42851514?v=4
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.daloopa.com over HTTP; 9 tools listed.
  name: Daloopa MCP Server
  slug: daloopa
modified: '2026-09-16'
name: Daloopa
nav: Providers
network: true
overview: 'Daloopa publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Companies API, Consumption API, and 16 more. Tagged areas include Financial Data, Fundamental Data, Market Data, Investment Research, and Equity Research.


  The Daloopa catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Daloopa''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 24 more developer resources.'
plans:
- name: Daloopa Plans Pricing
  plan_count: 0
  slug: daloopa-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Daloopa Rate Limits
  slug: daloopa-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Daloopa API Rules
  rule_count: 60
  severity_counts:
    error: 41
    hint: 0
    info: 5
    warn: 14
  slug: daloopa-rules
score:
  band: strong
  composite: 56.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 66.8
    developer_ergonomics: 60.7
    discoverability: 75.0
    operational_transparency: 63.2
  previous_composite: 52.4
  provenance:
    conformance: derived
    contracts:
      callable: 84.2
      derived: 0
      marker_coverage: 94.7
      total: 19
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/daloopa/daloopa-2026-08-17T080848.png
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
skill_count: 21
skills:
- name: build-model
  slug: daloopa-build-model
- name: bull-bear
  slug: daloopa-bull-bear
- name: capital-allocation
  slug: daloopa-capital-allocation
- name: comp-sheet
  slug: daloopa-comp-sheet
- name: comps
  slug: daloopa-comps
- name: dcf
  slug: daloopa-dcf
- name: earnings-flash
  slug: daloopa-earnings-flash
- name: earnings-prep
  slug: daloopa-earnings-prep
- name: earnings-review
  slug: daloopa-earnings-review
- name: guidance-tracker
  slug: daloopa-guidance-tracker
- name: ib-deck
  slug: daloopa-ib-deck
- name: industry
  slug: daloopa-industry
- name: inflection
  slug: daloopa-inflection
- name: initiate
  slug: daloopa-initiate
- name: precedent-transactions
  slug: daloopa-precedent-transactions
- name: research-note
  slug: daloopa-research-note
- name: setup
  slug: daloopa-setup
- name: supply-chain
  slug: daloopa-supply-chain
- name: tearsheet
  slug: daloopa-tearsheet
- name: unit-economics
  slug: daloopa-unit-economics
- name: working-capital
  slug: daloopa-working-capital
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
- Agent-Native
- Agent Skills
- Webhook
- Data Warehouse
website: https://daloopa.com/
---

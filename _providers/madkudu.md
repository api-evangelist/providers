---
access_model:
  confidence: high
  label: API access add-on, contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developers.madkudu.com/getting-started/usage-and-credits
  - https://developers.madkudu.com/readme.md
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.4
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The current MadKudu API (MadAPI) exposes account and person lookup, full account/person details and activities, company hiring/job-posting enrichment, advanced account and person search, prospect disc
  name: MadKudu API (MadAPI)
  slug: madkudu-api-madapi
- description: The legacy MadKudu Scoring API returns customer-fit (demographics), likelihood-to-buy and lead-grade scores for companies by domain and persons by email, plus a job-changes watch list and a ping utili
  name: MadKudu Legacy Scoring API
  slug: madkudu-legacy-scoring-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://madkudu.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.madkudu.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.madkudu.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.madkudu.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.madkudu.com/getting-started/quickstart
- group: agent
  title: ''
  type: MCPServer
  url: mcp/madkudu-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/madkudu-tool-crosswalk.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MadKudu
- group: operate
  title: ''
  type: Support
  url: mailto:support@madkudu.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.madkudu.com/
- group: company
  title: ''
  type: Blog
  url: https://madkudu.com/blog
- group: start
  title: ''
  type: Login
  url: https://msi.madkudu.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hginsights.com/product/pricing-guide/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hginsights.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hginsights.com/privacy-page/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.madkudu.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/madkudu-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/madkudu-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/madkudu-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/madkudu-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/madkudu-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/madkudu-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/madkudu-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/madkudu-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/madkudu-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/madkudu-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/madkudu-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/madkudu-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/madkudu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/madkudu-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/madkudu-llms.txt
created: '2026-07-17'
description: MadKudu is a predictive lead scoring and account intelligence platform for B2B sales and marketing teams, using AI-driven propensity modeling and dynamic scoring across fit, intent, and engagement signals to surface high-propensity accounts and people. Its developer surface (MadAPI) programmatically exposes account and person lookup, enrichment, activity, search, sourcing discovery, AI web search, organisation endpoints and a "coming soon" custom ingestion API, alongside a legacy Scoring API and a hosted Model Context Protocol (MCP) server for AI agents. MadKudu publishes OpenAPI 3.1.0 for both surfaces, but only as per-operation blocks embedded in its GitBook reference — no spec document is served. MadKudu was acquired by HG Insights in 2025; the docs are now titled "HG Platform API" and API access is contact-sales. Originally backed by Partech and Techstars.
image: https://cdn.prod.website-files.com/6107b1101d4d3e748743f234/65f31ad2b4ac6cf0cb8bd691_og-img.png
layout: provider
mcp_servers:
- description: ''
  name: madkudu-mcp.yml
  slug: madkudu-mcpyml
modified: '2026-08-14'
name: MadKudu
nav: Providers
network: true
overview: 'MadKudu publishes 2 APIs on the [APIs.io](https://apis.io/) network: API (MadAPI) and Legacy Scoring API. Tagged areas include Company, Applicative Saas, Sales Intelligence, Lead Scoring, and Predictive Analytics.


  MadKudu''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 25 more developer resources.'
plans:
- name: Madkudu Plans Pricing
  plan_count: 0
  slug: madkudu-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Madkudu Rate Limits
  slug: madkudu-rate-limits
score:
  band: strong
  composite: 54.9
  delta: -1.5
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 16.7
    contract_quality: 56.6
    developer_ergonomics: 70.8
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 39.5
  previous_composite: 56.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/madkudu/refs/heads/main/screenshots/madkudu-2026-07-25T225833.png
security:
- kind: authentication
  name: Madkudu Authentication
  slug: madkudu-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Madkudu Domain Security
  slug: madkudu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Madkudu Trust Center
  slug: madkudu-trust-center
  summary_line: SOC 2 Type 2, CAIQ, SIG Lite
slug: madkudu
tags:
- Company
- Applicative Saas
- Sales Intelligence
- Lead Scoring
- Predictive Analytics
- Account Intelligence
- Data Enrichment
- MCP
- Agents
- Go To Market
website: https://madkudu.com/
---

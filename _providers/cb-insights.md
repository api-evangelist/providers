---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-08-12'
api_count: 13
apis:
- description: The original CB Insights REST API — 11 documented GET operations over organizations, deals (fundings, investments, portfolio exits), people, business relationships, expert collections and the credit l
  name: CB Insights API v1
  slug: cb-insights-api-v1
- description: 'Hosted, remote Model Context Protocol server at mcp.cbinsights.com, offered as the supported replacement for the deprecated self-hosted cbi-mcp-server reference implementation. Protected by OAuth 2.1 '
  name: CB Insights MCP Server
  slug: cb-insights-mcp-server
- description: The Authorization API from CB Insights — 1 operation(s) for authorization.
  name: CB Insights Authorization API
  slug: cb-insights-authorization-api
- description: This dataset contains information about partnerships, clients/vendors, licensing activity, and CBI-generated insights to predict future M&As and shifts in strategy.
  name: CB Insights Business Relationships API
  slug: cb-insights-businessrelationships-api
- description: The ChatCBI API from CB Insights — 3 operation(s) for chatcbi.
  name: CB Insights Chat CBI API
  slug: cb-insights-chatcbi-api
- description: This dataset contains information about funding deals, cap table history, M&As, IPOs, and CBI-generated insights that extract key themes.
  name: CB Insights Financial Transactions API
  slug: cb-insights-financialtransactions-api
- description: This dataset contains profiles on private companies, public companies, and investors. Includes general information like location, headcount, and industry, as well as proprietary data like business mod
  name: CB Insights Firmographics API
  slug: cb-insights-firmographics-api
- description: This dataset includes leadership teams, board members, and the Management factor of the Mosaic Score — our proprietary algorithm which evaluates leadership teams based on past achievements.
  name: CB Insights Management And Board API
  slug: cb-insights-managementandboard-api
- description: The Organizations API from CB Insights — 1 operation(s) for organizations.
  name: CB Insights Organizations API
  slug: cb-insights-organizations-api
- description: This dataset contains proprietary data science analysis including Mosaic Score, Commercial Maturity, and Exit Probability. Proven to predict winners better than top VCs. More about these proprietary d
  name: CB Insights Outlook API
  slug: cb-insights-outlook-api
- description: The Revenue API from CB Insights — 2 operation(s) for revenue.
  name: CB Insights Revenue API
  slug: cb-insights-revenue-api
- description: A CB Insights scouting report for a private company provides a comprehensive analysis of a business, including its market position, competitive landscape, and growth potential to offer a clear underst
  name: CB Insights Scouting Reports API
  slug: cb-insights-scoutingreports-api
- description: The StrategyMap API from CB Insights — 1 operation(s) for strategymap.
  name: CB Insights Strategy Map API
  slug: cb-insights-strategymap-api
artifact_total: 19
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cbinsights/cbi-mcp-server/issues
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cb-insights-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cbinsights.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.cbinsights.com/portal
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.cbinsights.com/portal/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.cbinsights.com/portal/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.cbinsights.com/portal/docs/quick-start
- group: operate
  title: ''
  type: Support
  url: https://www.cbinsights.com/company/support
- group: company
  title: ''
  type: Blog
  url: https://www.cbinsights.com/research/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cbinsights
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cbinsights.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://api-docs.cbinsights.com/portal/signup
- group: start
  title: ''
  type: Login
  url: https://www.cbinsights.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api-docs.cbinsights.com/portal/api-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cbinsights.com/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: security/cb-insights-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cbinsights.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/cb-insights-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cbinsights.com/security-and-privacy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/cb-insights-api-v2-openapi.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cb-insights-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cb-insights-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cb-insights-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cb-insights-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cb-insights-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cb-insights-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cb-insights-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cb-insights-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cb-insights-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cb-insights-well-known.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cb-insights-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cb-insights-api-v2-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/cb-insights-packages.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cb-insights-vocabulary.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cb-insights-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-09'
description: 'CB Insights (CB Information Services, Inc.) is a New York-based private-market intelligence platform covering 12M+ private and public company profiles, funding deals, cap tables, M&A and IPO exits, business relationships, management and board data, and proprietary predictive scores (Mosaic, Commercial Maturity, Exit Probability, Competitor Score). The company exposes that data programmatically through the CB Insights API v2 — a token-authenticated REST API at api.cbinsights.com documented with a published Swagger 2.0 contract of 28 operations across Firmographics, Financial Transactions, Business Relationships, Management & Board, Outlook, Revenue, Strategy Map, Scouting Reports and the ChatCBI research LLM — plus a maintenance-mode v1 REST API, a hosted OAuth-protected MCP server at mcp.cbinsights.com listed in Claude, ChatGPT, Perplexity and Microsoft Copilot connector directories, a Snowflake Marketplace data share with Semantic Views and a Cortex Knowledge Extension, and
  Salesforce and Microsoft 365 Copilot connectors. Access is credit-metered and credential-gated: clientId/clientSecret are issued by CB Insights, exchanged for a 24-hour bearer token, and every data call debits an account credit ledger.'
image: https://api-docs.cbinsights.com/portal/img/cbinsights-social-card.png
layout: provider
mcp_servers:
- description: ''
  name: cb-insights-mcp.yml
  slug: cb-insights-mcpyml
- description: ''
  name: mcp.cbinsights.com
  slug: mcpcbinsightscom
modified: '2026-08-09'
name: CB Insights
nav: Providers
network: true
overview: 'CB Insights publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Business Relationships API, Chat CBI API, and 8 more. Tagged areas include Company, market-intelligence, private-company-data, venture-capital, and funding-data.


  CB Insights'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
random_paper: 35
rate_limits:
- limit_count: 1
  name: Cb Insights Rate Limits
  slug: cb-insights-rate-limits
score:
  band: developing
  composite: 55.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 53.1
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 31.3
    operational_transparency: 42.1
  previous_composite: 55.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Cb Insights Authentication
  slug: cb-insights-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Cb Insights Domain Security
  slug: cb-insights-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cb Insights Trust Center
  slug: cb-insights-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA, EU AI Act (deployer obligations)
slug: cb-insights
tags:
- Company
- market-intelligence
- private-company-data
- venture-capital
- funding-data
- investor-data
- company-data
- people-data
- business-relationships
- predictive-scoring
- mcp
- agent-native
- data-enrichment
- snowflake
website: https://www.cbinsights.com/
---

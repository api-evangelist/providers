---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The original CB Insights REST API — 11 documented GET operations over organizations, deals (fundings, investments, portfolio exits), people, business relationships, expert collections and the credit l
  name: CB Insights API v1
  slug: cb-insights-api-v1
- description: 'Hosted, remote Model Context Protocol server at mcp.cbinsights.com, offered as the supported replacement for the deprecated self-hosted cbi-mcp-server reference implementation. Protected by OAuth 2.1 '
  name: CB Insights MCP Server
  slug: cb-insights-mcp-server
- baseURL: https://api.cbinsights.com
  baseurl_source: declared
  description: The Authorization API from CB Insights — 1 operation(s) for authorization.
  name: CB Insights Authorization API
  slug: cb-insights-authorization-api
- baseURL: https://api.cbinsights.com
  baseurl_source: declared
  description: This dataset contains information about partnerships, clients/vendors, licensing activity, and CBI-generated insights to predict future M&As and shifts in strategy.
  name: CB Insights Business Relationships API
  slug: cb-insights-businessrelationships-api
- baseURL: https://api.cbinsights.com
  baseurl_source: declared
  description: The ChatCBI API from CB Insights — 3 operation(s) for chatcbi.
  name: CB Insights Chat CBI API
  slug: cb-insights-chatcbi-api
- baseURL: https://api.cbinsights.com
  baseurl_source: declared
  description: This dataset contains profiles on private companies, public companies, and investors. Includes general information like location, headcount, and industry, as well as proprietary data like business mod
  name: CB Insights Firmographics API
  slug: cb-insights-firmographics-api
- baseURL: https://api.cbinsights.com
  baseurl_source: declared
  description: This dataset includes leadership teams, board members, and the Management factor of the Mosaic Score — our proprietary algorithm which evaluates leadership teams based on past achievements.
  name: CB Insights Management And Board API
  slug: cb-insights-managementandboard-api
- baseURL: https://api.cbinsights.com
  baseurl_source: declared
  description: The Organizations API from CB Insights — 1 operation(s) for organizations.
  name: CB Insights Organizations API
  slug: cb-insights-organizations-api
- baseURL: https://api.cbinsights.com
  baseurl_source: declared
  description: This dataset contains proprietary data science analysis including Mosaic Score, Commercial Maturity, and Exit Probability. Proven to predict winners better than top VCs. More about these proprietary d
  name: CB Insights Outlook API
  slug: cb-insights-outlook-api
- baseURL: https://api.cbinsights.com
  baseurl_source: declared
  description: The Revenue API from CB Insights — 2 operation(s) for revenue.
  name: CB Insights Revenue API
  slug: cb-insights-revenue-api
- baseURL: https://api.cbinsights.com
  baseurl_source: declared
  description: A CB Insights scouting report for a private company provides a comprehensive analysis of a business, including its market position, competitive landscape, and growth potential to offer a clear underst
  name: CB Insights Scouting Reports API
  slug: cb-insights-scoutingreports-api
- baseURL: https://api.cbinsights.com
  baseurl_source: declared
  description: The StrategyMap API from CB Insights — 1 operation(s) for strategymap.
  name: CB Insights Strategy Map API
  slug: cb-insights-strategymap-api
- baseURL: https://api.cbinsights.com
  baseurl_source: declared
  description: This dataset contains information about funding deals, cap table history, M&As, IPOs, and CBI-generated insights that extract key themes.
  name: CB Insights Financial Transactions API
  slug: cb-insights-financial-transactions-api
artifact_total: 36
collections:
- collection_type: open
  name: CB Insights Authorization API
  slug: open-cb-insights-authorization-api
- collection_type: open
  name: CB Insights Business Relationships API
  slug: open-cb-insights-businessrelationships-api
- collection_type: open
  name: CB Insights Chat CBI API
  slug: open-cb-insights-chatcbi-api
- collection_type: open
  name: CB Insights Financial Transactions API
  slug: open-cb-insights-financialtransactions-api
- collection_type: open
  name: CB Insights Firmographics API
  slug: open-cb-insights-firmographics-api
- collection_type: open
  name: CB Insights Management And Board API
  slug: open-cb-insights-managementandboard-api
- collection_type: open
  name: CB Insights Organizations API
  slug: open-cb-insights-organizations-api
- collection_type: open
  name: CB Insights Outlook API
  slug: open-cb-insights-outlook-api
- collection_type: open
  name: CB Insights Revenue API
  slug: open-cb-insights-revenue-api
- collection_type: open
  name: CB Insights Scouting Reports API
  slug: open-cb-insights-scoutingreports-api
- collection_type: open
  name: CB Insights Strategy Map API
  slug: open-cb-insights-strategymap-api
common:
- group: other
  href: https://artifacts.apis.io/cb-insights/capabilities/cb-insights-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cb-insights-capability-edges.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cbinsights.com/research/feed/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/cbinsights/cbi-mcp-server/issues
- group: auth
  href: https://artifacts.apis.io/cb-insights/security/cb-insights-domain-security.yml
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
  href: https://artifacts.apis.io/cb-insights/security/cb-insights-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cb-insights-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cbinsights.com/
- group: auth
  href: https://artifacts.apis.io/cb-insights/conformance/cb-insights-conformance.yml
  title: ''
  type: Compliance
  url: conformance/cb-insights-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cbinsights.com/security-and-privacy/
- group: docs
  href: https://artifacts.apis.io/cb-insights/openapi/_original/cb-insights-api-v2-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/cb-insights-api-v2-openapi.json
- group: agent
  href: https://artifacts.apis.io/cb-insights/mcp/cb-insights-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cb-insights-mcp.yml
- group: build
  href: https://artifacts.apis.io/cb-insights/mcp/cb-insights-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cb-insights-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/cb-insights/authentication/cb-insights-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cb-insights-authentication.yml
- group: design
  href: https://artifacts.apis.io/cb-insights/conventions/cb-insights-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cb-insights-conventions.yml
- group: design
  href: https://artifacts.apis.io/cb-insights/errors/cb-insights-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cb-insights-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/cb-insights/rate-limits/cb-insights-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cb-insights-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cb-insights/lifecycle/cb-insights-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cb-insights-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cb-insights/changelog/cb-insights-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cb-insights-changelog.yml
- group: design
  href: https://artifacts.apis.io/cb-insights/conformance/cb-insights-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cb-insights-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cb-insights/well-known/cb-insights-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cb-insights-well-known.yml
- group: design
  href: https://artifacts.apis.io/cb-insights/data-model/cb-insights-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cb-insights-data-model.yml
- group: other
  href: https://artifacts.apis.io/cb-insights/overlays/cb-insights-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cb-insights-api-v2-overlay.yaml
- group: build
  href: https://artifacts.apis.io/cb-insights/packages/cb-insights-packages.yml
  title: ''
  type: Packages
  url: packages/cb-insights-packages.yml
- group: design
  href: https://artifacts.apis.io/cb-insights/vocabulary/cb-insights-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cb-insights-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cb-insights/llms/cb-insights-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cb-insights-llms.txt
- group: agent
  href: https://artifacts.apis.io/cb-insights/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/cb-insights/plans/cb-insights-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cb-insights-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/cb-insights/scopes/cb-insights-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cb-insights-scopes.yml
created: '2026-08-09'
description: 'CB Insights (CB Information Services, Inc.) is a New York-based private-market intelligence platform covering 12M+ private and public company profiles, funding deals, cap tables, M&A and IPO exits, business relationships, management and board data, and proprietary predictive scores (Mosaic, Commercial Maturity, Exit Probability, Competitor Score). The company exposes that data programmatically through the CB Insights API v2 — a token-authenticated REST API at api.cbinsights.com documented with a published Swagger 2.0 contract of 28 operations across Firmographics, Financial Transactions, Business Relationships, Management & Board, Outlook, Revenue, Strategy Map, Scouting Reports and the ChatCBI research LLM — plus a maintenance-mode v1 REST API, a hosted OAuth-protected MCP server at mcp.cbinsights.com listed in Claude, ChatGPT, Perplexity and Microsoft Copilot connector directories, a Snowflake Marketplace data share with Semantic Views and a Cortex Knowledge Extension, and
  Salesforce and Microsoft 365 Copilot connectors. Access is credit-metered and credential-gated: clientId/clientSecret are issued by CB Insights, exchanged for a 24-hour bearer token, and every data call debits an account credit ledger.'
finops:
- has_sources: true
  method: derived
  name: Cb Insights Finops
  primary_unit: ''
  service_category: ''
  slug: cb-insights-finops
  template: true
image: https://api-docs.cbinsights.com/portal/img/cbinsights-social-card.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.cbinsights.com over streamable HTTP.
  name: CB Insights MCP Server
  slug: cb-insights-mcp-server
modified: '2026-10-06'
name: CB Insights
nav: Providers
network: true
overview: 'CB Insights publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authorization API, Business Relationships API, Chat CBI API, and 10 more. Tagged areas include Company, Market Intelligence, private-company-data, Venture Capital, and Funding Data.


  The CB Insights catalog on APIs.io includes 1 Spectral governance ruleset.


  CB Insights'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Cb Insights Plans Pricing
  plan_count: 2
  slug: cb-insights-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Cb Insights Rate Limits
  slug: cb-insights-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: CB Insights API Rules
  rule_count: 61
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 6
  slug: cb-insights-rules
scopes:
- name: Cb Insights Scopes
  scope_count: 3
  slug: cb-insights-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.5
    catalog_earned_first_party: 21.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 81.6
    contract_governance: 47.0
    contract_quality: 55.5
    developer_ergonomics: 58.9
    discoverability: 68.3
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 61.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cb-insights/cb-insights-2026-08-17T080811.png
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
skill_count: 3
skills:
- name: cb-insights-company-outlook
  slug: cb-insights-company-outlook
- name: cb-insights-funding-history
  slug: cb-insights-funding-history
- name: cb-insights-resolve-organizations
  slug: cb-insights-resolve-organizations
slug: cb-insights
tags:
- Company
- Market Intelligence
- private-company-data
- Venture Capital
- Funding Data
- investor-data
- Company Data
- People Data
- BusinessRelationships
- predictive-scoring
- MCP
- Agent-Native
- Data Enrichment
- Snowflake
website: https://www.cbinsights.com/
---

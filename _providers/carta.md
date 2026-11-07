---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
api_count: 6
apis:
- description: Enables incorporation partners and law firms to programmatically onboard new companies onto the Carta platform, streamlining the company formation and cap table initialisation workflow.
  name: Carta Launch API
  slug: launch-api
- description: Permits fund operators to retrieve cap table summaries and portfolio position data for their holdings, enabling downstream analytics, reporting, and portfolio management workflows.
  name: Carta Investor API
  slug: investor-api
- description: Allows law firms and technology partners to retrieve cap table data on behalf of companies, supporting legal workflows, equity issuance, and 409A valuation processes.
  name: Carta Issuer API
  slug: issuer-api
- description: Enables personal finance and wealth management platforms to aggregate equity holdings data for individuals, supporting estate planning, tax preparation, option financing, and underwriting use cases.
  name: Carta Portfolio API
  slug: portfolio-api
- description: Facilitates deal and fundraising relationship management across investment processes for fund operators, providing structured access to CRM data within the Carta platform.
  name: Carta CRM API
  slug: crm-api
- baseURL: https://api.carta.com
  baseurl_source: declared
  description: 'Carta API as documented publicly: 40 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Carta API
  slug: carta-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/carta/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/carta/rules/carta-rules.yml
  title: ''
  type: Spectral
  url: rules/carta-rules.yml
- group: design
  href: https://artifacts.apis.io/carta/json-ld/carta-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carta-context.jsonld
- group: design
  href: https://artifacts.apis.io/carta/vocabulary/carta-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carta-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/carta/data-model/carta-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carta-data-model.yml
- group: design
  href: https://artifacts.apis.io/carta/conventions/carta-conventions.yml
  title: ''
  type: Conventions
  url: conventions/carta-conventions.yml
- group: start
  href: https://artifacts.apis.io/carta/sandbox/carta-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/carta-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.carta.com/
- group: auth
  href: https://artifacts.apis.io/carta/authentication/carta-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carta-authentication.yml
- group: design
  href: https://artifacts.apis.io/carta/errors/carta-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carta-problem-types.yml
- group: design
  href: https://artifacts.apis.io/carta/conformance/carta-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carta-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carta/llms/carta-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carta-llms.txt
- group: build
  href: https://artifacts.apis.io/carta/mcp/carta-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/carta-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/carta/mcp/carta-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carta-mcp.yml
- group: auth
  href: https://artifacts.apis.io/carta/well-known/carta-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/carta-status-security.txt
- group: agent
  href: https://artifacts.apis.io/carta/well-known/carta-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carta-well-known.yml
- group: other
  href: https://artifacts.apis.io/carta/hosts/carta-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carta-hosts.yml
- group: build
  href: https://artifacts.apis.io/carta/integrations/carta-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/carta-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/carta/vendors/carta-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carta-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carta.com/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://carta.com/security/generative-ai-at-carta/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carta.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://carta.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://carta.com/learn/private-funds/management/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.carta.com/api-platform/reference/v-1-alpha-1-draft-issuers-create-draft-issuer
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.carta.com/api-platform/guides/getting-started/quickstart-guide
- group: start
  title: ''
  type: Login
  url: https://login.app.carta.com/credentials/login/
- group: operate
  title: ''
  type: Support
  url: https://docs.carta.com/api-platform/guides/references/faq-and-support
- group: auth
  href: https://artifacts.apis.io/carta/security/carta-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/carta-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/carta/security/carta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carta.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.carta.com/api-platform/guides/getting-started/introduction
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/carta
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carta--
- group: company
  title: ''
  type: Blog
  url: https://carta.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://carta.com/plans/pricing-for-investors/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.carta.com
- group: other
  title: ''
  type: X
  url: https://x.com/cartainc
- group: commercial
  href: https://artifacts.apis.io/carta/plans/carta-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carta-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/carta/rate-limits/carta-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/carta-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/carta/finops/carta-finops.yml
  title: ''
  type: FinOps
  url: finops/carta-finops.yml
created: '2026-06-13'
description: Carta is an equity management platform offering a REST API for cap table management, 409A valuations, fund administration, employee equity plans, and investor portfolio management. Carta's Developer Platform exposes four API suites — Launch, Investor, Issuer, and Portfolio — authenticated via OAuth 2.0 (Authorization Code and Client Credentials flows). Partner access is invite-only and requires SOC 2 Type 2 certification; Carta customers may request access to their own data on demand. A mock API environment at mock-api.carta.com is provided for sandbox development.
finops:
- has_sources: false
  method: generated
  name: Carta Finops
  primary_unit: ''
  service_category: ''
  slug: carta-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carta.png
json_schemas:
- name: GetV1Alpha1IssuersIssueridTransactionsResponse
  property_count: 1
  slug: carta-get-v1-alpha1-issuers-issuerid-transactions-response
- name: PostV1Alpha1InvestorsFirmsFirmidFundsFundidCapitalcallsReque
  property_count: 4
  slug: carta-post-v1-alpha1-investors-firms-firmid-funds-fundid-capitalcalls-reque
- name: PostV1Alpha1InvestorsFirmsFirmidFundsFundidCapitalcallsRespo
  property_count: 2
  slug: carta-post-v1-alpha1-investors-firms-firmid-funds-fundid-capitalcalls-respo
- name: PostV1Alpha1InvestorsFirmsFirmidFundsFundidManagementfeesReq
  property_count: 4
  slug: carta-post-v1-alpha1-investors-firms-firmid-funds-fundid-managementfees-req
- name: PostV1Alpha1InvestorsFirmsFirmidFundsFundidManagementfeesRes
  property_count: 1
  slug: carta-post-v1-alpha1-investors-firms-firmid-funds-fundid-managementfees-res
- name: PostV1Alpha1IssuersIssueridSecuritiesStocksplitchangesRespon
  property_count: 3
  slug: carta-post-v1-alpha1-issuers-issuerid-securities-stocksplitchanges-respon
jsonld:
- class_count: 10
  name: Carta Context
  property_count: 0
  slug: carta-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.app.carta.com over HTTP.
  name: Carta MCP Server
  slug: carta
modified: '2026-06-13'
name: Carta
nav: Providers
network: true
overview: 'Carta is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Equity Management, Cap Table, 409A Valuations, Fund Administration, and Employee Equity.


  The Carta catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Carta''s developer surface includes sandbox, authentication, API reference, getting-started guide, support, documentation, engineering blog, and 34 more developer resources.'
plans:
- name: Carta Plans Pricing
  plan_count: 3
  slug: carta-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Carta Rate Limits
  slug: carta-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Carta API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: carta-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 23.7
    developer_ergonomics: 39.9
    discoverability: 81.7
    operational_transparency: 47.4
  previous_composite: 49.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/carta/carta-2026-06-20T174019.png
security:
- kind: authentication
  name: Carta Authentication
  slug: carta-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Carta Domain Security
  slug: carta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Carta Trust Center
  slug: carta-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 2
skills:
- name: carta-book-capital-call
  slug: carta-book-capital-call
- name: carta-list-fund-investments
  slug: carta-list-fund-investments
slug: carta
tags:
- Equity Management
- Cap Table
- 409A Valuations
- Fund Administration
- Employee Equity
- Investor Portfolio
- Private Markets
- Fintech
- Startups
website: https://carta.com
---

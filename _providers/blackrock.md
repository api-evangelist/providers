---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Blackrock Agentic Access
  operation_count: 13
  slug: blackrock-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 6
apis:
- description: The Aladdin Developer program provides APIs that enable clients to access BlackRock's Aladdin platform capabilities programmatically. Aladdin APIs support portfolio analytics, risk reporting, data acc
  name: BlackRock Aladdin API
  slug: aladdin-api
- baseURL: https://{defaultWebServer}/api/platform/infrastructure/token/v1
  baseurl_source: declared
  description: The AuthorizationUrl:generate API from BlackRock — 1 operation(s) for authorizationurl:generate.
  name: BlackRock Authorization Url:generate API
  slug: blackrock-authorizationurl-generate-api
- baseURL: https://{defaultWebServer}/api/platform/infrastructure/token/v1
  baseurl_source: declared
  description: The StudioNotifications API from BlackRock — 2 operation(s) for studionotifications.
  name: BlackRock Studio Notifications API
  slug: blackrock-studionotifications-api
- baseURL: https://{defaultWebServer}/api/platform/infrastructure/token/v1
  baseurl_source: declared
  description: The StudioNotifications:batchCreate API from BlackRock — 1 operation(s) for studionotifications:batchcreate.
  name: BlackRock Studio Notifications:batch Create API
  slug: blackrock-studionotifications-batchcreate-api
- baseURL: https://{defaultWebServer}/api/platform/infrastructure/token/v1
  baseurl_source: declared
  description: The StudioNotifications:filter API from BlackRock — 1 operation(s) for studionotifications:filter.
  name: BlackRock Studio Notifications:filter API
  slug: blackrock-studionotifications-filter-api
- baseURL: https://{defaultWebServer}/api/platform/infrastructure/token/v1
  baseurl_source: declared
  description: The StudioSubscriptions API from BlackRock — 3 operation(s) for studiosubscriptions.
  name: BlackRock Studio Subscriptions API
  slug: blackrock-studiosubscriptions-api
- baseURL: https://{defaultWebServer}/api/platform/infrastructure/token/v1
  baseurl_source: declared
  description: The StudioSubscriptions:batchCreate API from BlackRock — 1 operation(s) for studiosubscriptions:batchcreate.
  name: BlackRock Studio Subscriptions:batch Create API
  slug: blackrock-studiosubscriptions-batchcreate-api
- baseURL: https://{defaultWebServer}/api/platform/infrastructure/token/v1
  baseurl_source: declared
  description: The StudioSubscriptions:filter API from BlackRock — 1 operation(s) for studiosubscriptions:filter.
  name: BlackRock Studio Subscriptions:filter API
  slug: blackrock-studiosubscriptions-filter-api
- baseURL: https://{defaultWebServer}/api/platform/infrastructure/token/v1
  baseurl_source: declared
  description: The Token:checkTokenExists API from BlackRock — 1 operation(s) for token:checktokenexists.
  name: BlackRock Token:check Token Exists API
  slug: blackrock-token-checktokenexists-api
- baseURL: https://{defaultWebServer}/api/platform/infrastructure/token/v1
  baseurl_source: declared
  description: The Token:generate API from BlackRock — 1 operation(s) for token:generate.
  name: BlackRock Token:generate API
  slug: blackrock-token-generate-api
artifact_total: 42
common:
- group: agent
  href: https://artifacts.apis.io/blackrock/agentic-access/blackrock-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blackrock-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blackrock/rules/blackrock-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/blackrock-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/blackrock/rules/blackrock-rules.yml
  title: ''
  type: Spectral
  url: rules/blackrock-rules.yml
- group: design
  href: https://artifacts.apis.io/blackrock/rules/blackrock-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/blackrock-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/blackrock/data-model/blackrock-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blackrock-data-model.yml
- group: design
  href: https://artifacts.apis.io/blackrock/errors/blackrock-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blackrock-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blackrock/conformance/blackrock-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blackrock-conformance.yml
- group: other
  href: https://artifacts.apis.io/blackrock/hosts/blackrock-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackrock-hosts.yml
- group: build
  href: https://artifacts.apis.io/blackrock/integrations/blackrock-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/blackrock-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/blackrock/vendors/blackrock-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackrock-vendors.yml
- group: build
  href: https://artifacts.apis.io/blackrock/packages/blackrock-packages.yml
  title: ''
  type: Packages
  url: packages/blackrock-packages.yml
- group: auth
  href: https://artifacts.apis.io/blackrock/scopes/blackrock-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/blackrock-scopes.yml
- group: auth
  href: https://artifacts.apis.io/blackrock/authentication/blackrock-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blackrock-authentication.yml
- group: commercial
  href: https://artifacts.apis.io/blackrock/plans/blackrock-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blackrock-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/blackrock/rate-limits/blackrock-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blackrock-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/blackrock/finops/blackrock-finops.yml
  title: ''
  type: FinOps
  url: finops/blackrock-finops.yml
- group: auth
  href: https://artifacts.apis.io/blackrock/security/blackrock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackrock-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blackrock
- group: company
  title: ''
  type: Website
  url: https://www.blackrock.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blackrock
- group: company
  title: ''
  type: Blog
  url: https://www.blackrock.com/us/individual/insights
- group: design
  href: https://artifacts.apis.io/blackrock/rules/blackrock-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/blackrock-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/blackrock/vocabulary/blackrock-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/blackrock-vocabulary.yaml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blackrock.com/corporate/compliance/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blackrock.com/corporate/compliance/privacy-notice
- group: start
  title: ''
  type: Login
  url: https://www.blackrock.com/us/individual/sign-on.oauth?redirectUrl=%2Fus%2Findividual%3FsignInAppWithOkta%3Dtrue
- group: company
  title: ''
  type: Newsroom
  url: https://www.blackrock.com/corporate/newsroom
- group: docs
  title: ''
  type: Documentation
  url: https://www.blackrock.com/aladdin/products/aladdin-studio
created: '2026-03-21'
description: BlackRock is the world's largest asset manager with over $10 trillion in assets under management. Through its Aladdin platform, BlackRock provides institutional investors, wealth managers, and financial services firms with risk analytics, portfolio management, and data capabilities via APIs. The Aladdin platform powers investment operations for many of the world's largest pension funds, insurers, and asset managers.
examples:
- key_count: 9
  name: Blackrock Portfolio Example
  slug: blackrock-portfolio-example
- key_count: 7
  name: Blackrock Risk Report Example
  slug: blackrock-risk-report-example
features:
- description: Multi-asset risk measurement and attribution capabilities accessible via API, including VaR, factor exposures, stress testing, and scenario analysis.
  name: Aladdin Risk Analytics
- description: APIs for portfolio construction, optimization, rebalancing, and compliance monitoring integrated with the Aladdin operating system.
  name: Portfolio Management APIs
- description: Structured access to market data, security reference data, and portfolio data via RESTful APIs with enterprise data governance.
  name: Data Access Layer
- description: APIs for trade order management, execution, and settlement workflows integrating with OMS and EMS systems.
  name: Order Management System Integration
- description: Open-source Python SDK providing programmatic access to Aladdin APIs with authentication, pagination, and data transformation utilities.
  name: AladdinSDK
- description: Event-driven workflow APIs enabling clients to automate investment operations processes and integrate with third-party systems.
  name: Workflow Automation
finops:
- has_sources: true
  method: generated
  name: Blackrock Finops
  primary_unit: ''
  service_category: Asset Management Technology
  slug: blackrock-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blackrock.png
integrations:
- description: Aladdin integrates with Charles River IMS for order management and compliance workflow automation.
  name: Charles River Development
- description: Integration between Aladdin risk analytics and SimCorp's portfolio management and accounting systems.
  name: SimCorp Dimension
- description: Market data and analytics integrations with Bloomberg Data License and Bloomberg PORT for risk and performance.
  name: Bloomberg
- description: Security master data and market data integrations with Refinitiv Datascope and Eikon platforms.
  name: Refinitiv
json_schemas:
- name: BlackRock Aladdin Portfolio
  property_count: 9
  slug: blackrock-portfolio
- name: BlackRock Aladdin Risk Report
  property_count: 7
  slug: blackrock-risk-report
json_structures:
- name: Blackrock Portfolio Structure
  property_count: 0
  slug: blackrock-portfolio-structure
- name: Blackrock Risk Report Structure
  property_count: 0
  slug: blackrock-risk-report-structure
jsonld:
- class_count: 13
  name: Blackrock Context
  property_count: 0
  slug: blackrock-context
layout: provider
modified: '2026-10-20'
name: BlackRock
nav: Providers
network: true
overview: 'BlackRock publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authorization Url:generate API, Studio Notifications API, Studio Notifications:batch Create API, and 7 more. Tagged areas include Asset Management, Finance, Fintech, Investment Management, and Portfolio Management.


  The BlackRock catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  BlackRock''s developer surface includes authentication, engineering blog, documentation, and 25 more developer resources.'
plans:
- name: Blackrock Plans Pricing
  plan_count: 1
  slug: blackrock-plans-pricing
press:
- date: ''
  title: BlackRock, Global Infrastructure Partners, Microsoft and ...
  url: https://news.microsoft.com/source/2024/09/17/blackrock-global-infrastructure-partners-microsoft-and-mgx-launch-new-ai-partnership-to-invest-in-data-centers-and-supporting-power-infrastructure/
- date: ''
  title: Global Infrastructure Partners, BlackRock, Microsoft, and ...
  url: https://www.global-infra.com/news/global-infrastructure-partners-blackrock-microsoft-and-mgx-launch-new-ai-partnership-to-invest-in-data-centers-and-supporting-power-infrastructure/
- date: ''
  title: View all our press releases | iShares - BlackRock
  url: https://www.ishares.com/us/library/press-releases
- date: ''
  title: AI Infrastructure Partnership - BlackRock
  url: https://www.blackrock.com/corporate/newsroom/press-releases/article/corporate-one/press-releases/ai-infrastructure-partnership
- date: ''
  title: Digital disruption and artificial intelligence (AI) - BlackRock
  url: https://www.blackrock.com/corporate/insights/blackrock-investment-institute/publications/mega-forces/artificial-intelligence
random_paper: 4
rate_limits:
- limit_count: 1
  name: Blackrock Rate Limits
  slug: blackrock-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: BlackRock — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: blackrock-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: BlackRock API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: blackrock-rules
- authorship: unmarked
  effective_rule_count: 5
  extends: []
  name: BlackRock API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: blackrock-spectral-rules
scopes:
- name: Blackrock Scopes
  scope_count: 4
  slug: blackrock-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 65.0
    catalog_earned_first_party: 0.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 31.8
    contract_quality: 59.0
    developer_ergonomics: 31.0
    discoverability: 64.3
    operational_transparency: 10.5
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blackrock Authentication
  slug: blackrock-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Blackrock Domain Security
  slug: blackrock-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blackrock
tags:
- Asset Management
- Finance
- Fintech
- Investment Management
- Portfolio Management
- Risk Analytics
- Fortune 500
use_cases:
- description: Institutional investors use Aladdin APIs to generate regulatory risk reports, UCITS compliance reports, and investor disclosures.
  name: Institutional Risk Reporting
- description: Wealth managers and RIAs integrate Aladdin risk analytics into their own client-facing and advisor-facing platforms.
  name: Portfolio Analytics Integration
- description: FinTech companies access structured investment data through Aladdin APIs to power analytics, research, and advisory products.
  name: Fintech Data Integration
- description: Portfolio managers automate rebalancing workflows using Aladdin APIs to trigger trades based on drift thresholds and target allocations.
  name: Automated Rebalancing
- description: Family offices and fund-of-funds use Aladdin APIs to aggregate portfolio data across multiple managers into a single risk view.
  name: Multi-Manager Aggregation
website: https://www.blackrock.com
---

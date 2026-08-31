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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Aladdin Developer program provides APIs that enable clients to access BlackRock's Aladdin platform capabilities programmatically. Aladdin APIs support portfolio analytics, risk reporting, data acc
  name: BlackRock Aladdin API
  slug: aladdin-api
artifact_total: 29
common:
- group: auth
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
- group: docs
  title: ''
  type: Documentation
  url: https://www.blackrock.com/aladdin/products/aladdin-developer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blackrock
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blackrock.com/us/individual/regulatory/privacy-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blackrock.com/us/individual/regulatory/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.blackrock.com/us/individual/insights
- group: design
  title: ''
  type: SpectralRules
  url: rules/blackrock-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/blackrock-vocabulary.yaml
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
- name: Blackrock Finops
  service_category: Asset Management Technology
  slug: blackrock-finops
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
modified: '2026-04-21'
name: BlackRock
nav: Providers
network: true
overview: 'BlackRock publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Asset Management, Finance, Fintech, Investment Management, and Portfolio-Management.


  The BlackRock catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BlackRock''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Blackrock Plans Pricing
  plan_count: 1
  slug: blackrock-plans-pricing
press:
- date: '2026-05-25'
  title: BlackRock, Global Infrastructure Partners, Microsoft and ...
  url: https://news.microsoft.com/source/2024/09/17/blackrock-global-infrastructure-partners-microsoft-and-mgx-launch-new-ai-partnership-to-invest-in-data-centers-and-supporting-power-infrastructure/
- date: '2026-05-25'
  title: Global Infrastructure Partners, BlackRock, Microsoft, and ...
  url: https://www.global-infra.com/news/global-infrastructure-partners-blackrock-microsoft-and-mgx-launch-new-ai-partnership-to-invest-in-data-centers-and-supporting-power-infrastructure/
- date: '2026-05-25'
  title: View all our press releases | iShares - BlackRock
  url: https://www.ishares.com/us/library/press-releases
- date: '2026-05-25'
  title: AI Infrastructure Partnership - BlackRock
  url: https://www.blackrock.com/corporate/newsroom/press-releases/article/corporate-one/press-releases/ai-infrastructure-partnership
- date: '2026-05-25'
  title: Digital disruption and artificial intelligence (AI) - BlackRock
  url: https://www.blackrock.com/corporate/insights/blackrock-investment-institute/publications/mega-forces/artificial-intelligence
random_paper: 16
rate_limits:
- limit_count: 1
  name: Blackrock Rate Limits
  slug: blackrock-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: BlackRock API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: blackrock-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: BlackRock API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: blackrock-spectral-rules
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 14
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 25.0
    contract_quality: 30.7
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 22.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
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
- Portfolio-Management
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

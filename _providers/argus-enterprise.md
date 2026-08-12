---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Argus Enterprise Agentic Access
  operation_count: 43
  slug: argus-enterprise-agentic-access
  summary_line: 43 operations · 21 acting
api_count: 12
apis:
- description: OAuth 2.0 token operations for API access
  name: ARGUS Enterprise Authentication API
  slug: argus-enterprise-authentication-api
- description: Cash flow projections and analysis
  name: ARGUS Enterprise Cash Flows API
  slug: argus-enterprise-cash-flows-api
- description: View webhook event history and delivery logs
  name: ARGUS Enterprise Events API
  slug: argus-enterprise-events-api
- description: Webhook service health and status
  name: ARGUS Enterprise Health API
  slug: argus-enterprise-health-api
- description: Lease agreements and terms
  name: ARGUS Enterprise Leases API
  slug: argus-enterprise-leases-api
- description: Organize and manage property portfolios
  name: ARGUS Enterprise Portfolios API
  slug: argus-enterprise-portfolios-api
- description: Manage commercial real estate properties and assets
  name: ARGUS Enterprise Properties API
  slug: argus-enterprise-properties-api
- description: Generate and retrieve analytical reports
  name: ARGUS Enterprise Reports API
  slug: argus-enterprise-reports-api
- description: Manage webhook subscriptions
  name: ARGUS Enterprise Subscriptions API
  slug: argus-enterprise-subscriptions-api
- description: Tenant records and contact information
  name: ARGUS Enterprise Tenants API
  slug: argus-enterprise-tenants-api
- description: User management and access control
  name: ARGUS Enterprise Users API
  slug: argus-enterprise-users-api
- description: Property valuations and appraisal data
  name: ARGUS Enterprise Valuations API
  slug: argus-enterprise-valuations-api
artifact_total: 165
collections:
- collection_type: postman
  name: Argus Enterprise Core Authentication API
  slug: postman-argus-enterprise-authentication-api
- collection_type: postman
  name: Argus Enterprise Core Authentication Cash Flows API
  slug: postman-argus-enterprise-cash-flows-api
- collection_type: postman
  name: Argus Enterprise Core Authentication Events API
  slug: postman-argus-enterprise-events-api
- collection_type: postman
  name: Argus Enterprise Core Authentication Health API
  slug: postman-argus-enterprise-health-api
- collection_type: postman
  name: Argus Enterprise Core Authentication Leases API
  slug: postman-argus-enterprise-leases-api
- collection_type: postman
  name: Argus Enterprise Core Authentication Portfolios API
  slug: postman-argus-enterprise-portfolios-api
- collection_type: postman
  name: Argus Enterprise Core Authentication Properties API
  slug: postman-argus-enterprise-properties-api
- collection_type: postman
  name: Argus Enterprise Core Authentication Reports API
  slug: postman-argus-enterprise-reports-api
- collection_type: postman
  name: Argus Enterprise Core Authentication Subscriptions API
  slug: postman-argus-enterprise-subscriptions-api
- collection_type: postman
  name: Argus Enterprise Core Authentication Tenants API
  slug: postman-argus-enterprise-tenants-api
- collection_type: postman
  name: Argus Enterprise Core Authentication Users API
  slug: postman-argus-enterprise-users-api
- collection_type: postman
  name: Argus Enterprise Core Authentication Valuations API
  slug: postman-argus-enterprise-valuations-api
- collection_type: open
  name: Argus Enterprise Core API
  slug: open-argus-enterprise-core
- collection_type: open
  name: Argus Enterprise Webhook API
  slug: open-argus-enterprise-webhooks
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/argus-enterprise/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/argus-enterprise-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/argus-enterprise-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/argus-enterprise-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.altusgroup.com/solutions/argus-enterprise/
- group: docs
  title: ''
  type: Documentation
  url: https://www.altusgroup.com/argus/downloads/argus-enterprise/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.altusgroup.com/support/start-using-argus-intelligence/
- group: start
  title: ''
  type: Portal
  url: https://cloud.altusplatform.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.altusgroup.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.altusgroup.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altusgroup.com/privacy-policy/
- group: learn
  title: ''
  type: Training
  url: https://www.altusgroup.com/argus/training/
- group: auth
  title: ''
  type: Security
  url: https://www.altusgroup.com/security/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/argus-enterprise-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/argus-enterprise-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/argus-enterprise-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.altusgroup.com/insights/
created: '2024-01-15'
description: ARGUS Enterprise is the industry-standard commercial property valuation and cash flow forecasting software by Altus Group, now integrated into the ARGUS Intelligence Platform. It provides lease-by-lease cash flow modeling, property valuations using DCF and yield-based methods, budgeting and forecasting, scenario testing, and 40+ industry-standard reports. Trusted by real estate investors, portfolio managers, valuation professionals, and asset managers worldwide and taught at 200+ universities.
examples:
- key_count: 5
  name: Argus Enterprise Address Example
  slug: argus-enterprise-address-example
- key_count: 15
  name: Argus Enterprise Cash Flow Period Example
  slug: argus-enterprise-cash-flow-period-example
- key_count: 7
  name: Argus Enterprise Cash Flow Projection Example
  slug: argus-enterprise-cash-flow-projection-example
- key_count: 7
  name: Argus Enterprise Cash Flow Summary Example
  slug: argus-enterprise-cash-flow-summary-example
- key_count: 6
  name: Argus Enterprise Delivery Attempt Example
  slug: argus-enterprise-delivery-attempt-example
- key_count: 7
  name: Argus Enterprise Event Example
  slug: argus-enterprise-event-example
- key_count: 2
  name: Argus Enterprise Event List Example
  slug: argus-enterprise-event-list-example
- key_count: 5
  name: Argus Enterprise Health Status Example
  slug: argus-enterprise-health-status-example
- key_count: 21
  name: Argus Enterprise Lease Example
  slug: argus-enterprise-lease-example
- key_count: 14
  name: Argus Enterprise Lease Input Example
  slug: argus-enterprise-lease-input-example
- key_count: 2
  name: Argus Enterprise Lease List Example
  slug: argus-enterprise-lease-list-example
- key_count: 5
  name: Argus Enterprise Lease Option Example
  slug: argus-enterprise-lease-option-example
- key_count: 4
  name: Argus Enterprise Pagination Example
  slug: argus-enterprise-pagination-example
- key_count: 9
  name: Argus Enterprise Portfolio Example
  slug: argus-enterprise-portfolio-example
- key_count: 4
  name: Argus Enterprise Portfolio Input Example
  slug: argus-enterprise-portfolio-input-example
- key_count: 2
  name: Argus Enterprise Portfolio List Example
  slug: argus-enterprise-portfolio-list-example
- key_count: 16
  name: Argus Enterprise Property Example
  slug: argus-enterprise-property-example
- key_count: 11
  name: Argus Enterprise Property Input Example
  slug: argus-enterprise-property-input-example
- key_count: 2
  name: Argus Enterprise Property List Example
  slug: argus-enterprise-property-list-example
- key_count: 8
  name: Argus Enterprise Report Example
  slug: argus-enterprise-report-example
- key_count: 2
  name: Argus Enterprise Report List Example
  slug: argus-enterprise-report-list-example
- key_count: 7
  name: Argus Enterprise Report Request Example
  slug: argus-enterprise-report-request-example
- key_count: 3
  name: Argus Enterprise Retry Policy Example
  slug: argus-enterprise-retry-policy-example
- key_count: 9
  name: Argus Enterprise Subscription Example
  slug: argus-enterprise-subscription-example
- key_count: 4
  name: Argus Enterprise Subscription Input Example
  slug: argus-enterprise-subscription-input-example
- key_count: 1
  name: Argus Enterprise Subscription List Example
  slug: argus-enterprise-subscription-list-example
- key_count: 12
  name: Argus Enterprise Tenant Example
  slug: argus-enterprise-tenant-example
- key_count: 7
  name: Argus Enterprise Tenant Input Example
  slug: argus-enterprise-tenant-input-example
- key_count: 2
  name: Argus Enterprise Tenant List Example
  slug: argus-enterprise-tenant-list-example
- key_count: 4
  name: Argus Enterprise Test Result Example
  slug: argus-enterprise-test-result-example
- key_count: 4
  name: Argus Enterprise Token Response Example
  slug: argus-enterprise-token-response-example
- key_count: 9
  name: Argus Enterprise User Example
  slug: argus-enterprise-user-example
- key_count: 2
  name: Argus Enterprise User List Example
  slug: argus-enterprise-user-list-example
- key_count: 18
  name: Argus Enterprise Valuation Example
  slug: argus-enterprise-valuation-example
- key_count: 11
  name: Argus Enterprise Valuation Input Example
  slug: argus-enterprise-valuation-input-example
- key_count: 2
  name: Argus Enterprise Valuation List Example
  slug: argus-enterprise-valuation-list-example
features:
- description: Model cash flows at the individual lease level across all property types including office, industrial, retail, and multifamily.
  name: Lease-by-Lease Cash Flow Modeling
- description: Support for DCF, cap rate, hardcore, term and reversion, and initial yield valuation methodologies.
  name: Multiple Valuation Methods
- description: Create property-level budgets with budget-to-actual tracking and prior-year comparison.
  name: Budgeting and Forecasting
- description: Run what-if scenarios to assess best-case and worst-case outcomes for investment decisions.
  name: Scenario Analysis
- description: Stress-test yield rates, growth assumptions, and modeling parameters.
  name: Sensitivity Analysis
- description: 40+ industry-standard asset and portfolio reports for investor and management communication.
  name: Portfolio Reporting
- description: Configure market leasing assumptions for new, vacant, and renewing spaces.
  name: Market Leasing Assumptions
- description: Model leveraged and unleveraged returns with debt tranche configuration.
  name: Debt Modeling
- description: ARGUS Enterprise is ISO/IEC 27001:2022 certified and SOC 2 Type II audited.
  name: ISO 27001 Certified
- description: Integrated with ARGUS Intelligence Platform for portfolio-level dashboards and benchmarking.
  name: ARGUS Intelligence Integration
finops:
- name: Argus Enterprise Finops
  service_category: API
  slug: argus-enterprise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/argus-enterprise.png
integrations:
- description: Native integration with ARGUS Intelligence for portfolio dashboards, analytics, and benchmarking.
  name: ARGUS Intelligence Platform
- description: Integration with ARGUS Developer for development-to-stabilization lifecycle management.
  name: ARGUS Developer
- description: Import property management and lease data from Yardi into ARGUS Enterprise models.
  name: Yardi
- description: Integrate MRI property management data into cash flow models.
  name: MRI Software
- description: JLL uses ARGUS Enterprise for asset management and portfolio analytics globally.
  name: JLL
- description: CBRE uses ARGUS Enterprise for valuation and investment analysis services.
  name: CBRE
json_schemas:
- name: Address
  property_count: 5
  slug: argus-enterprise-address
- name: CashFlowPeriod
  property_count: 15
  slug: argus-enterprise-cash-flow-period
- name: CashFlowProjection
  property_count: 7
  slug: argus-enterprise-cash-flow-projection
- name: CashFlowSummary
  property_count: 7
  slug: argus-enterprise-cash-flow-summary
- name: DeliveryAttempt
  property_count: 6
  slug: argus-enterprise-delivery-attempt
- name: EventList
  property_count: 2
  slug: argus-enterprise-event-list
- name: Event
  property_count: 7
  slug: argus-enterprise-event
- name: HealthStatus
  property_count: 5
  slug: argus-enterprise-health-status
- name: LeaseInput
  property_count: 14
  slug: argus-enterprise-lease-input
- name: LeaseList
  property_count: 2
  slug: argus-enterprise-lease-list
- name: LeaseOption
  property_count: 5
  slug: argus-enterprise-lease-option
- name: Argus Enterprise Lease
  property_count: 21
  slug: argus-enterprise-lease
- name: Pagination
  property_count: 4
  slug: argus-enterprise-pagination
- name: PortfolioInput
  property_count: 4
  slug: argus-enterprise-portfolio-input
- name: PortfolioList
  property_count: 2
  slug: argus-enterprise-portfolio-list
- name: Argus Enterprise Portfolio
  property_count: 9
  slug: argus-enterprise-portfolio
- name: PropertyInput
  property_count: 11
  slug: argus-enterprise-property-input
- name: PropertyList
  property_count: 2
  slug: argus-enterprise-property-list
- name: Argus Enterprise Property
  property_count: 16
  slug: argus-enterprise-property
- name: ReportList
  property_count: 2
  slug: argus-enterprise-report-list
- name: ReportRequest
  property_count: 7
  slug: argus-enterprise-report-request
- name: Report
  property_count: 8
  slug: argus-enterprise-report
- name: RetryPolicy
  property_count: 3
  slug: argus-enterprise-retry-policy
- name: SubscriptionInput
  property_count: 4
  slug: argus-enterprise-subscription-input
- name: SubscriptionList
  property_count: 1
  slug: argus-enterprise-subscription-list
- name: Subscription
  property_count: 9
  slug: argus-enterprise-subscription
- name: TenantInput
  property_count: 7
  slug: argus-enterprise-tenant-input
- name: TenantList
  property_count: 2
  slug: argus-enterprise-tenant-list
- name: Tenant
  property_count: 12
  slug: argus-enterprise-tenant
- name: TestResult
  property_count: 4
  slug: argus-enterprise-test-result
- name: TokenResponse
  property_count: 4
  slug: argus-enterprise-token-response
- name: UserList
  property_count: 2
  slug: argus-enterprise-user-list
- name: User
  property_count: 9
  slug: argus-enterprise-user
- name: ValuationInput
  property_count: 11
  slug: argus-enterprise-valuation-input
- name: ValuationList
  property_count: 2
  slug: argus-enterprise-valuation-list
- name: Argus Enterprise Valuation
  property_count: 18
  slug: argus-enterprise-valuation
json_structures:
- name: Argus Enterprise Address Structure
  property_count: 5
  slug: argus-enterprise-address-structure
- name: Argus Enterprise Cash Flow Period Structure
  property_count: 15
  slug: argus-enterprise-cash-flow-period-structure
- name: Argus Enterprise Cash Flow Projection Structure
  property_count: 7
  slug: argus-enterprise-cash-flow-projection-structure
- name: Argus Enterprise Cash Flow Summary Structure
  property_count: 7
  slug: argus-enterprise-cash-flow-summary-structure
- name: Argus Enterprise Delivery Attempt Structure
  property_count: 6
  slug: argus-enterprise-delivery-attempt-structure
- name: Argus Enterprise Event List Structure
  property_count: 2
  slug: argus-enterprise-event-list-structure
- name: Argus Enterprise Event Structure
  property_count: 7
  slug: argus-enterprise-event-structure
- name: Argus Enterprise Health Status Structure
  property_count: 5
  slug: argus-enterprise-health-status-structure
- name: Argus Enterprise Lease Input Structure
  property_count: 14
  slug: argus-enterprise-lease-input-structure
- name: Argus Enterprise Lease List Structure
  property_count: 2
  slug: argus-enterprise-lease-list-structure
- name: Argus Enterprise Lease Option Structure
  property_count: 5
  slug: argus-enterprise-lease-option-structure
- name: Argus Enterprise Lease Structure
  property_count: 21
  slug: argus-enterprise-lease-structure
- name: Argus Enterprise Pagination Structure
  property_count: 4
  slug: argus-enterprise-pagination-structure
- name: Argus Enterprise Portfolio Input Structure
  property_count: 4
  slug: argus-enterprise-portfolio-input-structure
- name: Argus Enterprise Portfolio List Structure
  property_count: 2
  slug: argus-enterprise-portfolio-list-structure
- name: Argus Enterprise Portfolio Structure
  property_count: 9
  slug: argus-enterprise-portfolio-structure
- name: Argus Enterprise Property Input Structure
  property_count: 11
  slug: argus-enterprise-property-input-structure
- name: Argus Enterprise Property List Structure
  property_count: 2
  slug: argus-enterprise-property-list-structure
- name: Argus Enterprise Property Structure
  property_count: 16
  slug: argus-enterprise-property-structure
- name: Argus Enterprise Report List Structure
  property_count: 2
  slug: argus-enterprise-report-list-structure
- name: Argus Enterprise Report Request Structure
  property_count: 7
  slug: argus-enterprise-report-request-structure
- name: Argus Enterprise Report Structure
  property_count: 8
  slug: argus-enterprise-report-structure
- name: Argus Enterprise Retry Policy Structure
  property_count: 3
  slug: argus-enterprise-retry-policy-structure
- name: Argus Enterprise Subscription Input Structure
  property_count: 4
  slug: argus-enterprise-subscription-input-structure
- name: Argus Enterprise Subscription List Structure
  property_count: 1
  slug: argus-enterprise-subscription-list-structure
- name: Argus Enterprise Subscription Structure
  property_count: 9
  slug: argus-enterprise-subscription-structure
- name: Argus Enterprise Tenant Input Structure
  property_count: 7
  slug: argus-enterprise-tenant-input-structure
- name: Argus Enterprise Tenant List Structure
  property_count: 2
  slug: argus-enterprise-tenant-list-structure
- name: Argus Enterprise Tenant Structure
  property_count: 12
  slug: argus-enterprise-tenant-structure
- name: Argus Enterprise Test Result Structure
  property_count: 4
  slug: argus-enterprise-test-result-structure
- name: Argus Enterprise Token Response Structure
  property_count: 4
  slug: argus-enterprise-token-response-structure
- name: Argus Enterprise User List Structure
  property_count: 2
  slug: argus-enterprise-user-list-structure
- name: Argus Enterprise User Structure
  property_count: 9
  slug: argus-enterprise-user-structure
- name: Argus Enterprise Valuation Input Structure
  property_count: 11
  slug: argus-enterprise-valuation-input-structure
- name: Argus Enterprise Valuation List Structure
  property_count: 2
  slug: argus-enterprise-valuation-list-structure
- name: Argus Enterprise Valuation Structure
  property_count: 18
  slug: argus-enterprise-valuation-structure
jsonld:
- class_count: 0
  name: Argus Enterprise Context
  property_count: 8
  slug: argus-enterprise-context
layout: provider
modified: '2026-05-19'
name: ARGUS Enterprise
nav: Providers
network: true
overview: 'ARGUS Enterprise publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Cash Flows API, Events API, and 9 more. Tagged areas include Altus Group, Asset Management, Cash Flow Modeling, Commercial Real Estate, and Portfolio Management.


  The ARGUS Enterprise catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ARGUS Enterprise''s developer surface includes authentication, documentation, getting-started guide, developer portal, support, training material, engineering blog, and 10 more developer resources.'
plans:
- name: Argus Enterprise Plans Pricing
  plan_count: 3
  slug: argus-enterprise-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 5
  name: Argus Enterprise Rate Limits
  slug: argus-enterprise-rate-limits
rules:
- name: ARGUS Enterprise API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: argus-enterprise-jsonschema-spectral-rules
- name: ARGUS Enterprise API Rules
  rule_count: 23
  severity_counts:
    error: 6
    hint: 0
    info: 4
    warn: 13
  slug: argus-enterprise-spectral-rules
score:
  band: developing
  composite: 52.0
  delta: -8.4
  facets:
    commercial_clarity: 36.8
    contract_quality: 66.2
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 18.4
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/argus-enterprise/refs/heads/main/screenshots/argus-enterprise-2026-06-20T172428.png
security:
- kind: authentication
  name: Argus Enterprise Authentication
  slug: argus-enterprise-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Argus Enterprise Domain Security
  slug: argus-enterprise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: argus-enterprise
tags:
- Altus Group
- Asset Management
- Cash Flow Modeling
- Commercial Real Estate
- Portfolio Management
- Valuation
use_cases:
- description: Produce DCF and yield-based valuations for commercial real estate appraisals and acquisitions.
  name: Asset Valuation
- description: Monitor portfolio-level performance against budgets and prior periods with dashboards.
  name: Portfolio Performance Monitoring
- description: Underwrite new property acquisitions with detailed cash flow and return analysis.
  name: Acquisition Underwriting
- description: Create and track property-level budgets against actual performance for active assets.
  name: Asset Management Budgeting
- description: Generate standardized reports for investors, lenders, and boards on asset and portfolio performance.
  name: Investor Reporting
- description: Model disposition scenarios and exit valuations for hold/sell decisions.
  name: Disposition Analysis
website: https://www.altusgroup.com/solutions/argus-enterprise/
---

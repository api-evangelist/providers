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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Allianz Trade Online Agentic Access
  operation_count: 17
  slug: allianz-trade-online-agentic-access
  summary_line: 17 operations · 4 acting
api_count: 4
apis:
- description: Insurance claim management operations
  name: Allianz Trade Claims API
  slug: allianz-trade-online-claims-api
- description: Company creditworthiness grading operations
  name: Allianz Trade Company Grade API
  slug: allianz-trade-online-company-grade-api
- description: Payment overdue reporting and management operations
  name: Allianz Trade Payment Overdues API
  slug: allianz-trade-online-payment-overdues-api
- description: Trade credit insurance policy management operations
  name: Allianz Trade Policy API
  slug: allianz-trade-online-policy-api
artifact_total: 97
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/allianz-trade-online-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allianz-trade-online-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/allianz-trade-online-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allianz-trade-online-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.allianz-trade.com/
- group: start
  title: ''
  type: Portal
  url: https://developers.allianz-trade.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.allianz-trade.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.allianz-trade.com/docs/api-design-guidelines
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.allianz-trade.com/whatsnew
- group: operate
  title: ''
  type: Support
  url: mailto:api@allianz-trade.com
- group: design
  title: ''
  type: SpectralRules
  url: rules/allianz-trade-online-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/allianz-trade-online-vocabulary.yaml
- group: build
  title: ''
  type: Packages
  url: packages/allianz-trade-online-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allianz-trade-online-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/allianz-trade-online-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allianz-trade-online-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/allianz-trade-online-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/allianz-trade-online-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/allianz-trade-online-lifecycle.yml
created: '2024-01-01'
description: 'Allianz Trade APIs enable businesses to automate trade credit insurance management including cover requests, credit limit monitoring, payment overdue reporting, claims management, and company credit grading. Built on secure REST architecture with OAuth2, the APIs support three business lines: Trade Credit Insurance, E-Commerce B2B, and Surety/Guarantee.'
examples:
- key_count: 13
  name: Trade Claims Claim Example
  slug: trade-claims-claim-example
- key_count: 1
  name: Trade Claims Claim_List Example
  slug: trade-claims-claim_list-example
- key_count: 3
  name: Trade Claims Error_Response Example
  slug: trade-claims-error_response-example
- key_count: 5
  name: Trade Claims Job_Response Example
  slug: trade-claims-job_response-example
- key_count: 8
  name: Trade Claims Submit_Claim_Request Example
  slug: trade-claims-submit_claim_request-example
- key_count: 12
  name: Trade Company Grade Company_Grade Example
  slug: trade-company-grade-company_grade-example
- key_count: 1
  name: Trade Company Grade Company_Grade_List Example
  slug: trade-company-grade-company_grade_list-example
- key_count: 6
  name: Trade Company Grade Company_Grade_Request Example
  slug: trade-company-grade-company_grade_request-example
- key_count: 3
  name: Trade Company Grade Error_Response Example
  slug: trade-company-grade-error_response-example
- key_count: 5
  name: Trade Company Grade Job_Response Example
  slug: trade-company-grade-job_response-example
- key_count: 3
  name: Trade Payment Overdues Error_Response Example
  slug: trade-payment-overdues-error_response-example
- key_count: 5
  name: Trade Payment Overdues Job_Response Example
  slug: trade-payment-overdues-job_response-example
- key_count: 11
  name: Trade Payment Overdues Overdue Example
  slug: trade-payment-overdues-overdue-example
- key_count: 1
  name: Trade Payment Overdues Overdue_List Example
  slug: trade-payment-overdues-overdue_list-example
- key_count: 8
  name: Trade Payment Overdues Report_Overdue_Request Example
  slug: trade-payment-overdues-report_overdue_request-example
- key_count: 3
  name: Trade Policy Add_Joint_Insured_Request Example
  slug: trade-policy-add_joint_insured_request-example
- key_count: 3
  name: Trade Policy Error_Response Example
  slug: trade-policy-error_response-example
- key_count: 5
  name: Trade Policy Job_Response Example
  slug: trade-policy-job_response-example
- key_count: 6
  name: Trade Policy Joint_Insured Example
  slug: trade-policy-joint_insured-example
- key_count: 1
  name: Trade Policy Joint_Insured_List Example
  slug: trade-policy-joint_insured_list-example
- key_count: 12
  name: Trade Policy Policy Example
  slug: trade-policy-policy-example
- key_count: 1
  name: Trade Policy Policy_List Example
  slug: trade-policy-policy_list-example
features:
- description: Automate credit limit and cover information importing from Allianz Trade into ERP systems for real-time credit risk management.
  name: Credit Limit Management
- description: Retrieve creditworthiness grades for clients and prospects with bulk operations supporting large portfolio risk assessments.
  name: Company Credit Grading
- description: Report payment defaults, request extension periods, and manage debt rescheduling through standardized overdue category codes.
  name: Payment Overdue Reporting
- description: Integrate claims declaration and tracking directly into ERP systems for streamlined insurance claim management.
  name: Claims Management
- description: Manage trade credit insurance policy portfolios including joint insured policies and policy configuration from enterprise systems.
  name: Policy Portfolio Management
- description: Real-time credit evaluation on a per-transaction basis for B2B e-commerce platforms enabling buy-now-pay-later type scenarios.
  name: E-Commerce B2B Credit
- description: Secure OAuth2 authentication for all API endpoints with client credentials flow for machine-to-machine ERP integrations.
  name: OAuth2 Security
- description: Webhook-based notifications for technical events (job completion) and functional events (business decisions) with HTTPS and IP whitelisting.
  name: Webhook Notifications
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allianz-trade-online.png
integrations:
- description: ERP integration with SAP for automated trade credit management, policy data synchronization, and claims processing.
  name: SAP
- description: Oracle ERP integration for credit limit monitoring and automated policy data synchronization.
  name: Oracle
- description: OpenAPI collections downloadable from the developer portal for Postman, Insomnia, and HTTPie testing.
  name: Postman
- description: CRM integration for combining Allianz Trade risk data with customer relationship management workflows.
  name: Salesforce
json_schemas:
- name: Claim
  property_count: 13
  slug: trade-claims-claim
- name: ClaimList
  property_count: 1
  slug: trade-claims-claim_list
- name: ErrorResponse
  property_count: 3
  slug: trade-claims-error_response
- name: JobResponse
  property_count: 5
  slug: trade-claims-job_response
- name: SubmitClaimRequest
  property_count: 8
  slug: trade-claims-submit_claim_request
- name: CompanyGrade
  property_count: 12
  slug: trade-company-grade-company_grade
- name: CompanyGradeList
  property_count: 1
  slug: trade-company-grade-company_grade_list
- name: CompanyGradeRequest
  property_count: 6
  slug: trade-company-grade-company_grade_request
- name: ErrorResponse
  property_count: 3
  slug: trade-company-grade-error_response
- name: JobResponse
  property_count: 5
  slug: trade-company-grade-job_response
- name: ErrorResponse
  property_count: 3
  slug: trade-payment-overdues-error_response
- name: JobResponse
  property_count: 5
  slug: trade-payment-overdues-job_response
- name: Overdue
  property_count: 11
  slug: trade-payment-overdues-overdue
- name: OverdueList
  property_count: 1
  slug: trade-payment-overdues-overdue_list
- name: ReportOverdueRequest
  property_count: 8
  slug: trade-payment-overdues-report_overdue_request
- name: AddJointInsuredRequest
  property_count: 3
  slug: trade-policy-add_joint_insured_request
- name: ErrorResponse
  property_count: 3
  slug: trade-policy-error_response
- name: JobResponse
  property_count: 5
  slug: trade-policy-job_response
- name: JointInsured
  property_count: 6
  slug: trade-policy-joint_insured
- name: JointInsuredList
  property_count: 1
  slug: trade-policy-joint_insured_list
- name: Policy
  property_count: 12
  slug: trade-policy-policy
- name: PolicyList
  property_count: 1
  slug: trade-policy-policy_list
json_structures:
- name: Trade Claims Claim Structure
  property_count: 13
  slug: trade-claims-claim-structure
- name: Trade Claims Claim_List Structure
  property_count: 1
  slug: trade-claims-claim_list-structure
- name: Trade Claims Error_Response Structure
  property_count: 3
  slug: trade-claims-error_response-structure
- name: Trade Claims Job_Response Structure
  property_count: 5
  slug: trade-claims-job_response-structure
- name: Trade Claims Submit_Claim_Request Structure
  property_count: 8
  slug: trade-claims-submit_claim_request-structure
- name: Trade Company Grade Company_Grade Structure
  property_count: 12
  slug: trade-company-grade-company_grade-structure
- name: Trade Company Grade Company_Grade_List Structure
  property_count: 1
  slug: trade-company-grade-company_grade_list-structure
- name: Trade Company Grade Company_Grade_Request Structure
  property_count: 6
  slug: trade-company-grade-company_grade_request-structure
- name: Trade Company Grade Error_Response Structure
  property_count: 3
  slug: trade-company-grade-error_response-structure
- name: Trade Company Grade Job_Response Structure
  property_count: 5
  slug: trade-company-grade-job_response-structure
- name: Trade Payment Overdues Error_Response Structure
  property_count: 3
  slug: trade-payment-overdues-error_response-structure
- name: Trade Payment Overdues Job_Response Structure
  property_count: 5
  slug: trade-payment-overdues-job_response-structure
- name: Trade Payment Overdues Overdue Structure
  property_count: 11
  slug: trade-payment-overdues-overdue-structure
- name: Trade Payment Overdues Overdue_List Structure
  property_count: 1
  slug: trade-payment-overdues-overdue_list-structure
- name: Trade Payment Overdues Report_Overdue_Request Structure
  property_count: 8
  slug: trade-payment-overdues-report_overdue_request-structure
- name: Trade Policy Add_Joint_Insured_Request Structure
  property_count: 3
  slug: trade-policy-add_joint_insured_request-structure
- name: Trade Policy Error_Response Structure
  property_count: 3
  slug: trade-policy-error_response-structure
- name: Trade Policy Job_Response Structure
  property_count: 5
  slug: trade-policy-job_response-structure
- name: Trade Policy Joint_Insured Structure
  property_count: 6
  slug: trade-policy-joint_insured-structure
- name: Trade Policy Joint_Insured_List Structure
  property_count: 1
  slug: trade-policy-joint_insured_list-structure
- name: Trade Policy Policy Structure
  property_count: 12
  slug: trade-policy-policy-structure
- name: Trade Policy Policy_List Structure
  property_count: 1
  slug: trade-policy-policy_list-structure
jsonld:
- class_count: 0
  name: Allianz Trade Claims Context
  property_count: 22
  slug: allianz-trade-claims-context
- class_count: 0
  name: Allianz Trade Company Grade Context
  property_count: 21
  slug: allianz-trade-company-grade-context
- class_count: 0
  name: Allianz Trade Payment Overdues Context
  property_count: 19
  slug: allianz-trade-payment-overdues-context
- class_count: 0
  name: Allianz Trade Policy Context
  property_count: 23
  slug: allianz-trade-policy-context
layout: provider
mcp_servers:
- description: ''
  name: allianz-trade-online-mcp.yml
  slug: allianz-trade-online-mcpyml
modified: '2026-06-20'
name: Allianz Trade
nav: Providers
network: true
overview: 'Allianz Trade publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Claims API, Company Grade API, Payment Overdues API, and 1 more. Tagged areas include Credit Insurance, Insurance, Risk Management, Trade Credit, and E-Commerce.


  The Allianz Trade catalog on APIs.io includes 4 JSON-LD contexts and 2 Spectral governance rulesets.


  Allianz Trade''s developer surface includes authentication, developer portal, getting-started guide, documentation, changelog, support, and 13 more developer resources.'
random_paper: 15
rules:
- name: Allianz Trade API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: allianz-trade-online-jsonschema-spectral-rules
- name: Allianz Trade API Rules
  rule_count: 31
  severity_counts:
    error: 6
    hint: 0
    info: 4
    warn: 21
  slug: allianz-trade-online-spectral-rules
scopes:
- name: Allianz Trade Online Scopes
  scope_count: 8
  slug: allianz-trade-online-scopes
  summary_line: 8 scopes · clientCredentials
score:
  band: thin
  composite: 39.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 30.6
    developer_ergonomics: 45.7
    discoverability: 92.6
    governance: 80.2
    operational_transparency: 15.8
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 51.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allianz-trade-online/refs/heads/main/screenshots/allianz-trade-online-2026-07-25T195702.png
security:
- kind: authentication
  name: Allianz Trade Online Authentication
  slug: allianz-trade-online-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Allianz Trade Online Domain Security
  slug: allianz-trade-online-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: allianz-trade-online
tags:
- Credit Insurance
- Insurance
- Risk Management
- Trade Credit
- E-Commerce
- Surety
use_cases:
- description: Integrate Allianz Trade APIs into SAP, Oracle, or other ERP systems to automate credit risk management and policy administration.
  name: ERP Credit Management Integration
- description: Build custom credit management dashboards pulling live credit grades, cover status, and claim data from Allianz Trade APIs.
  name: Automated Credit Risk Dashboard
- description: Enable real-time per-transaction credit underwriting for B2B online marketplaces and trade platforms using the E-Commerce APIs.
  name: B2B E-Commerce Credit Evaluation
- description: Automate payment overdue reporting to Allianz Trade when customers miss payment deadlines, triggering insurance coverage workflows.
  name: Payment Monitoring and Overdue Automation
website: https://www.allianz-trade.com/
---

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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 51
  human_in_the_loop: 1
  name: Remote Com Agentic Access
  operation_count: 121
  slug: remote-com-agentic-access
  summary_line: 121 operations · 51 acting · 1 human-in-the-loop
api_count: 40
apis:
- description: Remote emits webhook events for every meaningful state change across companies, employments, contractors, payroll, billing, time off, timesheets, benefits, identity verification, and SSO. Webhooks are
  name: Remote Webhooks
  slug: remote-webhooks
- description: Country and employment benefit offers
  name: Remote Benefit Offers API
  slug: remote-com-benefit-offers-api
- description: Annual benefit-renewal requests
  name: Remote Benefit Renewals API
  slug: remote-com-benefit-renewals-api
- description: Customer-facing invoices and statements
  name: Remote Billing Documents API
  slug: remote-com-billing-documents-api
- description: Create, retrieve, and update company records
  name: Remote Companies API
  slug: remote-com-companies-api
- description: List currencies a company can be billed in
  name: Remote Company Currencies API
  slug: remote-com-company-currencies-api
- description: Manage administrators and managers within a company
  name: Remote Company Managers API
  slug: remote-com-company-managers-api
- description: Reporting hierarchy and structure nodes for employees
  name: Remote Company Structure API
  slug: remote-com-company-structure-api
- description: Read compliance profiles and supported jurisdictions
  name: Remote Compliance API
  slug: remote-com-compliance-api
- description: Submit and track contract amendments
  name: Remote Contract Amendments API
  slug: remote-com-contract-amendments-api
- description: Sign, retrieve, and manage employment contract documents
  name: Remote Contract Documents API
  slug: remote-com-contract-documents-api
- description: Verify contractor-vs-employee classification
  name: Remote Contract Eligibility API
  slug: remote-com-contract-eligibility-api
- description: List currencies available for contractor payments
  name: Remote Contractor Currencies API
  slug: remote-com-contractor-currencies-api
- description: List and inspect contractor invoices
  name: Remote Contractor Invoices API
  slug: remote-com-contractor-invoices-api
- description: Manage contractor plan subscriptions (Standard, Plus, COR)
  name: Remote Contractor Subscriptions API
  slug: remote-com-contractor-subscriptions-api
- description: Terminate Contractor-of-Record engagements
  name: Remote COR Termination API
  slug: remote-com-cor-termination-api
- description: Estimate the loaded cost of hiring in a given country
  name: Remote Cost Calculator API
  slug: remote-com-cost-calculator-api
- description: List of countries Remote supports
  name: Remote Countries API
  slug: remote-com-countries-api
- description: Customer-defined fields on companies and employments
  name: Remote Custom Fields API
  slug: remote-com-custom-fields-api
- description: Manage company-defined departments and org structure
  name: Remote Departments API
  slug: remote-com-departments-api
- description: View active and pending employment contracts
  name: Remote Employment Contracts API
  slug: remote-com-employment-contracts-api
- description: Create, read, update, and invite employment records
  name: Remote Employments API
  slug: remote-com-employments-api
- description: Employee expense reimbursements
  name: Remote Expenses API
  slug: remote-com-expenses-api
- description: Document upload and retrieval
  name: Remote Files API
  slug: remote-com-files-api
- description: Inspect the identity of the current access token
  name: Remote Identity API
  slug: remote-com-identity-api
- description: One-time bonuses and recurring incentives
  name: Remote Incentives API
  slug: remote-com-incentives-api
- description: Per-employee leave balances
  name: Remote Leave Balances API
  slug: remote-com-leave-balances-api
- description: Per-country leave policy definitions
  name: Remote Leave Policies API
  slug: remote-com-leave-policies-api
- description: Generate passwordless magic links for users and employees
  name: Remote Magic Links API
  slug: remote-com-magic-links-api
- description: OAuth 2.0 authorization endpoints
  name: Remote OAuth API
  slug: remote-com-oauth-api
- description: Drive employee offboarding flows
  name: Remote Offboarding API
  slug: remote-com-offboarding-api
- description: Drive employee onboarding flows
  name: Remote Onboarding API
  slug: remote-com-onboarding-api
- description: Inspect payroll calendars for company, EOR, and Global Payroll
  name: Remote Payroll Calendars API
  slug: remote-com-payroll-calendars-api
- description: Released payslips for employees
  name: Remote Payslips API
  slug: remote-com-payslips-api
- description: Schedule recurring contractor invoices
  name: Remote Scheduled Invoices API
  slug: remote-com-scheduled-invoices-api
- description: Configure SAML/OIDC single sign-on for a company
  name: Remote SSO API
  slug: remote-com-sso-api
- description: Time-off requests and approvals
  name: Remote Time Off API
  slug: remote-com-time-off-api
- description: Hourly and salaried timesheets
  name: Remote Timesheets API
  slug: remote-com-timesheets-api
- description: Travel letter requests for employees moving across borders
  name: Remote Travel Letters API
  slug: remote-com-travel-letters-api
- description: Work authorization (visa / right to work) requests
  name: Remote Work Authorization API
  slug: remote-com-work-authorization-api
arazzos:
- description: Submit a contract amendment for an employment and track it to a resolved state.
  name: Remote Amend An Employment Contract
  slug: remote-com-amend-contract-workflow
- description: Find an employment's approved time off request and cancel it.
  name: Remote Cancel A Time Off Request
  slug: remote-com-cancel-time-off-workflow
- description: Confirm a country is supported, list its leave policies, and fetch one policy's detail.
  name: Remote Look Up A Country Leave Policy
  slug: remote-com-country-leave-policy-workflow
- description: Create a bonus or commission incentive for an employment and confirm it.
  name: Remote Create An Incentive
  slug: remote-com-create-incentive-workflow
- description: Find an active employee by email, list their payslips, and fetch the latest payslip detail.
  name: Remote Retrieve An Employee Payslip
  slug: remote-com-employee-payslip-workflow
- description: Read the benefit offers schema for an employment, select offers, and upsert the elections.
  name: Remote Enroll An Employee In Benefits
  slug: remote-com-enroll-employee-benefits-workflow
- description: Estimate the loaded cost of a hire, then create the employment once the budget is confirmed.
  name: Remote Estimate Cost Then Hire
  slug: remote-com-estimate-and-hire-workflow
- description: Create an EOR employment, confirm it, and invite the worker to self-serve onboarding.
  name: Remote Hire An EOR Employee
  slug: remote-com-hire-eor-employee-workflow
- description: Submit an offboarding for an employment and confirm it entered review.
  name: Remote Offboard An Employee
  slug: remote-com-offboard-employee-workflow
- description: Create a company, then add an initial department and an admin manager under it.
  name: Remote Onboard A New Company
  slug: remote-com-onboard-company-workflow
- description: Create a time off request, confirm it, and approve or decline it.
  name: Remote Request And Resolve Time Off
  slug: remote-com-request-time-off-workflow
- description: Find the latest issued billing document, confirm it, and pull its line-item breakdown.
  name: Remote Review A Billing Document
  slug: remote-com-review-billing-document-workflow
- description: Find a submitted timesheet for an employment and approve it or send it back.
  name: Remote Review A Timesheet
  slug: remote-com-review-timesheet-workflow
- description: Bulk-create scheduled contractor invoices, then confirm the first schedule.
  name: Remote Schedule Recurring Contractor Invoices
  slug: remote-com-schedule-contractor-invoices-workflow
- description: Run a contractor misclassification check, then act on the recommendation.
  name: Remote Screen A Contractor For Misclassification
  slug: remote-com-screen-contractor-workflow
- description: Create an expense, confirm it, and approve or decline it.
  name: Remote Submit And Resolve An Expense
  slug: remote-com-submit-expense-workflow
- description: Create a COR termination request, confirm it, and submit the termination.
  name: Remote Terminate A Contractor Of Record Engagement
  slug: remote-com-terminate-contractor-workflow
artifact_total: 137
asyncapis:
- description: Remote emits webhook events for nearly every state change across its Companies, Employments, Contractors, Payroll, Billing, Time Off, Timesheets, Benefits, Identity Verification, and SSO surfaces. All
  name: Remote Webhooks
  slug: remote-webhooks-asyncapi
collections:
- collection_type: postman
  name: Remote Benefits API
  slug: postman-remote-benefits-api
- collection_type: postman
  name: Remote Companies API
  slug: postman-remote-companies-api
- collection_type: postman
  name: Remote Contractors API
  slug: postman-remote-contractors-api
- collection_type: postman
  name: Remote Employments API
  slug: postman-remote-employments-api
- collection_type: postman
  name: Remote Files And Custom Fields API
  slug: postman-remote-files-api
- collection_type: postman
  name: Remote OAuth 2.0 API
  slug: postman-remote-oauth-api
- collection_type: postman
  name: Remote Payroll and Billing API
  slug: postman-remote-payroll-billing-api
- collection_type: postman
  name: Remote Time and Attendance API
  slug: postman-remote-time-attendance-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Remote Benefits API
  slug: open-remote-benefits-api
- collection_type: open
  name: Remote Benefits Benefit Offers API
  slug: open-remote-com-benefit-offers-api
- collection_type: open
  name: Remote Benefits Benefit Offers Benefit Renewals API
  slug: open-remote-com-benefit-renewals-api
- collection_type: open
  name: Remote Benefits Benefit Offers Billing Documents API
  slug: open-remote-com-billing-documents-api
- collection_type: open
  name: Remote Benefits Benefit Offers Companies API
  slug: open-remote-com-companies-api
- collection_type: open
  name: Remote Benefits Benefit Offers Company Currencies API
  slug: open-remote-com-company-currencies-api
- collection_type: open
  name: Remote Benefits Benefit Offers Company Managers API
  slug: open-remote-com-company-managers-api
- collection_type: open
  name: Remote Benefits Benefit Offers Company Structure API
  slug: open-remote-com-company-structure-api
- collection_type: open
  name: Remote Benefits Benefit Offers Compliance API
  slug: open-remote-com-compliance-api
- collection_type: open
  name: Remote Benefits Benefit Offers Contract Amendments API
  slug: open-remote-com-contract-amendments-api
- collection_type: open
  name: Remote Benefits Benefit Offers Contract Documents API
  slug: open-remote-com-contract-documents-api
- collection_type: open
  name: Remote Benefits Benefit Offers Contract Eligibility API
  slug: open-remote-com-contract-eligibility-api
- collection_type: open
  name: Remote Benefits Benefit Offers Contractor Currencies API
  slug: open-remote-com-contractor-currencies-api
- collection_type: open
  name: Remote Benefits Benefit Offers Contractor Invoices API
  slug: open-remote-com-contractor-invoices-api
- collection_type: open
  name: Remote Benefits Benefit Offers Contractor Subscriptions API
  slug: open-remote-com-contractor-subscriptions-api
- collection_type: open
  name: Remote Benefits Benefit Offers COR Termination API
  slug: open-remote-com-cor-termination-api
- collection_type: open
  name: Remote Benefits Benefit Offers Cost Calculator API
  slug: open-remote-com-cost-calculator-api
- collection_type: open
  name: Remote Benefits Benefit Offers Countries API
  slug: open-remote-com-countries-api
- collection_type: open
  name: Remote Benefits Benefit Offers Custom Fields API
  slug: open-remote-com-custom-fields-api
- collection_type: open
  name: Remote Benefits Benefit Offers Departments API
  slug: open-remote-com-departments-api
- collection_type: open
  name: Remote Benefits Benefit Offers Employment Contracts API
  slug: open-remote-com-employment-contracts-api
- collection_type: open
  name: Remote Benefits Benefit Offers Employments API
  slug: open-remote-com-employments-api
- collection_type: open
  name: Remote Benefits Benefit Offers Expenses API
  slug: open-remote-com-expenses-api
- collection_type: open
  name: Remote Benefits Benefit Offers Files API
  slug: open-remote-com-files-api
- collection_type: open
  name: Remote Benefits Benefit Offers Identity API
  slug: open-remote-com-identity-api
- collection_type: open
  name: Remote Benefits Benefit Offers Incentives API
  slug: open-remote-com-incentives-api
- collection_type: open
  name: Remote Benefits Benefit Offers Leave Balances API
  slug: open-remote-com-leave-balances-api
- collection_type: open
  name: Remote Benefits Benefit Offers Leave Policies API
  slug: open-remote-com-leave-policies-api
- collection_type: open
  name: Remote Benefits Benefit Offers Magic Links API
  slug: open-remote-com-magic-links-api
- collection_type: open
  name: Remote Benefits Benefit Offers OAuth API
  slug: open-remote-com-oauth-api
- collection_type: open
  name: Remote Benefits Benefit Offers Offboarding API
  slug: open-remote-com-offboarding-api
- collection_type: open
  name: Remote Benefits Benefit Offers Onboarding API
  slug: open-remote-com-onboarding-api
- collection_type: open
  name: Remote Benefits Benefit Offers Payroll Calendars API
  slug: open-remote-com-payroll-calendars-api
- collection_type: open
  name: Remote Benefits Benefit Offers Payslips API
  slug: open-remote-com-payslips-api
- collection_type: open
  name: Remote Benefits Benefit Offers Scheduled Invoices API
  slug: open-remote-com-scheduled-invoices-api
- collection_type: open
  name: Remote Benefits Benefit Offers SSO API
  slug: open-remote-com-sso-api
- collection_type: open
  name: Remote Benefits Benefit Offers Time Off API
  slug: open-remote-com-time-off-api
- collection_type: open
  name: Remote Benefits Benefit Offers Timesheets API
  slug: open-remote-com-timesheets-api
- collection_type: open
  name: Remote Benefits Benefit Offers Travel Letters API
  slug: open-remote-com-travel-letters-api
- collection_type: open
  name: Remote Benefits Benefit Offers Work Authorization API
  slug: open-remote-com-work-authorization-api
- collection_type: open
  name: Remote Companies API
  slug: open-remote-companies-api
- collection_type: open
  name: Remote Contractors API
  slug: open-remote-contractors-api
- collection_type: open
  name: Remote Employments API
  slug: open-remote-employments-api
- collection_type: open
  name: Remote Files And Custom Fields API
  slug: open-remote-files-api
- collection_type: open
  name: Remote OAuth 2.0 API
  slug: open-remote-oauth-api
- collection_type: open
  name: Remote Payroll and Billing API
  slug: open-remote-payroll-billing-api
- collection_type: open
  name: Remote Time and Attendance API
  slug: open-remote-time-attendance-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/remote-com-benefits-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/remote-com-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/remote-com-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/remote-com-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/remote-com-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/remote-com-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/remote-com-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/remote-com-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/remote-com-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/remote-com-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/remote-com-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/remote-com-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/remote-com-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/remote-com-cli.yml
- group: design
  title: ''
  type: Components
  url: components/remote-com-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/remote-com-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/remote-com-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/remote-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/remote-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/remote-com-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/remote/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-amend-contract-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-cancel-time-off-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-country-leave-policy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-create-incentive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-employee-payslip-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-enroll-employee-benefits-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-estimate-and-hire-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-hire-eor-employee-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-offboard-employee-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-onboard-company-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-request-time-off-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-review-billing-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-review-timesheet-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-schedule-contractor-invoices-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-screen-contractor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-submit-expense-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/remote-com-terminate-contractor-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://remote.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.remote.com
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.remote.com/llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.remote.com/docs/changelogs
- group: operate
  title: ''
  type: StatusPage
  url: https://remote.com/status
- group: auth
  title: ''
  type: Security
  url: https://trust.remote.com
- group: commercial
  title: ''
  type: Pricing
  url: https://remote.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://remote.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.remote.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://remote.com/legal/terms
- group: commercial
  title: ''
  type: Privacy
  url: https://remote.com/legal/privacy
- group: company
  title: ''
  type: Careers
  url: https://remote.com/careers
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/remote
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/remote-com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/remoteoss
- group: commercial
  title: ''
  type: Plans
  url: plans/remote-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/remote-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/remote-com-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/remote-com-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/remote-com-vocabulary.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: build
  title: ''
  type: CLI
  url: https://github.com/remoteoss/remote-cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/remoteoss/ai-agent-toolkit
- group: build
  title: ''
  type: SDKs
  url: https://github.com/remoteoss/remote-flows
- group: build
  title: ''
  type: SDKs
  url: https://github.com/remoteoss/json-schema-form
- group: build
  title: ''
  type: SDKs
  url: https://github.com/remoteoss/react-url-modal
- group: docs
  title: ''
  type: Documentation
  url: https://developer.remote.com/docs/introduction-to-remote-mcp
created: '2026-05-25'
description: Remote.com is a global employment platform that lets companies hire, pay, and manage employees and contractors in 90+ countries without setting up local entities. Remote owns in-country legal entities across its EOR footprint and runs its own global payroll and benefits infrastructure rather than reselling third-party providers. The platform layers a developer API, partner OAuth flows, webhooks, a CLI, language SDKs, an AI agent toolkit, and an official MCP server on top of these services so customers and partners can fully automate hiring, onboarding, payroll, benefits, time off, expenses, and offboarding.
examples:
- key_count: 2
  name: Remote Cost Estimate Example
  slug: remote-cost-estimate-example
- key_count: 2
  name: Remote Create Employment Example
  slug: remote-create-employment-example
- key_count: 2
  name: Remote Create Timeoff Example
  slug: remote-create-timeoff-example
- key_count: 4
  name: Remote Employment Onboarding Completed Webhook Example
  slug: remote-employment-onboarding-completed-webhook-example
- key_count: 2
  name: Remote Oauth Token Exchange Example
  slug: remote-oauth-token-exchange-example
finops:
- name: Remote Com Finops
  service_category: ''
  slug: remote-com-finops
image: https://remote.com/favicon.ico
json_schemas:
- name: BillingDocument
  property_count: 10
  slug: remote-billing-document
- name: Company
  property_count: 12
  slug: remote-company
- name: Employment
  property_count: 18
  slug: remote-employment
- name: TimeOff
  property_count: 10
  slug: remote-time-off
jsonld:
- class_count: 0
  name: Remote Com Context
  property_count: 10
  slug: remote-com-context
layout: provider
mcp_servers:
- description: 'Remote.com''s official MCP server lets MCP-standard AI agents act on Remote data. Authentication is OAuth 2.0 Authorization Code with PKCE through the normal Remote browser sign-in with Dynamic Client '
  name: Remote MCP Server
  slug: remote-mcp-server
modified: '2026-06-20'
name: Remote
nav: Providers
network: true
overview: 'Remote publishes 40 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Benefit Offers API, Benefit Renewals API, and 37 more. Tagged areas include Global Payroll, EOR, Contractor Management, Contractor of Record, and PEO.


  The Remote catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Remote''s developer surface includes sandbox, changelog, CLI, authentication, pricing, engineering blog, support, and 58 more developer resources.'
plans:
- name: Remote Com Plans Pricing
  plan_count: 11
  slug: remote-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Remote Com Rate Limits
  slug: remote-com-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Remote API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: remote-com-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Remote API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: remote-com-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Remote API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 6
  slug: remote-com-rules
scopes:
- name: Remote Com Scopes
  scope_count: 74
  slug: remote-com-scopes
  summary_line: 74 scopes · authorizationCode/clientCredentials/urn:ietf:params:oauth:grant-type:jwt-bearer
score:
  band: exemplar
  composite: 70.4
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 45.5
    contract_quality: 71.5
    developer_ergonomics: 73.8
    discoverability: 75.9
    governance: 45.5
    operational_transparency: 68.4
  previous_composite: 70.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 39
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/remote-com/refs/heads/main/screenshots/remote-com-2026-06-20T192847.png
security:
- kind: authentication
  name: Remote Com Authentication
  slug: remote-com-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Remote Com Domain Security
  slug: remote-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Remote Com Vulnerability Disclosure
  slug: remote-com-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Remote Com Trust Center
  slug: remote-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: remote-com
tags:
- Global Payroll
- EOR
- Contractor Management
- Contractor of Record
- PEO
- HRIS
- Recruiting
- Benefits
- Employment
- HR
- Compliance
- Workforce
- MCP
- AI Agents
website: https://remote.com
---

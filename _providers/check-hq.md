---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: unknown
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 90
  human_in_the_loop: 0
  name: Check Hq Agentic Access
  operation_count: 188
  slug: check-hq-agentic-access
  summary_line: 188 operations · 90 acting
api_count: 1
apis:
- description: The Check Payroll API is a comprehensive REST API for embedding end-to-end U.S. payroll inside another platform. It models companies, workplaces, employees, contractors, pay schedules, paydays, payrol
  name: Check Payroll API
  slug: payroll-api
- description: Check Components is a library of white-labeled, drop-in React UI elements that handle the highest-friction surfaces of embedded payroll — company onboarding, terms of service, bank linking, employee t
  name: Check Components
  slug: components
- description: The Check MCP Server exposes the Check Payroll API to AI tools and agents via the Model Context Protocol. It is offered as both a hosted (remote) endpoint requiring no infrastructure and a self-hosted
  name: Check MCP Server
  slug: mcp-server
- description: The Check Command-Line Interface is a Python-based CLI installed via the uv package manager that exposes 270 functions across 18 resource groups of the Check Payroll API. It is designed for shell scri
  name: Check CLI
  slug: cli
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Addresses API from Check — 1 operation(s) for addresses.
  name: Check Addresses API
  slug: check-hq-addresses-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Agencies API from Check — 2 operation(s) for agencies.
  name: Check Agencies API
  slug: check-hq-agencies-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Bank Accounts API from Check — 3 operation(s) for bank accounts.
  name: Check Bank Accounts API
  slug: check-hq-bank-accounts-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Benefits API from Check — 2 operation(s) for benefits.
  name: Check Benefits API
  slug: check-hq-benefits-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Communications API from Check — 2 operation(s) for communications.
  name: Check Communications API
  slug: check-hq-communications-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Companies API from Check — 31 operation(s) for companies.
  name: Check Companies API
  slug: check-hq-companies-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Company Benefits API from Check — 2 operation(s) for company benefits.
  name: Check Company Benefits API
  slug: check-hq-company-benefits-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Company Provided Documents API from Check — 1 operation(s) for company provided documents.
  name: Check Company Provided Documents API
  slug: check-hq-company-provided-documents-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Company Tax Elections API from Check — 1 operation(s) for company tax elections.
  name: Check Company Tax Elections API
  slug: check-hq-company-tax-elections-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Company Tax Params API from Check — 2 operation(s) for company tax params.
  name: Check Company Tax Params API
  slug: check-hq-company-tax-params-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Contractor Payments API from Check — 3 operation(s) for contractor payments.
  name: Check Contractor Payments API
  slug: check-hq-contractor-payments-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Contractors API from Check — 7 operation(s) for contractors.
  name: Check Contractors API
  slug: check-hq-contractors-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Corrections API from Check — 10 operation(s) for corrections.
  name: Check Corrections API
  slug: check-hq-corrections-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Documents API from Check — 7 operation(s) for documents.
  name: Check Documents API
  slug: check-hq-documents-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Earning Codes API from Check — 2 operation(s) for earning codes.
  name: Check Earning Codes API
  slug: check-hq-earning-codes-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Earning Rates API from Check — 2 operation(s) for earning rates.
  name: Check Earning Rates API
  slug: check-hq-earning-rates-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Employee Tax Elections API from Check — 1 operation(s) for employee tax elections.
  name: Check Employee Tax Elections API
  slug: check-hq-employee-tax-elections-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Employee Tax Params API from Check — 4 operation(s) for employee tax params.
  name: Check Employee Tax Params API
  slug: check-hq-employee-tax-params-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Employee Tax Statements API from Check — 2 operation(s) for employee tax statements.
  name: Check Employee Tax Statements API
  slug: check-hq-employee-tax-statements-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Employees API from Check — 5 operation(s) for employees.
  name: Check Employees API
  slug: check-hq-employees-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The External Payrolls API from Check — 6 operation(s) for external payrolls.
  name: Check External Payrolls API
  slug: check-hq-external-payrolls-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Filings API from Check — 4 operation(s) for filings.
  name: Check Filings API
  slug: check-hq-filings-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Forms API from Check — 2 operation(s) for forms.
  name: Check Forms API
  slug: check-hq-forms-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Fulfillments API from Check — 3 operation(s) for fulfillments.
  name: Check Fulfillments API
  slug: check-hq-fulfillments-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Integrations API from Check — 6 operation(s) for integrations.
  name: Check Integrations API
  slug: check-hq-integrations-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Logs API from Check — 2 operation(s) for logs.
  name: Check Logs API
  slug: check-hq-logs-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Net Pay Splits API from Check — 1 operation(s) for net pay splits.
  name: Check Net Pay Splits API
  slug: check-hq-net-pay-splits-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Notifications API from Check — 2 operation(s) for notifications.
  name: Check Notifications API
  slug: check-hq-notifications-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Pay Schedules API from Check — 3 operation(s) for pay schedules.
  name: Check Pay Schedules API
  slug: check-hq-pay-schedules-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Payments API from Check — 4 operation(s) for payments.
  name: Check Payments API
  slug: check-hq-payments-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Payroll Items API from Check — 3 operation(s) for payroll items.
  name: Check Payroll Items API
  slug: check-hq-payroll-items-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Payrolls API from Check — 12 operation(s) for payrolls.
  name: Check Payrolls API
  slug: check-hq-payrolls-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Post Tax Deductions API from Check — 2 operation(s) for post tax deductions.
  name: Check Post Tax Deductions API
  slug: check-hq-post-tax-deductions-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Report Runs API from Check — 3 operation(s) for report runs.
  name: Check Report Runs API
  slug: check-hq-report-runs-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Setups API from Check — 2 operation(s) for setups.
  name: Check Setups API
  slug: check-hq-setups-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Tax Packages API from Check — 3 operation(s) for tax packages.
  name: Check Tax Packages API
  slug: check-hq-tax-packages-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Taxes API from Check — 2 operation(s) for taxes.
  name: Check Taxes API
  slug: check-hq-taxes-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Usage API from Check — 2 operation(s) for usage.
  name: Check Usage API
  slug: check-hq-usage-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Webhook Configs API from Check — 2 operation(s) for webhook configs.
  name: Check Webhook Configs API
  slug: check-hq-webhook-configs-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Webhook Deliveries API from Check — 3 operation(s) for webhook deliveries.
  name: Check Webhook Deliveries API
  slug: check-hq-webhook-deliveries-api
- baseURL: https://api.checkhq.com
  baseurl_source: declared
  description: The Workplaces API from Check — 2 operation(s) for workplaces.
  name: Check Workplaces API
  slug: check-hq-workplaces-api
artifact_total: 60
common:
- group: other
  href: https://artifacts.apis.io/check-hq/capabilities/check-hq-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/check-hq-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/check-hq/agentic-access/check-hq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/check-hq-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/check-hq/rules/check-hq-rules.yml
  title: ''
  type: Spectral
  url: rules/check-hq-rules.yml
- group: design
  href: https://artifacts.apis.io/check-hq/json-ld/check-hq-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/check-hq-context.jsonld
- group: design
  href: https://artifacts.apis.io/check-hq/vocabulary/check-hq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/check-hq-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/check-hq/data-model/check-hq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/check-hq-data-model.yml
- group: design
  href: https://artifacts.apis.io/check-hq/conventions/check-hq-conventions.yml
  title: ''
  type: Conventions
  url: conventions/check-hq-conventions.yml
- group: design
  href: https://artifacts.apis.io/check-hq/errors/check-hq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/check-hq-problem-types.yml
- group: design
  href: https://artifacts.apis.io/check-hq/conformance/check-hq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/check-hq-conformance.yml
- group: agent
  href: https://artifacts.apis.io/check-hq/llms/check-hq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/check-hq-llms.txt
- group: other
  href: https://artifacts.apis.io/check-hq/hosts/check-hq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/check-hq-hosts.yml
- group: other
  href: https://artifacts.apis.io/check-hq/vendors/check-hq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/check-hq-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.checkhq.com/company/terms
- group: auth
  title: ''
  type: Security
  url: https://www.checkhq.com/company/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.checkhq.com/company/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.checkhq.com/company/press
- group: auth
  href: https://artifacts.apis.io/check-hq/authentication/check-hq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/check-hq-authentication.yml
- group: auth
  href: https://artifacts.apis.io/check-hq/security/check-hq-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/check-hq-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/check-hq/security/check-hq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/check-hq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.checkhq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.checkhq.com
- group: start
  title: ''
  type: Portal
  url: https://console.checkhq.com
- group: start
  title: ''
  type: Console
  url: https://console.checkhq.com/login
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.checkhq.com
- group: company
  title: ''
  type: Blog
  url: https://www.checkhq.com/resources
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.checkhq.com/resources/changelog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.checkhq.com
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.checkhq.com/docs/status-page
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/checkhq
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.checkhq.com/llms.txt
- group: company
  title: ''
  type: Careers
  url: https://www.checkhq.com/company/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/check-technologies
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/check-2a75
- group: other
  title: ''
  type: Customers
  url: ''
- group: other
  title: ''
  type: Funding
  url: ''
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/check-technologies/mcp-server-check
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://docs.checkhq.com/docs/overview
created: '2026-05-25'
description: Check is an embedded payroll infrastructure platform that allows vertical SaaS, HR, workforce management, and financial services companies to natively offer payroll inside their own products. Check provides a comprehensive REST API, a library of white-labeled React components (Check Components and Check Onboard), a CLI, and a Model Context Protocol (MCP) server that together cover company and employee onboarding, pay schedules, payroll preview and approval, contractor payments, tax calculation, multi-state withholdings, tax filings, tax deposits, money movement, paystubs, garnishments, post-tax deductions, net pay splits, benefits (health, 401k, workers' comp), W-2 and 1099 generation, and webhook event delivery. Check operates in all 50 U.S. states plus D.C., has been incubated and led-funded by Stripe (Series B and Series C), and powers payroll for partners such as Homebase, ServiceTitan, 7shifts, Housecall Pro, Wave, Zoho, and Procare — collectively paying more than 1M employees
  across 35,000+ businesses and moving $15B+ annually.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/check-hq.png
json_schemas:
- name: EarningRate
  property_count: 9
  slug: check-hq-earning-rate
- name: Log
  property_count: 13
  slug: check-hq-log
jsonld:
- class_count: 2
  name: Check Hq Context
  property_count: 21
  slug: check-hq-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: Remote MCP server at docs.checkhq.com over HTTP.
  name: Check MCP Server
  slug: check-hq
modified: '2026-07-12'
name: Check
nav: Providers
network: true
overview: 'Check publishes 45 API contracts indexed on the [APIs.io](https://apis.io/) network, including Addresses API, Agencies API, Bank Accounts API, and 42 more. Tagged areas include Payroll, Embedded Payroll, Payroll Infrastructure, Payroll API, and Tax Filing.


  The Check catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Check''s developer surface includes authentication, documentation, developer portal, developer console, sandbox, engineering blog, changelog, and 28 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Check API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 2
  slug: check-hq-rules
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.0
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 70.3
    developer_ergonomics: 64.3
    discoverability: 67.5
    operational_transparency: 52.6
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 41
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/check-hq/check-hq-2026-06-20T174239.png
security:
- kind: authentication
  name: Check Hq Authentication
  slug: check-hq-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Check Hq Domain Security
  slug: check-hq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Check Hq Vulnerability Disclosure
  slug: check-hq-vulnerability-disclosure
  summary_line: no policy recorded
slug: check-hq
solutions:
- description: Drop-in Components let early-stage platforms launch payroll quickly without bespoke UI.
  name: Startups
- description: Flexible API enables deeply customized payroll experiences for large vertical SaaS and workforce platforms.
  name: Enterprise Platforms
- description: Couple scheduling and timekeeping with end-to-end payroll, taxes, and money movement.
  name: Workforce Management
- description: Embed native payroll inside industry-specific software for trades, hospitality, fitness, and more.
  name: Vertical SaaS
- description: Sync payroll journals and tax events into accounting platforms with workplace breakdowns.
  name: Accounting and Financial Management
tags:
- Payroll
- Embedded Payroll
- Payroll Infrastructure
- Payroll API
- Tax Filing
- Tax Calculation
- Money Movement
- Human Resources
- Workforce Management
- Fintech
- Compensation
- Benefits
- '1099'
- W-2
- Contractor Payments
- Embedded Finance
website: https://www.checkhq.com
---

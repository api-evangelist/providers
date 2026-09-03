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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Gusto Agentic Access
  operation_count: 25
  slug: gusto-agentic-access
  summary_line: 25 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Gusto Embedded Payroll API enables platforms to build and embed modern payroll, benefits, and HR tooling into their own products. The API exposes endpoints for company onboarding, employee and con
  name: Gusto Embedded Payroll API
  slug: embedded-payroll-api
- description: The Gusto Embedded React SDK provides pre-built UI flows and components that platforms can drop into their own React applications to surface Gusto Embedded Payroll experiences (company onboarding, emp
  name: Gusto Embedded React SDK
  slug: embedded-react-sdk
- baseURL: https://api.gusto.com
  baseurl_source: declared
  description: The BankAccounts API from Gusto — 3 operation(s) for bankaccounts.
  name: Gusto BankAccounts API
  slug: gusto-bankaccounts-api
- baseURL: https://api.gusto.com
  baseurl_source: declared
  description: The Companies API from Gusto — 4 operation(s) for companies.
  name: Gusto Companies API
  slug: gusto-companies-api
- baseURL: https://api.gusto.com
  baseurl_source: declared
  description: The ContractorPayments API from Gusto — 2 operation(s) for contractorpayments.
  name: Gusto ContractorPayments API
  slug: gusto-contractorpayments-api
- baseURL: https://api.gusto.com
  baseurl_source: declared
  description: The Contractors API from Gusto — 2 operation(s) for contractors.
  name: Gusto Contractors API
  slug: gusto-contractors-api
- baseURL: https://api.gusto.com
  baseurl_source: declared
  description: The Employees API from Gusto — 1 operation(s) for employees.
  name: Gusto Employees API
  slug: gusto-employees-api
- baseURL: https://api.gusto.com
  baseurl_source: declared
  description: The Flows API from Gusto — 1 operation(s) for flows.
  name: Gusto Flows API
  slug: gusto-flows-api
- baseURL: https://api.gusto.com
  baseurl_source: declared
  description: The Payrolls API from Gusto — 3 operation(s) for payrolls.
  name: Gusto Payrolls API
  slug: gusto-payrolls-api
- baseURL: https://api.gusto.com
  baseurl_source: declared
  description: The PaySchedules API from Gusto — 2 operation(s) for payschedules.
  name: Gusto PaySchedules API
  slug: gusto-payschedules-api
- baseURL: https://api.gusto.com
  baseurl_source: declared
  description: The Reports API from Gusto — 2 operation(s) for reports.
  name: Gusto Reports API
  slug: gusto-reports-api
- baseURL: https://api.gusto.com
  baseurl_source: declared
  description: The Webhooks API from Gusto — 1 operation(s) for webhooks.
  name: Gusto Webhooks API
  slug: gusto-webhooks-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gusto Embedded Payroll Webhooks
  slug: open-gusto-asyncapi
- collection_type: open
  name: Gusto Embedded Payroll BankAccounts API
  slug: open-gusto-bankaccounts-api
- collection_type: open
  name: Gusto Embedded Payroll BankAccounts Companies API
  slug: open-gusto-companies-api
- collection_type: open
  name: Gusto Embedded Payroll BankAccounts ContractorPayments API
  slug: open-gusto-contractorpayments-api
- collection_type: open
  name: Gusto Embedded Payroll BankAccounts Contractors API
  slug: open-gusto-contractors-api
- collection_type: open
  name: Gusto Embedded Payroll BankAccounts Employees API
  slug: open-gusto-employees-api
- collection_type: open
  name: Gusto Embedded Payroll BankAccounts Flows API
  slug: open-gusto-flows-api
- collection_type: open
  name: Gusto Embedded Payroll BankAccounts Payrolls API
  slug: open-gusto-payrolls-api
- collection_type: open
  name: Gusto Embedded Payroll BankAccounts PaySchedules API
  slug: open-gusto-payschedules-api
- collection_type: open
  name: Gusto Embedded Payroll BankAccounts Reports API
  slug: open-gusto-reports-api
- collection_type: open
  name: Gusto Embedded Payroll BankAccounts Webhooks API
  slug: open-gusto-webhooks-api
- collection_type: open
  name: Gusto Embedded Payroll API
  slug: open-gusto
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Gusto/embedded-react-sdk/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Gusto/embedded-react-sdk/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Gusto/embedded-react-sdk/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gusto-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gusto-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gusto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gusto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gusto-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gustohq
- group: company
  title: ''
  type: Website
  url: https://gusto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gusto.com/embedded-payroll
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gusto.com/embedded-payroll
- group: start
  title: ''
  type: SignupURL
  url: https://gusto.com/embedded-payroll
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Gusto
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Gusto/gusto-python-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Gusto/gusto-typescript-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Gusto/gusto-ruby-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Gusto/gusto-java-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Gusto/gusto-csharp-client
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gusto.com/about/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gusto.com/about/terms
- group: operate
  title: ''
  type: Support
  url: https://support.gusto.com/
- group: company
  title: ''
  type: Blog
  url: https://gusto.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.gusto.com/login
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.gusto.com/llms.txt
created: '2026-05-05'
description: A cloud-based payroll, benefits, and human resources platform designed for small and medium-sized businesses. Gusto Embedded enables platforms to integrate payroll, tax filing, and HR workflows directly into their products via a REST API, React SDK, and webhooks.
graphqls:
- description: This document describes the conceptual GraphQL schema for the Gusto Embedded Payroll API. Gusto provides a REST API; this schema represents the domain model as a GraphQL type system to enable graph-ba
  name: Gusto GraphQL Schema
  slug: gusto-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gusto.png
layout: provider
modified: '2026-05-30'
name: Gusto
nav: Providers
network: true
overview: 'Gusto publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Embedded Payroll API, BankAccounts API, Companies API, and 8 more. Tagged areas include Human Resources, Payroll, Benefits, Enterprise Software, and Embedded Finance.


  Gusto''s developer surface includes authentication, documentation, support, engineering blog, and 21 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 62.1
    developer_ergonomics: 34.5
    discoverability: 70.4
    governance: 0.0
    operational_transparency: 9.2
  open_source:
    applies: true
    score: 25.0
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gusto/refs/heads/main/screenshots/gusto-2026-06-20T182442.png
security:
- kind: authentication
  name: Gusto Authentication
  slug: gusto-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gusto Domain Security
  slug: gusto-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Gusto Vulnerability Disclosure
  slug: gusto-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Gusto Trust Center
  slug: gusto-trust-center
  summary_line: SOC 2, HIPAA
slug: gusto
tags:
- Human Resources
- Payroll
- Benefits
- Enterprise Software
- Embedded Finance
website: https://gusto.com/
---

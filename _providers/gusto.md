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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Gusto Agentic Access
  operation_count: 25
  slug: gusto-agentic-access
  summary_line: 25 operations · 17 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: The Gusto Embedded Payroll API enables platforms to build and embed modern payroll, benefits, and HR tooling into their own products. The API exposes endpoints for company onboarding, employee and con
  name: Gusto Embedded Payroll API
  slug: embedded-payroll-api
- description: The Gusto Embedded React SDK provides pre-built UI flows and components that platforms can drop into their own React applications to surface Gusto Embedded Payroll experiences (company onboarding, emp
  name: Gusto Embedded React SDK
  slug: embedded-react-sdk
- description: The BankAccounts API from Gusto — 3 operation(s) for bankaccounts.
  name: Gusto BankAccounts API
  slug: gusto-bankaccounts-api
- description: The Companies API from Gusto — 4 operation(s) for companies.
  name: Gusto Companies API
  slug: gusto-companies-api
- description: The ContractorPayments API from Gusto — 2 operation(s) for contractorpayments.
  name: Gusto ContractorPayments API
  slug: gusto-contractorpayments-api
- description: The Contractors API from Gusto — 2 operation(s) for contractors.
  name: Gusto Contractors API
  slug: gusto-contractors-api
- description: The Employees API from Gusto — 1 operation(s) for employees.
  name: Gusto Employees API
  slug: gusto-employees-api
- description: The Flows API from Gusto — 1 operation(s) for flows.
  name: Gusto Flows API
  slug: gusto-flows-api
- description: The Payrolls API from Gusto — 3 operation(s) for payrolls.
  name: Gusto Payrolls API
  slug: gusto-payrolls-api
- description: The PaySchedules API from Gusto — 2 operation(s) for payschedules.
  name: Gusto PaySchedules API
  slug: gusto-payschedules-api
- description: The Reports API from Gusto — 2 operation(s) for reports.
  name: Gusto Reports API
  slug: gusto-reports-api
- description: The Webhooks API from Gusto — 1 operation(s) for webhooks.
  name: Gusto Webhooks API
  slug: gusto-webhooks-api
artifact_total: 20
collections:
- collection_type: open
  name: Gusto Embedded Payroll Webhooks
  slug: open-gusto-asyncapi
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
random_paper: 82
score:
  band: developing
  composite: 42.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 66.1
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 90.9
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.11.0
  scored_at: '2026-08-12'
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

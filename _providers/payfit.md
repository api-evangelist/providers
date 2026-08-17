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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Payfit Agentic Access
  operation_count: 17
  slug: payfit-agentic-access
  summary_line: 17 operations · 3 acting
api_count: 9
apis:
- description: OAuth 2.0 REST API for solution developers building integrations with PayFit. Once enabled by a customer, partners can synchronize collaborators, payroll journals, meal vouchers, and other HR data.
  name: PayFit Partner API
  slug: partner-api
- description: Private REST API for PayFit customers to access their own company data via long-lived private API keys, suitable for in-house scripts and direct integrations.
  name: PayFit Customer API
  slug: customer-api
- description: The Absences API from PayFit — 1 operation(s) for absences.
  name: PayFit Absences API
  slug: payfit-absences-api
- description: The Collaborators API from PayFit — 2 operation(s) for collaborators.
  name: PayFit Collaborators API
  slug: payfit-collaborators-api
- description: The Company API from PayFit — 4 operation(s) for company.
  name: PayFit Company API
  slug: payfit-company-api
- description: The Contracts API from PayFit — 2 operation(s) for contracts.
  name: PayFit Contracts API
  slug: payfit-contracts-api
- description: The Documents API from PayFit — 1 operation(s) for documents.
  name: PayFit Documents API
  slug: payfit-documents-api
- description: The Insurance API from PayFit — 3 operation(s) for insurance.
  name: PayFit Insurance API
  slug: payfit-insurance-api
- description: The Payslips API from PayFit — 2 operation(s) for payslips.
  name: PayFit Payslips API
  slug: payfit-payslips-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PayFit Partner & Customer Absences API
  slug: open-payfit-absences-api
- collection_type: open
  name: PayFit Partner & Customer Absences Collaborators API
  slug: open-payfit-collaborators-api
- collection_type: open
  name: PayFit Partner & Customer Absences Company API
  slug: open-payfit-company-api
- collection_type: open
  name: PayFit Partner & Customer Absences Contracts API
  slug: open-payfit-contracts-api
- collection_type: open
  name: PayFit Partner & Customer Absences Documents API
  slug: open-payfit-documents-api
- collection_type: open
  name: PayFit Partner & Customer Absences Insurance API
  slug: open-payfit-insurance-api
- collection_type: open
  name: PayFit Partner & Customer Absences Payslips API
  slug: open-payfit-payslips-api
- collection_type: open
  name: PayFit Partner & Customer API
  slug: open-payfit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/payfit-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/payfit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/payfit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payfit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/payfit-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PayFit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/payfit
- group: company
  title: ''
  type: Website
  url: https://payfit.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.payfit.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://payfit.com/uk/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.payfit.com/signup
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.payfit.io/llms.txt
created: '2026-05-11'
description: 'PayFit is a cloud-based payroll and HR platform serving small and mid-sized businesses in France, the United Kingdom, Spain, Germany, and Italy with automated payroll, expense management, leave and time tracking, and employee self-service. The platform handles country-specific payroll calculations, tax filings, and social declarations alongside core HR workflows. PayFit exposes two REST APIs: a Customer API authenticated via private API keys for direct company-data access, and a Partner API using OAuth 2.0 for integration developers building marketplace solutions.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payfit.png
layout: provider
modified: '2026-05-11'
name: PayFit
nav: Providers
network: true
overview: 'PayFit publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Absences API, Collaborators API, Company API, and 4 more. Tagged areas include Payroll, Human Resources, HR Tech, Europe Payroll, and Time and Attendance.


  PayFit''s developer surface includes authentication, documentation, pricing, signup flow, and 8 more developer resources.'
random_paper: 57
score:
  band: thin
  composite: 32.9
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 55.2
    developer_ergonomics: 19.6
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payfit/refs/heads/main/screenshots/payfit-2026-06-20T191458.png
security:
- kind: authentication
  name: Payfit Authentication
  slug: payfit-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Payfit Domain Security
  slug: payfit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Payfit Vulnerability Disclosure
  slug: payfit-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Payfit Trust Center
  slug: payfit-trust-center
  summary_line: ISO 27001
slug: payfit
tags:
- Payroll
- Human Resources
- HR Tech
- Europe Payroll
- Time and Attendance
- Employee Management
website: https://payfit.com
---

---
access_model:
  confidence: high
  label: Customer-only; key issued by an Insperity Integration Specialist behind an IP allow-list
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developer.insperity.com/get-started
  - https://developer.insperity.com/api/swagger/payroll_tax
  trial: false
  try_now: false
api_count: 4
apis:
- description: Use your own applicant tracking or HR application to send candidate hire information to Insperity Premier Onboarding. One published operation, POST /public/Employee/Onboarding/v2, which accepts a call
  name: Insperity Onboarding API
  slug: insperity-onboarding-api
- description: Update an employee's compensation and retrieve general ledger information post payroll. Three published operations covering billing group changes, remuneration changes and the payroll ledger read.
  name: Insperity Payroll & Tax API
  slug: insperity-payroll-tax-api
- description: Transfer employee information to and from Insperity Premier. Twenty-six published operations — fifteen named employee change events written as POSTs (address, email, phone, department, location, super
  name: Insperity HRIS API
  slug: insperity-hris-api
- description: Company-scoped reference data. Some Insperity API fields require specific values as defined in Insperity Premier, and the Core APIs return the list of accepted options — benefit classes, billing group
  name: Insperity Core API
  slug: insperity-core-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.insperity.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/insperity
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.insperity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.insperity.com/developer-resources
- group: docs
  title: ''
  type: APIReference
  url: https://developer.insperity.com/categories
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.insperity.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://developer.insperity.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.insperity.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.insperity.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/insperity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/insperity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/insperity-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/insperity-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/insperity-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/insperity-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/insperity-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/insperity-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/insperity-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/insperity-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/insperity-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insperity-domain-security.yml
created: '2026-04-28'
description: 'Insperity is a professional employer organization (PEO) headquartered in Kingwood, Texas that provides human resources and business performance solutions to small and medium-sized businesses, including payroll processing, employee benefits, workers'' compensation, HR compliance and the Insperity Premier HR technology platform. Insperity Premier exposes a REST Public API at https://api.insperity.com/public organized into four categories — Onboarding, Payroll & Tax, HRIS and Core — covering 45 publicly listed operations that let a client''s applicant tracking system, HRIS or payroll application send new-hire records, submit employee change events, retrieve post-payroll general ledger data, and read the company-scoped reference code lists those writes must resolve against. Access is not self-service: a key is issued per customer by an Insperity Integration Specialist after an API Terms of Use Agreement is signed, requests must originate from allow-listed IP addresses, and the
  developer portal''s Swagger documents require a Premier account.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/insperity.png
layout: provider
modified: '2026-09-13'
name: Insperity
nav: Providers
network: true
overview: 'Insperity publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Human Resources, Payroll, Benefits, and HRIS.


  Insperity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 14 more developer resources.'
plans:
- name: Insperity Plans Pricing
  plan_count: 0
  slug: insperity-plans-pricing
press:
- date: '2026-05-25'
  title: 'Artificial Intelligence (AI) At Work: What You Need To Know'
  url: https://www.insperity.com/blog/artificial-intelligence-ai-at-work-what-you-need-to-know/
- date: '2026-05-25'
  title: Insperity Archives - NSCA
  url: https://www.nsca.org/tag/insperity/
- date: '2026-05-25'
  title: 'Earnings call transcript: Insperity Q1 2026 earnings miss ...'
  url: https://www.investing.com/news/transcripts/earnings-call-transcript-insperity-q1-2026-earnings-miss-forecast-stock-dips-93CH-4651652
- date: '2026-05-25'
  title: Business Outlook Report 2024
  url: https://www.insperity.com/resources/guide/business-outlook-report/
- date: '2026-05-25'
  title: Workday and Insperity Announce Exclusive Strategic ...
  url: https://newsroom.workday.com/2024-02-08-Workday-and-Insperity-Announce-Exclusive-Strategic-Partnership-to-Provide-Best-in-Class-HR-Service-and-Technology-to-Small-and-Midsize-Businesses
random_paper: 12
rate_limits:
- limit_count: 0
  name: Insperity Rate Limits
  slug: insperity-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/insperity/refs/heads/main/screenshots/insperity-2026-06-20T183405.png
security:
- kind: authentication
  name: Insperity Authentication
  slug: insperity-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Insperity Domain Security
  slug: insperity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: insperity
tags:
- Fortune 1000
- Human Resources
- Payroll
- Benefits
- HRIS
- Onboarding
- Professional Employer Organization
- Workforce Management
- Employer of Record
website: https://www.insperity.com
---

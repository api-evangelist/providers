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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: The TriNet Company API provides access to company-level HR data including organizational structure, departments, holiday schedules, workers compensation codes, and company configuration. Used by HR ad
  name: TriNet Company API
  slug: company-api
- description: The TriNet Employees API provides full lifecycle employee data management including retrieving all employee details, adding new employees (onboarding), and managing employee records. Supports HR workf
  name: TriNet Employees API
  slug: employees-api
- description: 'The TriNet Payroll API provides access to employee payroll and compensation data including pay rates, pay frequency, bonuses, and additional pay components. Enables integration with financial systems '
  name: TriNet Payroll API
  slug: payroll-api
- description: The TriNet Identity API provides access to employee identity and sensitive personally identifiable information (PII) such as Social Security Numbers for authorized systems. Access is strictly scoped a
  name: TriNet Identity API
  slug: identity-api
- description: The TriNet Manage Employee API enables management of employee roles and access permissions within the TriNet platform. Supports HR administrators in assigning, updating, and auditing employee roles fo
  name: TriNet Manage Employee API
  slug: manage-employee-api
artifact_total: 37
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trinet-group-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.trinet.com/insights
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trinet
- group: company
  title: ''
  type: Website
  url: https://www.trinet.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.trinet.com/home
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.trinet.com/home
- group: auth
  title: ''
  type: Authentication
  url: https://apidocs.trinet.com/oauth-scopes
- group: company
  title: ''
  type: PartnerProgram
  url: https://www.trinet.com/hr-services/technology-platform/integration-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trinet.com/privacy-policy
created: '2026-03-24'
description: TriNet Group is a professional employer organization (PEO) providing small and midsize businesses with full-service human resources solutions including payroll processing, employee benefits administration, risk management, compliance, and HR technology. TriNet serves over 16,000 companies and 340,000 worksite employees across verticals including technology, financial services, life sciences, professional services, and nonprofits.
features:
- name: Payroll Processing
- name: Benefits Administration
- name: Risk Management
- name: Compliance Support
- name: HR Technology Platform
- name: Employee Onboarding
- name: Time and Attendance
- name: Workers Compensation
- name: Expense Management
- name: Performance Management
- name: Learning and Development
- name: QuickBooks Online Integration
finops:
- name: Trinet Group Finops
  service_category: HR / PEO
  slug: trinet-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trinet-group.png
integrations:
- name: QuickBooks Online
- name: Salesforce
- name: Slack
- name: Microsoft Teams
- name: Google Workspace
- name: Okta
- name: Finch
- name: Merge
- name: Apideck
layout: provider
modified: '2026-05-03'
name: TriNet Group
nav: Providers
network: true
overview: 'TriNet Group publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Benefits, Compliance, Human Resources, Payroll, and Professional Employer Organization.


  TriNet Group''s developer surface includes engineering blog, documentation, authentication, and 6 more developer resources.'
plans:
- name: Trinet Group Plans Pricing
  plan_count: 1
  slug: trinet-group-plans-pricing
press:
- date: '2026-05-25'
  title: TriNet posts 2025 results and sets 2026 guidance
  url: https://www.stocktitan.net/sec-filings/TNET/8-k-trinet-group-inc-reports-material-event-76bc25bed174.html
- date: '2026-05-25'
  title: TriNet Announces First Quarter 2026 Results
  url: https://www.prnewswire.com/news-releases/trinet-announces-first-quarter-2026-results-302758367.html
- date: '2026-05-25'
  title: AI-Powered HR Technology
  url: https://www.trinet.com/hr-services/technology-platform/ai
- date: '2026-05-25'
  title: TriNet to Launch AI-Powered Suite of Offerings to Empower ...
  url: https://www.trinet.com/about-us/news-press/press-releases/trinet-to-launch-ai-powered-suite-of-offerings-to-empower-smbs-with-personalized-data-driven-hr-support
- date: '2026-05-25'
  title: TriNet to launch AI-powered HR suite for small businesses
  url: https://www.investing.com/news/company-news/trinet-to-launch-aipowered-hr-suite-for-small-businesses-93CH-4302017
random_paper: 4
rate_limits:
- limit_count: 1
  name: Trinet Group Rate Limits
  slug: trinet-group-rate-limits
score:
  band: emerging
  composite: 16.4
  delta: -2.5
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 18.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trinet-group/refs/heads/main/screenshots/trinet-group-2026-06-20T195719.png
security:
- kind: domain-security
  name: Trinet Group Domain Security
  slug: trinet-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trinet-group
tags:
- Benefits
- Compliance
- Human Resources
- Payroll
- Professional Employer Organization
- Risk Management
- Fortune 1000
use_cases:
- name: Employee Data Sync
- name: Payroll Integration
- name: Benefits Enrollment Automation
- name: HR System Integration
- name: Compliance Reporting
- name: Onboarding Automation
- name: Headcount Reporting
website: https://www.trinet.com
---

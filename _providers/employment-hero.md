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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Employment Hero Agentic Access
  operation_count: 24
  slug: employment-hero-agentic-access
  summary_line: 24 operations · 9 acting
api_count: 12
apis:
- description: Versioned REST API (v1) for accessing Employment Hero HR, payroll, and employee data including organisations, employees, teams, leave, pay runs, and onboarding. Apps register through the Developer Por
  name: Employment Hero REST API
  slug: rest-api
- description: Employment Hero Payroll (formerly KeyPay) REST API for managing businesses, employees, pay runs, leave, timesheets, super, tax, and reporting across the AU, UK, NZ, and SG payroll regions.
  name: Employment Hero Payroll API (KeyPay)
  slug: payroll-api
- description: The Bank Accounts API from Employment Hero — 1 operation(s) for bank accounts.
  name: Employment Hero Bank Accounts API
  slug: employment-hero-bank-accounts-api
- description: The Certifications API from Employment Hero — 5 operation(s) for certifications.
  name: Employment Hero Certifications API
  slug: employment-hero-certifications-api
- description: The Cost Centres API from Employment Hero — 1 operation(s) for cost centres.
  name: Employment Hero Cost Centres API
  slug: employment-hero-cost-centres-api
- description: The Custom Fields API from Employment Hero — 1 operation(s) for custom fields.
  name: Employment Hero Custom Fields API
  slug: employment-hero-custom-fields-api
- description: The Departments API from Employment Hero — 2 operation(s) for departments.
  name: Employment Hero Departments API
  slug: employment-hero-departments-api
- description: The Documents API from Employment Hero — 1 operation(s) for documents.
  name: Employment Hero Documents API
  slug: employment-hero-documents-api
- description: The Emergency Contacts API from Employment Hero — 1 operation(s) for emergency contacts.
  name: Employment Hero Emergency Contacts API
  slug: employment-hero-emergency-contacts-api
- description: The Employees API from Employment Hero — 3 operation(s) for employees.
  name: Employment Hero Employees API
  slug: employment-hero-employees-api
- description: The Forms API from Employment Hero — 4 operation(s) for forms.
  name: Employment Hero Forms API
  slug: employment-hero-forms-api
- description: The Job Histories API from Employment Hero — 1 operation(s) for job histories.
  name: Employment Hero Job Histories API
  slug: employment-hero-job-histories-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Employment Hero REST Bank Accounts API
  slug: open-employment-hero-bank-accounts-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Certifications API
  slug: open-employment-hero-certifications-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Cost Centres API
  slug: open-employment-hero-cost-centres-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Custom Fields API
  slug: open-employment-hero-custom-fields-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Departments API
  slug: open-employment-hero-departments-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Documents API
  slug: open-employment-hero-documents-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Emergency Contacts API
  slug: open-employment-hero-emergency-contacts-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Employees API
  slug: open-employment-hero-employees-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Forms API
  slug: open-employment-hero-forms-api
- collection_type: open
  name: Employment Hero REST Bank Accounts Job Histories API
  slug: open-employment-hero-job-histories-api
- collection_type: open
  name: Employment Hero REST API
  slug: open-employment-hero
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/employment-hero-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/employment-hero-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/employment-hero-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/employment-hero-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/employment-hero-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Thinkei
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/employment-hero
- group: company
  title: ''
  type: Website
  url: https://employmenthero.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.employmenthero.com
- group: docs
  title: ''
  type: API Documentation
  url: https://developer.employmenthero.com/api-references
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.employmenthero.com
- group: commercial
  title: ''
  type: Pricing
  url: https://employmenthero.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://employmenthero.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://employmenthero.com/feed/
created: '2026-05-11'
description: Employment Hero is an AI-powered Employment Operating System for Australian and international businesses combining HR, payroll, recruitment, onboarding, learning, and employee benefits into a single platform. The product covers policy management, automated workflows, AI-assisted hiring, an employee mobile app, and the HeroForce managed employment service. The Employment Hero API is a versioned REST API authenticated via OAuth 2.0 with short- lived (15-minute) access tokens and refresh tokens.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/employment-hero.png
layout: provider
modified: '2026-05-11'
name: Employment Hero
nav: Providers
network: true
overview: 'Employment Hero publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Bank Accounts API, Certifications API, Cost Centres API, and 7 more. Tagged areas include HR, HRIS, Payroll, Recruitment, and Employee Benefits.


  Employment Hero''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 9 more developer resources.'
random_paper: 83
scopes:
- name: Employment Hero Scopes
  scope_count: 0
  slug: employment-hero-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.8
  delta: -0.5
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 40.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/employment-hero/refs/heads/main/screenshots/employment-hero-2026-06-20T180642.png
security:
- kind: authentication
  name: Employment Hero Authentication
  slug: employment-hero-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Employment Hero Domain Security
  slug: employment-hero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Employment Hero Vulnerability Disclosure
  slug: employment-hero-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: employment-hero
tags:
- HR
- HRIS
- Payroll
- Recruitment
- Employee Benefits
- Workforce Management
- HR Tech
website: https://employmenthero.com
---

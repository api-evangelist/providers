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
- acting_count: 6
  human_in_the_loop: 0
  name: Breathe Hr Agentic Access
  operation_count: 15
  slug: breathe-hr-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 6
apis:
- description: JSON REST API for managing employees, absences, holidays, sick leaves, accounts, and related HR records inside Breathe. Calls require an X-API-KEY header containing the account-level token generated f
  name: Breathe HR REST API
  slug: rest-api
- description: The Absences API from Breathe HR — 2 operation(s) for absences.
  name: Breathe HR Absences API
  slug: breathe-hr-absences-api
- description: The Account API from Breathe HR — 1 operation(s) for account.
  name: Breathe HR Account API
  slug: breathe-hr-account-api
- description: The Employees API from Breathe HR — 2 operation(s) for employees.
  name: Breathe HR Employees API
  slug: breathe-hr-employees-api
- description: The Holidays API from Breathe HR — 2 operation(s) for holidays.
  name: Breathe HR Holidays API
  slug: breathe-hr-holidays-api
- description: The Sicknesses API from Breathe HR — 2 operation(s) for sicknesses.
  name: Breathe HR Sicknesses API
  slug: breathe-hr-sicknesses-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Breathe HR REST Absences API
  slug: open-breathe-hr-absences-api
- collection_type: open
  name: Breathe HR REST Absences Account API
  slug: open-breathe-hr-account-api
- collection_type: open
  name: Breathe HR REST Absences Employees API
  slug: open-breathe-hr-employees-api
- collection_type: open
  name: Breathe HR REST Absences Holidays API
  slug: open-breathe-hr-holidays-api
- collection_type: open
  name: Breathe HR REST Absences Sicknesses API
  slug: open-breathe-hr-sicknesses-api
- collection_type: open
  name: Breathe HR REST API
  slug: open-breathe-hr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/breathe-hr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/breathe-hr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/breathe-hr-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.breathehr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.breathehr.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.breathehr.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.breathehr.com/en-gb/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.breathehr.com/en-gb/free-trial
- group: other
  title: ''
  type: Knowledge Base
  url: https://intercom.help/breathehr/en
- group: operate
  title: ''
  type: Support
  url: mailto:support@breathehr.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/breathehr
created: '2026-05-11'
description: Breathe is a UK-headquartered cloud HRIS designed for small and midsize businesses, covering employee records, holiday and sickness tracking, performance, documents, expenses, and rota scheduling. The Breathe API is a REST/JSON service that exposes employee, absence, account, and related HR resources for integration with payroll, identity, and analytics tools. Authentication uses a per-account API key passed in the X-API-KEY header against a production base URL of https://api.breathehr.com/v1 with a sandbox available at https://api.sandbox.breathehr.com/v1.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/breathe-hr.png
layout: provider
modified: '2026-05-11'
name: Breathe HR
nav: Providers
network: true
overview: 'Breathe HR publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Absences API, Account API, Employees API, and 2 more. Tagged areas include HR, HRIS, Human Resources, Employee Management, and Absence Management.


  Breathe HR''s developer surface includes authentication, documentation, pricing, signup flow, support, and 6 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 31.0
  delta: -1.5
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/breathe-hr/refs/heads/main/screenshots/breathe-hr-2026-06-20T173649.png
security:
- kind: authentication
  name: Breathe Hr Authentication
  slug: breathe-hr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Breathe Hr Domain Security
  slug: breathe-hr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: breathe-hr
tags:
- HR
- HRIS
- Human Resources
- Employee Management
- Absence Management
- Holiday Tracking
- SMB
- UK
website: https://www.breathehr.com
---

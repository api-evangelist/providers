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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Workmotion Agentic Access
  operation_count: 20
  slug: workmotion-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 7
apis:
- description: Time-off and leave management.
  name: WorkMotion Absences API
  slug: workmotion-absences-api
- description: Employment contracts and contract changes.
  name: WorkMotion Contracts API
  slug: workmotion-contracts-api
- description: Employment cost estimation by country.
  name: WorkMotion Cost Calculator API
  slug: workmotion-cost-calculator-api
- description: Employment documents attached to a talent.
  name: WorkMotion Documents API
  slug: workmotion-documents-api
- description: Talents employed through WorkMotion.
  name: WorkMotion Employees API
  slug: workmotion-employees-api
- description: Accelerated global onboarding workflows.
  name: WorkMotion Onboarding API
  slug: workmotion-onboarding-api
- description: Event subscription management.
  name: WorkMotion Webhooks API
  slug: workmotion-webhooks-api
artifact_total: 14
collections:
- collection_type: open
  name: WorkMotion Partner API
  slug: open-workmotion
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workmotion-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workmotion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workmotion-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.workmotion.com/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/workmotion
- group: company
  title: ''
  type: Website
  url: https://www.workmotion.com
- group: docs
  title: ''
  type: Documentation
  url: https://workmotion.com/integrations/
- group: commercial
  title: ''
  type: Plans
  url: plans/workmotion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/workmotion-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/workmotion-finops.yml
created: '2026-07-01'
description: WorkMotion is a global employment and Employer of Record (EOR) platform that lets companies compliantly hire, onboard, and pay international employees and contractors across 160+ countries. Its partner/Open API surfaces employee and contract data, onboarding workflows, absences and time-off, documents, employment cost calculations, and webhooks so HRIS and payroll systems can integrate with WorkMotion's managed employment infrastructure.
finops:
- name: Workmotion Finops
  service_category: Human Resources
  slug: workmotion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workmotion.png
layout: provider
modified: '2026-07-01'
name: WorkMotion
nav: Providers
network: true
overview: 'WorkMotion publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Absences API, Contracts API, Cost Calculator API, and 4 more. Tagged areas include Employer of Record, EOR, Global Employment, HR, and Payroll.


  WorkMotion''s developer surface includes authentication, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Workmotion Plans Pricing
  plan_count: 4
  slug: workmotion-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 2
  name: Workmotion Rate Limits
  slug: workmotion-rate-limits
score:
  band: thin
  composite: 35.7
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Workmotion Authentication
  slug: workmotion-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Workmotion Domain Security
  slug: workmotion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: workmotion
tags:
- Employer of Record
- EOR
- Global Employment
- HR
- Payroll
- Onboarding
- Contractors
- Compliance
website: https://www.workmotion.com
---

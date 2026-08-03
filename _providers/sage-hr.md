---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 25
  human_in_the_loop: 2
  name: Sage Hr Agentic Access
  operation_count: 53
  slug: sage-hr-agentic-access
  summary_line: 53 operations · 25 acting · 2 human-in-the-loop
api_count: 14
apis:
- description: The Documents API from Sage HR — 2 operation(s) for documents.
  name: Sage HR Documents API
  slug: sage-hr-documents-api
- description: The Employee API from Sage HR — 9 operation(s) for employee.
  name: Sage HR Employee API
  slug: sage-hr-employee-api
- description: The Integrations API from Sage HR — 12 operation(s) for integrations.
  name: Sage HR Integrations API
  slug: sage-hr-integrations-api
- description: The KIT days API from Sage HR — 3 operation(s) for kit days.
  name: Sage HR KIT days API
  slug: sage-hr-kit-days-api
- description: The Leave management API from Sage HR — 8 operation(s) for leave management.
  name: Sage HR Leave management API
  slug: sage-hr-leave-management-api
- description: The Offboarding API from Sage HR — 2 operation(s) for offboarding.
  name: Sage HR Offboarding API
  slug: sage-hr-offboarding-api
- description: The Onboarding API from Sage HR — 2 operation(s) for onboarding.
  name: Sage HR Onboarding API
  slug: sage-hr-onboarding-api
- description: The Performance API from Sage HR — 4 operation(s) for performance.
  name: Sage HR Performance API
  slug: sage-hr-performance-api
- description: The Policies API from Sage HR — 2 operation(s) for policies.
  name: Sage HR Policies API
  slug: sage-hr-policies-api
- description: The Positions API from Sage HR — 1 operation(s) for positions.
  name: Sage HR Positions API
  slug: sage-hr-positions-api
- description: The Recruitment API from Sage HR — 5 operation(s) for recruitment.
  name: Sage HR Recruitment API
  slug: sage-hr-recruitment-api
- description: The Teams API from Sage HR — 1 operation(s) for teams.
  name: Sage HR Teams API
  slug: sage-hr-teams-api
- description: The Terminations reasons API from Sage HR — 1 operation(s) for terminations reasons.
  name: Sage HR Terminations reasons API
  slug: sage-hr-terminations-reasons-api
- description: The Timesheets API from Sage HR — 1 operation(s) for timesheets.
  name: Sage HR Timesheets API
  slug: sage-hr-timesheets-api
artifact_total: 25
collections:
- collection_type: open
  name: Sage HR API
  slug: open-sage-hr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sage-hr-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sage-hr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sage-hr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sage-hr-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://sage.hr/
- group: start
  title: ''
  type: Portal
  url: https://www.sage.com/en-gb/sage-business-cloud/hr/
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.sage.hr/
- group: docs
  title: ''
  type: Documentation
  url: https://support.sage.hr/en/articles/3246469-how-does-cakehr-api-work
- group: operate
  title: ''
  type: Support
  url: https://support.sage.hr/
- group: commercial
  title: ''
  type: Pricing
  url: https://sage.hr/pricing/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sage-hr/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sagehr
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Sage
- group: commercial
  title: ''
  type: Plans
  url: plans/sage-hr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sage-hr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sage-hr-finops.yml
created: '2026-05-25'
description: Sage HR (formerly CakeHR) is a cloud HRIS for small and mid-sized businesses, owned by Sage Group plc. It bundles core HR records, leave management, performance, recruitment (ATS), timesheets, shift scheduling, expenses, and onboarding/offboarding into a modular per-employee SaaS. The Sage HR REST API at apidoc.sage.hr exposes 53 operations across employees, leave, recruitment, performance, timesheets, documents, onboarding, offboarding, organization, and a Vikarina payroll integration bridge. Authentication is a tenant-scoped X-Auth-Token API key against the customer's own subdomain (https://{subdomain}.sage.hr/api).
finops:
- name: Sage Hr Finops
  service_category: Business Applications - HR
  slug: sage-hr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sage-hr.png
json_schemas:
- name: Sage HR Employee
  property_count: 26
  slug: sage-hr-employee
jsonld:
- class_count: 0
  name: Sage Hr Context
  property_count: 7
  slug: sage-hr-context
layout: provider
modified: '2026-05-25'
name: Sage HR
nav: Providers
network: true
overview: 'Sage HR publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Employee API, Integrations API, and 11 more. Tagged areas include HR, HRIS, People, SMB, and Leave Management.


  The Sage HR catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sage HR''s developer surface includes authentication, developer portal, documentation, support, pricing, GitHub presence, and 10 more developer resources.'
plans:
- name: Sage Hr Plans Pricing
  plan_count: 6
  slug: sage-hr-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Sage Hr Rate Limits
  slug: sage-hr-rate-limits
rules:
- name: Sage HR API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sage-hr-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.1
    developer_ergonomics: 32.6
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sage-hr/refs/heads/main/screenshots/sage-hr-2026-06-20T193324.png
security:
- kind: authentication
  name: Sage Hr Authentication
  slug: sage-hr-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sage Hr Domain Security
  slug: sage-hr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sage Hr Vulnerability Disclosure
  slug: sage-hr-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sage-hr
tags:
- HR
- HRIS
- People
- SMB
- Leave Management
- Recruitment
- Performance
- Timesheets
- Onboarding
website: https://sage.hr/
---

---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 0
  human_in_the_loop: 0
  name: Charliehr Agentic Access
  operation_count: 13
  slug: charliehr-agentic-access
  summary_line: 13 operations
api_count: 4
apis:
- description: Company record, offices, and teams.
  name: CharlieHR Company API
  slug: charliehr-company-api
- description: Leave (time off) requests.
  name: CharlieHR Leave / Absences API
  slug: charliehr-leave-absences-api
- description: Leave allowance balances.
  name: CharlieHR Leave Allowances API
  slug: charliehr-leave-allowances-api
- description: Company team members and their notes.
  name: CharlieHR Team Members API
  slug: charliehr-team-members-api
artifact_total: 13
collections:
- collection_type: open
  name: CharlieHR API
  slug: open-charliehr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/charliehr-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/charliehr-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/charliehr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/charliehr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/charliehr-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CharlieHR
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/charliehr
- group: company
  title: ''
  type: Website
  url: https://www.charliehr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.charliehr.com/api_docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/charliehr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/charliehr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/charliehr-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.charliehr.com/blog
created: '2026-06-21'
description: CharlieHR is a small-business HR platform that handles people management, time off, onboarding, and employee records. Its REST API exposes a company's team members, leave requests, leave allowances, and company structure (offices and teams) using OAuth 2.0 client credentials over HTTPS.
finops:
- name: Charliehr Finops
  service_category: Business Applications
  slug: charliehr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/charliehr.png
layout: provider
modified: '2026-06-21'
name: CharlieHR
nav: Providers
network: true
overview: 'CharlieHR publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Company API, Leave / Absences API, Leave Allowances API, and 1 more. Tagged areas include HR, HRIS, People, Leave, and Time Off.


  CharlieHR''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Charliehr Plans Pricing
  plan_count: 4
  slug: charliehr-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 2
  name: Charliehr Rate Limits
  slug: charliehr-rate-limits
scopes:
- name: Charliehr Scopes
  scope_count: 0
  slug: charliehr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.7
  delta: -3.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/charliehr/refs/heads/main/screenshots/charliehr-2026-07-25T205104.png
security:
- kind: authentication
  name: Charliehr Authentication
  slug: charliehr-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Charliehr Domain Security
  slug: charliehr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Charliehr Trust Center
  slug: charliehr-trust-center
  summary_line: ISO 27001, GDPR
slug: charliehr
tags:
- HR
- HRIS
- People
- Leave
- Time Off
website: https://www.charliehr.com/
---

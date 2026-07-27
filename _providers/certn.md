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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Certn Agentic Access
  operation_count: 14
  slug: certn-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 6
apis:
- description: Invite or instantly screen applicants and list applications (HR and PM surfaces).
  name: Certn Applications API
  slug: certn-applications-api
- description: Individual check types requested and returned within an application.
  name: Certn Checks API
  slug: certn-checks-api
- description: Predefined bundles of checks and application upgrades.
  name: Certn Packages API
  slug: certn-packages-api
- description: Consolidated applicant screening reports and results.
  name: Certn Reports API
  slug: certn-reports-api
- description: Organizational hierarchy - Superteams, Teams, Users, reference templates.
  name: Certn Teams and Users API
  slug: certn-teams-and-users-api
- description: Signed server-to-server callbacks for screening status updates.
  name: Certn Webhooks API
  slug: certn-webhooks-api
artifact_total: 14
collections:
- collection_type: open
  name: Certn API
  slug: open-certn
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/certn-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/certn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/certn-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/certn-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Certn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/certn
- group: company
  title: ''
  type: Website
  url: https://certn.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.certn.co/api
- group: commercial
  title: ''
  type: Plans
  url: plans/certn-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/certn-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/certn-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://certn.co/blog/feed
created: '2026-07-03'
description: Certn is a Canada-based, globally operating background check and identity verification platform. Its RESTful API lets HR, property management, gig, and marketplace platforms order and retrieve criminal record checks, identity verification, credit, employment, education, credential, and reference checks across 200+ countries, then receive results and adjudicated reports. The API authenticates with OAuth 2.0 client credentials (Client ID / Client Secret exchanged for a Bearer token) and pushes status updates via signed webhooks. The original api.certn.co v1 REST API is deprecated (discontinued 2026-08-05) in favor of the newer CertnCentric APIs; both are modeled here honestly.
finops:
- name: Certn Finops
  service_category: Identity and Background Screening
  slug: certn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/certn.png
layout: provider
modified: '2026-07-03'
name: Certn
nav: Providers
network: true
overview: 'Certn publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Checks API, Packages API, and 3 more. Tagged areas include Background Checks, Identity Verification, Criminal Record Check, Screening, and HR Tech.


  Certn''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Certn Plans Pricing
  plan_count: 4
  slug: certn-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 3
  name: Certn Rate Limits
  slug: certn-rate-limits
score:
  band: thin
  composite: 41.5
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.8
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/certn/refs/heads/main/screenshots/certn-2026-07-25T205011.png
security:
- kind: authentication
  name: Certn Authentication
  slug: certn-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Certn Domain Security
  slug: certn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Certn Vulnerability Disclosure
  slug: certn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: certn
tags:
- Background Checks
- Identity Verification
- Criminal Record Check
- Screening
- HR Tech
- Compliance
- Trust and Safety
website: https://certn.co
---

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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Certn Agentic Access
  operation_count: 14
  slug: certn-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 1
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
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Certn Applications API
  slug: open-certn-applications-api
- collection_type: open
  name: Certn Applications Checks API
  slug: open-certn-checks-api
- collection_type: open
  name: Certn Applications Packages API
  slug: open-certn-packages-api
- collection_type: open
  name: Certn Applications Reports API
  slug: open-certn-reports-api
- collection_type: open
  name: Certn Applications Teams and Users API
  slug: open-certn-teams-and-users-api
- collection_type: open
  name: Certn Applications Webhooks API
  slug: open-certn-webhooks-api
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
random_paper: 15
rate_limits:
- limit_count: 3
  name: Certn Rate Limits
  slug: certn-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 42.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 33.3
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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

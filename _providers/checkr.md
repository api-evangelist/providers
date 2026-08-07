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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Checkr Agentic Access
  operation_count: 60
  slug: checkr-agentic-access
  summary_line: 60 operations · 25 acting
api_count: 14
apis:
- description: Account and user metadata.
  name: Checkr Account API
  slug: checkr-account-api
- description: FCRA adverse action workflows against a report.
  name: Checkr Adverse Actions API
  slug: checkr-adverse-actions-api
- description: Candidate records that background checks are run against.
  name: Checkr Candidates API
  slug: checkr-candidates-api
- description: Ongoing monitoring for new records.
  name: Checkr Continuous Checks API
  slug: checkr-continuous-checks-api
- description: Files attached to a candidate.
  name: Checkr Documents API
  slug: checkr-documents-api
- description: State/locale definitions scoping pricing and compliance.
  name: Checkr Geos API
  slug: checkr-geos-api
- description: Hosted invitations for candidates to submit their own information.
  name: Checkr Invitations API
  slug: checkr-invitations-api
- description: Tree of nodes modeling account/organization structure.
  name: Checkr Nodes and Hierarchy API
  slug: checkr-nodes-and-hierarchy-api
- description: Bundles of screenings and the programs that group them.
  name: Checkr Packages API
  slug: checkr-packages-api
- description: The container aggregating a candidate's screenings and result.
  name: Checkr Reports API
  slug: checkr-reports-api
- description: Individual screening components nested under a report.
  name: Checkr Screenings API
  slug: checkr-screenings-api
- description: Recurring re-runs of a package for a candidate.
  name: Checkr Subscriptions API
  slug: checkr-subscriptions-api
- description: Education and employment verification screenings.
  name: Checkr Verifications API
  slug: checkr-verifications-api
- description: Event notification subscriptions.
  name: Checkr Webhooks API
  slug: checkr-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: Checkr API
  slug: open-checkr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/checkr-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/checkr-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/checkr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/checkr-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/checkr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/checkr
- group: company
  title: ''
  type: Website
  url: https://checkr.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.checkr.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/checkr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/checkr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/checkr-finops.yml
created: '2026-07-03'
description: Checkr is a technology-driven background check platform for employment screening. Its REST API lets employers, staffing firms, and platform partners run compliant background checks programmatically - creating candidates, sending invitations, ordering packages, and retrieving reports composed of individual screenings (SSN trace, county/state/national/federal criminal searches, sex offender registry, motor vehicle records, education and employment verifications, and more). The API also covers adverse action workflows, continuous checks and subscriptions, node/hierarchy and geo account structure, Form I-9, documents, and webhooks for event-driven report status updates. Authentication is HTTP Basic auth with a secret API key, with OAuth for Checkr Partner integrations.
finops:
- name: Checkr Finops
  service_category: Background Screening and Compliance
  slug: checkr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/checkr.png
layout: provider
modified: '2026-07-03'
name: Checkr
nav: Providers
network: true
overview: 'Checkr publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account API, Adverse Actions API, Candidates API, and 11 more. Tagged areas include Background Checks, Employment Screening, Compliance, HR Tech, and Identity Verification.


  Checkr''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Checkr Plans Pricing
  plan_count: 5
  slug: checkr-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 2
  name: Checkr Rate Limits
  slug: checkr-rate-limits
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 56.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/checkr/refs/heads/main/screenshots/checkr-2026-07-25T205136.png
security:
- kind: authentication
  name: Checkr Authentication
  slug: checkr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Checkr Domain Security
  slug: checkr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Checkr Trust Center
  slug: checkr-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: checkr
tags:
- Background Checks
- Employment Screening
- Compliance
- HR Tech
- Identity Verification
- Criminal Records
website: https://checkr.com
---

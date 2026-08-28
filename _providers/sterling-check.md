---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Sterling Check Agentic Access
  operation_count: 15
  slug: sterling-check-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 7
apis:
- description: OAuth2 token exchange using your Client ID and Client Secret.
  name: Sterling Authentication API
  slug: sterling-check-authentication-api
- description: Candidate (subject) records that screenings are run against.
  name: Sterling Candidates API
  slug: sterling-check-candidates-api
- description: Candidate invitations to complete consent and data collection.
  name: Sterling Invites API
  slug: sterling-check-invites-api
- description: Screening packages (groups of screening products) available to your account.
  name: Sterling Packages API
  slug: sterling-check-packages-api
- description: Results of completed screenings, with per-item statuses (PDF or HTML).
  name: Sterling Reports API
  slug: sterling-check-reports-api
- description: Screening orders and their lifecycle, including recurring/continuous screening.
  name: Sterling Screenings API
  slug: sterling-check-screenings-api
- description: Real-time screening status callbacks.
  name: Sterling Webhooks API
  slug: sterling-check-webhooks-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sterling Authentication API
  slug: open-sterling-check-authentication-api
- collection_type: open
  name: Sterling Authentication Candidates API
  slug: open-sterling-check-candidates-api
- collection_type: open
  name: Sterling Authentication Invites API
  slug: open-sterling-check-invites-api
- collection_type: open
  name: Sterling Authentication Packages API
  slug: open-sterling-check-packages-api
- collection_type: open
  name: Sterling Authentication Reports API
  slug: open-sterling-check-reports-api
- collection_type: open
  name: Sterling Authentication Screenings API
  slug: open-sterling-check-screenings-api
- collection_type: open
  name: Sterling Authentication Webhooks API
  slug: open-sterling-check-webhooks-api
- collection_type: open
  name: Sterling API
  slug: open-sterling-check
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sterling-check-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sterling-check-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sterling-check-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sterling-check-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sterlingcheck
- group: company
  title: ''
  type: Website
  url: https://www.sterlingcheck.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.sterlingcheck.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sterlingcheck.app/
- group: commercial
  title: ''
  type: Plans
  url: plans/sterling-check-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sterling-check-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sterling-check-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://fadv.com/resources/news/
created: '2026-07-03'
description: Sterling (Sterling Check Corp) is a global background and identity screening provider offering criminal checks, employment and education verifications, drug and health screening, identity verification, and continuous (recurring) monitoring. The Sterling API is a documented RESTful, OAuth2-secured developer API that lets platforms, ATS/HRIS systems, and marketplaces initiate background checks, manage candidates and screening packages, retrieve results and reports (PDF/HTML), send candidate invites, and receive real-time status updates via webhook callbacks. Access is gated - developers request a Client ID and Client Secret per screening region (US, EMEA, Canada, or APAC) - and the docs are published via a Postman-hosted portal at apidocs.sterlingcheck.app with a developer portal at developer.sterlingcheck.app. Sterling was acquired by First Advantage Corporation for $2.2 billion, with the deal closing on October 31, 2024; Sterling now operates as "a First Advantage company."
finops:
- name: Sterling Check Finops
  service_category: Background and Identity Screening
  slug: sterling-check-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sterling-check.png
layout: provider
modified: '2026-07-03'
name: Sterling
nav: Providers
network: true
overview: 'Sterling publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Candidates API, Invites API, and 4 more. Tagged areas include Background Screening, Identity Verification, Background Check, HR Tech, and Compliance.


  Sterling''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Sterling Check Plans Pricing
  plan_count: 3
  slug: sterling-check-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Sterling Check Rate Limits
  slug: sterling-check-rate-limits
scopes:
- name: Sterling Check Scopes
  scope_count: 0
  slug: sterling-check-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.0
  delta: 1.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Sterling Check Authentication
  slug: sterling-check-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Sterling Check Domain Security
  slug: sterling-check-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sterling-check
tags:
- Background Screening
- Identity Verification
- Background Check
- HR Tech
- Compliance
- Gated API
website: https://www.sterlingcheck.com
---

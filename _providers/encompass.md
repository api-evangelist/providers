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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Encompass Agentic Access
  operation_count: 43
  slug: encompass-agentic-access
  summary_line: 43 operations · 21 acting
api_count: 1
apis:
- description: OAuth 2.0 token issuance.
  name: Encompass Authentication API
  slug: encompass-authentication-api
- description: Borrower/co-borrower application entities within a loan (modeled).
  name: Encompass Borrower Pairs API
  slug: encompass-borrower-pairs-api
- description: Underwriting, preliminary, and post-closing conditions (modeled).
  name: Encompass Conditions API
  slug: encompass-conditions-api
- description: Borrower (consumer) and business contacts (modeled).
  name: Encompass Contacts API
  slug: encompass-contacts-api
- description: Documents and attachments in a loan's eFolder.
  name: Encompass eFolder API
  slug: encompass-efolder-api
- description: Create, read, update, and delete Encompass loan files and loan data.
  name: Encompass Loan Management API
  slug: encompass-loan-management-api
- description: Search loans and loan fields across the pipeline with cursor pagination.
  name: Encompass Loan Pipeline API
  slug: encompass-loan-pipeline-api
- description: Loan workflow milestones and associates (modeled).
  name: Encompass Milestones API
  slug: encompass-milestones-api
- description: Internal Encompass user administration (modeled).
  name: Encompass Users API
  slug: encompass-users-api
- description: Event subscriptions, resources, events, and custom auth functions.
  name: Encompass Webhooks API
  slug: encompass-webhooks-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Encompass Developer Connect Authentication API
  slug: open-encompass-authentication-api
- collection_type: open
  name: Encompass Developer Connect Authentication Borrower Pairs API
  slug: open-encompass-borrower-pairs-api
- collection_type: open
  name: Encompass Developer Connect Authentication Conditions API
  slug: open-encompass-conditions-api
- collection_type: open
  name: Encompass Developer Connect Authentication Contacts API
  slug: open-encompass-contacts-api
- collection_type: open
  name: Encompass Developer Connect Authentication eFolder API
  slug: open-encompass-efolder-api
- collection_type: open
  name: Encompass Developer Connect Authentication Loan Management API
  slug: open-encompass-loan-management-api
- collection_type: open
  name: Encompass Developer Connect Authentication Loan Pipeline API
  slug: open-encompass-loan-pipeline-api
- collection_type: open
  name: Encompass Developer Connect Authentication Milestones API
  slug: open-encompass-milestones-api
- collection_type: open
  name: Encompass Developer Connect Authentication Users API
  slug: open-encompass-users-api
- collection_type: open
  name: Encompass Developer Connect Authentication Webhooks API
  slug: open-encompass-webhooks-api
- collection_type: open
  name: Encompass Developer Connect API
  slug: open-encompass
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/encompass-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/encompass-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/encompass-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/encompass-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist/encompass-developer-connect
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/ice-mortgage-technology/
- group: company
  title: ''
  type: Website
  url: https://www.icemortgagetechnology.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.icemortgagetechnology.com/developer-connect/docs/welcome
- group: commercial
  title: ''
  type: Plans
  url: plans/encompass-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/encompass-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/encompass-finops.yml
created: '2026-07-04'
description: Encompass is the dominant mortgage loan origination system (LOS), a product of ICE Mortgage Technology (formerly Ellie Mae, acquired by Intercontinental Exchange / ICE in 2020). Its developer program, Encompass Developer Connect, exposes REST APIs that let partners and lenders configure, customize, and administer loan information and resources programmatically - loan manufacturing, loan pipeline, borrower pairs, contacts, eFolder documents and attachments, milestones, conditions, users, product and pricing, and event webhooks. Access is partner/tenant-gated (OAuth 2.0 credentials issued per Encompass instance by a super administrator), but the API reference is publicly documented at developer.icemortgagetechnology.com.
finops:
- name: Encompass Finops
  service_category: Software as a Service - Mortgage Loan Origination
  slug: encompass-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encompass.png
layout: provider
modified: '2026-07-04'
name: Encompass
nav: Providers
network: true
overview: 'Encompass publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Borrower Pairs API, Conditions API, and 7 more. Tagged areas include Mortgage, Loan Origination, LOS, Fintech, and ICE Mortgage Technology.


  Encompass'' developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Encompass Plans Pricing
  plan_count: 2
  slug: encompass-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 4
  name: Encompass Rate Limits
  slug: encompass-rate-limits
scopes:
- name: Encompass Scopes
  scope_count: 1
  slug: encompass-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.9
    developer_ergonomics: 20.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/encompass/refs/heads/main/screenshots/encompass-2026-07-25T213304.png
security:
- kind: authentication
  name: Encompass Authentication
  slug: encompass-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Encompass Domain Security
  slug: encompass-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: encompass
tags:
- Mortgage
- Loan Origination
- LOS
- Fintech
- ICE Mortgage Technology
- Ellie Mae
- Lending
website: https://www.icemortgagetechnology.com/
---

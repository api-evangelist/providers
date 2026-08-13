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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cms Blue Button Agentic Access
  operation_count: 8
  slug: cms-blue-button-agentic-access
  summary_line: 8 operations
api_count: 5
apis:
- description: Medicare coverage resources, one per coverage type.
  name: CMS Blue Button 2.0 Coverage API
  slug: cms-blue-button-coverage-api
- description: Medicare Parts A, B, and D claims as CARIN Blue Button EOB profiles.
  name: CMS Blue Button 2.0 ExplanationOfBenefit API
  slug: cms-blue-button-explanationofbenefit-api
- description: FHIR capability statement.
  name: CMS Blue Button 2.0 Metadata API
  slug: cms-blue-button-metadata-api
- description: Beneficiary demographic and administrative data.
  name: CMS Blue Button 2.0 Patient API
  slug: cms-blue-button-patient-api
- description: OpenID Connect userinfo for the authorizing beneficiary.
  name: CMS Blue Button 2.0 UserInfo API
  slug: cms-blue-button-userinfo-api
artifact_total: 12
collections:
- collection_type: open
  name: CMS Blue Button 2.0 API
  slug: open-cms-blue-button
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cms-blue-button-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cms-blue-button-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cms-blue-button-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://bluebutton.cms.gov
- group: docs
  title: ''
  type: Documentation
  url: https://bluebutton.cms.gov/api-documentation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CMSgov
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.bluebutton.cms.gov
- group: start
  title: ''
  type: GettingStarted
  url: https://bluebutton.cms.gov/production-access/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bluebutton.cms.gov/terms/
- group: commercial
  title: ''
  type: Plans
  url: plans/cms-blue-button-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cms-blue-button-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cms-blue-button-finops.yml
created: '2026-07-11'
description: Blue Button 2.0 is the Centers for Medicare & Medicaid Services (CMS) API that lets Medicare beneficiaries share their Parts A, B, and D claims data with applications they trust. It is a FHIR R4 API conforming to the CARIN Blue Button Implementation Guide (CARIN Consumer Directed Payer Data Exchange), serving ExplanationOfBenefit, Patient, and Coverage resources for 60+ million people with Medicare. Access is patient-facing - each beneficiary authorizes an app through an OAuth 2.0 authorization-code flow (with mandatory PKCE) on Medicare.gov, choosing whether to share demographic data. A self-serve sandbox with synthetic enrollee data is open to everyone; production credentials are free but require CMS approval of the application.
finops:
- name: Cms Blue Button Finops
  service_category: Healthcare Data
  slug: cms-blue-button-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cms-blue-button.png
layout: provider
modified: '2026-07-11'
name: CMS Blue Button 2.0
nav: Providers
network: true
overview: 'CMS Blue Button 2.0 publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Coverage API, ExplanationOfBenefit API, Metadata API, and 2 more. Tagged areas include Blue Button, CARIN, Medicare, FHIR, and Claims Data.


  CMS Blue Button 2.0''s developer surface includes authentication, documentation, sandbox, getting-started guide, and 8 more developer resources.'
plans:
- name: Cms Blue Button Plans Pricing
  plan_count: 2
  slug: cms-blue-button-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Cms Blue Button Rate Limits
  slug: cms-blue-button-rate-limits
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.6
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cms-blue-button/refs/heads/main/screenshots/cms-blue-button-2026-07-25T205758.png
security:
- kind: authentication
  name: Cms Blue Button Authentication
  slug: cms-blue-button-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cms Blue Button Domain Security
  slug: cms-blue-button-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cms-blue-button
tags:
- Blue Button
- CARIN
- Medicare
- FHIR
- Claims Data
- Patient Access
- Healthcare
- Government
website: https://bluebutton.cms.gov
---

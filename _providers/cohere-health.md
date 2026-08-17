---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: HL7 Da Vinci Coverage Requirements Discovery (CRD) FHIR API that lets a provider system instantly verify whether prior authorization is required and confirm service coverage at the point of care. Docu
  name: Cohere Health Coverage Requirements Discovery (CRD) API
  slug: cohere-health-crd-api
- description: 'HL7 Da Vinci Documentation Templates and Rules (DTR) FHIR API that intelligently gathers and submits the documentation a prior authorization request requires, driven by digitized medical policy (FHIR '
  name: Cohere Health Documentation Templates and Rules (DTR) API
  slug: cohere-health-dtr-api
- description: HL7 Da Vinci Prior Authorization Support (PAS) FHIR API that submits an authorization request and returns the outcome, wrapping X12 278 utilization-management exchange in a FHIR interface for CMS-0057
  name: Cohere Health Prior Authorization Support (PAS) API
  slug: cohere-health-pas-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.coherehealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.coherehealth.com/utilization-management/api-based
- group: start
  title: ''
  type: Login
  url: https://login.coherehealth.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coherehealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cohere-health
- group: company
  title: ''
  type: Blog
  url: https://www.coherehealth.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.coherehealth.com/connect
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.coherehealth.com/cohere-health-learning-center/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coherehealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coherehealth.com/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://next.coherehealth.com/organization_onboarding
- group: auth
  title: ''
  type: Compliance
  url: https://www.coherehealth.com/news/cohere-health-earns-hitrust-r2-certification
- group: auth
  title: ''
  type: Authentication
  url: authentication/cohere-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cohere-health-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cohere-health-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cohere-health-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cohere-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cohere-health-llms.txt
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cohere-health-glossary.yml
- group: build
  title: ''
  type: Packages
  url: packages/cohere-health-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cohere-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cohere-health-rate-limits.yml
- group: other
  title: ''
  type: Glossary
  url: https://www.coherehealth.com/glossary
- group: company
  title: ''
  type: Press
  url: https://www.coherehealth.com/press
coverage:
  checked: '2026-08-14'
  detail: The Cohere Connect™ platform API host discovered in the provider-portal bundle, core-platform.coherehealth.com, answers every anonymous request — including the CDS Hooks discovery endpoint /cds-services and /fhir/metadata, which their specs expect to be public — with a JSON 403 "Not Authorized", and the CRD/DTR/PAS FHIR reference is provisioned per health-plan tenant with no public developer portal anywhere in the 521-URL sitemap.
  evidence:
  - status: 403
    url: https://core-platform.coherehealth.com/cds-services
  - status: 403
    url: https://core-platform.coherehealth.com/fhir/metadata
  - status: 403
    url: https://core-platform.coherehealth.com/openapi.json
  - status: 404
    url: https://www.coherehealth.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-07-24'
description: Cohere Health is a United States clinical-intelligence and utilization-management company that digitizes prior authorization for health plans. Its Unify platform applies clinical AI and evidence-based policy to streamline authorization intake, review, and decisioning, and its API suite implements the HL7 Da Vinci Burden Reduction guides — Coverage Requirements Discovery (CRD), Documentation Templates and Rules (DTR), and Prior Authorization Support (PAS) — to help payers meet the CMS Interoperability and Prior Authorization Final Rule (CMS-0057-F). The FHIR R4 APIs support SMART on FHIR applications and are sold to and embedded with health plans rather than offered through a self-serve public developer portal; the documented product surface is real but the API endpoints are partner/health-plan gated. The API-based offering is branded Cohere Connect™ and sits alongside the Cohere Unify platform (utilization management, payment integrity, appeals, care management, claims operations
  and quality), with in-workflow submission via Epic's Payer Platform. The company reports more than 15 million authorizations processed through the APIs and over 4,000 digitized policies.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-14T00:00:00Z'
name: Cohere Health
nav: Providers
network: true
overview: 'Cohere Health publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Prior Authorization, Utilization Management, and Payer.


  Cohere Health''s developer surface includes documentation, engineering blog, support, signup flow, authentication, and 19 more developer resources.'
plans:
- name: Cohere Health Plans Pricing
  plan_count: 0
  slug: cohere-health-plans-pricing
random_paper: 113
rate_limits:
- limit_count: 0
  name: Cohere Health Rate Limits
  slug: cohere-health-rate-limits
scopes:
- name: Cohere Health Scopes
  scope_count: 7
  slug: cohere-health-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 30.4
  delta: 1.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 83.3
    governance: 22.9
    operational_transparency: 5.3
  previous_composite: 29.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cohere-health/refs/heads/main/screenshots/cohere-health-2026-07-25T210019.png
security:
- kind: authentication
  name: Cohere Health Authentication
  slug: cohere-health-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Cohere Health Domain Security
  slug: cohere-health-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cohere-health
tags:
- Healthcare
- United States
- Prior Authorization
- Utilization Management
- Payer
- FHIR
- HL7
- Da Vinci
- SMART on FHIR
- Interoperability
website: https://www.coherehealth.com/
---

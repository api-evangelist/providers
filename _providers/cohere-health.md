---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
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
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cohere-health-domain-security.yml
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
created: '2026-07-24'
description: Cohere Health is a United States clinical-intelligence and utilization-management company that digitizes prior authorization for health plans. Its Unify platform applies clinical AI and evidence-based policy to streamline authorization intake, review, and decisioning, and its API suite implements the HL7 Da Vinci Burden Reduction guides — Coverage Requirements Discovery (CRD), Documentation Templates and Rules (DTR), and Prior Authorization Support (PAS) — to help payers meet the CMS Interoperability and Prior Authorization Final Rule (CMS-0057-F). The FHIR R4 APIs support SMART on FHIR applications and are sold to and embedded with health plans rather than offered through a self-serve public developer portal; the documented product surface is real but the API endpoints are partner/health-plan gated.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24T18:00:00Z'
name: Cohere Health
nav: Providers
network: true
overview: 'Cohere Health publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Prior Authorization, Utilization Management, and Payer.


  Cohere Health''s developer surface includes documentation, engineering blog, support, signup flow, authentication, and 14 more developer resources.'
random_paper: 41
scopes:
- name: Cohere Health Scopes
  scope_count: 7
  slug: cohere-health-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 32.0
  delta: -0.7
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 83.3
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 32.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 76.3
  schema_version: 0.6
  scored_at: '2026-07-28'
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

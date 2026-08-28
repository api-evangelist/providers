---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 29.3
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: 'REST API for the Proactive Patient Risk Feed: upload FHIR R4 US Core / CCLF / custom claims and EHR datasets, then retrieve ranked actionable risk lists, per-patient risk profiles with contributing fa'
  name: Diagnostic Robotics Precision Population Health API
  slug: diagnostic-robotics-precision-population-health-api
- description: REST API for the patient-questionnaire and triage service. Create a patient, open a visit, attach symptoms, walk the adaptive question tree one question at a time, finish the visit, then read the medi
  name: Diagnostic Robotics Patient Questionnaire API
  slug: diagnostic-robotics-patient-questionnaire-api
- description: 'REST API for symptom lookup inside the patient-questionnaire flow: autocomplete a free-text symptom string against the Diagnostic Robotics symptom ontology, and list the symptoms already attached to a'
  name: Diagnostic Robotics Symptom Search Service
  slug: diagnostic-robotics-symptom-search-service
artifact_total: 12
collections:
- collection_type: open
  name: Diagnostic Robotics API
  slug: open-diagnostic-robotics-patient-questionnaire
- collection_type: open
  name: Diagnostic Robotics API
  slug: open-diagnostic-robotics-precision-population-health
- collection_type: open
  name: Search Service
  slug: open-diagnostic-robotics-symptom-search
common:
- group: company
  title: ''
  type: Website
  url: https://diagnosticrobotics.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.diagnosticrobotics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.diagnosticrobotics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.diagnosticrobotics.com/docs/proactive-patient-risk-feed-api/usgko1x40nf1c-diagnostic-robotics-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.diagnosticrobotics.com/docs/proactive-patient-risk-feed-api/3y8qknbsqo42r-authentication
- group: operate
  title: ''
  type: Support
  url: https://diagnosticrobotics.com/contact
- group: company
  title: ''
  type: Blog
  url: https://diagnosticrobotics.com/thought-leadership
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Diagnostic-Robotics
- group: commercial
  title: ''
  type: TermsOfService
  url: https://diagnosticrobotics.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://diagnosticrobotics.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://diagnosticrobotics.statuspage.io
- group: auth
  title: ''
  type: TrustCenter
  url: security/diagnostic-robotics-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://diagnosticrobotics.com/about/trust-center
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/diagnostic-robotics/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/DiagnosticRobo
- group: auth
  title: ''
  type: Authentication
  url: authentication/diagnostic-robotics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/diagnostic-robotics-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/diagnostic-robotics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/diagnostic-robotics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/diagnostic-robotics-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/diagnostic-robotics-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/diagnostic-robotics-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/diagnostic-robotics-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/diagnostic-robotics-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/diagnostic-robotics-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/diagnostic-robotics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/diagnostic-robotics-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/diagnostic-robotics-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: 'Diagnostic Robotics is a Tel Aviv and Boston based clinical AI company whose platform turns medical claims, EHR and FHIR data into predictive risk stratification, actionable next steps and automated care operations for health plans, providers and care organizations. The company publishes two public developer projects on a Stoplight-hosted documentation portal: a Patient Questionnaire / triage API that walks a patient through symptom search, adaptive questioning and a triage outcome, and a Proactive Patient Risk Feed (Precision Population Health) API that ingests FHIR R4 US Core, CCLF and custom claims datasets and returns ranked risk lists, per-patient risk profiles, HCC/RAF risk-adjustment gaps and embeddable widgets. Access is OAuth 2.0 client-credentials or API key and is provisioned per customer on a dedicated per-client subdomain.'
image: https://storage.googleapis.com/gpt-engineer-file-uploads/fKseK09ayVTXZOhSuXAlVH1splM2/social-images/social-1781800345789-Screenshot_2026-06-18_at_19.32.17.webp
layout: provider
modified: '2026-08-12'
name: Diagnostic Robotics
nav: Providers
network: true
overview: 'Diagnostic Robotics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Precision Population Health API, Patient Questionnaire API, and Symptom Search Service. Tagged areas include Health, Healthcare, Clinical AI, Population Health, and Risk Adjustment.


  Diagnostic Robotics'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 22 more developer resources.'
plans:
- name: Diagnostic Robotics Plans Pricing
  plan_count: 0
  slug: diagnostic-robotics-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Diagnostic Robotics Rate Limits
  slug: diagnostic-robotics-rate-limits
scopes:
- name: Diagnostic Robotics Scopes
  scope_count: 0
  slug: diagnostic-robotics-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.2
  delta: -0.6
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 30.3
    contract_quality: 46.6
    developer_ergonomics: 66.1
    discoverability: 74.1
    governance: 30.3
    operational_transparency: 18.4
  previous_composite: 53.8
  provenance:
    conformance: first-party
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 68.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/diagnostic-robotics/refs/heads/main/screenshots/diagnostic-robotics-2026-08-17T080902.png
security:
- kind: authentication
  name: Diagnostic Robotics Authentication
  slug: diagnostic-robotics-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Diagnostic Robotics Domain Security
  slug: diagnostic-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Diagnostic Robotics Trust Center
  slug: diagnostic-robotics-trust-center
  summary_line: HIPAA, ISO 27001, ISO 27799, SOC 2 Type II
slug: diagnostic-robotics
tags:
- Health
- Healthcare
- Clinical AI
- Population Health
- Risk Adjustment
- Predictive Analytics
- triage
- FHIR
- Claims Data
- Care Management
- Payers
- Medical Coding
website: https://diagnosticrobotics.com/
---

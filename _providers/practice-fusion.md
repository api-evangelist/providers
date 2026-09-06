---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: 'ONC Certified FHIR R4 (v4.0.1) API implementing US Core 6.1.0, SMART App Launch 2.0.0, and Bulk Data Access 1.0.1. Provides read and search access across 47 FHIR resource types (Patient, Observation, '
  name: Practice Fusion FHIR API (Patient Data Sharing)
  slug: practice-fusion-fhir-api-patient-data-sharing
- description: Patient-facing personal health record API documented in the PDS API Developer Guide. Serves a patient their own clinical documents and record data from the Practice Fusion EHR, authorized with OAuth 2
  name: Practice Fusion Patient Fusion PHR API
  slug: practice-fusion-patient-fusion-phr-api
- description: Proprietary bi-directional laboratory integration API connecting practices with 300+ independent, hospital, and health-system labs including Labcorp, Quest Diagnostics, RadNet, SimonMed, and Rayus for
  name: Practice Fusion Labs API
  slug: practice-fusion-labs-api
- description: Proprietary bi-directional imaging integration API for order receipt and study transmission across imaging providers, supporting 100,000+ medical professionals.
  name: Practice Fusion Imaging API
  slug: practice-fusion-imaging-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/practice-fusion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/practice-fusion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/practice-fusion-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/practice-fusion-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/practice-fusion-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.practicefusion.com/onc-certified-ehr/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/practice-fusion-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/practice-fusion-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/practice-fusion-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/practice-fusion-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/practice-fusion-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/practice-fusion-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/practice-fusion-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.practicefusion.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.practicefusion.com/fhir/
- group: docs
  title: ''
  type: Documentation
  url: https://www.practicefusion.com/fhir/api-specifications/
- group: docs
  title: ''
  type: APIReference
  url: https://www.practicefusion.com/fhir/api-specifications/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.practicefusion.com/fhir/get-started/
- group: operate
  title: ''
  type: Support
  url: https://partnersupport.practicefusion.com/s/
- group: start
  title: ''
  type: SignUp
  url: https://pfpds.practicefusion.com/s/Registration
- group: company
  title: ''
  type: Blog
  url: https://www.practicefusion.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.practicefusion.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.practicefusion.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.practicefusion.com/pages/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.practicefusion.com/pages/privacy-policy.html
- group: build
  title: ''
  type: Packages
  url: packages/practice-fusion-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/practice-fusion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/practice-fusion-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/practice-fusion-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/practice-fusion-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/practice-fusion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://veradigm.com/legal/security-program/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/practicefusion
- group: start
  title: ''
  type: Login
  url: https://static.practicefusion.com/apps/ehr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.practicefusion.com/developer-center/
- group: docs
  title: ''
  type: Documentation
  url: https://www.practicefusion.com/pds-api/developer-guide/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.practicefusion.com/pds-api/termsofservice/
- group: operate
  title: ''
  type: Support
  url: https://help.practicefusion.com/s/article/using-fhir-in-practice-fusion
created: '2026-07-17'
description: Practice Fusion is a cloud-based electronic health record (EHR) platform for independent ambulatory medical practices, serving roughly 6.4% of U.S. ambulatory practices with more than 43 million clinical records and around 5 million patient visits per month. Its developer surface centers on an ONC Certified Health IT FHIR R4 (Patient Data Sharing / PDS) API implementing US Core 6.1.0, SMART App Launch 2.0.0, and Bulk Data Access 1.0.1 over SMART-on-FHIR OAuth2, alongside proprietary bi-directional Labs and Imaging APIs and a partner marketplace of 600+ integrated companies.
image: https://www.practicefusion.com/assets/img/practice-fusion-logo.png
layout: provider
modified: '2026-08-14'
name: Practice Fusion
nav: Providers
network: true
overview: 'Practice Fusion publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Electronic Health Records, EHR, and FHIR.


  Practice Fusion''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, engineering blog, and 32 more developer resources.'
plans:
- name: Practice Fusion Plans Pricing
  plan_count: 8
  slug: practice-fusion-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Practice Fusion Rate Limits
  slug: practice-fusion-rate-limits
scopes:
- name: Practice Fusion Scopes
  scope_count: 0
  slug: practice-fusion-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 34.4
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 61.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 73.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/practice-fusion/refs/heads/main/screenshots/practice-fusion-2026-08-17T081329.png
security:
- kind: authentication
  name: Practice Fusion Authentication
  slug: practice-fusion-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Practice Fusion Domain Security
  slug: practice-fusion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Practice Fusion Vulnerability Disclosure
  slug: practice-fusion-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Practice Fusion Trust Center
  slug: practice-fusion-trust-center
  summary_line: SOC 2 Type 2, EHNAC accreditation, EPCS certification, ISO 9001:2015, ONC Certification Rule (Certified Health IT), HIPAA
slug: practice-fusion
tags:
- Company
- Healthcare
- Electronic Health Records
- EHR
- FHIR
- Interoperability
- Medical
- Health IT
- SMART on FHIR
- Clinical Data
website: https://www.practicefusion.com/
---

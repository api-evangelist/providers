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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-10-31'
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
artifact_total: 16
common:
- group: auth
  href: https://artifacts.apis.io/practice-fusion/security/practice-fusion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/practice-fusion-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/practice-fusion/authentication/practice-fusion-authentication.yml
  title: ''
  type: Authentication
  url: authentication/practice-fusion-authentication.yml
- group: auth
  href: https://artifacts.apis.io/practice-fusion/scopes/practice-fusion-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/practice-fusion-scopes.yml
- group: agent
  href: https://artifacts.apis.io/practice-fusion/well-known/practice-fusion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/practice-fusion-well-known.yml
- group: design
  href: https://artifacts.apis.io/practice-fusion/conformance/practice-fusion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/practice-fusion-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.practicefusion.com/onc-certified-ehr/
- group: design
  href: https://artifacts.apis.io/practice-fusion/errors/practice-fusion-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/practice-fusion-problem-types.yml
- group: design
  href: https://artifacts.apis.io/practice-fusion/lifecycle/practice-fusion-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/practice-fusion-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/practice-fusion/conventions/practice-fusion-conventions.yml
  title: ''
  type: Conventions
  url: conventions/practice-fusion-conventions.yml
- group: design
  href: https://artifacts.apis.io/practice-fusion/conventions/practice-fusion-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/practice-fusion-conventions.yml
- group: design
  href: https://artifacts.apis.io/practice-fusion/data-model/practice-fusion-data-model.yml
  title: ''
  type: DataModel
  url: data-model/practice-fusion-data-model.yml
- group: agent
  href: https://artifacts.apis.io/practice-fusion/mcp/practice-fusion-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/practice-fusion-mcp.yml
- group: agent
  href: https://artifacts.apis.io/practice-fusion/llms/practice-fusion-llms.txt
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
  href: https://artifacts.apis.io/practice-fusion/packages/practice-fusion-packages.yml
  title: ''
  type: Packages
  url: packages/practice-fusion-packages.yml
- group: commercial
  href: https://artifacts.apis.io/practice-fusion/plans/practice-fusion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/practice-fusion-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/practice-fusion/rate-limits/practice-fusion-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/practice-fusion-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/practice-fusion/changelog/practice-fusion-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/practice-fusion-changelog.yml
- group: agent
  href: https://artifacts.apis.io/practice-fusion/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/practice-fusion/security/practice-fusion-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/practice-fusion-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/practice-fusion/security/practice-fusion-vulnerability-disclosure.yml
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
finops:
- has_sources: true
  method: derived
  name: Practice Fusion Finops
  primary_unit: provider
  service_category: ''
  slug: practice-fusion-finops
  template: false
image: https://www.practicefusion.com/assets/img/practice-fusion-logo.png
layout: provider
modified: '2026-08-14'
name: Practice Fusion
nav: Providers
network: true
overview: 'Practice Fusion is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Electronic Health Records, FHIR, and Interoperability.


  Practice Fusion''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, engineering blog, and 32 more developer resources.'
plans:
- name: Practice Fusion Plans Pricing
  plan_count: 2
  slug: practice-fusion-plans-pricing
random_paper: 12
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
  composite: 58.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 51.0
    catalog_earned_first_party: 8.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 32.3
    developer_ergonomics: 58.9
    discoverability: 71.4
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 58.9
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
    score: 46.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/practice-fusion/practice-fusion-2026-08-17T081329.png
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
skill_count: 4
skills:
- name: Run a Practice Fusion FHIR Bulk Data group export
  slug: practice-fusion-bulk-export
- name: Retrieve clinical documents and provenance from Practice Fusion
  slug: practice-fusion-clinical-documents
- name: Connect to a Practice Fusion FHIR endpoint with SMART on FHIR
  slug: practice-fusion-connect-smart
- name: Assemble a patient chart summary from Practice Fusion
  slug: practice-fusion-patient-chart-summary
slug: practice-fusion
tags:
- Company
- Healthcare
- Electronic Health Records
- FHIR
- Interoperability
- Medical
- Health IT
- SMART on FHIR
- Clinical Data
website: https://www.practicefusion.com/
---

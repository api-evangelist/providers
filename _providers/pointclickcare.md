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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pointclickcare Agentic Access
  operation_count: 8
  slug: pointclickcare-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: PointClickCare FHIR API provides HL7 FHIR-compliant access to resident clinical data for post-acute and long-term care settings, supporting interoperability with other healthcare systems and care coor
  name: PointClickCare FHIR API
  slug: pointclickcare-fhir-api
- description: Clinical assessments (MDS, fall risk, etc.)
  name: PointClickCare Assessments API
  slug: pointclickcare-assessments-api
- description: Diagnosis and condition records
  name: PointClickCare Diagnoses API
  slug: pointclickcare-diagnoses-api
- description: Facility and unit management
  name: PointClickCare Facilities API
  slug: pointclickcare-facilities-api
- description: Medication orders and administration records (MAR)
  name: PointClickCare Medications API
  slug: pointclickcare-medications-api
- description: Resident/patient demographics and admission data
  name: PointClickCare Patients API
  slug: pointclickcare-patients-api
- description: Vital signs records
  name: PointClickCare Vitals API
  slug: pointclickcare-vitals-api
artifact_total: 19
collections:
- collection_type: open
  name: PointClickCare Long-Term Care EHR API
  slug: open-pointclickcare-ehr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pointclickcare-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pointclickcare-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pointclickcare-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pointclickcare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pointclickcare-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pointclickcare
- group: start
  title: ''
  type: Portal
  url: https://developer.pointclickcare.com/spa
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pointclickcare.com/spa
- group: company
  title: ''
  type: Website
  url: https://www.pointclickcare.com/
- group: operate
  title: ''
  type: Support
  url: https://pointclickcare.com/customer-support/
- group: company
  title: ''
  type: Blog
  url: https://pointclickcare.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pointclickcare.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pointclickcare.com/legal/terms-conditions/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pointclickcare.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PointClickCare
created: '2026-03-18'
description: PointClickCare is the leading cloud-based software platform for the senior care and post-acute care industry, providing electronic health records (EHR), care coordination, financial management, and clinical decision support to skilled nursing facilities, senior living communities, and home health agencies. PointClickCare publishes both a partner EHR API and a HL7 FHIR API for clinical interoperability across the long-term and post-acute care (LTPAC) ecosystem.
finops:
- name: Pointclickcare Finops
  service_category: API
  slug: pointclickcare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pointclickcare.png
json_schemas:
- name: PointClickCare Patient
  property_count: 20
  slug: pointclickcare-patient
jsonld:
- class_count: 0
  name: Pointclickcare Context
  property_count: 33
  slug: pointclickcare-context
layout: provider
modified: '2026-05-19'
name: PointClickCare
nav: Providers
network: true
overview: 'PointClickCare publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Assessments API, Diagnoses API, Facilities API, and 3 more. Tagged areas include Healthcare, Long-Term Care, Post-Acute Care, EHR, and FHIR.


  The PointClickCare catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PointClickCare''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 10 more developer resources.'
plans:
- name: Pointclickcare Plans Pricing
  plan_count: 3
  slug: pointclickcare-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 5
  name: Pointclickcare Rate Limits
  slug: pointclickcare-rate-limits
rules:
- name: PointClickCare API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: pointclickcare-jsonschema-spectral-rules
scopes:
- name: Pointclickcare Scopes
  scope_count: 3
  slug: pointclickcare-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 66.8
  delta: 2.8
  facets:
    commercial_clarity: 68.4
    contract_quality: 72.6
    developer_ergonomics: 34.8
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 64.0
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 87.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pointclickcare/refs/heads/main/screenshots/pointclickcare-2026-06-20T191845.png
security:
- kind: authentication
  name: Pointclickcare Authentication
  slug: pointclickcare-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Pointclickcare Domain Security
  slug: pointclickcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pointclickcare Trust Center
  slug: pointclickcare-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: pointclickcare
tags:
- Healthcare
- Long-Term Care
- Post-Acute Care
- EHR
- FHIR
- Senior Care
- Interoperability
website: https://www.pointclickcare.com/
---

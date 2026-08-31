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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pointclickcare Agentic Access
  operation_count: 8
  slug: pointclickcare-agentic-access
  summary_line: 8 operations
api_count: 1
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
artifact_total: 32
collections:
- collection_type: postman
  name: PointClickCare Long-Term Care EHR Assessments API
  slug: postman-pointclickcare-assessments-api
- collection_type: postman
  name: PointClickCare Long-Term Care EHR Assessments Diagnoses API
  slug: postman-pointclickcare-diagnoses-api
- collection_type: postman
  name: PointClickCare Long-Term Care EHR Assessments Facilities API
  slug: postman-pointclickcare-facilities-api
- collection_type: postman
  name: PointClickCare Long-Term Care EHR Assessments Medications API
  slug: postman-pointclickcare-medications-api
- collection_type: postman
  name: PointClickCare Long-Term Care EHR Assessments Patients API
  slug: postman-pointclickcare-patients-api
- collection_type: postman
  name: PointClickCare Long-Term Care EHR Assessments Vitals API
  slug: postman-pointclickcare-vitals-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PointClickCare Long-Term Care EHR Assessments API
  slug: open-pointclickcare-assessments-api
- collection_type: open
  name: PointClickCare Long-Term Care EHR Assessments Diagnoses API
  slug: open-pointclickcare-diagnoses-api
- collection_type: open
  name: PointClickCare Long-Term Care EHR API
  slug: open-pointclickcare-ehr
- collection_type: open
  name: PointClickCare Long-Term Care EHR Assessments Facilities API
  slug: open-pointclickcare-facilities-api
- collection_type: open
  name: PointClickCare Long-Term Care EHR Assessments Medications API
  slug: open-pointclickcare-medications-api
- collection_type: open
  name: PointClickCare Long-Term Care EHR Assessments Patients API
  slug: open-pointclickcare-patients-api
- collection_type: open
  name: PointClickCare Long-Term Care EHR Assessments Vitals API
  slug: open-pointclickcare-vitals-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/pointclickcare-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pointclickcare/overview
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


  PointClickCare''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 12 more developer resources.'
plans:
- name: Pointclickcare Plans Pricing
  plan_count: 3
  slug: pointclickcare-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Pointclickcare Rate Limits
  slug: pointclickcare-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: PointClickCare API Rules
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
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 56.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 9.8
    contract_quality: 63.3
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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

---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Community Health Systems Agentic Access
  operation_count: 4
  slug: community-health-systems-agentic-access
  summary_line: 4 operations
api_count: 5
apis:
- description: FHIR R4 read API exposing provider and pharmacy directory data in compliance with CMS interoperability requirements. Third-party applications can search Practitioner, Organization, and Location resour
  name: Community Health Systems Provider Directory API
  slug: provider-directory-api
- description: Adjudicated claims and encounter data
  name: Community Health Systems Claims API
  slug: community-health-systems-claims-api
- description: Formulary and medication data
  name: Community Health Systems Formulary API
  slug: community-health-systems-formulary-api
- description: Patient demographic and clinical data
  name: Community Health Systems Patient API
  slug: community-health-systems-patient-api
- description: Provider information
  name: Community Health Systems Practitioner API
  slug: community-health-systems-practitioner-api
artifact_total: 17
collections:
- collection_type: open
  name: Community Health Systems Patient Access API
  slug: open-chs-patient-access-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/community-health-systems-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/community-health-systems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/community-health-systems-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/community-health-systems-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/community-health-systems
- group: company
  title: ''
  type: Website
  url: https://www.chs.net
- group: start
  title: ''
  type: PatientPortal
  url: https://www.chs.net/patients-visitors/
- group: company
  title: ''
  type: Investors
  url: https://www.chs.net/investors/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chs.net/privacy-statement/
- group: other
  title: ''
  type: CMSInteroperability
  url: https://www.cms.gov/regulations-and-guidance/guidance/interoperability/index
- group: other
  title: ''
  type: HL7FHIRR4
  url: https://hl7.org/fhir/R4/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/community-health-systems-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/chs-fhir-bundle-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/community-health-systems-rules.yml
created: '2026-03-21'
description: Community Health Systems (CHS) is a Fortune 500 hospital operator that owns, leases, and operates general acute care hospitals across the United States. In compliance with the CMS Interoperability and Patient Access Final Rule (CMS-9115-F), CHS publishes FHIR R4 healthcare interoperability APIs that allow third-party applications to access patient demographics and clinical data, adjudicated claims and encounters, formulary information, and provider directory data. The APIs use the HL7 FHIR R4 standard and SMART-on-FHIR authorization for patient-scoped access.
finops:
- name: Community Health Systems Finops
  service_category: Healthcare
  slug: community-health-systems-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/community-health-systems.png
json_schemas:
- name: CHS FHIR Bundle
  property_count: 6
  slug: chs-fhir-bundle
jsonld:
- class_count: 0
  name: Community Health Systems Context
  property_count: 5
  slug: community-health-systems-context
layout: provider
modified: '2026-05-19'
name: Community Health Systems
nav: Providers
network: true
overview: 'Community Health Systems publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Claims API, Formulary API, Patient API, and 1 more. Tagged areas include CMS-9115-F, FHIR, Healthcare, Hospitals, and Interoperability.


  The Community Health Systems catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Community Health Systems'' developer surface includes authentication and 13 more developer resources.'
plans:
- name: Community Health Systems Plans Pricing
  plan_count: 1
  slug: community-health-systems-plans-pricing
press:
- date: '2026-05-25'
  title: Press Releases
  url: https://www.googlecloudpresscorner.com/healthcare-life-sciences?l=25&o=50
- date: '2026-05-25'
  title: Community Health Systems and Denim Health Announce a ...
  url: https://www.businesswire.com/news/home/20241007978867/en/Community-Health-Systems-and-Denim-Health-Announce-a-Development-Partnership-Designed-to-Broadly-Scale-Conversational-AI-Across-the-CHS-Patient-Access-Center
- date: '2026-05-25'
  title: CHS migrates to Google Cloud data platform, adopts ...
  url: https://www.healthcaredive.com/news/community-health-systems-google-cloud-generative-AI/706130/
- date: '2026-05-25'
  title: Community Health Systems, Inc. Announces Third Quarter ...
  url: https://chsnet.gcs-web.com/news-releases/news-release-details/community-health-systems-inc-announces-third-quarter-ended-2
- date: '2026-05-25'
  title: Community Health Systems Completes Data Migration and ...
  url: https://www.prnewswire.com/news-releases/community-health-systems-completes-data-migration-and-implements-new-generative-ai-innovations-with-google-cloud-302048799.html
random_paper: 39
rate_limits:
- limit_count: 1
  name: Community Health Systems Rate Limits
  slug: community-health-systems-rate-limits
rules:
- name: Community Health Systems API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: community-health-systems-jsonschema-spectral-rules
- name: Community Health Systems API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: community-health-systems-rules
scopes:
- name: Community Health Systems Scopes
  scope_count: 2
  slug: community-health-systems-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 44.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.7
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/community-health-systems/refs/heads/main/screenshots/community-health-systems-2026-06-20T174823.png
security:
- kind: authentication
  name: Community Health Systems Authentication
  slug: community-health-systems-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Community Health Systems Domain Security
  slug: community-health-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: community-health-systems
tags:
- CMS-9115-F
- FHIR
- Healthcare
- Hospitals
- Interoperability
- Patient Access
- Provider Directory
- SMART-on-FHIR
- Fortune 500
website: https://www.chs.net
---

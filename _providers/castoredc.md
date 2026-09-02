---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
- acting_count: 7
  human_in_the_loop: 0
  name: Castoredc Agentic Access
  operation_count: 34
  slug: castoredc-agentic-access
  summary_line: 34 operations · 7 acting
api_count: 1
apis:
- description: Immutable audit trail of study changes.
  name: Castor Audit Trail API
  slug: castoredc-audit-trail-api
- description: Bulk export of study data, structure, and option groups.
  name: Castor Data Export API
  slug: castoredc-data-export-api
- description: Study fields and their metadata (dependencies, option groups, validations).
  name: Castor Fields API
  slug: castoredc-fields-api
- description: Institutes (sites / centers) participating in a study.
  name: Castor Institutes API
  slug: castoredc-institutes-api
- description: Reference metadata such as countries.
  name: Castor Metadata API
  slug: castoredc-metadata-api
- description: Participants (records / subjects) enrolled in a study.
  name: Castor Participants API
  slug: castoredc-participants-api
- description: Reports / repeating data and their instances.
  name: Castor Reports API
  slug: castoredc-reports-api
- description: Studies accessible to the API client.
  name: Castor Studies API
  slug: castoredc-studies-api
- description: Collected values for study forms.
  name: Castor Study Data Points API
  slug: castoredc-study-data-points-api
- description: Surveys, survey packages, and ePRO.
  name: Castor Surveys API
  slug: castoredc-surveys-api
- description: Users and study membership.
  name: Castor Users API
  slug: castoredc-users-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Castor EDC / CDMS Audit Trail API
  slug: open-castoredc-audit-trail-api
- collection_type: open
  name: Castor EDC / CDMS Audit Trail Data Export API
  slug: open-castoredc-data-export-api
- collection_type: open
  name: Castor EDC / CDMS Audit Trail Fields API
  slug: open-castoredc-fields-api
- collection_type: open
  name: Castor EDC / CDMS Audit Trail Institutes API
  slug: open-castoredc-institutes-api
- collection_type: open
  name: Castor EDC / CDMS Audit Trail Metadata API
  slug: open-castoredc-metadata-api
- collection_type: open
  name: Castor EDC / CDMS Audit Trail Participants API
  slug: open-castoredc-participants-api
- collection_type: open
  name: Castor EDC / CDMS Audit Trail Reports API
  slug: open-castoredc-reports-api
- collection_type: open
  name: Castor EDC / CDMS Audit Trail Studies API
  slug: open-castoredc-studies-api
- collection_type: open
  name: Castor EDC / CDMS Audit Trail Study Data Points API
  slug: open-castoredc-study-data-points-api
- collection_type: open
  name: Castor EDC / CDMS Audit Trail Surveys API
  slug: open-castoredc-surveys-api
- collection_type: open
  name: Castor EDC / CDMS Audit Trail Users API
  slug: open-castoredc-users-api
- collection_type: open
  name: Castor EDC / CDMS API
  slug: open-castoredc
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/castoredc-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/castoredc-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/castoredc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/castoredc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/castoredc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/castoredc-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/castoredc
- group: company
  title: ''
  type: Website
  url: https://www.castoredc.com
- group: docs
  title: ''
  type: Documentation
  url: https://helpdesk.castoredc.com/application-programming-interface-api
- group: commercial
  title: ''
  type: Plans
  url: plans/castoredc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/castoredc-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/castoredc-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.castoredc.com/blog/
created: '2026-07-05'
description: Castor (Castor EDC / CDMS) is a cloud electronic data capture (EDC) and clinical data management platform for clinical trials and real-world research. Its RESTful API at https://data.castoredc.com/api exposes study configuration and collected data - studies, participants (records), institutes (sites), users, fields and field metadata, study data points, repeating data (reports), surveys and survey packages, audit trail, and batch data export - authenticated with OAuth2 client-credentials. The API is used to integrate Castor with external systems, automate data entry and extraction, and support statistical analysis via the official R and Python wrapper packages.
finops:
- name: Castoredc Finops
  service_category: Healthcare and Life Sciences
  slug: castoredc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/castoredc.png
layout: provider
modified: '2026-07-05'
name: Castor
nav: Providers
network: true
overview: 'Castor publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Audit Trail API, Data Export API, Fields API, and 8 more. Tagged areas include Clinical Trials, Electronic Data Capture, EDC, Clinical Data Management, and Healthcare.


  Castor''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Castoredc Plans Pricing
  plan_count: 3
  slug: castoredc-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Castoredc Rate Limits
  slug: castoredc-rate-limits
scopes:
- name: Castoredc Scopes
  scope_count: 3
  slug: castoredc-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.4
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/castoredc/refs/heads/main/screenshots/castoredc-2026-07-25T204743.png
security:
- kind: authentication
  name: Castoredc Authentication
  slug: castoredc-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Castoredc Domain Security
  slug: castoredc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Castoredc Vulnerability Disclosure
  slug: castoredc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: castoredc
tags:
- Clinical Trials
- Electronic Data Capture
- EDC
- Clinical Data Management
- Healthcare
- Life Sciences
- Research
website: https://www.castoredc.com
---

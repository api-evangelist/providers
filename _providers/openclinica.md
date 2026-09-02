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
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Openclinica Agentic Access
  operation_count: 14
  slug: openclinica-agentic-access
  summary_line: 14 operations · 9 acting
api_count: 1
apis:
- description: OAuth 2.0 token acquisition.
  name: OpenClinica Authentication API
  slug: openclinica-authentication-api
- description: Bulk participant and event operations plus the bulk actions log.
  name: OpenClinica Bulk Operations API
  slug: openclinica-bulk-operations-api
- description: Import and retrieve CRF data using CDISC ODM.
  name: OpenClinica Clinical Data API
  slug: openclinica-clinical-data-api
- description: Read ODM study design metadata.
  name: OpenClinica Metadata API
  slug: openclinica-metadata-api
- description: Study participants (subjects) - add, update, list, and extract contact info.
  name: OpenClinica Participants API
  slug: openclinica-participants-api
- description: Scheduling and updating study events (visits) for participants.
  name: OpenClinica Study Events API
  slug: openclinica-study-events-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenClinica REST Authentication API
  slug: open-openclinica-authentication-api
- collection_type: open
  name: OpenClinica REST Authentication Bulk Operations API
  slug: open-openclinica-bulk-operations-api
- collection_type: open
  name: OpenClinica REST Authentication Clinical Data API
  slug: open-openclinica-clinical-data-api
- collection_type: open
  name: OpenClinica REST Authentication Metadata API
  slug: open-openclinica-metadata-api
- collection_type: open
  name: OpenClinica REST Authentication Participants API
  slug: open-openclinica-participants-api
- collection_type: open
  name: OpenClinica REST Authentication Study Events API
  slug: open-openclinica-study-events-api
- collection_type: open
  name: OpenClinica REST API
  slug: open-openclinica
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openclinica-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/openclinica-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openclinica-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openclinica-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenClinica
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openclinica
- group: company
  title: ''
  type: Website
  url: https://www.openclinica.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openclinica.com/oc4/how-and-when-to-use-apis/
- group: commercial
  title: ''
  type: Plans
  url: plans/openclinica-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openclinica-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openclinica-finops.yml
created: '2026-07-05'
description: OpenClinica is a clinical-trial electronic data capture (EDC) and clinical data management platform used to build studies, capture case report form (CRF) data, schedule study events, and manage participants across sites. It ships as a free, open-source Community Edition (LGPL) and as a fully supported, hosted Enterprise Edition. OpenClinica exposes a documented REST web services API - authenticated with OAuth 2.0 bearer tokens - for programmatically adding and updating participants (single and bulk), scheduling and updating study events, and importing and retrieving clinical data. Data is interchanged using the CDISC ODM (Operational Data Model) standard as XML or JSON, so studies remain portable and standards-based.
finops:
- name: Openclinica Finops
  service_category: Clinical Data Management
  slug: openclinica-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openclinica.png
layout: provider
modified: '2026-07-05'
name: OpenClinica
nav: Providers
network: true
overview: 'OpenClinica publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Bulk Operations API, Clinical Data API, and 3 more. Tagged areas include Clinical Trials, Electronic Data Capture, EDC, Clinical Data Management, and CDISC ODM.


  OpenClinica''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Openclinica Plans Pricing
  plan_count: 2
  slug: openclinica-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Openclinica Rate Limits
  slug: openclinica-rate-limits
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 14.1
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openclinica/refs/heads/main/screenshots/openclinica-2026-08-07T190538.png
security:
- kind: authentication
  name: Openclinica Authentication
  slug: openclinica-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openclinica Domain Security
  slug: openclinica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Openclinica Trust Center
  slug: openclinica-trust-center
  summary_line: SOC 2, ISO 27001
slug: openclinica
tags:
- Clinical Trials
- Electronic Data Capture
- EDC
- Clinical Data Management
- CDISC ODM
- Healthcare
- Open-Source
website: https://www.openclinica.com
---

---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 254
  human_in_the_loop: 7
  name: Ku Leuven Agentic Access
  operation_count: 536
  slug: ku-leuven-agentic-access
  summary_line: 536 operations · 254 acting · 7 human-in-the-loop
api_count: 41
apis:
- description: ICTS Data Services REST API exposing public personnel / who-is-who person information. An expanded intranet variant requires a service account.
  name: KU Leuven Person Information API
  slug: person
- description: ICTS Data Services REST API exposing public educational offering data, including programs (opleidingen) and course components.
  name: KU Leuven Educational Offering (Onderwijsaanbod) API
  slug: program
- description: ICTS Data Services REST API exposing public organizational-structure information matching the institutional organizational chart. An expanded intranet variant is available via service account.
  name: KU Leuven Organizational Chart (Organigram) API
  slug: organigram
- description: ICTS Data Services REST API exposing public job vacancy / job posting data.
  name: KU Leuven Vacancies (Vacatures) API
  slug: vacancies
- description: ICTS Data Services API exposing an individual's personal timetable. Protected by OAuth 2.0 (authorization code grant) with SAML as a fallback; OAuth client credentials are issued by KU Leuven on reque
  name: KU Leuven Individual Timetable (Uurrooster) API
  slug: timetable
- description: The Access API from KU Leuven — 23 operation(s) for access.
  name: KU Leuven Access API
  slug: ku-leuven-access-api
- description: Uploads a set of files to a dataset
  name: KU Leuven addFilesToDataset API
  slug: ku-leuven-addfilestodataset-api
- description: Uploads a file for a dataset
  name: KU Leuven addFileToDataset API
  slug: ku-leuven-addfiletodataset-api
- description: Uploads a Globus file for a dataset
  name: KU Leuven addGlobusFilesToDataset API
  slug: ku-leuven-addglobusfilestodataset-api
- description: The Admin API from KU Leuven — 131 operation(s) for admin.
  name: KU Leuven Admin API
  slug: ku-leuven-admin-api
- description: The Batch API from KU Leuven — 3 operation(s) for batch.
  name: KU Leuven Batch API
  slug: ku-leuven-batch-api
- description: The Builtin Users API from KU Leuven — 4 operation(s) for builtin users.
  name: KU Leuven Builtin Users API
  slug: ku-leuven-builtin-users-api
- description: The Datasetfields API from KU Leuven — 1 operation(s) for datasetfields.
  name: KU Leuven Datasetfields API
  slug: ku-leuven-datasetfields-api
- description: The Datasets API from KU Leuven — 92 operation(s) for datasets.
  name: KU Leuven Datasets API
  slug: ku-leuven-datasets-api
- description: The Datatags API from KU Leuven — 1 operation(s) for datatags.
  name: KU Leuven Datatags API
  slug: ku-leuven-datatags-api
- description: The DataverseFeaturedItems API from KU Leuven — 1 operation(s) for dataversefeatureditems.
  name: KU Leuven DataverseFeaturedItems API
  slug: ku-leuven-dataversefeatureditems-api
- description: The Dataverses API from KU Leuven — 39 operation(s) for dataverses.
  name: KU Leuven Dataverses API
  slug: ku-leuven-dataverses-api
- description: The Edit API from KU Leuven — 1 operation(s) for edit.
  name: KU Leuven Edit API
  slug: ku-leuven-edit-api
- description: The ExternalTools API from KU Leuven — 2 operation(s) for externaltools.
  name: KU Leuven ExternalTools API
  slug: ku-leuven-externaltools-api
- description: The Files API from KU Leuven — 20 operation(s) for files.
  name: KU Leuven Files API
  slug: ku-leuven-files-api
- description: The Harvest API from KU Leuven — 7 operation(s) for harvest.
  name: KU Leuven Harvest API
  slug: ku-leuven-harvest-api
- description: The Inbox API from KU Leuven — 1 operation(s) for inbox.
  name: KU Leuven Inbox API
  slug: ku-leuven-inbox-api
- description: The Info API from KU Leuven — 49 operation(s) for info.
  name: KU Leuven Info API
  slug: ku-leuven-info-api
- description: The Ingest API from KU Leuven — 1 operation(s) for ingest.
  name: KU Leuven Ingest API
  slug: ku-leuven-ingest-api
- description: The Licenses API from KU Leuven — 6 operation(s) for licenses.
  name: KU Leuven Licenses API
  slug: ku-leuven-licenses-api
- description: The Localcontexts API from KU Leuven — 2 operation(s) for localcontexts.
  name: KU Leuven Localcontexts API
  slug: ku-leuven-localcontexts-api
- description: The Logout API from KU Leuven — 1 operation(s) for logout.
  name: KU Leuven Logout API
  slug: ku-leuven-logout-api
- description: The Mail API from KU Leuven — 1 operation(s) for mail.
  name: KU Leuven Mail API
  slug: ku-leuven-mail-api
- description: The Meta API from KU Leuven — 2 operation(s) for meta.
  name: KU Leuven Meta API
  slug: ku-leuven-meta-api
- description: The Metadatablocks API from KU Leuven — 2 operation(s) for metadatablocks.
  name: KU Leuven Metadatablocks API
  slug: ku-leuven-metadatablocks-api
- description: The Mydata API from KU Leuven — 1 operation(s) for mydata.
  name: KU Leuven Mydata API
  slug: ku-leuven-mydata-api
- description: The Notifications API from KU Leuven — 6 operation(s) for notifications.
  name: KU Leuven Notifications API
  slug: ku-leuven-notifications-api
- description: The Pids API from KU Leuven — 6 operation(s) for pids.
  name: KU Leuven Pids API
  slug: ku-leuven-pids-api
- description: Replace a file to a dataset
  name: KU Leuven replaceFilesInDataset API
  slug: ku-leuven-replacefilesindataset-api
- description: The Roles API from KU Leuven — 3 operation(s) for roles.
  name: KU Leuven Roles API
  slug: ku-leuven-roles-api
- description: Save Auxiliary File With Version
  name: KU Leuven saveAuxiliaryFileWithVersion API
  slug: ku-leuven-saveauxiliaryfilewithversion-api
- description: The Search API from KU Leuven — 2 operation(s) for search.
  name: KU Leuven Search API
  slug: ku-leuven-search-api
- description: The Sendfeedback API from KU Leuven — 1 operation(s) for sendfeedback.
  name: KU Leuven Sendfeedback API
  slug: ku-leuven-sendfeedback-api
- description: Uploads a logo for a dataset
  name: KU Leuven uploadDatasetLogo API
  slug: ku-leuven-uploaddatasetlogo-api
- description: The Users API from KU Leuven — 10 operation(s) for users.
  name: KU Leuven Users API
  slug: ku-leuven-users-api
- description: The Workflows API from KU Leuven — 1 operation(s) for workflows.
  name: KU Leuven Workflows API
  slug: ku-leuven-workflows-api
artifact_total: 59
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ku-leuven-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ku-leuven-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ku-leuven-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kuleuven.be
- group: start
  title: ''
  type: DeveloperPortal
  url: https://admin.kuleuven.be/icts/services/dataservices
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kuleuven
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/ku-leuven/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/KU-Leuven-Libraries
- group: commercial
  title: ''
  type: Plans
  url: plans/ku-leuven-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ku-leuven-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ku-leuven-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'KU Leuven (Katholieke Universiteit Leuven) is a research university in Leuven, Belgium, founded in 1425 and ranked #45 in the QS World University Rankings 2025. It maintains a documented public developer footprint through its ICTS Data Services, which expose REST APIs for person/who-is-who information, curriculum information, organizational-chart data, research information, educational offerings, and job vacancies, alongside an OAuth-protected individual timetable API. KU Leuven also operates the Research Data Repository (RDR), a Dataverse-based institutional repository whose REST API is publicly reachable, and runs an active official GitHub organization.'
examples:
- key_count: 2
  name: Ku Leuven Dataset Example
  slug: ku-leuven-dataset-example
- key_count: 2
  name: Ku Leuven Info Version Example
  slug: ku-leuven-info-version-example
finops:
- name: Ku Leuven Finops
  service_category: Education
  slug: ku-leuven-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ku-leuven.png
json_schemas:
- name: KU Leuven RDR DataFile
  property_count: 12
  slug: ku-leuven-datafile
- name: KU Leuven RDR Dataset
  property_count: 14
  slug: ku-leuven-dataset
- name: KU Leuven RDR DatasetVersion
  property_count: 13
  slug: ku-leuven-datasetversion
- name: KU Leuven RDR Info Version Response
  property_count: 2
  slug: ku-leuven-info-version
json_structures:
- name: Ku Leuven Datafile Structure
  property_count: 11
  slug: ku-leuven-datafile-structure
- name: Ku Leuven Dataset Structure
  property_count: 14
  slug: ku-leuven-dataset-structure
- name: Ku Leuven Datasetversion Structure
  property_count: 12
  slug: ku-leuven-datasetversion-structure
jsonld:
- class_count: 16
  name: Ku Leuven Context
  property_count: 3
  slug: ku-leuven-context
layout: provider
modified: '2026-06-03'
name: KU Leuven
nav: Providers
network: true
overview: 'KU Leuven publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Access API, addFilesToDataset API, addFileToDataset API, and 33 more. Tagged areas include Education, Higher Education, University, Research Data, and Open Data.


  The KU Leuven catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  KU Leuven''s developer surface includes GitHub presence and 11 more developer resources.'
plans:
- name: Ku Leuven Plans Pricing
  plan_count: 2
  slug: ku-leuven-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Ku Leuven Rate Limits
  slug: ku-leuven-rate-limits
rules:
- name: KU Leuven API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ku-leuven-jsonschema-spectral-rules
- name: KU Leuven API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 2
  slug: ku-leuven-rules
score:
  band: thin
  composite: 36.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.4
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ku-leuven/refs/heads/main/screenshots/ku-leuven-2026-06-20T184201.png
security:
- kind: domain-security
  name: Ku Leuven Domain Security
  slug: ku-leuven-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ku Leuven Vulnerability Disclosure
  slug: ku-leuven-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ku-leuven
tags:
- Education
- Higher Education
- University
- Research Data
- Open Data
- Belgium
- Europe
website: https://www.kuleuven.be
---

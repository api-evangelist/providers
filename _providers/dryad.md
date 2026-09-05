---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Dryad Agentic Access
  operation_count: 25
  slug: dryad-agentic-access
  summary_line: 25 operations · 9 acting
api_count: 1
apis:
- baseURL: https://datadryad.org/api/v2
  baseurl_source: declared
  description: Dataset operations
  name: Dryad datasets API
  slug: dryad-datasets-api
- baseURL: https://datadryad.org/api/v2
  baseurl_source: declared
  description: Operations on individual files of a dataset
  name: Dryad files API
  slug: dryad-files-api
- baseURL: https://datadryad.org/api/v2
  baseurl_source: declared
  description: Internal APIs not of general interest to the public
  name: Dryad internal API
  slug: dryad-internal-api
- baseURL: https://datadryad.org/api/v2
  baseurl_source: declared
  description: Reports on content in Dryad
  name: Dryad reports API
  slug: dryad-reports-api
- baseURL: https://datadryad.org/api/v2
  baseurl_source: declared
  description: Root-level API calls
  name: Dryad root API
  slug: dryad-root-api
- baseURL: https://datadryad.org/api/v2
  baseurl_source: declared
  description: Searching datasets
  name: Dryad search API
  slug: dryad-search-api
- baseURL: https://datadryad.org/api/v2
  baseurl_source: declared
  description: Operations on individual versions of a dataset
  name: Dryad versions API
  slug: dryad-versions-api
artifact_total: 74
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dryad datasets API
  slug: open-dryad-datasets-api
- collection_type: open
  name: Dryad datasets files API
  slug: open-dryad-files-api
- collection_type: open
  name: Dryad datasets internal API
  slug: open-dryad-internal-api
- collection_type: open
  name: Dryad datasets reports API
  slug: open-dryad-reports-api
- collection_type: open
  name: Dryad datasets root API
  slug: open-dryad-root-api
- collection_type: open
  name: Dryad datasets search API
  slug: open-dryad-search-api
- collection_type: open
  name: Dryad datasets versions API
  slug: open-dryad-versions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/dryad-capability-edges.yml
- group: operate
  title: ''
  type: Releases
  url: https://github.com/datadryad/dryad-app/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/datadryad/dryad-app/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dryad-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dryad-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dryad-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://github.com/datadryad/dryad-app/blob/main/documentation/apis/api_accounts.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datadryad.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datadryad.org/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://datadryad.org/help/requirements/costs
- group: operate
  title: ''
  type: Contact
  url: https://datadryad.org/contact
- group: company
  title: ''
  type: Blog
  url: https://blog.datadryad.org
- group: build
  title: ''
  type: GitHub
  url: https://github.com/datadryad
- group: start
  title: ''
  type: Signup
  url: https://datadryad.org/account
- group: company
  title: ''
  type: InstitutionalPartners
  url: https://datadryad.org/institutions
- group: company
  title: ''
  type: PublisherPartners
  url: https://datadryad.org/publishers
description: Dryad is a nonprofit open data publishing platform and repository that enables researchers to publish, preserve, and access research datasets. It provides a REST API for submitting, updating, and retrieving datasets associated with peer-reviewed publications in biology, ecology, and related disciplines.
examples:
- key_count: 1
  name: Delete Files Id Response 403
  slug: delete-files-id-response-403
- key_count: 1
  name: Get Reports Name Response 404
  slug: get-reports-name-response-404
- key_count: 1
  name: Get Reports Name Response 500
  slug: get-reports-name-response-500
- key_count: 1
  name: Get Search Response 400
  slug: get-search-response-400
- key_count: 1
  name: Get Versions Id Download Response 404
  slug: get-versions-id-download-response-404
- key_count: 1
  name: Patch Datasets Doi Response 403
  slug: patch-datasets-doi-response-403
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://datadryad.org/images/logo.png
json_schemas:
- name: Error
  property_count: 1
  slug: Error
- name: Admin Values
  property_count: 11
  slug: admin_values
- name: Author
  property_count: 9
  slug: author
- name: Dataset
  property_count: 0
  slug: dataset
- name: Dataset Links
  property_count: 1
  slug: dataset_links
- name: Dataset Submission
  property_count: 3
  slug: dataset_submission
- name: Datasets
  property_count: 0
  slug: datasets
- name: Dc Metadata
  property_count: 11
  slug: dc_metadata
- name: Embargo
  property_count: 1
  slug: embargo
- name: Embedded Datasets
  property_count: 1
  slug: embedded_datasets
- name: Embedded Files
  property_count: 1
  slug: embedded_files
- name: Embedded Versions
  property_count: 1
  slug: embedded_versions
- name: File
  property_count: 0
  slug: file
- name: File Links
  property_count: 1
  slug: file_links
- name: Files
  property_count: 0
  slug: files
- name: Funder
  property_count: 6
  slug: funder
- name: Geolocation
  property_count: 3
  slug: geolocation
- name: Geolocationbox
  property_count: 4
  slug: geolocationBox
- name: Geolocationpoint
  property_count: 2
  slug: geolocationPoint
- name: Hal Curie
  property_count: 3
  slug: hal_curie
- name: Hal Dataset Links
  property_count: 4
  slug: hal_dataset_links
- name: Hal File Links
  property_count: 5
  slug: hal_file_links
- name: Hal Link
  property_count: 1
  slug: hal_link
- name: Hal Links
  property_count: 2
  slug: hal_links
- name: Hal Page Links
  property_count: 4
  slug: hal_page_links
- name: Hal Paged Response
  property_count: 0
  slug: hal_paged_response
- name: Hal Self Link
  property_count: 1
  slug: hal_self_link
- name: Hal Version Links
  property_count: 4
  slug: hal_version_links
- name: Paging Counts
  property_count: 2
  slug: paging_counts
- name: Processor Result
  property_count: 0
  slug: processor_result
- name: Processor Results
  property_count: 0
  slug: processor_results
- name: Relatedwork
  property_count: 3
  slug: relatedWork
- name: Related Type
  property_count: 1
  slug: related_type
- name: Reports
  property_count: 1
  slug: reports
- name: Root
  property_count: 1
  slug: root
- name: Root Links
  property_count: 4
  slug: root_links
- name: Simple Author
  property_count: 4
  slug: simple_author
- name: Simple Version
  property_count: 0
  slug: simple_version
- name: Tenant
  property_count: 5
  slug: tenant
- name: Url
  property_count: 1
  slug: url
- name: Url Json
  property_count: 1
  slug: url_json
- name: Version
  property_count: 0
  slug: version
- name: Version Links
  property_count: 1
  slug: version_links
- name: Versions
  property_count: 0
  slug: versions
jsonld:
- class_count: 29
  name: Api Context
  property_count: 7
  slug: api
- class_count: 29
  name: context Context
  property_count: 7
  slug: context
layout: provider
modified: '2026-06-13'
name: Dryad
nav: Providers
network: true
overview: 'Dryad publishes 7 APIs on the [APIs.io](https://apis.io/) network, including datasets API, files API, internal API, and 4 more. Tagged areas include Research Data, Open Science, Data Repository, Datasets, and Biology.


  The Dryad catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Dryad''s developer surface includes authentication, pricing, engineering blog, GitHub presence, signup flow, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 7
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Dryad API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dryad-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.3
    catalog_earned_first_party: 0.0
    catalog_gap: 40.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 25.0
    contract_quality: 63.5
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 21.1
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dryad/refs/heads/main/screenshots/dryad-2026-06-20T180256.png
security:
- kind: authentication
  name: Dryad Authentication
  slug: dryad-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dryad Domain Security
  slug: dryad-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dryad
tags:
- Research Data
- Open Science
- Data Repository
- Datasets
- Biology
- Ecology
- Open Access
---

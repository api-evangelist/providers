---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - '{''url'': ''https://www.centaurlabs.com/'', ''status'': 301, ''note'': ''declared website redirects to https://centaur.ai/ — a different registrable domain (centaurlabs.com -> centaur.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 51
  human_in_the_loop: 3
  name: Centaur Labs Agentic Access
  operation_count: 76
  slug: centaur-labs-agentic-access
  summary_line: 76 operations · 51 acting · 3 human-in-the-loop
api_count: 5
apis:
- description: Public REST API for importing data and managing labeling projects, tasks, cases, assets, gold standards, prelabels, tags and for downloading aggregated labeling results. Split across several versioned
  name: Centaur Public API
  slug: centaur-public-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: Set and remove gold standard answers and prelabels on the cases in a task.
  name: Centaur Labs Add and Manage Labels API
  slug: centaur-labs-add-and-manage-labels-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: Create, update, list, and delete projects.
  name: Centaur Labs Add and Manage Projects API
  slug: centaur-labs-add-and-manage-projects-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: Create and configure labeling tasks, including their answer classes, label class groups, and instructions.
  name: Centaur Labs Add and Manage Tasks API
  slug: centaur-labs-add-and-manage-tasks-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: Create, duplicate, update, and delete the individual cases that labelers work on.
  name: Centaur Labs Create and Manage Cases API
  slug: centaur-labs-create-and-manage-cases-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: The Get API Version API from Centaur Labs — 4 operation(s) for get api version.
  name: Centaur Labs Get API Version API
  slug: centaur-labs-get-api-version-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: The Get Case Results API from Centaur Labs — 2 operation(s) for get case results.
  name: Centaur Labs Get Case Results API
  slug: centaur-labs-get-case-results-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: The Get Task Results API from Centaur Labs — 3 operation(s) for get task results.
  name: Centaur Labs Get Task Results API
  slug: centaur-labs-get-task-results-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: Import assets from cloud storage or URLs, and manage the resulting assets and file manifests.
  name: Centaur Labs Import and Manage Data API
  slug: centaur-labs-import-and-manage-data-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: The Login API from Centaur Labs — 1 operation(s) for login.
  name: Centaur Labs Login API
  slug: centaur-labs-login-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: The Logout API from Centaur Labs — 1 operation(s) for logout.
  name: Centaur Labs Logout API
  slug: centaur-labs-logout-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: The masks-public API from Centaur Labs — 2 operation(s) for masks-public.
  name: Centaur Labs Masks Public API
  slug: centaur-labs-masks-public-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: The Reads (Opinions) Lookup API from Centaur Labs — 1 operation(s) for reads (opinions) lookup.
  name: Centaur Labs Reads (Opinions) Lookup API
  slug: centaur-labs-reads-opinions-lookup-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: The Refresh Token API from Centaur Labs — 1 operation(s) for refresh token.
  name: Centaur Labs Refresh Token API
  slug: centaur-labs-refresh-token-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: Organize cases and assets by applying, removing, and listing tags.
  name: Centaur Labs Tags API
  slug: centaur-labs-tags-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: The Test Token API from Centaur Labs — 1 operation(s) for test token.
  name: Centaur Labs Test Token API
  slug: centaur-labs-test-token-api
- baseURL: https://api.centaurlabs.com
  baseurl_source: declared
  description: Report the running version of the Ingest API.
  name: Centaur Labs Version API
  slug: centaur-labs-version-api
artifact_total: 44
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/agentic-access/centaur-labs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/centaur-labs-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/rules/centaur-labs-rules.yml
  title: ''
  type: Spectral
  url: rules/centaur-labs-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/json-ld/centaur-labs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/centaur-labs-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/vocabulary/centaur-labs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/centaur-labs-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/errors/centaur-labs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/centaur-labs-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/hosts/centaur-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centaur-labs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/vendors/centaur-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centaur-labs-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://go.centaurlabs.com/playground
- group: company
  title: ''
  type: Newsroom
  url: https://centaur.ai/news
- group: company
  title: ''
  type: Website
  url: https://www.centaurlabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://go.centaurlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.centaurlabs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.centaurlabs.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.centaurlabs.com/docs/getting-started-1
- group: company
  title: ''
  type: Blog
  url: https://centaur.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.centaurlabs.com/docs/get-support
- group: start
  title: ''
  type: SignUp
  url: https://go.centaurlabs.com/signup
- group: start
  title: ''
  type: Login
  url: https://go.centaurlabs.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://centaur.ai/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.centaurlabs.com/changelog/welcome-to-centaur
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/conformance/centaur-labs-conformance.yml
  title: ''
  type: Compliance
  url: conformance/centaur-labs-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/security/centaur-labs-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/centaur-labs-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/security/centaur-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centaur-labs-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/well-known/centaur-labs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/centaur-labs-well-known.yml
created: '2026-07-17'
description: Centaur Labs (centaur.ai) provides expert data annotation and labeling for healthcare and scientific AI. Its platform combines large crowds of vetted human experts with AI models in a competitive "collective intelligence" model to produce high-quality, aggregated training labels across images, text, audio, video, waveform and DICOM medical imaging. Centaur exposes a public REST API (api.centaurlabs.com) for importing data, creating and managing labeling projects, tasks, cases, gold standards, tags and prelabels, and for downloading aggregated results. The company is SOC 2 Type II audited and HIPAA compliant, was founded by Erik Duhaime out of the MIT Center for Collective Intelligence, and is backed by Accel and Matrix Partners.
image: https://files.readme.io/90ad1dc-small-Centaur_Labs_black3x.png
json_schemas:
- name: CaseResultList
  property_count: 4
  slug: centaur-labs-case-result-list
- name: CaseResult
  property_count: 19
  slug: centaur-labs-case-result
- name: CommitMasksRequestPublicApi
  property_count: 2
  slug: centaur-labs-commit-masks-request-public-api
- name: CommitMasksResponse
  property_count: 2
  slug: centaur-labs-commit-masks-response
- name: ExistingTaskClassification
  property_count: 19
  slug: centaur-labs-existing-task-classification
- name: ExistingTaskClassification_V2
  property_count: 20
  slug: centaur-labs-existing-task-classification-v2
- name: ExistingTaskRange
  property_count: 19
  slug: centaur-labs-existing-task-range
- name: ExistingTaskSegmentation
  property_count: 19
  slug: centaur-labs-existing-task-segmentation
- name: GeneratePresignedURLsRequest
  property_count: 3
  slug: centaur-labs-generate-presigned-urls-request
- name: GeneratePresignedURLsResponse
  property_count: 3
  slug: centaur-labs-generate-presigned-urls-response
- name: MessageResponse
  property_count: 1
  slug: centaur-labs-message-response
- name: PublicLoginRequest
  property_count: 2
  slug: centaur-labs-public-login-request
- name: PublicLoginResponse
  property_count: 8
  slug: centaur-labs-public-login-response
- name: ReadsLookupRequest
  property_count: 3
  slug: centaur-labs-reads-lookup-request
- name: ReadsLookup
  property_count: 3
  slug: centaur-labs-reads-lookup
- name: RefreshTokenResponse
  property_count: 1
  slug: centaur-labs-refresh-token-response
- name: ResultListV1
  property_count: 4
  slug: centaur-labs-result-list-v1
- name: ResultV1
  property_count: 16
  slug: centaur-labs-result-v1
- name: TaskClassification_V2
  property_count: 16
  slug: centaur-labs-task-classification-v2
- name: TaskRange_V2
  property_count: 16
  slug: centaur-labs-task-range-v2
- name: VersionResponse
  property_count: 1
  slug: centaur-labs-version-response
jsonld:
- class_count: 120
  name: Centaur Labs Context
  property_count: 203
  slug: centaur-labs-context
layout: provider
modified: '2026-07-18'
name: Centaur Labs
nav: Providers
network: true
overview: 'Centaur Labs publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Add and Manage Labels API, Add and Manage Projects API, Add and Manage Tasks API, and 14 more. Tagged areas include Company, Artificial Intelligence, Data Annotation, Data Labeling, and Machine Learning.


  The Centaur Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Centaur Labs'' developer surface includes sandbox, documentation, API reference, getting-started guide, engineering blog, support, signup flow, and 17 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Centaur Labs API Rules
  rule_count: 14
  severity_counts:
    error: 7
    hint: 0
    info: 2
    warn: 5
  slug: centaur-labs-rules
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.2
  facets:
    access_clarity: 32.9
    contract_governance: 35.6
    contract_quality: 66.5
    developer_ergonomics: 44.6
    discoverability: 80.4
    operational_transparency: 15.8
  previous_composite: 26.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/centaur-labs/refs/heads/main/screenshots/centaur-labs-2026-07-25T204921.png
security:
- kind: authentication
  name: Centaur Labs Authentication
  slug: centaur-labs-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Centaur Labs Domain Security
  slug: centaur-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Centaur Labs Trust Center
  slug: centaur-labs-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: centaur-labs
tags:
- Company
- Artificial Intelligence
- Data Annotation
- Data Labeling
- Machine Learning
- Healthcare
- Medical Imaging
- Training Data
website: https://www.centaurlabs.com/
---

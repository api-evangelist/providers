---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 26.3
  scored_at: '2026-10-17'
api_count: 12
apis:
- description: Google Dataplex REST API for managing lakes, zones, and assets.
  name: Dataplex REST API
  slug: dataplex-rest-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Apt API from Google Dataplex — 1 operation(s) for apt.
  name: Google Dataplex Apt API
  slug: google-dataplex-apt-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Auth API from Google Dataplex — 1 operation(s) for auth.
  name: Google Dataplex Auth API
  slug: google-dataplex-auth-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Computemetadata API from Google Dataplex — 1 operation(s) for computemetadata.
  name: Google Dataplex Computemetadata API
  slug: google-dataplex-computemetadata-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Dl API from Google Dataplex — 2 operation(s) for dl.
  name: Google Dataplex Dl API
  slug: google-dataplex-dl-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Documents Analyzeentities API from Google Dataplex — 1 operation(s) for documents analyzeentities.
  name: Google Dataplex Documents Analyzeentities API
  slug: google-dataplex-documents-analyzeentities-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Drive API from Google Dataplex — 1 operation(s) for drive.
  name: Google Dataplex Drive API
  slug: google-dataplex-drive-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Google Dataplex API API from Google Dataplex — 2 operation(s) for google dataplex api.
  name: Google Dataplex Google Dataplex API
  slug: google-dataplex-google-dataplex-api-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Instance API from Google Dataplex — 1 operation(s) for instance.
  name: Google Dataplex Instance API
  slug: google-dataplex-instance-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Language API from Google Dataplex — 1 operation(s) for language.
  name: Google Dataplex Language API
  slug: google-dataplex-language-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Projects API from Google Dataplex — 4 operation(s) for projects.
  name: Google Dataplex Projects API
  slug: google-dataplex-projects-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The V1Beta API from Google Dataplex — 1 operation(s) for v1beta.
  name: Google Dataplex V1Beta API
  slug: google-dataplex-v1beta-api
artifact_total: 21
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-dataplex/refs/heads/main/rules/google-dataplex-rules.yml
  title: ''
  type: Spectral
  url: rules/google-dataplex-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-dataplex/refs/heads/main/json-ld/google-dataplex-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-dataplex-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-dataplex/refs/heads/main/vocabulary/google-dataplex-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/google-dataplex-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-dataplex/refs/heads/main/data-model/google-dataplex-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-dataplex-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/google-dataplex/refs/heads/main/conformance/google-dataplex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-dataplex-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-dataplex/refs/heads/main/well-known/google-dataplex-google-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-dataplex-google-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-dataplex/refs/heads/main/well-known/google-dataplex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-dataplex-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/google-dataplex/refs/heads/main/hosts/google-dataplex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/google-dataplex-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: auth
  title: ''
  type: Security
  url: https://accounts.google.com/ServiceLogin?hl=en-US&continue=https://myaccount.google.com/intro/security
- group: start
  title: ''
  type: Sandbox
  url: https://play.google.com/console/about/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: start
  title: ''
  type: Login
  url: https://accounts.google.com/v3/signin/identifier?continue=https://docs.google.com/&emr=1&followup=https://docs.google.com/&osid=1&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1697375348:1791925185981580
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.googleblog.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-dataplex/refs/heads/main/security/google-dataplex-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-dataplex-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-dataplex/refs/heads/main/security/google-dataplex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-dataplex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com/dataplex
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloud.google.com/knowledge-catalog/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/dataplex/docs/quickstart-guide
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/dataplex/pricing
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://cloud.google.com/dataplex/docs/release-notes
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cloud.google.com/dataplex
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Google Dataplex, now known as Google Cloud Knowledge Catalog, is a unified data governance and metadata management service that helps organizations discover, curate, and manage data assets across Google Cloud services and external sources. It provides automated metadata harvesting, semantic enrichment, data lineage, and policy enforcement, enabling AI agents and users to reliably access high‑quality, contextualized data. The platform supports integration with BigQuery, Cloud Storage, Looker, and third‑party catalogs, offering searchable, governed data products for analytics and machine learning workloads.
image: https://www.gstatic.com/bricks/image/cloud_google_com__static_cloud_images_social_icon_google_cloud_1200_630_png.png
json_schemas:
- name: GetComputemetadataV1InstanceServiceAccountsDefaultDefaultidR
  property_count: 3
  slug: google-dataplex-get-computemetadata-v1-instance-service-accounts-default-defaultid-r
- name: PostRequest
  property_count: 4
  slug: google-dataplex-post-request
- name: PostV1BetaModelsGemini35FlashGeneratecontentRequest
  property_count: 1
  slug: google-dataplex-post-v1-beta-models-gemini35-flash-generatecontent-request
- name: PostV1ProjectsServiceaccountsRequest
  property_count: 2
  slug: google-dataplex-post-v1-projects-serviceaccounts-request
- name: PostV2ProjectsRequest
  property_count: 2
  slug: google-dataplex-post-v2-projects-request
jsonld:
- class_count: 5
  name: Google Dataplex Context
  property_count: 12
  slug: google-dataplex-context
layout: provider
modified: '2026-10-13'
name: Google Dataplex
nav: Providers
network: true
overview: 'Google Dataplex is listed with 12 APIs on the [APIs.io](https://apis.io/) network, including Apt API, Auth API, Computemetadata API, and 9 more. Tagged areas include Company, Data Governance, Metadata Management, Google Cloud, and AI Agents.


  The Google Dataplex catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Dataplex''s developer surface includes sandbox, documentation, getting-started guide, pricing, release notes, and 16 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Google Dataplex API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: google-dataplex-rules
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 38.1
    discoverability: 62.5
    operational_transparency: 26.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Google Dataplex Domain Security
  slug: google-dataplex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Dataplex Vulnerability Disclosure
  slug: google-dataplex-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-dataplex
tags:
- Company
- Data Governance
- Metadata Management
- Google Cloud
- AI Agents
website: https://cloud.google.com/dataplex
---

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
api_count: 11
apis:
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Apt API from Vertex AI Search — 1 operation(s) for apt.
  name: Vertex AI Search Apt API
  slug: vertex-ai-search-apt-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Auth API from Vertex AI Search — 1 operation(s) for auth.
  name: Vertex AI Search Auth API
  slug: vertex-ai-search-auth-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Computemetadata API from Vertex AI Search — 1 operation(s) for computemetadata.
  name: Vertex AI Search Computemetadata API
  slug: vertex-ai-search-computemetadata-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Dl API from Vertex AI Search — 2 operation(s) for dl.
  name: Vertex AI Search Dl API
  slug: vertex-ai-search-dl-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Documents Analyzeentities API from Vertex AI Search — 1 operation(s) for documents analyzeentities.
  name: Vertex AI Search Documents Analyzeentities API
  slug: vertex-ai-search-documents-analyzeentities-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Drive API from Vertex AI Search — 1 operation(s) for drive.
  name: Vertex AI Search Drive API
  slug: vertex-ai-search-drive-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Language API from Vertex AI Search — 1 operation(s) for language.
  name: Vertex AI Search Language API
  slug: vertex-ai-search-language-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Projects API from Vertex AI Search — 3 operation(s) for projects.
  name: Vertex AI Search Projects API
  slug: vertex-ai-search-projects-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Tokeninfo API from Vertex AI Search — 1 operation(s) for tokeninfo.
  name: Vertex AI Search Tokeninfo API
  slug: vertex-ai-search-tokeninfo-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The V1Beta API from Vertex AI Search — 2 operation(s) for v1beta.
  name: Vertex AI Search V1Beta API
  slug: vertex-ai-search-v1beta-api
- baseURL: https://packages.cloud.google.com
  baseurl_source: declared
  description: The Vertex AI Search API API from Vertex AI Search — 2 operation(s) for vertex ai search api.
  name: Vertex AI Search Vertex AI Search API
  slug: vertex-ai-search-vertex-ai-search-api-api
artifact_total: 21
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vertex-ai-search/refs/heads/main/rules/vertex-ai-search-rules.yml
  title: ''
  type: Spectral
  url: rules/vertex-ai-search-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vertex-ai-search/refs/heads/main/json-ld/vertex-ai-search-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vertex-ai-search-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vertex-ai-search/refs/heads/main/vocabulary/vertex-ai-search-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vertex-ai-search-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vertex-ai-search/refs/heads/main/data-model/vertex-ai-search-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vertex-ai-search-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vertex-ai-search/refs/heads/main/conformance/vertex-ai-search-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vertex-ai-search-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vertex-ai-search/refs/heads/main/well-known/vertex-ai-search-google-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vertex-ai-search-google-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vertex-ai-search/refs/heads/main/well-known/vertex-ai-search-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vertex-ai-search-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/vertex-ai-search/refs/heads/main/hosts/vertex-ai-search-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vertex-ai-search-hosts.yml
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
  url: https://accounts.google.com/v3/signin/identifier?continue=https://docs.google.com/&emr=1&followup=https://docs.google.com/&osid=1&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S456074708:1791925249456281
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloud.google.com/docs/get-started/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vertex-ai-search/refs/heads/main/security/vertex-ai-search-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vertex-ai-search-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vertex-ai-search/refs/heads/main/security/vertex-ai-search-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vertex-ai-search-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/ai-machine-learning/vertex-ai-search-and-conversation-is-now-generally-available
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search/docs
coverage:
  checked: '2026-10-13'
  detail: The product page https://cloud.google.com/vertex-ai-search returns a 404, providing no machine‑readable API specification.
  evidence:
  - status: 404
    url: https://cloud.google.com/vertex-ai-search
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Vertex AI Search is Google Cloud’s enterprise search solution that leverages generative AI to enable organizations to index, search, and retrieve information across structured and unstructured data sources. It integrates with Vertex AI, BigQuery, and other Google Cloud services to provide semantic search, relevance tuning, and secure access controls, helping businesses unlock insights from their data at scale.
image: https://cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png
json_schemas:
- name: GetComputemetadataV1InstanceServiceAccountsDefaultDefaultidR
  property_count: 3
  slug: vertex-ai-search-get-computemetadata-v1-instance-service-accounts-default-defaultid-r
- name: GetTokeninfoResponse
  property_count: 8
  slug: vertex-ai-search-get-tokeninfo-response
- name: PostRequest
  property_count: 4
  slug: vertex-ai-search-post-request
- name: PostV1BetaModelsGemini35FlashGeneratecontentRequest
  property_count: 1
  slug: vertex-ai-search-post-v1-beta-models-gemini35-flash-generatecontent-request
- name: PostV1ProjectsServiceaccountsRequest
  property_count: 2
  slug: vertex-ai-search-post-v1-projects-serviceaccounts-request
- name: PostV2ProjectsRequest
  property_count: 2
  slug: vertex-ai-search-post-v2-projects-request
jsonld:
- class_count: 6
  name: Vertex Ai Search Context
  property_count: 19
  slug: vertex-ai-search-context
layout: provider
modified: '2026-10-13'
name: Vertex AI Search
nav: Providers
network: true
overview: 'Vertex AI Search is listed with 11 APIs on the [APIs.io](https://apis.io/) network, including Apt API, Auth API, Computemetadata API, and 8 more. Tagged areas include Company, Artificial Intelligence, Search, Enterprise, and Google Cloud.


  The Vertex AI Search catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Vertex AI Search''s developer surface includes sandbox, getting-started guide, engineering blog, documentation, and 16 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Vertex AI Search API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: vertex-ai-search-rules
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 25.6
    developer_ergonomics: 40.5
    discoverability: 71.4
    operational_transparency: 10.5
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
    score: 28.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Vertex Ai Search Domain Security
  slug: vertex-ai-search-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vertex Ai Search Vulnerability Disclosure
  slug: vertex-ai-search-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vertex-ai-search
tags:
- Company
- Artificial Intelligence
- Search
- Enterprise
- Google Cloud
website: https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search
---

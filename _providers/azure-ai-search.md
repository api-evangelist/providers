---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-17'
api_count: 7
apis:
- description: Azure AI Search REST API
  name: Azure AI Search API
  slug: azure-ai-search-api-2
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Azure AI Search API API from Azure AI Search — 1 operation(s) for azure ai search api.
  name: Azure AI Search Azure AI Search API
  slug: azure-ai-search-azure-ai-search-api-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Indexes API from Azure AI Search — 2 operation(s) for indexes.
  name: Azure AI Search Indexes API
  slug: azure-ai-search-indexes-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Subscriptions API from Azure AI Search — 2 operation(s) for subscriptions.
  name: Azure AI Search Subscriptions API
  slug: azure-ai-search-subscriptions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Swagger API from Azure AI Search — 1 operation(s) for swagger.
  name: Azure AI Search Swagger API
  slug: azure-ai-search-swagger-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Todoitems API from Azure AI Search — 2 operation(s) for todoitems.
  name: Azure AI Search Todoitems API
  slug: azure-ai-search-todoitems-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Weatherforecast API from Azure AI Search — 1 operation(s) for weatherforecast.
  name: Azure AI Search Weatherforecast API
  slug: azure-ai-search-weatherforecast-api
artifact_total: 19
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/well-known/azure-ai-search-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/azure-ai-search-www-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/well-known/azure-ai-search-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/azure-ai-search-well-known.yml
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.microsoft.com/privacy?icid=DSM_Footer_Company_Privacy
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/rules/azure-ai-search-rules.yml
  title: ''
  type: Spectral
  url: rules/azure-ai-search-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/json-ld/azure-ai-search-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/azure-ai-search-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/vocabulary/azure-ai-search-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/azure-ai-search-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/data-model/azure-ai-search-data-model.yml
  title: ''
  type: DataModel
  url: data-model/azure-ai-search-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/authentication/azure-ai-search-authentication.yml
  title: ''
  type: Authentication
  url: authentication/azure-ai-search-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/conformance/azure-ai-search-conformance.yml
  title: ''
  type: Conformance
  url: conformance/azure-ai-search-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/llms/azure-ai-search-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/azure-ai-search-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/hosts/azure-ai-search-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azure-ai-search-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/vendors/azure-ai-search-vendors.yml
  title: ''
  type: Vendors
  url: vendors/azure-ai-search-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/community
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/security/azure-ai-search-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/azure-ai-search-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azure-ai-search/refs/heads/main/security/azure-ai-search-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azure-ai-search-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/products/ai-services/ai-search
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/search/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/searchservice/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/search/search-get-started-text
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/search/
coverage:
  checked: '2026-10-13'
  detail: Documentation pages exist but no machine‑readable OpenAPI or other contract was found.
  evidence:
  - status: 200
    url: https://learn.microsoft.com/en-us/rest/api/searchservice/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Azure AI Search is a cloud-based search-as-a-service offering from Microsoft Azure, providing powerful AI-driven indexing, semantic search, and customizable relevance tuning for developers and enterprises. It enables integration of advanced search capabilities into applications, supporting full-text, vector, and hybrid search scenarios, with built-in security, scaling, and monitoring features. This service is part of Azure AI Services, delivering intelligent information retrieval across structured and unstructured data.
json_schemas:
- name: GetResponse
  property_count: 3
  slug: azure-ai-search-get-response
- name: GetSwaggerV1SwaggerJsonResponse
  property_count: 1
  slug: azure-ai-search-get-swagger-v1-swagger-json-response
- name: GetWeatherforecastResponse
  property_count: 1
  slug: azure-ai-search-get-weatherforecast-response
- name: PatchTodoitemsIdRequest
  property_count: 1
  slug: azure-ai-search-patch-todoitems-id-request
- name: PostTodoitemsRequest
  property_count: 1
  slug: azure-ai-search-post-todoitems-request
- name: PutTodoitemsIdRequest
  property_count: 1
  slug: azure-ai-search-put-todoitems-id-request
jsonld:
- class_count: 9
  name: Azure Ai Search Context
  property_count: 3
  slug: azure-ai-search-context
layout: provider
modified: '2026-10-13'
name: Azure AI Search
nav: Providers
network: true
overview: 'Azure AI Search is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Azure AI Search API, Indexes API, Subscriptions API, and 4 more. Tagged areas include Artificial Intelligence, Search, Microsoft Azure, Cloud, and Services.


  The Azure AI Search catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure AI Search''s developer surface includes support, engineering blog, authentication, changelog, documentation, API reference, getting-started guide, and 18 more developer resources.'
plans:
- name: Azure Ai Search Plans Pricing
  plan_count: 0
  slug: azure-ai-search-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Azure AI Search API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: azure-ai-search-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 27.2
    developer_ergonomics: 57.1
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Azure Ai Search Authentication
  slug: azure-ai-search-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Azure Ai Search Domain Security
  slug: azure-ai-search-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Azure Ai Search Vulnerability Disclosure
  slug: azure-ai-search-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: azure-ai-search
tags:
- Artificial Intelligence
- Search
- Microsoft Azure
- Cloud
- Services
website: https://azure.microsoft.com/products/ai-services/ai-search
---

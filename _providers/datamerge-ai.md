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
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: DataMerge API provides endpoints for company and contact data enrichment.
  name: DataMerge API
  slug: datamerge-api
- baseURL: https://api.datamerge.ai
  baseurl_source: declared
  description: 'DataMerge API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DataMerge API
  slug: datamerge-ai-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/datamerge-ai/rules/datamerge-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/datamerge-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/datamerge-ai/json-ld/datamerge-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datamerge-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/datamerge-ai/vocabulary/datamerge-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datamerge-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datamerge-ai/data-model/datamerge-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datamerge-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/datamerge-ai/authentication/datamerge-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datamerge-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/datamerge-ai/conformance/datamerge-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datamerge-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datamerge-ai/llms/datamerge-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datamerge-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/datamerge-ai/hosts/datamerge-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datamerge-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/datamerge-ai/vendors/datamerge-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datamerge-ai-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.datamerge.ai/integrations/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datamerge.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datamerge.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datamerge.ai/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.datamerge.ai/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.datamerge.ai/developers
- group: auth
  href: https://artifacts.apis.io/datamerge-ai/security/datamerge-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datamerge-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datamerge.ai/
coverage:
  checked: '2026-11-05'
  detail: Developer portal provides documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://www.datamerge.ai/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DataMerge provides B2B company and contact data enrichment services, offering verified legal name resolution, corporate hierarchy information, and contact emails for over 375 million companies worldwide. Their platform aggregates data from more than 20 providers, enabling sales teams, founders, and solopreneurs to enrich leads with accurate company details and email addresses, with a focus on privacy and compliance.
image: https://www.datamerge.ai/og-default.png
json_schemas:
- name: DeleteV1ListsCompanyTargetAccountsRecordidResponse
  property_count: 2
  slug: datamerge-ai-delete-v1-lists-company-target-accounts-recordid-response
- name: DeleteV1ListsCompanyTargetAccountsResponse
  property_count: 2
  slug: datamerge-ai-delete-v1-lists-company-target-accounts-response
- name: GetV1CreditsBalanceResponse
  property_count: 2
  slug: datamerge-ai-get-v1-credits-balance-response
- name: GetV1ListsCompanyTargetAccountsResponse
  property_count: 2
  slug: datamerge-ai-get-v1-lists-company-target-accounts-response
- name: GetV1ListsResponse
  property_count: 2
  slug: datamerge-ai-get-v1-lists-response
- name: PostV1ContactSearchRequest
  property_count: 3
  slug: datamerge-ai-post-v1-contact-search-request
jsonld:
- class_count: 14
  name: Datamerge Ai Context
  property_count: 11
  slug: datamerge-ai-context
layout: provider
modified: '2026-11-05'
name: DataMerge
nav: Providers
network: true
overview: 'DataMerge is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Enrichment, B2B, Contact Data, and Company Data.


  The DataMerge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DataMerge''s developer surface includes authentication, pricing, documentation, and 14 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: DataMerge API Rules
  rule_count: 48
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 2
  slug: datamerge-ai-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 31.0
    discoverability: 48.2
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datamerge Ai Authentication
  slug: datamerge-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Datamerge Ai Domain Security
  slug: datamerge-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datamerge-ai
tags:
- Data Enrichment
- B2B
- Contact Data
- Company Data
website: https://datamerge.ai/
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api-dev.openany.si
  baseurl_source: declared
  description: 'OpenAny API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: OpenAny API
  slug: openany-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/openany/rules/openany-rules.yml
  title: ''
  type: Spectral
  url: rules/openany-rules.yml
- group: design
  href: https://artifacts.apis.io/openany/json-ld/openany-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openany-context.jsonld
- group: design
  href: https://artifacts.apis.io/openany/vocabulary/openany-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openany-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/openany/data-model/openany-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openany-data-model.yml
- group: design
  href: https://artifacts.apis.io/openany/conformance/openany-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openany-conformance.yml
- group: agent
  href: https://artifacts.apis.io/openany/llms/openany-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openany-llms.txt
- group: other
  href: https://artifacts.apis.io/openany/hosts/openany-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openany-hosts.yml
- group: other
  href: https://artifacts.apis.io/openany/vendors/openany-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openany-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://openany.si/sign-up?returnTo=%2Fdashboard%3Fpage%3Dapi-keys
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openany.si/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://openany.si/apis/categories/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.openany.si/
- group: auth
  href: https://artifacts.apis.io/openany/security/openany-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openany-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openany.si/
- group: docs
  title: ''
  type: Documentation
  url: https://openany.si/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://openany.si/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openany.si/terms/
coverage:
  checked: '2026-11-02'
  detail: Documentation at https://openany.si/docs/ provides only HTML with no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://openany.si/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: OpenAny is an open marketplace for AI agents operated by Alephant AI LLC in San Francisco. It offers a unified API key and prepaid balance to access a catalog of AI models, data APIs, and portable skills. Users can browse the catalog, read documentation, create an account and API key for free, and pay per use without any subscription. The platform emphasizes one‑key access, usage‑based billing, and integration flexibility for developers building intelligent agents.
image: https://openany.si/og/af63a24c860189fe.png
json_schemas:
- name: PostExecuteRequest
  property_count: 1
  slug: openany-post-execute-request
- name: PostV1ChatCompletionsRequest
  property_count: 3
  slug: openany-post-v1-chat-completions-request
jsonld:
- class_count: 2
  name: Openany Context
  property_count: 4
  slug: openany-context
layout: provider
modified: '2026-11-02'
name: OpenAny
nav: Providers
network: true
overview: 'OpenAny is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Agents, and Models.


  The OpenAny catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenAny''s developer surface includes signup flow, documentation, pricing, and 14 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: OpenAny API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: openany-rules
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 9.5
    discoverability: 58.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Openany Domain Security
  slug: openany-domain-security
  summary_line: TLSv1.3 · HSTS
slug: openany
tags:
- Artificial Intelligence
- Marketplace
- Agents
- Models
website: https://openany.si/
---

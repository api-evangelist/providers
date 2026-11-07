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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API v1 for DealFilter, base URL https://dealfilter.ai/api/v1
  name: DealFilter API
  slug: dealfilter-api
- description: 'omninoo GmbH API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: omninoo GmbH API
  slug: dealfilter-ai-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/dealfilter-ai/rules/dealfilter-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/dealfilter-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/dealfilter-ai/json-ld/dealfilter-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dealfilter-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/dealfilter-ai/vocabulary/dealfilter-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dealfilter-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dealfilter-ai/data-model/dealfilter-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dealfilter-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/dealfilter-ai/conformance/dealfilter-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dealfilter-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dealfilter-ai/llms/dealfilter-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dealfilter-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/dealfilter-ai/well-known/dealfilter-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dealfilter-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/dealfilter-ai/hosts/dealfilter-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealfilter-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/dealfilter-ai/vendors/dealfilter-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealfilter-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://dealfilter.ai/de/signin
- group: docs
  title: ''
  type: Documentation
  url: https://dealfilter.ai/de/docs
- group: company
  title: ''
  type: Blog
  url: https://dealfilter.ai/de/blog
- group: auth
  href: https://artifacts.apis.io/dealfilter-ai/security/dealfilter-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealfilter-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dealfilter.ai/
coverage:
  checked: '2026-11-05'
  detail: Documentation is HTML rendered via JavaScript with no machine‑readable OpenAPI spec discovered despite probing common spec URLs.
  evidence:
  - status: 404
    url: https://dealfilter.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DealFilter analysiert Projektanfragen für IT-Freelancer im DACH-Markt in Sekunden. Bewertet Deals, erkennt kritische Faktoren und bietet 14 Tage kostenlos testen. Das Unternehmen omninoo GmbH bietet eine Plattform zur Bewertung und Filterung von Projektanfragen für IT-Freelancer, unterstützt durch KI-gestützte Analyse und klare Preisgestaltung.
image: https://dealfilter.ai/og-image.png
json_schemas:
- name: GetApiV1ApplicationsResponse
  property_count: 4
  slug: dealfilter-ai-get-api-v1-applications-response
- name: GetApiV1QuotaResponse
  property_count: 4
  slug: dealfilter-ai-get-api-v1-quota-response
- name: PostApiMcpRequest
  property_count: 4
  slug: dealfilter-ai-post-api-mcp-request
- name: PostApiOauthTokenRequest
  property_count: 4
  slug: dealfilter-ai-post-api-oauth-token-request
- name: PostApiOauthTokenResponse
  property_count: 3
  slug: dealfilter-ai-post-api-oauth-token-response
- name: PostApiV1ApplicationsRequest
  property_count: 4
  slug: dealfilter-ai-post-api-v1-applications-request
jsonld:
- class_count: 11
  name: Dealfilter Ai Context
  property_count: 27
  slug: dealfilter-ai-context
layout: provider
modified: '2026-11-05'
name: omninoo GmbH
nav: Providers
network: true
overview: 'omninoo GmbH is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Freelance, IT, Marketplace, and Artificial Intelligence.


  The omninoo GmbH catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  omninoo GmbH''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: omninoo GmbH API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: dealfilter-ai-rules
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dealfilter Ai Domain Security
  slug: dealfilter-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dealfilter-ai
tags:
- Company
- Freelance
- IT
- Marketplace
- Artificial Intelligence
- Germany
website: https://dealfilter.ai/
---

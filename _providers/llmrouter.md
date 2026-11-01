---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: LLMrouter API documentation and quickstart guide
  name: LLMrouter API
  slug: llmrouter-api-2
- baseURL: https://proxy.llmrouter.eu
  baseurl_source: declared
  description: 'LLMrouter.eu API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: LLMrouter.eu API
  slug: llmrouter-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/llmrouter/rules/llmrouter-rules.yml
  title: ''
  type: Spectral
  url: rules/llmrouter-rules.yml
- group: design
  href: https://artifacts.apis.io/llmrouter/json-ld/llmrouter-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/llmrouter-context.jsonld
- group: design
  href: https://artifacts.apis.io/llmrouter/vocabulary/llmrouter-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/llmrouter-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/llmrouter/data-model/llmrouter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/llmrouter-data-model.yml
- group: auth
  href: https://artifacts.apis.io/llmrouter/authentication/llmrouter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/llmrouter-authentication.yml
- group: design
  href: https://artifacts.apis.io/llmrouter/conformance/llmrouter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/llmrouter-conformance.yml
- group: agent
  href: https://artifacts.apis.io/llmrouter/well-known/llmrouter-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/llmrouter-well-known.yml
- group: other
  href: https://artifacts.apis.io/llmrouter/hosts/llmrouter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llmrouter-hosts.yml
- group: other
  href: https://artifacts.apis.io/llmrouter/vendors/llmrouter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/llmrouter-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.llmrouter.eu/en/
- group: auth
  href: https://artifacts.apis.io/llmrouter/security/llmrouter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llmrouter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llmrouter.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.llmrouter.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.llmrouter.eu/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.llmrouter.eu/
- group: company
  title: ''
  type: Blog
  url: https://www.llmrouter.eu/de/news
- group: start
  title: ''
  type: SignUp
  url: https://app.llmrouter.eu/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.llmrouter.eu/de/impressum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/32798619
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://llmrouter.eu/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: LLMrouter.eu provides a secure, EU‑compliant gateway for managing Large Language Models (LLMs). Based in Munich, it offers data‑privacy‑focused SaaS solutions, helping enterprises avoid vendor lock‑in, reduce costs, and ensure compliance with European regulations. The platform emphasizes reliability, cost‑optimization, and integration flexibility, supporting multi‑LLM management with a focus on security certifications such as ISO 9001, ISO 27001, and TISAX.
image: https://llmrouter.eu/site/og-image.png
json_schemas:
- name: GetV1ModelsResponse
  property_count: 2
  slug: llmrouter-get-v1-models-response
- name: PostV1ChatCompletionsRequest
  property_count: 2
  slug: llmrouter-post-v1-chat-completions-request
- name: PostV1ChatCompletionsResponse
  property_count: 2
  slug: llmrouter-post-v1-chat-completions-response
jsonld:
- class_count: 3
  name: Llmrouter Context
  property_count: 4
  slug: llmrouter-context
layout: provider
modified: '2026-10-18'
name: LLMrouter.eu
nav: Providers
network: true
overview: 'LLMrouter.eu is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Software-as-a-Service, Security, and EU.


  The LLMrouter.eu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LLMrouter.eu''s developer surface includes authentication, documentation, API reference, engineering blog, signup flow, and 14 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: LLMrouter.eu API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: llmrouter-rules
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 32.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Llmrouter Authentication
  slug: llmrouter-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Llmrouter Domain Security
  slug: llmrouter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: llmrouter
tags:
- Company
- Artificial Intelligence
- Software-as-a-Service
- Security
- EU
website: https://llmrouter.eu/
---

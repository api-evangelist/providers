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
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Cytado Citation API provides endpoints for citation generation, bibliography creation, verification, and evidence retrieval.
  name: Citation API
  slug: citation-api
- description: 'Cytado API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Cytado API
  slug: cytado-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/cytado-com/rules/cytado-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cytado-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cytado-com/json-ld/cytado-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cytado-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cytado-com/vocabulary/cytado-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cytado-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cytado-com/data-model/cytado-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cytado-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cytado-com/conformance/cytado-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cytado-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cytado-com/well-known/cytado-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cytado-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cytado-com/hosts/cytado-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cytado-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cytado.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://cytado.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cytado.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://cytado.com/login
- group: company
  title: ''
  type: Blog
  url: https://cytado.com/blog
- group: auth
  href: https://artifacts.apis.io/cytado-com/security/cytado-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cytado-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cytado.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://cytado.com/api/mcp
  - status: 200
    url: https://cytado.com/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: Cytado provides a bibliography and citation generator that uses verified academic sources to produce accurate footnotes with real page numbers. It offers integrations for Google Docs, Claude, ChatGPT, and a Chrome extension, plus APIs for citation, bibliography, verification, and evidence retrieval. The service is priced per project with generous fair‑use limits and supports APA, MLA, Chicago, and BibTeX styles.
image: https://cytado.com/og.png
json_schemas:
- name: GetApiExtCorpusResponse
  property_count: 5
  slug: cytado-com-get-api-ext-corpus-response
- name: GetApiExtCorpusStatusResponse
  property_count: 5
  slug: cytado-com-get-api-ext-corpus-status-response
- name: PostApiExtUsageRequest
  property_count: 3
  slug: cytado-com-post-api-ext-usage-request
- name: PostCytadoHookRequest
  property_count: 3
  slug: cytado-com-post-cytado-hook-request
- name: PostFindSourceRequest
  property_count: 5
  slug: cytado-com-post-find-source-request
- name: PostFindSourceResponse
  property_count: 13
  slug: cytado-com-post-find-source-response
jsonld:
- class_count: 10
  name: Cytado Com Context
  property_count: 33
  slug: cytado-com-context
layout: provider
modified: '2026-11-04'
name: Cytado
nav: Providers
network: true
overview: 'Cytado is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Citations, Bibliography, Academic, and Research.


  The Cytado catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cytado''s developer surface includes support, engineering blog, and 12 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: Cytado API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: cytado-com-rules
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 7.1
    discoverability: 48.2
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
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cytado Com Domain Security
  slug: cytado-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cytado-com
tags:
- Citations
- Bibliography
- Academic
- Research
website: https://cytado.com/
---

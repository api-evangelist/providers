---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Read‑only MCP JSON‑RPC server exposing tools for AI regulatory data such as vendor commitments, framework version history, corpus search, partnership patterns and listings.
  name: Anteroom MCP
  slug: anteroom-mcp
- baseURL: https://mcp.anteroom.so
  baseurl_source: declared
  description: 'Anteroom API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Anteroom API
  slug: anteroom-so-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/anteroom-so/rules/anteroom-so-rules.yml
  title: ''
  type: Spectral
  url: rules/anteroom-so-rules.yml
- group: design
  href: https://artifacts.apis.io/anteroom-so/json-ld/anteroom-so-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anteroom-so-context.jsonld
- group: design
  href: https://artifacts.apis.io/anteroom-so/vocabulary/anteroom-so-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anteroom-so-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/anteroom-so/data-model/anteroom-so-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anteroom-so-data-model.yml
- group: design
  href: https://artifacts.apis.io/anteroom-so/conformance/anteroom-so-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anteroom-so-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anteroom-so/llms/anteroom-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anteroom-so-llms.txt
- group: other
  href: https://artifacts.apis.io/anteroom-so/hosts/anteroom-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anteroom-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/anteroom-so/vendors/anteroom-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anteroom-so-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anteroom.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anteroom.so/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://anteroom.so/corpus/changelog
- group: auth
  href: https://artifacts.apis.io/anteroom-so/security/anteroom-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anteroom-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anteroom.so/
- group: docs
  title: ''
  type: Documentation
  url: https://anteroom.so/mcp
- group: operate
  title: ''
  type: Support
  url: https://anteroom.so/about
- group: company
  title: ''
  type: Blog
  url: https://anteroom.so/blog
coverage:
  checked: '2026-11-01'
  detail: Public MCP documentation exists but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec is published.
  evidence:
  - status: 200
    url: https://anteroom.so/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Anteroom is a structured legal‑review tool that helps organizations assess AI launch compliance. It provides curated, up‑to‑date regulatory insights across jurisdictions, offering a searchable corpus of statutes, guidance, and case law. Users can input launch details to receive a tailored analysis of applicable regulations, obligations, and risk mitigations, supporting responsible AI deployment.
image: https://anteroom.so/opengraph-image
json_schemas:
- name: PostMcpRequest
  property_count: 3
  slug: anteroom-so-post-mcp-request
jsonld:
- class_count: 1
  name: Anteroom So Context
  property_count: 3
  slug: anteroom-so-context
layout: provider
modified: '2026-11-01'
name: Anteroom
nav: Providers
network: true
overview: 'Anteroom is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Legal Tech, Compliance, Regulations, and Startups.


  The Anteroom catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Anteroom''s developer surface includes changelog, documentation, support, engineering blog, and 12 more developer resources.'
plans:
- name: Anteroom So Plans Pricing
  plan_count: 0
  slug: anteroom-so-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Anteroom So Rate Limits
  slug: anteroom-so-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Anteroom API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: anteroom-so-rules
scopes:
- name: Anteroom So Scopes
  scope_count: 0
  slug: anteroom-so-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 8.3
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 25.0
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anteroom So Authentication
  slug: anteroom-so-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anteroom So Domain Security
  slug: anteroom-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anteroom-so
tags:
- Artificial Intelligence
- Legal Tech
- Compliance
- Regulations
- Startups
website: https://anteroom.so/
---

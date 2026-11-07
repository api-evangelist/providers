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
- description: Developer portal for Amber Memory MCP service providing API documentation and reference.
  name: Amber Memory API
  slug: amber-memory-api
- baseURL: https://ambermem.com
  baseurl_source: declared
  description: 'Amber API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Amber API
  slug: ambermem-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/ambermem-com/rules/ambermem-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ambermem-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ambermem-com/json-ld/ambermem-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ambermem-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ambermem-com/vocabulary/ambermem-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ambermem-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ambermem-com/data-model/ambermem-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ambermem-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/ambermem-com/conformance/ambermem-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ambermem-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ambermem-com/llms/ambermem-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ambermem-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ambermem-com/well-known/ambermem-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ambermem-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ambermem-com/hosts/ambermem-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ambermem-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ambermem-com/vendors/ambermem-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ambermem-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ambermem.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ambermem.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://dev.ambermem.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ambermem
- group: auth
  href: https://artifacts.apis.io/ambermem-com/security/ambermem-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ambermem-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ambermem.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://ambermem.com/mcp
  - status: 401
    url: https://api.ambermem.com/mcp
  - status: 401
    url: https://dev.ambermem.com/mcp
  - status: 200
    url: https://ambermem.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Amber provides a subscription Model Context Protocol (MCP) service that securely stores a person’s long‑term memories, moments, decisions and lessons. Users get an isolated, permanent, portable database that can be accessed by any MCP‑compatible AI, ensuring continuity across conversations and platforms. The service offers OAuth 2.1 authentication via PayPal and a free 90‑day trial before a $2.99 /month plan.
json_schemas:
- name: GetBackupTaskidResponse
  property_count: 1
  slug: ambermem-com-get-backup-taskid-response
- name: PostBackupResponse
  property_count: 2
  slug: ambermem-com-post-backup-response
- name: PostFeedbackRequest
  property_count: 2
  slug: ambermem-com-post-feedback-request
- name: PostImportFromUrlRequest
  property_count: 1
  slug: ambermem-com-post-import-from-url-request
- name: PostImportPresignResponse
  property_count: 2
  slug: ambermem-com-post-import-presign-response
- name: PostImportResponse
  property_count: 2
  slug: ambermem-com-post-import-response
jsonld:
- class_count: 6
  name: Ambermem Com Context
  property_count: 8
  slug: ambermem-com-context
layout: provider
modified: '2026-11-01'
name: Amber
nav: Providers
network: true
overview: 'Amber is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Subscription, MCP, and Personal Data.


  The Amber catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amber''s developer surface includes documentation and 14 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Amber API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: ambermem-com-rules
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 22.8
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 2.6
  previous_composite: 21.6
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ambermem Com Domain Security
  slug: ambermem-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ambermem-com
tags:
- Artificial Intelligence
- Memory
- Subscription
- MCP
- Personal Data
website: https://ambermem.com/
---

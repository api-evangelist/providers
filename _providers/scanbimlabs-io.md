---
agent_readiness:
  band: human-only
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
artifact_total: 11
common:
- group: other
  href: https://artifacts.apis.io/scanbimlabs-io/hosts/scanbimlabs-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scanbimlabs-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/scanbimlabs-io/vendors/scanbimlabs-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scanbimlabs-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/scanbimlabs-io/security/scanbimlabs-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scanbimlabs-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scanbimlabs.io/
created: '2026-10-29'
description: 'scanbimlabs-io is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: GetApiMorpheonPersonasResponse
  property_count: 1
  slug: scanbimlabs-io-get-api-morpheon-personas-response
- name: GetApiZapierTriggersUploadsResponse
  property_count: 8
  slug: scanbimlabs-io-get-api-zapier-triggers-uploads-response
- name: PostApiAuthLoginRequest
  property_count: 2
  slug: scanbimlabs-io-post-api-auth-login-request
- name: PostApiMorpheonChatRequest
  property_count: 2
  slug: scanbimlabs-io-post-api-morpheon-chat-request
- name: PostApiMorpheonChatResponse
  property_count: 3
  slug: scanbimlabs-io-post-api-morpheon-chat-response
- name: PostApiMorpheonMemoryRememberRequest
  property_count: 2
  slug: scanbimlabs-io-post-api-morpheon-memory-remember-request
jsonld:
- class_count: 11
  name: Scanbimlabs Io Context
  property_count: 20
  slug: scanbimlabs-io-context
layout: provider
modified: '2026-10-29'
name: scanbimlabs-io
nav: Providers
network: true
overview: 'scanbimlabs-io publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The scanbimlabs-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Scanbimlabs Io Plans Pricing
  plan_count: 3
  slug: scanbimlabs-io-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: scanbimlabs-io API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: scanbimlabs-io-rules
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.5
    catalog_earned_first_party: 12.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 14.9
    developer_ergonomics: 0.0
    discoverability: 26.8
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 6
      marker_coverage: 85.7
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Scanbimlabs Io Authentication
  slug: scanbimlabs-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Scanbimlabs Io Domain Security
  slug: scanbimlabs-io-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: scanbimlabs-io
tags:
- Company
website: https://scanbimlabs.io/
---

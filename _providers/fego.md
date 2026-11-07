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
  band: human-only
  dimensions:
    agent_card: conformant
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 9
common:
- group: auth
  href: https://artifacts.apis.io/fego/security/fego-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fego-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fego.ai/
created: '2026-10-20'
description: 'Fego.ai is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: GetDomainsResponse
  property_count: 10
  slug: fego-get-domains-response
- name: GetRegistrarV1ContactsHandleResponse
  property_count: 7
  slug: fego-get-registrar-v1-contacts-handle-response
- name: GetRegistrarV1DomainsCheckDomainnameResponse
  property_count: 7
  slug: fego-get-registrar-v1-domains-check-domainname-response
- name: GetRegistrarV1DomainsDomainnameDnssecResponse
  property_count: 7
  slug: fego-get-registrar-v1-domains-domainname-dnssec-response
- name: GetRegistrarV1DomainsDomainnameLockResponse
  property_count: 7
  slug: fego-get-registrar-v1-domains-domainname-lock-response
- name: PutRegistrarV1DomainsDomainnameLockResponse
  property_count: 7
  slug: fego-put-registrar-v1-domains-domainname-lock-response
jsonld:
- class_count: 19
  name: Fego Context
  property_count: 32
  slug: fego-context
layout: provider
modified: '2026-10-20'
name: Fego.ai
nav: Providers
network: true
overview: 'Fego.ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Fego.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Fego.ai API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: fego-rules
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 30.5
    catalog_earned_first_party: 0.0
    catalog_gap: 84.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 14.7
    developer_ergonomics: 0.0
    discoverability: 33.9
    operational_transparency: 0.0
  previous_composite: 7.9
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
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Fego Domain Security
  slug: fego-domain-security
  summary_line: TLSv1.3
slug: fego
tags:
- Company
website: https://fego.ai/
---

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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/shonanfarm-com/llms/shonanfarm-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shonanfarm-com-llms.txt
- group: other
  href: https://artifacts.apis.io/shonanfarm-com/hosts/shonanfarm-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shonanfarm-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shonanfarm.com/home/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://shonanfarm.com/
- group: auth
  href: https://artifacts.apis.io/shonanfarm-com/security/shonanfarm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shonanfarm-com-domain-security.yml
coverage:
  checked: '2026-10-30'
  detail: The website https://shonanfarm.com/ is a bike shop with no API documentation or contracts.
  evidence:
  - status: 404
    url: https://shonanfarm.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-10-30'
description: 'shonanfarm-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-30'
name: shonanfarm-com
nav: Providers
network: true
overview: shonanfarm-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Stub, Unknown, API, and Placeholder.
plans:
- name: Shonanfarm Com Plans Pricing
  plan_count: 0
  slug: shonanfarm-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Shonanfarm Com Rate Limits
  slug: shonanfarm-com-rate-limits
scopes:
- name: Shonanfarm Com Scopes
  scope_count: 0
  slug: shonanfarm-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Shonanfarm Com Authentication
  slug: shonanfarm-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Shonanfarm Com Domain Security
  slug: shonanfarm-com-domain-security
  summary_line: TLSv1.3
slug: shonanfarm-com
tags:
- Company
- Stub
- Unknown
- API
- Placeholder
website: https://shonanfarm.com/
---

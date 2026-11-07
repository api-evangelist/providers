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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Zhihuo Net Agentic Access
  operation_count: 4
  slug: zhihuo-net-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- description: Public JSON API for single-carton container loading (Brimload T1).
  name: Brimload T1 WebAPI
  slug: brimload-t1-webapi
artifact_total: 8
common:
- group: other
  href: https://artifacts.apis.io/zhihuo-net/vendors/zhihuo-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zhihuo-net-vendors.yml
- group: agent
  href: https://artifacts.apis.io/zhihuo-net/agentic-access/zhihuo-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zhihuo-net-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/zhihuo-net/rules/zhihuo-net-rules.yml
  title: ''
  type: Spectral
  url: rules/zhihuo-net-rules.yml
- group: agent
  href: https://artifacts.apis.io/zhihuo-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/zhihuo-net/errors/zhihuo-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zhihuo-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/zhihuo-net/conformance/zhihuo-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zhihuo-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zhihuo-net/llms/zhihuo-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zhihuo-net-llms.txt
- group: other
  href: https://artifacts.apis.io/zhihuo-net/hosts/zhihuo-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zhihuo-net-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brimload.com/privacy.html
- group: docs
  title: ''
  type: Documentation
  url: https://brimload.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://brimload.com/t1/developers/
- group: company
  title: ''
  type: Website
  url: https://zhihuo.net/
- group: auth
  href: https://artifacts.apis.io/zhihuo-net/security/zhihuo-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zhihuo-net-domain-security.yml
created: '2026-10-30'
description: zhihuo-net is currently a placeholder entry in the API Evangelist network. The company was identified from the MCP registry harvest but no public website, documentation, or API endpoints could be verified. Attempts to resolve https://zhihuo.net/ redirected to an unrelated site, and no alternative domain or developer portal was found. Consequently, the profile contains minimal information and serves as a stub for future enrichment when authoritative sources become available.
image: https://brimload.com/logo.png
layout: provider
modified: '2026-10-30'
name: zhihuo-net
nav: Providers
network: true
overview: 'zhihuo-net is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company and Harvest.


  The zhihuo-net catalog on APIs.io includes 1 Spectral governance ruleset.


  zhihuo-net''s developer surface includes documentation, API reference, and 11 more developer resources.'
plans:
- name: Zhihuo Net Plans Pricing
  plan_count: 0
  slug: zhihuo-net-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Zhihuo Net Rate Limits
  slug: zhihuo-net-rate-limits
rules:
- authorship: generated
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: zhihuo-net API Rules
  rule_count: 6
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 0
  slug: zhihuo-net-rules
scopes:
- name: Zhihuo Net Scopes
  scope_count: 0
  slug: zhihuo-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 5.3
    contract_governance: 15.9
    contract_quality: 0.0
    developer_ergonomics: 14.8
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 17.4
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zhihuo-net/zhihuo-net-2026-11-03T150522.png
security:
- kind: authentication
  name: Zhihuo Net Authentication
  slug: zhihuo-net-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Zhihuo Net Domain Security
  slug: zhihuo-net-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zhihuo-net
tags:
- Company
- Harvest
website: https://zhihuo.net/
---

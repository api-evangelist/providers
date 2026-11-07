---
access_model:
  confidence: low
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
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/scotty-labs/llms/scotty-labs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scotty-labs-llms.txt
- group: other
  href: https://artifacts.apis.io/scotty-labs/hosts/scotty-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scotty-labs-hosts.yml
- group: auth
  href: https://artifacts.apis.io/scotty-labs/security/scotty-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scotty-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scotty.ai/
coverage:
  checked: '2026-10-29'
  detail: Landing page https://www.scotty.ai/lander returned 403 and no machine-readable docs were found.
  evidence:
  - status: 403
    url: https://www.scotty.ai/lander
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: 'Scotty Labs is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by gradient-ventures) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-10-29'
name: Scotty Labs
nav: Providers
network: true
overview: Scotty Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
plans:
- name: Scotty Labs Plans Pricing
  plan_count: 0
  slug: scotty-labs-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Scotty Labs Rate Limits
  slug: scotty-labs-rate-limits
scopes:
- name: Scotty Labs Scopes
  scope_count: 0
  slug: scotty-labs-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 33.9
    operational_transparency: 0.0
  previous_composite: 3.5
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/scotty-labs/scotty-labs-2026-11-03T142822.png
security:
- kind: authentication
  name: Scotty Labs Authentication
  slug: scotty-labs-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Scotty Labs Domain Security
  slug: scotty-labs-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: scotty-labs
tags:
- Company
website: https://www.scotty.ai/
---

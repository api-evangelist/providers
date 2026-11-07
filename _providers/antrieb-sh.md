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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP endpoint providing tool access for Antrieb testbeds.
  name: Antrieb MCP
  slug: antrieb-mcp
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/antrieb-sh/well-known/antrieb-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/antrieb-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/antrieb-sh/hosts/antrieb-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/antrieb-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/antrieb-sh/vendors/antrieb-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/antrieb-sh-vendors.yml
- group: auth
  href: https://artifacts.apis.io/antrieb-sh/security/antrieb-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antrieb-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://antrieb.sh/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jade-pico
coverage:
  checked: '2026-11-01'
  detail: The MCP endpoint at https://antrieb.sh/mcp returns HTTP 401 Unauthorized, requiring an API key.
  evidence:
  - status: 401
    url: https://antrieb.sh/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Antrieb provides AI‑driven disposable testbeds that let developers verify infrastructure changes in realistic environments. It offers tools to provision clusters, execute commands, inspect results, save artifacts, and clean up resources, supporting operating systems, routers, firewalls, private networks, and Kubernetes workloads.
layout: provider
modified: '2026-11-01'
name: Antrieb
nav: Providers
network: true
overview: Antrieb is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Testbeds, Infrastructure, Verification, and Cloud.
plans:
- name: Antrieb Sh Plans Pricing
  plan_count: 0
  slug: antrieb-sh-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Antrieb Sh Rate Limits
  slug: antrieb-sh-rate-limits
scopes:
- name: Antrieb Sh Scopes
  scope_count: 0
  slug: antrieb-sh-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 2.6
  previous_composite: 7.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Antrieb Sh Authentication
  slug: antrieb-sh-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Antrieb Sh Domain Security
  slug: antrieb-sh-domain-security
  summary_line: TLSv1.3
slug: antrieb-sh
tags:
- Artificial Intelligence
- Testbeds
- Infrastructure
- Verification
- Cloud
website: https://antrieb.sh/
---

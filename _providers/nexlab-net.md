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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Model Context Protocol (MCP) servers for autonomous agents, providing data with source attribution.
  name: Nexlab MCP
  slug: nexlab-mcp
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/nexlab-net/llms/nexlab-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nexlab-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/nexlab-net/well-known/nexlab-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nexlab-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/nexlab-net/hosts/nexlab-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nexlab-net-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nextime
- group: company
  title: ''
  type: Website
  url: https://nexlab.net/
- group: auth
  href: https://artifacts.apis.io/nexlab-net/security/nexlab-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nexlab-net-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: Documentation UI is public but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec was found.
  evidence:
  - status: 200
    url: https://mcp.nexlab.net/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: nexlab-net appears in the API Evangelist harvest as a stub entry with no verifiable corporate website or public documentation. The domain https://nexlab.net resolves to a personal portfolio site unrelated to a distinct company, and no official API documentation, developer portal, or organizational information could be located. Consequently, the provider's identity remains unconfirmed beyond the placeholder record.
layout: provider
modified: '2026-10-29'
name: nexlab-net
nav: Providers
network: true
overview: nexlab-net is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, and Placeholder.
plans:
- name: Nexlab Net Plans Pricing
  plan_count: 0
  slug: nexlab-net-plans-pricing
random_paper: 22
scopes:
- name: Nexlab Net Scopes
  scope_count: 0
  slug: nexlab-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nexlab-net/nexlab-net-2026-11-03T140156.png
security:
- kind: authentication
  name: Nexlab Net Authentication
  slug: nexlab-net-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nexlab Net Domain Security
  slug: nexlab-net-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nexlab-net
tags:
- Company
- Technology
- Placeholder
website: https://nexlab.net/
---

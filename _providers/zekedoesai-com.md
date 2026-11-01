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
  href: https://artifacts.apis.io/zekedoesai-com/llms/zekedoesai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zekedoesai-com-llms.txt
- group: other
  href: https://artifacts.apis.io/zekedoesai-com/hosts/zekedoesai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zekedoesai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/zekedoesai-com/vendors/zekedoesai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zekedoesai-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/zekedoesai-com/security/zekedoesai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zekedoesai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zekedoesai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://zekedoesai.com/architecture/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zekerutledge
coverage:
  checked: '2026-10-30'
  detail: The provider's site and documentation contain no public API specifications or endpoints.
  evidence:
  - status: 200
    url: https://zekedoesai.com/
  reason: not-a-software-company
  state: none
created: '2026-10-30'
description: Zeke Does AI is a personal homelab project that showcases practical AI tools, networking, automation, and MCP server integrations. The site documents the journey of combining AI, networking, and homelab infrastructure, offering open‑source examples, small‑scale hardware setups, and curiosity‑driven experiments that make modern technology approachable for enthusiasts.
image: https://avatars.githubusercontent.com/u/258098646?v=4
layout: provider
modified: '2026-10-30'
name: zekedoesai-com
nav: Providers
network: true
overview: 'zekedoesai-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Homelab, MCP, Networking, and Open-source.


  zekedoesai-com''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Zekedoesai Com Plans Pricing
  plan_count: 0
  slug: zekedoesai-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Zekedoesai Com Rate Limits
  slug: zekedoesai-com-rate-limits
scopes:
- name: Zekedoesai Com Scopes
  scope_count: 0
  slug: zekedoesai-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Zekedoesai Com Authentication
  slug: zekedoesai-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Zekedoesai Com Domain Security
  slug: zekedoesai-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: zekedoesai-com
tags:
- AI
- Homelab
- MCP
- Networking
- Open-source
website: https://zekedoesai.com/
---

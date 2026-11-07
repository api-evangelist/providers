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
    mcp_server: documented
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
  score: 24.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'How to connect Pieter‑Jan Scheir’s MCP server to Claude, ChatGPT, Cursor, VS Code and other AI assistants: the server URL, the steps per app and what it can answer.'
  name: MCP
  slug: mcp
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/scheir-eu/well-known/scheir-eu-vercel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scheir-eu-vercel-security.txt
- group: agent
  href: https://artifacts.apis.io/scheir-eu/llms/scheir-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scheir-eu-llms.txt
- group: agent
  href: https://artifacts.apis.io/scheir-eu/mcp/scheir-eu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scheir-eu-mcp.yml
- group: agent
  href: https://artifacts.apis.io/scheir-eu/well-known/scheir-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scheir-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/scheir-eu/hosts/scheir-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scheir-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/scheir-eu/vendors/scheir-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scheir-eu-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pieterjanscheir
- group: docs
  title: ''
  type: Documentation
  url: https://dev.scheir.eu/
- group: auth
  href: https://artifacts.apis.io/scheir-eu/security/scheir-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scheir-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scheir.eu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scheir.eu/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://scheir.eu/en/contact
created: '2026-10-31'
description: Scheir is the personal brand of Pieter‑Jan Scheir, an AI‑first full‑stack developer based in Belgium. He builds web applications, AI‑driven tools, and MCP servers using TypeScript, React, and Next.js, leveraging Claude Code, Cursor, and Codex. His work blends legal‑tech expertise with modern AI development practices, offering innovative solutions across multiple languages and platforms.
image: https://scheir.eu/en/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at scheir.eu.
  name: scheir-eu MCP Server
  slug: scheir-eu-mcp-yml
modified: '2026-10-31'
name: scheir-eu
nav: Providers
network: true
overview: 'scheir-eu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Full-Stack, Developers, Belgium, and Legal Tech.


  scheir-eu''s developer surface includes documentation, support, and 10 more developer resources.'
plans:
- name: Scheir Eu Plans Pricing
  plan_count: 0
  slug: scheir-eu-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Scheir Eu Rate Limits
  slug: scheir-eu-rate-limits
scopes:
- name: Scheir Eu Scopes
  scope_count: 0
  slug: scheir-eu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 65.0
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - belgium
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 14.8
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/scheir-eu/scheir-eu-2026-11-03T142810.png
security:
- kind: authentication
  name: Scheir Eu Authentication
  slug: scheir-eu-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Scheir Eu Domain Security
  slug: scheir-eu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scheir-eu
tags:
- Artificial Intelligence
- Full-Stack
- Developers
- Belgium
- Legal Tech
- Company
website: https://scheir.eu/
---

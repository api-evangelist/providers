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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agent Plugin API for DecRec, connecting AI tools via MCP.
  name: DecRec API
  slug: decrec-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/decrec-io/well-known/decrec-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/decrec-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/decrec-io/hosts/decrec-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/decrec-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/decrec-io/vendors/decrec-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/decrec-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://decrec.io/login
- group: auth
  href: https://artifacts.apis.io/decrec-io/security/decrec-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/decrec-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://decrec.io/
- group: docs
  title: ''
  type: Documentation
  url: https://decrec.io/docs
- group: company
  title: ''
  type: Blog
  url: https://decrec.io/blog
- group: operate
  title: ''
  type: Support
  url: https://decrec.io/legal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/decrec-io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://decrec.io/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://decrec.io/legal
coverage:
  checked: '2026-11-05'
  detail: Documentation pages load via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://decrec.io/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DecRec provides a decision‑recording platform that captures, preserves, and surfaces the reasoning behind choices made in AI‑assisted workflows. Users can commit decisions, recall prior reasoning, and share context across tools like Claude, ChatGPT, Cursor, Codex, and VS Code. The service aims to prevent reopening settled decisions, improve institutional memory, and streamline collaborative AI interactions.
image: https://decrec.io/demo-poster.jpg
layout: provider
modified: '2026-11-05'
name: DecRec
nav: Providers
network: true
overview: 'DecRec is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  DecRec''s developer surface includes documentation, engineering blog, support, and 9 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Decrec Io Domain Security
  slug: decrec-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: decrec-io
tags:
- Company
website: https://decrec.io/
---

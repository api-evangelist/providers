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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Rubiic provides an AI‑powered creative platform with an API accessible via its MCP; documentation is gated behind login.
  name: Rubiic API
  slug: rubiic-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/rubiic-com/well-known/rubiic-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rubiic-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/rubiic-com/hosts/rubiic-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rubiic-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/rubiic-com/vendors/rubiic-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rubiic-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://rubiic.com/login
- group: auth
  href: https://artifacts.apis.io/rubiic-com/security/rubiic-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rubiic-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rubiic.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://rubiic.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rubiic.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rubiic.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://rubiic.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rubiic
coverage:
  checked: '2026-10-30'
  detail: API specification URLs redirect to a login page, requiring authentication.
  evidence:
  - status: 200
    url: https://rubiic.com/openapi.json
  reason: auth-required
  state: gated
created: '2026-10-30'
description: Rubiic is an AI‑powered creative platform that enables users to generate videos, graphics, GIFs, and animations through conversational prompts. Users can think out loud, try a direction, and change their mind, with free signup credits and paid credit packs or a subscription plan. Rubiic integrates with coding agents via its MCP, supporting Cursor, Claude Code, Codex, and VS Code, offering step‑by‑step setup and copyable configurations. It positions itself as a creative partner from idea to finished media.
image: https://rubiic.com/rubiic-flat-mark-og.png
layout: provider
modified: '2026-10-30'
name: rubiic-com
nav: Providers
network: true
overview: 'rubiic-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Creative, Video Generation, Graphics, and Automation.


  rubiic-com''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Rubiic Com Plans Pricing
  plan_count: 4
  slug: rubiic-com-plans-pricing
- name: Rubiic Com Plans
  plan_count: 0
  slug: rubiic-com-plans
random_paper: 18
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Rubiic Com Domain Security
  slug: rubiic-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: rubiic-com
tags:
- AI
- Creative
- Video Generation
- Graphics
- Automation
- MCP
website: https://rubiic.com/
---

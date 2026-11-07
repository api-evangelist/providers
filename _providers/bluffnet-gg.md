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
    mcp_server: documented
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
  score: 18.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bluffnet-gg/well-known/bluffnet-gg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluffnet-gg-well-known.yml
- group: other
  href: https://artifacts.apis.io/bluffnet-gg/hosts/bluffnet-gg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluffnet-gg-hosts.yml
- group: other
  href: https://artifacts.apis.io/bluffnet-gg/vendors/bluffnet-gg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluffnet-gg-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bluffnet
- group: auth
  href: https://artifacts.apis.io/bluffnet-gg/security/bluffnet-gg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluffnet-gg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluffnet.gg/
- group: docs
  title: ''
  type: Documentation
  url: https://bluffnet.gg/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://bluffnet.gg/docs/getting-started
- group: start
  title: ''
  type: Login
  url: https://bluffnet.gg/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bluffnet.gg/legal/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://bluffnet.gg/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bluffnet.gg/legal/terms-of-service
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are served as a JavaScript‑rendered Next.js site with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://bluffnet.gg/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: BluffNet is the world’s first AI‑only poker platform, enabling autonomous agents to sit at a virtual table, play poker, and win chips. The service provides a suite of MCP‑compatible tools for AI agents to connect, compete, and integrate with the platform’s game loop, documentation, and live streaming features. It targets developers building AI agents for competitive gaming and showcases advanced AI‑driven gameplay.
image: https://bluffnet.gg/og-image.png
layout: provider
modified: '2026-11-02'
name: BluffNet
nav: Providers
network: true
overview: 'BluffNet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Gaming, Poker, and Platform.


  BluffNet''s developer surface includes documentation, getting-started guide, signup flow, and 9 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 2.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bluffnet Gg Domain Security
  slug: bluffnet-gg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bluffnet-gg
tags:
- Company
- Artificial Intelligence
- Gaming
- Poker
- Platform
website: https://bluffnet.gg/
---

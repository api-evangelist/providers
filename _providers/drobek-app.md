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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Drobek platform, documented at the developer docs.
  name: Drobek API
  slug: drobek-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/drobek-app/llms/drobek-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drobek-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/drobek-app/well-known/drobek-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drobek-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/drobek-app/hosts/drobek-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drobek-app-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drobek.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.drobek.app/privacy
- group: start
  title: ''
  type: Login
  url: https://drobek.app/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/caddy-dns
- group: docs
  title: ''
  type: Documentation
  url: https://www.drobek.app/docs
- group: auth
  href: https://artifacts.apis.io/drobek-app/security/drobek-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drobek-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drobek.app/
coverage:
  checked: '2026-11-06'
  detail: Documentation pages are served as JavaScript-rendered single-page apps, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://www.drobek.app/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: drobek is an open-source, self‑hosted vibe‑coding hosting platform that lets AI agents build small web apps directly via its MCP. Users can connect Claude Code, Cursor, or Codex, write files, preview builds, and publish apps. The service offers a hosted instance at drobek.app and a fully open‑source core under AGPL‑3.0 for self‑hosting, with documentation, API keys, and integration guides for agents.
image: https://www.drobek.app/drobek-og.png
layout: provider
modified: '2026-11-05'
name: drobek
nav: Providers
network: true
overview: 'drobek is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Source, Vibe Coding, Hosting, AI Integration, and Self-Hosted.


  drobek''s developer surface includes documentation and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
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
  name: Drobek App Domain Security
  slug: drobek-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: drobek-app
tags:
- Open Source
- Vibe Coding
- Hosting
- AI Integration
- Self-Hosted
website: https://drobek.app/
---

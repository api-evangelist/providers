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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/aginx-net/hosts/aginx-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aginx-net-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aginx-net/security/aginx-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aginx-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aginx.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://browser.aginx.net/
- group: docs
  title: ''
  type: Documentation
  url: https://brain.aginx.net/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yinnho
- group: company
  title: ''
  type: Blog
  url: https://duphub.com
coverage:
  checked: '2026-11-01'
  detail: Documentation pages on brain.aginx.net render a JavaScript SPA, preventing machine‑readable extraction of API contracts.
  evidence:
  - status: 200
    url: https://brain.aginx.net/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Aginx provides an open-source protocol stack enabling every Agent to have a unique address, offering routing, runtime, browser, model and device capabilities. It delivers a binary‑only gateway, zero‑dependency deployment, and tools like AginxBrowser and AginxBrain for AI model routing, all under the Apache‑2.0 license.
image: https://aginx.net/og-card.png
layout: provider
modified: '2026-11-01'
name: Aginx
nav: Providers
network: true
overview: 'Aginx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Source, Infrastructure, Agent Network, and API Platform.


  Aginx''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 8.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aginx Net Domain Security
  slug: aginx-net-domain-security
  summary_line: TLSv1.3
slug: aginx-net
tags:
- Company
- Open Source
- Infrastructure
- Agent Network
- API Platform
website: https://aginx.net/
---

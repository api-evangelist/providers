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
api_count: 1
apis:
- description: Amendor provides a change‑request widget that lets users submit feedback directly on a live website, which is turned into pull requests.
  name: Amendor API
  slug: amendor-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/amendor-site/llms/amendor-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amendor-site-llms.txt
- group: other
  href: https://artifacts.apis.io/amendor-site/hosts/amendor-site-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amendor-site-hosts.yml
- group: build
  href: https://artifacts.apis.io/amendor-site/packages/amendor-site-packages.yml
  title: ''
  type: SDKs
  url: packages/amendor-site-packages.yml
- group: build
  href: https://artifacts.apis.io/amendor-site/packages/amendor-site-packages.yml
  title: ''
  type: Packages
  url: packages/amendor-site-packages.yml
- group: company
  title: ''
  type: Blog
  url: https://amendor.site/blog/collect-change-requests
- group: auth
  href: https://artifacts.apis.io/amendor-site/security/amendor-site-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amendor-site-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amendor.site/
- group: docs
  title: ''
  type: Documentation
  url: https://amendor.site/about
- group: start
  title: ''
  type: GettingStarted
  url: https://amendor.site/demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amendor.site/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amendor.site/terms
created: '2026-11-01'
description: Amendor provides a change‑request widget that lets users submit feedback directly on a live website, which is then turned into a pull request by a coding agent. This enables seamless UI updates without email or screenshots, supporting any hosting platform and integrating with popular MCP coding agents like Claude Code, Cursor, and Replit. Amendor is operated by Datary AB in Stockholm, Sweden.
image: https://amendor.site/og.png
layout: provider
modified: '2026-11-01'
name: Amendor
nav: Providers
network: true
overview: 'Amendor is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Feedback, UI, Pull Request, Coding Agents, and Software-as-a-Service.


  Amendor''s developer surface includes engineering blog, documentation, getting-started guide, and 8 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 15.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amendor Site Domain Security
  slug: amendor-site-domain-security
  summary_line: TLSv1.3 · DMARC
slug: amendor-site
tags:
- Feedback
- UI
- Pull Request
- Coding Agents
- Software-as-a-Service
website: https://amendor.site/
---

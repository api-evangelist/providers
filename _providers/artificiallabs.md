---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Artificial Labs provides an AI coding platform with autonomous agents.
  name: Artificial Labs API
  slug: artificial-labs-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/artificiallabs/refs/heads/main/well-known/artificiallabs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/artificiallabs-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artificiallabs/refs/heads/main/hosts/artificiallabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artificiallabs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artificiallabs/refs/heads/main/vendors/artificiallabs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artificiallabs-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artificiallabs/refs/heads/main/security/artificiallabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artificiallabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.artificiallabs.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.artificiallabs.ai/help
- group: start
  title: ''
  type: GettingStarted
  url: https://www.artificiallabs.ai/help
- group: commercial
  title: ''
  type: Pricing
  url: https://www.artificiallabs.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.artificiallabs.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.artificiallabs.ai/privacy
coverage:
  checked: 2026-09-26
  detail: OpenAPI endpoint returns HTML marketing page instead of a machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.artificiallabs.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Artificiallabs is an AI‑powered coding platform that automates software development. It provides an autonomous AI engineer named Lloyd that writes, runs, tests, and validates code in real cloud VMs, delivering live proof of functionality. Users interact via a chat‑like interface to describe features, bugs, or refactors, and watch the AI build and verify the solution, with support for web‑based IDE, LLM Lab, and integration tools.
layout: provider
modified: '2026-09-26'
name: Artificiallabs
nav: Providers
network: true
overview: 'Artificiallabs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Coding Platform, Automation, Developer Tools, and Software-as-a-Service.


  Artificiallabs'' developer surface includes documentation, getting-started guide, pricing, and 7 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Artificiallabs Domain Security
  slug: artificiallabs-domain-security
  summary_line: TLSv1.3 · DMARC
slug: artificiallabs
tags:
- Artificial Intelligence
- Coding Platform
- Automation
- Developer Tools
- Software-as-a-Service
website: https://www.artificiallabs.ai
---

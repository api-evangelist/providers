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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Window.ai browser extension to configure and use AI models on web pages.
  name: Window AI API
  slug: window-ai-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/windowai/hosts/windowai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/windowai-hosts.yml
- group: other
  href: https://artifacts.apis.io/windowai/vendors/windowai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/windowai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/windowai/security/windowai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/windowai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://windowai.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alexanderatallah/window.ai
coverage:
  checked: '2026-10-19'
  detail: The provider's documentation is only a GitHub README and a plain website without machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://windowai.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: Window.ai provides a browser extension that lets users run their own AI models directly on the web without needing API keys or a backend. The platform supports models from OpenAI, Google, Anthropic, Together, Cohere, and even self‑hosted models for privacy. Users can configure which model to use per site, keep conversation histories, and share extensions. The service emphasizes user control, privacy, and ease of integration, targeting both casual users and developers looking to embed AI into web experiences.
layout: provider
modified: '2026-10-19'
name: Window.ai
nav: Providers
network: true
overview: Window.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Browser Extension, Privacy, and UserControl.
random_paper: 2
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 2.6
  previous_composite: 4.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Windowai Domain Security
  slug: windowai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: windowai
tags:
- Company
- Artificial Intelligence
- Browser Extension
- Privacy
- UserControl
website: https://windowai.io/
---

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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides labor management, field measurement, compliance, and forecasting capabilities for agricultural producers.
  name: FruitScout API
  slug: fruitscout-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/fruitscout/llms/fruitscout-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fruitscout-llms.txt
- group: other
  href: https://artifacts.apis.io/fruitscout/hosts/fruitscout-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fruitscout-hosts.yml
- group: auth
  href: https://artifacts.apis.io/fruitscout/security/fruitscout-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fruitscout-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fruitscout.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fruitscout.ai/platform/
- group: docs
  title: ''
  type: Documentation
  url: https://fruitscout.ai/platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://fruitscout.ai/get-started/
- group: operate
  title: ''
  type: Support
  url: https://fruitscout.ai/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fruitscout.ai/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fruitscout
coverage:
  checked: '2026-10-29'
  detail: API endpoints require authentication (GraphQL and MCP return 401), preventing access to machine-readable contracts.
  evidence:
  - status: 401
    url: https://farmagent.fruitscout.ai/api/graphql
  - status: 401
    url: https://farmagent.fruitscout.ai/api/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: FruitScout provides plant-level crop measurement, AI-driven harvest planning, crew management, and audit‑ready compliance solutions. Their platform, proven at industrial scale in agave, offers advanced inventory, field measurement, forecasting, and regulatory audit tools, helping producers optimize timing, quality, efficiency, and yield across high‑value crops. The system integrates computer‑vision and data analytics to deliver real‑time insights, supporting both enterprise producers and field crews with mobile apps and compliance modules.
image: https://fruitscout.ai/fruitscout-mark.svg
layout: provider
modified: '2026-10-29'
name: FruitScout
nav: Providers
network: true
overview: 'FruitScout is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, Artificial Intelligence, Crop-Management, Compliance, and Field Operations.


  FruitScout''s developer surface includes documentation, getting-started guide, support, and 7 more developer resources.'
plans:
- name: Fruitscout Plans Pricing
  plan_count: 0
  slug: fruitscout-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Fruitscout Rate Limits
  slug: fruitscout-rate-limits
scopes:
- name: Fruitscout Scopes
  scope_count: 0
  slug: fruitscout-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 64.3
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.8
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fruitscout/fruitscout-2026-11-03T132350.png
security:
- kind: authentication
  name: Fruitscout Authentication
  slug: fruitscout-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fruitscout Domain Security
  slug: fruitscout-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: fruitscout
tags:
- Agriculture
- Artificial Intelligence
- Crop-Management
- Compliance
- Field Operations
website: https://fruitscout.ai/
---

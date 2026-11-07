---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for meeting coordination platform as described in developer documentation.
  name: Ask My Envoy API
  slug: ask-my-envoy-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/askmyenvoy-com/plans/askmyenvoy-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askmyenvoy-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/askmyenvoy-com/hosts/askmyenvoy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askmyenvoy-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/askmyenvoy-com/vendors/askmyenvoy-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askmyenvoy-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askmyenvoy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askmyenvoy.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://askmyenvoy.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/askmyenvoy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://askmyenvoy.com/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://askmyenvoy.com/getting-started
- group: auth
  href: https://artifacts.apis.io/askmyenvoy-com/security/askmyenvoy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askmyenvoy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askmyenvoy.com/
coverage:
  checked: '2026-11-01'
  detail: Developer documentation provides HTML pages but no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract.
  evidence:
  - status: 200
    url: https://askmyenvoy.com/developer
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Ask My Envoy provides AI‑driven meeting coordination software that automates scheduling across calendars, handling complex constraints and multi‑company meetings. The platform offers booking links, integrates with Google Calendar and Microsoft Outlook, and includes trust, control, and pricing tiers. It aims to replace paper planners with intelligent agents that manage availability, routing rules, and meeting logistics.
image: https://askmyenvoy.com/og-card.png
layout: provider
modified: '2026-11-01'
name: Ask My Envoy
nav: Providers
network: true
overview: 'Ask My Envoy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Meeting Coordination, Scheduling, Calendar Integration, and Automation.


  Ask My Envoy''s developer surface includes pricing, getting-started guide, and 9 more developer resources.'
plans:
- name: Askmyenvoy Com Plans Pricing
  plan_count: 2
  slug: askmyenvoy-com-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 20.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askmyenvoy Com Domain Security
  slug: askmyenvoy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: askmyenvoy-com
tags:
- Artificial Intelligence
- Meeting Coordination
- Scheduling
- Calendar Integration
- Automation
website: https://askmyenvoy.com/
---

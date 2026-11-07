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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AssessLane provides an MCP endpoint for AI integration.
  name: AssessLane API
  slug: assesslane-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/assesslane-com/well-known/assesslane-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/assesslane-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/assesslane-com/hosts/assesslane-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assesslane-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/assesslane-com/vendors/assesslane-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assesslane-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://assesslane.com/support
- group: start
  title: ''
  type: GettingStarted
  url: https://assesslane.com/mcp/setup
- group: auth
  href: https://artifacts.apis.io/assesslane-com/security/assesslane-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assesslane-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assesslane.com/
- group: start
  title: ''
  type: SignUp
  url: https://assesslane.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assesslane.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assesslane.com/legal/privacy
coverage:
  checked: '2026-11-02'
  detail: Provider documentation pages are rendered via JavaScript, preventing machine‑readable extraction of an API contract.
  evidence:
  - status: 200
    url: https://assesslane.com/mcp/setup
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AssessLane provides AI‑native team assessment tools that let organizations create, assign, and track knowledge‑check quizzes using any MCP‑compatible AI such as Claude or Cursor. Users can run a free 14‑day trial without a credit card, view sample assessments, and retrieve completion reports via the MCP interface. The platform offers per‑seat pricing starting at $3 per seat per month and supports unlimited quizzes and reporting.
image: https://assesslane.com/brand-icon.png
layout: provider
modified: '2026-11-01'
name: AssessLane
nav: Providers
network: true
overview: 'AssessLane is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Team Assessments, Software-as-a-Service, MCP, and Productivity.


  AssessLane''s developer surface includes support, getting-started guide, signup flow, and 7 more developer resources.'
plans:
- name: Assesslane Com Plans Pricing
  plan_count: 0
  slug: assesslane-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Assesslane Com Rate Limits
  slug: assesslane-com-rate-limits
scopes:
- name: Assesslane Com Scopes
  scope_count: 0
  slug: assesslane-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 17.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Assesslane Com Authentication
  slug: assesslane-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Assesslane Com Domain Security
  slug: assesslane-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: assesslane-com
tags:
- Artificial Intelligence
- Team Assessments
- Software-as-a-Service
- MCP
- Productivity
website: https://assesslane.com/
---

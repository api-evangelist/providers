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
    agent_skills: unknown
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Run your business from one connected workspace
  name: Toolspad API
  slug: toolspad-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/toolspad/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/toolspad/llms/toolspad-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/toolspad-llms.txt
- group: agent
  href: https://artifacts.apis.io/toolspad/well-known/toolspad-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/toolspad-well-known.yml
- group: other
  href: https://artifacts.apis.io/toolspad/hosts/toolspad-hosts.yml
  title: ''
  type: Hosts
  url: hosts/toolspad-hosts.yml
- group: other
  href: https://artifacts.apis.io/toolspad/vendors/toolspad-vendors.yml
  title: ''
  type: Vendors
  url: vendors/toolspad-vendors.yml
- group: auth
  href: https://artifacts.apis.io/toolspad/security/toolspad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toolspad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://toolspad.com
- group: commercial
  title: ''
  type: Pricing
  url: https://toolspad.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://toolspad.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://toolspad.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.toolspad.com/signup
coverage:
  checked: '2026-10-31'
  detail: API documentation is behind a login page; no public spec is available.
  evidence:
  - status: 200
    url: https://app.toolspad.com/login
  reason: auth-required
  state: gated
created: '2026-10-31'
description: ToolsPad provides a connected workspace that integrates CRM, sales, scheduling, delivery, billing, publishing and everyday operations for small and service businesses. With 21 built‑in applications such as Notes, Whiteboards, Tasks, Lead Forms, Surveys, Polls, Landing Pages, Subscription Tracker, Estimates & Quotes, Invoice Maker, Testimonial Collector, Business Calculators, Appointment Scheduling, Time Tracking, Smart Links, CRM, Opportunities, QR Code Generator, Dashboards, Documents & Media, and Blogs, it enables teams to run their entire workflow from a single platform, offering a free plan with 30‑day Premium trial and paid tiers starting at $19 per workspace.
image: https://toolspad.com/toolspad-logo-512.png
layout: provider
modified: '2026-10-31'
name: ToolsPad
nav: Providers
network: true
overview: 'ToolsPad is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, Software-as-a-Service, Productivity, Business, and Workspace.


  ToolsPad''s developer surface includes pricing, signup flow, and 9 more developer resources.'
random_paper: 6
scopes:
- name: Toolspad Scopes
  scope_count: 0
  slug: toolspad-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 18.1
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Toolspad Authentication
  slug: toolspad-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Toolspad Domain Security
  slug: toolspad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: toolspad
tags:
- CRM
- Software-as-a-Service
- Productivity
- Business
- Workspace
website: https://toolspad.com
---

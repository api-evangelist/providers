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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/aimgod-com/llms/aimgod-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aimgod-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aimgod-com/well-known/aimgod-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aimgod-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aimgod-com/hosts/aimgod-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aimgod-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aimgod-com/vendors/aimgod-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aimgod-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aimgod-com/security/aimgod-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aimgod-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aimgod.com/
- group: company
  title: ''
  type: Blog
  url: https://aimgod.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://aimgod.com/premium
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aimgod.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aimgod.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://aimgod.com/support
coverage:
  checked: '2026-11-01'
  detail: No public developer documentation or API reference pages were found on the company's website.
  evidence:
  - status: 200
    url: https://aimgod.com/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: Aimgod offers a personal day planner with built-in AI, helping users organize tasks, goals, and focus sessions. The platform provides a web app and iPhone application, integrates with calendars, and includes free forever plans without requiring a credit card. It emphasizes productivity through AI‑assisted planning and team collaboration features.
image: https://aimgod.com/landing/og.jpg
layout: provider
modified: '2026-11-01'
name: Aimgod
nav: Providers
network: true
overview: 'Aimgod is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Productivity, Artificial Intelligence, Planner, Team Collaboration, and Personal.


  Aimgod''s developer surface includes engineering blog, pricing, support, and 8 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 13.0
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aimgod Com Domain Security
  slug: aimgod-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aimgod-com
tags:
- Productivity
- Artificial Intelligence
- Planner
- Team Collaboration
- Personal
website: https://aimgod.com/
---

---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/calfeed-ai/plans/calfeed-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/calfeed-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/calfeed-ai/llms/calfeed-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/calfeed-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/calfeed-ai/hosts/calfeed-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calfeed-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/calfeed-ai/vendors/calfeed-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calfeed-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://calfeed.ai/sign-in
- group: auth
  href: https://artifacts.apis.io/calfeed-ai/security/calfeed-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calfeed-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calfeed.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://calfeed.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calfeed.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calfeed.ai/privacy
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are rendered via JavaScript and provide no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://calfeed.ai/learn
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Calfeed is a calendar publishing web app that lets users paste schedules, upload PDFs, photos, or spreadsheets, and instantly generate shareable calendar links for Apple, Google, or Outlook. Built by founder Ryan Scherf, Calfeed aims to simplify broadcasting schedules to audiences, offering features like event validation, gap detection, and quick calendar feed generation.
image: https://calfeed.ai/about/opengraph-image-1v42b1?c11680ee7d439dd3
layout: provider
modified: '2026-11-03'
name: Calfeed
nav: Providers
network: true
overview: 'Calfeed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Calendar, Productivity, Scheduling, and Web App.


  Calfeed''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Calfeed Ai Plans Pricing
  plan_count: 5
  slug: calfeed-ai-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 39.3
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calfeed Ai Domain Security
  slug: calfeed-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: calfeed-ai
tags:
- Calendar
- Productivity
- Scheduling
- Web App
website: https://calfeed.ai/
---

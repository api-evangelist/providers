---
access_model:
  confidence: low
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/easykanb-app/plans/easykanb-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/easykanb-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/easykanb-app/llms/easykanb-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easykanb-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/easykanb-app/well-known/easykanb-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easykanb-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/easykanb-app/hosts/easykanb-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easykanb-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/easykanb-app/vendors/easykanb-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easykanb-app-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://easykanb.app/blog/trello-vs-jira
- group: auth
  href: https://artifacts.apis.io/easykanb-app/security/easykanb-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easykanb-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easykanb.app/
- group: company
  title: ''
  type: Blog
  url: https://easykanb.app/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easykanb.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://easykanb.app/privacy
coverage:
  checked: '2026-11-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found despite public documentation.
  evidence:
  - status: 200
    url: https://easykanb.app/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: EasyKanban provides a free online kanban board with unlimited cards for personal work, freelancers, and small teams. It offers a calm, minimalist interface, real‑time collaboration, drag‑and‑drop, dark mode, and AI‑enhanced features in its Pro plan. The service is web‑based, requires no credit card to start, and aims to be a simple Trello alternative for focused productivity.
image: https://easykanb.app/opengraph-image?67ef44f00e6387d6
layout: provider
modified: '2026-11-06'
name: EasyKanban
nav: Providers
network: true
overview: 'EasyKanban is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Kanban, Productivity, Collaboration, Free, and Minimalist.


  EasyKanban''s developer surface includes getting-started guide, engineering blog, and 9 more developer resources.'
plans:
- name: Easykanb App Plans Pricing
  plan_count: 2
  slug: easykanb-app-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Easykanb App Domain Security
  slug: easykanb-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: easykanb-app
tags:
- Kanban
- Productivity
- Collaboration
- Free
- Minimalist
- Company
website: https://easykanb.app/
---

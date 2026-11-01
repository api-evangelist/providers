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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Documentation site for Agints platform offering AI agent services.
  name: Agints Docs API
  slug: agints-docs-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/agints-com/llms/agints-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agints-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agints-com/well-known/agints-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agints-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agints-com/hosts/agints-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agints-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agints-com/vendors/agints-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agints-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agints.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://agints.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agints.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://agints.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agints.com/
- group: auth
  href: https://artifacts.apis.io/agints-com/security/agints-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agints-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agints.com/
coverage:
  checked: '2026-10-30'
  detail: Docs site renders via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.agints.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Agints builds custom AI agents for businesses, offering a 24/7 AI phone receptionist named Gini that handles calls, transcriptions, and appointment bookings. Their platform provides a Skills Store with over 350 skills, customizable workflows, and integration with various tools. Pricing includes a free 14‑day trial, a pay‑per‑minute option, and enterprise installations with setup and monthly care fees. The company focuses on automating mundane web work, enhancing productivity, and delivering AI‑driven assistance for admin, growth, and other business functions.
image: https://agints.com/assets/og-default-1200x630.jpg
layout: provider
modified: '2026-10-29'
name: agints-com
nav: Providers
network: true
overview: 'agints-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Agents, Automation, Business, and SaaS.


  agints-com''s developer surface includes support, engineering blog, documentation, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agints Com Domain Security
  slug: agints-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agints-com
tags:
- AI
- Agents
- Automation
- Business
- SaaS
website: https://agints.com/
---

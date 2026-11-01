---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Risotto provides an AI help desk platform with integrations for Slack, Jira, Zendesk, Notion, and more.
  name: Risotto API
  slug: risotto-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/risotto/plans/risotto-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/risotto-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/risotto/llms/risotto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/risotto-llms.txt
- group: other
  href: https://artifacts.apis.io/risotto/hosts/risotto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/risotto-hosts.yml
- group: other
  href: https://artifacts.apis.io/risotto/vendors/risotto-vendors.yml
  title: ''
  type: Vendors
  url: vendors/risotto-vendors.yml
- group: auth
  href: https://artifacts.apis.io/risotto/security/risotto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/risotto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryrisotto.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.tryrisotto.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryrisotto.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.tryrisotto.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tryrisotto.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tryrisotto.com/privacy-policy
coverage:
  checked: '2026-10-22'
  detail: Documentation pages return 404 or redirect, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 301
    url: https://tryrisotto.com/openapi.json
  - status: 404
    url: https://www.tryrisotto.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Risotto is an AI help desk platform that automates internal support tickets, knowledge requests, access management, and troubleshooting with context‑aware AI. It integrates with Slack, Jira, Zendesk, Notion, Confluence and more, offering cross‑department functionality and IAM automations for IT teams.
image: https://cdn.prod.website-files.com/687df3ce131ebdf359c40fc7/68ac0e3a31e48d94e2f2cdbf_OG%20Image%20(1)%20(1).webp
layout: provider
modified: '2026-10-21'
name: Risotto
nav: Providers
network: true
overview: 'Risotto is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, HelpDesk, ITAutomation, and Ticketing.


  Risotto''s developer surface includes documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Risotto Plans Pricing
  plan_count: 2
  slug: risotto-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Risotto Domain Security
  slug: risotto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: risotto
tags:
- Company
- AI
- HelpDesk
- ITAutomation
- Ticketing
website: https://tryrisotto.com
---

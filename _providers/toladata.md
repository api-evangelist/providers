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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for TolaData platform, documented at the Help Center.
  name: TolaData API
  slug: toladata-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/toladata/plans/toladata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/toladata-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/toladata/changelog/toladata-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/toladata-changelog.yml
- group: agent
  href: https://artifacts.apis.io/toladata/llms/toladata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/toladata-llms.txt
- group: other
  href: https://artifacts.apis.io/toladata/hosts/toladata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/toladata-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.toladata.com/terms-and-policies/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.toladata.com/privacy/
- group: other
  title: ''
  type: Leadership
  url: https://www.toladata.com/team/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.toladata.com/docs/release-notes/
- group: auth
  href: https://artifacts.apis.io/toladata/security/toladata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toladata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://toladata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.toladata.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.toladata.com/docs/quick-start-guide/
- group: company
  title: ''
  type: Blog
  url: https://www.toladata.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.toladata.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.toladata.com/contact-us/
coverage:
  checked: '2026-10-21'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://www.toladata.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: TolaData provides a cloud‑based platform for nonprofit and development organizations to manage projects, track results, and report on impact. The service includes tools for data collection, monitoring, evaluation, and collaborative planning, helping NGOs and donors improve transparency and effectiveness. TolaData’s API enables integration with external systems for data exchange and automation, supporting a data‑driven approach to development work.
layout: provider
modified: '2026-10-21'
name: TolaData
nav: Providers
network: true
overview: 'TolaData is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Non-Profit, Monitoring, Evaluation, and Data Integration.


  TolaData''s developer surface includes changelog, documentation, getting-started guide, engineering blog, pricing, support, and 9 more developer resources.'
plans:
- name: Toladata Plans Pricing
  plan_count: 11
  slug: toladata-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Toladata Domain Security
  slug: toladata-domain-security
  summary_line: TLSv1.3 · DMARC
slug: toladata
tags:
- Company
- Non-Profit
- Monitoring
- Evaluation
- Data Integration
website: https://toladata.com/
---

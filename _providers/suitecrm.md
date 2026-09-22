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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: Security
  url: https://suitecrm.com/security-policy/security/
- group: company
  title: ''
  type: Newsroom
  url: https://suitecrm.com/category/news/
- group: start
  title: ''
  type: Login
  url: https://suitecrm.com/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SuiteCRM
- group: operate
  title: ''
  type: ChangeLog
  url: https://suitecrm.com/releases/
- group: company
  title: ''
  type: Blog
  url: https://suitecrm.com/hacktoberfest-2022-x-suitecrm/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/suitecrm/refs/heads/main/security/suitecrm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/suitecrm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://suitecrm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://suitecrm.com/what-is-suitecrm/
- group: start
  title: ''
  type: GettingStarted
  url: https://suitecrm.com/download/
- group: operate
  title: ''
  type: Roadmap
  url: https://suitecrm.com/suitecrm-roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://suitecrm.com/suitecrmhosted/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://suitecrm.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://suitecrm.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://suitecrm.com/contact-us/
coverage:
  checked: 2026-09-21
  detail: Documentation pages are served as HTML shells with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.suitecrm.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-21'
description: 'SuiteCRM is the world’s #1 open source CRM, offering self‑hosted deployments for full data sovereignty and a hosted SaaS option with no licence fees. It provides a flexible data model, robust reporting, and extensive customization for sales, marketing, and support teams. The platform supports on‑premise installations as well as SuiteCRM Hosted, delivering enterprise‑grade features without vendor lock‑in.'
image: https://suitecrm.com/wp-content/uploads/2018/01/favicon-144-1.png
layout: provider
modified: '2026-09-21'
name: SuiteCRM
nav: Providers
network: true
overview: 'SuiteCRM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, Open-Source, Software-as-a-Service, Self-Hosted, and Enterprise.


  SuiteCRM''s developer surface includes changelog, engineering blog, documentation, getting-started guide, pricing, support, and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 36.8
  provenance:
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Suitecrm Domain Security
  slug: suitecrm-domain-security
  summary_line: TLSv1.2 · DMARC
slug: suitecrm
tags:
- CRM
- Open-Source
- Software-as-a-Service
- Self-Hosted
- Enterprise
website: https://suitecrm.com/
---

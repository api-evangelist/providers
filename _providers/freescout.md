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
- description: FreeScout provides a REST API and webhooks for integration with its help desk platform.
  name: FreeScout API
  slug: freescout-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/freescout/hosts/freescout-hosts.yml
  title: ''
  type: Hosts
  url: hosts/freescout-hosts.yml
- group: other
  href: https://artifacts.apis.io/freescout/vendors/freescout-vendors.yml
  title: ''
  type: Vendors
  url: vendors/freescout-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://freescout.net/legal/terms/
- group: auth
  title: ''
  type: Security
  url: https://freescout.net/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://freescout.net/legal/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/freescout-helpdesk/freescout/wiki/Releases
- group: company
  title: ''
  type: Blog
  url: https://freescout.net/blog/category/news/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.freescout.net/
- group: auth
  href: https://artifacts.apis.io/freescout/security/freescout-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/freescout-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://freescout.net/
coverage:
  checked: '2026-10-26'
  detail: The provider's website lists an API page but no OpenAPI or other machine‑readable contract is publicly available.
  evidence:
  - status: 200
    url: https://freescout.net/module/api-webhooks/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: FreeScout is an open-source help desk and shared inbox solution built with PHP (Laravel). It offers omnichannel support via email, WhatsApp, Telegram, Facebook, Slack, live chat, and more. Features include AI‑powered assistance, unlimited agents, multi‑language UI, SAML SSO, OAuth for Microsoft 365 and Google Workspace, web‑push notifications, and extensive integrations via Zapier, Make, and custom modules. The platform is self‑hosted, privacy‑focused, and includes a REST API and webhooks for automation.
layout: provider
modified: '2026-10-26'
name: FreeScout
nav: Providers
network: true
overview: 'FreeScout is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HelpDesk, OpenSource, PHP, and Laravel.


  FreeScout''s developer surface includes changelog, engineering blog, documentation, and 7 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 26.3
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
  name: Freescout Domain Security
  slug: freescout-domain-security
  summary_line: TLSv1.3 · HSTS
slug: freescout
tags:
- Company
- HelpDesk
- OpenSource
- PHP
- Laravel
website: https://freescout.net/
---

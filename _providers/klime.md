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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Klime offers AI‑powered automation routines; the public documentation is at the Routines docs page.
  name: Klime API
  slug: klime-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/klime/plans/klime-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/klime-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/klime/hosts/klime-hosts.yml
  title: ''
  type: Hosts
  url: hosts/klime-hosts.yml
- group: other
  href: https://artifacts.apis.io/klime/vendors/klime-vendors.yml
  title: ''
  type: Vendors
  url: vendors/klime-vendors.yml
- group: build
  href: https://artifacts.apis.io/klime/packages/klime-packages.yml
  title: ''
  type: SDKs
  url: packages/klime-packages.yml
- group: build
  href: https://artifacts.apis.io/klime/packages/klime-packages.yml
  title: ''
  type: Packages
  url: packages/klime-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://klime.com/routines/team/sales
- group: auth
  href: https://artifacts.apis.io/klime/security/klime-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/klime-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://klime.com/
- group: docs
  title: ''
  type: Documentation
  url: https://klime.com/routines/works-with/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://klime.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://klime.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://klime.com/security
- group: commercial
  title: ''
  type: Pricing
  url: https://klime.com/pricing
coverage:
  checked: '2026-10-29'
  detail: Documentation is a JavaScript‑rendered SPA, so no machine‑readable spec was discoverable.
  evidence:
  - status: 200
    url: https://klime.com/routines/works-with/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Klime is an AI‑powered automation platform that helps teams streamline repetitive work by creating AI‑driven routines. Users can customize routines via chat, integrate with tools like Google Docs, Slack, and CRM systems, and approve AI‑generated outputs before they are sent. The service supports multiple languages, offers a pricing page, and provides a public documentation hub for routine setup and integrations. Founded in the Netherlands, Klime aims to boost productivity across sales, marketing, finance, and operations teams.
image: https://klime.com/api/og?v=13&d=eyJ0aXRsZSI6IlN0b3AgZG9pbmcgdGhlIHNhbWUgd29yayB0d2ljZS4iLCJtdXRlZCI6IlRoZXJlJ3MgQUkgZm9yIHRoYXQuIiwidmlzdWFsIjp7ImtpbmQiOiJyb3V0aW5lIiwiaWQiOiJwcmVwYXJlLWEtbW9ybmluZy1icmllZiIsImxvY2FsZSI6ImVuIn19&s=YNKRfcR-FfiGSMf8JzPxa8
layout: provider
modified: '2026-10-29'
name: Klime
nav: Providers
network: true
overview: 'Klime is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Productivity, Software-as-a-Service, and Collaboration.


  Klime''s developer surface includes documentation, pricing, and 11 more developer resources.'
plans:
- name: Klime Plans Pricing
  plan_count: 3
  slug: klime-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 58.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/klime/klime-2026-11-03T134445.png
security:
- kind: domain-security
  name: Klime Domain Security
  slug: klime-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: klime
tags:
- Artificial Intelligence
- Automation
- Productivity
- Software-as-a-Service
- Collaboration
website: https://klime.com/
---

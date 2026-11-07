---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
- description: REST API for interacting with Finicom. Non-public API for external integrations.
  name: Finicom API
  slug: finicom-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/finicom/plans/finicom-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/finicom-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/finicom/changelog/finicom-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/finicom-changelog.yml
- group: design
  href: https://artifacts.apis.io/finicom/conformance/finicom-conformance.yml
  title: ''
  type: Conformance
  url: conformance/finicom-conformance.yml
- group: other
  href: https://artifacts.apis.io/finicom/hosts/finicom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finicom-hosts.yml
- group: other
  href: https://artifacts.apis.io/finicom/vendors/finicom-vendors.yml
  title: ''
  type: Vendors
  url: vendors/finicom-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://finicom.com/docs/changelog
- group: auth
  href: https://artifacts.apis.io/finicom/security/finicom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finicom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finicom.com/
- group: docs
  title: ''
  type: Documentation
  url: https://finicom.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://finicom.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://finicom.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finicom.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finicom.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://finicom.com/docs
created: '2026-10-20'
description: Finicom offers a platform that synchronizes bank transaction data with applications such as Google Sheets, Notion, Airtable, Zapier, and Slack. It supports connections to over 12,000 financial institutions in the US and Canada and provides features like AI‑powered receipt and statement imports, real‑time notifications, and team collaboration tools. The service is available for personal use at no cost and includes paid tiers for additional connected banks and destinations.
image: https://finicom.com/api/og
layout: provider
modified: '2026-10-20'
name: Finicom
nav: Providers
network: true
overview: 'Finicom is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Automation, Data Sync, BusinessTools, and Integration.


  Finicom''s developer surface includes changelog, documentation, pricing, engineering blog, getting-started guide, and 9 more developer resources.'
plans:
- name: Finicom Plans Pricing
  plan_count: 4
  slug: finicom-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 27.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/finicom/finicom-2026-11-03T132037.png
security:
- kind: domain-security
  name: Finicom Domain Security
  slug: finicom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: finicom
tags:
- Fintech
- Automation
- Data Sync
- BusinessTools
- Integration
website: https://finicom.com/
---

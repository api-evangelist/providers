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
- description: CiraSync provides synchronization of Microsoft Directory contacts, calendars, and other data to mobile devices.
  name: CiraSync API
  slug: cirasync-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/cirasync/plans/cirasync-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cirasync-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cirasync/conformance/cirasync-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cirasync-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cirasync/llms/cirasync-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cirasync-llms.txt
- group: other
  href: https://artifacts.apis.io/cirasync/hosts/cirasync-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cirasync-hosts.yml
- group: other
  href: https://artifacts.apis.io/cirasync/vendors/cirasync-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cirasync-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://cirasync.com/blog-articles/security/cirasync-compliance-with-gdpr/
- group: company
  title: ''
  type: Newsroom
  url: https://cirasync.com/newsroom/
- group: operate
  title: ''
  type: ChangeLog
  url: https://cirasync.com/release-notes/cirahub-v0-5-11/
- group: start
  title: ''
  type: GettingStarted
  url: https://cirasync.com/quickstart-guide/auto-license-settings/
- group: auth
  href: https://artifacts.apis.io/cirasync/security/cirasync-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cirasync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cirasync.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.cirasync.com/
- group: operate
  title: ''
  type: Support
  url: https://cirasync.com/support-home/
- group: company
  title: ''
  type: Blog
  url: https://cirasync.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://cirasync.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://cirasync.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cirasync.com/terms-of-service/
coverage:
  checked: '2026-10-19'
  detail: Portal pages are rendered via Blazor SPA, no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://portal.cirasync.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: CiraApps Ltd provides CiraSync, a solution that synchronizes Microsoft Directory contacts, calendars, and other data to mobile phones quickly and securely. It supports one‑way, two‑way, and multi‑way sync across on‑prem and cloud environments, targeting industries such as healthcare, finance, government, and more. The platform emphasizes high security, on‑prem deployment options, and integration with popular services like Salesforce, QuickBooks, and HubSpot.
image: https://cirasync.com/wp-content/uploads/2019/04/contact-us-featured.jpg
layout: provider
modified: '2026-10-19'
name: CiraApps Ltd
nav: Providers
network: true
overview: 'CiraApps Ltd is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sync, Mobile, Directory, and Integration.


  CiraApps Ltd''s developer surface includes changelog, getting-started guide, support, engineering blog, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Cirasync Plans Pricing
  plan_count: 4
  slug: cirasync-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cirasync Domain Security
  slug: cirasync-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cirasync
tags:
- Company
- Sync
- Mobile
- Directory
- Integration
website: https://cirasync.com/
---

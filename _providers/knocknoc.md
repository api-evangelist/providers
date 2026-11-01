---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Knocknoc platform providing device provisioning, real‑time messaging and analytics.
  name: Knocknoc API
  slug: knocknoc-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/knocknoc/well-known/knocknoc-knocknoc-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/knocknoc-knocknoc-security.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://knocknoc.io/legal/privacy-policy/
- group: commercial
  href: https://artifacts.apis.io/knocknoc/plans/knocknoc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/knocknoc-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://www.knocknoc.io/contact-us/
- group: auth
  href: https://artifacts.apis.io/knocknoc/well-known/knocknoc-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/knocknoc-security.txt
- group: auth
  href: https://artifacts.apis.io/knocknoc/well-known/knocknoc-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/knocknoc-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/knocknoc/well-known/knocknoc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/knocknoc-well-known.yml
- group: other
  href: https://artifacts.apis.io/knocknoc/hosts/knocknoc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/knocknoc-hosts.yml
- group: other
  href: https://artifacts.apis.io/knocknoc/vendors/knocknoc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/knocknoc-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.knocknoc.io/
- group: start
  title: ''
  type: SignUp
  url: https://licensing.knocknoc.io/register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knocknoc-io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.knocknoc.io/books/admin-guide/page/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://dev.knocknoc.io/
- group: auth
  href: https://artifacts.apis.io/knocknoc/security/knocknoc-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/knocknoc-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/knocknoc/security/knocknoc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/knocknoc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://knocknoc.io
- group: operate
  title: ''
  type: Support
  url: https://knocknoc.io/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://knocknoc.io/pricing
coverage:
  detail: Docs site renders content via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.knocknoc.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Knocknoc provides a platform for secure, low‑latency communication between IoT devices and enterprise back‑ends. The service offers device provisioning, real‑time messaging, and analytics dashboards, all accessible via RESTful APIs and MQTT. Founded in 2022 and backed by Decibel, Knocknoc focuses on edge‑compute integration, OTA updates, and compliance with industry security standards, targeting smart‑home, industrial automation, and fleet management sectors.
image: https://knocknoc.io/wp-content/uploads/2022/12/Knocknoc_Symbol.svg
layout: provider
modified: '2026-10-29'
name: Knocknoc
nav: Providers
network: true
overview: 'Knocknoc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Communication, Edge Computing, and Security.


  Knocknoc''s developer surface includes signup flow, getting-started guide, documentation, support, pricing, and 14 more developer resources.'
plans:
- name: Knocknoc Plans Pricing
  plan_count: 5
  slug: knocknoc-plans-pricing
random_paper: 14
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Knocknoc Domain Security
  slug: knocknoc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Knocknoc Vulnerability Disclosure
  slug: knocknoc-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: knocknoc
tags:
- Company
- IoT
- Communication
- Edge Computing
- Security
website: https://knocknoc.io
---

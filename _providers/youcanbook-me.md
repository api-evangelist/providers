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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API reference page for YouCanBook.me (no machine-readable spec available).
  name: YouCanBook API
  slug: youcanbook-api
artifact_total: 4
common:
- group: start
  title: ''
  type: SignUp
  url: https://youcanbook.me/product-updates/registered-sms-booking-reminders-sent-from-a-registered-number-in-your-country
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/youcanbook-me/refs/heads/main/plans/youcanbook-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/youcanbook-me-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://youcanbook.me/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/youcanbook-me/refs/heads/main/conformance/youcanbook-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/youcanbook-me-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/youcanbook-me/refs/heads/main/llms/youcanbook-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/youcanbook-me-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/youcanbook-me/refs/heads/main/hosts/youcanbook-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/youcanbook-me-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/youcanbook-me/refs/heads/main/vendors/youcanbook-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/youcanbook-me-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/youcanbook-me/refs/heads/main/packages/youcanbook-me-packages.yml
  title: ''
  type: SDKs
  url: packages/youcanbook-me-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/youcanbook-me/refs/heads/main/packages/youcanbook-me-packages.yml
  title: ''
  type: Packages
  url: packages/youcanbook-me-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://youcanbook.me/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/youcanbook-me/refs/heads/main/security/youcanbook-me-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/youcanbook-me-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/youcanbook-me/refs/heads/main/security/youcanbook-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/youcanbook-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://youcanbook.me
- group: operate
  title: ''
  type: Support
  url: https://youcanbook.me/help
- group: company
  title: ''
  type: Blog
  url: https://youcanbook.me/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://youcanbook.me/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://youcanbook.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://youcanbook.me/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/youcanbookme/workspace
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://youcanbook.me/mcp
  - status: 200
    url: https://youcanbook.me
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: YouCanBook.me provides a free online scheduling tool that helps individuals and businesses create customizable booking pages, manage availability, automate notifications, accept payments, and integrate with calendars. The platform supports various use cases across industries such as beauty, coaching, education, healthcare, and more, offering features like meeting polls, admin controls, analytics, and virtual meeting integrations. It aims to save time, attract more clients, and generate revenue for small to midsize businesses.
image: https://youcanbook.me/hubfs/1200x630-Cover-Image.png
layout: provider
modified: '2026-10-13'
name: YouCanBook.me
nav: Providers
network: true
overview: 'YouCanBook.me is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Scheduling, Software-as-a-Service, Automation, and Integration.


  YouCanBook.me''s developer surface includes signup flow, support, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Youcanbook Me Plans Pricing
  plan_count: 4
  slug: youcanbook-me-plans-pricing
random_paper: 17
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.3
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Youcanbook Me Domain Security
  slug: youcanbook-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Youcanbook Me Trust Center
  slug: youcanbook-me-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: youcanbook-me
tags:
- Company
- Scheduling
- Software-as-a-Service
- Automation
- Integration
website: https://youcanbook.me
---

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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/azibo/refs/heads/main/plans/azibo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/azibo-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azibo/refs/heads/main/hosts/azibo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azibo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/azibo/refs/heads/main/vendors/azibo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/azibo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.azibo.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.azibo.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.azibo.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.azibo.com/team/jk-paek
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/azibo/refs/heads/main/security/azibo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azibo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.azibo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.azibo.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.azibo.com/pricing
- group: company
  title: ''
  type: About
  url: https://www.azibo.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.azibo.com/contact-us
- group: operate
  title: ''
  type: Roadmap
  url: https://www.azibo.com/product-road-map
- group: company
  title: ''
  type: Careers
  url: https://www.azibo.com/careers
- group: start
  title: ''
  type: SignUp
  url: https://www.azibo.com/signup-renter
- group: start
  title: ''
  type: Login
  url: https://app.azibo.com/login
coverage:
  checked: 2026-09-27
  detail: The documentation site renders via JavaScript and provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.azibo.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Azibo provides a free, cloud‑based platform that simplifies rental property financial management for landlords. It offers tools for rent collection, tenant screening, lease agreements, document storage, maintenance requests, accounting, and reporting, all integrated to help property owners achieve financial flexibility and streamline operations.
image: https://cdn.prod.website-files.com/642f473d941777c50fefada7/64650f1c75f6f7f1c0d8cd74_opengraph.webp
layout: provider
modified: '2026-09-27'
name: Azibo
nav: Providers
network: true
overview: 'Azibo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Property Management, Fintech, Software-as-a-Service, and Landlord Tools.


  Azibo''s developer surface includes documentation, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Azibo Plans Pricing
  plan_count: 2
  slug: azibo-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 51.8
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Azibo Domain Security
  slug: azibo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azibo
tags:
- Real Estate
- Property Management
- Fintech
- Software-as-a-Service
- Landlord Tools
- Company
website: https://www.azibo.com/
---

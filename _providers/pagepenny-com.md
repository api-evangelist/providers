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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Templated PDF and image generation API.
  name: PagePenny API
  slug: pagepenny-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/pagepenny-com/plans/pagepenny-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pagepenny-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pagepenny-com/conformance/pagepenny-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pagepenny-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pagepenny-com/llms/pagepenny-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pagepenny-com-llms.txt
- group: other
  href: https://artifacts.apis.io/pagepenny-com/hosts/pagepenny-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pagepenny-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pagepenny-com/vendors/pagepenny-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pagepenny-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://pagepenny.com/login
- group: auth
  href: https://artifacts.apis.io/pagepenny-com/security/pagepenny-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pagepenny-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pagepenny.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pagepenny.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://pagepenny.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pagepenny.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pagepenny.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pagepenny.com/tools
created: '2026-10-30'
description: PagePenny provides a low‑cost PDF and image generation API that renders templates into PDFs, PNGs, and social images for a penny per render. Users can send JSON data with a chosen template to receive invoices, receipts, reports, or custom graphics instantly via a simple HTTP POST. The service offers a free tier with 100 renders per month and paid usage at $0.01 per render. Documentation, pricing, and a live demo are available on the site, and an API key can be obtained after login.
image: https://pagepenny.com/og.png
layout: provider
modified: '2026-10-30'
name: pagepenny-com
nav: Providers
network: true
overview: 'pagepenny-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API, Templates, Developers, and Automation.


  pagepenny-com''s developer surface includes documentation, pricing, and 11 more developer resources.'
plans:
- name: Pagepenny Com Plans Pricing
  plan_count: 1
  slug: pagepenny-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.2
    catalog_earned_first_party: 0.0
    catalog_gap: 75.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pagepenny Com Domain Security
  slug: pagepenny-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pagepenny-com
tags:
- API
- Templates
- Developers
- Automation
website: https://pagepenny.com/
---

---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/auctria/plans/auctria-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auctria-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/auctria/llms/auctria-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auctria-llms.txt
- group: agent
  href: https://artifacts.apis.io/auctria/well-known/auctria-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/auctria-well-known.yml
- group: other
  href: https://artifacts.apis.io/auctria/hosts/auctria-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auctria-hosts.yml
- group: other
  href: https://artifacts.apis.io/auctria/vendors/auctria-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auctria-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.auctria.com/news/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.auctria.com/webinar/getting-started-with-auctria
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Auctria
- group: auth
  href: https://artifacts.apis.io/auctria/security/auctria-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auctria-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.auctria.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.auctria.com/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.auctria.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.auctria.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auctria.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/7817344
- group: operate
  title: ''
  type: Support
  url: https://www.auctria.com/contact/
coverage:
  checked: '2026-10-27'
  detail: The developer portal at https://www.auctria.com/developers loads a JavaScript‑rendered single‑page app, preventing machine‑readable discovery of an OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.auctria.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Auctria provides a cloud‑based fundraising platform that helps nonprofits run auctions, ticketed events, and donation campaigns. Its solution includes event websites, payment processing, mobile apps, and analytics to streamline donor engagement and maximize fundraising outcomes. The platform is designed for ease of use, offering tools for event creation, ticket sales, auction management, and comprehensive reporting, all accessible via a web interface.
image: https://www.auctria.com/logo.png
layout: provider
modified: '2026-10-27'
name: Auctria
nav: Providers
network: true
overview: 'Auctria is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fundraising, Nonprofit, SaaS, and Auctions.


  Auctria''s developer surface includes getting-started guide, documentation, pricing, engineering blog, support, and 11 more developer resources.'
plans:
- name: Auctria Plans Pricing
  plan_count: 3
  slug: auctria-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auctria Domain Security
  slug: auctria-domain-security
  summary_line: TLSv1.3 · DMARC
slug: auctria
tags:
- Company
- Fundraising
- Nonprofit
- SaaS
- Auctions
website: https://www.auctria.com/
---

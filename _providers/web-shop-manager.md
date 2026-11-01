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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/web-shop-manager/conformance/web-shop-manager-conformance.yml
  title: ''
  type: Conformance
  url: conformance/web-shop-manager-conformance.yml
- group: agent
  href: https://artifacts.apis.io/web-shop-manager/llms/web-shop-manager-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/web-shop-manager-llms.txt
- group: agent
  href: https://artifacts.apis.io/web-shop-manager/well-known/web-shop-manager-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/web-shop-manager-well-known.yml
- group: other
  href: https://artifacts.apis.io/web-shop-manager/hosts/web-shop-manager-hosts.yml
  title: ''
  type: Hosts
  url: hosts/web-shop-manager-hosts.yml
- group: other
  href: https://artifacts.apis.io/web-shop-manager/vendors/web-shop-manager-vendors.yml
  title: ''
  type: Vendors
  url: vendors/web-shop-manager-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://webshopmanager.com/sign-up-for-wsm-text-alerts/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://webshopmanager.com/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.webshopmanager.com/google-analytics-site-search-tracking-setup
- group: docs
  title: ''
  type: Documentation
  url: https://help.webshopmanager.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/webshopmanager
- group: auth
  href: https://artifacts.apis.io/web-shop-manager/security/web-shop-manager-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/web-shop-manager-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://webshopmanager.com/
- group: company
  title: ''
  type: Blog
  url: https://webshopmanager.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://webshopmanager.com/pricing/
coverage:
  checked: '2026-10-27'
  detail: Homepage loads via JavaScript and provides no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://webshopmanager.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Web Shop Manager provides a cloud‑based platform that enables merchants to create, manage, and scale their online stores with integrated inventory, order processing, payment gateways, and analytics. The solution offers customizable storefront themes, multi‑channel sales support, and robust APIs for developers to extend functionality, automate workflows, and integrate third‑party services. Targeted at small to medium‑size businesses, it aims to simplify e‑commerce operations while delivering a seamless shopping experience for end‑customers.
image: https://webshopmanager.com/wp-content/uploads/2026/05/wsm-og-default.jpg
layout: provider
modified: '2026-10-27'
name: Web Shop Manager
nav: Providers
network: true
overview: 'Web Shop Manager is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include eCommerce, Automotive, SaaS, B2B, and API.


  Web Shop Manager''s developer surface includes signup flow, getting-started guide, documentation, engineering blog, pricing, and 9 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: derived
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
  name: Web Shop Manager Domain Security
  slug: web-shop-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: web-shop-manager
tags:
- eCommerce
- Automotive
- SaaS
- B2B
- API
website: https://webshopmanager.com/
---

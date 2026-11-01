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
- group: agent
  href: https://artifacts.apis.io/dealmaker/llms/dealmaker-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dealmaker-llms.txt
- group: auth
  href: https://artifacts.apis.io/dealmaker/well-known/dealmaker-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dealmaker-support-security.txt
- group: agent
  href: https://artifacts.apis.io/dealmaker/well-known/dealmaker-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dealmaker-well-known.yml
- group: other
  href: https://artifacts.apis.io/dealmaker/hosts/dealmaker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealmaker-hosts.yml
- group: other
  href: https://artifacts.apis.io/dealmaker/vendors/dealmaker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealmaker-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dealmaker.tech/terms
- group: operate
  title: ''
  type: Support
  url: https://help.dealmaker.tech/
- group: auth
  title: ''
  type: Security
  url: https://www.dealmaker.tech/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dealmaker.tech/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.dealmaker.tech/category/press
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.dealmaker.tech/developer/applications
- group: company
  title: ''
  type: Blog
  url: https://www.dealmaker.tech/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.dealmaker.tech/whats-the-process-for-onboarding-with-dealmaker-shareholder-services
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dealmaker.tech/
- group: auth
  href: https://artifacts.apis.io/dealmaker/security/dealmaker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealmaker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dealmaker.tech/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.dealmaker.tech/mcp
  - status: 200
    url: https://www.dealmaker.tech/
  - status: 403
    url: https://forgeglobal.com/dealmaker_stock/
  reason: partner-login
  state: gated
created: '2026-10-22'
description: DealMaker is a capital‑raising platform that enables businesses to raise funds from everyday investors through an end‑to‑end online solution. Founded by capital‑markets lawyers, the service has facilitated over $2 billion in raises for more than 500 k investors across diverse industries such as sports, robotics, cleantech, hospitality and media. DealMaker provides tools for campaign creation, investor relations, compliance, and marketing, positioning itself as a comprehensive fintech solution for private capital formation.
image: https://cdn.prod.website-files.com/656f55af4b70f4ce7ae4b997/685d988c9d3abae4ca097302_opengraphimage.png
layout: provider
modified: '2026-10-22'
name: DealMaker
nav: Providers
network: true
overview: 'DealMaker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Capital Raising, Investment Platform, and Software-as-a-Service.


  DealMaker''s developer surface includes support, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 18.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: derived
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
  name: Dealmaker Domain Security
  slug: dealmaker-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dealmaker
tags:
- Company
- Fintech
- Capital Raising
- Investment Platform
- Software-as-a-Service
website: https://www.dealmaker.tech/
---

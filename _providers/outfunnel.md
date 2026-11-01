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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Outfunnel provides a sales and marketing workflow platform with API documentation at the support site.
  name: Outfunnel API
  slug: outfunnel-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/outfunnel/plans/outfunnel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/outfunnel-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/outfunnel/llms/outfunnel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/outfunnel-llms.txt
- group: auth
  href: https://artifacts.apis.io/outfunnel/well-known/outfunnel-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/outfunnel-support-security.txt
- group: agent
  href: https://artifacts.apis.io/outfunnel/well-known/outfunnel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/outfunnel-well-known.yml
- group: other
  href: https://artifacts.apis.io/outfunnel/hosts/outfunnel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/outfunnel-hosts.yml
- group: other
  href: https://artifacts.apis.io/outfunnel/vendors/outfunnel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/outfunnel-vendors.yml
- group: auth
  href: https://artifacts.apis.io/outfunnel/security/outfunnel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/outfunnel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://outfunnel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://outfunnel.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://outfunnel.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://outfunnel.com/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.outfunnel.com/en/
- group: company
  title: ''
  type: About
  url: https://outfunnel.com/about/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://outfunnel.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://outfunnel.com/terms/
coverage:
  checked: '2026-10-21'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the provider's API host.
  evidence:
  - status: 404
    url: https://api.outfunnel.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Outfunnel provides a sales and marketing workflow platform that synchronizes CRM data with email, spreadsheet, and other marketing tools, automating data flow to eliminate manual work. The service offers features such as contact syncing, engagement tracking, lead forms, integrations with popular apps, pricing plans for startups to enterprises, a help center, blog, and resources. It aims to give sales teams more context and streamline marketing operations across platforms.
image: https://outfunnel.com/wp-content/uploads/2021/03/outfunnel-connecting-things-transparent-square.png
layout: provider
modified: '2026-10-21'
name: Outfunnel
nav: Providers
network: true
overview: 'Outfunnel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Marketing, Automation, and Integration.


  Outfunnel''s developer surface includes documentation, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Outfunnel Plans Pricing
  plan_count: 3
  slug: outfunnel-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Outfunnel Domain Security
  slug: outfunnel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: outfunnel
tags:
- Company
- Sales
- Marketing
- Automation
- Integration
website: https://outfunnel.com/
---

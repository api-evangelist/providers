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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/insignia-financial/hosts/insignia-financial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/insignia-financial-hosts.yml
- group: build
  href: https://artifacts.apis.io/insignia-financial/integrations/insignia-financial-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/insignia-financial-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/insignia-financial/vendors/insignia-financial-vendors.yml
  title: ''
  type: Vendors
  url: vendors/insignia-financial-vendors.yml
- group: auth
  href: https://artifacts.apis.io/insignia-financial/security/insignia-financial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/insignia-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://insigniafinancial.com.au/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insigniafinancial.com.au/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.insigniafinancial.com.au/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/insignia-financial
created: '2026-10-21'
description: 'Insignia Financial Ltd (ASX: IFL), formerly IOOF Holdings (renamed December 2021), is an Australian wealth management group headquartered in Docklands, Melbourne, with roots dating to 1846. It runs a multibranded, vertically integrated model spanning financial advice, superannuation and investment platforms (master trust and wrap), and asset management, under brands including MLC and IOOF. No public developer API, developer portal or API documentation was found; its website (insigniafinancial.com.au) sits behind an Akamai edge that refuses automated clients.'
layout: provider
modified: '2026-10-21'
name: Insignia Financial
nav: Providers
network: true
overview: 'Insignia Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Wealth Management, Superannuation, and Asset Management.


  Insignia Financial''s developer surface includes support and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 6.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Insignia Financial Domain Security
  slug: insignia-financial-domain-security
  summary_line: DMARC
slug: insignia-financial
tags:
- Company
- Financial Services
- Wealth Management
- Superannuation
- Asset Management
- Financial Advice
- Australia
website: https://insigniafinancial.com.au/
---

---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: No public developer API documented; only a Shopify storefront GraphQL endpoint was discovered, which belongs to Shopify, not Cala Systems.
  name: Cala Systems API
  slug: cala-systems-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cala-systems/refs/heads/main/llms/cala-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cala-systems-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cala-systems/refs/heads/main/well-known/cala-systems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cala-systems-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cala-systems/refs/heads/main/hosts/cala-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cala-systems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cala-systems/refs/heads/main/vendors/cala-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cala-systems-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.calasystems.com/terms-of-sale
- group: operate
  title: ''
  type: Support
  url: https://www.calasystems.com/mobile-app/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.calasystems.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.calasystems.com/news/were-shipping-cala
- group: start
  title: ''
  type: Login
  url: https://www.calasystems.com/log-in
- group: company
  title: ''
  type: Blog
  url: https://www.calasystems.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.calasystems.com/news/the-ira-may-be-ending-but-the-future-of-heat-pump-water-heaters-is-just-getting-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cala-systems/refs/heads/main/security/cala-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cala-systems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.calasystems.com/
- group: other
  title: ''
  type: Image
  url: https://cdn.prod.website-files.com/66ab6ecca15b64cceee53ca0/66c8477e956e0699ad18307d_cala-og-preview.png
created: '2026-10-06'
description: Cala Systems designs and manufactures intelligent heat pump water heaters that customize heating for each home daily, delivering reliable hot water while significantly reducing energy costs. Proudly designed and assembled in the USA, the company focuses on innovative, energy‑efficient solutions for residential water heating, backed by extensive technical specifications, savings calculators, and a network of professional installers.
image: https://cdn.prod.website-files.com/66ab6ecca15b64cceee53ca0/66c8477e956e0699ad18307d_cala-og-preview.png
layout: provider
modified: '2026-10-06'
name: Cala Systems
nav: Providers
network: true
overview: 'Cala Systems is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HeatPump, WaterHeater, EnergyEfficiency, and USA.


  Cala Systems'' developer surface includes support, engineering blog, getting-started guide, and 11 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cala Systems Domain Security
  slug: cala-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cala-systems
tags:
- Company
- HeatPump
- WaterHeater
- EnergyEfficiency
- USA
website: https://www.calasystems.com/
---

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
  href: https://artifacts.apis.io/green-chef/hosts/green-chef-hosts.yml
  title: ''
  type: Hosts
  url: hosts/green-chef-hosts.yml
- group: other
  href: https://artifacts.apis.io/green-chef/vendors/green-chef-vendors.yml
  title: ''
  type: Vendors
  url: vendors/green-chef-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greenchef.com:443/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greenchef.com:443/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.greenchef.com:443/plans
- group: auth
  href: https://artifacts.apis.io/green-chef/security/green-chef-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/green-chef-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.greenchef.com:443/
- group: docs
  title: ''
  type: Documentation
  url: https://www.greenchef.com/about/how-it-works
- group: docs
  title: ''
  type: Documentation
  url: https://www.greenchef.com/plans
- group: docs
  title: ''
  type: Documentation
  url: https://www.greenchef.com/about/app
coverage:
  checked: '2026-10-26'
  detail: The provider's website serves only HTML pages with no OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.greenchef.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Green Chef provides organic meal‑kit delivery services, offering chef‑crafted recipes with responsibly sourced produce and premium proteins. Customers receive weekly boxes containing fresh ingredients, detailed cooking instructions, and nutrition information, supporting healthy lifestyles while minimizing food waste. The company emphasizes sustainability, seasonal menus, and convenient home cooking solutions for busy individuals and families.
image: https://hf-website-live.s3.eu-west-1.amazonaws.com/us/greenchef/Web_Large-Banner_NABRAND-47306_GC_UniversalLinkPreview-CRO_2026-05.jpg
layout: provider
modified: '2026-10-26'
name: Green Chef
nav: Providers
network: true
overview: 'Green Chef is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MealKit, Organic, Sustainability, and Food.


  Green Chef''s developer surface includes pricing, documentation, and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
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
  name: Green Chef Domain Security
  slug: green-chef-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: green-chef
tags:
- Company
- MealKit
- Organic
- Sustainability
- Food
website: https://www.greenchef.com:443/
---

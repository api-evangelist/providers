---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: GraphQL endpoint providing schema for Colorescience data.
  name: GraphQL API
  slug: graphql-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/colorescience/llms/colorescience-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/colorescience-llms.txt
- group: agent
  href: https://artifacts.apis.io/colorescience/well-known/colorescience-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/colorescience-well-known.yml
- group: other
  href: https://artifacts.apis.io/colorescience/hosts/colorescience-hosts.yml
  title: ''
  type: Hosts
  url: hosts/colorescience-hosts.yml
- group: other
  href: https://artifacts.apis.io/colorescience/vendors/colorescience-vendors.yml
  title: ''
  type: Vendors
  url: vendors/colorescience-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.colorescience.com/pages/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.colorescience.com/pages/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.colorescience.com/pages/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.colorescience.com/blogs/blog
- group: auth
  href: https://artifacts.apis.io/colorescience/security/colorescience-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/colorescience-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.colorescience.com
created: '2026-10-09'
description: Colorescience is a premium skincare brand specializing in mineral sunscreen and clinical skincare products. Founded in 2006, the company offers a range of SPF formulations, serums, moisturizers, and cosmetics designed for health-conscious consumers. Their mission is to provide dermatologist-recommended, broad-spectrum sun protection while supporting skin health through science-backed ingredients and sustainable practices. The brand operates an e‑commerce site, a professional B2B portal, and provides educational resources for skin health.
image: https://cdn.shopify.com/s/files/1/0251/2184/9419/files/colorescience-logo_1.png?height=628&pad_color=fff&v=1613529315&width=1200
layout: provider
modified: '2026-10-09'
name: Colorescience
nav: Providers
network: true
overview: 'Colorescience is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Skincare, Sunscreen, Cosmetics, Health, and E-Commerce.


  Colorescience''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 12.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Colorescience Domain Security
  slug: colorescience-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: colorescience
tags:
- Skincare
- Sunscreen
- Cosmetics
- Health
- E-Commerce
website: https://www.colorescience.com
---

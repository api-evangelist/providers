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
- description: GraphQL API providing access to Xena Workwear product and store data.
  name: Xena Workwear GraphQL API
  slug: xena-workwear-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xena-workwear/refs/heads/main/llms/xena-workwear-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xena-workwear-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xena-workwear/refs/heads/main/well-known/xena-workwear-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xena-workwear-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xena-workwear/refs/heads/main/hosts/xena-workwear-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xena-workwear-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xena-workwear/refs/heads/main/vendors/xena-workwear-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xena-workwear-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xenaworkwear.com/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xenaworkwear.com/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://xenaworkwear.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xena-workwear/refs/heads/main/security/xena-workwear-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xena-workwear-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xenaworkwear.com
- group: company
  title: ''
  type: Blog
  url: https://xenaworkwear.com/blogs/blog
- group: operate
  title: ''
  type: Support
  url: https://xenaworkwear.com/pages/contact-us
created: '2026-10-12'
description: Xena Workwear designs and sells safety footwear and work apparel specifically for women. Their product line includes steel‑toe boots, slip‑resistant shoes, and rugged workwear, emphasizing comfort, durability, and style. The company operates an online store, provides a blog with industry news, and offers a store locator for physical retail partners. Founded with backing from Starting Line VC, Xena Workwear aims to fill a niche in women‑focused occupational footwear.
image: https://xenaworkwear.com/assets/logo.png
layout: provider
modified: '2026-10-12'
name: Xena Workwear
nav: Providers
network: true
overview: 'Xena Workwear is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Footwear, Women, Safety, and E-Commerce.


  Xena Workwear''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Xena Workwear Domain Security
  slug: xena-workwear-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xena-workwear
tags:
- Company
- Footwear
- Women
- Safety
- E-Commerce
website: https://xenaworkwear.com
---

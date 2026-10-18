---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: BuildDirect provides an online marketplace for flooring products. The API surface is not publicly documented; only a GraphQL endpoint was discovered but appears to belong to the underlying Shopify pla
  name: BuildDirect API
  slug: builddirect-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/builddirect-technologies/refs/heads/main/llms/builddirect-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/builddirect-technologies-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/builddirect-technologies/refs/heads/main/well-known/builddirect-technologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/builddirect-technologies-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/builddirect-technologies/refs/heads/main/hosts/builddirect-technologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/builddirect-technologies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/builddirect-technologies/refs/heads/main/vendors/builddirect-technologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/builddirect-technologies-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.builddirect.com/pages/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.builddirect.com/pages/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.builddirect.com/blogs/news
- group: company
  title: ''
  type: Blog
  url: https://blog.builddirect.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/builddirect-technologies/refs/heads/main/security/builddirect-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/builddirect-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.builddirect.com
created: '2026-10-06'
description: BuildDirect is an online marketplace specializing in flooring products, offering a wide selection of hardwood, laminate, vinyl, and tile flooring for both residential and commercial projects. The platform provides expert guidance, detailed product information, and a streamlined purchasing experience, enabling customers to browse, compare, and order flooring materials directly online with delivery options across North America. BuildDirect aims to simplify the flooring buying process through competitive pricing, extensive inventory, and dedicated customer support.
image: https://www.builddirect.com/cdn/shop/files/builddirect-og-image.jpg?v=1690822919&width=1200
layout: provider
modified: '2026-10-06'
name: BuildDirect
nav: Providers
network: true
overview: 'BuildDirect is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Flooring, Home Improvement, Building Materials, and Trade Services.


  BuildDirect''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Builddirect Technologies Domain Security
  slug: builddirect-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: builddirect-technologies
tags:
- Flooring
- Home Improvement
- Building Materials
- Trade Services
website: https://www.builddirect.com
---

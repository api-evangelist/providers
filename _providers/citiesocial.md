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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/citiesocial/refs/heads/main/llms/citiesocial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/citiesocial-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/citiesocial/refs/heads/main/well-known/citiesocial-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/citiesocial-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/citiesocial/refs/heads/main/hosts/citiesocial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/citiesocial-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/citiesocial/refs/heads/main/vendors/citiesocial-vendors.yml
  title: ''
  type: Vendors
  url: vendors/citiesocial-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/citiesocial/refs/heads/main/packages/citiesocial-packages.yml
  title: ''
  type: SDKs
  url: packages/citiesocial-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/citiesocial/refs/heads/main/packages/citiesocial-packages.yml
  title: ''
  type: Packages
  url: packages/citiesocial-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.citiesocial.com/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.citiesocial.com/pages/privacypolicy
- group: company
  title: ''
  type: Newsroom
  url: https://www.citiesocial.com/blogs/news
- group: company
  title: ''
  type: Blog
  url: https://www.citiesocial.com/a/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/citiesocial
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/citiesocial/refs/heads/main/security/citiesocial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/citiesocial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.citiesocial.com
coverage:
  checked: '2026-10-08'
  detail: The provider's GraphQL endpoint at https://www.citiesocial.com/api/graphql returns JSON but cannot be verified as owned by Citiesocial.
  evidence:
  - status: 200
    url: https://www.citiesocial.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Citiesocial is a Taiwan‑based curated e‑commerce marketplace that connects consumers with premium global brands. Founded in 2011, it offers cross‑border logistics, brand localization, and omni‑channel sales, serving over 600,000 customers across Taiwan, Singapore, Malaysia and Japan. The platform showcases a wide range of lifestyle, tech, fashion and home products, emphasizing quality and curated selections for modern living.
image: http://www.citiesocial.com/cdn/shop/files/cs-og-image-0914_800x800.png?v=1753420633
layout: provider
modified: '2026-10-08'
name: Citiesocial
nav: Providers
network: true
overview: 'Citiesocial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Marketplace, curated, Taiwan, and Cross-Border.


  Citiesocial''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 12.3
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
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 5.3
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
  name: Citiesocial Domain Security
  slug: citiesocial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: citiesocial
tags:
- E-Commerce
- Marketplace
- curated
- Taiwan
- Cross-Border
website: https://www.citiesocial.com
---

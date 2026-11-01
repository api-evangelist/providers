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
api_count: 1
apis:
- description: IMIA does not appear to publish a public API; attempts to locate OpenAPI or other contracts on the documented API host returned 404.
  name: IMIA API
  slug: imia-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/international-map-industry-association-imia/llms/international-map-industry-association-imia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/international-map-industry-association-imia-llms.txt
- group: other
  href: https://artifacts.apis.io/international-map-industry-association-imia/hosts/international-map-industry-association-imia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/international-map-industry-association-imia-hosts.yml
- group: other
  href: https://artifacts.apis.io/international-map-industry-association-imia/vendors/international-map-industry-association-imia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/international-map-industry-association-imia-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imiamaps.org/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://imiamaps.org/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://imiamaps.org/category/news/
- group: company
  title: ''
  type: Blog
  url: https://imiamaps.org/category/blog/
- group: auth
  href: https://artifacts.apis.io/international-map-industry-association-imia/security/international-map-industry-association-imia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/international-map-industry-association-imia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://imiamaps.org/
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found on the API host (api.imiamaps.org) despite probing common spec endpoints.
  evidence:
  - status: 404
    url: https://api.imiamaps.org/openapi.json
  - status: 404
    url: https://api.imiamaps.org/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: The International Map Industry Association (IMIA) is a global nonprofit organization that connects map publishers, geospatial companies, data providers, retailers, and technology partners. Through membership, events, sponsorship opportunities, and industry collaborations, IMIA promotes the business of maps, supports standards, and fosters networking among mapping professionals worldwide.
image: https://imiamaps.org/wp-content/uploads/2026/06/home-hero-1.jpg
layout: provider
modified: '2026-10-26'
name: International Map Industry Association (IMIA)
nav: Providers
network: true
overview: 'International Map Industry Association (IMIA) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mapping, Geospatial, Nonprofit, and Industry.


  International Map Industry Association (IMIA)''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 0.0
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
  name: International Map Industry Association Imia Domain Security
  slug: international-map-industry-association-imia-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: international-map-industry-association-imia
tags:
- Company
- Mapping
- Geospatial
- Nonprofit
- Industry
website: https://imiamaps.org/
---

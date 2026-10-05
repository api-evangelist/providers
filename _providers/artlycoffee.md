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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/artlycoffee/refs/heads/main/llms/artlycoffee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/artlycoffee-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/artlycoffee/refs/heads/main/well-known/artlycoffee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/artlycoffee-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artlycoffee/refs/heads/main/hosts/artlycoffee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artlycoffee-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artlycoffee/refs/heads/main/vendors/artlycoffee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artlycoffee-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artly.coffee/pages/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artlycoffee/refs/heads/main/security/artlycoffee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artlycoffee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artly.coffee
coverage:
  checked: 2026-09-26
  detail: GraphQL endpoint is public but the schema belongs to Shopify, not Artlycoffee, so no owned contract.
  evidence:
  - status: 200
    url: https://artly.coffee/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Artlycoffee is a coffee‑related technology company that appears in the API Evangelist harvest backlog. While detailed public information is limited, the stub indicates the organization may be involved in coffee‑centric applications or services, potentially offering APIs for coffee ordering, barista assistance, or related data. Further investigation is required to confirm its product offerings, API endpoints, and documentation.
image: http://artly.coffee/cdn/shop/files/video-cover_75660956-d4de-4d1c-8c88-4e78d2c93db8.jpg?v=1682093979
layout: provider
modified: '2026-09-26'
name: Artlycoffee
nav: Providers
network: true
overview: Artlycoffee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coffee, Technology, and E-Commerce.
random_paper: 6
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Artlycoffee Domain Security
  slug: artlycoffee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: artlycoffee
tags:
- Company
- Coffee
- Technology
- E-Commerce
website: https://artly.coffee
---

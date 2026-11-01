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
- group: agent
  href: https://artifacts.apis.io/diginn/llms/diginn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/diginn-llms.txt
- group: other
  href: https://artifacts.apis.io/diginn/hosts/diginn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diginn-hosts.yml
- group: other
  href: https://artifacts.apis.io/diginn/vendors/diginn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/diginn-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.diginn.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.diginn.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.diginn.com/account/signin/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/diginn
- group: auth
  href: https://artifacts.apis.io/diginn/security/diginn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diginn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.diginn.com
coverage:
  checked: '2026-10-23'
  detail: Diginn is a fast‑casual restaurant brand with no public API surface.
  evidence:
  - status: 200
    url: https://www.diginn.com
  reason: not-a-software-company
  state: none
created: '2026-10-23'
description: DIG (Diginn) is a fast‑casual restaurant brand offering healthy bowls, vegetables, and comfort food. It provides delivery, pickup, and catering services through its locations. The company’s website presents its menu, locations, and ordering options, but no public API documentation or developer portal is evident.
image: https://storyblok.pleinaircdn.com/f/274373/1324x1324/8ffe601b0a/dig-inn-default-meta-image.png
layout: provider
modified: '2026-10-23'
name: Diginn
nav: Providers
network: true
overview: Diginn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurant, Food, Delivery, and Catering.
random_paper: 9
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 5.3
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
  name: Diginn Domain Security
  slug: diginn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: diginn
tags:
- Company
- Restaurant
- Food
- Delivery
- Catering
website: https://www.diginn.com
---

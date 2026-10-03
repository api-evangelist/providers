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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: GraphQL API for Better Booch e‑commerce store
  name: Better Booch GraphQL API
  slug: better-booch-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/better-booch/refs/heads/main/llms/better-booch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/better-booch-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/better-booch/refs/heads/main/well-known/better-booch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/better-booch-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/better-booch/refs/heads/main/hosts/better-booch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/better-booch-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/better-booch/refs/heads/main/vendors/better-booch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/better-booch-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://betterbooch.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://betterbooch.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://betterbooch.com/pages/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/better-booch/refs/heads/main/security/better-booch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/better-booch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://betterbooch.com
created: '2026-09-28'
description: Better Booch is a premium small craft kombucha brand based in Los Angeles, CA. Their organic, canned kombucha is brewed with naturally-occurring probiotics, botanicals, herbs, and adaptogens, delivering a flavorful, health‑supporting beverage. Available at over 5,000 retailers nationwide, Better Booch emphasizes sustainability, quality ingredients, and innovative flavors, positioning itself as a leader in the craft kombucha market.
image: https://betterbooch.com/cdn/shop/files/Copy_of_BetterBooch_Logo_Stacked_Horizontal_Black_V1_532x266.png?v=1636060843
layout: provider
modified: '2026-09-28'
name: Better Booch
nav: Providers
network: true
overview: Better Booch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beverages, Kombucha, Health, and Organic.
random_paper: 4
score:
  band: emerging
  composite: 11.5
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
    developer_ergonomics: 0.0
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Better Booch Domain Security
  slug: better-booch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: better-booch
tags:
- Company
- Beverages
- Kombucha
- Health
- Organic
website: https://betterbooch.com
---

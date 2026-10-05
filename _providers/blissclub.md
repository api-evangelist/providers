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
api_count: 1
apis:
- description: GraphQL API for Blissclub providing query capabilities.
  name: Blissclub GraphQL API
  slug: blissclub-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blissclub/refs/heads/main/llms/blissclub-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blissclub-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blissclub/refs/heads/main/well-known/blissclub-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blissclub-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blissclub/refs/heads/main/hosts/blissclub-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blissclub-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blissclub/refs/heads/main/vendors/blissclub-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blissclub-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blissclub.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blissclub.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://blissclub.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blissclub/refs/heads/main/security/blissclub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blissclub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blissclub.com
created: '2026-09-29'
description: Blissclub is an Indian functional apparel brand engineering thoughtfully designed clothing for women and men. It focuses on comfort, performance, and movement, offering a range of activewear, everyday wear, and specialty collections. The company operates an online store with a strong emphasis on customer loyalty programs and sustainable materials.
image: http://blissclub.com/cdn/shop/files/Logo.jpg?v=1652856086&width=2048
layout: provider
modified: '2026-09-29'
name: Blissclub
nav: Providers
network: true
overview: Blissclub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apparel, E-Commerce, Fashion, Activewear, and Indian.
random_paper: 17
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 6
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blissclub Domain Security
  slug: blissclub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blissclub
tags:
- Apparel
- E-Commerce
- Fashion
- Activewear
- Indian
website: https://blissclub.com
---

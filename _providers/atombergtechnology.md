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
- description: Developer portal for Atomberg's smart home appliance APIs.
  name: Atomberg API
  slug: atomberg-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atombergtechnology/refs/heads/main/llms/atombergtechnology-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atombergtechnology-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atombergtechnology/refs/heads/main/well-known/atombergtechnology-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atombergtechnology-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atombergtechnology/refs/heads/main/hosts/atombergtechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atombergtechnology-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atombergtechnology/refs/heads/main/vendors/atombergtechnology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atombergtechnology-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://media-dev.atomberg.com/media/pdf/Atomberg-Code-of-Conduct.pdf?v=10
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.atomberg.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atombergtechnology/refs/heads/main/security/atombergtechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atombergtechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atomberg.com
- group: docs
  title: ''
  type: Documentation
  url: https://atomberg.com/pages/about-us
- group: operate
  title: ''
  type: Support
  url: https://atomberg.com/pages/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atomberg.com/pages/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atomberg.com/pages/customer-policy
- group: company
  title: ''
  type: Blog
  url: https://atomberg.com/blogs/blog
coverage:
  checked: 2026-09-26
  detail: Only GraphQL endpoint discovered; no OpenAPI or other machine-readable contract found.
  evidence:
  - status: 0
    url: https://api.atomberg.com/openapi.json
  - status: 404
    url: https://dev.atomberg.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Atomberg is an Indian smart home appliance brand offering energy‑efficient ceiling fans, mixer grinders, water purifiers, juicers and smart locks. Founded with a focus on cutting‑edge technology and design, the company emphasizes low power consumption, durability and modern aesthetics for contemporary homes. Their product line integrates IoT features and aims to provide sustainable solutions for everyday living, serving customers across India and expanding globally.
image: http://atomberg.com/cdn/shop/files/Atomberg-logo_1.svg?v=1786346457
layout: provider
modified: '2026-09-26'
name: Atombergtechnology
nav: Providers
network: true
overview: 'Atombergtechnology publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Home, Appliances, India, and EnergyEfficient.


  Atombergtechnology''s developer surface includes documentation, support, engineering blog, and 10 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atombergtechnology Domain Security
  slug: atombergtechnology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atombergtechnology
tags:
- Company
- Smart Home
- Appliances
- India
- EnergyEfficient
website: https://atomberg.com
---

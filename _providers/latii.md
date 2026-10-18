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
- description: GraphQL API endpoint discovered at https://latii.com/api/graphql
  name: Latii API
  slug: latii-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/latii/refs/heads/main/llms/latii-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/latii-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/latii/refs/heads/main/well-known/latii-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/latii-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/latii/refs/heads/main/hosts/latii-hosts.yml
  title: ''
  type: Hosts
  url: hosts/latii-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/latii/refs/heads/main/vendors/latii-vendors.yml
  title: ''
  type: Vendors
  url: vendors/latii-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://latii.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/latii/refs/heads/main/security/latii-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/latii-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://latii.com/
- group: docs
  title: ''
  type: Documentation
  url: https://latii.com/pages/our-platform
- group: start
  title: ''
  type: GettingStarted
  url: https://latii.com/pages/request-a-demo
- group: company
  title: ''
  type: About
  url: https://latii.com/pages/about-us-1
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://latii.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://latii.com/policies/terms-of-service
created: '2026-10-12'
description: Latii is a SaaS platform that modernizes the window and door industry by providing an AI‑driven marketplace for architects, contractors, and manufacturers. The solution streamlines quoting, ordering, and project lifecycle management, reducing errors and accelerating installations. Latii offers a unified view of product specifications, pricing, and availability, enabling stakeholders to collaborate efficiently from design through installation. Backed by leadout‑capital, the company aims to become the single source of truth for the entire window‑door supply chain.
layout: provider
modified: '2026-10-12'
name: Latii
nav: Providers
network: true
overview: 'Latii is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Window-Doors, Marketplace, and Artificial Intelligence.


  Latii''s developer surface includes documentation, getting-started guide, and 10 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 71.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Latii Domain Security
  slug: latii-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: latii
tags:
- Company
- Software-as-a-Service
- Window-Doors
- Marketplace
- Artificial Intelligence
website: https://latii.com/
---

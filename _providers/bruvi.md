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
- description: Bruvi provides a coffee brewing and pod ordering API accessible via GraphQL.
  name: Bruvi API
  slug: bruvi-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bruvi/refs/heads/main/llms/bruvi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bruvi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bruvi/refs/heads/main/well-known/bruvi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bruvi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bruvi/refs/heads/main/hosts/bruvi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bruvi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bruvi/refs/heads/main/vendors/bruvi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bruvi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bruvi.com/policies/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.bruvi.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bruvi.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://bruvi.com/blogs/articles/tagged/press
- group: docs
  title: ''
  type: Documentation
  url: https://help.bruvi.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bruvi/refs/heads/main/security/bruvi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bruvi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bruvi.com/
created: '2026-10-06'
description: Bruvi is a Los Angeles‑based company offering a next‑generation single‑serve coffee system. It sells brewers, reusable B‑Pods and a mobile app that automates brewing, pod ordering and personalization. The brand emphasizes sustainability, premium craft coffee, and a subscription model for fresh pods delivered to customers.
image: https://cdn.shopify.com/s/files/1/0078/7582/1620/files/Cream-Brewer-New-Bundle-With-Filter.png?v=1745960737
layout: provider
modified: '2026-10-06'
name: Bruvi
nav: Providers
network: true
overview: 'Bruvi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coffee, Subscription, Sustainability, and E-Commerce.


  Bruvi''s developer surface includes support, documentation, and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.4
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
    developer_ergonomics: 14.3
    discoverability: 75.0
    operational_transparency: 0.0
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
  name: Bruvi Domain Security
  slug: bruvi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bruvi
tags:
- Company
- Coffee
- Subscription
- Sustainability
- E-Commerce
website: https://bruvi.com/
---

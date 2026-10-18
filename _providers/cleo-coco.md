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
- description: GraphQL API providing access to Cleo+Coco product and content data.
  name: Cleo+Coco GraphQL API
  slug: cleo-coco-graphql-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cleo-coco/refs/heads/main/conformance/cleo-coco-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cleo-coco-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cleo-coco/refs/heads/main/llms/cleo-coco-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cleo-coco-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cleo-coco/refs/heads/main/well-known/cleo-coco-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cleo-coco-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleo-coco/refs/heads/main/hosts/cleo-coco-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleo-coco-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleo-coco/refs/heads/main/vendors/cleo-coco-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleo-coco-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cleo-coco/refs/heads/main/security/cleo-coco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleo-coco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleoandcoco.com/
- group: company
  title: ''
  type: Blog
  url: https://cleoandcoco.com/blogs/news
- group: docs
  title: ''
  type: Documentation
  url: https://cleoandcoco.com/pages/our-story
- group: operate
  title: ''
  type: Support
  url: https://cleoandcoco.com/pages/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleoandcoco.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleoandcoco.com/policies/privacy-policy
created: '2026-10-08'
description: Cleo+Coco creates next-level clean, high-performance personal care products for every body. Their natural deodorants, body powders, dry hair shampoo, and functional sprays are aluminum‑free, synthetic‑fragrance‑free, and feature five odor‑fighting ingredients. The brand emphasizes safe, effective ingredients, real protection, and confidence, targeting consumers seeking clean, sustainable personal care solutions.
image: http://cleoandcoco.com/cdn/shop/files/C_C_Product-Deail_Balm_Basil-Mint_056fd0f2-b5d0-402b-87b2-d39ffb6d14ed.png?v=1747405081
layout: provider
modified: '2026-10-08'
name: Cleo+Coco
nav: Providers
network: true
overview: 'Cleo+Coco is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Deodorant, Personal Care, Body Powder, Functional Spray, and Clean Beauty.


  Cleo+Coco''s developer surface includes engineering blog, documentation, support, and 9 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cleo Coco Domain Security
  slug: cleo-coco-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cleo-coco
tags:
- Deodorant
- Personal Care
- Body Powder
- Functional Spray
- Clean Beauty
website: https://cleoandcoco.com/
---

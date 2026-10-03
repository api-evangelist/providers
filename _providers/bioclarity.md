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
- description: API for bioClarity services
  name: bioClarity API
  slug: bioclarity-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bioclarity/refs/heads/main/llms/bioclarity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bioclarity-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bioclarity/refs/heads/main/well-known/bioclarity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bioclarity-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bioclarity/refs/heads/main/hosts/bioclarity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bioclarity-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bioclarity/refs/heads/main/vendors/bioclarity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bioclarity-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bioclarity.com/policies/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.bioclarity.com/pages/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bioclarity.com/policies/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.bioclarity.com/account/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bioclarity/refs/heads/main/security/bioclarity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bioclarity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bioclarity.com
created: '2026-09-28'
description: bioClarity is a plant‑based, vegan skincare brand offering a range of cruelty‑free products designed to promote clear, glowing skin. Their catalog includes cleansers, moisturizers, masks, and targeted routines, all formulated with natural ingredients and free from harmful chemicals. The company emphasizes sustainability, ethical sourcing, and community engagement through educational content and a loyalty program.
image: http://www.bioclarity.com/cdn/shop/files/bioclarity_shareable_link_img.png?v=1644945104
layout: provider
modified: '2026-09-28'
name: bioClarity
nav: Providers
network: true
overview: 'bioClarity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Skincare, Vegan, Plant-Based, Beauty, and E-Commerce.


  bioClarity''s developer surface includes support and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 73.2
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
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bioclarity Domain Security
  slug: bioclarity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bioclarity
tags:
- Skincare
- Vegan
- Plant-Based
- Beauty
- E-Commerce
website: https://www.bioclarity.com
---

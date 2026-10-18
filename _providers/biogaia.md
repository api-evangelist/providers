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
- description: Biogaia provides probiotic products; their developer portal is not publicly documented.
  name: Biogaia API
  slug: biogaia-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/biogaia/refs/heads/main/llms/biogaia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/biogaia-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/biogaia/refs/heads/main/well-known/biogaia-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biogaia-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biogaia/refs/heads/main/hosts/biogaia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biogaia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biogaia/refs/heads/main/vendors/biogaia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biogaia-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.biogaia.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.biogaia.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.biogaia.com/blogs/news
- group: start
  title: ''
  type: Login
  url: https://www.biogaia.com/tools/recurring/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biogaia/refs/heads/main/security/biogaia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biogaia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biogaia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.biogaia.com/pages/science-and-research
created: '2026-10-12'
description: BioGaia is a Swedish healthcare company specializing in probiotic research and products. It develops clinically studied probiotic strains for infants, children, and adults, focusing on gut health, immunity, and oral health. The company operates globally, offering products through retail and healthcare professional channels, and provides scientific resources and information on its website.
image: http://www.biogaia.com/cdn/shop/files/BioGaia_1200_x_628.jpg?v=1757694133
layout: provider
modified: '2026-10-12'
name: BioGaia
nav: Providers
network: true
overview: 'BioGaia is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Probiotics, Healthcare, Sweden, GutHealth, and ConsumerProducts.


  BioGaia''s developer surface includes documentation and 10 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 15.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biogaia Domain Security
  slug: biogaia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biogaia
tags:
- Probiotics
- Healthcare
- Sweden
- GutHealth
- ConsumerProducts
website: https://www.biogaia.com/
---

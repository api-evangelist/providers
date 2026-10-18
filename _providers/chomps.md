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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chomps/refs/heads/main/well-known/chomps-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chomps-clarity-security.txt
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chomps/refs/heads/main/llms/chomps-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chomps-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chomps/refs/heads/main/well-known/chomps-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chomps-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chomps/refs/heads/main/hosts/chomps-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chomps-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chomps/refs/heads/main/vendors/chomps-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chomps-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chomps.com/pages/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.chomps.com/en-US
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chomps.com/pages/privacy-notice
- group: docs
  title: ''
  type: Documentation
  url: https://dev.chomps.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chomps/refs/heads/main/security/chomps-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chomps-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chomps/refs/heads/main/security/chomps-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chomps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chomps.com
created: '2026-10-08'
description: Chomps is a snack food company offering 100% grass‑fed beef jerky sticks and other paleo‑friendly, Whole30‑approved meat snacks. Founded to provide convenient, high‑protein, low‑carb snacks, Chomps sells a variety of beef, chicken, turkey, and venison jerky sticks through its online store and retail partners. The brand emphasizes sustainable sourcing and clean ingredients, catering to health‑conscious consumers seeking portable, flavorful protein options.
image: http://chomps.com/cdn/shop/files/chomps-logo-sharing.jpg?v=1789678049
layout: provider
modified: '2026-10-08'
name: Chomps
nav: Providers
network: true
overview: 'Chomps is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Snacks, Beef, and Paleo.


  Chomps'' developer surface includes support, documentation, and 11 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chomps Domain Security
  slug: chomps-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chomps Vulnerability Disclosure
  slug: chomps-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chomps
tags:
- Company
- Food
- Snacks
- Beef
- Paleo
website: https://chomps.com
---

---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/trustedparts/well-known/trustedparts-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trustedparts-well-known.yml
- group: other
  href: https://artifacts.apis.io/trustedparts/hosts/trustedparts-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trustedparts-hosts.yml
- group: other
  href: https://artifacts.apis.io/trustedparts/vendors/trustedparts-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trustedparts-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trustedparts
- group: auth
  href: https://artifacts.apis.io/trustedparts/security/trustedparts-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trustedparts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.trustedparts.com/
created: '2026-10-27'
description: TrustedParts is a provider of automotive parts and components, offering a catalog of products through an online platform. The company focuses on delivering high-quality, OEM‑grade parts to mechanics, repair shops, and end‑users. TrustedParts aims to simplify parts sourcing with searchable listings, detailed specifications, and integration possibilities for partners seeking to incorporate parts data into their own applications or services. While the public website currently presents a JavaScript‑protected front page, the organization’s core mission remains centered on reliable parts distribution and customer support.
layout: provider
modified: '2026-10-27'
name: TrustedParts
nav: Providers
network: true
overview: TrustedParts is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Parts, E-commerce, B2B, and SupplyChain.
random_paper: 13
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Trustedparts Domain Security
  slug: trustedparts-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trustedparts
tags:
- Automotive
- Parts
- E-commerce
- B2B
- SupplyChain
website: https://www.trustedparts.com/
---

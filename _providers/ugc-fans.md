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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/ugc-fans/plans/ugc-fans-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ugc-fans-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/ugc-fans/security/ugc-fans-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ugc-fans-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ugc-fans/well-known/ugc-fans-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ugc-fans-security.txt
- group: agent
  href: https://artifacts.apis.io/ugc-fans/well-known/ugc-fans-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ugc-fans-well-known.yml
- group: other
  href: https://artifacts.apis.io/ugc-fans/hosts/ugc-fans-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ugc-fans-hosts.yml
- group: other
  href: https://artifacts.apis.io/ugc-fans/vendors/ugc-fans-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ugc-fans-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ugc.fans/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://ugc.fans/support
- group: operate
  title: ''
  type: StatusPage
  url: https://ugc.fans/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ugc.fans/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://ugc.fans/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://ugc.fans/docs/mcp
- group: auth
  href: https://artifacts.apis.io/ugc-fans/security/ugc-fans-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ugc-fans-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ugc-fans/security/ugc-fans-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ugc-fans-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ugc.fans/
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://ugc.fans/docs/mcp
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: ugc-fans is a platform that enables creators and fans to connect through user‑generated content. It offers tools for content sharing, monetization, and community engagement. The service provides APIs for managing user profiles, media uploads, fan interactions, and payment processing, allowing developers to integrate UGC functionality into their applications.
image: https://ugc.fans/og.png
layout: provider
modified: '2026-10-30'
name: ugc-fans
nav: Providers
network: true
overview: 'ugc-fans is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, UGC, ContentPlatform, API, and Community.


  ugc-fans'' developer surface includes support, pricing, documentation, and 12 more developer resources.'
plans:
- name: Ugc Fans Plans Pricing
  plan_count: 5
  slug: ugc-fans-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ugc Fans Domain Security
  slug: ugc-fans-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ugc Fans Vulnerability Disclosure
  slug: ugc-fans-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ugc-fans
tags:
- Company
- UGC
- ContentPlatform
- API
- Community
website: https://ugc.fans/
---

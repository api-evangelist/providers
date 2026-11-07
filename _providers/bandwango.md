---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/bandwango/well-known/bandwango-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bandwango-help-security.txt
- group: agent
  href: https://artifacts.apis.io/bandwango/well-known/bandwango-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bandwango-well-known.yml
- group: other
  href: https://artifacts.apis.io/bandwango/hosts/bandwango-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bandwango-hosts.yml
- group: other
  href: https://artifacts.apis.io/bandwango/vendors/bandwango-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bandwango-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.bandwango.com/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bandwango
- group: auth
  href: https://artifacts.apis.io/bandwango/security/bandwango-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bandwango-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bandwango.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bandwango.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.bandwango.com/resource/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bandwango.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bandwango.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bandwango.com/legal/privacy
coverage:
  checked: '2026-09-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files were found on the provider's hosts.
  evidence:
  - status: dns_error
    url: https://api.bandwango.com/openapi.json
  - status: 404
    url: https://www.bandwango.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bandwango provides a mobile pass platform that enables destinations, tourism boards, and local businesses to engage visitors, track interactions, and generate economic impact. The solution offers customizable passes, QR code redemptions, analytics dashboards, and integration tools for event ticketing, visitor check‑ins, and marketing campaigns, serving over 500 clients across the United States.
image: https://cdn.prod.website-files.com/66578bb311ff6fff251290a9/66955a382b006365a5c79126_bw-og.webp
layout: provider
modified: '2026-09-27'
name: Bandwango
nav: Providers
network: true
overview: 'Bandwango is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include MobilePass, Tourism, Analytics, QR Codes, and Community.


  Bandwango''s developer surface includes support, documentation, engineering blog, getting-started guide, and 9 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 13.2
  previous_composite: 16.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bandwango/bandwango-2026-10-11T101518.png
security:
- kind: domain-security
  name: Bandwango Domain Security
  slug: bandwango-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bandwango
tags:
- MobilePass
- Tourism
- Analytics
- QR Codes
- Community
website: https://www.bandwango.com/
---

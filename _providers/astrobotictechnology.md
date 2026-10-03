---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astrobotictechnology/refs/heads/main/hosts/astrobotictechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astrobotictechnology-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/astrobotictechnology/refs/heads/main/vendors/astrobotictechnology-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astrobotictechnology-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astrobotic.com/lunar-delivery/send-to-the-moon/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astrobotic.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.astrobotic.com/plans-detailed-for-first-u-s-mission-to-land-on-moon-since-apollo/
- group: company
  title: ''
  type: Newsroom
  url: https://www.astrobotic.com/category/press/
- group: company
  title: ''
  type: Blog
  url: https://www.astrobotic.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.astrobotic.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/astrobotictechnology/refs/heads/main/security/astrobotictechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astrobotictechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.astrobotic.com
coverage:
  checked: '2026-09-26'
  detail: No OpenAPI or other machine‑readable contract was found on the developer portal.
  evidence:
  - status: 404
    url: https://dev.astrobotic.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Astrobotic Technology is a Pittsburgh‑based space robotics company that contracts payloads for lunar missions. It offers customers the ability to configure missions, reserve flight slots, and access technology for delivering payloads to the Moon. The firm provides services ranging from mission planning to hardware integration, aiming to enable scientific and commercial exploration of lunar space.
layout: provider
modified: '2026-09-26'
name: Astrobotictechnology
nav: Providers
network: true
overview: 'Astrobotictechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Space, Robotics, Lunar, Payload, and Technology.


  Astrobotictechnology''s developer surface includes pricing, engineering blog, documentation, and 7 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 46.4
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
  name: Astrobotictechnology Domain Security
  slug: astrobotictechnology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astrobotictechnology
tags:
- Space
- Robotics
- Lunar
- Payload
- Technology
- Company
website: https://www.astrobotic.com
---

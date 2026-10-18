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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pawscout/refs/heads/main/hosts/pawscout-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pawscout-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pawscout/refs/heads/main/vendors/pawscout-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pawscout-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pawscout/refs/heads/main/security/pawscout-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pawscout-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pawscout.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://pawscout.com/join/
- group: operate
  title: ''
  type: Support
  url: https://support.pawscout.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://pawscout.com/pawscout-pro/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pawscout.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pawscout.com/privacy-policy/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at api.pawscout.com endpoints.
  evidence:
  - status: 404
    url: https://api.pawscout.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Pawscout provides modern, affordable pet safety solutions, including a free mobile app and lightweight GPS-enabled tags for cats and dogs. Their mission is to build the world’s largest network for pet safety, well‑being, and fun, empowering owners to protect their pets and foster safer neighborhoods. The company offers a range of products, a community platform, and resources for lost‑pet recovery, supported by a growing user base and partnerships with shelters.
image: http://pawscout.com/img/og_image.jpg
layout: provider
modified: '2026-10-12'
name: Pawscout
nav: Providers
network: true
overview: 'Pawscout is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pet Safety, Mobile App, GPS Tags, and Community.


  Pawscout''s developer surface includes getting-started guide, support, pricing, and 6 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
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
  name: Pawscout Domain Security
  slug: pawscout-domain-security
  summary_line: TLSv1.3
slug: pawscout
tags:
- Company
- Pet Safety
- Mobile App
- GPS Tags
- Community
website: https://pawscout.com/
---

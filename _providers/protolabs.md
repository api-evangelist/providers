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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/protolabs/refs/heads/main/conformance/protolabs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/protolabs-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/protolabs/refs/heads/main/well-known/protolabs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/protolabs-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/protolabs/refs/heads/main/hosts/protolabs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/protolabs-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/protolabs/refs/heads/main/vendors/protolabs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/protolabs-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.protolabs.com/legal-notices/
- group: operate
  title: ''
  type: Support
  url: https://www.protolabs.com/help-center/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.protolabs.com/help-center/pricing-and-payment-options/
- group: company
  title: ''
  type: Newsroom
  url: https://www.protolabs.com/about-us/press/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.protolabs.com/resources/release-notes/
- group: company
  title: ''
  type: Blog
  url: https://www.protolabs.com/resources/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/protolabs/refs/heads/main/security/protolabs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/protolabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.protolabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.protolabs.com/resources
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.protolabs.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Protolabs provides rapid prototyping and on‑demand production services, offering digital manufacturing across injection molding, CNC machining, 3D printing, and sheet‑metal fabrication. Customers can upload CAD files, receive instant quotes, and order low‑volume production parts with fast lead times. The company serves engineers, product developers, and manufacturers worldwide, emphasizing quick turnaround, material variety, and automated manufacturing workflows.
image: https://www.protolabs.com/media/0dopqiik/home-meta.jpg
layout: provider
modified: '2026-10-12'
name: Protolabs
nav: Providers
network: true
overview: 'Protolabs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, RapidPrototyping, DigitalManufacturing, and Engineering.


  Protolabs'' developer surface includes support, pricing, changelog, engineering blog, documentation, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Protolabs Domain Security
  slug: protolabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: protolabs
tags:
- Company
- Manufacturing
- RapidPrototyping
- DigitalManufacturing
- Engineering
website: https://www.protolabs.com
---

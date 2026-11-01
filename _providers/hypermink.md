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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/hypermink/hosts/hypermink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hypermink-hosts.yml
- group: other
  href: https://artifacts.apis.io/hypermink/vendors/hypermink-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hypermink-vendors.yml
- group: auth
  href: https://artifacts.apis.io/hypermink/security/hypermink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hypermink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hypermink.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/HyperMink/inferenceable
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/HyperMink/inferenceable
- group: other
  title: ''
  type: ProductPage
  url: https://countermove.io
coverage:
  checked: '2026-10-18'
  detail: The homepage provides no machine‑readable API specification or documentation.
  evidence:
  - status: 200
    url: https://hypermink.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-17'
description: HyperMink builds accessible AI tools, offering a plug‑in USB device and open‑source inference server Inferenceable. Their mission is to demystify AI, ensuring privacy and ease of use for everyday individuals. Products include Countermove for email analysis and open‑source AI inference solutions.
image: https://hypermink.com/images/hypermink.png
layout: provider
modified: '2026-10-17'
name: HyperMink
nav: Providers
network: true
overview: 'HyperMink is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Accessibility, Privacy, and Open Source.


  HyperMink''s developer surface includes documentation and 6 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 7.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hypermink Domain Security
  slug: hypermink-domain-security
  summary_line: TLSv1.3
slug: hypermink
tags:
- Company
- Artificial Intelligence
- Accessibility
- Privacy
- Open Source
website: https://hypermink.com/
---

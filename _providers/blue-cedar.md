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
api_count: 1
apis:
- description: API for Blue Cedar mobile security platform
  name: Blue Cedar API
  slug: blue-cedar-api
artifact_total: 2
common:
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.bluecedar.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-cedar/refs/heads/main/hosts/blue-cedar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blue-cedar-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-cedar/refs/heads/main/vendors/blue-cedar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blue-cedar-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://apollo.bluecedar.com/platform/release-notes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blue-cedar/refs/heads/main/security/blue-cedar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blue-cedar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bluecedar.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bluecedar.com/sign-up
- group: operate
  title: ''
  type: Support
  url: https://www.bluecedar.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.bluecedar.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bluecedar.com/privacy-policy
coverage:
  checked: '2026-09-29'
  detail: The developer documentation pages return JavaScript-rendered shells, preventing machine‑readable contract discovery.
  evidence:
  - status: 404
    url: https://www.bluecedar.com/product-documentation
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: Blue Cedar provides intelligent mobile app security solutions, enabling enterprises to protect device integrity, prevent data loss, and safeguard intellectual property. Their platform offers self‑defending mobile applications, comprehensive security policies, and compliance tools for a mobile‑first universe.
image: https://www.bluecedar.com/hubfs/BC2020/blue_cedar_facebook_og_image.jpg
layout: provider
modified: '2026-09-29'
name: Blue Cedar
nav: Providers
network: true
overview: 'Blue Cedar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobile Security, Enterprise, App Protection, and Compliance.


  Blue Cedar''s developer surface includes documentation, changelog, getting-started guide, support, engineering blog, and 5 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blue Cedar Domain Security
  slug: blue-cedar-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blue-cedar
tags:
- Company
- Mobile Security
- Enterprise
- App Protection
- Compliance
website: https://www.bluecedar.com/
---

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
  href: https://raw.githubusercontent.com/api-evangelist/qasa/refs/heads/main/hosts/qasa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qasa-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qasa/refs/heads/main/vendors/qasa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qasa-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qasa/refs/heads/main/security/qasa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qasa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qasa.com/se/sv
- group: company
  title: ''
  type: Blog
  url: https://qasa.com/se/sv/blog
- group: operate
  title: ''
  type: Support
  url: https://support.qasa.se/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://qasa.com/se/sv/signup
- group: start
  title: ''
  type: Login
  url: https://qasa.com/se/sv/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qasa-public-production.s3.eu-west-1.amazonaws.com/Qasa.com_SV_Privacy%20Policy%20incl%20HomeQ%2C%202026-04-30-20260519T114340.pdf
coverage:
  checked: '2026-10-15'
  detail: No machine‑readable API specification was found on the provider's known hosts (e.g., https://api.qasa.com/openapi.json returned 404).
  evidence:
  - status: 404
    url: https://api.qasa.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Qasa is a Swedish digital platform that connects renters and landlords, simplifying the process of finding, listing, and managing rental properties. The service offers a searchable catalogue of over 25,000 homes across Sweden and other Nordic countries, tools for landlords to create listings, and features like premium services, tenant screening, and secure contract handling. Qasa aims to make renting transparent, efficient, and trustworthy for both tenants and property owners, leveraging technology to streamline communication and payments.
image: https://img.qasa.se/unsafe/600x300/https://qasa.s3.eu-west-1.amazonaws.com/uploads/qasa-og-share-image-wide.png
layout: provider
modified: '2026-10-15'
name: Qasa
nav: Providers
network: true
overview: 'Qasa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Rentals, Marketplace, and Sweden.


  Qasa''s developer surface includes engineering blog, support, signup flow, and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Qasa Domain Security
  slug: qasa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: qasa
tags:
- Company
- Real Estate
- Rentals
- Marketplace
- Sweden
website: https://qasa.com/se/sv
---

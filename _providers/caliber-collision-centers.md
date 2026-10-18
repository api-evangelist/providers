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
api_count: 1
apis:
- description: API documentation is presented on the Caliber developer portal, but the site is a JavaScript‑rendered single‑page app with no machine‑readable OpenAPI or other contract discovered.
  name: Caliber Collision API
  slug: caliber-collision-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caliber-collision-centers/refs/heads/main/security/caliber-collision-centers-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/caliber-collision-centers-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caliber-collision-centers/refs/heads/main/hosts/caliber-collision-centers-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caliber-collision-centers-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caliber-collision-centers/refs/heads/main/vendors/caliber-collision-centers-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caliber-collision-centers-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caliber-collision-centers/refs/heads/main/security/caliber-collision-centers-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/caliber-collision-centers-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caliber-collision-centers/refs/heads/main/security/caliber-collision-centers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caliber-collision-centers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.caliber.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.caliber.com/about-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.caliber.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.caliber.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.caliber.com/online-estimate
- group: operate
  title: ''
  type: Support
  url: https://www.caliber.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.caliber.com/newsroom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caliber.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caliber.com/privacy-policy
coverage:
  checked: '2026-10-06'
  detail: Developer portal at https://www.caliber.com/developers is a JavaScript‑rendered SPA with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://www.caliber.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Caliber Collision Centers provides automotive collision repair, auto glass replacement, and fleet services across a national network of locations. The company emphasizes trusted service, skilled technicians, and a purpose-driven approach to restoring customers’ vehicles and lives. It offers online estimates, appointment scheduling, and flexible payment options, serving both individual drivers and commercial fleets.
image: https://www.caliber.com/images-next/Caliber_1200x630.png
layout: provider
modified: '2026-10-06'
name: Caliber Collision Centers
nav: Providers
network: true
overview: 'Caliber Collision Centers is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Collision-Repair, Auto-Glass, and Fleet-Services.


  Caliber Collision Centers'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
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
  name: Caliber Collision Centers Domain Security
  slug: caliber-collision-centers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Caliber Collision Centers Vulnerability Disclosure
  slug: caliber-collision-centers-vulnerability-disclosure
  summary_line: no policy recorded
slug: caliber-collision-centers
tags:
- Company
- Automotive
- Collision-Repair
- Auto-Glass
- Fleet-Services
website: https://www.caliber.com/
---

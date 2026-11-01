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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/calibre-web/security/calibre-web-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calibre-web-domain-security.yml
- group: operate
  href: https://artifacts.apis.io/calibre-web/changelog/calibre-web-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/calibre-web-changelog.yml
- group: other
  href: https://artifacts.apis.io/calibre-web/hosts/calibre-web-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calibre-web-hosts.yml
- group: other
  href: https://artifacts.apis.io/calibre-web/vendors/calibre-web-vendors.yml
  title: ''
  type: Vendors
  url: vendors/calibre-web-vendors.yml
- group: build
  href: https://artifacts.apis.io/calibre-web/packages/calibre-web-packages.yml
  title: ''
  type: SDKs
  url: packages/calibre-web-packages.yml
- group: build
  href: https://artifacts.apis.io/calibre-web/packages/calibre-web-packages.yml
  title: ''
  type: Packages
  url: packages/calibre-web-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calibre-ebook.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://calibre-ebook.com/whats-new
- group: company
  title: ''
  type: Website
  url: https://calibre-ebook.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/janeczku/calibre-web/wiki
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/janeczku/calibre-web/wiki
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/janeczku/calibre-web#quick-start
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/h2VsJ2NEfB
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/janeczku/calibre-web
coverage:
  checked: '2026-10-28'
  detail: The provider's website https://calibre-ebook.com returns HTML with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://calibre-ebook.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Calibre-Web is an open-source web application that provides a clean, intuitive interface for browsing, reading, and downloading eBooks from a Calibre database. It supports user management, responsive design, Docker deployment, and integrates with various eBook formats, making it easy to self-host a personal digital library.
layout: provider
modified: '2026-10-28'
name: Calibre-Web
nav: Providers
network: true
overview: 'Calibre-Web is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Open-Source, eBook, Library, Web-App, and Python.


  Calibre-Web''s developer surface includes changelog, documentation, getting-started guide, support, and 10 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 44.6
    operational_transparency: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calibre Web Domain Security
  slug: calibre-web-domain-security
  summary_line: TLSv1.3 · DMARC
slug: calibre-web
tags:
- Open-Source
- eBook
- Library
- Web-App
- Python
website: https://calibre-ebook.com
---

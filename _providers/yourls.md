---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: YOURLS provides a simple HTTP API for creating, managing, and retrieving short URLs as documented in the developer guide.
  name: YOURLS API
  slug: yourls-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/yourls/authentication/yourls-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yourls-authentication.yml
- group: auth
  href: https://artifacts.apis.io/yourls/well-known/yourls-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yourls-security.txt
- group: agent
  href: https://artifacts.apis.io/yourls/well-known/yourls-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yourls-well-known.yml
- group: other
  href: https://artifacts.apis.io/yourls/hosts/yourls-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yourls-hosts.yml
- group: other
  href: https://artifacts.apis.io/yourls/vendors/yourls-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yourls-vendors.yml
- group: build
  href: https://artifacts.apis.io/yourls/packages/yourls-packages.yml
  title: ''
  type: SDKs
  url: packages/yourls-packages.yml
- group: build
  href: https://artifacts.apis.io/yourls/packages/yourls-packages.yml
  title: ''
  type: Packages
  url: packages/yourls-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://yourls.org/blog/tags/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/YOURLS/YOURLS/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://yourls.org/docs/category/getting-started
- group: auth
  href: https://artifacts.apis.io/yourls/security/yourls-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/yourls-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/yourls/security/yourls-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yourls-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yourls.org/
- group: docs
  title: ''
  type: Documentation
  url: https://yourls.org/docs
- group: company
  title: ''
  type: Blog
  url: https://yourls.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/YOURLS/YOURLS
- group: operate
  title: ''
  type: Support
  url: https://yourls.org/sponsor
- group: docs
  title: ''
  type: References
  url: https://yourls.org/hooklist.php
- group: docs
  title: ''
  type: References
  url: https://yourls.org/xref/
coverage:
  checked: '2026-10-28'
  detail: Documentation is provided as HTML pages without a downloadable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://yourls.org/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: YOURLS (Your Own URL Shortener) is an open‑source PHP application that lets you run your own URL shortening service on a self‑hosted server. It provides a simple web interface, API endpoints for creating, managing, and tracking short URLs, and supports plugins for extending functionality. The project is maintained by the community and offers documentation, a GitHub repository, and a public blog for updates and support.
image: https://yourls.org/assets/images/splash.png
layout: provider
modified: '2026-10-28'
name: YOURLS
nav: Providers
network: true
overview: 'YOURLS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, URL-Shortener, Open-Source, PHP, and Self-Hosted.


  YOURLS''s developer surface includes authentication, changelog, getting-started guide, documentation, engineering blog, support, and 13 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 31.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Yourls Authentication
  slug: yourls-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Yourls Domain Security
  slug: yourls-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Yourls Vulnerability Disclosure
  slug: yourls-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: yourls
tags:
- Company
- URL-Shortener
- Open-Source
- PHP
- Self-Hosted
website: https://yourls.org/
---

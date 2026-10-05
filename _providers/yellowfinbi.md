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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Public REST API exposing endpoints for reports, dashboards, stories, users and administration features.
  name: Yellowfin REST API
  slug: yellowfin-rest-api
artifact_total: 2
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/yellowfinbi/refs/heads/main/changelog/yellowfinbi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/yellowfinbi-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yellowfinbi/refs/heads/main/llms/yellowfinbi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yellowfinbi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yellowfinbi/refs/heads/main/well-known/yellowfinbi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yellowfinbi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yellowfinbi/refs/heads/main/hosts/yellowfinbi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yellowfinbi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yellowfinbi/refs/heads/main/vendors/yellowfinbi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yellowfinbi-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yellowfinbi/refs/heads/main/packages/yellowfinbi-packages.yml
  title: ''
  type: SDKs
  url: packages/yellowfinbi-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yellowfinbi/refs/heads/main/packages/yellowfinbi-packages.yml
  title: ''
  type: Packages
  url: packages/yellowfinbi-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.yellowfinbi.com/evaluation-guide/security
- group: operate
  title: ''
  type: Roadmap
  url: https://www.yellowfinbi.com/resources-tags/roadmap
- group: company
  title: ''
  type: Newsroom
  url: https://www.yellowfinbi.com/company/newsroom
- group: start
  title: ''
  type: Login
  url: https://community.yellowfinbi.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.yellowfinbi.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.yellowfinbi.com/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://www.yellowfinbi.com/suite/mobile-bi/setup/form
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/YellowfinBI
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yellowfinbi/refs/heads/main/security/yellowfinbi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yellowfinbi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.yellowfinbi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.yellowfinbi.com/space/yfcurrent/2200018/REST+API
- group: company
  title: ''
  type: Blog
  url: https://www.yellowfinbi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yellowfinbi.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.yellowfinbi.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yellowfinbi.com/privacy
coverage:
  checked: '2026-10-02'
  detail: The provider's documentation is markdown pages without a published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://wiki.yellowfinbi.com/space/yfcurrent/2200018/REST%20API
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Yellowfin provides an embedded analytics and business intelligence platform that enables organizations to create interactive dashboards, reports, and data stories. Its public REST API lets developers integrate content, manage users, and embed analytics into their own applications, supporting a range of data visualisation and storytelling capabilities.
image: https://www.yellowfinbi.com/assets/files/2024/06/cropped-YF-Digital-Badge-2024-FINAL-1.png
layout: provider
modified: '2026-10-02'
name: Yellowfin
nav: Providers
network: true
overview: 'Yellowfin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Business Intelligence, Embedded, and Data Visualization.


  Yellowfin''s developer surface includes changelog, getting-started guide, documentation, engineering blog, pricing, support, and 16 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 66.1
    operational_transparency: 36.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Yellowfinbi Domain Security
  slug: yellowfinbi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yellowfinbi
tags:
- Company
- Analytics
- Business Intelligence
- Embedded
- Data Visualization
website: https://www.yellowfinbi.com/
---

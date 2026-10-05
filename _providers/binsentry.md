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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for BinSentry platform providing feed inventory data and alerts.
  name: Binsentry API
  slug: binsentry-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/binsentry/refs/heads/main/hosts/binsentry-hosts.yml
  title: ''
  type: Hosts
  url: hosts/binsentry-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/binsentry/refs/heads/main/packages/binsentry-packages.yml
  title: ''
  type: SDKs
  url: packages/binsentry-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/binsentry/refs/heads/main/packages/binsentry-packages.yml
  title: ''
  type: Packages
  url: packages/binsentry-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.binsentry.com/resources/media
- group: other
  title: ''
  type: Leadership
  url: https://www.binsentry.com/company/leadership/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BinSentry
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/binsentry/refs/heads/main/security/binsentry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/binsentry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.binsentry.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.binsentry.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.binsentry.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://www.binsentry.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.binsentry.com/request-a-demo
coverage:
  checked: '2026-09-28'
  detail: Docs at https://docs.api.binsentry.com render via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.api.binsentry.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: BinSentry provides AI‑driven feed management solutions for animal feed and grain operations. Using computer‑vision sensors, it creates 3‑D images of bin contents, delivering real‑time inventory data, alerts, and analytics via a cloud dashboard. The platform helps producers, integrators, and feed mills reduce waste, improve safety, and optimize logistics across thousands of bins worldwide.
image: https://www.binsentry.com/media/fxthmrkh/og-logo.png
layout: provider
modified: '2026-09-28'
name: Binsentry
nav: Providers
network: true
overview: 'Binsentry publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Feed Management, Agriculture, and IoT.


  Binsentry''s developer surface includes documentation, engineering blog, support, signup flow, and 8 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 60.7
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Binsentry Domain Security
  slug: binsentry-domain-security
  summary_line: TLSv1.3 · DMARC
slug: binsentry
tags:
- Company
- Artificial Intelligence
- Feed Management
- Agriculture
- IoT
- Inventory
website: https://www.binsentry.com
---

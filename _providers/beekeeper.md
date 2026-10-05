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
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.4
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beekeeper/refs/heads/main/llms/beekeeper-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beekeeper-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beekeeper/refs/heads/main/well-known/beekeeper-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beekeeper-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beekeeper/refs/heads/main/hosts/beekeeper-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beekeeper-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beekeeper/refs/heads/main/vendors/beekeeper-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beekeeper-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/beekeeper/refs/heads/main/packages/beekeeper-packages.yml
  title: ''
  type: SDKs
  url: packages/beekeeper-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/beekeeper/refs/heads/main/packages/beekeeper-packages.yml
  title: ''
  type: Packages
  url: packages/beekeeper-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.lumapps.com/hc/en-us
- group: auth
  title: ''
  type: Security
  url: https://www.lumapps.com/platform/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.lumapps.com/insights/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lumapps.com/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.lumapps.com/insights/blog
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lumapps.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lumapps
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beekeeper/refs/heads/main/security/beekeeper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beekeeper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lumapps.com/beekeeper
coverage:
  checked: '2026-09-27'
  detail: Developer portal pages are HTML shells rendered by JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://developer.lumapps.com/index.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Beekeeper provides an employee communication platform that enables frontline teams to stay informed, collaborate, and access company resources via mobile and web apps. After being acquired by LumApps, Beekeeper continues as a product within the LumApps suite, offering features such as shift scheduling, real‑time messaging, and integration with enterprise tools. The platform serves retail, hospitality, and other frontline‑focused industries, helping organizations improve engagement and operational efficiency.
image: https://cdn.prod.website-files.com/694159454607d4764c350591/6a025ba1ef4d4ee97b17589a_en-lumapps-modern-employee-intranet.jpg
layout: provider
modified: '2026-09-27'
name: Beekeeper
nav: Providers
network: true
overview: 'Beekeeper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, Employee Engagement, Frontline, and Software-as-a-Service.


  Beekeeper''s developer surface includes support, engineering blog, documentation, and 12 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beekeeper Domain Security
  slug: beekeeper-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: beekeeper
tags:
- Company
- Communications
- Employee Engagement
- Frontline
- Software-as-a-Service
website: https://www.lumapps.com/beekeeper
---

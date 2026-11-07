---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for ShareLogic Unifi integration, documented on the ShareLogic Unifi docs site.
  name: ShareLogic Unifi API
  slug: sharelogic-unifi-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/sharelogic/changelog/sharelogic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sharelogic-changelog.yml
- group: agent
  href: https://artifacts.apis.io/sharelogic/llms/sharelogic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sharelogic-llms.txt
- group: auth
  href: https://artifacts.apis.io/sharelogic/well-known/sharelogic-sharelogic-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sharelogic-sharelogic-security.txt
- group: auth
  href: https://artifacts.apis.io/sharelogic/well-known/sharelogic-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sharelogic-api-security.txt
- group: agent
  href: https://artifacts.apis.io/sharelogic/well-known/sharelogic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sharelogic-well-known.yml
- group: other
  href: https://artifacts.apis.io/sharelogic/hosts/sharelogic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sharelogic-hosts.yml
- group: other
  href: https://artifacts.apis.io/sharelogic/vendors/sharelogic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sharelogic-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sharelogic.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.sharelogic.com/unifi/install/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sharelogic.com/unifi/2.2/release/setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sharelogic
- group: auth
  href: https://artifacts.apis.io/sharelogic/security/sharelogic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sharelogic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sharelogic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sharelogic.com/
coverage:
  checked: '2026-10-21'
  detail: Docs are served via GitBook with JavaScript rendering and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://docs.sharelogic.com/unifi/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: ShareLogic provides enterprise integration services on the ServiceNow platform, specializing in eBonding, process integrations, and ticket exchange. They help organizations connect disparate systems, automate workflows, and streamline data exchange across SaaS and on‑premise applications, delivering scalable solutions for digital transformation.
image: https://assets-global.website-files.com/5f7309b9b23271560fc996ba/653c3d03b1a6c52faacfda70_ShareLogic-open-graph.png
layout: provider
modified: '2026-10-21'
name: ShareLogic
nav: Providers
network: true
overview: 'ShareLogic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, ServiceNow, Enterprise, and Automation.


  ShareLogic''s developer surface includes changelog, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 55.4
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sharelogic/sharelogic-2026-11-03T143108.png
security:
- kind: domain-security
  name: Sharelogic Domain Security
  slug: sharelogic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sharelogic
tags:
- Integration
- ServiceNow
- Enterprise
- Automation
website: https://sharelogic.com/
---

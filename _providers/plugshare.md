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
  href: https://raw.githubusercontent.com/api-evangelist/plugshare/refs/heads/main/hosts/plugshare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plugshare-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/plugshare/refs/heads/main/vendors/plugshare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plugshare-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.plugshare.com/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://developer.plugshare.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PlugShare
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plugshare/refs/heads/main/security/plugshare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plugshare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plugshare.com
coverage:
  checked: '2026-10-14'
  detail: The main site https://www.plugshare.com returns only a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://www.plugshare.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: PlugShare provides the most comprehensive map of electric vehicle (EV) charging stations worldwide. Users can find, filter, and navigate to charging locations, read reviews, see photos, and get real-time availability where supported. The platform also offers an embed map, permalinking, and API access for developers to integrate charging data into apps, services, and navigation solutions. PlugShare supports community contributions, charging tips, and detailed station information, helping EV drivers plan trips and locate reliable charging infrastructure.
image: https://assets.plugshare.com/assets/plugshare-og.png
layout: provider
modified: '2026-10-14'
name: PlugShare
nav: Providers
network: true
overview: 'PlugShare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  PlugShare''s developer surface includes support, documentation, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 39.3
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Plugshare Domain Security
  slug: plugshare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: plugshare
tags:
- Company
website: https://www.plugshare.com
---

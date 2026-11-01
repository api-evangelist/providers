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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/tautulli/llms/tautulli-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tautulli-llms.txt
- group: agent
  href: https://artifacts.apis.io/tautulli/well-known/tautulli-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tautulli-well-known.yml
- group: other
  href: https://artifacts.apis.io/tautulli/hosts/tautulli-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tautulli-hosts.yml
- group: other
  href: https://artifacts.apis.io/tautulli/vendors/tautulli-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tautulli-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Tautulli/Tautulli/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tautulli.com/getting-started/installation
- group: auth
  href: https://artifacts.apis.io/tautulli/security/tautulli-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tautulli-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tautulli.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Tautulli/Tautulli/wiki
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/Tautulli/Tautulli/wiki/Tautulli-API-Reference
- group: operate
  title: ''
  type: Support
  url: https://tautulli.com/discord.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tautulli
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://docs.tautulli.com/extending-tautulli/api-reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Tautulli is an open‑source web application that monitors, analyzes and provides notifications for Plex Media Server activity. It offers real‑time monitoring, detailed statistics, history logs, graphs, and customizable alerts, helping users track what is being watched, by whom, and when. The tool runs alongside Plex, supporting multiple platforms via Python and includes a mobile remote app for on‑the‑go access.
image: https://tautulli.com/images/logo-circle.png
layout: provider
modified: '2026-10-28'
name: Tautulli
nav: Providers
network: true
overview: 'Tautulli is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, Plex, Open-Source, and Analytics.


  Tautulli''s developer surface includes changelog, getting-started guide, documentation, API reference, support, and 7 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 13.7
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
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tautulli Domain Security
  slug: tautulli-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tautulli
tags:
- Company
- Monitoring
- Plex
- Open-Source
- Analytics
website: https://tautulli.com/
---

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
overview: 'Tautulli is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Monitoring, Plex, Open Source, and Analytics.


  Tautulli''s developer surface includes changelog, getting-started guide, documentation, API reference, support, and 7 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tautulli/tautulli-2026-11-03T144327.png
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
- Open Source
- Analytics
website: https://tautulli.com/
---

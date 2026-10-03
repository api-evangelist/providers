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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Provides access to vetted research participants across emerging markets via a RESTful API.
  name: Besample API
  slug: besample-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/besample/refs/heads/main/llms/besample-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/besample-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/besample/refs/heads/main/hosts/besample-hosts.yml
  title: ''
  type: Hosts
  url: hosts/besample-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/besample/refs/heads/main/security/besample-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/besample-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://besample.app
- group: docs
  title: ''
  type: Documentation
  url: https://besample.app/resources
- group: company
  title: ''
  type: Blog
  url: https://blog.besample.app/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/besample/
coverage:
  checked: '2026-09-27'
  detail: Documentation pages are served as markdown but require JavaScript rendering to access full content, preventing machine-readable contract discovery.
  evidence:
  - status: 200
    url: https://besample.app/resources
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Besample provides access to vetted research participants across emerging markets, enabling behavioral scientists to conduct studies globally. The platform offers a searchable database of participants from Africa, Asia, Latin America, and Eastern Europe, with tools for recruitment, consent, and data collection, supporting academic and commercial research initiatives.
image: https://besample.app/og/home.png
layout: provider
modified: '2026-09-27'
name: Besample
nav: Providers
network: true
overview: 'Besample publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Research, Participants, Behavioral Science, and Data Platform.


  Besample''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Besample Domain Security
  slug: besample-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: besample
tags:
- Company
- Research
- Participants
- Behavioral Science
- Data Platform
website: https://besample.app
---

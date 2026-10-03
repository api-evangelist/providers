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
- description: API for Beeplus coworking space platform
  name: Beeplus API
  slug: beeplus-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beepluscoworkingspace/refs/heads/main/hosts/beepluscoworkingspace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beepluscoworkingspace-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beeplus.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beeplus.io/privacy
- group: company
  title: ''
  type: Blog
  url: https://blog.beeplus.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.beeplus.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beepluscoworkingspace/refs/heads/main/security/beepluscoworkingspace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beepluscoworkingspace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beeplus.io
coverage:
  checked: '2026-09-27'
  detail: Help documentation at https://help.beeplus.io/ loads HTML pages without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://help.beeplus.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Beeplus provides agile management solutions for service teams, offering a platform that integrates process mapping, training, and productivity tools to boost efficiency and client satisfaction. Founded in 2017, it serves companies seeking transformational agile practices across Brazil and beyond.
image: https://beeplus.io/blog/wp-content/uploads/2024/07/Frame-34214-700x488.png
layout: provider
modified: '2026-09-27'
name: Beepluscoworkingspace
nav: Providers
network: true
overview: 'Beepluscoworkingspace publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agile, Management, Software-as-a-Service, and Brazil.


  Beepluscoworkingspace''s developer surface includes engineering blog, documentation, and 5 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beepluscoworkingspace Domain Security
  slug: beepluscoworkingspace-domain-security
  summary_line: TLSv1.3 · DMARC
slug: beepluscoworkingspace
tags:
- Company
- Agile
- Management
- Software-as-a-Service
- Brazil
website: https://beeplus.io
---

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
  score: 15.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/placetel/conformance/placetel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/placetel-conformance.yml
- group: agent
  href: https://artifacts.apis.io/placetel/llms/placetel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/placetel-llms.txt
- group: agent
  href: https://artifacts.apis.io/placetel/well-known/placetel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/placetel-well-known.yml
- group: other
  href: https://artifacts.apis.io/placetel/hosts/placetel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/placetel-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.placetel.de/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.placetel.de
- group: start
  title: ''
  type: Login
  url: https://helpdesk.placetel.de/customer/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.placetel.de/developers
- group: company
  title: ''
  type: Blog
  url: https://www.placetel.de/blog
- group: docs
  title: ''
  type: APIReference
  url: https://api.placetel.de/v2/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Placetel
- group: auth
  href: https://artifacts.apis.io/placetel/security/placetel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/placetel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.placetel.de/
coverage:
  checked: '2026-10-26'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.placetel.de/produkt-integrationen
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Placetel provides cloud-based telephone systems for businesses, offering features such as virtual phone numbers, call routing, voicemail, conferencing, and integrations with CRM tools. Their platform enables companies to manage communications over the internet with scalable, reliable services, supporting both domestic and international calling.
image: https://res.cloudinary.com/cisco-placetel/images/c_lfill,h_628,w_1200/f_auto/ieczyeohmdpkv3qqofy0/plt-keyvisual-1
layout: provider
modified: '2026-10-26'
name: Placetel
nav: Providers
network: true
overview: 'Placetel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Call Center, Messaging, Video Meetings, and Collaboration.


  Placetel''s developer surface includes support, engineering blog, API reference, and 10 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 39.3
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Placetel Domain Security
  slug: placetel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: placetel
tags:
- Call Center
- Messaging
- Video Meetings
- Collaboration
website: https://www.placetel.de/
---

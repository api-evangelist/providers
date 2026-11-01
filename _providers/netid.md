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
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/netid/well-known/netid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/netid-well-known.yml
- group: other
  href: https://artifacts.apis.io/netid/hosts/netid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netid-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.netid.de/
- group: auth
  href: https://artifacts.apis.io/netid/security/netid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://netid.de/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.netid.de
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://broker.netid.de/privacycenter
coverage:
  checked: '2026-10-26'
  detail: Developer portal returns HTML pages for OpenAPI endpoints instead of machine‑readable JSON/YAML.
  evidence:
  - status: 200
    url: https://developer.netid.de/openapi.yaml
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: netID provides a unified login solution for German online services, allowing users to register once and access multiple partner platforms with a single set of credentials. The service emphasizes user control, privacy, and ease of use, offering a clear consent management system and a privacy center. It targets both consumers and businesses seeking streamlined authentication across various e‑commerce and digital offerings, positioning itself as a central identity hub in the German market.
layout: provider
modified: '2026-10-26'
name: netID
nav: Providers
network: true
overview: 'netID is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Authentication, Login, and German.


  netID''s developer surface includes documentation and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Netid Domain Security
  slug: netid-domain-security
  summary_line: TLSv1.3
slug: netid
tags:
- Company
- Identity
- Authentication
- Login
- German
website: https://netid.de/
---

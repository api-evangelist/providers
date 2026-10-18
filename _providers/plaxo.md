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
  href: https://raw.githubusercontent.com/api-evangelist/plaxo/refs/heads/main/hosts/plaxo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plaxo-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/plaxo/refs/heads/main/security/plaxo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plaxo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plaxo.com
coverage:
  checked: '2026-10-12'
  detail: No public developer program or API documentation was found for Plaxo; attempts to fetch OpenAPI specs from api.plaxo.com failed.
  evidence:
  - status: unreachable
    url: https://api.plaxo.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Plaxo was founded as a social networking service focused on address book synchronization and contact management. Over time, it evolved its platform to provide APIs for developers to integrate contact data, social features, and user profile management into applications. While the original consumer service has been discontinued, the company’s legacy API offerings remain of interest for historical and integration purposes. This profile aims to document the available technical resources, documentation, and contact points for the Plaxo API ecosystem.
layout: provider
modified: '2026-10-12'
name: Plaxo
nav: Providers
network: true
overview: Plaxo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contacts, Legacy, and Social.
random_paper: 20
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Plaxo Domain Security
  slug: plaxo-domain-security
  summary_line: DNSSEC
slug: plaxo
tags:
- Company
- Contacts
- Legacy
- Social
website: https://www.plaxo.com
---

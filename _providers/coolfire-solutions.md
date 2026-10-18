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
  href: https://raw.githubusercontent.com/api-evangelist/coolfire-solutions/refs/heads/main/hosts/coolfire-solutions-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coolfire-solutions-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coolfiresolutions.com/legal/terms-of-service/
- group: start
  title: ''
  type: SignUp
  url: https://coolfiresolutions.com/signup
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coolfire-solutions/refs/heads/main/security/coolfire-solutions-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coolfire-solutions-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coolfiresolutions.com
coverage:
  checked: '2026-10-11'
  detail: The API endpoint https://api.coolfiresolutions.com/openapi.json returns HTML instead of a machine‑readable OpenAPI document.
  evidence:
  - status: 200
    url: https://api.coolfiresolutions.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Coolfire Solutions provides flexible work management software designed to defeat operational chaos across industries such as logistics, telecommunications, energy, and government. Their flagship Coolfire Core platform enables teams to coordinate tasks, workflows, and communications, offering features for field service management, enterprise collaboration, and real-time situational awareness.
image: https://coolfiresolutions.com/wp-content/uploads/2023/10/Defeat-operational-chaos.png
layout: provider
modified: '2026-10-10'
name: Coolfire Solutions
nav: Providers
network: true
overview: 'Coolfire Solutions is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, WorkManagement, Collaboration, FieldService, and Logistics.


  Coolfire Solutions'' developer surface includes signup flow and 4 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coolfire Solutions Domain Security
  slug: coolfire-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coolfire-solutions
tags:
- Company
- WorkManagement
- Collaboration
- FieldService
- Logistics
website: https://coolfiresolutions.com
---

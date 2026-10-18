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
  href: https://raw.githubusercontent.com/api-evangelist/sagelink/refs/heads/main/hosts/sagelink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sagelink-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sagelink/refs/heads/main/vendors/sagelink-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sagelink-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sagelink/refs/heads/main/security/sagelink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sagelink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sage-link.com/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.sage-link.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: SageLink provides rig support and excavation services, originating from Unique Oilfield Technology Services (UNOTEC) and rebranded in 2008. It offers health and safety, equipment services, and consulting for trackhoe drilling operations, emphasizing safety, efficiency, and innovative sumpless drilling solutions.
layout: provider
modified: '2026-10-12'
name: SageLink
nav: Providers
network: true
overview: SageLink is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, RigSupport, Excavation, Safety, and Trackhoe.
random_paper: 10
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
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
  name: Sagelink Domain Security
  slug: sagelink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sagelink
tags:
- Company
- RigSupport
- Excavation
- Safety
- Trackhoe
website: https://sage-link.com/
---

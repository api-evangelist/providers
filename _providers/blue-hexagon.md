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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blue-hexagon/refs/heads/main/hosts/blue-hexagon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blue-hexagon-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blue-hexagon/refs/heads/main/security/blue-hexagon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blue-hexagon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluehexagon.ai/
coverage:
  checked: '2026-09-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the provider's hosts.
  evidence:
  - status: null
    url: https://api.bluehexagon.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: Blue Hexagon is a cybersecurity company that provides an agent‑less, cloud‑native AI security platform. Leveraging deep‑learning models, it offers real‑time threat detection, continuous compliance, and automated hardening across multi‑cloud workloads, networks, and storage. The solution is designed for enterprises seeking advanced threat defense without the overhead of traditional agents, delivering visibility and protection at runtime.
layout: provider
modified: '2026-09-29'
name: Blue Hexagon
nav: Providers
network: true
overview: Blue Hexagon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Artificial Intelligence, Cloud, Threat Detection, and Enterprise.
random_paper: 5
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 0
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blue Hexagon Domain Security
  slug: blue-hexagon-domain-security
  summary_line: DMARC
slug: blue-hexagon
tags:
- Cybersecurity
- Artificial Intelligence
- Cloud
- Threat Detection
- Enterprise
website: https://bluehexagon.ai/
---

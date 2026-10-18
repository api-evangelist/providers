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
  href: https://raw.githubusercontent.com/api-evangelist/agentorbit/refs/heads/main/hosts/agentorbit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentorbit-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentorbit/refs/heads/main/security/agentorbit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentorbit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentorbit.tech/
coverage:
  checked: '2026-10-15'
  detail: No API documentation or developer program is publicly available; the main domain is unreachable.
  evidence:
  - status: 404
    url: https://api.agentorbit.tech/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: AgentOrbit is a stub entry in the API Evangelist catalog, originally sourced from the G2 catalog. The company currently has no publicly reachable website; attempts to resolve https://agentorbit.tech/ and http://agentorbit.com result in domain‑for‑sale pages. As such, no API documentation, developer portal, or other resources are available at this time. This entry serves as a placeholder for future enrichment when the company establishes an online presence and publishes API specifications.
layout: provider
modified: '2026-10-15'
name: AgentOrbit
nav: Providers
network: true
overview: AgentOrbit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Automation, Integration, and Marketing.
random_paper: 15
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
  name: Agentorbit Domain Security
  slug: agentorbit-domain-security
  summary_line: no transport/DNS hardening detected
slug: agentorbit
tags:
- Company
- Software-as-a-Service
- Automation
- Integration
- Marketing
website: https://agentorbit.tech/
---

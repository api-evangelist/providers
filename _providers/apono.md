---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-04'
api_count: 5
apis:
- description: API reference for Apono's privileged access management platform.
  name: Apono API
  slug: apono-api
- baseURL: https://api.apono.io
  baseurl_source: declared
  description: The Api Reference API from Apono — 3 operation(s) for api reference.
  name: Apono Api Reference API
  slug: apono-api-reference-api
- baseURL: https://api.apono.io
  baseurl_source: declared
  description: The Apono API API from Apono — 1 operation(s) for apono api.
  name: Apono Apono API
  slug: apono-apono-api-api
- baseURL: https://api.apono.io
  baseurl_source: declared
  description: The Docs API from Apono — 2 operation(s) for docs.
  name: Apono Docs API
  slug: apono-docs-api
- baseURL: https://api.apono.io
  baseurl_source: declared
  description: The User API from Apono — 1 operation(s) for user.
  name: Apono User API
  slug: apono-user-api
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apono/refs/heads/main/security/apono-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apono-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.apono.io
coverage:
  checked: 2026-09-25
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the API host.
  evidence:
  - status: 404
    url: https://api.apono.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Apono provides a cloud‑native privileged access management (PAM) platform that delivers just‑in‑time, zero‑standing‑privilege access for humans, machines and AI agents. Now part of 1Password, Apono helps security, IAM and DevOps teams reduce risk by granting scoped permissions only when needed and automatically revoking them, while offering audit evidence for compliance.
layout: provider
modified: '2026-09-25'
name: Apono
nav: Providers
network: true
overview: Apono publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Api Reference API, Apono API, Docs API, and 2 more. Tagged areas include Company, Privileged Access Management, Cloud Security, Zero Standing Privilege, and AI Agents.
random_paper: 13
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 62.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Apono Domain Security
  slug: apono-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: apono
tags:
- Company
- Privileged Access Management
- Cloud Security
- Zero Standing Privilege
- AI Agents
- Identity Governance
website: https://www.apono.io
---

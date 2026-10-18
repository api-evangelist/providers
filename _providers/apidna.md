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
api_count: 1
apis:
- description: API endpoint discovered at api.apidna.ai, but no machine-readable contract was found.
  name: APIDNA API
  slug: apidna-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apidna/refs/heads/main/hosts/apidna-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apidna-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apidna.ai/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apidna.ai/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apidna/refs/heads/main/security/apidna-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apidna-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apidna.ai/
coverage:
  checked: '2026-10-15'
  detail: API host https://api.apidna.ai/ returned no OpenAPI, AsyncAPI, GraphQL, or other contract despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.apidna.ai/openapi.json
  - status: 0
    url: https://api.apidna.ai/openapi.yaml
  - status: 0
    url: https://api.apidna.ai/v1/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: APIDNA builds vertically‑trained agentic systems that automate complex workflows across enterprise systems. The platform offers AI agents that execute real‑world tasks, providing high reliability, security (ISO 20022, PSD2, GDPR, SOC 2 Type II), and auditability. It targets industries needing integration across APIs, ERPs, and databases, delivering fast deployment (under 48 hours), 99 % workflow accuracy, and 99.99 % uptime SLA. The company’s website showcases solutions, platform details, and a live agent execution canvas.
image: https://apidna.io/og-image.png
layout: provider
modified: '2026-10-15'
name: APIDNA
nav: Providers
network: true
overview: APIDNA is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Enterprise, Agents, and Integration.
random_paper: 5
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apidna Domain Security
  slug: apidna-domain-security
  summary_line: TLSv1.3 · HSTS
slug: apidna
tags:
- Artificial Intelligence
- Automation
- Enterprise
- Agents
- Integration
website: https://apidna.ai/
---

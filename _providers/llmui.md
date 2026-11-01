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
    error_semantics: documented
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
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: LLMUI Core provides REST endpoints for AI orchestration. See API documentation for details.
  name: LLMUI Core API
  slug: llmui-core-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/llmui/errors/llmui-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/llmui-problem-types.yml
- group: other
  href: https://artifacts.apis.io/llmui/hosts/llmui-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llmui-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GenAICos
- group: auth
  href: https://artifacts.apis.io/llmui/security/llmui-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llmui-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llmui.org/
coverage:
  checked: '2026-10-18'
  detail: OpenAPI spec at https://api.llmui.org/openapi.json is unrelated to LLMUI, and no machine‑readable contract is provided for the documented API.
  evidence:
  - status: 200
    url: https://api.llmui.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Nexios Technologies TF, operating under the brand LLMUI, provides an on‑premise AI multi‑LLM orchestration platform. Developed in Québec, it offers both an open‑source Core version (AGPLv3) and a proprietary Enterprise edition with advanced features like consensus pipelines, multi‑role agents, and enterprise security. The platform enables local, sovereign AI deployments, integrating tools such as Git connectors, Proxmox testing, and push notifications.
image: https://llmui.org/og-image.png
layout: provider
modified: '2026-10-18'
name: Nexios Technologies TF
nav: Providers
network: true
overview: Nexios Technologies TF is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Orchestration, Open Source, and Enterprise.
random_paper: 19
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Llmui Domain Security
  slug: llmui-domain-security
  summary_line: TLSv1.3 · DMARC
slug: llmui
tags:
- Company
- Artificial Intelligence
- Orchestration
- Open Source
- Enterprise
website: https://llmui.org/
---

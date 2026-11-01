---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Vectoree provides an OpenAI‑compatible backend API for AI coding agents.
  name: Vectoree API
  slug: vectoree-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/vectoree/authentication/vectoree-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vectoree-authentication.yml
- group: agent
  href: https://artifacts.apis.io/vectoree/llms/vectoree-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vectoree-llms.txt
- group: other
  href: https://artifacts.apis.io/vectoree/a2a/vectoree-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/vectoree-a2a.yml
- group: agent
  href: https://artifacts.apis.io/vectoree/well-known/vectoree-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vectoree-well-known.yml
- group: other
  href: https://artifacts.apis.io/vectoree/hosts/vectoree-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vectoree-hosts.yml
- group: other
  href: https://artifacts.apis.io/vectoree/vendors/vectoree-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vectoree-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://vectoree.ai/dashboard/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VectoreeAI
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.vectoree.ai/changelog
- group: auth
  href: https://artifacts.apis.io/vectoree/security/vectoree-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vectoree-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vectoree.ai
- group: docs
  title: ''
  type: Documentation
  url: https://vectoree.ai/SKILL.md
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vectoree.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vectoree.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vectoree.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://blog.vectoree.ai
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/SgbKCtqEgT
coverage:
  checked: '2026-10-20'
  detail: Documentation pages are rendered via Mintlify and do not expose a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 307
    url: https://docs.vectoree.ai/api-reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-20'
description: Vectoree is a backend-as-a-service platform designed for AI coding agents. It offers OpenAI‑compatible model access, authentication, managed Postgres databases, object storage, and a curated tool hub. Developers install a single CLI, obtain a project key, and interact via standard OpenAI SDKs, enabling rapid development, deployment, and scaling of agents with a simple pay‑as‑you‑go model.
image: https://vectoree.ai/og-home.png
layout: provider
modified: '2026-10-20'
name: Vectoree
nav: Providers
network: true
overview: 'Vectoree is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Backend-as-a-Service, OpenAI-Compatible, and Agents.


  Vectoree''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, support, and 10 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Vectoree Authentication
  slug: vectoree-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Vectoree Domain Security
  slug: vectoree-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vectoree
tags:
- Company
- AI
- Backend-as-a-Service
- OpenAI-Compatible
- Agents
website: https://vectoree.ai
---

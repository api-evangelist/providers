---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Gogs Agentic Access
  operation_count: 104
  slug: gogs-agentic-access
  summary_line: 104 operations · 52 acting
api_count: 1
apis:
- description: RESTful API for interacting with Gogs instances, similar to GitHub REST API v3.
  name: Gogs API
  slug: gogs-api
- baseURL: https://gogs.example.com/api/v1
  baseurl_source: spec
  description: Site administration endpoints (requires admin privileges)
  name: Gogs Administration API
  slug: gogs-administration-api
- baseURL: https://gogs.example.com/api/v1
  baseurl_source: spec
  description: Manage repository collaborators and deploy keys
  name: Gogs Collaborators and Deploy Keys API
  slug: gogs-collaborators-and-deploy-keys-api
- baseURL: https://gogs.example.com/api/v1
  baseurl_source: spec
  description: Manage issues, comments, labels, and milestones
  name: Gogs Issues API
  slug: gogs-issues-api
- baseURL: https://gogs.example.com/api/v1
  baseurl_source: spec
  description: Markdown rendering and Git data endpoints
  name: Gogs Miscellaneous API
  slug: gogs-miscellaneous-api
- baseURL: https://gogs.example.com/api/v1
  baseurl_source: spec
  description: Manage organizations, members, and teams
  name: Gogs Organizations API
  slug: gogs-organizations-api
- baseURL: https://gogs.example.com/api/v1
  baseurl_source: spec
  description: List repository releases
  name: Gogs Releases API
  slug: gogs-releases-api
- baseURL: https://gogs.example.com/api/v1
  baseurl_source: spec
  description: Create, search, and manage repositories, branches, commits, and contents
  name: Gogs Repositories API
  slug: gogs-repositories-api
- baseURL: https://gogs.example.com/api/v1
  baseurl_source: spec
  description: Search users, manage access tokens, emails, followers, and public keys
  name: Gogs Users API
  slug: gogs-users-api
- baseURL: https://gogs.example.com/api/v1
  baseurl_source: spec
  description: Create, edit, and delete repository webhooks
  name: Gogs Webhooks API
  slug: gogs-webhooks-api
artifact_total: 19
common:
- group: other
  href: https://artifacts.apis.io/gogs/capabilities/gogs-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gogs-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/gogs/agentic-access/gogs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gogs-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/gogs/rules/gogs-rules.yml
  title: ''
  type: Spectral
  url: rules/gogs-rules.yml
- group: design
  href: https://artifacts.apis.io/gogs/json-ld/gogs-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gogs-context.jsonld
- group: design
  href: https://artifacts.apis.io/gogs/vocabulary/gogs-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gogs-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gogs/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gogs/data-model/gogs-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gogs-data-model.yml
- group: design
  href: https://artifacts.apis.io/gogs/errors/gogs-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gogs-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gogs/conformance/gogs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gogs-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gogs/llms/gogs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gogs-llms.txt
- group: other
  href: https://artifacts.apis.io/gogs/a2a/gogs-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gogs-a2a.yml
- group: agent
  href: https://artifacts.apis.io/gogs/well-known/gogs-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gogs-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: https://gogs.io/advancing/webhooks
- group: auth
  href: https://artifacts.apis.io/gogs/authentication/gogs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gogs-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gogs/security/gogs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gogs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gogs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://gogs.io/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://gogs.io/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://gogs.io/getting-started/introduction
- group: operate
  title: ''
  type: Support
  url: https://gogs.io/advancing/authentication
coverage:
  checked: 2026-09-21
  detail: OpenAPI spec points to https://gogs.example.com/api/v1, a domain not owned by Gogs, so ownership cannot be verified.
  evidence:
  - status: 200
    url: https://gogs.io/api-reference/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-21'
description: Gogs is a painless self‑hosted Git service that lets you run your own Git server with a simple, lightweight web UI. It supports repository creation, issue tracking, pull requests, webhooks, and integrates with LDAP and OAuth providers. Gogs is written in Go, easy to install on Linux, macOS, and Windows, and is suitable for teams that need a fast, low‑maintenance version‑control platform they can host themselves.
image: https://unknwon.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DGetting%2Bstarted%26title%3DIntroduction%26description%3DThe%2Bpainless%2Bway%2Bto%2Bhost%2Byour%2Bown%2BGit%2Bservice%26theme%3Dae1e6af0f2409a2f7f17f292&w=1200&q=100
jsonld:
- class_count: 22
  name: Gogs Context
  property_count: 75
  slug: gogs-context
layout: provider
modified: '2026-09-21'
name: Gogs
nav: Providers
network: true
overview: 'Gogs publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Administration API, Collaborators and Deploy Keys API, Issues API, and 7 more. Tagged areas include Company, Version Control, Self-Hosted, Open Source, and Go.


  The Gogs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gogs'' developer surface includes authentication, documentation, API reference, getting-started guide, support, and 15 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Gogs API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: gogs-rules
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 54.8
    developer_ergonomics: 30.4
    discoverability: 64.3
    operational_transparency: 3.9
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 9
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/gogs/gogs-2026-10-11T104945.png
security:
- kind: authentication
  name: Gogs Authentication
  slug: gogs-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Gogs Domain Security
  slug: gogs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 4
skills:
- name: gogs-create-and-list-orgs
  slug: gogs-create-and-list-orgs
- name: gogs-create-issue-with-labels
  slug: gogs-create-issue-with-labels
- name: gogs-manage-follow
  slug: gogs-manage-follow
- name: gogs-webhooks-setup
  slug: gogs-webhooks-setup
slug: gogs
tags:
- Company
- Version Control
- Self-Hosted
- Open Source
- Go
- A2A
website: https://gogs.io/
---

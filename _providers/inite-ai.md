---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 66
  human_in_the_loop: 4
  name: Inite Ai Agentic Access
  operation_count: 141
  slug: inite-ai-agentic-access
  summary_line: 141 operations · 66 acting · 4 human-in-the-loop
api_count: 2
apis:
- baseURL: https://inite.ai
  baseurl_source: declared
  description: The agent API from inite-ai — 3 operation(s) for agent.
  name: inite-ai Agent API
  slug: inite-ai-agent-api
- baseURL: https://inite.ai
  baseurl_source: declared
  description: The atlas API from inite-ai — 4 operation(s) for atlas.
  name: inite-ai Atlas API
  slug: inite-ai-atlas-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Belief-level reads over the semantic_belief substrate: what the brain currently holds about a free-text (subject, field) key, with its supersede chain and inline scene provenance. Read-only — the scen'
  name: inite-ai Beliefs API
  slug: inite-ai-beliefs-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'The document pipeline: Source → Indexer → Candidates → Brain. Dark behind DOCUMENT_INGEST_ENABLED (default off).'
  name: inite-ai Documents API
  slug: inite-ai-documents-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Tenant-level pack management: install, list, eval, uninstall (scope `brain:admin`).'
  name: inite-ai Domain Packs API
  slug: inite-ai-domain-packs-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'The entity read surface (scope `brain:read`): typeahead, profile, bitemporal timeline and typed connections. The GDPR cascade on the same controller is an operator action and lives on the admin surfac'
  name: inite-ai Entities API
  slug: inite-ai-entities-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'The raw-substrate driver: verbatim pre-extraction dialogue turns (L0) as a contract — keyset reads, NDJSON export, and signed new-episode webhooks — so any consumer can build its own projection withou'
  name: inite-ai Episodes API
  slug: inite-ai-episodes-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'The multimodal evidence substrate, both directions. IN: the metadata-only ingest surface — register asset headers + citation-target fragments (originUri required, storageRef rejected, no bytes — the M'
  name: inite-ai Evidence API
  slug: inite-ai-evidence-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Fact-level reads: one fact by id and its grounding episodes — provenance-first memory ("show me why I remember this"). Flag: FACTS_API_ENABLED (off → 404); fact retraction stays flag-independent.'
  name: inite-ai Facts API
  slug: inite-ai-facts-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: Read-only operator view (scope `brain:admin`) over the tenant’s installed indexers and their run health. Dark behind INDEXER_OPERATOR_VIEW_ENABLED (default off).
  name: inite-ai Indexer operations API
  slug: inite-ai-indexer-operations-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'The external-indexer protocol (scope `indexer:write`): poll → claim → read content → submit candidates / fail. See docs/indexer-protocol.md.'
  name: inite-ai Indexer work API
  slug: inite-ai-indexer-work-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Writing memory: the declared-fact path (scope `brain:write`). Every write goes through bitemporal conflict resolution, so the response reports a decision, not an acknowledgement.'
  name: inite-ai Ingest API
  slug: inite-ai-ingest-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Self-serve credentials: issue, list and revoke API keys brain verifies itself. Bounded by the calling credential — a key is never wider than its issuer — and available identically on the hosted servic'
  name: inite-ai Keys API
  slug: inite-ai-keys-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Featured curation (scope `registry:curate`), pack pricing + publisher profiles (scope `registry:publish`) and the paid-pack checkout (scope `brain:admin`). State is instance-local — never part of the '
  name: inite-ai Marketplace API
  slug: inite-ai-marketplace-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: File-shaped memory — the storage behind Anthropic’s memory tool (`memory_20250818`). A model’s own notes, kept in the tenant’s database behind the same fences as every other memory rather than in a di
  name: inite-ai Memory files API
  slug: inite-ai-memory-files-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Derived surfaces as first-class records: lifecycle status, watermark, builder identity, and rebuild as the public verb. Flag: PROJECTIONS_API_ENABLED (off → 404).'
  name: inite-ai Projections API
  slug: inite-ai-projections-api
- baseURL: https://inite.ai
  baseurl_source: declared
  description: The public API from inite-ai — 2 operation(s) for public.
  name: inite-ai Public API
  slug: inite-ai-public-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: Discovery reads over the global Domain Pack registry (shared across all tenants).
  name: inite-ai Registry API
  slug: inite-ai-registry-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: Publisher-facing writes to the global registry (scope `registry:publish`).
  name: inite-ai Registry publishing API
  slug: inite-ai-registry-publishing-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Scene-level reads over the memory_episode substrate: coherent multi-turn groupings of raw turns — what happened, together, when — with their member episodes, backlinks, state deltas and memory value. '
  name: inite-ai Scenes API
  slug: inite-ai-scenes-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Reading memory (scope `brain:read`): hybrid search, chained multi-hop search, and cited synthesis over the same retrieval stack. All three share the per-credential `expensive` throttle bucket (10 req/'
  name: inite-ai Search API
  slug: inite-ai-search-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Where brain READS raw evidence from (scope `brain:admin`): connections that instantiate a pack’s declared `sources` entry, the per-connection catalogue of external items, and the sync engine. Flag: `S'
  name: inite-ai Source Plane API
  slug: inite-ai-source-plane-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Read-only trust inputs (scope `brain:read`): declared source identity ⋈ learned reputation. Public projection — operator annotations (owner/note) stay on the admin surface.'
  name: inite-ai Sources API
  slug: inite-ai-sources-api
- baseURL: https://brain.inite.ai
  baseurl_source: declared
  description: 'Per-user surfaces: the rolling user profile assembled from user-scoped memory. Flag: USER_PROFILE_API_ENABLED (off → 404).'
  name: inite-ai Users API
  slug: inite-ai-users-api
artifact_total: 42
asyncapis:
- description: ''
  name: Inite Ai Webhooks
  slug: inite-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/inite-ai/agentic-access/inite-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/inite-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/inite-ai/rules/inite-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/inite-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/inite-ai/json-ld/inite-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/inite-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/inite-ai/vocabulary/inite-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/inite-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/inite-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/inite-ai/asyncapi/inite-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/inite-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/inite-ai/data-model/inite-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/inite-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/inite-ai/errors/inite-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/inite-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/inite-ai/conformance/inite-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inite-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/inite-ai/llms/inite-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inite-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/inite-ai/a2a/inite-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/inite-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/inite-ai/mcp/inite-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/inite-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/inite-ai/well-known/inite-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/inite-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/inite-ai/well-known/inite-ai-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/inite-ai-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/inite-ai/well-known/inite-ai-blog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/inite-ai-blog-security.txt
- group: auth
  href: https://artifacts.apis.io/inite-ai/well-known/inite-ai-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/inite-ai-app-security.txt
- group: auth
  href: https://artifacts.apis.io/inite-ai/well-known/inite-ai-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/inite-ai-api-security.txt
- group: agent
  href: https://artifacts.apis.io/inite-ai/well-known/inite-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/inite-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/inite-ai/hosts/inite-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inite-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/inite-ai/vendors/inite-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inite-ai-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://inite.ai/en/news
- group: auth
  href: https://artifacts.apis.io/inite-ai/authentication/inite-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inite-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/inite-ai/security/inite-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/inite-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/inite-ai/security/inite-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inite-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inite.ai/
- group: company
  title: ''
  type: Blog
  url: https://blog.inite.ai/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.inite.ai/en
- group: docs
  title: ''
  type: Documentation
  url: https://dev.inite.ai/en
- group: docs
  title: ''
  type: APIReference
  url: https://dev.inite.ai/en
- group: commercial
  title: ''
  type: Pricing
  url: https://inite.ai/en/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inite.ai/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inite.ai/en/terms
- group: operate
  title: ''
  type: Support
  url: https://inite.ai/en/atlas/category/support
- group: auth
  title: ''
  type: Security
  url: https://inite.ai/en/atlas/category/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inite-ai
- group: start
  title: ''
  type: Login
  url: https://app.inite.ai/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://inite.ai/.well-known/openapi.json
  - status: null
    url: https://inite.ai/api/mcp
  - status: null
    url: https://api.inite.ai/.well-known/openapi.json
  - status: null
    url: https://app.inite.ai/.well-known/openapi.json
  - status: 401
    url: https://billing.inite.ai/mcp
  - status: 200
    url: https://inite.ai/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: INITE provides AI automation platform for mid‑size companies (10‑200 employees) to design, implement, and monitor AI‑driven workflows. It deploys 1‑3 AI workflows in 2‑4 weeks, then hands them to your team, offering a 15‑minute self‑check to model ROI before building. The service helps businesses turn chaos into profit with rapid AI integration and measurable outcomes.
image: https://inite.ai/api/og?locale=en&title=Turn+chaos+into+profit+with+AI+automation&subtitle=Diagnostic+%E2%86%92+ROI+plan+%E2%86%92+implementation+in+2-4+weeks.&kicker=INITE+%2F+PROTOCOL&mode=brand
jsonld:
- class_count: 120
  name: Inite Ai Context
  property_count: 342
  slug: inite-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at inite.ai.
  name: inite-ai MCP Server
  slug: inite-ai-mcp-yml
modified: '2026-10-29'
name: inite-ai
nav: Providers
network: true
overview: 'inite-ai publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Atlas API, Beliefs API, and 21 more. Tagged areas include Company, AI, Automation, SaaS, and Workflow.


  The inite-ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  inite-ai''s developer surface includes authentication, engineering blog, documentation, API reference, pricing, support, and 30 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: inite-ai API Rules
  rule_count: 18
  severity_counts:
    error: 12
    hint: 0
    info: 3
    warn: 3
  slug: inite-ai-rules
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 65.2
    developer_ergonomics: 51.7
    discoverability: 66.7
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Inite Ai Authentication
  slug: inite-ai-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Inite Ai Domain Security
  slug: inite-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Inite Ai Vulnerability Disclosure
  slug: inite-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 10
skills:
- name: call-a2a
  slug: call-a2a
- name: call-mcp-rail
  slug: call-mcp-rail
- name: call-mcp
  slug: call-mcp
- name: call-a2a
  slug: callA2a
- name: compare-verified-plans
  slug: compare-verified-plans
- name: get-atlas-tool
  slug: get-atlas-tool
- name: get-company-data
  slug: get-company-data
- name: get-live-dataset
  slug: get-live-dataset
- name: get-visibility-badge
  slug: get-visibility-badge
- name: search-atlas
  slug: search-atlas
slug: inite-ai
tags:
- Company
- AI
- Automation
- SaaS
- Workflow
- Mid-size
website: https://inite.ai/
---

---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Jentic Agentic Access
  operation_count: 4
  slug: jentic-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 2
apis:
- description: The Jentic Remote MCP Server is the hosted Model Context Protocol endpoint that exposes the Jentic catalog to MCP-capable clients (Claude Desktop, ChatGPT, Cursor, Windsurf, VS Code). It speaks the sa
  name: Jentic Remote MCP Server
  slug: jentic-mcp
- description: Open-source Python engine that executes Arazzo workflow specifications alongside OpenAPI operation definitions. Powers the Jentic platform's workflow execution and is also installable standalone as ar
  name: Arazzo Engine
  slug: arazzo-engine
- description: 'Open-source composable reasoning agent framework that plans, acts, and recovers from failures, preconfigured with Jentic tools and a ReWOO reasoning loop. Primary entry point is the ReWOOAgent Python '
  name: Jentic Standard Agent
  slug: standard-agent
- description: 'Free, open-source, self-hosted API execution layer that sits between an agent and the outside world. The agent says what it wants to do and Jentic Mini handles the how: finding the right API, injectin'
  name: Jentic Mini
  slug: jentic-mini
- description: Technical specification for evaluating how interpretable, operable, and trustworthy an API is for AI systems and autonomous agents. Defines the signals, dimensions, scoring model, and normalization ru
  name: Jentic API AI-Readiness Framework (JAIRF)
  slug: jairf
- baseURL: https://api.jentic.com/api/v1
  baseurl_source: declared
  description: Registration and API key management for accessing the Jentic platform.
  name: Jentic Authentication API
  slug: jentic-authentication-api
- baseURL: https://api.jentic.com/api/v1
  baseurl_source: declared
  description: Load execution details and execute API operations or Arazzo workflows with managed authentication and credential injection.
  name: Jentic Execution API
  slug: jentic-execution-api
- baseURL: https://api.jentic.com/api/v1
  baseurl_source: declared
  description: Semantic search over the Jentic API and workflow catalog using natural language queries.
  name: Jentic Search API
  slug: jentic-search-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: 'Actor-agnostic, multi-item access-request surface (Core / Access bounded context). When an agent''s brokered call is rejected by a permission rule — or the agent needs access it doesn''t yet have — the '
  name: Jentic Access Requests API
  slug: jentic-access-requests-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Unified actor directory — a lightweight read-only view across all actor types (users, agents, service accounts). Returns ID-to-name mappings for UI cache hydration so dashboards can display friendly n
  name: Jentic Actors API
  slug: jentic-actors-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Dynamic agent registration (RFC 7591-style) — register a new agent client, poll registration status, update, or delete a registration.
  name: Jentic Agent Registration API
  slug: jentic-agent-registration-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Agent actors — autonomous principals that call the Broker. Covers the agent lifecycle (list, read, approve / deny, enable / disable, archive) and the toolkits bound to each agent.
  name: Jentic Agents API
  slug: jentic-agents-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Sub-resource of **APIs** (Registry bounded context). Enumerate the operations exposed by a registered API — either the live (`current_revision_id`) view or a specific revision. Complements `Search` (r
  name: Jentic API Operations API
  slug: jentic-api-operations-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Sub-resource of **APIs** (Registry bounded context). Download the underlying OpenAPI document for a registered API — either the live (`current_revision_id`) view or a specific revision. Supports `appl
  name: Jentic API Spec API
  slug: jentic-api-spec-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: The `Api` aggregate root — what APIs are registered for this deployment, addressable by the loose `(vendor, name, version)` tuple. Every successful import lands a new immutable `ApiRevision`; the `Api
  name: Jentic APIs API
  slug: jentic-apis-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Append-only administrative audit trail — who did what, when. Distinct from `Executions` (brokered upstream calls); this records control-plane mutations.
  name: Jentic Audit API
  slug: jentic-audit-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: 'The public API **catalog** — a registry-side browse/preview/import surface over the Jentic public-APIs GitHub manifest. Powers the Discover experience: list importable APIs (`GET /catalog`, keyset cur'
  name: Jentic Catalog API
  slug: jentic-catalog-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Runtime, DB-backed platform configuration. Lets an operator set, read, and list configuration that previously required hand-editing backend YAML and restarting the server — starting with credential pr
  name: Jentic Configuration API
  slug: jentic-configuration-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Part of the **Core / Access** bounded context — the authoritative record of "who can call what, with which secret". A `Credential` is the auth secret + header configuration the Broker injects on the w
  name: Jentic Credentials API
  slug: jentic-credentials-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Unauthenticated metadata discovery — the JWKS document and OAuth authorization server metadata under `/.well-known/*`.
  name: Jentic Discovery API
  slug: jentic-discovery-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Curated, severity-tagged event stream surfaced to dashboards and operators. Each event is either **informational** (no action required, e.g. `import.completed`) or **actionable** (requires operator fo
  name: Jentic Events API
  slug: jentic-events-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Append-only audit log of every Broker call (sync or async) — timing, status, trace IDs, and the upstream API reference (`vendor:name:version`). Bodies are not stored. Records are written by the Broker
  name: Jentic Executions API
  slug: jentic-executions-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Identity introspection for the calling principal (human, agent, or service account) — `GET /me` returns the resolved subject, scopes, and permissions behind the presented token.
  name: Jentic Identity API
  slug: jentic-identity-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Resolve a single registered operation to its full structural detail — parameters, response schema, security scheme, server URL. Heavier than `Lookup` (which is the Broker hot path) and separate from `
  name: Jentic Inspect API
  slug: jentic-inspect-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: In-flight async-job tracker for both Registry import jobs and Broker async-execution jobs — one uniform `Job` shape keyed by `kind`. Lifecycle only — type-specific result payloads (the imported revisi
  name: Jentic Jobs API
  slug: jentic-jobs-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: MCP (Model Context Protocol) transport reporting. The `jentic mcp` stdio server terminates all MCP protocol traffic locally; the control plane only sees plain HTTP. This tag covers the small reporting
  name: Jentic MCP API
  slug: jentic-mcp-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Dashboard-oriented aggregation endpoints — execution volume, success/failure ratios, and top operations over a bounded time window. Results are cached in-process (TTL ~120 s) so concurrent dashboard v
  name: Jentic Monitoring API
  slug: jentic-monitoring-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Free-form annotations attached to registry resources — an `Api`, an `ApiRevision`, a registered `operation_id`, an `ExecutionRecord`, or a `Credential`. Used to capture human or agent observations abo
  name: Jentic Notes API
  slug: jentic-notes-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: OAuth 2.0 / OIDC endpoints exposed by the platform authorization server — the authorize, token, introspection, revocation, and assertion-mint endpoints plus the redirect callback.
  name: Jentic OAuth API
  slug: jentic-oauth-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Admin-managed registry of third-party OAuth clients (confidential, secret-bearing). Registered clients integrate with Jentic One via the standard Authorization Code + PKCE flow. Admins can create, lis
  name: Jentic OAuth Clients API
  slug: jentic-oauth-clients-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: OpenAPI Overlay 1.0 (`https://spec.openapis.org/overlay/v1.0.0`) documents that correct an imported spec without rewriting it. Overlays capture wrong required fields, missing security schemes, undocum
  name: Jentic Overlays API
  slug: jentic-overlays-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Part of the **Admin / Audit** bounded context — the catalogue of grantable permission strings. Permissions are namespaced `resource:action` strings (`users:write`, `capabilities:execute`, `credentials
  name: Jentic Permissions API
  slug: jentic-permissions-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Machine principals for non-interactive integrations — lifecycle (create, list, read, approve / deny, enable / disable, archive) mirroring the agent surface.
  name: Jentic Service Accounts API
  slug: jentic-service-accounts-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Operational endpoints for service health and platform tooling. Not part of any bounded context — surfaced here so orchestrators and load balancers have a stable probe target.
  name: Jentic System API
  slug: jentic-system-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Sub-resource of **Toolkits** (Core / Access bounded context). A toolkit doesn't own credentials directly — it **binds** to credentials that already exist in `/credentials`. The binding is the link rec
  name: Jentic Toolkit Credentials API
  slug: jentic-toolkit-credentials-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Sub-resource of **Toolkits** (Core / Access bounded context). A toolkit can hold many API keys at once — different agents, machines, or environments typically each get their own. Each key record (`ck_
  name: Jentic Toolkit Keys API
  slug: jentic-toolkit-keys-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: Sub-resource of **Toolkits** (Core / Access bounded context). The fine-grained PBAC tier — per-`(toolkit, credential)` allow / deny / require-approval rules evaluated server-side. Rules use a priority
  name: Jentic Toolkit Permissions API
  slug: jentic-toolkit-permissions-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: 'Part of the **Core / Access** bounded context — a `Toolkit` is a scoped bundle of credentials and permissions issued to an agent or service. This tag covers **toolkit lifecycle**: list, create, read, '
  name: Jentic Toolkits API
  slug: jentic-toolkits-api
- baseURL: https://api.jentic.com/mcp
  baseurl_source: declared
  description: 'Part of the **Admin / Audit** bounded context — the human roster of the organisation. One organisation, many users; admin surfaces here cover create / list / read / update / delete plus the AIP-style '
  name: Jentic Users API
  slug: jentic-users-api
artifact_total: 68
collections:
- collection_type: postman
  name: Jentic Authentication API
  slug: postman-jentic-authentication-api
- collection_type: postman
  name: Jentic Authentication Execution API
  slug: postman-jentic-execution-api
- collection_type: postman
  name: Jentic Authentication Search API
  slug: postman-jentic-search-api
- collection_type: open
  name: Jentic Authentication API
  slug: open-jentic-authentication-api
- collection_type: open
  name: Jentic Authentication Execution API
  slug: open-jentic-execution-api
- collection_type: open
  name: Jentic Authentication Search API
  slug: open-jentic-search-api
- collection_type: open
  name: Jentic API
  slug: open-jentic
common:
- group: other
  href: https://artifacts.apis.io/jentic/capabilities/jentic-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/jentic-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/jentic/plans/jentic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jentic-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/jentic/rate-limits/jentic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jentic-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jentic/finops/jentic-finops.yml
  title: ''
  type: FinOps
  url: finops/jentic-finops.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/jentic/overview
- group: agent
  href: https://artifacts.apis.io/jentic/agentic-access/jentic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jentic-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/jentic/security/jentic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jentic-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/jentic/authentication/jentic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jentic-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://jentic.com/
- group: company
  title: ''
  type: Blog
  url: https://jentic.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jentic.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://jentic.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.jentic.com/sign-up
- group: start
  title: ''
  type: Console
  url: https://app.jentic.com/
- group: operate
  title: ''
  type: Contact
  url: https://jentic.com/contact
- group: company
  title: ''
  type: About
  url: https://jentic.com/company
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jentic
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jentic.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jentic.com/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jentic
- group: learn
  title: ''
  type: YouTube
  url: https://youtube.com/@JenticAI
- group: operate
  title: ''
  type: Support
  url: https://docs.jentic.com/community/support/
- group: operate
  title: ''
  type: FAQ
  url: https://docs.jentic.com/community/faq/
- group: auth
  title: ''
  type: Security
  url: https://docs.jentic.com/community/security/
- group: other
  title: ''
  type: Contributing
  url: https://docs.jentic.com/community/contributing/
- group: company
  title: ''
  type: Press
  url: https://jentic.com/blog/press
- group: company
  title: ''
  type: BlogFeed
  url: https://jentic.com/blog/feed.xml
- group: build
  title: ''
  type: PythonPackage
  url: https://pypi.org/project/jentic/
- group: build
  title: ''
  type: PythonPackage
  url: https://pypi.org/project/arazzo-runner/
- group: design
  href: https://artifacts.apis.io/jentic/vocabulary/jentic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jentic-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jentic/json-ld/jentic-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jentic-context.jsonld
- group: docs
  href: https://artifacts.apis.io/jentic/json-schema/jentic-operation-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/jentic-operation-schema.json
- group: docs
  href: https://artifacts.apis.io/jentic/json-schema/jentic-agent-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/jentic-agent-schema.json
- group: docs
  href: https://artifacts.apis.io/jentic/json-schema/jentic-workflow-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/jentic-workflow-schema.json
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/jentic/jentic-skills
created: '2026-01-02'
description: Jentic is an AI infrastructure company building the agentic knowledge layer for APIs. Founded in late 2024 and backed by $4.5M in pre-seed funding, Jentic enables enterprises to confidently manage, scale, and govern AI agent initiatives in a unified platform built on open standards. The platform provides secure execution, managed authentication, unified permissions, and observability for AI agents accessing 1,500+ public APIs and 2,000+ agent-ready workflows. Jentic's bet is that AI agents need a standards-based control plane built on OpenAPI plus Arazzo workflows plus MCP, rather than ad-hoc tool wiring inside every agent framework. The platform ships the Jentic Public APIs catalog, the Arazzo Engine (workflow runner), the Standard Agent (a composable ReWOO-style reasoning agent), the Jentic Mini self-hosted execution layer, a hosted Remote MCP server at api.jentic.com/mcp, and the Jentic API AI-Readiness Framework (JAIRF) for scoring API readiness for agents.
examples:
- key_count: 5
  name: Jentic Execute Example
  slug: jentic-execute-example
- key_count: 5
  name: Jentic Load Example
  slug: jentic-load-example
- key_count: 5
  name: Jentic Register Example
  slug: jentic-register-example
- key_count: 5
  name: Jentic Search Example
  slug: jentic-search-example
- key_count: 6
  name: Jentic Workflow Execute Example
  slug: jentic-workflow-execute-example
finops:
- has_sources: true
  method: derived
  name: Jentic Finops
  primary_unit: ''
  service_category: ''
  slug: jentic-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jentic.png
json_schemas:
- name: Jentic Agent
  property_count: 9
  slug: jentic-agent
- name: Jentic Operation
  property_count: 10
  slug: jentic-operation
- name: Jentic Workflow
  property_count: 10
  slug: jentic-workflow
json_structures:
- name: Jentic Operation Structure
  property_count: 0
  slug: jentic-operation-structure
jsonld:
- class_count: 0
  name: Jentic Context
  property_count: 6
  slug: jentic-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.jentic.com over HTTP; 4 tools listed.
  name: Jentic MCP Server
  slug: jentic
modified: '2026-05-19'
name: Jentic
nav: Providers
network: true
overview: 'Jentic publishes 39 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Execution API, Search API, and 36 more. Tagged areas include AI Agents, Arazzo, OpenAPI, MCP, and Workflows.


  The Jentic catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Jentic''s developer surface includes authentication, engineering blog, documentation, pricing, signup flow, developer console, YouTube channel, and 28 more developer resources.'
plans:
- name: Jentic Plans Pricing
  plan_count: 3
  slug: jentic-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Jentic Rate Limits
  slug: jentic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Jentic — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: jentic-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Jentic API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 5
  slug: jentic-rules
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.0
    catalog_earned_first_party: 12.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 76.3
    contract_governance: 27.3
    contract_quality: 67.8
    developer_ergonomics: 62.4
    discoverability: 61.7
    operational_transparency: 23.7
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 18.4
      derived: 0
      marker_coverage: 0.0
      total: 38
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/jentic/jentic-2026-06-20T183721.png
security:
- kind: authentication
  name: Jentic Authentication
  slug: jentic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Jentic Domain Security
  slug: jentic-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 3
skills:
- name: jentic-v1
  slug: jentic-v1
- name: jentic-workflows
  slug: jentic-workflows
- name: jentic
  slug: jentic
slug: jentic
tags:
- AI Agents
- Arazzo
- OpenAPI
- MCP
- Workflows
- Integration
- Agent Runtime
- Standard Agent
- Just In Time Tooling
- Credential Vault
- Agent Governance
- Observability
- API AI Readiness
website: https://jentic.com/
---

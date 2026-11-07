---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Globant Enterprise AI platform API. Twenty-six documented API groups — Access Control, Agents, Agentic Processes, Analytics, Assistant, Chat, Corpus, Corpus Semantic Similarity, Embeddings, Evalua
  name: Globant Enterprise AI (Glob.AI OS) API
  slug: globant-api
- baseURL: https://api.saia.ai
  baseurl_source: declared
  description: The Catalog API from Globant — 1 operation(s) for catalog.
  name: Globant Catalog API
  slug: globant-catalog-api
- baseURL: https://api.saia.ai
  baseurl_source: declared
  description: The Health API from Globant — 1 operation(s) for health.
  name: Globant Health API
  slug: globant-health-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/globant/finops/globant-finops.yml
  title: ''
  type: FinOps
  url: finops/globant-finops.yml
- group: other
  href: https://artifacts.apis.io/globant/overlays/globant-glob-ai-public-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/globant-glob-ai-public-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.globant.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.globant.ai/en/wiki?4458,Table+of+contents%3AGlob.AI+OS,
- group: docs
  title: ''
  type: APIReference
  url: https://docs.globant.ai/en/wiki?20,Glob.AI+OS+API+Reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.globant.ai/en/wiki?4623,Getting+started+with+Glob.AI+OS
- group: operate
  title: ''
  type: Support
  url: https://globant-services-noc.atlassian.net/helpcenter/GEAIS/user/login
- group: company
  title: ''
  type: Blog
  url: https://stayrelevant.globant.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://glob.ai/en/catalog
- group: start
  title: ''
  type: SignUp
  url: https://glob.ai/en/access/request
- group: start
  title: ''
  type: Login
  url: https://glob.ai/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://glob.ai/en/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://glob.ai/en/legal#privacy
- group: auth
  href: https://artifacts.apis.io/globant/authentication/globant-authentication.yml
  title: ''
  type: Authentication
  url: authentication/globant-authentication.yml
- group: design
  href: https://artifacts.apis.io/globant/conventions/globant-conventions.yml
  title: ''
  type: Conventions
  url: conventions/globant-conventions.yml
- group: design
  href: https://artifacts.apis.io/globant/conventions/globant-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/globant-conventions.yml
- group: design
  href: https://artifacts.apis.io/globant/errors/globant-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/globant-error-codes.yml
- group: design
  href: https://artifacts.apis.io/globant/lifecycle/globant-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/globant-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/globant/lifecycle/globant-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/globant-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/globant/changelog/globant-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/globant-changelog.yml
- group: design
  href: https://artifacts.apis.io/globant/conformance/globant-conformance.yml
  title: ''
  type: Conformance
  url: conformance/globant-conformance.yml
- group: auth
  href: https://artifacts.apis.io/globant/conformance/globant-conformance.yml
  title: ''
  type: Compliance
  url: conformance/globant-conformance.yml
- group: build
  href: https://artifacts.apis.io/globant/packages/globant-packages.yml
  title: ''
  type: Packages
  url: packages/globant-packages.yml
- group: build
  href: https://artifacts.apis.io/globant/packages/globant-packages.yml
  title: ''
  type: SDKs
  url: packages/globant-packages.yml
- group: build
  href: https://artifacts.apis.io/globant/cli/globant-cli.yml
  title: ''
  type: CLI
  url: cli/globant-cli.yml
- group: commercial
  href: https://artifacts.apis.io/globant/plans/globant-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/globant-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/globant/rate-limits/globant-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/globant-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/globant/data-model/globant-data-model.yml
  title: ''
  type: DataModel
  url: data-model/globant-data-model.yml
- group: agent
  href: https://artifacts.apis.io/globant/well-known/globant-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/globant-well-known.yml
- group: other
  href: https://artifacts.apis.io/globant/well-known/globant-glob-ai-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/globant-glob-ai-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/globant/llms/globant-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/globant-llms.txt
- group: agent
  href: https://artifacts.apis.io/globant/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/globant/mcp/globant-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/globant-mcp.yml
- group: auth
  href: https://artifacts.apis.io/globant/security/globant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/globant-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/globant
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/globant
- group: company
  title: ''
  type: Website
  url: https://www.globant.com
created: '2026-04-19'
description: Globant is a NYSE-listed digital and cognitive transformation company that, through two distinct platforms, publishes a genuinely agent-facing API surface. Globant Enterprise AI (Glob.AI OS) — the platform that began life as GeneXus' SAIA and was renamed after Globant acquired GeneXus — documents 26 API groups covering agents, agentic processes, RAG, corpora, tools, embeddings, guardrails and usage limits at api.saia.ai, with a Python SDK (PyGEAI), a geai CLI, a full numeric error registry and a dated one-year support window per release. Separately, Glob.AI, the AI-native delivery platform launched in August 2026, publishes an OpenAPI 3.1 description, an RFC 9727 api-catalog, an llms.txt, digest-pinned Agent Skills and an MCP server card at glob.ai. Globant also ships the CODA agentic coding CLI.
finops:
- has_sources: true
  method: derived
  name: Globant Finops
  primary_unit: ''
  service_category: ''
  slug: globant-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/globant.png
layout: provider
mcp_servers:
- description: Globant publishes an MCP server card at https://glob.ai/.well-known/mcp/server-card.json describing an MCP server named "orchestrator" that exposes the Glob.AI Hubs Orchestrator API — projects, goals,
  name: Glob.AI Hubs Orchestrator MCP Server
  slug: glob-ai-hubs-orchestrator-mcp-server
modified: '2026-09-14'
name: Globant
nav: Providers
network: true
overview: 'Globant publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog API, Health API, and 1 more. Tagged areas include Software, Digital Transformation, Artificial Intelligence, Agents, and MCP.


  The Globant catalog on APIs.io includes 1 Spectral governance ruleset.


  Globant''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Globant Plans Pricing
  plan_count: 0
  slug: globant-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Globant Rate Limits
  slug: globant-rate-limits
rules:
- authorship: generated
  effective_rule_count: 67
  extends:
  - spectral:oas
  name: Globant API Rules
  rule_count: 26
  severity_counts:
    error: 24
    hint: 0
    info: 1
    warn: 1
  slug: globant-rules
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 14.5
    contract_governance: 31.8
    contract_quality: 44.9
    developer_ergonomics: 78.6
    discoverability: 81.7
    operational_transparency: 26.3
  previous_composite: 44.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/globant/globant-2026-06-20T181931.png
security:
- kind: authentication
  name: Globant Authentication
  slug: globant-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Globant Domain Security
  slug: globant-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: globai-catalog
  slug: globant-globai-catalog
- name: orchestrator-mcp-setup
  slug: globant-orchestrator-mcp-setup
slug: globant
tags:
- Software
- Digital Transformation
- Artificial Intelligence
- Agents
- MCP
- Consulting
- Enterprise
website: https://www.globant.com
---

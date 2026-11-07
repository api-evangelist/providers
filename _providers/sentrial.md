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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.sentrial.com
  baseurl_source: declared
  description: Track events within agent sessions.
  name: Sentrial Events API
  slug: sentrial-events-api
- baseURL: https://api.sentrial.com
  baseurl_source: declared
  description: Create and manage agent sessions.
  name: Sentrial Sessions API
  slug: sentrial-sessions-api
artifact_total: 9
collections:
- collection_type: open
  name: Sentrial SDK Events API
  slug: open-sentrial-events-api
- collection_type: open
  name: Sentrial SDK Events Sessions API
  slug: open-sentrial-sessions-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.sentrial.com/
- group: auth
  href: https://artifacts.apis.io/sentrial/security/sentrial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sentrial-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sentrial/authentication/sentrial-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sentrial-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.sentrial.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.sentrial.com/docs/api/sessions
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sentrial.com/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.sentrial.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://sentrial.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sentrial.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sentrial.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sentrialdev
- group: build
  href: https://artifacts.apis.io/sentrial/packages/sentrial-packages.yml
  title: ''
  type: Packages
  url: packages/sentrial-packages.yml
- group: build
  href: https://artifacts.apis.io/sentrial/packages/sentrial-packages.yml
  title: ''
  type: SDKs
  url: packages/sentrial-packages.yml
- group: build
  href: https://artifacts.apis.io/sentrial/cli/sentrial-cli.yml
  title: ''
  type: CLI
  url: cli/sentrial-cli.yml
- group: design
  href: https://artifacts.apis.io/sentrial/conventions/sentrial-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sentrial-conventions.yml
- group: design
  href: https://artifacts.apis.io/sentrial/errors/sentrial-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/sentrial-error-codes.yml
- group: design
  href: https://artifacts.apis.io/sentrial/data-model/sentrial-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sentrial-data-model.yml
- group: design
  href: https://artifacts.apis.io/sentrial/conformance/sentrial-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sentrial-conformance.yml
- group: design
  href: https://artifacts.apis.io/sentrial/lifecycle/sentrial-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sentrial-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/sentrial/overlays/sentrial-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sentrial-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/sentrial/mcp/sentrial-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sentrial-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sentrial/llms/sentrial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sentrial-llms.txt
- group: agent
  href: https://artifacts.apis.io/sentrial/skills/sentrial-track-agent-session.md
  title: ''
  type: AgentSkill
  url: skills/sentrial-track-agent-session.md
- group: agent
  href: https://artifacts.apis.io/sentrial/skills/sentrial-record-tool-call.md
  title: ''
  type: AgentSkill
  url: skills/sentrial-record-tool-call.md
created: '2026-07-17'
description: Sentrial is an observability platform for AI agents, backed by Y Combinator. It tracks every agent session, tool call, and LLM interaction, then automatically detects issues, diagnoses root causes, and helps teams fix them in code. Developers instrument agents with the Sentrial Python or TypeScript SDK (one-line integrations for LangChain, CrewAI, AutoGen, Mastra, the Vercel AI SDK, and the Claude Agent SDK), by sending OpenTelemetry traces, or by calling the REST ingestion API (https://api.sentrial.com) directly to create sessions and record events. A `sentrial` CLI ships with the SDK for local setup, scriptable session/event inspection, diagnosis, and CI regression gates.
image: https://www.sentrial.com/og-image.png
layout: provider
modified: '2026-07-21'
name: Sentrial
nav: Providers
network: true
overview: 'Sentrial publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Events API and Sessions API. Tagged areas include Company, AI Agents, Observability, Monitoring, and LLM.


  The Sentrial catalog on APIs.io includes 1 Spectral governance ruleset.


  Sentrial''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, CLI, and 17 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Sentrial API Rules
  rule_count: 57
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 1
  slug: sentrial-rules
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 24.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sentrial/sentrial-2026-08-17T081809.png
security:
- kind: authentication
  name: Sentrial Authentication
  slug: sentrial-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sentrial Domain Security
  slug: sentrial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Record a tool call or decision event
  slug: sentrial-record-tool-call
- name: Track an agent session end-to-end
  slug: sentrial-track-agent-session
slug: sentrial
tags:
- Company
- AI Agents
- Observability
- Monitoring
- LLM
- Developer Tools
- Tracing
website: https://www.sentrial.com/
---

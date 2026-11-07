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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Archal Agentic Access
  operation_count: 16
  slug: archal-agentic-access
  summary_line: 16 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.archal.ai
  baseurl_source: declared
  description: Hosted clone session lifecycle.
  name: Archal Sessions API
  slug: archal-sessions-api
- baseURL: https://api.archal.ai
  baseurl_source: declared
  description: The Environments API from Archal — 3 operation(s) for environments.
  name: Archal Environments API
  slug: archal-environments-api
arazzos:
- description: Provision a hosted clone session, POST a request into the cloned service through the runtime proxy, read the resulting trace, then stop the session.
  name: Create an Archal clone session, drive it, and read the trace
  slug: archal-create-and-evaluate
artifact_total: 14
collections:
- collection_type: open
  name: Archal Auth API
  slug: open-archal-auth-api
- collection_type: open
  name: Archal Auth Catalog API
  slug: open-archal-catalog-api
- collection_type: open
  name: Archal Auth Results API
  slug: open-archal-results-api
- collection_type: open
  name: Archal Auth Runtime API
  slug: open-archal-runtime-api
- collection_type: open
  name: Archal Auth Sessions API
  slug: open-archal-sessions-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.archal.ai/
- group: agent
  href: https://artifacts.apis.io/archal/agentic-access/archal-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/archal-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/archal/security/archal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/archal-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/archal/authentication/archal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/archal-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.archal.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.archal.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.archal.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.archal.ai/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Archal-Labs
- group: build
  href: https://artifacts.apis.io/archal/packages/archal-packages.yml
  title: ''
  type: Packages
  url: packages/archal-packages.yml
- group: build
  href: https://artifacts.apis.io/archal/packages/archal-packages.yml
  title: ''
  type: SDKs
  url: packages/archal-packages.yml
- group: build
  href: https://artifacts.apis.io/archal/cli/archal-cli.yml
  title: ''
  type: CLI
  url: cli/archal-cli.yml
- group: start
  href: https://artifacts.apis.io/archal/sandbox/archal-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/archal-sandbox.yml
- group: design
  href: https://artifacts.apis.io/archal/conventions/archal-conventions.yml
  title: ''
  type: Conventions
  url: conventions/archal-conventions.yml
- group: design
  href: https://artifacts.apis.io/archal/conventions/archal-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/archal-conventions.yml
- group: design
  href: https://artifacts.apis.io/archal/errors/archal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/archal-problem-types.yml
- group: design
  href: https://artifacts.apis.io/archal/lifecycle/archal-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/archal-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/archal/conformance/archal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/archal-conformance.yml
- group: agent
  href: https://artifacts.apis.io/archal/mcp/archal-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/archal-mcp.yml
- group: agent
  href: https://artifacts.apis.io/archal/llms/archal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/archal-llms.txt
- group: other
  href: https://artifacts.apis.io/archal/overlays/archal-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/archal-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/archal/data-model/archal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/archal-data-model.yml
- group: agent
  href: https://artifacts.apis.io/archal/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/archal/arazzo/archal-create-and-evaluate.yml
  title: ''
  type: Arazzo
  url: arazzo/archal-create-and-evaluate.yml
created: '2026-07-17'
description: Archal is a Y Combinator (S26) company building QA and an improvement loop for AI agents. It provisions hosted, service-shaped CLONES of real SaaS services — GitHub, Slack, Stripe, Jira, Linear, Supabase, Ramp, HubSpot, Datadog, Discord, Google Workspace and more — so an agent that can send emails, change code repositories, or call third-party APIs is tested and scored before it touches production. Clones hold state, enforce referential integrity, and return authentic error shapes, unlike traditional mocks. Its Autoloop turns real production agent traces into reproducible failures and can open a fix PR. Archal ships an npm CLI and Vitest SDK, a device-auth login, a runtime clone proxy, and per-session MCP endpoints.
image: https://docs.archal.ai/logo/dark.svg
layout: provider
modified: '2026-07-18'
name: Archal
nav: Providers
network: true
overview: 'Archal publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Sessions API and Environments API. Tagged areas include Company, AI Agents, Agent Testing, Developer Tools, and API Testing.


  The Archal catalog on APIs.io includes 1 Spectral governance ruleset.


  Archal''s developer surface includes authentication, documentation, API reference, getting-started guide, CLI, sandbox, and 18 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Archal API Rules
  rule_count: 55
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 4
  slug: archal-rules
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 46.6
    developer_ergonomics: 73.2
    discoverability: 71.7
    operational_transparency: 2.6
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 25.0
      total: 8
    mcp: first-party
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
    score: 0.0
screenshot: https://apis.io/screenshots/archal/archal-2026-07-25T201020.png
security:
- kind: authentication
  name: Archal Authentication
  slug: archal-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Archal Domain Security
  slug: archal-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Inspect Archal runs, traces, and results
  slug: archal-inspect-results
- name: Run an agent against an Archal clone session
  slug: archal-run-clone-session
slug: archal
tags:
- Company
- AI Agents
- Agent Testing
- Developer Tools
- API Testing
- Sandbox
- Evaluation
- Infrastructure
website: https://www.archal.ai/
---

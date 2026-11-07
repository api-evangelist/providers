---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Agenticcontrolplane Com Agentic Access
  operation_count: 27
  slug: agenticcontrolplane-com-agentic-access
  summary_line: 27 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.agenticcontrolplane.com
  baseurl_source: declared
  description: Agent profiles — the governed identity + limits an agent runs under.
  name: Agentic Control Plane Agents API
  slug: agenticcontrolplane-com-agents-api
- baseURL: https://api.agenticcontrolplane.com
  baseurl_source: declared
  description: Short-lived scoped tokens bound to a user's stored OAuth credential.
  name: Agentic Control Plane Credentials API
  slug: agenticcontrolplane-com-credentials-api
- baseURL: https://api.agenticcontrolplane.com
  baseurl_source: declared
  description: 'Agent-to-agent delegation: scope-narrowed child API keys (ADCS).'
  name: Agentic Control Plane Delegation API
  slug: agenticcontrolplane-com-delegation-api
- baseURL: https://api.agenticcontrolplane.com
  baseurl_source: declared
  description: Read-only self-introspection over the caller's own governed footprint.
  name: Agentic Control Plane Introspect API
  slug: agenticcontrolplane-com-introspect-api
- baseURL: https://api.agenticcontrolplane.com
  baseurl_source: declared
  description: Model Context Protocol endpoint (streamable HTTP).
  name: Agentic Control Plane MCP API
  slug: agenticcontrolplane-com-mcp-api
- baseURL: https://api.agenticcontrolplane.com
  baseurl_source: declared
  description: Service metadata.
  name: Agentic Control Plane Meta API
  slug: agenticcontrolplane-com-meta-api
- baseURL: https://api.agenticcontrolplane.com
  baseurl_source: declared
  description: Governed model proxy — OpenAI- and Anthropic-compatible.
  name: Agentic Control Plane Proxy API
  slug: agenticcontrolplane-com-proxy-api
- baseURL: https://api.agenticcontrolplane.com
  baseurl_source: declared
  description: Run summaries — the same pre-aggregated data the console reads.
  name: Agentic Control Plane Runs API
  slug: agenticcontrolplane-com-runs-api
- baseURL: https://api.agenticcontrolplane.com
  baseurl_source: declared
  description: Zero-signup sandbox workspaces for agents with no tenant yet.
  name: Agentic Control Plane Sandbox API
  slug: agenticcontrolplane-com-sandbox-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/agenticcontrolplane-com/agentic-access/agenticcontrolplane-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agenticcontrolplane-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agenticcontrolplane-com/rules/agenticcontrolplane-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agenticcontrolplane-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agenticcontrolplane-com/json-ld/agenticcontrolplane-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agenticcontrolplane-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agenticcontrolplane-com/vocabulary/agenticcontrolplane-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agenticcontrolplane-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agenticcontrolplane-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agenticcontrolplane-com/data-model/agenticcontrolplane-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agenticcontrolplane-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://agenticcontrolplane.com/trust
- group: auth
  title: ''
  type: Security
  url: https://agenticcontrolplane.com/trust
- group: auth
  href: https://artifacts.apis.io/agenticcontrolplane-com/authentication/agenticcontrolplane-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenticcontrolplane-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agenticcontrolplane-com/scopes/agenticcontrolplane-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agenticcontrolplane-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/agenticcontrolplane-com/lifecycle/agenticcontrolplane-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agenticcontrolplane-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/agenticcontrolplane-com/errors/agenticcontrolplane-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agenticcontrolplane-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agenticcontrolplane-com/conformance/agenticcontrolplane-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenticcontrolplane-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenticcontrolplane-com/llms/agenticcontrolplane-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenticcontrolplane-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/agenticcontrolplane-com/well-known/agenticcontrolplane-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agenticcontrolplane-com-security.txt
- group: agent
  href: https://artifacts.apis.io/agenticcontrolplane-com/well-known/agenticcontrolplane-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenticcontrolplane-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenticcontrolplane-com/hosts/agenticcontrolplane-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticcontrolplane-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenticcontrolplane-com/vendors/agenticcontrolplane-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenticcontrolplane-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/agenticcontrolplane-com/packages/agenticcontrolplane-com-packages.yml
  title: ''
  type: SDKs
  url: packages/agenticcontrolplane-com-packages.yml
- group: build
  href: https://artifacts.apis.io/agenticcontrolplane-com/packages/agenticcontrolplane-com-packages.yml
  title: ''
  type: Packages
  url: packages/agenticcontrolplane-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://cloud.agenticcontrolplane.com/login
- group: auth
  href: https://artifacts.apis.io/agenticcontrolplane-com/security/agenticcontrolplane-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agenticcontrolplane-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/agenticcontrolplane-com/security/agenticcontrolplane-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agenticcontrolplane-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agenticcontrolplane-com/security/agenticcontrolplane-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticcontrolplane-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenticcontrolplane.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agenticcontrolplane.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://agenticcontrolplane.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agenticcontrolplane.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://agenticcontrolplane.com/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://agenticcontrolplane.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://agenticcontrolplane.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentic-control-plane
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenticcontrolplane.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenticcontrolplane.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.agenticcontrolplane.com/openapi.json
  - status: 401
    url: https://api.agenticcontrolplane.com/mcp
  - status: 200
    url: https://agenticcontrolplane.com/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: ACP shows you every tool call your coding agents make, lets you allow, ask, or deny each one, and prices every model call. Claude Code, Codex, OpenCode, Hermes, Cursor, and more. One command, no code changes. Free for individuals.
image: https://agenticcontrolplane.com/assets/img/favicon.svg
jsonld:
- class_count: 3
  name: Agenticcontrolplane Com Context
  property_count: 2
  slug: agenticcontrolplane-com-context
layout: provider
modified: '2026-11-01'
name: Agentic Control Plane
nav: Providers
network: true
overview: 'Agentic Control Plane publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Credentials API, Delegation API, and 6 more. Tagged areas include Artificial Intelligence, Agents, Control Plane, Tool Management, and Monitoring.


  The Agentic Control Plane catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agentic Control Plane''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 28 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Agentic Control Plane API Rules
  rule_count: 18
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 4
  slug: agenticcontrolplane-com-rules
scopes:
- name: Agenticcontrolplane Com Scopes
  scope_count: 4
  slug: agenticcontrolplane-com-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.2
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 52.1
    developer_ergonomics: 45.7
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenticcontrolplane Com Authentication
  slug: agenticcontrolplane-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agenticcontrolplane Com Domain Security
  slug: agenticcontrolplane-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agenticcontrolplane Com Vulnerability Disclosure
  slug: agenticcontrolplane-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Agenticcontrolplane Com Trust Center
  slug: agenticcontrolplane-com-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
skill_count: 2
skills:
- name: agents
  slug: agents
- name: proxy
  slug: proxy
slug: agenticcontrolplane-com
tags:
- Artificial Intelligence
- Agents
- Control Plane
- Tool Management
- Monitoring
website: https://agenticcontrolplane.com/
---

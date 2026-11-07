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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 49.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Agentsim Dev Agentic Access
  operation_count: 13
  slug: agentsim-dev-agentic-access
  summary_line: 13 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.agentsim.dev/v1
  baseurl_source: declared
  description: The Agents API from AgentSIM — 1 operation(s) for agents.
  name: AgentSIM Agents API
  slug: agentsim-dev-agents-api
- baseURL: https://api.agentsim.dev/v1
  baseurl_source: declared
  description: The Browser Access API from AgentSIM — 3 operation(s) for browser access.
  name: AgentSIM Browser Access API
  slug: agentsim-dev-browser-access-api
- baseURL: https://api.agentsim.dev/v1
  baseurl_source: declared
  description: The Sessions API from AgentSIM — 5 operation(s) for sessions.
  name: AgentSIM Sessions API
  slug: agentsim-dev-sessions-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/agentsim-dev/agentic-access/agentsim-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentsim-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentsim-dev/rules/agentsim-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/agentsim-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/agentsim-dev/json-ld/agentsim-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentsim-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentsim-dev/vocabulary/agentsim-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentsim-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentsim-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentsim-dev/data-model/agentsim-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentsim-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/agentsim-dev/changelog/agentsim-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agentsim-dev-changelog.yml
- group: auth
  href: https://artifacts.apis.io/agentsim-dev/security/agentsim-dev-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentsim-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentsim-dev/authentication/agentsim-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentsim-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentsim-dev/errors/agentsim-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentsim-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentsim-dev/conformance/agentsim-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentsim-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentsim-dev/llms/agentsim-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentsim-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/agentsim-dev/a2a/agentsim-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentsim-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentsim-dev/mcp/agentsim-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentsim-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentsim-dev/well-known/agentsim-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentsim-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/agentsim-dev/well-known/agentsim-dev-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentsim-dev-docs-security.txt
- group: auth
  href: https://artifacts.apis.io/agentsim-dev/well-known/agentsim-dev-console-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentsim-dev-console-security.txt
- group: agent
  href: https://artifacts.apis.io/agentsim-dev/well-known/agentsim-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentsim-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentsim-dev/hosts/agentsim-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentsim-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentsim-dev/vendors/agentsim-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentsim-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentsim-dev/packages/agentsim-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/agentsim-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/agentsim-dev/packages/agentsim-dev-packages.yml
  title: ''
  type: Packages
  url: packages/agentsim-dev-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentsim.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentsim.dev/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentsimdev
- group: operate
  title: ''
  type: ChangeLog
  url: https://agentsim.dev/changelog
- group: company
  title: ''
  type: Blog
  url: https://agentsim.dev/blog
- group: start
  title: ''
  type: SignUp
  url: https://console.agentsim.dev/sign-up
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agentsim.dev/llms.txt
- group: auth
  href: https://artifacts.apis.io/agentsim-dev/security/agentsim-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentsim-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentsim-dev/security/agentsim-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentsim-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentsim.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentsim.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentsim.dev/quickstart
created: '2026-11-01'
description: AgentSIM provides operational identity for agents hitting authentication walls. It lets you verify apps you own, run live SMS challenges, and return a code or safe stop into the agent workflow, enabling seamless integration of auth decisions into automated processes.
image: https://agentsim.dev/opengraph-image?2a28ea6a8fd47a32
json_schemas:
- name: BrowserConnection
  property_count: 8
  slug: agentsim-dev-browser-connection
- name: Session
  property_count: 8
  slug: agentsim-dev-session
jsonld:
- class_count: 3
  name: Agentsim Dev Context
  property_count: 16
  slug: agentsim-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.agentsim.dev requiring an API key.
  name: AgentSIM MCP Server
  slug: agentsim-dev-mcp-yml
modified: '2026-11-01'
name: AgentSIM
nav: Providers
network: true
overview: 'AgentSIM publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Agents API, Browser Access API, and Sessions API. Tagged areas include AgentSIM, Authentication, Identity, and Security.


  The AgentSIM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentSIM''s developer surface includes changelog, authentication, engineering blog, signup flow, API reference, documentation, getting-started guide, and 27 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AgentSIM API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: agentsim-dev-rules
scopes:
- name: Agentsim Dev Scopes
  scope_count: 0
  slug: agentsim-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 61.8
    developer_ergonomics: 41.0
    discoverability: 56.7
    operational_transparency: 21.1
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentsim Dev Authentication
  slug: agentsim-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agentsim Dev Domain Security
  slug: agentsim-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Agentsim Dev Vulnerability Disclosure
  slug: agentsim-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: agentsim
  slug: agentsim-dev-agentsim
slug: agentsim-dev
tags:
- AgentSIM
- Authentication
- Identity
- Security
website: https://agentsim.dev/
---

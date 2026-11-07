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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 67
  human_in_the_loop: 0
  name: Fleetai Com Agentic Access
  operation_count: 139
  slug: fleetai-com-agentic-access
  summary_line: 139 operations · 67 acting
api_count: 2
apis:
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The account API from Fleet — 2 operation(s) for account.
  name: Fleet Account API
  slug: fleetai-com-account-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The browsers API from Fleet — 3 operation(s) for browsers.
  name: Fleet Browsers API
  slug: fleetai-com-browsers-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The cost-attribution API from Fleet — 1 operation(s) for cost-attribution.
  name: Fleet Cost Attribution API
  slug: fleetai-com-cost-attribution-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The instances API from Fleet — 13 operation(s) for instances.
  name: Fleet Instances API
  slug: fleetai-com-instances-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The jobs API from Fleet — 20 operation(s) for jobs.
  name: Fleet Jobs API
  slug: fleetai-com-jobs-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The matg API from Fleet — 18 operation(s) for matg.
  name: Fleet Matg API
  slug: fleetai-com-matg-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The provenance-audits API from Fleet — 2 operation(s) for provenance-audits.
  name: Fleet Provenance Audits API
  slug: fleetai-com-provenance-audits-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The seed-gen API from Fleet — 16 operation(s) for seed-gen.
  name: Fleet Seed Gen API
  slug: fleetai-com-seed-gen-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The seeds API from Fleet — 1 operation(s) for seeds.
  name: Fleet Seeds API
  slug: fleetai-com-seeds-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The sessions API from Fleet — 4 operation(s) for sessions.
  name: Fleet Sessions API
  slug: fleetai-com-sessions-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The task-groups API from Fleet — 2 operation(s) for task-groups.
  name: Fleet Task Groups API
  slug: fleetai-com-task-groups-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The tasks API from Fleet — 31 operation(s) for tasks.
  name: Fleet Tasks API
  slug: fleetai-com-tasks-api
- baseURL: https://orchestrator.fleetai.com
  baseurl_source: declared
  description: The verifiers API from Fleet — 9 operation(s) for verifiers.
  name: Fleet Verifiers API
  slug: fleetai-com-verifiers-api
artifact_total: 32
common:
- group: other
  href: https://artifacts.apis.io/fleetai-com/capabilities/fleetai-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fleetai-com-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/fleetai-com/agentic-access/fleetai-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fleetai-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/fleetai-com/rules/fleetai-com-rules.yml
  title: ''
  type: Spectral
  url: rules/fleetai-com-rules.yml
- group: design
  href: https://artifacts.apis.io/fleetai-com/json-ld/fleetai-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fleetai-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/fleetai-com/vocabulary/fleetai-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fleetai-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/fleetai-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/fleetai-com/data-model/fleetai-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fleetai-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/fleetai-com/cli/fleetai-com-cli.yml
  title: ''
  type: CLI
  url: cli/fleetai-com-cli.yml
- group: design
  href: https://artifacts.apis.io/fleetai-com/conventions/fleetai-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/fleetai-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/fleetai-com/conventions/fleetai-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fleetai-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/fleetai-com/security/fleetai-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/fleetai-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/fleetai-com/lifecycle/fleetai-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fleetai-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fleetai-com/errors/fleetai-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fleetai-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fleetai-com/conformance/fleetai-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fleetai-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/fleetai-com/overlays/fleetai-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fleetai-com-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/fleetai-com/mcp/fleetai-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fleetai-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/fleetai-com/mcp/fleetai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fleetai-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/fleetai-com/well-known/fleetai-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fleetai-com-security.txt
- group: auth
  href: https://artifacts.apis.io/fleetai-com/well-known/fleetai-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fleetai-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/fleetai-com/well-known/fleetai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fleetai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/fleetai-com/hosts/fleetai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fleetai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/fleetai-com/vendors/fleetai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fleetai-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/fleetai-com/packages/fleetai-com-packages.yml
  title: ''
  type: SDKs
  url: packages/fleetai-com-packages.yml
- group: build
  href: https://artifacts.apis.io/fleetai-com/packages/fleetai-com-packages.yml
  title: ''
  type: Packages
  url: packages/fleetai-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/fleetai-com/authentication/fleetai-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fleetai-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/fleetai-com/security/fleetai-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fleetai-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fleetai-com/security/fleetai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fleetai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fleetai.com/
- group: company
  title: ''
  type: About
  url: https://fleetai.com/about
- group: company
  title: ''
  type: Careers
  url: https://fleetai.com/careers
- group: start
  title: ''
  type: Login
  url: https://app.fleetai.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fleetai.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.fleetai.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fleet-ai
- group: other
  title: ''
  type: X
  url: https://x.com/fleet_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fleet-so/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fleetai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fleetai.com/privacy
- group: other
  title: ''
  type: CookiePolicy
  url: https://fleetai.com/cookies
created: '2026-10-27'
description: 'Fleet (Fleet AI, Inc.) is an applied research lab that builds environments: diverse, high-fidelity simulated training gyms that model real-world work so AI agents can practice tasks while humans provide supervision. It works with frontier labs, hyperscalers and enterprises on evals and environments for agents, and is backed by Sequoia Capital, Menlo Ventures and SV Angel. Its public site lists no public API; its documentation host (docs.fleetai.com) redirects to a login page.'
image: https://fleetai.com/images/OG-Image.jpg
json_schemas:
- name: CounselDeskTaskQAStateResponse
  property_count: 20
  slug: fleetai-com-counsel-desk-task-qastate-response
- name: InstanceRequest
  property_count: 38
  slug: fleetai-com-instance-request
- name: InstanceResponse
  property_count: 36
  slug: fleetai-com-instance-response
- name: JobCreateRequestPayload
  property_count: 85
  slug: fleetai-com-job-create-request-payload
- name: TaskRequest
  property_count: 23
  slug: fleetai-com-task-request
- name: VerifiersExecuteRequest
  property_count: 29
  slug: fleetai-com-verifiers-execute-request
jsonld:
- class_count: 120
  name: Fleetai Com Context
  property_count: 424
  slug: fleetai-com-context
layout: provider
mcp_servers:
- description: 'Fleet''s official fleet-python SDK (PyPI fleet-python 0.2.133, Apache-2.0, repository github.com/fleet-ai/fleet-sdk) ships a local stdio MCP server, FastMCP("fleetcode"), exposed as the console script '
  name: FleetCode MCP server (Fleet)
  slug: fleetcode-mcp-server-fleet
modified: '2026-10-27'
name: Fleet
nav: Providers
network: true
overview: 'Fleet publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Browsers API, Cost Attribution API, and 10 more. Tagged areas include Company, Artificial Intelligence, AI Agents, Reinforcement Learning Environments, and Evaluation.


  The Fleet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fleet''s developer surface includes CLI, authentication, and 37 more developer resources.'
plans:
- name: Fleetai Com Plans Pricing
  plan_count: 0
  slug: fleetai-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Fleetai Com Rate Limits
  slug: fleetai-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Fleet API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: fleetai-com-rules
score:
  band: developing
  composite: 43.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 61.9
    developer_ergonomics: 32.7
    discoverability: 65.0
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/fleetai-com/fleetai-com-2026-11-03T132130.png
security:
- kind: authentication
  name: Fleetai Com Authentication
  slug: fleetai-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fleetai Com Domain Security
  slug: fleetai-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Fleetai Com Vulnerability Disclosure
  slug: fleetai-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: fleetai-com-author-tasks-in-a-project
  slug: fleetai-com-author-tasks-in-a-project
- name: fleetai-com-execute-a-verifier
  slug: fleetai-com-execute-a-verifier
- name: fleetai-com-launch-and-monitor-a-job
  slug: fleetai-com-launch-and-monitor-a-job
- name: fleetai-com-provision-an-environment-instance
  slug: fleetai-com-provision-an-environment-instance
slug: fleetai-com
tags:
- Company
- Artificial Intelligence
- AI Agents
- Reinforcement Learning Environments
- Evaluation
- Simulation
- Training Data
website: https://fleetai.com/
---

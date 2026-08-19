---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 19
  human_in_the_loop: 17
  name: Accept Agentic Access
  operation_count: 83
  slug: accept-agentic-access
  summary_line: 83 operations · 19 acting · 17 human-in-the-loop
api_count: 23
apis:
- description: The Agents API from Accept — 1 operation(s) for agents.
  name: Accept Agents API
  slug: accept-agents-api
- description: The Aisystems API from Accept — 5 operation(s) for aisystems.
  name: Accept Aisystems API
  slug: accept-aisystems-api
- description: The Businessservices API from Accept — 3 operation(s) for businessservices.
  name: Accept Businessservices API
  slug: accept-businessservices-api
- description: The Capabilities API from Accept — 5 operation(s) for capabilities.
  name: Accept Capabilities API
  slug: accept-capabilities-api
- description: The Controlplane API from Accept — 18 operation(s) for controlplane.
  name: Accept Controlplane API
  slug: accept-controlplane-api
- description: The Coverage API from Accept — 1 operation(s) for coverage.
  name: Accept Coverage API
  slug: accept-coverage-api
- description: The Decisions API from Accept — 1 operation(s) for decisions.
  name: Accept Decisions API
  slug: accept-decisions-api
- description: The Drift API from Accept — 15 operation(s) for drift.
  name: Accept Drift API
  slug: accept-drift-api
- description: The Envelopes API from Accept — 2 operation(s) for envelopes.
  name: Accept Envelopes API
  slug: accept-envelopes-api
- description: The Escalation Targets API from Accept — 4 operation(s) for escalation targets.
  name: Accept Escalation Targets API
  slug: accept-escalation-targets-api
- description: The Escalations API from Accept — 1 operation(s) for escalations.
  name: Accept Escalations API
  slug: accept-escalations-api
- description: The Evaluate API from Accept — 1 operation(s) for evaluate.
  name: Accept Evaluate API
  slug: accept-evaluate-api
- description: The Evidence API from Accept — 4 operation(s) for evidence.
  name: Accept Evidence API
  slug: accept-evidence-api
- description: The Fail Mode Policies API from Accept — 3 operation(s) for fail mode policies.
  name: Accept Fail Mode Policies API
  slug: accept-fail-mode-policies-api
- description: The Grants API from Accept — 2 operation(s) for grants.
  name: Accept Grants API
  slug: accept-grants-api
- description: The Graphs API from Accept — 2 operation(s) for graphs.
  name: Accept Graphs API
  slug: accept-graphs-api
- description: The Healthz API from Accept — 1 operation(s) for healthz.
  name: Accept Healthz API
  slug: accept-healthz-api
- description: The Platform API from Accept — 1 operation(s) for platform.
  name: Accept Platform API
  slug: accept-platform-api
- description: The Processes API from Accept — 3 operation(s) for processes.
  name: Accept Processes API
  slug: accept-processes-api
- description: The Profiles API from Accept — 4 operation(s) for profiles.
  name: Accept Profiles API
  slug: accept-profiles-api
- description: The Readyz API from Accept — 1 operation(s) for readyz.
  name: Accept Readyz API
  slug: accept-readyz-api
- description: The Reviews API from Accept — 1 operation(s) for reviews.
  name: Accept Reviews API
  slug: accept-reviews-api
- description: The Surfaces API from Accept — 4 operation(s) for surfaces.
  name: Accept Surfaces API
  slug: accept-surfaces-api
artifact_total: 52
asyncapis:
- description: External event contract for MIDAS decision governance. Events are written to a transactional outbox in the same Postgres transaction as domain state changes, then dispatched to Kafka by a background d
  name: MIDAS External Event Contract
  slug: accept-midas-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MIDAS Agents API
  slug: open-accept-agents-api
- collection_type: open
  name: MIDAS Agents Aisystems API
  slug: open-accept-aisystems-api
- collection_type: open
  name: MIDAS Agents Businessservices API
  slug: open-accept-businessservices-api
- collection_type: open
  name: MIDAS Agents Capabilities API
  slug: open-accept-capabilities-api
- collection_type: open
  name: MIDAS Agents Controlplane API
  slug: open-accept-controlplane-api
- collection_type: open
  name: MIDAS Agents Coverage API
  slug: open-accept-coverage-api
- collection_type: open
  name: MIDAS Agents Decisions API
  slug: open-accept-decisions-api
- collection_type: open
  name: MIDAS Agents Drift API
  slug: open-accept-drift-api
- collection_type: open
  name: MIDAS Agents Envelopes API
  slug: open-accept-envelopes-api
- collection_type: open
  name: MIDAS Agents Escalation Targets API
  slug: open-accept-escalation-targets-api
- collection_type: open
  name: MIDAS Agents Escalations API
  slug: open-accept-escalations-api
- collection_type: open
  name: MIDAS Agents Evaluate API
  slug: open-accept-evaluate-api
- collection_type: open
  name: MIDAS Agents Evidence API
  slug: open-accept-evidence-api
- collection_type: open
  name: MIDAS Agents Fail Mode Policies API
  slug: open-accept-fail-mode-policies-api
- collection_type: open
  name: MIDAS Agents Grants API
  slug: open-accept-grants-api
- collection_type: open
  name: MIDAS Agents Graphs API
  slug: open-accept-graphs-api
- collection_type: open
  name: MIDAS Agents Healthz API
  slug: open-accept-healthz-api
- collection_type: open
  name: MIDAS Agents Platform API
  slug: open-accept-platform-api
- collection_type: open
  name: MIDAS Agents Processes API
  slug: open-accept-processes-api
- collection_type: open
  name: MIDAS Agents Profiles API
  slug: open-accept-profiles-api
- collection_type: open
  name: MIDAS Agents Readyz API
  slug: open-accept-readyz-api
- collection_type: open
  name: MIDAS Agents Surfaces API
  slug: open-accept-surfaces-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/accept-midas-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/accept-io/midas/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/accept-io/midas/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/accept-io/midas/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/accept-io/midas/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accept-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/accept-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/accept-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/accept-midas-asyncapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/accept-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/accept-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/accept-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accept-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/accept-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/accept-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/accept-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/accept-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accept-llms.txt
- group: build
  title: ''
  type: CLI
  url: cli/accept-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/accept-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/accept-io/midas/blob/main/CHANGELOG.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/accept-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/accept-io/midas/blob/main/SECURITY.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.accept.io
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/accept-io/midas/tree/main/docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/accept-io/midas/blob/main/docs/api/http-api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/accept-io/midas/blob/main/docs/getting-started.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/accept-io
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/accept-io/midas
- group: operate
  title: ''
  type: Support
  url: https://github.com/accept-io/community
- group: company
  title: ''
  type: Blog
  url: https://www.accept.io/learn/learn-midas
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/accept-io/midas/blob/main/ROADMAP.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/accept-io/midas/blob/main/LICENSE
- group: start
  title: ''
  type: Sandbox
  url: sandbox/accept-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://midas.accept.io/explorer
created: '2026-07-17'
description: Accept Labs is the company behind MIDAS, an open-source authority-governance engine for autonomous decisions. MIDAS evaluates every agent or AI-system action against explicit authority, operational boundaries, and execution context before the action occurs, then produces exactly one outcome (accept, escalate, reject, or request_clarification) and one tamper-evident audit envelope. The platform is Apache-2.0 Go software with a runtime evaluation API (POST /v1/evaluate), a YAML control-plane for surfaces/profiles/grants, an evidence and integrity API, drift detection, an Explorer UI, and OIDC/local IAM. It is positioned for enterprise teams governing what automated actors are authorised to decide.
image: https://github.com/accept-io.png
layout: provider
mcp_servers:
- description: ''
  name: accept-mcp.yml
  slug: accept-mcpyml
modified: '2026-07-18'
name: Accept
nav: Providers
network: true
overview: 'Accept publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Aisystems API, Businessservices API, and 20 more. Tagged areas include Company, Enterprise, Governance, AI Agents, and Authority.


  The Accept catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Accept''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, support, and 29 more developer resources.'
random_paper: 28
score:
  band: developing
  composite: 45.2
  delta: 0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 59.6
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/accept/refs/heads/main/screenshots/accept-2026-07-25T181433.png
security:
- kind: authentication
  name: Accept Authentication
  slug: accept-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Accept Domain Security
  slug: accept-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Accept Vulnerability Disclosure
  slug: accept-vulnerability-disclosure
  summary_line: contact published
slug: accept
tags:
- Company
- Enterprise
- Governance
- AI Agents
- Authority
- Decision Governance
- Audit
- Open Source
website: https://www.accept.io
---

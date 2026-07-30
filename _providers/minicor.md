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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Minicor Agentic Access
  operation_count: 7
  slug: minicor-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 3
apis:
- description: Laminar Configuration Store endpoints, for managing configuration stores and properties within workspaces.
  name: Minicor Configuration Stores API
  slug: minicor-configuration-stores-api
- description: The external API from Minicor — 7 operation(s) for external.
  name: Minicor external API
  slug: minicor-external-api
- description: Laminar Workflow endpoints, for managing workflows and workflow executions.
  name: Minicor Workflows API
  slug: minicor-workflows-api
artifact_total: 13
asyncapis:
- description: ''
  name: Minicor Webhooks
  slug: minicor-webhooks
collections:
- collection_type: postman
  name: Laminar Configuration Stores API
  slug: postman-minicor-configuration-stores-api
- collection_type: postman
  name: Laminar Configuration Stores external API
  slug: postman-minicor-external-api
- collection_type: postman
  name: Laminar Configuration Stores Workflows API
  slug: postman-minicor-workflows-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/minicor/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.laminar.run/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.laminar.run/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.laminar.run/api-guide/execute-a-workflow
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.laminar.run/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/minicor-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://minicor.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/laminar-run
- group: operate
  title: ''
  type: Support
  url: https://docs.laminar.run/get-in-touch/product-support
- group: start
  title: ''
  type: SignUp
  url: https://app.laminar.run/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.laminar.run/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.laminar.run/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.laminar.run/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.laminar.run/get-in-touch/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/minicor-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/minicor-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/minicor-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/minicor-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/minicor-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/minicor-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/minicor-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/minicor-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/minicor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/minicor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/minicor-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.mycroft.io/trust/laminar
- group: auth
  title: ''
  type: Compliance
  url: https://app.mycroft.io/trust/laminar
- group: design
  title: ''
  type: Conformance
  url: conformance/minicor-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/minicor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/minicor-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/minicor-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/minicor-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/minicor-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/minicor-agentic-access.yml
created: '2026-07-17'
description: 'Minicor (operated by Laminar Run, Inc.) is a platform for building and running desktop automations at scale using computer-use AI agents. Legacy desktop software such as EHRs, ERPs, DMS, WMS and PMS systems often has no API, so the only way to read or write data is to drive the desktop like a human. Minicor automates these systems reliably: install a desktop client on the machines running the legacy software, record a workflow, and trigger a full desktop workflow on a Windows VM with a single API call that returns structured JSON. Automations are stored as deterministic code for speed while a reasoning model, grounding model, reflection agent and OCR handle recovery, adaptation and edge cases, self-healing when UIs change. The developer-facing surface is the Laminar API (api.laminar.run) for executing workflows and managing configuration stores, authenticated with an API key. Minicor is SOC 2 Type II and HIPAA compliant and is a Y Combinator (X26) company.'
image: https://minicor.com/images/logo-minicor.svg
layout: provider
mcp_servers:
- description: ''
  name: minicor-mcp.yml
  slug: minicor-mcpyml
modified: '2026-07-20'
name: Minicor
nav: Providers
network: true
overview: 'Minicor publishes 3 APIs on the [APIs.io](https://apis.io/) network: Configuration Stores API, external API, and Workflows API. Tagged areas include Company, Desktop Automation, RPA, Computer Use Agents, and Workflow Automation.


  The Minicor catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Minicor''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, signup flow, and 28 more developer resources.'
random_paper: 15
score:
  band: strong
  composite: 58.8
  delta: -3.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.3
    developer_ergonomics: 73.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Minicor Authentication
  slug: minicor-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Minicor Domain Security
  slug: minicor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Minicor Vulnerability Disclosure
  slug: minicor-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Minicor Trust Center
  slug: minicor-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: minicor
tags:
- Company
- Desktop Automation
- RPA
- Computer Use Agents
- Workflow Automation
- Healthcare
- Legacy Systems
- AI Agents
- Integration
website: https://docs.laminar.run/
---

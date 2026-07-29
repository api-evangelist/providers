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
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 3
  name: Method Security Agentic Access
  operation_count: 18
  slug: method-security-agentic-access
  summary_line: 18 operations · 10 acting · 3 human-in-the-loop
api_count: 10
apis:
- description: The audit API from Method Security — 1 operation(s) for audit.
  name: Method Security audit API
  slug: method-security-audit-api
- description: The auth API from Method Security — 1 operation(s) for auth.
  name: Method Security auth API
  slug: method-security-auth-api
- description: The blueprints API from Method Security — 2 operation(s) for blueprints.
  name: Method Security blueprints API
  slug: method-security-blueprints-api
- description: The environments API from Method Security — 2 operation(s) for environments.
  name: Method Security environments API
  slug: method-security-environments-api
- description: The issues API from Method Security — 2 operation(s) for issues.
  name: Method Security issues API
  slug: method-security-issues-api
- description: The reports API from Method Security — 1 operation(s) for reports.
  name: Method Security reports API
  slug: method-security-reports-api
- description: The signals API from Method Security — 1 operation(s) for signals.
  name: Method Security signals API
  slug: method-security-signals-api
- description: The skills API from Method Security — 3 operation(s) for skills.
  name: Method Security skills API
  slug: method-security-skills-api
- description: The system API from Method Security — 1 operation(s) for system.
  name: Method Security system API
  slug: method-security-system-api
- description: The targets API from Method Security — 3 operation(s) for targets.
  name: Method Security targets API
  slug: method-security-targets-api
artifact_total: 17
asyncapis:
- description: ''
  name: Method Security Webhooks
  slug: method-security-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://method.security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.method.security
- group: docs
  title: ''
  type: Documentation
  url: https://docs.method.security
- group: docs
  title: ''
  type: APIReference
  url: https://docs.method.security/developer/api-reference/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.method.security/guides/overview/get-started
- group: company
  title: ''
  type: Blog
  url: https://method.security/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/method-security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://method.security/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://method.security/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/method-security-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/method-security-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/method-security-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/method-security-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/method-security-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/method-security-api-catalog.json
- group: build
  title: ''
  type: Packages
  url: packages/method-security-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/method-security-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/method-security-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/method-security-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/method-security-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/method-security-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/method-security-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/method-security-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/method-security-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/method-security-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/method-security-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/method-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.method.security/platform/security-governance/reporting-security-concerns
- group: auth
  title: ''
  type: TrustCenter
  url: security/method-security-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/method-security-trust-center.yml
created: '2026-07-17'
description: 'Method Security is a cybersecurity company delivering cyber resilience to the U.S. Government and critical enterprises through an AI-native, full-spectrum security platform. The Method Platform blends offensive and defensive operations across cloud, on-premise, and internet-denied environments, and ships two flagship products: Bastion (digital-twin driven exposure and attack-surface management that maps, validates, and controls resources and attack paths) and Reaper/Operations (software-defined offensive operations and red-team execution). The platform is built around an Ontology object model, AI Agents governed by granular Policies, Jackal C2 agents, Overwatch terminal session recording, and an Explorer/Automator workspace. Method exposes a public REST API (OpenAPI 3.1) through the method-api-gateway, a published Python SDK (methodsdk), a docs MCP server, and OAuth 2.0 client-credentials authentication backed by Keycloak. Backed by OpenAI, Palantir, Andreessen Horowitz, General
  Catalyst, and Blackstone.'
image: https://www.method.security/content/seo/method-graphic-social-1200x628.png
layout: provider
mcp_servers:
- description: ''
  name: method-security-mcp.yml
  slug: method-security-mcpyml
modified: '2026-07-20'
name: Method Security
nav: Providers
network: true
overview: 'Method Security publishes 10 APIs on the [APIs.io](https://apis.io/) network, including audit API, auth API, blueprints API, and 7 more. Tagged areas include Company, Security, Cybersecurity, Offensive Security, and Exposure Management.


  The Method Security catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Method Security''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, CLI, changelog, and 24 more developer resources.'
random_paper: 35
score:
  band: developing
  composite: 54.6
  delta: -1.6
  facets:
    commercial_clarity: 36.8
    contract_quality: 55.8
    developer_ergonomics: 71.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 66.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Method Security Authentication
  slug: method-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Method Security Domain Security
  slug: method-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Method Security Vulnerability Disclosure
  slug: method-security-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Method Security Trust Center
  slug: method-security-trust-center
  summary_line: SOC 2
slug: method-security
tags:
- Company
- Security
- Cybersecurity
- Offensive Security
- Exposure Management
- Attack Surface Management
- Vulnerability Management
- Red Team
- AI Agents
- Government
website: https://method.security
---

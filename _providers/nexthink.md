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
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 72.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Nexthink Agentic Access
  operation_count: 17
  slug: nexthink-agentic-access
  summary_line: 17 operations · 11 acting
api_count: 8
apis:
- description: The Campaigns API from Nexthink — 1 operation(s) for campaigns.
  name: Nexthink Campaigns API
  slug: nexthink-campaigns-api
- description: The device-deletions API from Nexthink — 1 operation(s) for device-deletions.
  name: Nexthink device-deletions API
  slug: nexthink-device-deletions-api
- description: The enrichment API from Nexthink — 1 operation(s) for enrichment.
  name: Nexthink enrichment API
  slug: nexthink-enrichment-api
- description: The Execute API from Nexthink — 2 operation(s) for execute.
  name: Nexthink Execute API
  slug: nexthink-execute-api
- description: The Export API from Nexthink — 2 operation(s) for export.
  name: Nexthink Export API
  slug: nexthink-export-api
- description: The Handoff API API from Nexthink — 1 operation(s) for handoff api.
  name: Nexthink Handoff API API
  slug: nexthink-handoff-api-api
- description: The Remote actions API from Nexthink — 3 operation(s) for remote actions.
  name: Nexthink Remote actions API
  slug: nexthink-remote-actions-api
- description: The Workflows API from Nexthink — 5 operation(s) for workflows.
  name: Nexthink Workflows API
  slug: nexthink-workflows-api
artifact_total: 15
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.nexthink.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nexthink.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nexthink.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nexthink.com/api/api-credentials
- group: auth
  title: ''
  type: Authentication
  url: authentication/nexthink-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nexthink-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nexthink-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nexthink-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nexthink-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nexthink-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.nexthink.com/platform/whats-new
- group: design
  title: ''
  type: DataModel
  url: data-model/nexthink-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nexthink-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.nexthink.com/trust-center
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.nexthink.com/trust-center
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nexthink-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nexthink-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nexthink-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nexthink-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nexthink-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.nexthink.com/responsible-disclosure-policy/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nexthink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexthink-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nexthink.com/blog
- group: operate
  title: ''
  type: Support
  url: https://community.nexthink.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nexthink
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nexthink.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.nexthink.com/legal/services-terms
- group: company
  title: ''
  type: Website
  url: https://www.nexthink.com
created: '2026-07-17'
description: Nexthink is a digital employee experience (DEX) management company. Its Infinity platform combines real-time endpoint analytics, employee sentiment, and automated remediation so IT teams can proactively detect and fix issues across every device. Nexthink exposes a set of OAuth 2.0-secured public APIs — NQL (query), Remote Actions, Workflows, Enrichment, Campaigns, Data Management, and Spark — that let external tools pull DEX data and drive endpoint automation. Backed by Index Ventures; added to the API Evangelist network and enriched from Nexthink's published developer documentation.
image: https://www.nexthink.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: nexthink-mcp.yml
  slug: nexthink-mcpyml
modified: '2026-07-20'
name: Nexthink
nav: Providers
network: true
overview: 'Nexthink publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, device-deletions API, enrichment API, and 5 more. Tagged areas include Company, Business Applications, Digital Employee Experience, Endpoint Analytics, and IT Operations.


  Nexthink''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 23 more developer resources.'
random_paper: 6
scopes:
- name: Nexthink Scopes
  scope_count: 1
  slug: nexthink-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 54.4
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 48.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Nexthink Authentication
  slug: nexthink-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Nexthink Domain Security
  slug: nexthink-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nexthink Vulnerability Disclosure
  slug: nexthink-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Nexthink Trust Center
  slug: nexthink-trust-center
  summary_line: trust center published
slug: nexthink
tags:
- Company
- Business Applications
- Digital Employee Experience
- Endpoint Analytics
- IT Operations
- Automation
- Observability
- DEX
website: https://www.nexthink.com
---

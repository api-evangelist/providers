---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Riot Agentic Access
  operation_count: 40
  slug: riot-agentic-access
  summary_line: 40 operations · 9 acting
api_count: 14
apis:
- description: Provides data about courses, their settings within the workspace and employees' learning progress.
  name: Riot Awareness API
  slug: riot-awareness-api
- description: The Breaches API from Riot — 3 operation(s) for breaches.
  name: Riot Breaches API
  slug: riot-breaches-api
- description: Provides an overview of the organization and employees' data.
  name: Riot General API
  slug: riot-general-api
- description: The Groups API from Riot — 2 operation(s) for groups.
  name: Riot Groups API
  slug: riot-groups-api
- description: The Inbox API from Riot — 3 operation(s) for inbox.
  name: Riot Inbox API
  slug: riot-inbox-api
- description: The SCIM API from Riot — 9 operation(s) for scim.
  name: Riot SCIM API
  slug: riot-scim-api
- description: Provides data about phishing campaigns, corresponding attacks and related events.
  name: Riot Simulation API
  slug: riot-simulation-api
- description: The Slash API from Riot — 2 operation(s) for slash.
  name: Riot Slash API
  slug: riot-slash-api
- description: The Sonar API from Riot — 0 operation(s) for sonar.
  name: Riot Sonar API
  slug: riot-sonar-api
- description: The Team awareness API from Riot — 4 operation(s) for team awareness.
  name: Riot Team awareness API
  slug: riot-team-awareness-api
- description: The Team inbox API from Riot — 5 operation(s) for team inbox.
  name: Riot Team inbox API
  slug: riot-team-inbox-api
- description: The Team platform API from Riot — 15 operation(s) for team platform.
  name: Riot Team platform API
  slug: riot-team-platform-api
- description: The Team simulation API from Riot — 8 operation(s) for team simulation.
  name: Riot Team simulation API
  slug: riot-team-simulation-api
- description: Server-to-server events Riot sends to customer-configured endpoints.
  name: Riot Webhook Events API
  slug: riot-webhook-events-api
artifact_total: 23
asyncapis:
- description: ''
  name: Riot Webhooks
  slug: riot-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/riot-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/riot-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://tryriot.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tryriot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryriot.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tryriot.com/
- group: company
  title: ''
  type: Blog
  url: https://tryriot.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://tryriot.com/support/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tryriot
- group: commercial
  title: ''
  type: Pricing
  url: https://tryriot.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.tryriot.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryriot.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryriot.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tryriot.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://tryriot.com/changelog/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/riot-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://tryriot.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/riot-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.tryriot.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/riot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/riot-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/riot-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/riot-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/riot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/riot-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/riot-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/riot-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/riot-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/riot-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/riot-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/riot-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/riot-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/riot-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/riot-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/riot-public-api-overlay.yaml
created: '2026-08-05'
description: Riot is a Paris-based employee security posture management (human risk management) platform that helps companies reduce the human attack surface. The product suite spans phishing and smishing simulation, security awareness training courses, credential breach monitoring, employee-reported email triage (Inbox), inbound email protection (Slash), and third-party SaaS/drive exposure monitoring (Sonar), fronted by a chat assistant that runs in Slack, Microsoft Teams and the web portal. Riot publishes a public REST API (OpenAPI 3.1.1, x-api-key authentication, cursor pagination, scoped keys) that exposes organization, employee, group, course, campaign, attack, breach and inbox data, a SCIM 2.0 provisioning surface for user and group lifecycle, and Standard-Webhooks server-to-server events whose payloads follow the OCSF Detection Finding schema so they can be ingested by a SIEM or SOAR without custom mapping.
image: https://cms-content.tryriot.com/riot_preview_305b31b839.png
layout: provider
mcp_servers:
- description: ''
  name: riot-mcp.yml
  slug: riot-mcpyml
modified: '2026-08-05'
name: Riot
nav: Providers
network: true
overview: 'Riot publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Awareness API, Breaches API, General API, and 11 more. Tagged areas include cybersecurity, security-awareness, human-risk-management, phishing-simulation, and employee-security.


  The Riot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Riot''s developer surface includes documentation, API reference, engineering blog, support, pricing, changelog, authentication, and 29 more developer resources.'
random_paper: 98
rate_limits:
- limit_count: 0
  name: Riot Rate Limits
  slug: riot-rate-limits
scopes:
- name: Riot Scopes
  scope_count: 4
  slug: riot-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 56.6
  delta: 1.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.0
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Riot Authentication
  slug: riot-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Riot Domain Security
  slug: riot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Riot Vulnerability Disclosure
  slug: riot-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Riot Trust Center
  slug: riot-trust-center
  summary_line: AICPA SOC 2 Type II, GDPR
slug: riot
tags:
- cybersecurity
- security-awareness
- human-risk-management
- phishing-simulation
- employee-security
- security-posture-management
- breach-detection
- email-security
- saas-security
- scim
- webhooks
- ocsf
- france
website: https://tryriot.com/
---

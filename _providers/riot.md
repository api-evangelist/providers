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
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Riot Agentic Access
  operation_count: 40
  slug: riot-agentic-access
  summary_line: 40 operations · 9 acting
api_count: 1
apis:
- description: Public REST API for the Riot employee security posture management platform. Read access to organization and workspace metadata, employees and groups, awareness courses and per-employee learning progre
  name: Riot Public API
  slug: riot-public-api
artifact_total: 9
asyncapis:
- description: ''
  name: Riot Webhooks
  slug: riot-webhooks
common:
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
modified: '2026-08-05'
name: Riot
nav: Providers
network: true
overview: 'Riot publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include cybersecurity, security-awareness, human-risk-management, phishing-simulation, and employee-security.


  The Riot catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Riot''s developer surface includes documentation, API reference, engineering blog, support, pricing, changelog, authentication, and 28 more developer resources.'
random_paper: 107
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
  composite: 56.3
  delta: -1.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 69.1
    developer_ergonomics: 42.9
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 57.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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

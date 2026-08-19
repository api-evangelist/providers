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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Parsec Agentic Access
  operation_count: 42
  slug: parsec-agentic-access
  summary_line: 42 operations · 26 acting
api_count: 8
apis:
- description: The App Rule API from Parsec — 3 operation(s) for app rule.
  name: Parsec App Rule API
  slug: parsec-app-rule-api
- description: The Audit Log API from Parsec — 2 operation(s) for audit log.
  name: Parsec Audit Log API
  slug: parsec-audit-log-api
- description: The Group API from Parsec — 7 operation(s) for group.
  name: Parsec Group API
  slug: parsec-group-api
- description: The Guest Access Invite API from Parsec — 4 operation(s) for guest access invite.
  name: Parsec Guest Access Invite API
  slug: parsec-guest-access-invite-api
- description: The Machine API from Parsec — 4 operation(s) for machine.
  name: Parsec Machine API
  slug: parsec-machine-api
- description: The Member API from Parsec — 2 operation(s) for member.
  name: Parsec Member API
  slug: parsec-member-api
- description: The Member Invite API from Parsec — 3 operation(s) for member invite.
  name: Parsec Member Invite API
  slug: parsec-member-invite-api
- description: The Relay API from Parsec — 2 operation(s) for relay.
  name: Parsec Relay API
  slug: parsec-relay-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Parsec Teams App Rule API
  slug: open-parsec-app-rule-api
- collection_type: open
  name: Parsec Teams App Rule Audit Log API
  slug: open-parsec-audit-log-api
- collection_type: open
  name: Parsec Teams App Rule Group API
  slug: open-parsec-group-api
- collection_type: open
  name: Parsec Teams App Rule Guest Access Invite API
  slug: open-parsec-guest-access-invite-api
- collection_type: open
  name: Parsec Teams App Rule Machine API
  slug: open-parsec-machine-api
- collection_type: open
  name: Parsec Teams App Rule Member API
  slug: open-parsec-member-api
- collection_type: open
  name: Parsec Teams App Rule Member Invite API
  slug: open-parsec-member-invite-api
- collection_type: open
  name: Parsec Teams App Rule Relay API
  slug: open-parsec-relay-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://parsec.app/docs/teams-api
- group: docs
  title: ''
  type: Documentation
  url: https://parsec.app/docs/teams-api
- group: docs
  title: ''
  type: APIReference
  url: https://parsec.app/docs/teams-api
- group: operate
  title: ''
  type: Support
  url: https://support.parsec.app
- group: company
  title: ''
  type: Blog
  url: https://parsec.app/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/parsec-cloud
- group: commercial
  title: ''
  type: Pricing
  url: https://parsec.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dash.parsec.app/signup
- group: start
  title: ''
  type: Login
  url: https://dash.parsec.app/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parsec.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unity.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.parsec.app
- group: operate
  title: ''
  type: ChangeLog
  url: https://parsec.app/changelog
- group: auth
  title: ''
  type: Security
  url: https://parsec.app/security
- group: auth
  title: ''
  type: Compliance
  url: https://parsec.app/security
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/parsec-teams-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parsec-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parsec-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/parsec-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/parsec-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parsec-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://parsec.app/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/parsec-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://parsec.app/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/parsec-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parsec-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/parsec-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/parsec-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parsec-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/parsec-teams-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parsec-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/parsec-changelog.yml
created: '2026-07-17'
description: Parsec is a high-performance, low-latency remote desktop and interactive video streaming product, now a Unity company, used to access graphics-intensive and latency-sensitive applications from anywhere across any device. Its peer-to-peer architecture streams in silky-smooth high definition and is used by game studios (EA, Ubisoft, Blizzard, Square Enix), film/TV, animation, broadcast and architecture teams. Parsec for Teams adds organization-wide administration, and the Parsec for Teams API exposes that admin surface — managing members, groups, team machines (computers), time-limited guest access, application rules, relays, and the team audit log — authenticated with an API key presented as an HTTP Bearer token and governed by a granular team permission model.
image: https://parsec.app/_next/static/media/opengraph.60ec26bf.png
layout: provider
mcp_servers:
- description: ''
  name: parsec-mcp.yml
  slug: parsec-mcpyml
modified: '2026-07-20'
name: Parsec
nav: Providers
network: true
overview: 'Parsec publishes 8 APIs on the [APIs.io](https://apis.io/) network, including App Rule API, Audit Log API, Group API, and 5 more. Tagged areas include Company, Remote Desktop, Cloud Gaming, Streaming, and Virtual Desktop.


  Parsec''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, changelog, and 26 more developer resources.'
random_paper: 42
rate_limits:
- limit_count: 1
  name: Parsec Rate Limits
  slug: parsec-rate-limits
score:
  band: strong
  composite: 54.8
  delta: -1.8
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 55.9
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 57.9
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parsec/refs/heads/main/screenshots/parsec-2026-08-07T191456.png
security:
- kind: authentication
  name: Parsec Authentication
  slug: parsec-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Parsec Domain Security
  slug: parsec-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Parsec Vulnerability Disclosure
  slug: parsec-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Parsec Trust Center
  slug: parsec-trust-center
  summary_line: SOC 2 Type 2
slug: parsec
tags:
- Company
- Remote Desktop
- Cloud Gaming
- Streaming
- Virtual Desktop
- Team Management
- Developer Tools
- Gaming
website: https://parsec.app/docs/teams-api
---

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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.3
  scored_at: '2026-07-28'
api_count: 22
apis:
- description: Operations related to access rules
  name: Opal Security access-rules API
  slug: opal-security-access-rules-api
- description: Operations related to apps
  name: Opal Security apps API
  slug: opal-security-apps-api
- description: Operations related to bundles
  name: Opal Security bundles API
  slug: opal-security-bundles-api
- description: Operations related to configuration templates
  name: Opal Security configuration-templates API
  slug: opal-security-configuration-templates-api
- description: Operations related to request reviewer delegations
  name: Opal Security delegations API
  slug: opal-security-delegations-api
- description: Operations related to event streaming connections
  name: Opal Security event-streams API
  slug: opal-security-event-streams-api
- description: Operations related to events
  name: Opal Security events API
  slug: opal-security-events-api
- description: Operations related to group bindings
  name: Opal Security group-bindings API
  slug: opal-security-group-bindings-api
- description: Operations related to groups
  name: Opal Security groups API
  slug: opal-security-groups-api
- description: Operations related to IDP group mappings
  name: Opal Security idp-group-mappings API
  slug: opal-security-idp-group-mappings-api
- description: Operations related to message channels
  name: Opal Security message-channels API
  slug: opal-security-message-channels-api
- description: Operations related to non-human identities
  name: Opal Security non-human-identities API
  slug: opal-security-non-human-identities-api
- description: Operations related to on-call schedules
  name: Opal Security on-call-schedules API
  slug: opal-security-on-call-schedules-api
- description: Operations related to OpalQuery
  name: Opal Security opal-queries API
  slug: opal-security-opal-queries-api
- description: Operations related to owners
  name: Opal Security owners API
  slug: opal-security-owners-api
- description: Operations related to requests
  name: Opal Security requests API
  slug: opal-security-requests-api
- description: Operations related to resources
  name: Opal Security resources API
  slug: opal-security-resources-api
- description: Operations related to sessions
  name: Opal Security sessions API
  slug: opal-security-sessions-api
- description: Operations related to tags
  name: Opal Security tags API
  slug: opal-security-tags-api
- description: Operations related to API tokens
  name: Opal Security tokens API
  slug: opal-security-tokens-api
- description: Operations related to UARs
  name: Opal Security uars API
  slug: opal-security-uars-api
- description: Operations related to users
  name: Opal Security users API
  slug: opal-security-users-api
artifact_total: 28
asyncapis:
- description: ''
  name: Opal Security Events Webhooks
  slug: opal-security-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opal-security-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opal-security-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opal-security-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/opal-security-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/opal-security-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opal-security-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/opal-security-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opal-security-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opal-security-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.opal.dev/
- group: design
  title: ''
  type: Conformance
  url: conformance/opal-security-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/opal-security-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/opal-security-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/opal-security-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/opal-security-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://opal.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.opal.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opal.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.opal.dev/api-reference/access-rules/get-access-rules
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.opal.dev/
- group: operate
  title: ''
  type: Changelog
  url: https://docs.opal.dev/changelog/changelog
- group: company
  title: ''
  type: Blog
  url: https://opal.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://opal.dev/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opalsecurity
- group: start
  title: ''
  type: SignUp
  url: https://app.opal.dev/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opal.dev/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opal.dev/privacy-policy
created: '2026-07-17'
description: 'Opal Security (legal entity Perma Security, Inc.) is a next-generation access management and identity security platform that gives enterprises comprehensive visibility into access across their systems, orchestrates just-in-time and least-privilege access, designs intelligent access policies, and automates user access reviews (UARs). Opal exposes a RESTful API at https://api.opal.dev/v1 covering apps, resources, groups, users, bundles, access requests, access rules, owners, events, event streaming, sessions, and tokens, plus official SDKs (Python, Go), a CLI, a Terraform provider, and three hosted Model Context Protocol (MCP) servers for AI agents. Backed by Greylock. Sector: cybersecurity.'
image: https://framerusercontent.com/images/HHjnsz66kJwSMAe0rpzp3eREB2k.png
layout: provider
mcp_servers:
- description: ''
  name: opal-security-mcp.yml
  slug: opal-security-mcpyml
modified: '2026-07-20'
name: Opal Security
nav: Providers
network: true
overview: 'Opal Security publishes 22 APIs on the [APIs.io](https://apis.io/) network, including access-rules API, apps API, bundles API, and 19 more. Tagged areas include Company, Cybersecurity, Access Management, Identity and Access Management, and Least Privilege.


  The Opal Security catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Opal Security''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, engineering blog, and 21 more developer resources.'
random_paper: 49
score:
  band: strong
  composite: 59.6
  delta: -0.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 66.4
    developer_ergonomics: 76.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 59.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: unknown
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Opal Security Authentication
  slug: opal-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opal Security Domain Security
  slug: opal-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opal Security Vulnerability Disclosure
  slug: opal-security-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Opal Security Trust Center
  slug: opal-security-trust-center
  summary_line: trust center published
slug: opal-security
tags:
- Company
- Cybersecurity
- Access Management
- Identity and Access Management
- Least Privilege
- Access Reviews
- Security
website: https://opal.dev/
---

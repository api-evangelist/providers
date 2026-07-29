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
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Fleet Agentic Access
  operation_count: 4
  slug: fleet-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: The Fleet API from Fleet — 2 operation(s) for fleet.
  name: Fleet Fleet API
  slug: fleet-fleet-api
artifact_total: 7
asyncapis:
- description: ''
  name: Fleet Webhooks
  slug: fleet-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://fleetdm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fleetdm.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://fleetdm.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://fleetdm.com/docs/rest-api/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://fleetdm.com/docs/get-started/anatomy
- group: operate
  title: ''
  type: Support
  url: https://fleetdm.com/support
- group: company
  title: ''
  type: Blog
  url: https://fleetdm.com/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fleetdm
- group: commercial
  title: ''
  type: Pricing
  url: https://fleetdm.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://fleetdm.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fleetdm.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fleetdm.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fleetdm.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fleet-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fleet-lifecycle.yml
- group: build
  title: ''
  type: CLI
  url: cli/fleet-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/fleet-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fleet-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fleet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fleet-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fleet-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fleet-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fleetdm.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/fleet-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fleet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/fleetdm/fleet/blob/main/SECURITY.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fleet-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fleet-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fleet-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fleet-premium-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fleet-llms.txt
created: '2026-07-17'
description: Fleet is an open-source device management platform built on osquery. It provides cross-platform MDM, endpoint telemetry, vulnerability and patch management, software inventory, and GitOps-driven configuration for macOS, Windows, Linux, iOS, and Android fleets. Fleet exposes a versioned REST API (/api/v1/fleet, bearer-token auth), the fleetctl CLI for live queries and config-as-code, and outbound webhook automations. It is developed in the open at github.com/fleetdm/fleet and backed by CRV.
image: https://avatars.githubusercontent.com/u/70264713?v=4
layout: provider
modified: '2026-07-19'
name: Fleet
nav: Providers
network: true
overview: 'Fleet publishes 1 API on the [APIs.io](https://apis.io/) network: Fleet API. Tagged areas include Company, Developer Tools, Device Management, MDM, and Endpoint Security.


  The Fleet catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fleet''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 54
score:
  band: developing
  composite: 54.8
  delta: 1.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 49.2
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fleet/refs/heads/main/screenshots/fleet-2026-07-25T214732.png
security:
- kind: authentication
  name: Fleet Authentication
  slug: fleet-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Fleet Domain Security
  slug: fleet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fleet Vulnerability Disclosure
  slug: fleet-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Fleet Trust Center
  slug: fleet-trust-center
  summary_line: SOC 2 Type 2, ISO 27001
slug: fleet
tags:
- Company
- Developer Tools
- Device Management
- MDM
- Endpoint Security
- Vulnerability Management
- osquery
- Open Source
- DevOps
website: https://fleetdm.com/
---

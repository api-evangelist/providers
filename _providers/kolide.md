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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.5
  scored_at: '2026-08-11'
api_count: 17
apis:
- description: The Admin Users API from Kolide — 2 operation(s) for admin users.
  name: Kolide Admin Users API
  slug: kolide-admin-users-api
- description: The Audit Logs API from Kolide — 2 operation(s) for audit logs.
  name: Kolide Audit Logs API
  slug: kolide-audit-logs-api
- description: The Auth Logs API from Kolide — 2 operation(s) for auth logs.
  name: Kolide Auth Logs API
  slug: kolide-auth-logs-api
- description: The Checks API from Kolide — 5 operation(s) for checks.
  name: Kolide Checks API
  slug: kolide-checks-api
- description: The Custom Check Drafts API from Kolide — 2 operation(s) for custom check drafts.
  name: Kolide Custom Check Drafts API
  slug: kolide-custom-check-drafts-api
- description: The Deprovisioned People API from Kolide — 1 operation(s) for deprovisioned people.
  name: Kolide Deprovisioned People API
  slug: kolide-deprovisioned-people-api
- description: The Device Groups API from Kolide — 5 operation(s) for device groups.
  name: Kolide Device Groups API
  slug: kolide-device-groups-api
- description: The Devices API from Kolide — 7 operation(s) for devices.
  name: Kolide Devices API
  slug: kolide-devices-api
- description: The Exemption Requests API from Kolide — 2 operation(s) for exemption requests.
  name: Kolide Exemption Requests API
  slug: kolide-exemption-requests-api
- description: The Issues API from Kolide — 2 operation(s) for issues.
  name: Kolide Issues API
  slug: kolide-issues-api
- description: The Live Query Campaigns API from Kolide — 3 operation(s) for live query campaigns.
  name: Kolide Live Query Campaigns API
  slug: kolide-live-query-campaigns-api
- description: The Packages API from Kolide — 2 operation(s) for packages.
  name: Kolide Packages API
  slug: kolide-packages-api
- description: The People API from Kolide — 5 operation(s) for people.
  name: Kolide People API
  slug: kolide-people-api
- description: The Person Groups API from Kolide — 3 operation(s) for person groups.
  name: Kolide Person Groups API
  slug: kolide-person-groups-api
- description: The Registration Requests API from Kolide — 2 operation(s) for registration requests.
  name: Kolide Registration Requests API
  slug: kolide-registration-requests-api
- description: The Reporting API from Kolide — 6 operation(s) for reporting.
  name: Kolide Reporting API
  slug: kolide-reporting-api
- description: The Whoami API from Kolide — 1 operation(s) for whoami.
  name: Kolide Whoami API
  slug: kolide-whoami-api
artifact_total: 23
asyncapis:
- description: ''
  name: Kolide Events
  slug: kolide-events
common:
- group: company
  title: ''
  type: Website
  url: https://kolide.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.kolide.com/docs/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.kolide.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://kolideapi.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kolide.com/docs/developers/usecases
- group: operate
  title: ''
  type: Support
  url: https://www.kolide.com/docs/about-kolide/support
- group: company
  title: ''
  type: Blog
  url: https://www.kolide.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kolide
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kolide.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.kolide.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kolide.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kolide.com/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/kolide-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kolide-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kolide-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kolide-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kolide-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.1password.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kolide-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kolide-events.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kolide-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/kolide-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kolide-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kolide-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/kolide-conformance.yml
- group: auth
  title: ''
  type: Security
  url: security/kolide-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kolide-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kolide-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kolide-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kolide-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/kolide-k2-overlay.yaml
created: '2026-07-17'
description: 'Kolide is a device trust and endpoint security platform, now part of 1Password Extended Access Management. It enforces Zero Trust access by blocking non-compliant devices from authenticating into corporate applications through Okta, Google Workspace or Microsoft Entra, runs continuous security and compliance checks across Linux, macOS, Windows, iOS and Android endpoints, and maintains fleet-wide device inventory built on thousands of osquery-sourced data points. Its distinguishing philosophy is user-first remediation: rather than silently denying access, Kolide educates the end user about the specific problem on their device and guides them through fixing it themselves, cutting helpdesk load. The public developer surface is the K2 API at api.kolide.com — 65 REST operations across devices, people, groups, security checks, compliance issues, live osquery campaigns, approval queues, reporting tables and audit logs — published as OpenAPI 3.0 on dated version lines, with HMAC-signed
  webhooks, an OpenID Shared Signals Framework (CAEP) event stream, and a first-party MCP server.'
image: https://www.kolide.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: kolide-mcp.yml
  slug: kolide-mcpyml
modified: '2026-07-19'
name: Kolide
nav: Providers
network: true
overview: 'Kolide publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Admin Users API, Audit Logs API, Auth Logs API, and 14 more. Tagged areas include Company, B2B, Security, Device Trust, and Endpoint Security.


  The Kolide catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kolide''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
random_paper: 52
score:
  band: strong
  composite: 58.1
  delta: -1.7
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.7
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 59.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kolide/refs/heads/main/screenshots/kolide-2026-07-25T224129.png
security:
- kind: authentication
  name: Kolide Authentication
  slug: kolide-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kolide Domain Security
  slug: kolide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kolide Vulnerability Disclosure
  slug: kolide-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Kolide Trust Center
  slug: kolide-trust-center
  summary_line: SOC 2 Type II, GDPR
slug: kolide
tags:
- Company
- B2B
- Security
- Device Trust
- Endpoint Security
- Zero Trust
- Compliance
- Identity
- osquery
- Device Management
website: https://kolide.com
---

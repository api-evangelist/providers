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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Sublime Security Agentic Access
  operation_count: 91
  slug: sublime-security-agentic-access
  summary_line: 91 operations · 48 acting
api_count: 16
apis:
- description: The BinExplode API from Sublime Security — 2 operation(s) for binexplode.
  name: Sublime Security BinExplode API
  slug: sublime-security-binexplode-api
- description: The Email Bombs API from Sublime Security — 3 operation(s) for email bombs.
  name: Sublime Security Email Bombs API
  slug: sublime-security-email-bombs-api
- description: The Enrichment API from Sublime Security — 1 operation(s) for enrichment.
  name: Sublime Security Enrichment API
  slug: sublime-security-enrichment-api
- description: The Events in the audit log API from Sublime Security — 3 operation(s) for events in the audit log.
  name: Sublime Security Events in the audit log API
  slug: sublime-security-events-in-the-audit-log-api
- description: The Hunt Jobs API from Sublime Security — 3 operation(s) for hunt jobs.
  name: Sublime Security Hunt Jobs API
  slug: sublime-security-hunt-jobs-api
- description: The Lists API from Sublime Security — 4 operation(s) for lists.
  name: Sublime Security Lists API
  slug: sublime-security-lists-api
- description: The Live flow API from Sublime Security — 1 operation(s) for live flow.
  name: Sublime Security Live flow API
  slug: sublime-security-live-flow-api
- description: The Mailboxes API from Sublime Security — 1 operation(s) for mailboxes.
  name: Sublime Security Mailboxes API
  slug: sublime-security-mailboxes-api
- description: The Message Groups API from Sublime Security — 17 operation(s) for message groups.
  name: Sublime Security Message Groups API
  slug: sublime-security-message-groups-api
- description: The Messages API from Sublime Security — 19 operation(s) for messages.
  name: Sublime Security Messages API
  slug: sublime-security-messages-api
- description: The Organizations API from Sublime Security — 4 operation(s) for organizations.
  name: Sublime Security Organizations API
  slug: sublime-security-organizations-api
- description: The Roles API from Sublime Security — 1 operation(s) for roles.
  name: Sublime Security Roles API
  slug: sublime-security-roles-api
- description: The Rules API from Sublime Security — 7 operation(s) for rules.
  name: Sublime Security Rules API
  slug: sublime-security-rules-api
- description: The SCIM API from Sublime Security — 8 operation(s) for scim.
  name: Sublime Security SCIM API
  slug: sublime-security-scim-api
- description: The Tasks API from Sublime Security — 1 operation(s) for tasks.
  name: Sublime Security Tasks API
  slug: sublime-security-tasks-api
- description: The User Reports API from Sublime Security — 1 operation(s) for user reports.
  name: Sublime Security User Reports API
  slug: sublime-security-user-reports-api
artifact_total: 22
asyncapis:
- description: ''
  name: Sublime Security Webhooks
  slug: sublime-security-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://sublime.security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sublime.security/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sublime.security/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sublime.security/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sublime.security/docs/sublime-managed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sublime-security
- group: start
  title: ''
  type: SignUp
  url: https://platform.sublime.security/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://statuspage.incident.io/sublime/customer
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sublime.security/
- group: auth
  title: ''
  type: Authentication
  url: authentication/sublime-security-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sublime-security-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sublime-security-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/sublime-security-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sublime-security-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sublime-security-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sublime-security-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sublime-security-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/sublime-security-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sublime-security-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sublime-security-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sublime-security-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sublime-security-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sublime-security-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sublime-security-platform-overlay.yaml
created: '2026-07-17'
description: Sublime Security is an adaptive, programmable email security platform that combines best-in-class detection effectiveness with deep visibility and control. Teams write detection-as-code in Sublime's Message Query Language (MQL) to stop business email compromise (BEC), credential phishing, malware, and other email attacks, and can hunt retroactively across historical messages. Sublime runs as a managed multi-region cloud service or self-managed on Docker, AWS, or Azure, integrates with Microsoft 365, Google Workspace, and IMAP, and exposes a REST Platform API (v0), outbound webhooks, SCIM 2.0 provisioning, a Multi-Tenancy API for MSPs, and a free Analysis API with an open rules community. Backed by Index Ventures and IVP.
image: https://platform.sublime.security/logo@192.png
layout: provider
mcp_servers:
- description: ''
  name: sublime-security-mcp.yml
  slug: sublime-security-mcpyml
modified: '2026-07-21'
name: Sublime Security
nav: Providers
network: true
overview: 'Sublime Security publishes 16 APIs on the [APIs.io](https://apis.io/) network, including BinExplode API, Email Bombs API, Enrichment API, and 13 more. Tagged areas include Company, Security, Email Security, Phishing, and Detection as Code.


  The Sublime Security catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sublime Security''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, CLI, and 19 more developer resources.'
random_paper: 27
score:
  band: developing
  composite: 44.6
  delta: -3.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 58.2
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sublime Security Authentication
  slug: sublime-security-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sublime Security Domain Security
  slug: sublime-security-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Sublime Security Trust Center
  slug: sublime-security-trust-center
  summary_line: trust center published
slug: sublime-security
tags:
- Company
- Security
- Email Security
- Phishing
- Detection as Code
- Threat Detection
- Cloud Email Security
- SCIM
website: https://sublime.security/
---

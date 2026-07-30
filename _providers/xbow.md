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
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 21
  human_in_the_loop: 1
  name: Xbow Agentic Access
  operation_count: 40
  slug: xbow-agentic-access
  summary_line: 40 operations · 21 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Endpoints related to assessments for assets. All endpoints require an _organization_ API key.
  name: Xbow Assessments API
  slug: xbow-assessments-api
- description: Endpoints related to assets within an organization. All endpoints require an _organization_ API key.
  name: Xbow Assets API
  slug: xbow-assets-api
- description: Endpoints for viewing and managing findings. All endpoints require an _organization_ API key.
  name: Xbow Findings API
  slug: xbow-findings-api
- description: Endpoints related to Lightspeed assessment requests.
  name: Xbow Lightspeed API
  slug: xbow-lightspeed-api
- description: Instance metadata endpoints.
  name: Xbow Meta API
  slug: xbow-meta-api
- description: Endpoints related to organizations and their management.
  name: Xbow Organizations API
  slug: xbow-organizations-api
- description: Endpoints for downloading and viewing reports. All endpoints require an _organization_ API key.
  name: Xbow Reports API
  slug: xbow-reports-api
- description: 'Upload and manage files used in assessments, such as source code archives. All endpoints require an _organization_ API key. ## Upload flow Resources use a multipart S3 upload. The full flow is: 1. **C'
  name: Xbow Resources API
  slug: xbow-resources-api
- description: Manage webhook subscriptions and receive event notifications. When creating an organization, you may provide an HTTPS webhook URL to receive events related to the organization's resources. We implemen
  name: Xbow Webhooks API
  slug: xbow-webhooks-api
artifact_total: 16
asyncapis:
- description: ''
  name: Xbow Webhooks
  slug: xbow-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xbow-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/xbow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xbow-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xbow-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://xbow.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.xbow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.xbow.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.xbow.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.xbow.com/console/get-started/introduction/
- group: operate
  title: ''
  type: Support
  url: mailto:support@xbow.com
- group: company
  title: ''
  type: Blog
  url: https://xbow.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xbow-engineering
- group: commercial
  title: ''
  type: Pricing
  url: https://xbow.com/pricing
- group: start
  title: ''
  type: Login
  url: https://console.xbow.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xbow.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xbow.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xbow.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.xbow.com/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.xbow.com/console/get-started/trust-and-safety/
- group: auth
  title: ''
  type: Security
  url: https://xbow.com/security-policy
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.xbow.com/api/#description/version-lifecycle
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xbow-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/xbow-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/xbow-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/xbow-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xbow-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xbow-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xbow-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xbow-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/xbow-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'XBOW is an autonomous offensive security platform that uses AI to perform penetration testing with real exploit validation — it identifies vulnerabilities, chains them into attack paths, and proves exploitability before findings reach security teams. The XBOW API (public preview) exposes the full platform workflow: register assets, launch and manage assessments, fetch validated findings and reports, upload source-code resources for gray-box testing, and subscribe webhooks with Ed25519-signed deliveries. XBOW has ranked #1 on the HackerOne and Microsoft MSRC leaderboards and is used by 150+ security teams.'
image: https://docs.xbow.com/xbow-logomark.svg
layout: provider
mcp_servers:
- description: ''
  name: xbow-mcp.yml
  slug: xbow-mcpyml
modified: '2026-07-21'
name: Xbow
nav: Providers
network: true
overview: 'Xbow publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Assessments API, Assets API, Findings API, and 6 more. Tagged areas include Security, Penetration Testing, Offensive Security, Artificial Intelligence, and Vulnerability Management.


  The Xbow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Xbow''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 24 more developer resources.'
random_paper: 38
score:
  band: strong
  composite: 57.6
  delta: -1.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.9
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 63.2
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Xbow Authentication
  slug: xbow-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Xbow Domain Security
  slug: xbow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Xbow Vulnerability Disclosure
  slug: xbow-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Xbow Trust Center
  slug: xbow-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, GDPR, HIPAA
slug: xbow
tags:
- Security
- Penetration Testing
- Offensive Security
- Artificial Intelligence
- Vulnerability Management
- Cybersecurity
- Application Security
website: https://xbow.com
---

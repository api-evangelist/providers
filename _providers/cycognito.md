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
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Cycognito Agentic Access
  operation_count: 43
  slug: cycognito-agentic-access
  summary_line: 43 operations · 31 acting
api_count: 12
apis:
- description: The Assets API from CyCognito — 6 operation(s) for assets.
  name: CyCognito Assets API
  slug: cycognito-assets-api
- description: The Audit Logs API from CyCognito — 1 operation(s) for audit logs.
  name: CyCognito Audit Logs API
  slug: cycognito-audit-logs-api
- description: The Cloud Connectors API from CyCognito — 4 operation(s) for cloud connectors.
  name: CyCognito Cloud Connectors API
  slug: cycognito-cloud-connectors-api
- description: The Export Data API from CyCognito — 6 operation(s) for export data.
  name: CyCognito Export Data API
  slug: cycognito-export-data-api
- description: The Issues API from CyCognito — 9 operation(s) for issues.
  name: CyCognito Issues API
  slug: cycognito-issues-api
- description: The Organizations API from CyCognito — 2 operation(s) for organizations.
  name: CyCognito Organizations API
  slug: cycognito-organizations-api
- description: The Realm API from CyCognito — 2 operation(s) for realm.
  name: CyCognito Realm API
  slug: cycognito-realm-api
- description: The Reports API from CyCognito — 2 operation(s) for reports.
  name: CyCognito Reports API
  slug: cycognito-reports-api
- description: The Revalidation API from CyCognito — 1 operation(s) for revalidation.
  name: CyCognito Revalidation API
  slug: cycognito-revalidation-api
- description: The Scope Management API from CyCognito — 1 operation(s) for scope management.
  name: CyCognito Scope Management API
  slug: cycognito-scope-management-api
- description: The Users API from CyCognito — 2 operation(s) for users.
  name: CyCognito Users API
  slug: cycognito-users-api
- description: The Verify IPs API from CyCognito — 1 operation(s) for verify ips.
  name: CyCognito Verify IPs API
  slug: cycognito-verify-ips-api
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.cycognito.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.platform.cycognito.com/v1/docs/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://api.platform.cycognito.com/v1/docs/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.platform.cycognito.com/v1/docs/index.html
- group: start
  title: ''
  type: SignUp
  url: https://www.cycognito.com/demo
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cycognito.com/platform/pricing.php
- group: company
  title: ''
  type: Blog
  url: https://www.cycognito.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cycognito.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cycognito.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CyCognito
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/joint-operations-participant-24342014/workspace/cycognito
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cycognito-v1-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/cycognito-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cycognito-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cycognito-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cycognito-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/cycognito-v1-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/cycognito-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cycognito.com/company/trust.php
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cycognito-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cycognito-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cycognito-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cycognito-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cycognito-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cycognito-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cycognito-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/cycognito-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cycognito-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cycognito-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: CyCognito is a cybersecurity company providing an external attack surface management (EASM) and exposure management platform. Its cloud-native platform continuously discovers, maps, and tests an organization's internet-exposed assets—domains, IPs, web apps, APIs, and cloud environments—to surface and validate critical exposures before attackers exploit them. The CyCognito API V1 is a REST API (API-key authenticated) that lets you query assets and issues, manage attack-surface scope, attribute assets to organizations, manage users and cloud connectors, run exports and executive reports, and verify the identity of scanner IPs. CyCognito is backed by Accel and Lightspeed Venture Partners.
image: https://www.cycognito.com/images/social/banner-homepage-2400x1256-email.png
layout: provider
mcp_servers:
- description: ''
  name: cycognito-mcp.yml
  slug: cycognito-mcpyml
modified: '2026-07-18'
name: CyCognito
nav: Providers
network: true
overview: 'CyCognito publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Audit Logs API, Cloud Connectors API, and 9 more. Tagged areas include Company, Cybersecurity, Attack Surface Management, Exposure Management, and Security.


  CyCognito''s developer surface includes documentation, API reference, signup flow, pricing, engineering blog, authentication, and 24 more developer resources.'
random_paper: 25
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.9
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cycognito/refs/heads/main/screenshots/cycognito-2026-07-25T211040.png
security:
- kind: authentication
  name: Cycognito Authentication
  slug: cycognito-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cycognito Domain Security
  slug: cycognito-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cycognito Vulnerability Disclosure
  slug: cycognito-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Cycognito Trust Center
  slug: cycognito-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, GDPR
slug: cycognito
tags:
- Company
- Cybersecurity
- Attack Surface Management
- Exposure Management
- Security
- Vulnerability Management
- Cloud Security
- API Security
website: https://www.cycognito.com/
---

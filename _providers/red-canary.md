---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Tenant-scoped REST API over the Red Canary portal. Documented resources include detections, threats, events, endpoints, endpoint_users, identities, investigations and audit_logs. Requests carry a per-
  name: Red Canary REST API v3
  slug: red-canary-rest-api-v3
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://redcanary.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.redcanary.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.redcanary.com/docs/red-canary-getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://go.my.redcanary.co/openapi/v3/docs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.redcanary.com/docs/red-canary-rest-api
- group: operate
  title: ''
  type: Support
  url: https://support.redcanary.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.redcanary.com/docs/getting-help
- group: company
  title: ''
  type: Blog
  url: https://redcanary.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redcanaryco
- group: start
  title: ''
  type: Login
  url: https://go.my.redcanary.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redcanary.com/license-agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redcanary.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redcanary.com/
- group: auth
  title: ''
  type: Security
  url: https://redcanary.com/responsible-disclosure/
- group: auth
  title: ''
  type: TrustCenter
  url: security/red-canary-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://redcanary.com/trust-center/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.redcanary.com/docs/red-canary-release-notes
- group: build
  title: ''
  type: Packages
  url: packages/red-canary-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/red-canary-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/red-canary-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/red-canary-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/red-canary-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/red-canary-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/red-canary-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/red-canary-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.redcanary.com/docs/red-canary-release-stages
- group: design
  title: ''
  type: Conformance
  url: conformance/red-canary-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/red-canary-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/red-canary-vulnerability-disclosure.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/red-canary-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/red-canary-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/red-canary-changelog.yml
created: '2026-08-05'
description: Red Canary is a Managed Detection and Response (MDR) provider that monitors endpoint, identity, cloud, email and network telemetry on behalf of its customers, confirms threats with a 24x7 human and AI detection engineering team, and drives containment through automation playbooks and response actions across partner platforms such as Microsoft Defender, CrowdStrike Falcon, SentinelOne, Palo Alto Cortex, Carbon Black and Zscaler. The company also publishes widely used open-source security research including Atomic Red Team, Chain Reactor, Surveyor and the annual Threat Detection Report. Red Canary was acquired by Zscaler in 2025. It operates a tenant-scoped REST API (openapi/v3) over detections, threats, events, endpoints, endpoint users, identities, investigations and audit logs, authenticated with a per-user X-Api-Key token; the Swagger/OpenAPI reference for that API is served inside the customer portal and is not reachable without a tenant subdomain and login.
image: https://redcanary.com/wp-content/uploads/2025/08/Open-Graph-2025-1200x628-1.jpg
layout: provider
modified: '2026-08-05'
name: Red Canary
nav: Providers
network: true
overview: 'Red Canary publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Managed Detection and Response, and Threat Detection.


  Red Canary''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 25 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 40.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 40.4
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Red Canary Authentication
  slug: red-canary-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Red Canary Domain Security
  slug: red-canary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Red Canary Vulnerability Disclosure
  slug: red-canary-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Red Canary Trust Center
  slug: red-canary-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2013, ISO 27701, JOSCAR, EU-U.S. Data Privacy Framework, UK Extension to the EU-U.S. Data Privacy Framework, Swiss-U.S. Data Privacy Framework
slug: red-canary
tags:
- Company
- Security
- Cybersecurity
- Managed Detection and Response
- Threat Detection
- Threat Intelligence
- Endpoint Security
- Incident Response
- Security Operations
- Automation
website: https://redcanary.com/
---

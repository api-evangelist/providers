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
    asyncapi_events: false
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
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Tessian Agentic Access
  operation_count: 13
  slug: tessian-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 10
apis:
- description: 'Endpoints in this section detail anomalous user activity that has been detected by the system, where anomalous activity is defined as users sending unusual numbers of sensitive emails to unauthorized '
  name: Tessian Anomalies API
  slug: tessian-anomalies-api
- description: Endpoints in this section allow you to access audit information of usage and changes made to your Tessian Products.
  name: Tessian Audits API
  slug: tessian-audits-api
- description: The Beta Endpoints API from Tessian — 1 operation(s) for beta endpoints.
  name: Tessian Beta Endpoints API
  slug: tessian-beta-endpoints-api
- description: '**⚠️ These endpoints are marked as deprecated and will be going away soon.** You should look to migrate away from using the endpoints in this section as they are no longer maintained. Timelines for re'
  name: Tessian Deprecated API
  slug: tessian-deprecated-api
- description: The Endpoints API from Tessian — 9 operation(s) for endpoints.
  name: Tessian Endpoints API
  slug: tessian-endpoints-api
- description: Endpoints in this section allow you to access security events from Tessian.
  name: Tessian Events API
  slug: tessian-events-api
- description: Groups are named collections of email addresses; their members may be specified either by specific address, or by a wildcard including all addresses in an entire domain.
  name: Tessian Groups API
  slug: tessian-groups-api
- description: Endpoints in this section provide ways to monitor information in Tessian.
  name: Tessian Monitoring API
  slug: tessian-monitoring-api
- description: Endpoints in this section expose risk drivers, which are the underlying components for the Tessian combined Risk Score.
  name: Tessian Risk API
  slug: tessian-risk-api
- description: The Triggers API from Tessian — 1 operation(s) for triggers.
  name: Tessian Triggers API
  slug: tessian-triggers-api
artifact_total: 14
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tessian.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tessian.com/documentation/api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.tessian.com/documentation/api/index.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/tessian-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tessian-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tessian-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tessian-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tessian-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tessian-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tessian-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tessian-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/tessian-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tessian-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tessian-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tessian
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.proofpoint.com/us/legal/api-terms-of-use
- group: operate
  title: ''
  type: Support
  url: mailto:support@tessian.com
- group: company
  title: ''
  type: Website
  url: https://www.tessian.com
created: '2026-07-17'
description: Tessian, now part of Proofpoint, is an AI-powered email security platform that protects against inbound threats (phishing and impersonation), accidental data loss, and deliberate data exfiltration across its Defender, Guardian, Enforcer, Architect, and Constructor modules. The Tessian API is a RESTful, JSON, read-oriented interface that exports security-event, anomaly, company-risk, user-monitoring, audit-log, and trigger data into SIEMs and other data-management tools. It authenticates with a static API token, paginates by checkpoint, and returns ISO 8601 UTC timestamps.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tessian.png
layout: provider
mcp_servers:
- description: ''
  name: tessian-mcp.yml
  slug: tessian-mcpyml
modified: '2026-07-21'
name: Tessian
nav: Providers
network: true
overview: 'Tessian publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Anomalies API, Audits API, Beta Endpoints API, and 7 more. Tagged areas include Company, Enterprise, Email Security, Cybersecurity, and Data Loss Prevention.


  Tessian''s developer surface includes documentation, API reference, authentication, support, and 15 more developer resources.'
random_paper: 39
score:
  band: thin
  composite: 34.4
  delta: -2.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 49.6
    developer_ergonomics: 42.9
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tessian Authentication
  slug: tessian-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tessian Domain Security
  slug: tessian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tessian
tags:
- Company
- Enterprise
- Email Security
- Cybersecurity
- Data Loss Prevention
- SIEM
- Security
- Phishing
website: https://www.tessian.com
---

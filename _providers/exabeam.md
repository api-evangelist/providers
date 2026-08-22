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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-19'
api_count: 13
apis:
- description: Manage users, roles, and permissions within the Exabeam platform.
  name: Exabeam Access Control API
  slug: exabeam-access-control-api
- description: Retrieve audit-trail and activity-log records from the platform.
  name: Exabeam Audit API
  slug: exabeam-audit-api
- description: OAuth2 token issuance and API key / secret authentication for the Exabeam API surface.
  name: Exabeam Authentication API
  slug: exabeam-authentication-api
- description: Configure and manage cloud-based log collectors.
  name: Exabeam Cloud Collectors API
  slug: exabeam-cloud-collectors-api
- description: Manage context tables and enrichment data used for detection and investigation.
  name: Exabeam Context Management API
  slug: exabeam-context-management-api
- description: Create and manage correlation rules for threat detection.
  name: Exabeam Correlation Rules API
  slug: exabeam-correlation-rules-api
- description: Manage detection rules and security content.
  name: Exabeam Detection Management API
  slug: exabeam-detection-management-api
- description: Access MITRE ATT&CK technique and tactic mappings within the platform.
  name: Exabeam MITRE ATT&CK API
  slug: exabeam-mitre-attck-api
- description: Search ingested log and event data across the platform.
  name: Exabeam Search API
  slug: exabeam-search-api
- description: Retrieve service-health status and data-consumption metrics.
  name: Exabeam Service Health and Consumption API
  slug: exabeam-service-health-and-consumption-api
- description: Configure and manage on-premises / site log collectors.
  name: Exabeam Site Collectors API
  slug: exabeam-site-collectors-api
- description: Manage cases, alerts, and investigations in Exabeam Threat Center.
  name: Exabeam Threat Center API
  slug: exabeam-threat-center-api
- description: Manage security use cases and their associated detection content.
  name: Exabeam Use Cases API
  slug: exabeam-use-cases-api
artifact_total: 19
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/exabeam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.exabeam.com/responsible-disclosure/
- group: company
  title: ''
  type: Website
  url: https://exabeam.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.exabeam.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.exabeam.com/exabeam/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.exabeam.com/exabeam/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.exabeam.com/exabeam/docs/api-keys
- group: auth
  title: ''
  type: Authentication
  url: authentication/exabeam-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/exabeam-scopes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.exabeam.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.exabeam.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://mycommunity.exabeam.com/category/forums
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Exabeam
- group: start
  title: ''
  type: Login
  url: https://developers.exabeam.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.exabeam.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exabeam.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://exabeam.statuspage.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://exabeam.securitypal.com/
- group: auth
  title: ''
  type: Compliance
  url: https://exabeam.securitypal.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/exabeam-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/exabeam-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exabeam-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/exabeam-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/exabeam-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/exabeam-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exabeam-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/exabeam-packages.yml
created: '2026-07-17'
description: Exabeam is a cybersecurity company that delivers faster, more accurate threat detection, investigation, and response (TDIR) through its AI-driven security operations platform. The platform combines cloud-native SIEM (security information and event management), user and entity behavioral analytics (UEBA), log management and collection, correlation and detection rules, and automated investigation workflows so security operations center (SOC) teams can monitor, triage, and respond to threats at scale. Exabeam exposes a REST API surface through its developer hub (developers.exabeam.com, hosted on ReadMe) covering access control, audit, authentication, cloud and site log collectors, context management, correlation rules, detection management, MITRE ATT&CK mappings, search, service health and consumption, threat center, and use cases. APIs are served from eight regional gateway hosts on the exabeam.cloud domain and secured with OAuth2 (API key and secret issued in the console). Exabeam
  also publishes an MCP server for agent-based access.
image: https://files.readme.io/e4416f6-small-Exabeam-2024-Logo-Color-Dark-Large-02.png
layout: provider
mcp_servers:
- description: ''
  name: exabeam-mcp.yml
  slug: exabeam-mcpyml
modified: '2026-07-19'
name: Exabeam
nav: Providers
network: true
overview: 'Exabeam publishes 13 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, SIEM, and UEBA.


  Exabeam''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 20 more developer resources.'
random_paper: 9
scopes:
- name: Exabeam Scopes
  scope_count: 3
  slug: exabeam-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 30.2
  delta: -7.8
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 38.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/exabeam/refs/heads/main/screenshots/exabeam-2026-07-25T213833.png
security:
- kind: authentication
  name: Exabeam Authentication
  slug: exabeam-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Exabeam Domain Security
  slug: exabeam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Exabeam Vulnerability Disclosure
  slug: exabeam-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Exabeam Trust Center
  slug: exabeam-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR, CCPA, IRAP, Cyber Essentials, TRUSTe
slug: exabeam
tags:
- Company
- Cybersecurity
- Security
- SIEM
- UEBA
- Threat Detection
- Security Operations
- SOC
- Log Management
- Incident Response
website: https://exabeam.com
---

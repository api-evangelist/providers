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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: 'REST API (apiv2) for searching and retrieving log events: initiate a search to get an RSID, then page results via the events/iterate endpoints, enumerate indexed fields with the fields/facet API, and '
  name: Loggly Event Retrieval API
  slug: loggly-event-retrieval-api
- description: Bulk/single event ingestion API. POST or GET log events to Loggly using a customer token; supports plain text and JSON payloads over HTTPS.
  name: Loggly HTTP/S Event Endpoint
  slug: loggly-https-event-endpoint
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loggly-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.solarwinds.com/en/success_center/loggly/content/loggly-documentation.htm
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.solarwinds.com/en/success_center/loggly/content/admin/api-overview.htm
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.solarwinds.com/en/success_center/loggly/content/admin/api-retrieving-data.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.solarwinds.com/en/success_center/loggly/content/admin/get-started.htm
- group: operate
  title: ''
  type: Support
  url: https://support.solarwinds.com/loggly
- group: company
  title: ''
  type: Blog
  url: https://www.loggly.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/loggly
- group: commercial
  title: ''
  type: Pricing
  url: https://www.loggly.com/plans-and-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.loggly.com/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solarwinds.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solarwinds.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.loggly.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.solarwinds.com/trust-center
- group: build
  title: ''
  type: Packages
  url: packages/loggly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/loggly-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loggly-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loggly-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loggly-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loggly-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.solarwinds.com/eol
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/loggly-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loggly-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.solarwinds.com/trust-center
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/loggly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.solarwinds.com/information-security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/loggly-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loggly-llms.txt
created: '2026-07-17'
description: Loggly is a cloud-based log management and analytics service (part of SolarWinds) that aggregates, searches, and visualizes application, server, and infrastructure logs in real time. Developers ship logs over syslog or the HTTP/S event endpoint and query them through a REST API supporting full-text search, field faceting, statistics, and dashboards. Loggly offers token-based (bearer) API authentication, an event-retrieval API (search, events, iterate, fields, stats) and a customer-token ingestion API, with SOC 2 Type II, PCI, and HIPAA-aligned security. Originally surfaced as a trinity-ventures portfolio lead, this profile has been enriched with real, searched API artifacts.
image: https://avatars.githubusercontent.com/u/6423?v=4
layout: provider
mcp_servers:
- description: ''
  name: loggly-mcp.yml
  slug: loggly-mcpyml
modified: '2026-07-20'
name: Loggly
nav: Providers
network: true
overview: 'Loggly publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Logging, Log Management, and Observability.


  Loggly''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 58
score:
  band: thin
  composite: 40.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 40.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loggly/refs/heads/main/screenshots/loggly-2026-07-25T225459.png
security:
- kind: authentication
  name: Loggly Authentication
  slug: loggly-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Loggly Domain Security
  slug: loggly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Loggly Vulnerability Disclosure
  slug: loggly-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Loggly Trust Center
  slug: loggly-trust-center
  summary_line: SOC 2 Type II, ISO 27001, PCI DSS, HIPAA, GDPR
slug: loggly
tags:
- Company
- Developer Tools
- Logging
- Log Management
- Observability
- Monitoring
- DevOps
- Analytics
- SaaS
website: https://documentation.solarwinds.com/en/success_center/loggly/content/loggly-documentation.htm
---

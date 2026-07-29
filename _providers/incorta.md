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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Tenant-scoped REST API for loading schemas, querying business views, extracting data to external tables, scheduling dashboard reports, and administration. Authenticated with a bearer Personal Access T
  name: Incorta Public API v2
  slug: incorta-public-api-v2
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.incorta.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.incorta.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.incorta.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.incorta.com/latest/references-public-api-v2/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.incorta.com/latest/references-public-api-v2/
- group: operate
  title: ''
  type: Support
  url: https://community.incorta.com/
- group: company
  title: ''
  type: Blog
  url: https://www.incorta.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Incorta
- group: operate
  title: ''
  type: StatusPage
  url: https://status.incorta.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.incorta.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.incorta.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: security/incorta-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/incorta-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/incorta-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/incorta-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/incorta-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/incorta-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/incorta-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/incorta-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/incorta-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/incorta-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/incorta-cli.yml
- group: design
  title: ''
  type: Components
  url: components/incorta-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/incorta-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/incorta-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/incorta-domain-security.yml
created: '2026-07-17'
description: Incorta is a unified data and analytics platform that lets teams acquire, enrich, analyze, and act on operational data without a traditional data warehouse or heavy dimensional modeling, using its Direct Data Mapping engine to query source data directly at high speed. For developers, Incorta exposes a tenant-scoped Public API (v1 and v2) under /incorta/api/v2 for loading physical schemas, querying business views, extracting data to external tables, scheduling dashboard reports, and administration, authenticated with Personal Access Tokens or OAuth 2.0 JWTs. Incorta also ships a Python CLI for metadata import/export, Python Data APIs for external notebooks, and a TypeScript Component SDK for building custom dashboard visualizations. Incorta is backed by GV and Kleiner Perkins.
image: https://cdn.prod.website-files.com/67b7abfbb037e687d0a415ec/67ec5981d1278178491febdf_Incorta-OG.jpg
layout: provider
mcp_servers:
- description: ''
  name: incorta-mcp.yml
  slug: incorta-mcpyml
modified: '2026-07-19'
name: Incorta
nav: Providers
network: true
overview: 'Incorta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Analytics, Business Intelligence, and Data Platform.


  Incorta''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 19 more developer resources.'
random_paper: 59
score:
  band: thin
  composite: 34.1
  delta: -1.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 44.7
  previous_composite: 35.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/incorta/refs/heads/main/screenshots/incorta-2026-07-25T222238.png
security:
- kind: authentication
  name: Incorta Authentication
  slug: incorta-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Incorta Domain Security
  slug: incorta-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Incorta Trust Center
  slug: incorta-trust-center
  summary_line: trust center published
slug: incorta
tags:
- Company
- Enterprise
- Analytics
- Business Intelligence
- Data Platform
- Data Analytics
- Data Integration
- Dashboards
website: https://www.incorta.com
---

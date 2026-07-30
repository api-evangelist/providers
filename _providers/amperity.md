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
    well_known_catalog: true
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: RESTful API for programmatic access to an Amperity tenant — list and manage campaigns, campaign drafts, segments, ingest jobs, audit events, and workflow runs. Authenticated with an OAuth2 client-cred
  name: Amperity API
  slug: amperity-api
- description: RESTful API for real-time access to unified customer profiles. List indexes, fetch an index, and read paginated customer profiles (or a single profile) for personalization and downstream activation. J
  name: Amperity Profile API
  slug: amperity-profile-api
- description: Low-latency, high-throughput REST API for real-time ingestion of event data from external systems into Amperity. POST JSON or XML payloads (up to 1 MB) to a tenant-specific stream. JWT bearer auth wit
  name: Amperity Streaming API
  slug: amperity-streaming-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.amperity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.amperity.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amperity.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amperity.com/reference/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.amperity.com/api/overview.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amperity
- group: operate
  title: ''
  type: StatusPage
  url: https://status.amperity.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.amperity.com/api/versioning.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amperity-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/amperity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amperity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amperity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amperity-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amperity-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amperity-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amperity-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amperity-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amperity-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amperity-domain-security.yml
created: '2026-07-17'
description: 'Amperity is a Seattle-based customer data platform (CDP) that helps consumer brands build accurate, unified customer profiles by stitching together fragmented first-party data from across their systems. Using AI-powered identity resolution (its patented Stitch technology), Amperity assembles a durable Customer 360 that powers segmentation, marketing campaigns, personalization, analytics, and activation to downstream destinations. For developers, Amperity exposes three public REST APIs: the Amperity API for programmatic access to tenant resources (campaigns, segments, ingest jobs, audit events, and workflow runs), the Profile API for real-time access to unified customer profiles by index, and the Streaming API for low-latency, high-throughput ingestion of events from external systems. The APIs use OAuth2 client-credentials tokens (JWT bearer), date-based versioning via an api-version header, and an RFC 8594 deprecation/sunset policy. Amperity serves retail, travel, hospitality,
  financial services, and other consumer-facing verticals.'
image: https://docs.amperity.com/_static/icon-light.svg
layout: provider
mcp_servers:
- description: ''
  name: amperity-mcp.yml
  slug: amperity-mcpyml
modified: '2026-07-17'
name: Amperity
nav: Providers
network: true
overview: 'Amperity publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Customer Data Platform, CDP, and Identity Resolution.


  Amperity''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, and 14 more developer resources.'
random_paper: 55
score:
  band: emerging
  composite: 26.1
  delta: -0.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 26.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amperity/refs/heads/main/screenshots/amperity-2026-07-25T200122.png
security:
- kind: authentication
  name: Amperity Authentication
  slug: amperity-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Amperity Domain Security
  slug: amperity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amperity
tags:
- Company
- Enterprise
- Customer Data Platform
- CDP
- Identity Resolution
- Customer 360
- Marketing
- Data
- Profiles
- Analytics
website: https://www.amperity.com
---

---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.splashthat.com
  baseurl_source: declared
  description: REST API for the Splash event marketing platform. Enables programmatic management of events, guest (GroupContact) records, organization-level contacts, unsubscribes, event approval workflows, team man
  name: Splash API
  slug: splash-api
artifact_total: 11
asyncapis:
- description: ''
  name: Splashthat Webhooks
  slug: splashthat-webhooks
collections:
- collection_type: postman
  name: Splash API v2.2
  slug: postman-splashthat-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/splashthat-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.splashthat.com/
- group: operate
  title: ''
  type: Support
  url: https://support.splashthat.com/
- group: company
  title: ''
  type: Blog
  url: https://splashthat.com/blog
- group: company
  title: ''
  type: Press
  url: https://splashthat.com/press
- group: commercial
  title: ''
  type: Pricing
  url: https://splashthat.com/pricing
- group: operate
  title: ''
  type: Status
  url: https://status.cvent.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://splashthat.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://splashthat.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://splashthat.com/security
- group: operate
  title: ''
  type: RateLimits
  url: https://support.splashthat.com/hc/en-us/articles/13759878758541-What-is-API-rate-limiting-and-what-are-the-benefits-and-impacts
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.splashthat.com/
- group: build
  title: ''
  type: Postman
  url: postman/splashthat-api.postman_collection.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SplashThat
- group: auth
  title: ''
  type: Authentication
  url: authentication/splashthat-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/splashthat-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/splashthat-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/splashthat-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/splashthat-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/splashthat-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/splashthat-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/splashthat-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/splashthat-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/splashthat-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/splashthat-llms.txt
created: '2026-06-13'
description: Splash is an event marketing platform that helps companies market, manage, and measure their live, virtual, and hybrid event programs. The Splash REST API enables brands and agencies to programmatically manage events, handle guest registration, process check-in, and pull event analytics. API access uses OAuth 2.0 client credentials and covers resources such as events, group contacts (guests), contacts, and ticketing.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/splashthat.png
jsonld:
- class_count: 14
  name: Splashthat Context
  property_count: 15
  slug: splashthat-context
layout: provider
mcp_servers:
- description: ''
  name: Splash MCP Server
  slug: splash-mcp-server
modified: '2026-08-13'
name: Splash
nav: Providers
network: true
overview: 'Splash publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Event, Event Marketing, Event Management, Guest Registration, and Ticketing.


  The Splash catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Splash''s developer surface includes documentation, support, engineering blog, pricing, status page, API reference, authentication, and 18 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 13
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
scopes:
- name: Splashthat Scopes
  scope_count: 1
  slug: splashthat-scopes
  summary_line: 1 scope
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 52.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 46.4
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/splashthat/refs/heads/main/screenshots/splashthat-2026-06-20T194323.png
security:
- kind: authentication
  name: Splashthat Authentication
  slug: splashthat-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Splashthat Domain Security
  slug: splashthat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: splashthat
tags:
- Event
- Event Marketing
- Event Management
- Guest Registration
- Ticketing
- Check-in
- Analytics
---

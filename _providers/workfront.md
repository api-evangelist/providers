---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Workfront Agentic Access
  operation_count: 59
  slug: workfront-agentic-access
  summary_line: 59 operations · 36 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The core Workfront REST API. Every object in the system has a URI of the form /attask/api/v22.0/{objCode}/{id}; GET retrieves or searches, POST inserts, PUT edits and DELETE removes. Adobe does not pu
  name: Adobe Workfront API
  slug: workfront-api
- description: The Workfront webhook/event surface. A system administrator registers a subscription for an object type (objCode) and event type (CREATE, UPDATE, DELETE) with a destination URL and auth token; Workfro
  name: Adobe Workfront Event Subscription API
  slug: workfront-event-subscription-api
- description: Adobe's hosted Model Context Protocol server for Workfront, generally available since June 2026. It exposes 87 documented tools across three families — Approvals (documents, approval workflows, remind
  name: Adobe Workfront MCP Server
  slug: workfront-mcp-server
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: 'Field management. Per-record-type quotas: max 500 fields total; max 20 PARAGRAPH (long-text) fields; max 20 FORMULA fields; max 30 REFERENCE fields. Field display names must be unique within a record '
  name: Adobe Workfront Fields API
  slug: workfront-fields-api
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: Resource permissions, member management, and access requests.
  name: Adobe Workfront Permissions API
  slug: workfront-permissions-api
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: Record Type Controller
  name: Adobe Workfront Record Types API
  slug: workfront-record-types-api
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: Record Controller
  name: Adobe Workfront Records API
  slug: workfront-records-api
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: 'View management. Limits: max 100 personal views per record type; max 255 characters for view name.'
  name: Adobe Workfront Views API
  slug: workfront-views-api
- baseURL: https://{customer-domain}.my.workfront.adobe.com/attask/api/v22.0
  baseurl_source: declared
  description: Workspace Controller
  name: Adobe Workfront Workspaces API
  slug: workfront-workspaces-api
artifact_total: 21
asyncapis:
- description: ''
  name: Workfront Event Subscriptions Webhooks
  slug: workfront-event-subscriptions-webhooks
collections:
- collection_type: open
  name: Workfront Planning API Version 1
  slug: open-workfront-planning-v1
- collection_type: open
  name: Workfront Planning API Version 2
  slug: open-workfront-planning-v2
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/workfront-planning-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/workfront-planning-v1-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workfront-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://business.adobe.com/products/workfront/main.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.adobe.com/wf-planning
- group: docs
  title: ''
  type: Documentation
  url: https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/workfront-api
- group: docs
  title: ''
  type: APIReference
  url: https://developersupport.workfront.com/page-api-explorer.html
- group: start
  title: ''
  type: GettingStarted
  url: https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/api-general-information/api-basics
- group: operate
  title: ''
  type: Support
  url: https://experienceleaguecommunities.adobe.com/t5/workfront/ct-p/workfront-community
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workfront
- group: commercial
  title: ''
  type: Pricing
  url: https://business.adobe.com/products/workfront/pricing.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy/policy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://experienceleague.adobe.com/en/docs/workfront/using/adobe-workfront-api/api-notes/api-version-support-schedule
- group: operate
  title: ''
  type: ChangeLog
  url: https://experienceleague.adobe.com/en/docs/workfront/using/product-announcements/product-releases/product-releases
- group: auth
  title: ''
  type: Security
  url: https://helpx.adobe.com/security.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.adobe.com/trust/compliance/compliance-list.html
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.adobe.com/trust.html
- group: build
  title: ''
  type: SDKs
  url: packages/workfront-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/workfront-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/workfront-cli.yml
- group: design
  title: ''
  type: Components
  url: components/workfront-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/workfront-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workfront-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/workfront-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/workfront-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/workfront-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/workfront-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/workfront-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/workfront-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/workfront-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/workfront-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workfront-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/workfront-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/workfront-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/workfront-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/workfront-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/workfront-event-subscriptions-webhooks.yml
created: '2026-08-12'
description: 'Adobe Workfront is Adobe''s enterprise work-management platform for marketing and creative operations — project and portfolio planning, request intake, task and resource management, proofing and approvals, timesheets, financial tracking and reporting — sold in Select, Prime and Ultimate packages. Its developer surface is unusually wide for a work-management vendor: a versioned REST core API at /attask/api (v22.0, 174 objects exposed through an anonymous object-metadata endpoint), the separately versioned Workfront Planning API published as first-party OpenAPI 3.0.1 and 3.1.0 documents on developer.adobe.com, an Event Subscription API that pushes object change events to customer webhook endpoints, a Document Webhooks API third-party document providers implement, and — since June 2026 — a hosted Model Context Protocol server at mcp.workfront.adobe.com exposing 87 documented tools behind OAuth 2.1, plus first-party agent Skills published in the adobe/skills repository.'
image: https://avatars.githubusercontent.com/u/3494194?v=4
layout: provider
mcp_servers:
- description: ''
  name: Adobe Workfront MCP server
  slug: adobe-workfront-mcp-server
modified: '2026-08-12'
name: Adobe Workfront
nav: Providers
network: true
overview: 'Adobe Workfront publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Fields API, Permissions API, Record Types API, and 3 more. Tagged areas include Company, Work Management, Project Management, Marketing Operations, and Creative Operations.


  The Adobe Workfront catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Adobe Workfront''s developer surface includes documentation, API reference, getting-started guide, support, pricing, changelog, CLI, and 33 more developer resources.'
plans:
- name: Workfront Plans Pricing
  plan_count: 3
  slug: workfront-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 9
  name: Workfront Rate Limits
  slug: workfront-rate-limits
scopes:
- name: Workfront Scopes
  scope_count: 18
  slug: workfront-scopes
  summary_line: 18 scopes · authorizationCode
score:
  band: strong
  composite: 63.8
  coverage:
    artifact_dirs: 25
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 4.5
    contract_quality: 60.1
    developer_ergonomics: 83.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 71.1
  previous_composite: 63.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workfront/refs/heads/main/screenshots/workfront-2026-08-17T075411.png
security:
- kind: authentication
  name: Workfront Authentication
  slug: workfront-authentication
  summary_line: http/apiKey/oauth2 · 8 schemes
- kind: domain-security
  name: Workfront Domain Security
  slug: workfront-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Workfront Vulnerability Disclosure
  slug: workfront-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Workfront Trust Center
  slug: workfront-trust-center
  summary_line: SOC 2 Type 2 (Security, Availability & Confidentiality), SOC 3 (Security, Availability & Confidentiality), ISO 9001:2015, ISO 27001:2022, ISO 27017:2015, ISO 27018:2019, ISO 22301:2019, HIPAA ready, IRAP Assessed (Australia), GLBA ready, FERPA ready
slug: workfront
tags:
- Company
- Work Management
- Project Management
- Marketing Operations
- Creative Operations
- Collaboration
- Approvals
- Resource Management
- Workflow-Automation
- Enterprise Software
- Adobe
- MCP
website: https://business.adobe.com/products/workfront/main.html
---

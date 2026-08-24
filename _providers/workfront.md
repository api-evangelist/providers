---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 61.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Workfront Agentic Access
  operation_count: 59
  slug: workfront-agentic-access
  summary_line: 59 operations · 36 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: The core Workfront REST API. Every object in the system has a URI of the form /attask/api/v22.0/{objCode}/{id}; GET retrieves or searches, POST inserts, PUT edits and DELETE removes. Adobe does not pu
  name: Adobe Workfront API
  slug: workfront-api
- description: 'The Workfront Planning (Maestro) API — workspaces, record types, records, fields, views and permissions — published by Adobe as an OpenAPI 3.1.0 document with 21 paths, 49 operations and 74 component '
  name: Adobe Workfront Planning API v2
  slug: workfront-planning-api-v2
- description: Version 1 of the Workfront Planning API, published by Adobe as an OpenAPI 3.0.1 document covering records, record types and workspaces across 7 paths and 10 operations. Released July 2024 and still th
  name: Adobe Workfront Planning API v1
  slug: workfront-planning-api-v1
- description: The Workfront webhook/event surface. A system administrator registers a subscription for an object type (objCode) and event type (CREATE, UPDATE, DELETE) with a destination URL and auth token; Workfro
  name: Adobe Workfront Event Subscription API
  slug: workfront-event-subscription-api
- description: Adobe's hosted Model Context Protocol server for Workfront, generally available since June 2026. It exposes 87 documented tools across three families — Approvals (documents, approval workflows, remind
  name: Adobe Workfront MCP Server
  slug: workfront-mcp-server
artifact_total: 17
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
overview: 'Adobe Workfront publishes 2 APIs on the [APIs.io](https://apis.io/) network: Planning API v2 and Planning API v1. Tagged areas include Company, Work Management, Project Management, Marketing Operations, and Creative Operations.


  The Adobe Workfront catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Adobe Workfront''s developer surface includes documentation, API reference, getting-started guide, support, pricing, changelog, CLI, and 31 more developer resources.'
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
  band: exemplar
  composite: 67.0
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 16.7
    contract_quality: 60.5
    developer_ergonomics: 83.3
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 71.1
  previous_composite: 67.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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

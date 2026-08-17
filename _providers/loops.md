---
access_model:
  confidence: high
  label: Free plan, self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://loops.so/pricing
  - https://loops.so/docs/api-reference/intro
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 69.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Loops Agentic Access
  operation_count: 24
  slug: loops-agentic-access
  summary_line: 24 operations · 10 acting
api_count: 20
apis:
- description: Validate a Loops API key and discover which team it belongs to. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops API key API
  slug: loops-api-key-api
- description: Read and create saved audience segments used to target campaigns and workflows. 3 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Audience segments API
  slug: loops-audience-segments-api
- description: Organize campaigns into groups. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Campaign groups API
  slug: loops-campaign-groups-api
- description: Create, target, schedule and update email campaigns. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Campaigns API
  slug: loops-campaigns-api
- description: Create, read and update reusable LMX email components. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Components API
  slug: loops-components-api
- description: Read team configuration, including dedicated sending IP addresses. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Configuration API
  slug: loops-configuration-api
- description: Create and list the custom properties available on contacts. 2 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Contact properties API
  slug: loops-contact-properties-api
- description: Create, update, find and delete contacts, and manage suppression status. 6 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Contacts API
  slug: loops-contacts-api
- description: Read, update, preview and Guardian-validate the LMX body of campaigns, workflow emails and transactional templates. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Email messages API
  slug: loops-email-messages-api
- description: Read the event patterns Loops has detected from incoming events, including their observed properties. 3 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Event patterns API
  slug: loops-event-patterns-api
- description: Send events that update contact activity and trigger published workflows. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Events API
  slug: loops-events-api
- description: List the mailing lists in your account. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Mailing lists API
  slug: loops-mailing-lists-api
- description: Create, read and update reusable email themes. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Themes API
  slug: loops-themes-api
- description: Create, edit, publish, list and send transactional email templates with data variables. 8 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Transactional emails API
  slug: loops-transactional-emails-api
- description: Organize transactional emails into groups. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Transactional groups API
  slug: loops-transactional-groups-api
- description: Upload image assets for use in emails via a presigned-URL flow. 2 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Uploads API
  slug: loops-uploads-api
- description: Create, read, update, delete and reroute the nodes of a workflow graph. 7 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Workflow nodes API
  slug: loops-workflow-nodes-api
- description: List, create, inspect and update automation workflows and their mailing-list targeting. 5 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Workflows API
  slug: loops-workflows-api
- description: Remote Model Context Protocol server for Loops, reachable at https://mcp.loops.so over Streamable HTTP with OAuth 2.0 (PKCE, scope "mcp"). Exposes four meta-tools — search, describe, execute and teams
  name: Loops MCP Server
  slug: loops-mcp-server
- description: Outbound event surface. Seventeen signed event types covering contact lifecycle, mailing-list membership, and email delivery, engagement and complaint signals, delivered by HTTP POST to one subscriber
  name: Loops Webhooks
  slug: loops-webhooks
artifact_total: 42
asyncapis:
- description: Event catalog for the Loops webhook surface, derived operation-for-operation from the `webhooks` block of the Loops OpenAPI 3.1 document (info.version 1.21.6, published at https://app.loops.so/openapi
  name: Loops Webhooks
  slug: loops-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Loops OpenAPI Spec API key API
  slug: open-loops-api-key-api
- collection_type: open
  name: Loops OpenAPI Spec API key Campaigns API
  slug: open-loops-campaigns-api
- collection_type: open
  name: Loops OpenAPI Spec API key Components API
  slug: open-loops-components-api
- collection_type: open
  name: Loops OpenAPI Spec API key Contact properties API
  slug: open-loops-contact-properties-api
- collection_type: open
  name: Loops OpenAPI Spec API key Contacts API
  slug: open-loops-contacts-api
- collection_type: open
  name: Loops OpenAPI Spec API key Dedicated sending IPs API
  slug: open-loops-dedicated-sending-ips-api
- collection_type: open
  name: Loops OpenAPI Spec API key Email messages API
  slug: open-loops-email-messages-api
- collection_type: open
  name: Loops OpenAPI Spec API key Events API
  slug: open-loops-events-api
- collection_type: open
  name: Loops OpenAPI Spec API key Mailing lists API
  slug: open-loops-mailing-lists-api
- collection_type: open
  name: Loops OpenAPI Spec API key Themes API
  slug: open-loops-themes-api
- collection_type: open
  name: Loops OpenAPI Spec API key Transactional emails API
  slug: open-loops-transactional-emails-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loops-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loops-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/loops-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loops-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/loops-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loops-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loops-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/loops-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loops-finops.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loops-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/loops-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/loops-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/loops-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/loops-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/loops-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/loops-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/loops-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/loops-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/loops-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loops-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.loops.so
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/loops-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loops-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/loops-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/loops-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loops-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loops-llms.txt
- group: company
  title: ''
  type: Website
  url: https://loops.so/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://loops.so/docs
- group: docs
  title: ''
  type: Documentation
  url: https://loops.so/docs
- group: docs
  title: ''
  type: APIReference
  url: https://loops.so/docs/api-reference/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://loops.so/docs/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://loops.so/docs/quickstart-agents
- group: operate
  title: ''
  type: Support
  url: https://app.loops.so/settings?page=support
- group: company
  title: ''
  type: Blog
  url: https://loops.so/engineering
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Loops-so
- group: commercial
  title: ''
  type: Pricing
  url: https://loops.so/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.loops.so/register
- group: start
  title: ''
  type: Login
  url: https://app.loops.so/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loops.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loops.so/privacy
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://loops.so/dpa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendwithloops
- group: other
  title: ''
  type: Glossary
  url: https://loops.so/glossary
created: '2026-05-08'
description: Loops is an email platform built for software companies, combining marketing campaigns, product and lifecycle automation, and transactional email on one contact model. Its REST API v1 exposes 64 operations across contacts, contact properties, mailing lists, audience segments, events and event patterns, campaigns, transactional emails, email messages authored in its own LMX markup, themes, components, uploads and workflow graphs, plus a 17-event signed webhook surface. Loops publishes its OpenAPI 3.1 document openly, ships first-party SDKs for JavaScript, Go, PHP, Ruby and Nuxt, a Go CLI, four versioned Agent Skills, and a hosted OAuth-protected MCP server at mcp.loops.so. Pricing is based on stored subscribed contacts rather than send volume, with a permanent free tier. The operating company is Astrodon Corporation.
finops:
- name: Loops Finops
  service_category: Email Marketing
  slug: loops-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loops.png
layout: provider
mcp_servers:
- description: ''
  name: loops-mcp.yml
  slug: loops-mcpyml
modified: '2026-08-13'
name: Loops
nav: Providers
network: true
overview: 'Loops publishes 19 APIs on the [APIs.io](https://apis.io/) network, including API key API, Audience segments API, Campaign groups API, and 16 more. Tagged areas include Email, Email API, Marketing Automation, Transactional Email, and Lifecycle Email.


  The Loops catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Loops'' developer surface includes authentication, code examples, CLI, changelog, documentation, API reference, getting-started guide, and 38 more developer resources.'
plans:
- name: Loops Plans Pricing
  plan_count: 2
  slug: loops-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 8
  name: Loops Rate Limits
  slug: loops-rate-limits
scopes:
- name: Loops Scopes
  scope_count: 0
  slug: loops-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.8
  delta: 36.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 65.6
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/loops/refs/heads/main/screenshots/loops-2026-06-20T184718.png
security:
- kind: authentication
  name: Loops Authentication
  slug: loops-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Loops Domain Security
  slug: loops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Loops Trust Center
  slug: loops-trust-center
  summary_line: SOC 2, EU-U.S. Data Privacy Framework, Swiss-U.S. Data Privacy Framework
slug: loops
tags:
- Email
- Email API
- Marketing Automation
- Transactional Email
- Lifecycle Email
- Webhooks
- SaaS
- Communications
- Developer Tools
- MCP
- Agents
- Campaigns
website: https://loops.so/
---

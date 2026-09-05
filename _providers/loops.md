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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Loops Agentic Access
  operation_count: 24
  slug: loops-agentic-access
  summary_line: 24 operations · 10 acting
api_count: 1
apis:
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Validate a Loops API key and discover which team it belongs to. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops API key API
  slug: loops-api-key-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Read and create saved audience segments used to target campaigns and workflows. 3 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Audience segments API
  slug: loops-audience-segments-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Organize campaigns into groups. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Campaign groups API
  slug: loops-campaign-groups-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, target, schedule and update email campaigns. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Campaigns API
  slug: loops-campaigns-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, read and update reusable LMX email components. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Components API
  slug: loops-components-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Read team configuration, including dedicated sending IP addresses. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Configuration API
  slug: loops-configuration-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create and list the custom properties available on contacts. 2 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Contact properties API
  slug: loops-contact-properties-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, update, find and delete contacts, and manage suppression status. 6 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Contacts API
  slug: loops-contacts-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Read, update, preview and Guardian-validate the LMX body of campaigns, workflow emails and transactional templates. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Email messages API
  slug: loops-email-messages-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Read the event patterns Loops has detected from incoming events, including their observed properties. 3 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Event patterns API
  slug: loops-event-patterns-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Send events that update contact activity and trigger published workflows. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Events API
  slug: loops-events-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: List the mailing lists in your account. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Mailing lists API
  slug: loops-mailing-lists-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, read and update reusable email themes. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Themes API
  slug: loops-themes-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, edit, publish, list and send transactional email templates with data variables. 8 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Transactional emails API
  slug: loops-transactional-emails-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Organize transactional emails into groups. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Transactional groups API
  slug: loops-transactional-groups-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Upload image assets for use in emails via a presigned-URL flow. 2 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Uploads API
  slug: loops-uploads-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, read, update, delete and reroute the nodes of a workflow graph. 7 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Workflow nodes API
  slug: loops-workflow-nodes-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: List, create, inspect and update automation workflows and their mailing-list targeting. 5 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Workflows API
  slug: loops-workflows-api
- description: Remote Model Context Protocol server for Loops, reachable at https://mcp.loops.so over Streamable HTTP with OAuth 2.0 (PKCE, scope "mcp"). Exposes four meta-tools — search, describe, execute and teams
  name: Loops MCP Server
  slug: loops-mcp-server
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Outbound event surface. Seventeen signed event types covering contact lifecycle, mailing-list membership, and email delivery, engagement and complaint signals, delivered by HTTP POST to one subscriber
  name: Loops Webhooks
  slug: loops-webhooks
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: 'Events Loops sends to your configured webhook endpoint when certain events happen in your account. Configure an endpoint in Settings → Webhooks. Each account supports one webhook endpoint. Events are '
  name: Loops Webhooks API
  slug: loops-webhooks-api
artifact_total: 43
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/loops-capability-edges.yml
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
  name: Loops MCP Server
  slug: loops-mcp-server
modified: '2026-08-13'
name: Loops
nav: Providers
network: true
overview: 'Loops publishes 20 APIs on the [APIs.io](https://apis.io/) network, including API key API, Audience segments API, Campaign groups API, and 17 more. Tagged areas include Email, Email API, Marketing Automation, Transactional Email, and Lifecycle Email.


  The Loops catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Loops'' developer surface includes authentication, code examples, CLI, changelog, documentation, API reference, getting-started guide, and 39 more developer resources.'
plans:
- name: Loops Plans Pricing
  plan_count: 2
  slug: loops-plans-pricing
random_paper: 11
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
  band: exemplar
  composite: 68.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 63.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 68.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
- Webhook
- Software-as-a-Service
- Communications
- Developer Tools
- MCP
- Agents
- Campaigns
website: https://loops.so/
---

---
access_model:
  confidence: high
  label: Public documentation, gated credentials
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://eventx.io/pricing
  - https://eventx-hq.gitbook.io/knowledge-base/api-doc/auth
  - https://esaas-api.eventx.io/api-docs/public-api/openApi.json
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Eventxtra Agentic Access
  operation_count: 58
  slug: eventxtra-agentic-access
  summary_line: 58 operations · 35 acting
api_count: 1
apis:
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Attendee API from EventX — 9 operation(s) for attendee.
  name: EventX Attendee API
  slug: eventxtra-attendee-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Auth API from EventX — 1 operation(s) for auth.
  name: EventX Auth API
  slug: eventxtra-auth-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Custom Field API from EventX — 2 operation(s) for custom field.
  name: EventX Custom Field API
  slug: eventxtra-custom-field-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Event API from EventX — 4 operation(s) for event.
  name: EventX Event API
  slug: eventxtra-event-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Event Webhook API from EventX — 3 operation(s) for event webhook.
  name: EventX Event Webhook API
  slug: eventxtra-event-webhook-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Invoice API from EventX — 2 operation(s) for invoice.
  name: EventX Invoice API
  slug: eventxtra-invoice-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Media API from EventX — 3 operation(s) for media.
  name: EventX Media API
  slug: eventxtra-media-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Order API from EventX — 2 operation(s) for order.
  name: EventX Order API
  slug: eventxtra-order-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Outreach API from EventX — 6 operation(s) for outreach.
  name: EventX Outreach API
  slug: eventxtra-outreach-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Public Api API from EventX — 5 operation(s) for public api.
  name: EventX Public API
  slug: eventxtra-public-api-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Registration Form API from EventX — 1 operation(s) for registration form.
  name: EventX Registration Form API
  slug: eventxtra-registration-form-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Registration Order API from EventX — 3 operation(s) for registration order.
  name: EventX Registration Order API
  slug: eventxtra-registration-order-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Registration Service API from EventX — 2 operation(s) for registration service.
  name: EventX Registration Service API
  slug: eventxtra-registration-service-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Salesforce API from EventX — 1 operation(s) for salesforce.
  name: EventX Salesforce API
  slug: eventxtra-salesforce-api
- baseURL: https://esaas-api.eventx.io
  baseurl_source: declared
  description: The Ticket Class API from EventX — 3 operation(s) for ticket class.
  name: EventX Ticket Class API
  slug: eventxtra-ticket-class-api
artifact_total: 23
asyncapis:
- description: ''
  name: Eventxtra Webhooks
  slug: eventxtra-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eventxtra-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eventxtra-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://eventx.io
- group: docs
  title: ''
  type: Documentation
  url: https://help.eventx.io/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.eventx.io/
- group: operate
  title: ''
  type: Support
  url: https://eventx.io/contact-us
- group: company
  title: ''
  type: Blog
  url: https://eventx.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://eventx.io/pricing
- group: start
  title: ''
  type: Login
  url: https://portal.eventx.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eventx.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eventx.io/terms-of-service
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eventxtra
- group: auth
  title: ''
  type: Compliance
  url: https://eventx.io/data-protection-and-security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eventxtra-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eventxtra-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/eventxtra-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/eventxtra-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eventxtra-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://eventx-hq.gitbook.io/knowledge-base/api-doc/auth
- group: start
  title: ''
  type: GettingStarted
  url: https://eventx-hq.gitbook.io/knowledge-base
- group: start
  title: ''
  type: SignUp
  url: https://portal.eventx.io/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.eventx.io/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/eventxtra-public-api-openapi.json
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/eventxtra-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/eventxtra-tool-crosswalk.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eventxtra-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eventxtra-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eventxtra-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eventxtra-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/eventxtra-public-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/eventxtra-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eventxtra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eventxtra-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eventxtra-knowledge-base-llms.txt
created: '2026-07-17'
description: EventX (EventXtra Limited) is an AI-powered, all-in-one event management and marketing platform for in-person, virtual, and hybrid events, headquartered in Hong Kong with offices across APAC. It provides event registration and RSVP, QR-code check-in and badge printing, ticketing and payment with 0% platform fees, AI Lead Finder, event website building, virtual event hosting, sponsor and exhibitor management, lead capture, and WhatsApp/email marketing. EventX serves 5,600+ brands and is ISO 27001 certified and GDPR compliant. It also offers an official hosted MCP server that lets AI assistants query live event data (registrations, sessions, ticket sales, attendance) in natural language, provisioned one-click from the EventX dashboard and compatible with Claude, ChatGPT, Cursor, and OpenCode. EventX publishes a REST Public API documented as an OpenAPI 3.2.0 contract (46 paths, 58 operations) at esaas-api.eventx.io, covering events, attendees, custom fields, ticket classes, orders,
  invoices, media, registration forms and outreach, plus a per-event webhook subscription API delivering five attendee lifecycle actions. Added to the API Evangelist network as a portfolio company of 500 Global and enriched via the pipeline.
image: https://eventx.io/images/og/index-b41677e1.png
layout: provider
mcp_servers:
- description: EventX ships an official hosted (remote) MCP server that exposes an organization's live EventX data to MCP-compatible AI assistants in natural language, without SQL or API knowledge. It is provisioned
  name: EventX MCP Server
  slug: eventx-mcp-server
modified: '2026-08-13'
name: EventX
nav: Providers
network: true
overview: 'EventX publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Attendee API, Auth API, Custom Field API, and 12 more. Tagged areas include Company, Event Management, Event Registration, Ticketing, and Check-in.


  The EventX catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EventX''s developer surface includes authentication, documentation, support, engineering blog, pricing, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Eventxtra Plans Pricing
  plan_count: 4
  slug: eventxtra-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Eventxtra Rate Limits
  slug: eventxtra-rate-limits
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 58.8
    developer_ergonomics: 32.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eventxtra/refs/heads/main/screenshots/eventxtra-2026-07-25T213718.png
security:
- kind: authentication
  name: Eventxtra Authentication
  slug: eventxtra-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Eventxtra Domain Security
  slug: eventxtra-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Eventxtra Trust Center
  slug: eventxtra-trust-center
  summary_line: ISO 27001, GDPR
slug: eventxtra
tags:
- Company
- Event Management
- Event Registration
- Ticketing
- Check-in
- Event Marketing
- Virtual Events
- Webhook
- OpenAPI
- MCP
- Artificial Intelligence
- Hong Kong
- APAC
website: https://eventx.io
---

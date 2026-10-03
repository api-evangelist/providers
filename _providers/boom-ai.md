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
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 41
  human_in_the_loop: 1
  name: Boom Ai Agentic Access
  operation_count: 80
  slug: boom-ai-agentic-access
  summary_line: 80 operations · 41 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://dev.useboom.ai
  baseurl_source: declared
  description: The CDP Custom Objects API from Boom Ai — 5 operation(s) for cdp custom objects.
  name: Boom Ai CDP Custom Objects API
  phrasing_intents:
  - id: cdp_custom_objects_list
    intent: List custom objects of one type
    question: Which orders or other custom records have I stored in the CDP for a given type?
  - id: cdp_custom_objects_upsert
    intent: Create or update a custom object
    question: How do I save a single order or subscription record into the CDP?
  - id: cdp_custom_objects_delete
    intent: Delete a custom object
    question: What happens to a custom object's relationships when I delete it?
  - id: cdp_custom_objects_get
    intent: Read one custom object
    question: What attributes are stored on a specific custom object?
  - id: cdp_custom_objects_batch_upsert
    intent: Bulk upsert custom objects
    question: How many custom objects can I load into the CDP in a single request?
  - id: cdp_custom_object_types_list
    intent: List custom object types
    question: Which custom object types have been defined for my organization?
  - id: cdp_custom_object_types_create
    intent: Define a new custom object type
    question: How do I define a new kind of custom record, like orders, before loading any?
  - id: cdp_custom_object_types_get
    intent: Read one custom object type
    question: What is the label and description of a particular custom object type?
  phrasing_ops: 8
  slug: boom-ai-cdp-custom-objects-api
- baseURL: https://dev.useboom.ai
  baseurl_source: declared
  description: The CDP Events API from Boom Ai — 3 operation(s) for cdp events.
  name: Boom Ai CDP Events API
  phrasing_intents:
  - id: cdp_events_list
    intent: List behavioral events
    question: Which events has a particular customer triggered recently?
  - id: cdp_events_record
    intent: Record one event in real time
    question: How do I send a checkout event so it can trigger a journey right away?
  - id: cdp_events_get
    intent: Read one event
    question: What payload was stored for a specific event?
  - id: cdp_events_batch_record
    intent: Bulk load historical events
    question: How do I backfill historical events without enrolling people in journeys?
  phrasing_ops: 4
  slug: boom-ai-cdp-events-api
- baseURL: https://dev.useboom.ai
  baseurl_source: declared
  description: The CDP People API from Boom Ai — 4 operation(s) for cdp people.
  name: Boom Ai CDP People API
  phrasing_intents:
  - id: cdp_people_list
    intent: List people in the CDP
    question: Who are the most recently added people in my customer data?
  - id: cdp_people_upsert
    intent: Create or update a person
    question: How do I add a customer with their phone number so Boom can reach them?
  - id: cdp_people_delete
    intent: Delete a person
    question: Are a person's events kept when I delete their profile?
  - id: cdp_people_get
    intent: Read one person by external id
    question: What profile data do we hold for a customer with a known external id?
  - id: cdp_people_batch_upsert
    intent: Bulk upsert people
    question: How many customers can I import into the CDP in one request?
  - id: cdp_people_search
    intent: Search people by name, email or phone
    question: How do I find a customer when I only know part of their email or phone number?
  phrasing_ops: 6
  slug: boom-ai-cdp-people-api
- baseURL: https://dev.useboom.ai
  baseurl_source: declared
  description: The CDP Relationships API from Boom Ai — 4 operation(s) for cdp relationships.
  name: Boom Ai CDP Relationships API
  phrasing_intents:
  - id: cdp_relationship_types_list
    intent: List relationship types
    question: Which relationship types are defined, so I know how people and objects can be linked?
  - id: cdp_relationship_types_register
    intent: Register a relationship type
    question: How do I define that a person places orders, or that an order has line items?
  - id: cdp_relationship_types_get
    intent: Read one relationship type
    question: What role and object types does a specific relationship type connect?
  - id: cdp_relationships_unlink
    intent: Unlink a relationship
    question: How do I remove the link between one person and a custom object?
  - id: cdp_relationships_list
    intent: List relationship links for a person or object
    question: Which orders or other objects is a given person linked to?
  - id: cdp_relationships_link
    intent: Link a person or object to an object
    question: How do I connect a single person to an order they placed?
  - id: cdp_relationships_batch
    intent: Bulk link or unlink relationships
    question: Can I link and unlink many relationships in one request?
  phrasing_ops: 7
  slug: boom-ai-cdp-relationships-api
- baseURL: https://dev.useboom.ai
  baseurl_source: declared
  description: The CDP Sources API from Boom Ai — 1 operation(s) for cdp sources.
  name: Boom Ai CDP Sources API
  phrasing_intents:
  - id: cdp_sources_list
    intent: List connected data sources
    question: Is my Shopify store connected and active in Boom?
  phrasing_ops: 1
  slug: boom-ai-cdp-sources-api
- baseURL: https://dev.useboom.ai
  baseurl_source: declared
  description: The HTTP credentials API from Boom Ai — 1 operation(s) for http credentials.
  name: Boom Ai HTTP credentials API
  phrasing_intents:
  - id: http_credentials_list
    intent: List reusable HTTP credentials
    question: Which stored credentials can an HTTP Request step authenticate with?
  phrasing_ops: 1
  slug: boom-ai-http-credentials-api
- baseURL: https://dev.useboom.ai
  baseurl_source: declared
  description: The Initiatives API from Boom Ai — 14 operation(s) for initiatives.
  name: Boom Ai Initiatives API
  phrasing_intents:
  - id: initiatives_list
    intent: List my initiatives
    question: Which initiatives does my organization have running right now?
  - id: initiatives_create
    intent: Create a draft initiative
    question: How do I start a new WhatsApp outreach initiative in Boom?
  - id: initiatives_get
    intent: Get one initiative's details
    question: What is the current status and objective of a specific initiative?
  - id: initiatives_update
    intent: Edit a draft initiative
    question: Can I change the objective or guiding context of an initiative that is still a draft?
  - id: initiatives_archive
    intent: Archive a finished initiative
    question: How do I hide a completed initiative from my initiatives list?
  - id: initiatives_cancel
    intent: Cancel an initiative for good
    question: How do I permanently cancel an initiative and stop all its conversations?
  - id: initiatives_summary
    intent: Get an initiative's data summary
    question: How many participants does an initiative have, and how well is each captured variable covered?
  - id: extraction_schema_get
    intent: Read an initiative's extraction schema
    question: Which typed fields is an initiative currently pulling out of each conversation?
  phrasing_ops: 23
  slug: boom-ai-initiatives-api
- baseURL: https://dev.useboom.ai
  baseurl_source: declared
  description: The Journeys API from Boom Ai — 16 operation(s) for journeys.
  name: Boom Ai Journeys API
  phrasing_intents:
  - id: journeys_list
    intent: List my journeys
    question: Which journeys has my organization built, and which ones are live?
  - id: journeys_create_draft
    intent: Create a draft journey from a full graph
    question: How do I create a brand-new journey for an initiative from a complete node graph?
  - id: journeys_get
    intent: Get a journey's trigger and steps
    question: What triggers a journey and what steps do people move through in it?
  - id: journeys_update_draft
    intent: Replace a draft journey's whole graph
    question: How do I overwrite an existing draft journey's entire graph in one call?
  - id: journeys_get_definition
    intent: Get a journey's full editable graph
    question: Where do I get every node's config and connection so I can edit a journey and save it back?
  - id: journeys_disconnect_nodes
    intent: Remove edges leaving a journey node
    question: How do I remove the connection between two steps in a journey?
  - id: journeys_connect_nodes
    intent: Connect two journey nodes
    question: How do I route a journey to the next step when someone replies?
  - id: journeys_create_draft_from_published
    intent: Fork a live journey into an editable draft
    question: How can I safely edit a journey that is already live?
  phrasing_ops: 21
  slug: boom-ai-journeys-api
- baseURL: https://dev.useboom.ai
  baseurl_source: declared
  description: The Segments API from Boom Ai — 7 operation(s) for segments.
  name: Boom Ai Segments API
  phrasing_intents:
  - id: segments_list
    intent: List my audience segments
    question: Which audience segments does my organization have?
  - id: segments_create
    intent: Create an audience segment
    question: How do I save a new audience of people based on attributes and events?
  - id: segments_delete
    intent: Delete a segment
    question: What happens to journeys triggered by a segment when I delete it?
  - id: segments_get
    intent: Get a segment and its member count
    question: How many people are in a given segment right now?
  - id: segments_update
    intent: Update a segment's filter or settings
    question: If I change a segment's filter, does its membership update right away?
  - id: segments_evaluate
    intent: Re-evaluate a segment's membership now
    question: Can I refresh who is in a segment immediately instead of waiting for its schedule?
  - id: segments_members_list
    intent: List the people in a segment
    question: Who exactly is in a segment?
  - id: segments_catalog
    intent: Get the segment filter catalog
    question: What attributes, related data and computed variables can I filter a segment on?
  phrasing_ops: 10
  slug: boom-ai-segments-api
- baseURL: https://dev.useboom.ai
  baseurl_source: declared
  description: The WhatsApp templates API from Boom Ai — 3 operation(s) for whatsapp templates.
  name: Boom Ai WhatsApp templates API
  phrasing_intents:
  - id: templates_list
    intent: List my WhatsApp templates
    question: Which of my WhatsApp templates have been approved?
  - id: templates_create
    intent: Create and submit a WhatsApp template
    question: How long does WhatsApp take to approve a new message template?
  - id: templates_get
    intent: Get a template's approval status
    question: Why was my WhatsApp template rejected?
  - id: whatsapp_numbers_list
    intent: List connected WhatsApp numbers
    question: Which WhatsApp phone numbers are connected to my organization?
  phrasing_ops: 4
  slug: boom-ai-whatsapp-templates-api
- baseURL: https://dev.useboom.ai
  baseurl_source: declared
  description: The Environments API from Boom Ai — 1 operation(s) for environments.
  name: Boom Ai Environments API
  phrasing_intents:
  - id: environments_list
    intent: List journey environments and their variables
    question: Which environments can a journey be pinned to?
  phrasing_ops: 1
  slug: boom-ai-environments-api
artifact_total: 31
asyncapis:
- description: ''
  name: Boom Ai Webhooks
  slug: boom-ai-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Boom CDP Custom Objects API
  slug: open-boom-ai-cdp-custom-objects-api
- collection_type: open
  name: Boom CDP Custom Objects CDP Events API
  slug: open-boom-ai-cdp-events-api
- collection_type: open
  name: Boom CDP Custom Objects CDP People API
  slug: open-boom-ai-cdp-people-api
- collection_type: open
  name: Boom CDP Custom Objects CDP Relationships API
  slug: open-boom-ai-cdp-relationships-api
- collection_type: open
  name: Boom CDP Custom Objects CDP Sources API
  slug: open-boom-ai-cdp-sources-api
- collection_type: open
  name: Boom CDP Custom Objects HTTP credentials API
  slug: open-boom-ai-http-credentials-api
- collection_type: open
  name: Boom CDP Custom Objects Initiatives API
  slug: open-boom-ai-initiatives-api
- collection_type: open
  name: Boom CDP Custom Objects Journeys API
  slug: open-boom-ai-journeys-api
- collection_type: open
  name: Boom CDP Custom Objects Segments API
  slug: open-boom-ai-segments-api
- collection_type: open
  name: Boom CDP Custom Objects WhatsApp templates API
  slug: open-boom-ai-whatsapp-templates-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.useboom.ai/
- group: commercial
  title: ''
  type: License
  url: https://github.com/BOOM-TML/skills/blob/main/LICENSE
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/capabilities/boom-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/boom-ai-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/agentic-access/boom-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/boom-ai-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/security/boom-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boom-ai-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/authentication/boom-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boom-ai-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.useboom.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useboom.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.useboom.ai/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.useboom.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://useboom.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://useboom.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://useboom.ai/demo
- group: start
  title: ''
  type: Login
  url: https://app.useboom.ai
- group: operate
  title: ''
  type: Support
  url: mailto:support@useboom.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drive.google.com/file/d/1SlTp1_QWhVASpbxncSj1NpmFqiiGBcF1/view
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drive.google.com/file/d/1ITWbsA8ZmyhinJYYr4ezRdhNe-MWQBC_/view
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/openapi/_original/boom-ai-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/boom-ai-openapi-original.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/mcp/boom-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/boom-ai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/llms/boom-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boom-ai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/overlays/boom-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/boom-ai-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/conformance/boom-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boom-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/errors/boom-ai-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/boom-ai-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/lifecycle/boom-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/boom-ai-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.useboom.ai/
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/sandbox/boom-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/boom-ai-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/conventions/boom-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/boom-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/conventions/boom-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/boom-ai-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/rate-limits/boom-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/boom-ai-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/changelog/boom-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/boom-ai-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/data-model/boom-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/boom-ai-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/a2a/boom-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/boom-ai-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/mcp/boom-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/boom-ai-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/well-known/boom-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boom-ai-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/scopes/boom-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/boom-ai-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/packages/boom-ai-packages.yml
  title: ''
  type: Packages
  url: packages/boom-ai-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/plans/boom-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boom-ai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/asyncapi/boom-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/boom-ai-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/security/boom-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/boom-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.useboom.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BOOM-TML
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/BOOM-TML/skills
created: '2026-07-17'
description: Boom AI (useboom.ai) is a Y Combinator-backed (Fall 2025) San Francisco company building "an AI workforce for your customers" — autonomous agents that hold real, multi-turn conversations over SMS, email, WhatsApp, and phone in 50+ languages to run collections and payment recovery, churn recovery, retention monitoring, customer onboarding, sales qualification, and market research for e-commerce and B2B brands. Boom exposes one uniform public REST API — and a hosted MCP server over the same capabilities — covering a customer data platform (people, custom objects, behavioral events, relationships, sources), segments, initiatives and participants, and journey authoring. Authentication is a Bearer organization API key (boom_org_...); the API uses cursor pagination, 1,000 requests/minute rate limits with X-RateLimit-*/Retry-After signaling, and idempotent upsert plus up-to-1000-record batch endpoints.
image: https://useboom.ai/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Boom Ai MCP Server
  slug: boom-ai-mcp-server
modified: '2026-08-13'
name: Boom Ai
nav: Providers
network: true
overview: 'Boom Ai publishes 11 APIs on the [APIs.io](https://apis.io/) network, including CDP Custom Objects API, CDP Events API, CDP People API, and 8 more. Tagged areas include Company, Artificial Intelligence, Conversational AI, Customer Engagement, and Customer Data Platform.


  The Boom Ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Boom Ai''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 36 more developer resources.'
plans:
- name: Boom Ai Plans Pricing
  plan_count: 4
  slug: boom-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Boom Ai Rate Limits
  slug: boom-ai-rate-limits
scopes:
- name: Boom Ai Scopes
  scope_count: 7
  slug: boom-ai-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: exemplar
  composite: 75.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 57.0
    developer_ergonomics: 71.4
    discoverability: 75.0
    operational_transparency: 55.3
  previous_composite: 75.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 36.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://raw.githubusercontent.com/api-evangelist/boom-ai/refs/heads/main/screenshots/boom-ai-2026-07-25T203612.png
security:
- kind: authentication
  name: Boom Ai Authentication
  slug: boom-ai-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Boom Ai Domain Security
  slug: boom-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Boom Ai Trust Center
  slug: boom-ai-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
slug: boom-ai
tags:
- Company
- Artificial Intelligence
- Conversational AI
- Customer Engagement
- Customer Data Platform
- Messaging
- WhatsApp
- SMS
- Marketing Automation
- E-Commerce
- Agents
- MCP
- A2A
website: https://www.useboom.ai/
---

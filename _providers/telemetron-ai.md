---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Telemetron Ai Agentic Access
  operation_count: 10
  slug: telemetron-ai-agentic-access
  summary_line: 10 operations · 9 acting
api_count: 4
apis:
- baseURL: https://admin.telemetron.ai/api/ext-v1
  baseurl_source: declared
  description: Create, update, and query customer records.
  name: Telemetron Customer API
  slug: telemetron-ai-customer-api
- baseURL: https://admin.telemetron.ai/api/ext-v1
  baseurl_source: declared
  description: Register and update devices; bulk-update device metadata.
  name: Telemetron Device API
  slug: telemetron-ai-device-api
- baseURL: https://admin.telemetron.ai/api/ext-v1
  baseurl_source: declared
  description: Map devices to customers for telemetry routing.
  name: Telemetron Device Assignment API
  slug: telemetron-ai-device-assignment-api
- baseURL: https://admin.telemetron.ai/api/ext-v1
  baseurl_source: declared
  description: Create support tickets.
  name: Telemetron Ticket API
  slug: telemetron-ai-ticket-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Telemetron External API (ext-v1) Customer API
  slug: open-telemetron-ai-customer-api
- collection_type: open
  name: Telemetron External API (ext-v1) Customer Device API
  slug: open-telemetron-ai-device-api
- collection_type: open
  name: Telemetron External API (ext-v1) Customer Device Assignment API
  slug: open-telemetron-ai-device-assignment-api
- collection_type: open
  name: Telemetron External API (ext-v1) Customer Ticket API
  slug: open-telemetron-ai-ticket-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/telemetron-ai-ext-v1-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telemetron-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telemetron-ai-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/telemetron-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telemetron-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/telemetron-ai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telemetron-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/telemetron-ai-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/telemetron-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/telemetron-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/telemetron-ai-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/telemetron-ai-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/telemetron-ai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.telemetron.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.telemetron.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.telemetron.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.telemetron.ai/api-reference/getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:support@telemetron.ai
- group: company
  title: ''
  type: Blog
  url: https://www.telemetron.ai/blog
- group: start
  title: ''
  type: Login
  url: https://admin.telemetron.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telemetron.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telemetron.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.telemetron.ai/
created: '2026-07-17'
description: Telemetron is an AI-powered customer support platform for hardware companies, backed by Y Combinator. It connects to IoT devices in real time, correlates device telemetry with customer records, diagnoses issues with AI, and resolves support tickets automatically. Its External API (ext-v1) lets hardware companies sync customers, devices, and ownership mappings into the platform, and an official hosted MCP server exposes org-scoped support tools (case lookup, customer search, device queries) to AI agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telemetron-ai.png
layout: provider
mcp_servers:
- description: 'Telemetron operates an official hosted MCP server at https://admin.telemetron.ai/api/mcp over HTTP transport, authenticated with the organization''s API key sent as an Authorization: Bearer token. The '
  name: Telemetron MCP Server
  slug: telemetron-mcp-server
modified: '2026-07-21'
name: Telemetron
nav: Providers
network: true
overview: 'Telemetron publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Customer API, Device API, Device Assignment API, and 1 more. Tagged areas include Company, Artificial Intelligence, Customer-Support, Internet of Things, and Hardware.


  Telemetron''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 18 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 26.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telemetron-ai/refs/heads/main/screenshots/telemetron-ai-2026-08-17T082304.png
security:
- kind: authentication
  name: Telemetron Ai Authentication
  slug: telemetron-ai-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Telemetron Ai Domain Security
  slug: telemetron-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telemetron-ai
tags:
- Company
- Artificial Intelligence
- Customer-Support
- Internet of Things
- Hardware
- Telemetry
- Support Tickets
- MCP
website: https://www.telemetron.ai/
---

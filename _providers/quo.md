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
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Operations related to calls
  name: Quo Calls API
  slug: quo-calls-api
- description: The Contact Custom Fields API from Quo — 1 operation(s) for contact custom fields.
  name: Quo Contact Custom Fields API
  slug: quo-contact-custom-fields-api
- description: Operations related to contacts
  name: Quo Contacts API
  slug: quo-contacts-api
- description: Operations related to conversations
  name: Quo Conversations API
  slug: quo-conversations-api
- description: Operations related to text messages
  name: Quo Messages API
  slug: quo-messages-api
- description: Operations related to phone numbers
  name: Quo Phone Numbers API
  slug: quo-phone-numbers-api
- description: The Tasks API from Quo — 10 operation(s) for tasks.
  name: Quo Tasks API
  slug: quo-tasks-api
- description: Operations related to users
  name: Quo Users API
  slug: quo-users-api
- description: Operations related to webhooks
  name: Quo Webhooks API
  slug: quo-webhooks-api
artifact_total: 24
asyncapis:
- description: ''
  name: Quo Webhooks
  slug: quo-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quo Public Calls API
  slug: open-quo-calls-api
- collection_type: open
  name: Quo Public Calls Contact Custom Fields API
  slug: open-quo-contact-custom-fields-api
- collection_type: open
  name: Quo Public Calls Contacts API
  slug: open-quo-contacts-api
- collection_type: open
  name: Quo Public Calls Conversations API
  slug: open-quo-conversations-api
- collection_type: open
  name: Quo Public Calls Messages API
  slug: open-quo-messages-api
- collection_type: open
  name: Quo Public Calls Phone Numbers API
  slug: open-quo-phone-numbers-api
- collection_type: open
  name: Quo Public Calls Tasks API
  slug: open-quo-tasks-api
- collection_type: open
  name: Quo Public Calls Users API
  slug: open-quo-users-api
- collection_type: open
  name: Quo Public Calls Webhooks API
  slug: open-quo-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/quo-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/quo-public-api-v1-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://quo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.quo.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.quo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.quo.com/docs/mdx/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.quo.com/docs/mdx/api-reference/send-your-first-message
- group: operate
  title: ''
  type: Support
  url: https://support.quo.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quo.com/docs/mdx/pricing-support/pricing-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quo.com/docs/mdx/pricing-support/terms-of-service
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.quo.com/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quo-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/quo-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quo-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quo-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/quo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/quo-trust-center.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/quo-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/quo-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/quo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Quo (formerly OpenPhone) is an AI-powered business communication platform that unifies calls, texts, and contacts in one shared workspace for startups and small businesses. Its REST Public API (https://api.quo.com/v1) lets developers send and receive SMS, manage contacts, conversations, and tasks, retrieve AI-generated call summaries and transcripts, and subscribe to Standard-Webhooks-signed events for messages and calls. Authentication is via a workspace API key sent in the Authorization header. This profile was added to the API Evangelist network from VC portfolio discovery and enriched from Quo's live developer documentation and published OpenAPI.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quo.png
layout: provider
mcp_servers:
- description: Candidate Model Context Protocol tool surface derived from the Quo Public API v1 OpenAPI operations. Quo markets a "Quo MCP" capability on quo.com, but no hosted/remote MCP server endpoint or manifest
  name: Quo API MCP (candidate)
  slug: quo-api-mcp-candidate
modified: '2026-07-20'
name: Quo
nav: Providers
network: true
overview: 'Quo publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Contact Custom Fields API, Contacts API, and 6 more. Tagged areas include Company, Communications, Messaging, SMS, and Voice.


  The Quo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Quo''s developer surface includes documentation, API reference, getting-started guide, support, pricing, changelog, authentication, and 14 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 68.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 49.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 36.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quo/refs/heads/main/screenshots/quo-2026-08-17T081432.png
security:
- kind: authentication
  name: Quo Authentication
  slug: quo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Quo Domain Security
  slug: quo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Quo Trust Center
  slug: quo-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: quo
tags:
- Company
- Communications
- Messaging
- SMS
- Voice
- Contacts
- Webhook
website: https://quo.com
---

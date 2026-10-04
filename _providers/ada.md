---
access_model:
  confidence: high
  label: Enterprise · Sales-led onboarding
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - https://www.ada.cx/
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: templated
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.3
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Ada Agentic Access
  operation_count: 45
  slug: ada-agentic-access
  summary_line: 45 operations · 26 acting
api_count: 4
apis:
- description: Model Context Protocol server exposing Ada's management surface to AI assistants — metrics, conversation transcripts, knowledge and coaching search, entity discovery, test cases and runs, change sets,
  name: Ada MCP Server
  slug: ada-mcp-server
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The channels API from Ada — 2 operation(s) for channels.
  name: Ada Channels API
  phrasing_intents:
  - id: get-channels
    intent: List messaging channels
    question: Which channels are set up for my AI Agent?
  - id: create-channel
    intent: Create a custom channel
    question: How do I add a new custom channel for my Ada AI Agent?
  - id: update-channel
    intent: Change a custom channel's capabilities
    question: How do I change what an existing custom channel can render?
  phrasing_ops: 3
  slug: ada-channels-api
- baseURL: https://{handle}.ada.support/api/v2
  baseurl_source: declared
  description: Read and manage conversations handled by the Ada AI Agent across all supported channels.
  name: Ada Conversations API
  phrasing_intents:
  - id: get-conversations
    intent: Export conversations in bulk (v2 export)
    question: How do I export conversations created in a date range from the v2 export endpoint?
  - id: return-conversations-matching-the-parameters
    intent: Export conversations via the legacy Data API v1.4
    question: How do I pull conversations from the older Data API v1.4?
  - id: create-email-conversation
    intent: Start an email conversation with a customer
    question: Can my AI Agent email a customer first to start a conversation?
  - id: create-conversation
    intent: Start a conversation on a custom channel
    question: How do I start a new conversation on my custom channel?
  - id: get-conversation-by-id
    intent: Look up one conversation
    question: How do I look up the details of a single conversation by its id?
  - id: patch-conversation-by-id
    intent: Add metadata to a conversation
    question: How do I attach extra metadata to a conversation that's already running?
  - id: fetch-conversation-messages-by-id
    intent: Read the messages in one conversation
    question: How can I read the full message history of one conversation?
  - id: create-message
    intent: Send a message into a conversation
    question: How do I post an end user's message into an ongoing conversation?
  phrasing_ops: 11
  slug: ada-conversations-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The customInstructions API from Ada — 2 operation(s) for custominstructions.
  name: Ada Custom Instructions API
  phrasing_intents:
  - id: list-custom-instructions
    intent: List the AI Agent's custom instructions
    question: What custom instructions is my AI Agent following right now?
  - id: create-custom-instruction
    intent: Add a custom instruction
    question: How do I give my Ada AI Agent a new rule to follow?
  - id: get-custom-instruction-by-id
    intent: Look up one custom instruction
    question: How can I view the full text and notes of one custom instruction?
  - id: delete-custom-instruction
    intent: Delete a custom instruction
    question: How do I permanently remove a custom instruction from my AI Agent?
  - id: update-custom-instruction
    intent: Edit or toggle a custom instruction
    question: How do I turn an existing custom instruction on or off?
  phrasing_ops: 5
  slug: ada-custominstructions-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The deleteChatterData API from Ada — 1 operation(s) for deletechatterdata.
  name: Ada Delete Chatter Data API
  phrasing_intents:
  - id: delete-all-data-associated-with-a-chatters-email-address
    intent: Erase a chatter's data by email address
    question: How do I honor a GDPR erasure request for a chatter using their email address?
  phrasing_ops: 1
  slug: ada-deletechatterdata-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The getDeletionJob API from Ada — 1 operation(s) for getdeletionjob.
  name: Ada Get Deletion Job API
  phrasing_intents:
  - id: get-a-deletion-job
    intent: Check a bulk deletion job's status
    question: How do I check whether my end-user erasure request has finished?
  phrasing_ops: 1
  slug: ada-getdeletionjob-api
- baseURL: https://{handle}.ada.support/api/v2
  baseurl_source: declared
  description: Manage knowledge sources, articles, and tags that Ada's AI Agent uses to ground answers to customer questions.
  name: Ada Knowledge API
  slug: ada-knowledge-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The knowledge > articles API from Ada — 3 operation(s) for knowledge > articles.
  name: Ada knowledge > articles API
  phrasing_intents:
  - id: list
    intent: List knowledge articles
    question: Which knowledge articles does my AI Agent have?
  - id: delete
    intent: Bulk delete knowledge articles by filter
    question: How do I delete every article from one knowledge source at once?
  - id: get
    intent: Get one knowledge article
    question: How do I read the content of a single knowledge article?
  - id: delete-by-id
    intent: Delete one knowledge article
    question: How do I remove a single outdated article from the knowledge base?
  - id: bulk-upsert
    intent: Create or update knowledge articles in bulk
    question: How do I sync my help center articles into the AI Agent's knowledge base?
  phrasing_ops: 5
  slug: ada-knowledge-articles-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The knowledge > sources API from Ada — 2 operation(s) for knowledge > sources.
  name: Ada knowledge > sources API
  phrasing_intents:
  - id: list
    intent: List knowledge sources
    question: Which knowledge sources feed my AI Agent?
  - id: create
    intent: Create a knowledge source
    question: How do I set up a new knowledge source for articles I'll upload?
  - id: delete
    intent: Delete a knowledge source and its articles
    question: How do I remove a whole knowledge source along with its articles?
  - id: update
    intent: Rename or edit a knowledge source
    question: How do I rename an existing knowledge source?
  phrasing_ops: 4
  slug: ada-knowledge-sources-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The knowledge > tags API from Ada — 3 operation(s) for knowledge > tags.
  name: Ada knowledge > tags API
  phrasing_intents:
  - id: list
    intent: List article tags
    question: What tags are available for organizing knowledge articles?
  - id: delete
    intent: Delete an article tag
    question: How do I remove an article tag I no longer use?
  - id: upsert-multiple
    intent: Create or update article tags in bulk
    question: How do I create several article tags in one request?
  phrasing_ops: 3
  slug: ada-knowledge-tags-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The messages API from Ada — 2 operation(s) for messages.
  name: Ada Messages API
  phrasing_intents:
  - id: get-messages
    intent: Export messages in bulk (v2 export)
    question: How do I export all messages created in a date range from the v2 export?
  - id: return-messages-matching-the-parameters
    intent: Export messages via the legacy Data API v1.4
    question: How do I pull messages from the older Data API v1.4?
  phrasing_ops: 2
  slug: ada-messages-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The persona API from Ada — 1 operation(s) for persona.
  name: Ada Persona API
  phrasing_intents:
  - id: get-persona
    intent: View the AI Agent's persona settings
    question: What personality and tone is my AI Agent currently set to?
  - id: update-persona
    intent: Change the AI Agent's persona
    question: How do I change my AI Agent's personality or tone?
  phrasing_ops: 2
  slug: ada-persona-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The platformIntegrations API from Ada — 4 operation(s) for platformintegrations.
  name: Ada Platform Integrations API
  phrasing_intents:
  - id: get-platform-integrations
    intent: List my platform integrations
    question: Which platform integrations has my developer account built?
  - id: create-platform-integration
    intent: Register a new platform integration
    question: How do I build and register an integration for the Ada platform?
  - id: update-single-platform-integration
    intent: Edit an integration still in development
    question: How do I change the details of an integration I'm still developing?
  - id: get-platform-integration-installation-self
    intent: Get the installation behind my access token
    question: How does my integration read the configuration an admin filled in on install?
  - id: update-platform-integration-installation
    intent: Mark an installation complete or incomplete
    question: How do I tell Ada an installation of my integration finished setup?
  phrasing_ops: 5
  slug: ada-platformintegrations-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The submitDeletionRequest API from Ada — 1 operation(s) for submitdeletionrequest.
  name: Ada Submit Deletion Request API
  phrasing_intents:
  - id: submit-a-bulk-end-user-deletion-request
    intent: Request bulk erasure of end users' data
    question: How do I erase personal data for many end users in one request?
  phrasing_ops: 1
  slug: ada-submitdeletionrequest-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The Variables API from Ada — 2 operation(s) for variables.
  name: Ada Variables API
  phrasing_intents:
  - id: list
    intent: List the AI Agent's variables
    question: Which variables can my AI Agent use?
  - id: get
    intent: Get one variable
    question: How do I look up a single variable by its id?
  phrasing_ops: 2
  slug: ada-variables-api
- description: Configure and invoke Actions, the integration layer that lets the Ada AI Agent call external systems and APIs during a conversation.
  name: Ada Integrations (Actions) API
  slug: ada-integrations-api
- description: Export conversation, message, and analytics data from Ada to data warehouses and BI tooling.
  name: Ada Data Export API
  slug: ada-data-export-api
- description: Run data subject access requests, data deletion, and other compliance operations across the Ada platform.
  name: Ada Data Compliance API
  slug: ada-data-compliance-api
- description: Configure and consume webhooks that notify external systems of conversation lifecycle events and other platform activity.
  name: Ada Webhooks API
  slug: ada-webhooks-api
- baseURL: https://example.ada.support/api/mcp
  baseurl_source: declared
  description: The Audit Log API from Ada — 1 operation(s) for audit log.
  name: Ada Audit Log API
  phrasing_intents:
  - id: list-audit-log-events
    intent: Pull the account's audit log events
    question: How can I pull my Ada account's audit log into our SIEM?
  phrasing_ops: 1
  slug: ada-audit-log-api
- baseURL: https://example.ada.support/api/mcp
  baseurl_source: declared
  description: The End Users API from Ada — 2 operation(s) for end users.
  name: Ada End Users API
  phrasing_intents:
  - id: get-end-user-by-id
    intent: Look up an end user by Ada id
    question: How do I view the profile of one end user using their Ada id?
  - id: patch-end-user-by-id
    intent: Update an end user's profile
    question: How do I change the profile details of an existing end user?
  - id: get-end-users
    intent: List end users or find one by external id
    question: How can I page through all the end users my AI Agent has talked to?
  - id: create-end-user
    intent: Create an end user before a conversation
    question: How do I give the AI Agent a customer's context before the first message?
  phrasing_ops: 4
  slug: ada-end-users-api
- baseURL: https://example.ada.support/api/mcp
  baseurl_source: declared
  description: The Webhook Management API from Ada — 5 operation(s) for webhook management.
  name: Ada Webhook Management API
  phrasing_intents:
  - id: list-webhooks
    intent: List webhook subscriptions
    question: What webhooks are configured for my AI Agent?
  - id: create-webhook
    intent: Subscribe a URL to webhook events
    question: How do I get Ada to send events to my server?
  - id: get-webhook
    intent: Get a webhook's details
    question: How do I check which URL and events one webhook is set to?
  - id: delete-webhook
    intent: Delete a webhook subscription
    question: How do I stop sending events to an endpoint permanently?
  - id: update-webhook
    intent: Change or disable a webhook
    question: How do I pause a webhook without deleting it?
  - id: get-webhook-secret
    intent: Get a webhook's signing secret
    question: How do I verify that incoming webhook payloads really came from Ada?
  - id: rotate-webhook-secret
    intent: Rotate a webhook's signing secret
    question: How do I rotate a webhook signing secret that may have leaked?
  - id: list-webhook-event-types
    intent: List subscribable webhook event types
    question: Which event types can a webhook subscribe to?
  phrasing_ops: 8
  slug: ada-webhook-management-api
artifact_total: 51
asyncapis:
- description: ''
  name: Ada Webhooks
  slug: ada-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Data Compliance subpackage_channels API
  slug: open-ada-subpackage-channels-api
- collection_type: open
  name: Data Compliance subpackage_channels subpackage_conversations API
  slug: open-ada-subpackage-conversations-api
- collection_type: open
  name: Data Compliance subpackage_channels subpackage_deleteChatterData API
  slug: open-ada-subpackage-deletechatterdata-api
- collection_type: open
  name: Data Compliance subpackage_channels subpackage_endUsers API
  slug: open-ada-subpackage-endusers-api
- collection_type: open
  name: Data Compliance subpackage_channels subpackage_knowledge.subpackage_knowledge/articles API
  slug: open-ada-subpackage-knowledge-subpackage-knowledge-articles-api
- collection_type: open
  name: Data Compliance subpackage_channels subpackage_knowledge.subpackage_knowledge/sources API
  slug: open-ada-subpackage-knowledge-subpackage-knowledge-sources-api
- collection_type: open
  name: Data Compliance subpackage_channels subpackage_knowledge.subpackage_knowledge/tags API
  slug: open-ada-subpackage-knowledge-subpackage-knowledge-tags-api
- collection_type: open
  name: Data Compliance subpackage_channels subpackage_messages API
  slug: open-ada-subpackage-messages-api
- collection_type: open
  name: Data Compliance subpackage_channels subpackage_platformIntegrations API
  slug: open-ada-subpackage-platformintegrations-api
- collection_type: open
  name: Data Compliance subpackage_channels subpackage_webhookManagement API
  slug: open-ada-subpackage-webhookmanagement-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/overlays/ada-subpackage-channels-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-channels-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/overlays/ada-subpackage-conversations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-conversations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/overlays/ada-subpackage-deletechatterdata-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-deletechatterdata-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/overlays/ada-subpackage-endusers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-endusers-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/overlays/ada-subpackage-knowledge-subpackage-knowledge-sources-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-knowledge-subpackage-knowledge-sources-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/overlays/ada-subpackage-knowledge-subpackage-knowledge-tags-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-knowledge-subpackage-knowledge-tags-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/overlays/ada-subpackage-messages-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-messages-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/overlays/ada-subpackage-platformintegrations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-platformintegrations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/overlays/ada-subpackage-webhookmanagement-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-webhookmanagement-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/agentic-access/ada-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ada-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/security/ada-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/ada-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/security/ada-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ada-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/security/ada-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ada-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/authentication/ada-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ada-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ada.cx/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ada.cx/reference/introduction/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adasupport
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/ada-cx
- group: company
  title: ''
  type: Blog
  url: https://www.ada.cx/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ada.cx/platform/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ada.support/
- group: other
  title: ''
  type: X
  url: https://x.com/ada_cx
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/plans/ada-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ada-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/rate-limits/ada-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ada-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/finops/ada-finops.yml
  title: ''
  type: FinOps
  url: finops/ada-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/vocabulary/ada-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ada-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/json-ld/ada-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/ada-context.jsonld
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ada.cx/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ada.cx/generative/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ada.cx/docs/welcome/getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:help@ada.cx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ada.cx/legal/customer-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ada.cx/legal/privacy-policy/
- group: start
  title: ''
  type: Demo
  url: https://www.ada.cx/demo/
- group: start
  title: ''
  type: Login
  url: https://www.ada.cx/login/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ada_cx
- group: auth
  title: ''
  type: Security
  url: https://www.ada.cx/legal/vulnerability-disclosure/
- group: auth
  title: ''
  type: Compliance
  url: https://security.ada.cx/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/packages/ada-packages.yml
  title: ''
  type: Packages
  url: packages/ada-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/packages/ada-packages.yml
  title: ''
  type: SDKs
  url: packages/ada-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/cli/ada-cli.yml
  title: ''
  type: CLI
  url: cli/ada-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/components/ada-components.yml
  title: ''
  type: Components
  url: components/ada-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/sandbox/ada-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ada-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/conventions/ada-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ada-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/conventions/ada-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ada-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/errors/ada-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ada-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/lifecycle/ada-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ada-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ada.cx/reference/introduction/migrate-to-v-2
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/changelog/ada-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ada-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.ada.cx/release-notes
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/conformance/ada-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ada-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/data-model/ada-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ada-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/scopes/ada-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ada-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/well-known/ada-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ada-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.ada.cx/.well-known/api-catalog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/llms/ada-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ada-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/mcp/ada-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ada-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/mcp/ada-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ada-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/asyncapi/ada-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ada-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/overlays/ada-subpackage-knowledge-subpackage-knowledge-articles-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-knowledge-subpackage-knowledge-articles-overlay.yaml
created: 2026-06-12
description: Ada is an AI-powered customer service automation platform that enables enterprises to deploy AI agents capable of resolving customer inquiries across digital channels without human intervention. The platform exposes a suite of REST APIs for managing knowledge bases, end-user profiles, conversation handling, data export, data compliance, and external integrations. All APIs use rotatable API keys for authentication, return JSON, and support cursor-based pagination. Ada serves global brands including Pinterest, Square, Ancestry, and Zendesk, and has powered more than 6.4 billion customer interactions since its founding in 2016.
examples:
- key_count: 8
  name: Ada Knowledge Examples
  slug: ada-knowledge-examples
finops:
- name: Ada Finops
  service_category: ''
  slug: ada-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ada.png
json_schemas:
- name: Ada Data Compliance Schemas
  property_count: 0
  slug: ada-data-compliance-schemas
- name: Ada Data Export Schemas
  property_count: 0
  slug: ada-data-export-schemas
- name: Ada Data Export V1 4 Schemas
  property_count: 0
  slug: ada-data-export-v1-4-schemas
- name: Ada Knowledge Schemas
  property_count: 0
  slug: ada-knowledge-schemas
jsonld:
- class_count: 9
  name: Ada Context
  property_count: 24
  slug: ada-context
layout: provider
mcp_servers:
- description: ''
  name: Ada MCP Server
  slug: ada-mcp-server
modified: 2026-08-14
name: Ada
nav: Providers
network: true
overview: 'Ada publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Conversations API, Custom Instructions API, and 19 more. Tagged areas include Artificial Intelligence, Customer Service, Chatbots, Automation, and Conversational AI.


  The Ada catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Ada''s developer surface includes authentication, documentation, engineering blog, pricing, API reference, getting-started guide, support, and 54 more developer resources.'
plans:
- name: Ada Plans Pricing
  plan_count: 1
  slug: ada-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Ada Rate Limits
  slug: ada-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Ada API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ada-jsonschema-spectral-rules
scopes:
- name: Ada Scopes
  scope_count: 8
  slug: ada-scopes
  summary_line: 8 scopes · authorizationCode/refreshToken
score:
  band: exemplar
  composite: 84.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 69.8
    catalog_earned_first_party: 8.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 82.9
    contract_governance: 41.7
    contract_quality: 65.0
    developer_ergonomics: 85.7
    discoverability: 83.3
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 84.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: CA
      standard: pipeda
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: cpra
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 3
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/screenshots/ada-2026-06-20T164442.png
security:
- kind: authentication
  name: Ada Authentication
  slug: ada-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Ada Domain Security
  slug: ada-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ada Vulnerability Disclosure
  slug: ada-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Ada Trust Center
  slug: ada-trust-center
  summary_line: SOC 2 Type 2, SOC 3, PCI DSS (Attestation of Compliance), HIPAA, GDPR, CCPA, CPRA, PIPEDA, VPAT 2024 (WCAG 2.1 AA)
slug: ada
tags:
- Artificial Intelligence
- Customer Service
- Chatbots
- Automation
- Conversational AI
- Help Desk
- CRM
- Integration
- Knowledge Management
- Data Export
- Canada
website: https://www.ada.cx/
---

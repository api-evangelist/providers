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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Ada Agentic Access
  operation_count: 45
  slug: ada-agentic-access
  summary_line: 45 operations · 26 acting
api_count: 4
apis:
- description: Real-time management of end-user profile information with webhook events for new chats and profile updates.
  name: Ada End Users API
  slug: ada-end-users-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: Build custom channels and extend Ada into proprietary apps or third-party platforms with full conversation lifecycle control.
  name: Ada Conversations API
  slug: ada-conversations-api
- description: Connect external applications to Ada using OAuth to extend AI agent capabilities with partner-built integrations.
  name: Ada Integrations API
  slug: ada-integrations-api
- description: Model Context Protocol server exposing Ada's management surface to AI assistants — metrics, conversation transcripts, knowledge and coaching search, entity discovery, test cases and runs, change sets,
  name: Ada MCP Server
  slug: ada-mcp-server
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The auditLog API from Ada — 1 operation(s) for auditlog.
  name: Ada Audit Log API
  slug: ada-auditlog-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The channels API from Ada — 2 operation(s) for channels.
  name: Ada Channels API
  slug: ada-channels-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The conversations API from Ada — 9 operation(s) for conversations.
  name: Ada Conversations API
  slug: ada-conversations-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The customInstructions API from Ada — 2 operation(s) for custominstructions.
  name: Ada Custom Instructions API
  slug: ada-custominstructions-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The deleteChatterData API from Ada — 1 operation(s) for deletechatterdata.
  name: Ada Delete Chatter Data API
  slug: ada-deletechatterdata-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The endUsers API from Ada — 2 operation(s) for endusers.
  name: Ada End Users API
  slug: ada-endusers-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The getDeletionJob API from Ada — 1 operation(s) for getdeletionjob.
  name: Ada Get Deletion Job API
  slug: ada-getdeletionjob-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The Knowledge API from Ada — 0 operation(s) for knowledge.
  name: Ada Knowledge API
  slug: ada-knowledge-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The knowledge > articles API from Ada — 3 operation(s) for knowledge > articles.
  name: Ada knowledge > articles API
  slug: ada-knowledge-articles-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The knowledge > sources API from Ada — 2 operation(s) for knowledge > sources.
  name: Ada knowledge > sources API
  slug: ada-knowledge-sources-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The knowledge > tags API from Ada — 3 operation(s) for knowledge > tags.
  name: Ada knowledge > tags API
  slug: ada-knowledge-tags-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The messages API from Ada — 2 operation(s) for messages.
  name: Ada Messages API
  slug: ada-messages-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The persona API from Ada — 1 operation(s) for persona.
  name: Ada Persona API
  slug: ada-persona-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The platformIntegrations API from Ada — 4 operation(s) for platformintegrations.
  name: Ada Platform Integrations API
  slug: ada-platformintegrations-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The submitDeletionRequest API from Ada — 1 operation(s) for submitdeletionrequest.
  name: Ada Submit Deletion Request API
  slug: ada-submitdeletionrequest-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The Variables API from Ada — 2 operation(s) for variables.
  name: Ada Variables API
  slug: ada-variables-api
- baseURL: https://example.ada.support
  baseurl_source: declared
  description: The webhookManagement API from Ada — 5 operation(s) for webhookmanagement.
  name: Ada Webhook Management API
  slug: ada-webhookmanagement-api
- description: The Ada REST API is the unified v2 interface to the Ada AI customer service platform. It covers knowledge sources and articles, end users, conversations, integrations (Actions), data export, data comp
  name: Ada REST API
  slug: ada-rest-api
- baseURL: https://{handle}.ada.support/api/v2
  baseurl_source: declared
  description: Manage knowledge sources, articles, and tags that Ada's AI Agent uses to ground answers to customer questions.
  name: Ada Knowledge API
  slug: ada-knowledge-api
- baseURL: https://{handle}.ada.support/api/v2
  baseurl_source: declared
  description: Read and manage conversations handled by the Ada AI Agent across all supported channels.
  name: Ada Conversations API
  slug: ada-conversations-api
- description: Create, look up, and update end users (customers) along with their metadata for use by Ada's AI Agent and Actions.
  name: Ada End Users API
  slug: ada-end-users-api
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
artifact_total: 59
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
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-channels-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-conversations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-deletechatterdata-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-endusers-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-knowledge-subpackage-knowledge-sources-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-knowledge-subpackage-knowledge-tags-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-messages-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-platformintegrations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/ada-subpackage-webhookmanagement-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ada-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ada-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ada-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ada-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/ada-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ada-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ada-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ada-vocabulary.yml
- group: design
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
  title: ''
  type: Packages
  url: packages/ada-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ada-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ada-cli.yml
- group: design
  title: ''
  type: Components
  url: components/ada-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ada-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ada-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ada-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ada-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ada-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ada.cx/reference/introduction/migrate-to-v-2
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ada-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.ada.cx/release-notes
- group: design
  title: ''
  type: Conformance
  url: conformance/ada-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ada-data-model.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ada-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ada-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.ada.cx/.well-known/api-catalog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ada-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ada-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ada-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ada-webhooks.yml
- group: other
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
graphqls:
- description: '> **NOT A PUBLISHED ADA CONTRACT.** Ada publishes no GraphQL API. Verified 2026-08-14: no'
  name: Ada GraphQL API
  slug: ada-graphql
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
overview: 'Ada publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Conversations API, Audit Log API, Channels API, and 18 more. Tagged areas include Artificial Intelligence, Customer Service, Chatbots, Automation, and Conversational AI.


  The Ada catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Ada''s developer surface includes authentication, documentation, engineering blog, pricing, API reference, getting-started guide, support, and 54 more developer resources.'
plans:
- name: Ada Plans Pricing
  plan_count: 1
  slug: ada-plans-pricing
random_paper: 0
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
  composite: 73.9
  coverage:
    artifact_dirs: 33
    catalog_gap: 44.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 82.9
    commercial_clarity: 82.9
    contract_governance: 43.2
    contract_quality: 71.6
    developer_ergonomics: 85.7
    discoverability: 92.6
    governance: 43.2
    operational_transparency: 60.5
  previous_composite: 73.9
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
- Knowledge-Management
- Data Export
website: https://www.ada.cx/
---

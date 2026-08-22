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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 56.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Ada Agentic Access
  operation_count: 45
  slug: ada-agentic-access
  summary_line: 45 operations · 26 acting
api_count: 14
apis:
- description: Real-time management of end-user profile information with webhook events for new chats and profile updates.
  name: Ada End Users API
  slug: ada-end-users-api
- description: Build custom channels and extend Ada into proprietary apps or third-party platforms with full conversation lifecycle control.
  name: Ada Conversations API
  slug: ada-conversations-api
- description: Connect external applications to Ada using OAuth to extend AI agent capabilities with partner-built integrations.
  name: Ada Integrations API
  slug: ada-integrations-api
- description: Model Context Protocol server exposing Ada's management surface to AI assistants — metrics, conversation transcripts, knowledge and coaching search, entity discovery, test cases and runs, change sets,
  name: Ada MCP Server
  slug: ada-mcp-server
- description: The subpackage_channels API from Ada — 1 operation(s) for subpackage_channels.
  name: Ada subpackage_channels API
  slug: ada-subpackage-channels-api
- description: The subpackage_conversations API from Ada — 9 operation(s) for subpackage_conversations.
  name: Ada subpackage_conversations API
  slug: ada-subpackage-conversations-api
- description: The subpackage_deleteChatterData API from Ada — 1 operation(s) for subpackage_deletechatterdata.
  name: Ada subpackage_deleteChatterData API
  slug: ada-subpackage-deletechatterdata-api
- description: The subpackage_endUsers API from Ada — 2 operation(s) for subpackage_endusers.
  name: Ada subpackage_endUsers API
  slug: ada-subpackage-endusers-api
- description: The subpackage_knowledge.subpackage_knowledge/articles API from Ada — 3 operation(s) for subpackage_knowledge.subpackage_knowledge/articles.
  name: Ada subpackage_knowledge.subpackage_knowledge/articles API
  slug: ada-subpackage-knowledge-subpackage-knowledge-articles-api
- description: The subpackage_knowledge.subpackage_knowledge/sources API from Ada — 2 operation(s) for subpackage_knowledge.subpackage_knowledge/sources.
  name: Ada subpackage_knowledge.subpackage_knowledge/sources API
  slug: ada-subpackage-knowledge-subpackage-knowledge-sources-api
- description: The subpackage_knowledge.subpackage_knowledge/tags API from Ada — 3 operation(s) for subpackage_knowledge.subpackage_knowledge/tags.
  name: Ada subpackage_knowledge.subpackage_knowledge/tags API
  slug: ada-subpackage-knowledge-subpackage-knowledge-tags-api
- description: The subpackage_messages API from Ada — 2 operation(s) for subpackage_messages.
  name: Ada subpackage_messages API
  slug: ada-subpackage-messages-api
- description: The subpackage_platformIntegrations API from Ada — 4 operation(s) for subpackage_platformintegrations.
  name: Ada subpackage_platformIntegrations API
  slug: ada-subpackage-platformintegrations-api
- description: The subpackage_webhookManagement API from Ada — 5 operation(s) for subpackage_webhookmanagement.
  name: Ada subpackage_webhookManagement API
  slug: ada-subpackage-webhookmanagement-api
artifact_total: 44
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
  name: ada-mcp.yml
  slug: ada-mcpyml
modified: 2026-08-14
name: Ada
nav: Providers
network: true
overview: 'Ada publishes 10 APIs on the [APIs.io](https://apis.io/) network, including subpackage_channels API, subpackage_conversations API, subpackage_deleteChatterData API, and 7 more. Tagged areas include ai, customer-service, chatbot, automation, and conversational-ai.


  The Ada catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Ada''s developer surface includes authentication, documentation, engineering blog, pricing, API reference, getting-started guide, support, and 45 more developer resources.'
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
  composite: 76.2
  delta: -6.1
  facets:
    access_clarity: 82.9
    commercial_clarity: 82.9
    contract_governance: 55.3
    contract_quality: 74.7
    developer_ergonomics: 85.7
    discoverability: 92.6
    governance: 55.3
    operational_transparency: 60.5
  previous_composite: 82.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
- ai
- customer-service
- chatbot
- automation
- conversational-ai
- helpdesk
- crm
- integrations
- knowledge-management
- data-export
website: https://www.ada.cx/
---

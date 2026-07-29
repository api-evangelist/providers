---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Ada Agentic Access
  operation_count: 45
  slug: ada-agentic-access
  summary_line: 45 operations · 26 acting
api_count: 13
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
artifact_total: 29
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
- description: Ada is an AI-powered customer service platform. The API covers bot configuration, conversation management, intents, responses, analytics, handoff to live agents, and multi-channel deployment for autom
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
modified: 2026-06-12
name: Ada
nav: Providers
network: true
overview: 'Ada publishes 10 APIs on the [APIs.io](https://apis.io/) network, including subpackage_channels API, subpackage_conversations API, subpackage_deleteChatterData API, and 7 more. Tagged areas include ai, customer-service, chatbot, automation, and conversational-ai.


  The Ada catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ada''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Ada Plans Pricing
  plan_count: 1
  slug: ada-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 0
  name: Ada Rate Limits
  slug: ada-rate-limits
rules:
- name: Ada API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ada-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.0
  delta: -3.9
  facets:
    commercial_clarity: 47.4
    contract_quality: 67.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ada/refs/heads/main/screenshots/ada-2026-06-20T164442.png
security:
- kind: authentication
  name: Ada Authentication
  slug: ada-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ada Domain Security
  slug: ada-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ada Vulnerability Disclosure
  slug: ada-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ada Trust Center
  slug: ada-trust-center
  summary_line: SOC 2, HIPAA, GDPR
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

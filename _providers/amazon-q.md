---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Q Agentic Access
  operation_count: 10
  slug: amazon-q-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 7
apis:
- description: API for Amazon Q Apps, a feature within Amazon Q Business that allows web experience users to create lightweight, purpose-built AI apps to fulfill specific tasks using their enterprise data. It suppor
  name: Amazon Q Business QApps API
  slug: amazon-q-business-qapps-api
- description: API for Amazon Q in Connect, a generative AI-powered customer service assistant integrated with Amazon Connect. It automatically detects customer intent during calls and chats using conversational ana
  name: Amazon Q Connect API
  slug: amazon-q-connect-api
- description: API for Amazon Q Developer in chat applications, which enables integration of Amazon Q Developer capabilities into messaging platforms. It provides descriptions, request parameters, and response forma
  name: Amazon Q Developer in Chat Applications API
  slug: amazon-q-developer-in-chat-applications-api
- description: The Applications API from Amazon Q — 2 operation(s) for applications.
  name: Amazon Q Applications API
  slug: amazon-q-applications-api
- description: The Conversations API from Amazon Q — 1 operation(s) for conversations.
  name: Amazon Q Conversations API
  slug: amazon-q-conversations-api
- description: The Data Sources API from Amazon Q — 1 operation(s) for data sources.
  name: Amazon Q Data Sources API
  slug: amazon-q-data-sources-api
- description: The Indices API from Amazon Q — 1 operation(s) for indices.
  name: Amazon Q Indices API
  slug: amazon-q-indices-api
artifact_total: 48
collections:
- collection_type: postman
  name: Amazon Q Business Applications API
  slug: postman-amazon-q-applications-api
- collection_type: postman
  name: Amazon Q Business Applications Conversations API
  slug: postman-amazon-q-conversations-api
- collection_type: postman
  name: Amazon Q Business Applications Data Sources API
  slug: postman-amazon-q-data-sources-api
- collection_type: postman
  name: Amazon Q Business Applications Indices API
  slug: postman-amazon-q-indices-api
- collection_type: open
  name: Amazon Q Business API
  slug: open-amazon-q
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-q/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-q-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-q-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-q-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-q-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-q-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/q/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/q/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/amazonq/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/aws/tag/amazon-q/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/q/faqs/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/q/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: start
  title: ''
  type: Portal
  url: https://console.aws.amazon.com/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: Community
  url: https://repost.aws/tags/TALmcXzmfeRaKOzrBowJ9cJQ/amazon-q
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-q-openapi-application-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-q-openapi-conversation-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-q-openapi-data-source-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-q-openapi-index-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-q-openapi-message-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-q-openapi-application-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-q-openapi-conversation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-q-openapi-data-source-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-q-openapi-index-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-q-openapi-message-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-q-openapi-application-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-q-openapi-conversation-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-q-openapi-data-source-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-q-openapi-index-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-q-openapi-message-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-q-openapi-application-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-q-openapi-conversation-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-q-openapi-data-source-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-q-openapi-index-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-q-openapi-message-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-q-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-q-vocabulary.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/amazon-q-openapi.yml
created: 2024-01-15 00:00:00+00:00
description: Amazon Q is a generative AI-powered assistant that helps with various tasks including answering questions, generating content, and taking actions based on your enterprise data and systems. It is available in multiple product variants including Amazon Q Business for enterprise knowledge, Amazon Q Developer for software development, and Amazon Q in Connect for customer service agents.
examples:
- key_count: 5
  name: Amazon Q Openapi Application Example
  slug: amazon-q-openapi-application-example
- key_count: 3
  name: Amazon Q Openapi Conversation Example
  slug: amazon-q-openapi-conversation-example
- key_count: 4
  name: Amazon Q Openapi Data Source Example
  slug: amazon-q-openapi-data-source-example
- key_count: 3
  name: Amazon Q Openapi Index Example
  slug: amazon-q-openapi-index-example
- key_count: 4
  name: Amazon Q Openapi Message Example
  slug: amazon-q-openapi-message-example
finops:
- name: Amazon Q Finops
  service_category: AI / Assistant
  slug: amazon-q-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-q.png
json_schemas:
- name: Application
  property_count: 5
  slug: amazon-q-application
- name: Conversation
  property_count: 3
  slug: amazon-q-conversation
- name: DataSource
  property_count: 4
  slug: amazon-q-datasource
- name: Index
  property_count: 3
  slug: amazon-q-index
- name: Message
  property_count: 4
  slug: amazon-q-message
- name: Application
  property_count: 5
  slug: amazon-q-openapi-application
- name: Conversation
  property_count: 3
  slug: amazon-q-openapi-conversation
- name: DataSource
  property_count: 4
  slug: amazon-q-openapi-data-source
- name: Index
  property_count: 3
  slug: amazon-q-openapi-index
- name: Message
  property_count: 4
  slug: amazon-q-openapi-message
json_structures:
- name: Amazon Q Openapi Application Structure
  property_count: 5
  slug: amazon-q-openapi-application-structure
- name: Amazon Q Openapi Conversation Structure
  property_count: 3
  slug: amazon-q-openapi-conversation-structure
- name: Amazon Q Openapi Data Source Structure
  property_count: 4
  slug: amazon-q-openapi-data-source-structure
- name: Amazon Q Openapi Index Structure
  property_count: 3
  slug: amazon-q-openapi-index-structure
- name: Amazon Q Openapi Message Structure
  property_count: 4
  slug: amazon-q-openapi-message-structure
- name: Amazon Q Structure
  property_count: 0
  slug: amazon-q-structure
jsonld:
- class_count: 1
  name: Amazon Q Openapi Application Context
  property_count: 5
  slug: amazon-q-openapi-application-context
- class_count: 1
  name: Amazon Q Openapi Conversation Context
  property_count: 3
  slug: amazon-q-openapi-conversation-context
- class_count: 1
  name: Amazon Q Openapi Data Source Context
  property_count: 4
  slug: amazon-q-openapi-data-source-context
- class_count: 1
  name: Amazon Q Openapi Index Context
  property_count: 3
  slug: amazon-q-openapi-index-context
- class_count: 1
  name: Amazon Q Openapi Message Context
  property_count: 4
  slug: amazon-q-openapi-message-context
layout: provider
modified: '2026-05-19'
name: Amazon Q
nav: Providers
network: true
overview: 'Amazon Q publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Conversations API, Data Sources API, and 1 more. Tagged areas include Artificial Intelligence, Assistant, Enterprise, and Generative AI.


  The Amazon Q catalog on APIs.io includes 5 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon Q''s developer surface includes authentication, developer portal, getting-started guide, documentation, engineering blog, FAQ, support, and 37 more developer resources.'
plans:
- name: Amazon Q Plans Pricing
  plan_count: 7
  slug: amazon-q-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Amazon Q Rate Limits
  slug: amazon-q-rate-limits
rules:
- name: Amazon Q API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-q-jsonschema-spectral-rules
- name: Amazon Q API Rules
  rule_count: 25
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 15
  slug: amazon-q-spectral-rules
score:
  band: strong
  composite: 63.9
  delta: -3.1
  facets:
    commercial_clarity: 78.9
    contract_quality: 61.0
    developer_ergonomics: 56.5
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 67.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-q/refs/heads/main/screenshots/amazon-q-2026-06-20T171808.png
security:
- kind: authentication
  name: Amazon Q Authentication
  slug: amazon-q-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Q Domain Security
  slug: amazon-q-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Q Vulnerability Disclosure
  slug: amazon-q-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Q Trust Center
  slug: amazon-q-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-q
tags:
- Artificial Intelligence
- Assistant
- Enterprise
- Generative AI
website: https://aws.amazon.com/q/
---

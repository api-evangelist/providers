---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Q Agentic Access
  operation_count: 10
  slug: amazon-q-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
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
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Applications API from Amazon Q — 2 operation(s) for applications.
  name: Amazon Q Applications API
  slug: amazon-q-applications-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Conversations API from Amazon Q — 1 operation(s) for conversations.
  name: Amazon Q Conversations API
  slug: amazon-q-conversations-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Data Sources API from Amazon Q — 1 operation(s) for data sources.
  name: Amazon Q Data Sources API
  slug: amazon-q-data-sources-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Indices API from Amazon Q — 1 operation(s) for indices.
  name: Amazon Q Indices API
  slug: amazon-q-indices-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Aiagents API from Amazon Q — 2 operation(s) for q aiagents.
  name: Amazon Q Q Aiagents API
  slug: amazon-q-aiagents-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Aiguardrails API from Amazon Q — 2 operation(s) for q aiguardrails.
  name: Amazon Q Q Aiguardrails API
  slug: amazon-q-aiguardrails-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Aiprompts API from Amazon Q — 2 operation(s) for q aiprompts.
  name: Amazon Q Q Aiprompts API
  slug: amazon-q-aiprompts-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Assistants API from Amazon Q — 2 operation(s) for q assistants.
  name: Amazon Q Q Assistants API
  slug: amazon-q-assistants-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Associations API from Amazon Q — 4 operation(s) for q associations.
  name: Amazon Q Q Associations API
  slug: amazon-q-associations-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Attachments API from Amazon Q — 4 operation(s) for q attachments.
  name: Amazon Q Q Attachments API
  slug: amazon-q-attachments-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Chatcontrols API from Amazon Q — 1 operation(s) for q chatcontrols.
  name: Amazon Q Q Chatcontrols API
  slug: amazon-q-chatcontrols-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Chatresponseconfigurations API from Amazon Q — 2 operation(s) for q chatresponseconfigurations.
  name: Amazon Q Q Chatresponseconfigurations API
  slug: amazon-q-chatresponseconfigurations-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Contents API from Amazon Q — 2 operation(s) for q contents.
  name: Amazon Q Q Contents API
  slug: amazon-q-contents-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Dataaccessors API from Amazon Q — 2 operation(s) for q dataaccessors.
  name: Amazon Q Q Dataaccessors API
  slug: amazon-q-dataaccessors-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Documents API from Amazon Q — 3 operation(s) for q documents.
  name: Amazon Q Q Documents API
  slug: amazon-q-documents-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Experiences API from Amazon Q — 2 operation(s) for q experiences.
  name: Amazon Q Q Experiences API
  slug: amazon-q-experiences-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Groups API from Amazon Q — 2 operation(s) for q groups.
  name: Amazon Q Q Groups API
  slug: amazon-q-groups-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Importjobs API from Amazon Q — 2 operation(s) for q importjobs.
  name: Amazon Q Q Importjobs API
  slug: amazon-q-importjobs-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Messagetemplates API from Amazon Q — 2 operation(s) for q messagetemplates.
  name: Amazon Q Q Messagetemplates API
  slug: amazon-q-messagetemplates-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Operations API from Amazon Q — 32 operation(s) for q operations.
  name: Amazon Q Q Operations API
  slug: amazon-q-operations-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Plugins API from Amazon Q — 2 operation(s) for q plugins.
  name: Amazon Q Q Plugins API
  slug: amazon-q-plugins-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Policy API from Amazon Q — 2 operation(s) for q policy.
  name: Amazon Q Q Policy API
  slug: amazon-q-policy-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Quickresponses API from Amazon Q — 2 operation(s) for q quickresponses.
  name: Amazon Q Q Quickresponses API
  slug: amazon-q-quickresponses-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Retrievers API from Amazon Q — 2 operation(s) for q retrievers.
  name: Amazon Q Q Retrievers API
  slug: amazon-q-retrievers-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Search API from Amazon Q — 3 operation(s) for q search.
  name: Amazon Q Q Search API
  slug: amazon-q-search-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Sessions API from Amazon Q — 2 operation(s) for q sessions.
  name: Amazon Q Q Sessions API
  slug: amazon-q-sessions-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Subscriptions API from Amazon Q — 2 operation(s) for q subscriptions.
  name: Amazon Q Q Subscriptions API
  slug: amazon-q-subscriptions-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Tags API from Amazon Q — 2 operation(s) for q tags.
  name: Amazon Q Q Tags API
  slug: amazon-q-tags-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Users API from Amazon Q — 2 operation(s) for q users.
  name: Amazon Q Q Users API
  slug: amazon-q-users-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Q Versions API from Amazon Q — 7 operation(s) for q versions.
  name: Amazon Q Q Versions API
  slug: amazon-q-versions-api
- baseURL: https://qbusiness.{region}.amazonaws.com
  baseurl_source: declared
  description: The Knowledge Bases API from Amazon Q — 2 operation(s) for knowledge bases.
  name: Amazon Q Knowledge Bases API
  slug: amazon-q-knowledge-bases-api
artifact_total: 80
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
  name: Amazon Q Business Applications API
  slug: open-amazon-q-applications-api
- collection_type: open
  name: Amazon Q Business Applications Conversations API
  slug: open-amazon-q-conversations-api
- collection_type: open
  name: Amazon Q Business Applications Data Sources API
  slug: open-amazon-q-data-sources-api
- collection_type: open
  name: Amazon Q Business Applications Indices API
  slug: open-amazon-q-indices-api
- collection_type: open
  name: Amazon Q Business API
  slug: open-amazon-q
common:
- group: other
  href: https://artifacts.apis.io/amazon-q/capabilities/amazon-q-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/amazon-q-capability-edges.yml
- group: operate
  href: https://artifacts.apis.io/amazon-q/rate-limits/amazon-q-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-q-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-q/finops/amazon-q-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-q-finops.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-q/plans/amazon-q-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-q-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/q/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/aws/amazon-q-connectjs/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/aws/amazon-q-connectjs/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/aws/amazon-q-connectjs/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/aws/amazon-q-connectjs/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/aws/amazon-q-connectjs/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-q/overview
- group: agent
  href: https://artifacts.apis.io/amazon-q/agentic-access/amazon-q-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-q-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-q/security/amazon-q-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-q-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-q/security/amazon-q-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-q-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-q/security/amazon-q-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-q-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/amazon-q/authentication/amazon-q-authentication.yml
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
  href: https://artifacts.apis.io/amazon-q/json-ld/amazon-q-openapi-application-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-q-openapi-application-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-q/json-ld/amazon-q-openapi-conversation-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-q-openapi-conversation-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-q/json-ld/amazon-q-openapi-data-source-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-q-openapi-data-source-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-q/json-ld/amazon-q-openapi-index-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-q-openapi-index-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-q/json-ld/amazon-q-openapi-message-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-q-openapi-message-context.jsonld
- group: docs
  href: https://artifacts.apis.io/amazon-q/json-schema/amazon-q-openapi-application-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-q-openapi-application-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-q/json-schema/amazon-q-openapi-conversation-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-q-openapi-conversation-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-q/json-schema/amazon-q-openapi-data-source-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-q-openapi-data-source-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-q/json-schema/amazon-q-openapi-index-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-q-openapi-index-schema.json
- group: docs
  href: https://artifacts.apis.io/amazon-q/json-schema/amazon-q-openapi-message-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amazon-q-openapi-message-schema.json
- group: design
  href: https://artifacts.apis.io/amazon-q/json-structure/amazon-q-openapi-application-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-q-openapi-application-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-q/json-structure/amazon-q-openapi-conversation-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-q-openapi-conversation-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-q/json-structure/amazon-q-openapi-data-source-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-q-openapi-data-source-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-q/json-structure/amazon-q-openapi-index-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-q-openapi-index-structure.json
- group: design
  href: https://artifacts.apis.io/amazon-q/json-structure/amazon-q-openapi-message-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amazon-q-openapi-message-structure.json
- group: build
  href: https://artifacts.apis.io/amazon-q/examples/amazon-q-openapi-application-example.json
  title: ''
  type: Examples
  url: examples/amazon-q-openapi-application-example.json
- group: build
  href: https://artifacts.apis.io/amazon-q/examples/amazon-q-openapi-conversation-example.json
  title: ''
  type: Examples
  url: examples/amazon-q-openapi-conversation-example.json
- group: build
  href: https://artifacts.apis.io/amazon-q/examples/amazon-q-openapi-data-source-example.json
  title: ''
  type: Examples
  url: examples/amazon-q-openapi-data-source-example.json
- group: build
  href: https://artifacts.apis.io/amazon-q/examples/amazon-q-openapi-index-example.json
  title: ''
  type: Examples
  url: examples/amazon-q-openapi-index-example.json
- group: build
  href: https://artifacts.apis.io/amazon-q/examples/amazon-q-openapi-message-example.json
  title: ''
  type: Examples
  url: examples/amazon-q-openapi-message-example.json
- group: design
  href: https://artifacts.apis.io/amazon-q/rules/amazon-q-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amazon-q-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-q/vocabulary/amazon-q-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-q-vocabulary.yaml
- group: docs
  href: https://artifacts.apis.io/amazon-q/openapi/_original/amazon-q-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/amazon-q-openapi.yml
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
- has_sources: true
  method: derived
  name: Amazon Q Finops
  primary_unit: user
  service_category: ''
  slug: amazon-q-finops
  template: false
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
modified: '2026-09-16'
name: Amazon Q
nav: Providers
network: true
overview: 'Amazon Q publishes 34 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Conversations API, Data Sources API, and 31 more. Tagged areas include Artificial Intelligence, Assistant, Amazon Web Services, Enterprise, and Generative AI.


  The Amazon Q catalog on APIs.io includes 5 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon Q''s developer surface includes authentication, developer portal, getting-started guide, documentation, engineering blog, FAQ, support, and 47 more developer resources.'
plans:
- name: Amazon Q Plans Pricing
  plan_count: 6
  slug: amazon-q-plans-pricing
- name: Amazon Q Price Estimates
  plan_count: 0
  slug: amazon-q-price-estimates
random_paper: 12
rate_limits:
- limit_count: 5
  name: Amazon Q Rate Limits
  slug: amazon-q-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Amazon Q — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-q-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 66
  extends:
  - spectral:oas
  name: Amazon Q API Rules
  rule_count: 25
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 15
  slug: amazon-q-spectral-rules
score:
  band: exemplar
  composite: 68.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.9
  facets:
    access_clarity: 92.1
    contract_governance: 27.3
    contract_quality: 66.8
    developer_ergonomics: 70.2
    discoverability: 66.1
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  open_source:
    applies: true
    score: 65.0
  previous_composite: 66.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 87.1
      total: 31
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/amazon-q/amazon-q-2026-06-20T171808.png
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
- Amazon Web Services
- Enterprise
- Generative AI
website: https://aws.amazon.com/q/
---

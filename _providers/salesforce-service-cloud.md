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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Salesforce Service Cloud Agentic Access
  operation_count: 18
  slug: salesforce-service-cloud-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 2
apis:
- description: SOAP-based API for enterprise integration and complex service cloud operations.
  name: Salesforce Service Cloud SOAP API
  slug: salesforce-service-cloud-soap-api
- baseURL: https://yourInstance.salesforce.com/cometd/59.0/
  baseurl_source: declared
  description: Real-time streaming API for push notifications and event-driven architecture.
  name: Service Cloud Streaming API
  slug: service-cloud-streaming-api
- description: API for managing knowledge base articles and content.
  name: Knowledge API
  slug: knowledge-api
- description: API for building and managing AI-powered chatbots for customer service.
  name: Einstein Bot API
  slug: einstein-bot-api
- description: API for managing omni-channel routing, agent presence, and work distribution across multiple service channels including chat, messaging, email, and voice.
  name: Omni-Channel API
  slug: omni-channel-api
- description: REST API for integrating telephony systems with Service Cloud Voice, enabling programmatic management of voice calls, call recording, and real-time transcription within the service console.
  name: Service Cloud Voice Telephony Integration API
  slug: service-cloud-voice-telephony-integration-api
- description: Developer API for connecting third-party telephony systems to Service Cloud Voice, including the Connector API for passing information between contact center platforms and Salesforce.
  name: Service Cloud Voice for Partner Telephony API
  slug: service-cloud-voice-for-partner-telephony-api
- description: REST API for building and deploying AI-powered service agents using Agentforce, enabling headless agent interactions, session management, and seamless escalation from AI agents to human service repres
  name: Agentforce Service Agent API
  slug: agentforce-service-agent-api
- baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Operations for managing account records
  name: Salesforce Service Cloud Accounts API
  slug: salesforce-service-cloud-accounts-api
- baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Agent availability and routing
  name: Salesforce Service Cloud Availability API
  slug: salesforce-service-cloud-availability-api
- baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Operations for managing customer service cases
  name: Salesforce Service Cloud Cases API
  slug: salesforce-service-cloud-cases-api
- baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Operations for managing contact records
  name: Salesforce Service Cloud Contacts API
  slug: salesforce-service-cloud-contacts-api
- baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Operations for managing knowledge articles
  name: Salesforce Service Cloud Knowledge API
  slug: salesforce-service-cloud-knowledge-api
- baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Chat message operations
  name: Salesforce Service Cloud Messages API
  slug: salesforce-service-cloud-messages-api
- baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: SOQL query operations
  name: Salesforce Service Cloud Query API
  slug: salesforce-service-cloud-query-api
- baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: SOSL search operations
  name: Salesforce Service Cloud Search API
  slug: salesforce-service-cloud-search-api
- baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Chat session lifecycle management
  name: Salesforce Service Cloud Sessions API
  slug: salesforce-service-cloud-sessions-api
- baseURL: https://yourInstance.salesforce.com/services/data/v59.0/
  baseurl_source: declared
  description: Chat deployment settings
  name: Salesforce Service Cloud Settings API
  slug: salesforce-service-cloud-settings-api
artifact_total: 58
asyncapis:
- description: 'Real-time event streaming API for Salesforce Service Cloud using the Bayeux protocol over CometD. Supports PushTopic events for sObject changes, Platform Events for custom event-driven architectures, '
  name: Salesforce Service Cloud Streaming API
  slug: salesforce-streaming-api-asyncapi
collections:
- collection_type: postman
  name: Salesforce Service Cloud Salesforce Chat REST Accounts API
  slug: postman-salesforce-service-cloud-accounts-api
- collection_type: postman
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Availability API
  slug: postman-salesforce-service-cloud-availability-api
- collection_type: postman
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Cases API
  slug: postman-salesforce-service-cloud-cases-api
- collection_type: postman
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Contacts API
  slug: postman-salesforce-service-cloud-contacts-api
- collection_type: postman
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Knowledge API
  slug: postman-salesforce-service-cloud-knowledge-api
- collection_type: postman
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Messages API
  slug: postman-salesforce-service-cloud-messages-api
- collection_type: postman
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Query API
  slug: postman-salesforce-service-cloud-query-api
- collection_type: postman
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Search API
  slug: postman-salesforce-service-cloud-search-api
- collection_type: postman
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Sessions API
  slug: postman-salesforce-service-cloud-sessions-api
- collection_type: postman
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Settings API
  slug: postman-salesforce-service-cloud-settings-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salesforce Service Cloud Salesforce Chat REST API
  slug: open-salesforce-live-agent
- collection_type: open
  name: Salesforce Service Cloud Salesforce Chat REST Accounts API
  slug: open-salesforce-service-cloud-accounts-api
- collection_type: open
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Availability API
  slug: open-salesforce-service-cloud-availability-api
- collection_type: open
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Cases API
  slug: open-salesforce-service-cloud-cases-api
- collection_type: open
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Contacts API
  slug: open-salesforce-service-cloud-contacts-api
- collection_type: open
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Knowledge API
  slug: open-salesforce-service-cloud-knowledge-api
- collection_type: open
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Messages API
  slug: open-salesforce-service-cloud-messages-api
- collection_type: open
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Query API
  slug: open-salesforce-service-cloud-query-api
- collection_type: open
  name: Salesforce Service Cloud REST API
  slug: open-salesforce-service-cloud-rest
- collection_type: open
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Search API
  slug: open-salesforce-service-cloud-search-api
- collection_type: open
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Sessions API
  slug: open-salesforce-service-cloud-sessions-api
- collection_type: open
  name: Salesforce Service Cloud Salesforce Chat REST Accounts Settings API
  slug: open-salesforce-service-cloud-settings-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/salesforce-service-cloud-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/salesforce-service-cloud/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-service-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesforce-service-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesforce-service-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salesforce-service-cloud-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/salesforce-for-service
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart.htm
- group: auth
  title: ''
  type: Authentication
  url: https://help.salesforce.com/articleView?id=sf.remoteaccess_authenticate.htm
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.salesforce.com/
- group: learn
  title: ''
  type: Trailhead (Learning)
  url: https://trailhead.salesforce.com/
- group: operate
  title: ''
  type: API Status
  url: https://status.salesforce.com/
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/
- group: operate
  title: ''
  type: Community
  url: https://trailblazercommunity.salesforce.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesforce.com/service-cloud/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs
- group: start
  title: ''
  type: Signup
  url: https://developer.salesforce.com/signup
- group: start
  title: ''
  type: Login
  url: https://login.salesforce.com/
- group: start
  title: ''
  type: Console
  url: https://developer.salesforce.com/developer-centers/service-cloud
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/developerforce
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/salesforce
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@SalesforceDevelopers
- group: docs
  title: Case Schema
  type: JSONSchema
  url: json-schema/salesforce-case-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/salesforce-service-cloud-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/salesforce-service-cloud-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/salesforce-service-cloud-vocabulary.yml
created: '2024'
description: Salesforce Service Cloud is a customer service and support platform that helps businesses deliver smarter, faster, and more personalized customer service across all channels.
examples:
- key_count: 7
  name: Salesforce Service Cloud Create Case Example
  slug: salesforce-service-cloud-create-case-example
- key_count: 7
  name: Salesforce Service Cloud Query Cases Example
  slug: salesforce-service-cloud-query-cases-example
finops:
- name: Salesforce Service Cloud Finops
  service_category: Customer Service Platform
  slug: salesforce-service-cloud-finops
graphqls:
- description: This conceptual GraphQL schema represents the Salesforce Service Cloud data model, derived from the Salesforce REST API, Live Agent REST API, and associated developer documentation. It covers the core
  name: Salesforce Service Cloud GraphQL Schema
  slug: salesforce-service-cloud-graphql
image: https://www.salesforce.com/content/dam/web/en_us/www/images/service/service-cloud-logo.png
json_schemas:
- name: Salesforce Service Cloud Case
  property_count: 24
  slug: salesforce-case
json_structures:
- name: Salesforce Service Cloud Case Structure
  property_count: 0
  slug: salesforce-service-cloud-case-structure
jsonld:
- class_count: 0
  name: Salesforce Service Cloud Context
  property_count: 6
  slug: salesforce-service-cloud-context
layout: provider
modified: '2026-05-19'
name: Salesforce Service Cloud
nav: Providers
network: true
overview: 'Salesforce Service Cloud publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Service Cloud Streaming API, Accounts API, Availability API, and 8 more. Tagged areas include Case Management, CRM, Customer Service, Help Desk, and Support.


  The Salesforce Service Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Salesforce Service Cloud''s developer surface includes authentication, getting-started guide, support, pricing, engineering blog, signup flow, developer console, and 22 more developer resources.'
plans:
- name: Salesforce Service Cloud Plans Pricing
  plan_count: 1
  slug: salesforce-service-cloud-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Salesforce Service Cloud Rate Limits
  slug: salesforce-service-cloud-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Salesforce Service Cloud API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: salesforce-service-cloud-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Salesforce Service Cloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: salesforce-service-cloud-jsonschema-spectral-rules
- effective_rule_count: 10
  extends: []
  name: Salesforce Service Cloud API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 4
  slug: salesforce-service-cloud-rules
scopes:
- name: Salesforce Service Cloud Scopes
  scope_count: 2
  slug: salesforce-service-cloud-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 61.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 28.8
    contract_quality: 69.9
    developer_ergonomics: 69.0
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 60.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesforce-service-cloud/refs/heads/main/screenshots/salesforce-service-cloud-2026-06-20T193350.png
security:
- kind: authentication
  name: Salesforce Service Cloud Authentication
  slug: salesforce-service-cloud-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Salesforce Service Cloud Domain Security
  slug: salesforce-service-cloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: salesforce-service-cloud
tags:
- Case Management
- CRM
- Customer Service
- Help Desk
- Support
- Ticketing
website: https://developer.salesforce.com/
---

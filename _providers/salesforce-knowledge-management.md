---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Salesforce Knowledge Management Agentic Access
  operation_count: 11
  slug: salesforce-knowledge-management-agentic-access
  summary_line: 11 operations · 4 acting
api_count: 5
apis:
- description: SOAP API for managing knowledge articles with enterprise integration.
  name: Salesforce Knowledge SOAP API
  slug: salesforce-knowledge-soap-api
- description: Knowledge article management operations
  name: Salesforce Knowledge Management Articles API
  slug: salesforce-knowledge-management-articles-api
- description: Data category management for knowledge articles
  name: Salesforce Knowledge Management Categories API
  slug: salesforce-knowledge-management-categories-api
- description: Knowledge article search operations
  name: Salesforce Knowledge Management Search API
  slug: salesforce-knowledge-management-search-api
- description: Article suggestion operations for cases and communities
  name: Salesforce Knowledge Management Suggestions API
  slug: salesforce-knowledge-management-suggestions-api
artifact_total: 21
collections:
- collection_type: open
  name: Salesforce Knowledge Management REST API
  slug: open-salesforce-knowledge-management-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-knowledge-management-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesforce-knowledge-management-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesforce-knowledge-management-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salesforce-knowledge-management-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs/feed
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/knowledge_development_intro.htm
- group: auth
  title: ''
  type: Authentication
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm
- group: build
  title: ''
  type: SDKs
  url: https://developer.salesforce.com/tools/sdks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
- group: learn
  title: ''
  type: Trailhead Learning
  url: https://trailhead.salesforce.com/en/content/learn/modules/knowledge-basics
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salesforce
- group: design
  title: ''
  type: SpectralRules
  url: rules/salesforce-knowledge-management-rules.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/knowledge-management.yaml
- group: docs
  title: Knowledge Article Schema
  type: JSONSchema
  url: json-schema/salesforce-knowledge-management-article-schema.json
- group: docs
  title: Knowledge Category Schema
  type: JSONSchema
  url: json-schema/salesforce-knowledge-management-category-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/salesforce-knowledge-management-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/salesforce-knowledge-management-vocabulary.yml
created: '2024'
description: API for managing knowledge articles, categories, and data in Salesforce Knowledge. Enables creating, reading, updating, publishing, and archiving knowledge articles for customer self-service and agent-assisted support scenarios across multiple channels including internal app, public knowledge base, and customer portals.
examples:
- key_count: 7
  name: Salesforce Knowledge Management Create Article Example
  slug: salesforce-knowledge-management-create-article-example
- key_count: 7
  name: Salesforce Knowledge Management Search Articles Example
  slug: salesforce-knowledge-management-search-articles-example
finops:
- name: Salesforce Knowledge Management Finops
  service_category: API
  slug: salesforce-knowledge-management-finops
image: https://www.salesforce.com/content/dam/web/en_us/www/images/sf-logo.svg
json_schemas:
- name: Salesforce Knowledge Article
  property_count: 17
  slug: salesforce-knowledge-management-article
- name: Salesforce Knowledge Data Category
  property_count: 4
  slug: salesforce-knowledge-management-category
json_structures:
- name: Salesforce Knowledge Management Article Structure
  property_count: 0
  slug: salesforce-knowledge-management-article-structure
jsonld:
- class_count: 0
  name: Salesforce Knowledge Management Context
  property_count: 18
  slug: salesforce-knowledge-management-context
layout: provider
modified: '2026-05-19'
name: Salesforce Knowledge Management
nav: Providers
network: true
overview: 'Salesforce Knowledge Management publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Categories API, Search API, and 1 more. Tagged areas include Articles, CRM, Customer Service, Documentation, and Knowledge Management.


  The Salesforce Knowledge Management catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Salesforce Knowledge Management''s developer surface includes authentication, engineering blog, getting-started guide, and 17 more developer resources.'
plans:
- name: Salesforce Knowledge Management Plans Pricing
  plan_count: 3
  slug: salesforce-knowledge-management-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Salesforce Knowledge Management Rate Limits
  slug: salesforce-knowledge-management-rate-limits
rules:
- name: Salesforce Knowledge Management API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: salesforce-knowledge-management-jsonschema-spectral-rules
- name: Salesforce Knowledge Management API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: salesforce-knowledge-management-rules
scopes:
- name: Salesforce Knowledge Management Scopes
  scope_count: 2
  slug: salesforce-knowledge-management-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 61.8
  delta: 3.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.5
    developer_ergonomics: 30.4
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 58.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesforce-knowledge-management/refs/heads/main/screenshots/salesforce-knowledge-management-2026-06-20T193346.png
security:
- kind: authentication
  name: Salesforce Knowledge Management Authentication
  slug: salesforce-knowledge-management-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Salesforce Knowledge Management Domain Security
  slug: salesforce-knowledge-management-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: salesforce-knowledge-management
tags:
- Articles
- CRM
- Customer Service
- Documentation
- Knowledge Management
- Support
website: https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/
---

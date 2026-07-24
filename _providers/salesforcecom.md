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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Salesforcecom Agentic Access
  operation_count: 13
  slug: salesforcecom-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 14
apis:
- description: 'The Salesforce Bulk API 2.0 is a specialized REST API for loading large numbers of records asynchronously. It is optimized for processing jobs that contain large data sets, supporting insert, update, '
  name: Salesforce Bulk API 2.0
  slug: bulk-api
- description: The Salesforce Streaming API lets you subscribe to changes in Salesforce data using push technology based on the Bayeux protocol. It enables real-time notifications via PushTopic events, Change Data C
  name: Salesforce Streaming API
  slug: streaming-api
- description: The Salesforce Metadata API enables you to retrieve, deploy, create, update, and delete customization information such as custom object definitions and page layouts for your organization. Used primari
  name: Salesforce Metadata API
  slug: metadata-api
- description: Salesforce Connect REST API provides access to Salesforce Experience Cloud, Files, Chatter, and community features. Enables social features, file management, user feeds, and collaboration across Sales
  name: Salesforce Connect REST API
  slug: connect-api
- description: The Marketing Cloud REST API provides access to Marketing Cloud data and functionality including email, SMS, push messaging, contact management, journeys, and data extensions. Enables programmatic man
  name: Salesforce Marketing Cloud REST API
  slug: marketing-cloud-api
- description: 'The Salesforce B2C Commerce API (SCAPI) provides RESTful access to commerce storefront functionality including products, catalogs, pricing, inventory, orders, customers, and baskets. Enables headless '
  name: Salesforce B2C Commerce API
  slug: commerce-cloud-api
- description: The Salesforce Agentforce API enables developers to build, deploy, and manage AI agents that can autonomously complete tasks across the Salesforce platform. Supports agent creation, customization, and
  name: Salesforce Agentforce API
  slug: agentforce-api
- description: The MuleSoft Anypoint Platform API enables programmatic management of APIs, integrations, and integration assets. Supports API lifecycle management, deployment, analytics, and policy enforcement acros
  name: Salesforce MuleSoft Anypoint Platform API
  slug: mulesoft-api
- description: Composite API for batching multiple operations
  name: Salesforce Composite API
  slug: salesforcecom-composite-api
- description: sObject metadata and describe operations
  name: Salesforce Metadata API
  slug: salesforcecom-metadata-api
- description: SOQL query execution
  name: Salesforce Query API
  slug: salesforcecom-query-api
- description: CRUD operations on Salesforce sObject records
  name: Salesforce Records API
  slug: salesforcecom-records-api
- description: SOSL search execution
  name: Salesforce Search API
  slug: salesforcecom-search-api
- description: API version information
  name: Salesforce Versions API
  slug: salesforcecom-versions-api
artifact_total: 33
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforcecom-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/salesforcecom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesforcecom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesforcecom-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.salesforce.com
- group: start
  title: ''
  type: Portal
  url: https://developer.salesforce.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs
- group: build
  title: ''
  type: APILibrary
  url: https://developer.salesforce.com/docs/apis
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs
- group: operate
  title: ''
  type: Community
  url: https://trailblazer.salesforce.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesforce.com/editions-pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com
- group: start
  title: ''
  type: Signup
  url: https://www.salesforce.com/form/signup/freetrial-salesforce/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/salesforce
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/salesforce
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forcedotcom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salesforcecli
- group: build
  title: ''
  type: CLI
  url: https://github.com/salesforcecli/cli
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/salesforce-developers/salesforce-developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/api_rest_whats_new.htm
- group: other
  title: ''
  type: Trailhead
  url: https://trailhead.salesforce.com
created: '2026-03-24'
description: Salesforce is a global leader in customer relationship management (CRM) software and cloud-based applications. The Salesforce Platform provides a comprehensive suite of APIs for sales, service, marketing, commerce, integration, analytics, and platform development including Agentforce AI capabilities.
examples:
- key_count: 2
  name: Salesforcecom Create Contact Example
  slug: salesforcecom-create-contact-example
- key_count: 2
  name: Salesforcecom Query Accounts Example
  slug: salesforcecom-query-accounts-example
finops:
- name: Salesforcecom Finops
  service_category: CRM Platform
  slug: salesforcecom-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salesforcecom.png
json_schemas:
- name: ErrorResponse
  property_count: 0
  slug: salesforcecom-errorresponse
- name: Salesforce SOQL Query Result
  property_count: 4
  slug: salesforcecom-query-result
- name: QueryResult
  property_count: 4
  slug: salesforcecom-queryresult
- name: Salesforce sObject
  property_count: 10
  slug: salesforcecom-sobject
- name: SObjectDescribe
  property_count: 10
  slug: salesforcecom-sobjectdescribe
json_structures:
- name: Salesforcecom Sobject Structure
  property_count: 0
  slug: salesforcecom-sobject-structure
- name: Salesforcecom Structure
  property_count: 0
  slug: salesforcecom-structure
jsonld:
- class_count: 0
  name: Salesforcecom Context
  property_count: 6
  slug: salesforcecom-context
layout: provider
modified: '2026-05-19'
name: Salesforce
nav: Providers
network: true
overview: 'Salesforce publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Composite API, Metadata API, Query API, and 3 more. Tagged areas include CRM, Cloud, Sales, Marketing, and Automation.


  The Salesforce catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Salesforce''s developer surface includes authentication, developer portal, documentation, engineering blog, pricing, support, signup flow, and 15 more developer resources.'
plans:
- name: Salesforcecom Plans Pricing
  plan_count: 1
  slug: salesforcecom-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Salesforcecom Rate Limits
  slug: salesforcecom-rate-limits
rules:
- name: Salesforce API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: salesforcecom-jsonschema-spectral-rules
- name: Salesforce API Rules
  rule_count: 14
  severity_counts:
    error: 3
    hint: 0
    info: 5
    warn: 6
  slug: salesforcecom-rules
score:
  band: developing
  composite: 57.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.5
    developer_ergonomics: 45.7
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 57.9
  previous_composite: 57.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesforcecom/refs/heads/main/screenshots/salesforcecom-2026-06-20T193352.png
security:
- kind: authentication
  name: Salesforcecom Authentication
  slug: salesforcecom-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Salesforcecom Domain Security
  slug: salesforcecom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Salesforcecom Vulnerability Disclosure
  slug: salesforcecom-vulnerability-disclosure
  summary_line: disclosure policy published
slug: salesforcecom
tags:
- CRM
- Cloud
- Sales
- Marketing
- Automation
- AI
- Fortune 500
website: https://www.salesforce.com
---

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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Amazon Resource Explorer Agentic Access
  operation_count: 14
  slug: amazon-resource-explorer-agentic-access
  summary_line: 14 operations · 13 acting
api_count: 1
apis:
- baseURL: https://resource-explorer-2.amazonaws.com
  baseurl_source: declared
  description: The Index API from Amazon Resource Explorer — 4 operation(s) for index.
  name: Amazon Resource Explorer Index API
  slug: amazon-resource-explorer-index-api
- baseURL: https://resource-explorer-2.amazonaws.com
  baseurl_source: declared
  description: The Resources API from Amazon Resource Explorer — 1 operation(s) for resources.
  name: Amazon Resource Explorer Resources API
  slug: amazon-resource-explorer-resources-api
- baseURL: https://resource-explorer-2.amazonaws.com
  baseurl_source: declared
  description: The Search API from Amazon Resource Explorer — 1 operation(s) for search.
  name: Amazon Resource Explorer Search API
  slug: amazon-resource-explorer-search-api
- baseURL: https://resource-explorer-2.amazonaws.com
  baseurl_source: declared
  description: The Tags API from Amazon Resource Explorer — 3 operation(s) for tags.
  name: Amazon Resource Explorer Tags API
  slug: amazon-resource-explorer-tags-api
- baseURL: https://resource-explorer-2.amazonaws.com
  baseurl_source: declared
  description: The Views API from Amazon Resource Explorer — 5 operation(s) for views.
  name: Amazon Resource Explorer Views API
  slug: amazon-resource-explorer-views-api
artifact_total: 47
collections:
- collection_type: postman
  name: Amazon Resource Explorer Index API
  slug: postman-amazon-resource-explorer-index-api
- collection_type: postman
  name: Amazon Resource Explorer Index Resources API
  slug: postman-amazon-resource-explorer-resources-api
- collection_type: postman
  name: Amazon Resource Explorer Index Search API
  slug: postman-amazon-resource-explorer-search-api
- collection_type: postman
  name: Amazon Resource Explorer Index Tags API
  slug: postman-amazon-resource-explorer-tags-api
- collection_type: postman
  name: Amazon Resource Explorer Index Views API
  slug: postman-amazon-resource-explorer-views-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Resource Explorer Index API
  slug: open-amazon-resource-explorer-index-api
- collection_type: open
  name: Amazon Resource Explorer Index Resources API
  slug: open-amazon-resource-explorer-resources-api
- collection_type: open
  name: Amazon Resource Explorer Index Search API
  slug: open-amazon-resource-explorer-search-api
- collection_type: open
  name: Amazon Resource Explorer Index Tags API
  slug: open-amazon-resource-explorer-tags-api
- collection_type: open
  name: Amazon Resource Explorer Index Views API
  slug: open-amazon-resource-explorer-views-api
- collection_type: open
  name: Amazon Resource Explorer API
  slug: open-amazon-resource-explorer
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-resource-explorer/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-resource-explorer-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-resource-explorer-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-resource-explorer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-resource-explorer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-resource-explorer-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/resourceexplorer/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/resourceexplorer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/resource-explorer/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/mt/tag/aws-resource-explorer/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Portal
  url: https://console.aws.amazon.com/resource-explorer/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-resource-explorer-openapi-index-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-resource-explorer-openapi-resource-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-resource-explorer-openapi-search-request-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-resource-explorer-openapi-search-response-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-resource-explorer-openapi-view-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-resource-explorer-openapi-index-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-resource-explorer-openapi-resource-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-resource-explorer-openapi-search-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-resource-explorer-openapi-search-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-resource-explorer-openapi-view-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-resource-explorer-openapi-index-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-resource-explorer-openapi-resource-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-resource-explorer-openapi-search-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-resource-explorer-openapi-search-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-resource-explorer-openapi-view-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-resource-explorer-openapi-index-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-resource-explorer-openapi-resource-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-resource-explorer-openapi-search-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-resource-explorer-openapi-search-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-resource-explorer-openapi-view-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-resource-explorer-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-resource-explorer-vocabulary.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/amazon-resource-explorer-openapi.yml
created: '2026-03-16'
description: AWS Resource Explorer is a resource search and discovery service. With Resource Explorer, you can explore your resources across AWS Regions using an internet search-like experience. It provides a unified view of your AWS resources and helps you understand your resource inventory.
examples:
- key_count: 3
  name: Amazon Resource Explorer Openapi Index Example
  slug: amazon-resource-explorer-openapi-index-example
- key_count: 6
  name: Amazon Resource Explorer Openapi Resource Example
  slug: amazon-resource-explorer-openapi-resource-example
- key_count: 4
  name: Amazon Resource Explorer Openapi Search Request Example
  slug: amazon-resource-explorer-openapi-search-request-example
- key_count: 4
  name: Amazon Resource Explorer Openapi Search Response Example
  slug: amazon-resource-explorer-openapi-search-response-example
- key_count: 3
  name: Amazon Resource Explorer Openapi View Example
  slug: amazon-resource-explorer-openapi-view-example
finops:
- name: Amazon Resource Explorer Finops
  service_category: API
  slug: amazon-resource-explorer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-resource-explorer.png
json_schemas:
- name: Index
  property_count: 3
  slug: amazon-resource-explorer-openapi-index
- name: Resource
  property_count: 6
  slug: amazon-resource-explorer-openapi-resource
- name: SearchRequest
  property_count: 4
  slug: amazon-resource-explorer-openapi-search-request
- name: SearchResponse
  property_count: 4
  slug: amazon-resource-explorer-openapi-search-response
- name: View
  property_count: 3
  slug: amazon-resource-explorer-openapi-view
json_structures:
- name: Amazon Resource Explorer Openapi Index Structure
  property_count: 3
  slug: amazon-resource-explorer-openapi-index-structure
- name: Amazon Resource Explorer Openapi Resource Structure
  property_count: 6
  slug: amazon-resource-explorer-openapi-resource-structure
- name: Amazon Resource Explorer Openapi Search Request Structure
  property_count: 4
  slug: amazon-resource-explorer-openapi-search-request-structure
- name: Amazon Resource Explorer Openapi Search Response Structure
  property_count: 4
  slug: amazon-resource-explorer-openapi-search-response-structure
- name: Amazon Resource Explorer Openapi View Structure
  property_count: 3
  slug: amazon-resource-explorer-openapi-view-structure
jsonld:
- class_count: 1
  name: Amazon Resource Explorer Openapi Index Context
  property_count: 3
  slug: amazon-resource-explorer-openapi-index-context
- class_count: 1
  name: Amazon Resource Explorer Openapi Resource Context
  property_count: 6
  slug: amazon-resource-explorer-openapi-resource-context
- class_count: 1
  name: Amazon Resource Explorer Openapi Search Request Context
  property_count: 4
  slug: amazon-resource-explorer-openapi-search-request-context
- class_count: 1
  name: Amazon Resource Explorer Openapi Search Response Context
  property_count: 4
  slug: amazon-resource-explorer-openapi-search-response-context
- class_count: 1
  name: Amazon Resource Explorer Openapi View Context
  property_count: 3
  slug: amazon-resource-explorer-openapi-view-context
layout: provider
modified: '2026-05-19'
name: Amazon Resource Explorer
nav: Providers
network: true
overview: 'Amazon Resource Explorer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Index API, Resources API, Search API, and 2 more. Tagged areas include Discovery, Inventory, and Resource Management.


  The Amazon Resource Explorer catalog on APIs.io includes 5 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon Resource Explorer''s developer surface includes authentication, developer portal, documentation, support, engineering blog, signup flow, code examples, and 35 more developer resources.'
plans:
- name: Amazon Resource Explorer Plans Pricing
  plan_count: 3
  slug: amazon-resource-explorer-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Amazon Resource Explorer Rate Limits
  slug: amazon-resource-explorer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Resource Explorer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-resource-explorer-jsonschema-spectral-rules
- effective_rule_count: 66
  extends:
  - spectral:oas
  name: Amazon Resource Explorer API Rules
  rule_count: 25
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 16
  slug: amazon-resource-explorer-spectral-rules
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 59.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 59.9
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-resource-explorer/refs/heads/main/screenshots/amazon-resource-explorer-2026-06-20T171809.png
security:
- kind: authentication
  name: Amazon Resource Explorer Authentication
  slug: amazon-resource-explorer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Resource Explorer Domain Security
  slug: amazon-resource-explorer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Resource Explorer Vulnerability Disclosure
  slug: amazon-resource-explorer-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Resource Explorer Trust Center
  slug: amazon-resource-explorer-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-resource-explorer
tags:
- Discovery
- Inventory
- Resource Management
website: https://aws.amazon.com/resourceexplorer/
---

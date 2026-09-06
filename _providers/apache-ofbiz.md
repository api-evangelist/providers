---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Apache Ofbiz Agentic Access
  operation_count: 5
  slug: apache-ofbiz-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://localhost:8443/rest
  baseurl_source: declared
  description: Obtain and refresh JWT tokens for API access
  name: Apache OFBiz Authentication API
  slug: apache-ofbiz-authentication-api
- baseURL: https://localhost:8443/rest
  baseurl_source: declared
  description: List and invoke exported OFBiz services
  name: Apache OFBiz Services API
  slug: apache-ofbiz-services-api
artifact_total: 58
collections:
- collection_type: postman
  name: Apache OFBiz REST Authentication API
  slug: postman-apache-ofbiz-authentication-api
- collection_type: postman
  name: Apache OFBiz REST Authentication Services API
  slug: postman-apache-ofbiz-services-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache OFBiz REST Authentication API
  slug: open-apache-ofbiz-authentication-api
- collection_type: open
  name: Apache OFBiz REST Authentication Services API
  slug: open-apache-ofbiz-services-api
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/ofbiz-framework/blob/trunk/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/ofbiz-framework/blob/trunk/CONTRIBUTING.adoc
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/ofbiz-framework/blob/trunk/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apache-ofbiz/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-ofbiz-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-ofbiz-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-ofbiz
- group: build
  title: Apache OFBiz Framework GitHub Repository
  type: GitHubRepository
  url: https://github.com/apache/ofbiz-framework
- group: build
  title: Apache Software Foundation GitHub
  type: GitHubOrganization
  url: https://github.com/apache
- group: docs
  title: Apache OFBiz Documentation
  type: Documentation
  url: https://ofbiz.apache.org/documentation.html
- group: start
  title: OFBiz Developer Manual
  type: GettingStarted
  url: https://nightlies.apache.org/ofbiz/stable/ofbiz/html5/developer-manual.html
- group: learn
  title: OFBiz Wiki
  type: Tutorials
  url: https://cwiki.apache.org/confluence/display/OFBIZ/Home
- group: operate
  title: Apache OFBiz FAQs
  type: FAQ
  url: https://ofbiz.apache.org/faqs.html
- group: operate
  title: OFBiz Release Notes
  type: ReleaseNotes
  url: https://github.com/apache/ofbiz-framework/blob/trunk/CHANGELOG.md
- group: commercial
  title: Apache License 2.0
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: operate
  title: Mailing Lists
  type: Support
  url: https://ofbiz.apache.org/mailing-lists.html
- group: operate
  title: OFBiz on Stack Overflow
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/ofbiz
- group: design
  title: Apache OFBiz Spectral Rules
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/rules/apache-ofbiz-spectral-rules.yml
- group: design
  title: Apache OFBiz Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/vocabulary/apache-ofbiz-vocabulary.yaml
- group: design
  title: Apache OFBiz JSON-LD Context
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/json-ld/apache-ofbiz-context.jsonld
created: '2026-03-16'
description: Apache OFBiz is an open-source enterprise resource planning (ERP) system providing a suite of integrated business applications for CRM, e-commerce, supply chain management, manufacturing, accounting, order management, inventory, and warehousing. Built on a service-oriented architecture with a service engine, entity engine, and widget framework, OFBiz exposes a REST API plugin allowing any exported service to be invoked via JWT- authenticated HTTP endpoints. Governed by the Apache Software Foundation under the Apache License 2.0. Written in Java with Groovy scripting support.
examples:
- key_count: 1
  name: Apache Ofbiz Refresh Request Example
  slug: apache-ofbiz-refresh-request-example
- key_count: 3
  name: Apache Ofbiz Service Entry Example
  slug: apache-ofbiz-service-entry-example
- key_count: 3
  name: Apache Ofbiz Service Link Example
  slug: apache-ofbiz-service-link-example
- key_count: 4
  name: Apache Ofbiz Service List Response Example
  slug: apache-ofbiz-service-list-response-example
- key_count: 4
  name: Apache Ofbiz Service Response Example
  slug: apache-ofbiz-service-response-example
- key_count: 4
  name: Apache Ofbiz Token Data Example
  slug: apache-ofbiz-token-data-example
- key_count: 4
  name: Apache Ofbiz Token Response Example
  slug: apache-ofbiz-token-response-example
features:
- description: All business logic encapsulated in services accessible via multiple protocols including REST, XML-RPC, and Java.
  name: Service-Oriented Architecture
- description: Plugin enabling any exported OFBiz service to be invoked via RESTful HTTP endpoints with JWT authentication.
  name: REST API Plugin
- description: OAuth2-compatible JWT-based authentication with access tokens and refresh tokens for secure API access.
  name: JWT Authentication
- description: Flexible data access layer supporting multiple databases with entity-based query API and relationship management.
  name: Entity Engine
- description: Central business logic executor with transaction management, error handling, and event-driven service chaining.
  name: Service Engine
- description: Built-in Swagger/OpenAPI UI at /docs/swagger-ui.html for API exploration and testing when REST plugin is deployed.
  name: Swagger UI Integration
- description: Groovy scripting support for service implementations and customizations without Java compilation.
  name: Groovy Scripting
- description: Modular plugin system allowing feature extension without modifying core framework code.
  name: Plugin Architecture
- description: Integrated modules for accounting, order management, inventory, manufacturing, CRM, e-commerce, and HR.
  name: Multi-Module ERP
- description: XML-based UI component framework for building consistent web interfaces across ERP modules.
  name: Widget Framework
finops:
- name: Apache Ofbiz Finops
  service_category: API
  slug: apache-ofbiz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-ofbiz.png
integrations:
- description: Integration for product and content search indexing across OFBiz data.
  name: Apache Solr
- description: Groovy scripting engine integration for service implementations and data transformations.
  name: Groovy
- description: Supported relational database backend via the OFBiz entity engine.
  name: PostgreSQL
- description: Supported relational database backend for OFBiz data persistence.
  name: MySQL
- description: Official Docker support for containerized OFBiz deployments.
  name: Docker
- description: OpenAPI documentation and testing interface bundled with the REST API plugin.
  name: Swagger UI
json_schemas:
- name: RefreshRequest
  property_count: 1
  slug: apache-ofbiz-refresh-request
- name: ServiceEntry
  property_count: 3
  slug: apache-ofbiz-service-entry
- name: ServiceLink
  property_count: 3
  slug: apache-ofbiz-service-link
- name: ServiceListResponse
  property_count: 4
  slug: apache-ofbiz-service-list-response
- name: ServiceResponse
  property_count: 4
  slug: apache-ofbiz-service-response
- name: TokenData
  property_count: 4
  slug: apache-ofbiz-token-data
- name: TokenResponse
  property_count: 4
  slug: apache-ofbiz-token-response
json_structures:
- name: Apache Ofbiz Refresh Request Structure
  property_count: 1
  slug: apache-ofbiz-refresh-request-structure
- name: Apache Ofbiz Service Entry Structure
  property_count: 3
  slug: apache-ofbiz-service-entry-structure
- name: Apache Ofbiz Service Link Structure
  property_count: 3
  slug: apache-ofbiz-service-link-structure
- name: Apache Ofbiz Service List Response Structure
  property_count: 4
  slug: apache-ofbiz-service-list-response-structure
- name: Apache Ofbiz Service Response Structure
  property_count: 4
  slug: apache-ofbiz-service-response-structure
- name: Apache Ofbiz Token Data Structure
  property_count: 4
  slug: apache-ofbiz-token-data-structure
- name: Apache Ofbiz Token Response Structure
  property_count: 4
  slug: apache-ofbiz-token-response-structure
jsonld:
- class_count: 9
  name: Apache Ofbiz Context
  property_count: 12
  slug: apache-ofbiz-context
layout: provider
modified: '2026-05-19'
name: Apache OFBiz
nav: Providers
network: true
overview: 'Apache OFBiz publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Services API. Tagged areas include ERP, CRM, E-Commerce, Business Applications, and Apache.


  The Apache OFBiz catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache OFBiz''s developer surface includes authentication, documentation, getting-started guide, FAQ, release notes, support, Stack Overflow tag, and 14 more developer resources.'
plans:
- name: Apache Ofbiz Plans Pricing
  plan_count: 3
  slug: apache-ofbiz-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Apache Ofbiz Rate Limits
  slug: apache-ofbiz-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache OFBiz API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-ofbiz-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Apache OFBiz API Rules
  rule_count: 36
  severity_counts:
    error: 12
    hint: 0
    info: 5
    warn: 19
  slug: apache-ofbiz-spectral-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 66.5
    catalog_earned_first_party: 0.0
    catalog_gap: 48.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 68.4
    developer_ergonomics: 39.3
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 75.0
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-ofbiz/refs/heads/main/screenshots/apache-ofbiz-2026-06-20T172127.png
security:
- kind: authentication
  name: Apache Ofbiz Authentication
  slug: apache-ofbiz-authentication
  summary_line: http · 2 schemes
slug: apache-ofbiz
tags:
- ERP
- CRM
- E-Commerce
- Business Applications
- Apache
- Java
- Open-Source
- Supply Chain
use_cases:
- description: Integrate external systems (CRM, WMS, payment processors) with OFBiz via REST API service calls.
  name: ERP System Integration
- description: Use OFBiz as a headless e-commerce backend with product catalog, pricing, order management, and fulfillment services.
  name: E-Commerce Backend
- description: Automate supply chain workflows including purchase orders, inventory updates, and supplier communications via REST services.
  name: Supply Chain Automation
- description: Automate accounting entries, invoicing, AR/AP processing, and financial reporting via OFBiz service API.
  name: Accounting Automation
- description: Manage manufacturing resource planning, work orders, bill of materials, and production scheduling via OFBiz services.
  name: Manufacturing Operations
- description: Build custom business process automations by chaining OFBiz services via the REST API.
  name: Custom Business Workflows
---

---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 28.8
  scored_at: '2026-07-23'
api_count: 6
apis:
- description: The Solution Manager REST API provides programmatic access to administer the Denodo Platform across environments and clusters. It exposes endpoints for cluster lifecycle management, environment config
  name: Denodo Solution Manager REST API
  slug: solution-manager-api
- description: The Denodo Data Catalog REST API provides programmatic access to the catalog of virtual views, web services, search, lineage, tags, categories, and certifications managed by the Denodo Platform. It po
  name: Denodo Data Catalog REST API
  slug: data-catalog-api
- description: 'The Denodo RESTful Web Service exposes any view in Virtual DataPort as a resource-oriented REST endpoint. It supports JSON, XML, and HTML representations, query filtering, projection, pagination, and '
  name: Denodo RESTful Web Service
  slug: rest-web-service
- description: The Denodo OData 4.0 service provides an OASIS OData v4 compliant interface for querying Virtual DataPort views over HTTP. It supports filter, select, expand, orderby, top, and skip query options as w
  name: Denodo OData 4.0 Service
  slug: odata-service
- description: The Denodo GraphQL Service enables clients to execute GraphQL queries against virtual views in the Denodo Platform. It generates a GraphQL schema from selected views and supports filtering, pagination
  name: Denodo GraphQL Service
  slug: graphql-service
- description: The Denodo Scheduler REST API allows programmatic management and monitoring of scheduled jobs and projects in the Denodo Scheduler component. Endpoints support listing, creating, executing, cancelling
  name: Denodo Scheduler REST API
  slug: scheduler-rest-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/denodo-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/denodo-technologies
- group: company
  title: ''
  type: Website
  url: https://www.denodo.com
- group: start
  title: ''
  type: Portal
  url: https://community.denodo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://community.denodo.com/docs/
- group: other
  title: ''
  type: Knowledge Base
  url: https://community.denodo.com/kb/
- group: learn
  title: ''
  type: Tutorials
  url: https://community.denodo.com/tutorials/
- group: company
  title: ''
  type: Express Edition
  url: https://www.denodo.com/en/denodo-platform/free-trials
- group: commercial
  title: ''
  type: Pricing
  url: https://www.denodo.com/en/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.denodo.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.denodo.com/en/legal/denodo-trust-center
- group: company
  title: ''
  type: Blog
  url: https://www.denodo.com/en/blog
- group: other
  title: ''
  type: Customers
  url: https://www.denodo.com/en/customers
- group: company
  title: ''
  type: Partners
  url: https://www.denodo.com/en/partners
- group: learn
  title: ''
  type: Training
  url: https://www.denodo.com/en/services/training
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/denodo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.denodo.com/en/legal/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.denodo.com/en/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.denodo.com/en/legal/denodo-trust-center
- group: design
  title: ''
  type: JSONLD
  url: json-ld/denodo-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/denodo-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/denodo-capabilities.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/denodo/denodo-skills
created: '2026-03-16'
description: Denodo is a leading data virtualization platform that enables real-time access, integration, and delivery of data from disparate sources across enterprise data landscapes. The Denodo Platform exposes a portfolio of REST, OData, GraphQL, and SOAP web service endpoints through Virtual DataPort, the Data Catalog, the Solution Manager, and the Scheduler so that data products can be published, governed, and administered programmatically.
finops:
- name: Denodo Finops
  service_category: API
  slug: denodo-finops
graphqls:
- description: The Denodo GraphQL Service enables clients to execute GraphQL queries against virtual views in the Denodo Platform. It generates a GraphQL schema from selected views and supports filtering, pagination
  name: Denodo GraphQL API
  slug: denodo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/denodo.png
jsonld:
- class_count: 0
  name: Denodo Context
  property_count: 6
  slug: denodo-context
layout: provider
modified: '2026-05-19'
name: Denodo
nav: Providers
network: true
overview: 'Denodo publishes 1 API on the [APIs.io](https://apis.io/) network: Data Catalog REST API. Tagged areas include Data Catalog, Data Fabric, Data Mesh, Data Virtualization, and GraphQL.


  The Denodo catalog on APIs.io includes 1 JSON-LD context.


  Denodo''s developer surface includes developer portal, documentation, pricing, support, engineering blog, training material, and 17 more developer resources.'
plans:
- name: Denodo Plans Pricing
  plan_count: 3
  slug: denodo-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Denodo Rate Limits
  slug: denodo-rate-limits
score:
  band: developing
  composite: 50.6
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 47.2
    developer_ergonomics: 23.9
    discoverability: 100.0
    governance: 13.2
    operational_transparency: 63.2
  previous_composite: 50.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/denodo/refs/heads/main/screenshots/denodo-2026-06-20T175914.png
security:
- kind: domain-security
  name: Denodo Domain Security
  slug: denodo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: denodo-vql-generation
  slug: denodo-vql-generation
slug: denodo
tags:
- Data Catalog
- Data Fabric
- Data Mesh
- Data Virtualization
- GraphQL
- Logical Data Warehouse
- OData
- REST
- Scheduler
- Solution Manager
website: https://www.denodo.com
---

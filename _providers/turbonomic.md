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
- acting_count: 12
  human_in_the_loop: 0
  name: Turbonomic Agentic Access
  operation_count: 28
  slug: turbonomic-agentic-access
  summary_line: 28 operations · 12 acting
api_count: 10
apis:
- description: Retrieve, accept, and reject optimization actions
  name: IBM Turbonomic Actions API
  slug: turbonomic-actions-api
- description: Authenticate and manage sessions
  name: IBM Turbonomic Authentication API
  slug: turbonomic-authentication-api
- description: Query and manage entities (VMs, containers, applications, storage)
  name: IBM Turbonomic Entities API
  slug: turbonomic-entities-api
- description: Create and manage logical groups of entities
  name: IBM Turbonomic Groups API
  slug: turbonomic-groups-api
- description: Access Turbonomic markets and projected states
  name: IBM Turbonomic Markets API
  slug: turbonomic-markets-api
- description: Manage automation and placement policies
  name: IBM Turbonomic Policies API
  slug: turbonomic-policies-api
- description: Retrieve historical and projected resource statistics
  name: IBM Turbonomic Statistics API
  slug: turbonomic-statistics-api
- description: Manage discovery targets and integrations
  name: IBM Turbonomic Targets API
  slug: turbonomic-targets-api
- description: Manage resource and hardware templates
  name: IBM Turbonomic Templates API
  slug: turbonomic-templates-api
- description: Explore infrastructure topology and supply chains
  name: IBM Turbonomic Topology API
  slug: turbonomic-topology-api
artifact_total: 30
collections:
- collection_type: open
  name: Turbonomic REST API
  slug: open-turbonomic-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/turbonomic-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/turbonomic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turbonomic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/turbonomic-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/turbonomic
- group: company
  title: ''
  type: Website
  url: https://www.ibm.com/products/turbonomic
- group: docs
  title: ''
  type: Documentation
  url: https://www.ibm.com/docs/en/tarm/8.19.3
- group: docs
  title: ''
  type: SwaggerUI
  url: https://try.turbonomic.io/apidoc/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ibm.com/docs/en/tarm/8.13.0?topic=reference-getting-started-turbonomic-rest-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/turbonomic
- group: company
  title: ''
  type: Blog
  url: https://www.ibm.com/blog/turbonomic/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ibm.com/products/turbonomic/pricing
- group: other
  title: ''
  type: Marketplace
  url: https://aws.amazon.com/marketplace/pp/prodview-5r3k3snu4ttnm
- group: operate
  title: ''
  type: Support
  url: https://www.ibm.com/mysupport/s/topic/0TO0z000000ZnCCGA0/turbonomic-application-resource-management
- group: operate
  title: ''
  type: Community
  url: https://developer.ibm.com/components/turbonomic/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ibm.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ibm.com/privacy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/turbonomic-rest-api-openapi.yml
- group: other
  title: ''
  type: KubernetesCRD
  url: crd/charts.helm.k8s.io_xls.yaml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/turbonomic-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/turbonomic-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/turbonomic-entity-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/turbonomic-action-schema.json
crds:
- name: charts.helm.k8s.io xls
  url: https://raw.githubusercontent.com/api-evangelist/turbonomic/refs/heads/main/crd/charts.helm.k8s.io_xls.yaml
created: '2026-03-16'
description: IBM Turbonomic is an Application Resource Management (ARM) platform that uses AI-powered automation to continuously analyze and optimize application performance and cloud costs across hybrid and multi-cloud environments. Turbonomic provides a comprehensive REST API enabling programmatic access to resource management data, workload actions, markets, policies, groups, templates, and topology information. The platform integrates with AWS, Azure, GCP, Kubernetes, VMware, and dozens of APM and ITSM tools.
examples:
- key_count: 2
  name: Turbonomic Creategroup Example
  slug: turbonomic-createGroup-example
- key_count: 2
  name: Turbonomic Getentities Example
  slug: turbonomic-getEntities-example
- key_count: 2
  name: Turbonomic Getentitystats Example
  slug: turbonomic-getEntityStats-example
- key_count: 2
  name: Turbonomic Getmarketactions Example
  slug: turbonomic-getMarketActions-example
- key_count: 2
  name: Turbonomic Loginuser Example
  slug: turbonomic-loginUser-example
finops:
- name: Turbonomic Finops
  service_category: API
  slug: turbonomic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turbonomic.png
json_schemas:
- name: Turbonomic Action
  property_count: 14
  slug: turbonomic-action
- name: Turbonomic Entity
  property_count: 10
  slug: turbonomic-entity
json_structures:
- name: Turbonomic Action Structure
  property_count: 0
  slug: turbonomic-action-structure
- name: Turbonomic Entity Structure
  property_count: 0
  slug: turbonomic-entity-structure
jsonld:
- class_count: 0
  name: Turbonomic Context
  property_count: 7
  slug: turbonomic-context
layout: provider
modified: '2026-05-19'
name: IBM Turbonomic
nav: Providers
network: true
overview: 'IBM Turbonomic publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Authentication API, Entities API, and 7 more. Tagged areas include Application Resource Management, Cloud Cost Optimization, Cloud Management, Hybrid Cloud, and IBM.


  The IBM Turbonomic catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  IBM Turbonomic''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, support, and 17 more developer resources.'
plans:
- name: Turbonomic Plans Pricing
  plan_count: 3
  slug: turbonomic-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Turbonomic Rate Limits
  slug: turbonomic-rate-limits
rules:
- name: IBM Turbonomic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: turbonomic-jsonschema-spectral-rules
- name: IBM Turbonomic API Rules
  rule_count: 12
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 7
  slug: turbonomic-rest-api-rules
score:
  band: strong
  composite: 62.3
  delta: 3.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 61.8
    developer_ergonomics: 37.0
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 59.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/turbonomic/refs/heads/main/screenshots/turbonomic-2026-06-20T195852.png
security:
- kind: authentication
  name: Turbonomic Authentication
  slug: turbonomic-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Turbonomic Domain Security
  slug: turbonomic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Turbonomic Vulnerability Disclosure
  slug: turbonomic-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: turbonomic
tags:
- Application Resource Management
- Cloud Cost Optimization
- Cloud Management
- Hybrid Cloud
- IBM
- Kubernetes
- Multi-Cloud
- Workload Optimization
website: https://www.ibm.com/products/turbonomic
---

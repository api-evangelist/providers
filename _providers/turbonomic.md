---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Turbonomic Agentic Access
  operation_count: 32
  slug: turbonomic-agentic-access
  summary_line: 32 operations · 10 acting
api_count: 1
apis:
- baseURL: https://{turbonomic_host}/api/v3
  baseurl_source: declared
  description: Retrieve, accept, and reject optimization actions
  name: IBM Turbonomic Actions API
  slug: turbonomic-actions-api
- baseURL: https://{turbonomic_host}/api/v3
  baseurl_source: declared
  description: Authenticate and manage sessions
  name: IBM Turbonomic Authentication API
  slug: turbonomic-authentication-api
- baseURL: https://{turbonomic_host}/api/v3
  baseurl_source: declared
  description: Query and manage entities (VMs, containers, applications, storage)
  name: IBM Turbonomic Entities API
  slug: turbonomic-entities-api
- baseURL: https://{turbonomic_host}/api/v3
  baseurl_source: declared
  description: Create and manage logical groups of entities
  name: IBM Turbonomic Groups API
  slug: turbonomic-groups-api
- baseURL: https://{turbonomic_host}/api/v3
  baseurl_source: declared
  description: Access Turbonomic markets and projected states
  name: IBM Turbonomic Markets API
  slug: turbonomic-markets-api
- baseURL: https://{turbonomic_host}/api/v3
  baseurl_source: declared
  description: Manage automation and placement policies
  name: IBM Turbonomic Policies API
  slug: turbonomic-policies-api
- baseURL: https://{turbonomic_host}/api/v3
  baseurl_source: declared
  description: Retrieve historical and projected resource statistics
  name: IBM Turbonomic Statistics API
  slug: turbonomic-statistics-api
- baseURL: https://{turbonomic_host}/api/v3
  baseurl_source: declared
  description: Manage discovery targets and integrations
  name: IBM Turbonomic Targets API
  slug: turbonomic-targets-api
- baseURL: https://{turbonomic_host}/api/v3
  baseurl_source: declared
  description: Manage resource and hardware templates
  name: IBM Turbonomic Templates API
  slug: turbonomic-templates-api
- baseURL: https://{turbonomic_host}/api/v3
  baseurl_source: declared
  description: Explore infrastructure topology and supply chains
  name: IBM Turbonomic Topology API
  slug: turbonomic-topology-api
artifact_total: 50
collections:
- collection_type: postman
  name: Turbonomic REST Actions API
  slug: postman-turbonomic-actions-api
- collection_type: postman
  name: Turbonomic REST Actions Authentication API
  slug: postman-turbonomic-authentication-api
- collection_type: postman
  name: Turbonomic REST Actions Entities API
  slug: postman-turbonomic-entities-api
- collection_type: postman
  name: Turbonomic REST Actions Groups API
  slug: postman-turbonomic-groups-api
- collection_type: postman
  name: Turbonomic REST Actions Markets API
  slug: postman-turbonomic-markets-api
- collection_type: postman
  name: Turbonomic REST Actions Policies API
  slug: postman-turbonomic-policies-api
- collection_type: postman
  name: Turbonomic REST Actions Statistics API
  slug: postman-turbonomic-statistics-api
- collection_type: postman
  name: Turbonomic REST Actions Targets API
  slug: postman-turbonomic-targets-api
- collection_type: postman
  name: Turbonomic REST Actions Templates API
  slug: postman-turbonomic-templates-api
- collection_type: postman
  name: Turbonomic REST Actions Topology API
  slug: postman-turbonomic-topology-api
- collection_type: open
  name: Turbonomic REST Actions API
  slug: open-turbonomic-actions-api
- collection_type: open
  name: Turbonomic REST Actions Authentication API
  slug: open-turbonomic-authentication-api
- collection_type: open
  name: Turbonomic REST Actions Entities API
  slug: open-turbonomic-entities-api
- collection_type: open
  name: Turbonomic REST Actions Groups API
  slug: open-turbonomic-groups-api
- collection_type: open
  name: Turbonomic REST Actions Markets API
  slug: open-turbonomic-markets-api
- collection_type: open
  name: Turbonomic REST Actions Policies API
  slug: open-turbonomic-policies-api
- collection_type: open
  name: Turbonomic REST API
  slug: open-turbonomic-rest-api
- collection_type: open
  name: Turbonomic REST Actions Statistics API
  slug: open-turbonomic-statistics-api
- collection_type: open
  name: Turbonomic REST Actions Targets API
  slug: open-turbonomic-targets-api
- collection_type: open
  name: Turbonomic REST Actions Templates API
  slug: open-turbonomic-templates-api
- collection_type: open
  name: Turbonomic REST Actions Topology API
  slug: open-turbonomic-topology-api
common:
- group: commercial
  href: https://artifacts.apis.io/turbonomic/plans/turbonomic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/turbonomic-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/turbonomic/rate-limits/turbonomic-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/turbonomic-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/turbonomic/finops/turbonomic-finops.yml
  title: ''
  type: FinOps
  url: finops/turbonomic-finops.yml
- group: other
  href: https://artifacts.apis.io/turbonomic/capabilities/turbonomic-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/turbonomic-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/ibm/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ibm-turbonomic/overview
- group: agent
  href: https://artifacts.apis.io/turbonomic/agentic-access/turbonomic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/turbonomic-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/turbonomic/security/turbonomic-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/turbonomic-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/turbonomic/security/turbonomic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/turbonomic-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/turbonomic/authentication/turbonomic-authentication.yml
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
  href: https://artifacts.apis.io/turbonomic/openapi/_original/turbonomic-rest-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/turbonomic-rest-api-openapi.yml
- group: other
  href: https://artifacts.apis.io/turbonomic/crd/charts.helm.k8s.io_xls.yaml
  title: ''
  type: KubernetesCRD
  url: crd/charts.helm.k8s.io_xls.yaml
- group: design
  href: https://artifacts.apis.io/turbonomic/vocabulary/turbonomic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/turbonomic-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/turbonomic/json-ld/turbonomic-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/turbonomic-context.jsonld
- group: docs
  href: https://artifacts.apis.io/turbonomic/json-schema/turbonomic-entity-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/turbonomic-entity-schema.json
- group: docs
  href: https://artifacts.apis.io/turbonomic/json-schema/turbonomic-action-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/turbonomic-action-schema.json
crds:
- name: charts.helm.k8s.io xls
  url: https://artifacts.apis.io/turbonomic/crd/charts.helm.k8s.io_xls.yaml
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
- has_sources: true
  method: derived
  name: Turbonomic Finops
  primary_unit: ''
  service_category: ''
  slug: turbonomic-finops
  template: true
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
modified: '2026-08-21'
name: IBM Turbonomic
nav: Providers
network: true
overview: 'IBM Turbonomic publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Authentication API, Entities API, and 7 more. Tagged areas include Application Resource Management, Cloud Cost Optimization, Cloud Management, Hybrid Cloud, and IBM.


  The IBM Turbonomic catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  IBM Turbonomic''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, support, and 23 more developer resources.'
plans:
- name: Turbonomic Plans Pricing
  plan_count: 4
  slug: turbonomic-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Turbonomic Rate Limits
  slug: turbonomic-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: IBM Turbonomic — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: turbonomic-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: IBM Turbonomic — rest api rules
  rule_count: 12
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 7
  slug: turbonomic-rest-api-rules
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 66.0
    catalog_earned_first_party: 12.0
    catalog_gap: 49.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 27.3
    contract_quality: 53.4
    developer_ergonomics: 48.8
    discoverability: 73.2
    operational_transparency: 21.1
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/turbonomic/turbonomic-2026-06-20T195852.png
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

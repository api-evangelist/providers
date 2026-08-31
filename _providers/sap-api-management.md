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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Sap Api Management Agentic Access
  operation_count: 18
  slug: sap-api-management-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 1
apis:
- description: The SAP API Management API provides programmatic access to manage APIs, API products, developer portal settings, and access control through the SAP API Management platform on SAP Business Technology P
  name: SAP API Management API
  slug: sap-api-management
- description: The SAP API Business Hub Enterprise (also called API Management Developer Portal) API enables programmatic management of the self-service developer portal. It supports managing API catalog content, de
  name: SAP API Business Hub Enterprise API
  slug: sap-api-business-hub-enterprise
- description: The SAP API Management Analytics API provides access to API usage metrics, performance statistics, error rates, and traffic analytics for APIs managed on the SAP API Management platform. It supports b
  name: SAP API Management Analytics API
  slug: sap-api-management-analytics
- description: Collections of APIs bundled as products for developer consumption
  name: SAP API Management API Products API
  slug: sap-api-management-api-products-api
- description: Backend systems that provide APIs for SAP API Management
  name: SAP API Management API Providers API
  slug: sap-api-management-api-providers-api
- description: Managed API proxies fronting backend services
  name: SAP API Management API Proxies API
  slug: sap-api-management-api-proxies-api
- description: Developer applications consuming API products
  name: SAP API Management Applications API
  slug: sap-api-management-applications-api
- description: Configuration key-value stores for policy runtime use
  name: SAP API Management Key Value Maps API
  slug: sap-api-management-key-value-maps-api
artifact_total: 36
collections:
- collection_type: postman
  name: SAP API Management API Portal API Products API
  slug: postman-sap-api-management-api-products-api
- collection_type: postman
  name: SAP API Management API Portal API Products API Providers API
  slug: postman-sap-api-management-api-providers-api
- collection_type: postman
  name: SAP API Management API Portal API Products API Proxies API
  slug: postman-sap-api-management-api-proxies-api
- collection_type: postman
  name: SAP API Management API Portal API Products Applications API
  slug: postman-sap-api-management-applications-api
- collection_type: postman
  name: SAP API Management API Portal API Products Key Value Maps API
  slug: postman-sap-api-management-key-value-maps-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SAP API Management API Portal API Products API
  slug: open-sap-api-management-api-products-api
- collection_type: open
  name: SAP API Management API Portal API Products API Providers API
  slug: open-sap-api-management-api-providers-api
- collection_type: open
  name: SAP API Management API Portal API Products API Proxies API
  slug: open-sap-api-management-api-proxies-api
- collection_type: open
  name: SAP API Management API Portal API Products Applications API
  slug: open-sap-api-management-applications-api
- collection_type: open
  name: SAP API Management API Portal API Products Key Value Maps API
  slug: open-sap-api-management-key-value-maps-api
- collection_type: open
  name: SAP API Management API Portal API
  slug: open-sap-api-management-portal
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sap/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sap-api-management/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-api-management-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-api-management-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-api-management-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-api-management-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sap-api-management-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://api.sap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/sap-api-management
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/products/technology-platform/api-management.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sap.com/docs/sap-api-management/sap-api-management/what-is-api-management
- group: auth
  title: ''
  type: Authentication
  url: https://help.sap.com/docs/sap-api-management/sap-api-management/user-authentication
- group: company
  title: ''
  type: Blog
  url: https://blogs.sap.com/tags/73554900100700002381/
- group: operate
  title: ''
  type: Community
  url: https://community.sap.com/topics/api-management
- group: operate
  title: ''
  type: Support
  url: https://support.sap.com/en/product/support-by-product/73554900100700002381.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP-samples
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/SAP/apibusinesshub-api-recipes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/about/agreements/policies/cloud-platform.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@SAPTechnology
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/sap-api-management
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sap-api-management-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/sap-api-management-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sap-api-management-context.jsonld
created: '2026-03-16'
description: SAP API Management is an API platform that enables organizations to design, import, publish, secure, and monitor APIs. It provides a self-service developer portal (API Business Hub Enterprise), OpenAPI-based API design tools, policy management, and access to the SAP Business Accelerator Hub for discovering and consuming SAP and partner APIs.
examples:
- key_count: 2
  name: Sap Api Management Create Api Product Example
  slug: sap-api-management-create-api-product-example
- key_count: 2
  name: Sap Api Management List Api Proxies Example
  slug: sap-api-management-list-api-proxies-example
finops:
- name: Sap Api Management Finops
  service_category: API Management
  slug: sap-api-management-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sap-api-management.png
json_schemas:
- name: SAP API Management API Product
  property_count: 7
  slug: sap-api-management-api-product
- name: SAP API Management API Proxy
  property_count: 9
  slug: sap-api-management-api-proxy
json_structures:
- name: Sap Api Management Api Proxy Structure
  property_count: 0
  slug: sap-api-management-api-proxy-structure
jsonld:
- class_count: 0
  name: Sap Api Management Context
  property_count: 12
  slug: sap-api-management-context
layout: provider
modified: '2026-08-21'
name: SAP API Management
nav: Providers
network: true
overview: 'SAP API Management publishes 5 APIs on the [APIs.io](https://apis.io/) network, including API Products API, API Providers API, API Proxies API, and 2 more. Tagged areas include API Management, Developer Portal, Enterprise, and SAP.


  The SAP API Management catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SAP API Management''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, YouTube channel, and 18 more developer resources.'
plans:
- name: Sap Api Management Plans Pricing
  plan_count: 1
  slug: sap-api-management-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Sap Api Management Rate Limits
  slug: sap-api-management-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SAP API Management API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sap-api-management-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: SAP API Management API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 3
  slug: sap-api-management-rules
scopes:
- name: Sap Api Management Scopes
  scope_count: 1
  slug: sap-api-management-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 25.0
    contract_quality: 61.9
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 23.7
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-api-management/refs/heads/main/screenshots/sap-api-management-2026-06-20T193414.png
security:
- kind: authentication
  name: Sap Api Management Authentication
  slug: sap-api-management-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sap Api Management Domain Security
  slug: sap-api-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Api Management Vulnerability Disclosure
  slug: sap-api-management-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-api-management
tags:
- API Management
- Developer Portal
- Enterprise
- SAP
website: https://www.sap.com/products/technology-platform/api-management.html
---

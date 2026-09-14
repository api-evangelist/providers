---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ifs Agentic Access
  operation_count: 7
  slug: ifs-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: 'IFS Field Service Management APIs enable work order management, scheduling optimization, technician dispatch, parts inventory, and mobile workforce coordination for energy, manufacturing, and telecom '
  name: IFS Field Service Management API
  slug: ifs-field-service-management-api
- description: IFS Enterprise Asset Management APIs provide integration with asset lifecycle management, maintenance planning, work order execution, and predictive maintenance workflows for industrial and infrastruc
  name: IFS Enterprise Asset Management API
  slug: ifs-enterprise-asset-management-api
- description: IFS Enterprise Service Management APIs enable IT service management, service catalog, incident management, and CMDB integration for enterprise IT and shared service organizations using the IFS Cloud p
  name: IFS Enterprise Service Management API
  slug: ifs-enterprise-service-management-api
- baseURL: https://{system-url}/main/ifsapplications/projection/v1
  baseurl_source: declared
  description: General ledger, vouchers, and financial entities
  name: IFS Finance API
  slug: ifs-finance-api
- baseURL: https://{system-url}/main/ifsapplications/projection/v1
  baseurl_source: declared
  description: Parts and inventory management
  name: IFS Inventory API
  slug: ifs-inventory-api
- baseURL: https://{system-url}/main/ifsapplications/projection/v1
  baseurl_source: declared
  description: Purchase orders and supplier management
  name: IFS Procurement API
  slug: ifs-procurement-api
- baseURL: https://{system-url}/main/ifsapplications/projection/v1
  baseurl_source: declared
  description: Maintenance work orders and job management
  name: IFS Work Orders API
  slug: ifs-work-orders-api
artifact_total: 25
asyncapis:
- description: ''
  name: Ifs Events
  slug: ifs-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IFS Cloud ERP API
  slug: open-ifs-cloud-erp
- collection_type: open
  name: IFS Cloud ERP Finance API
  slug: open-ifs-finance-api
- collection_type: open
  name: IFS Cloud ERP Finance Inventory API
  slug: open-ifs-inventory-api
- collection_type: open
  name: IFS Cloud ERP Finance Procurement API
  slug: open-ifs-procurement-api
- collection_type: open
  name: IFS Cloud ERP Finance Work Orders API
  slug: open-ifs-work-orders-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ifs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ifs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ifs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ifs-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ifs
- group: company
  title: ''
  type: Blog
  url: https://blog.ifs.com/feed/
- group: company
  title: ''
  type: Website
  url: https://www.ifs.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.ifs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ifs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ifs.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ifs.com/techdocs/26r1/040_tailoring/300_extensibility/020_api_explorer/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ifs.com/techdocs/26r1/040_tailoring/300_extensibility/010_get_started/
- group: operate
  title: ''
  type: Support
  url: https://community.ifs.com/
- group: operate
  title: ''
  type: Community
  url: https://community.ifs.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ifs.com/en/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ifs.com/en/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.ifs.com/en/about/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ifs.com/policy/DeprecationPolicy/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ifs-work-order-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/ifs-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/ifs-jsonschema-spectral-rules.yml
- group: build
  title: ''
  type: Packages
  url: packages/ifs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ifs-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ifs-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ifs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ifs-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/ifs-trust-center.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ifs-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ifs-events.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ifs-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ifs-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ifs-plans-pricing.yml
created: '2026-05-04'
description: IFS is a global enterprise software company providing cloud ERP, enterprise asset management, field service management, and enterprise service management platforms. APIs enable integration with IFS Cloud across manufacturing, energy, aerospace, defense, and service industries. IFS is headquartered in Linköping, Sweden with operations in over 90 countries.
finops:
- name: Ifs Finops
  service_category: Enterprise Software
  slug: ifs-finops
image: https://ifs-p-001.sitecorecontenthub.cloud/api/public/content/ifs-logo.png-e018c7?v=ec7c2a48
json_schemas:
- name: IFS Work Order
  property_count: 17
  slug: ifs-work-order
jsonld:
- class_count: 19
  name: Ifs Context
  property_count: 14
  slug: ifs-context
layout: provider
modified: '2026-09-13'
name: IFS
nav: Providers
network: true
overview: 'IFS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Finance API, Inventory API, Procurement API, and 1 more. Tagged areas include ERP, Field Service, Asset Management, Manufacturing, and Energy.


  The IFS catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  IFS''s developer surface includes authentication, engineering blog, developer portal, documentation, API reference, getting-started guide, support, and 25 more developer resources.'
plans:
- name: Ifs Plans Pricing
  plan_count: 0
  slug: ifs-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Ifs Rate Limits
  slug: ifs-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: IFS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ifs-jsonschema-spectral-rules
scopes:
- name: Ifs Scopes
  scope_count: 2
  slug: ifs-scopes
  summary_line: 2 scopes · clientCredentials/authorizationCode/authorizationCode+PKCE/password
screenshot: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/screenshots/ifs-2026-06-20T183215.png
security:
- kind: authentication
  name: Ifs Authentication
  slug: ifs-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Ifs Domain Security
  slug: ifs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ifs Trust Center
  slug: ifs-trust-center
  summary_line: ISO/IEC 27001:2013 Information Security Management, SOC 1 Type II, SOC 2 Type II, ISO 9001, TickIT Plus
slug: ifs
tags:
- ERP
- Field Service
- Asset Management
- Manufacturing
- Energy
- Cloud
- Sweden
website: https://www.ifs.com/
---

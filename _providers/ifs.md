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
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-09-20'
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
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/agentic-access/ifs-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ifs-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/security/ifs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ifs-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/authentication/ifs-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ifs-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/scopes/ifs-scopes.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/json-schema/ifs-work-order-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/ifs-work-order-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/json-ld/ifs-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/ifs-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/rules/ifs-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/ifs-jsonschema-spectral-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/packages/ifs-packages.yml
  title: ''
  type: Packages
  url: packages/ifs-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/cli/ifs-cli.yml
  title: ''
  type: CLI
  url: cli/ifs-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/changelog/ifs-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ifs-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/lifecycle/ifs-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ifs-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/conformance/ifs-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ifs-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/security/ifs-trust-center.yml
  title: ''
  type: Compliance
  url: security/ifs-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/conventions/ifs-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ifs-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/asyncapi/ifs-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/ifs-events.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/llms/ifs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ifs-llms.txt
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/rate-limits/ifs-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ifs-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/plans/ifs-plans-pricing.yml
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
random_paper: 14
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
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 54.3
    catalog_earned_first_party: 0.0
    catalog_gap: 60.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 28.0
    contract_quality: 73.8
    developer_ergonomics: 26.2
    discoverability: 75.9
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 70.3
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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

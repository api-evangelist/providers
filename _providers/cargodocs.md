---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Cargodocs Agentic Access
  operation_count: 12
  slug: cargodocs-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 3
apis:
- baseURL: https://api.essdocs.com
  baseurl_source: declared
  description: Common API endpoints shared across partner operations
  name: CargoDocs Common API
  slug: cargodocs-common-api
- baseURL: https://api.essdocs.com
  baseurl_source: declared
  description: Endpoints for retrieving and downloading documents
  name: CargoDocs Documents API
  slug: cargodocs-documents-api
- baseURL: https://api.essdocs.com
  baseurl_source: declared
  description: Partner Exchange API endpoints for customer and employee data
  name: CargoDocs Exchange API
  slug: cargodocs-exchange-api
- baseURL: https://api.essdocs.com
  baseurl_source: declared
  description: Endpoints for importing shipment data to create documents
  name: CargoDocs Import API
  slug: cargodocs-import-api
- baseURL: https://api.essdocs.com
  baseurl_source: declared
  description: Endpoints for drafting, issuing, and re-issuing electronic bills of lading
  name: CargoDocs Issuance API
  slug: cargodocs-issuance-api
- baseURL: https://api.essdocs.com
  baseurl_source: declared
  description: Endpoints for receiving surrendered electronic bills of lading
  name: CargoDocs Surrender API
  slug: cargodocs-surrender-api
- baseURL: https://api.essdocs.com
  baseurl_source: declared
  description: Endpoints for finding and managing transactions
  name: CargoDocs Transactions API
  slug: cargodocs-transactions-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CargoDocs Customer Data/Docs Common API
  slug: open-cargodocs-common-api
- collection_type: open
  name: CargoDocs Customer Data/Docs API
  slug: open-cargodocs-customer
- collection_type: open
  name: CargoDocs Customer Data/Docs Common Documents API
  slug: open-cargodocs-documents-api
- collection_type: open
  name: CargoDocs Customer Data/Docs Common Exchange API
  slug: open-cargodocs-exchange-api
- collection_type: open
  name: CargoDocs Customer Data/Docs Common Import API
  slug: open-cargodocs-import-api
- collection_type: open
  name: CargoDocs Customer Data/Docs Common Issuance API
  slug: open-cargodocs-issuance-api
- collection_type: open
  name: CargoDocs Issuer API
  slug: open-cargodocs-issuer
- collection_type: open
  name: CargoDocs Partner API
  slug: open-cargodocs-partner
- collection_type: open
  name: CargoDocs Customer Data/Docs Common Surrender API
  slug: open-cargodocs-surrender-api
- collection_type: open
  name: CargoDocs Customer Data/Docs Common Transactions API
  slug: open-cargodocs-transactions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cargodocs-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cargodocs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cargodocs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cargodocs-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.essdocs.com/
- group: other
  title: ''
  type: Product
  url: https://www.essdocs.com/cargodocs
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cargodocs-context.jsonld
- group: docs
  title: ''
  type: Partner Docs
  url: https://cargodocs-partner.readme.io/
- group: docs
  title: ''
  type: Issuer Docs
  url: https://cargodocs-issuer.readme.io/
- group: docs
  title: ''
  type: Customer Docs
  url: https://cargodocs-customer.readme.io/
- group: company
  title: ''
  type: Blog
  url: https://www.essdocs.com/blog
- group: operate
  title: ''
  type: Contact
  url: https://www.essdocs.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.essdocs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.essdocs.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/essdocs
created: '2025-01-08'
description: CargoDocs, operated by EssDocs, is a digital trade documentation platform that eliminates paper-based shipping documents by letting carriers, shippers, banks, and partner platforms issue, sign, transfer, and surrender original electronic bills of lading (eBoL), sea waybills (SWB), warehouse warrants (eWW), and supporting trade documents. CargoDocs DocEx is used by container lines, NVOCCs, bulk/tanker carriers, commodity shippers, and trade finance banks to move documents in minutes rather than days while retaining negotiability and legal effect. Developers interact with CargoDocs through three OpenAPI-described REST APIs hosted on ReadMe - the Partner API (embed DocEx in third-party platforms), the Issuer API (carrier/NVOCC issuance and amendments), and the Customer Data/Docs API (exporter drafting and back-office integration).
finops:
- name: Cargodocs Finops
  service_category: Trade Documentation Platform
  slug: cargodocs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cargodocs.png
json_schemas:
- name: CargoDocs Bill of Lading
  property_count: 10
  slug: cargodocs-bill-of-lading
- name: CargoDocs Counterparty
  property_count: 2
  slug: cargodocs-counterparty
- name: CargoDocs Customer
  property_count: 2
  slug: cargodocs-customer
- name: CargoDocs Document
  property_count: 4
  slug: cargodocs-document
- name: CargoDocs Transaction
  property_count: 4
  slug: cargodocs-transaction
jsonld:
- class_count: 0
  name: Cargodocs Context
  property_count: 5
  slug: cargodocs-context
layout: provider
modified: '2026-05-19'
name: CargoDocs
nav: Providers
network: true
overview: 'CargoDocs publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Common API, Documents API, Exchange API, and 4 more. Tagged areas include Bills of Lading, Documentation, eBoL, EssDocs, and MLETR.


  The CargoDocs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CargoDocs'' developer surface includes authentication, engineering blog, and 13 more developer resources.'
plans:
- name: Cargodocs Plans Pricing
  plan_count: 1
  slug: cargodocs-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Cargodocs Rate Limits
  slug: cargodocs-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CargoDocs API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cargodocs-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 65.3
    catalog_earned_first_party: 0.0
    catalog_gap: 49.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 67.6
    developer_ergonomics: 25.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cargodocs/refs/heads/main/screenshots/cargodocs-2026-08-17T123110.png
security:
- kind: authentication
  name: Cargodocs Authentication
  slug: cargodocs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cargodocs Domain Security
  slug: cargodocs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cargodocs
tags:
- Bills of Lading
- Documentation
- eBoL
- EssDocs
- MLETR
- Shipping
- Supply Chain
- Trade
- Trade Finance
- Warehouse Warrants
website: https://www.essdocs.com/
---

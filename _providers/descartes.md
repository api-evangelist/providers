---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Descartes Agentic Access
  operation_count: 25
  slug: descartes-agentic-access
  summary_line: 25 operations · 16 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: Trade content and classification for customs and regulatory compliance. Delivers Harmonized System (HS) codes and product classification, current tariff and duty rates and preferential-tariff details,
  name: Descartes CustomsInfo Trade Content API
  provenance: modeled
  slug: descartes-customsinfo-trade-content-api
- description: Programmatic access to Descartes Datamyne's global import/export trade data - bill-of-lading and customs records, trade flows, and company/commodity intelligence - for embedding market and supply chai
  name: Descartes Datamyne Global Trade Data API
  provenance: modeled
  slug: descartes-datamyne-trade-data-api
- description: Real-time B2B connectivity over the Descartes Global Logistics Network, complementing traditional EDI. Provides synchronous request/response integrations for marketplace connectivity (exchanging listi
  name: Descartes B2B API Connectivity
  slug: descartes-b2b-api-connectivity
- baseURL: https://macropoint-lite.com/api/1.0
  baseurl_source: declared
  description: The 3rd Party TMS Integration API from Descartes Systems Group — 5 operation(s) for 3rd party tms integration.
  name: Descartes Systems Group 3rd Party TMS Integration API
  slug: descartes-3rd-party-tms-integration-api
- baseURL: https://macropoint-lite.com/api/1.0
  baseurl_source: declared
  description: The API - XML API from Descartes Systems Group — 5 operation(s) for api - xml.
  name: Descartes Systems Group API - XML API
  slug: descartes-api-xml-api
- baseURL: https://macropoint-lite.com/api/1.0
  baseurl_source: declared
  description: The Carrier Data Connection and Communication API from Descartes Systems Group — 3 operation(s) for carrier data connection and communication.
  name: Descartes Systems Group Carrier Data Connection and Communication API
  slug: descartes-carrier-data-connection-and-communication-api
- baseURL: https://macropoint-lite.com/api/1.0
  baseurl_source: declared
  description: The Custom Integration API from Descartes Systems Group — 2 operation(s) for custom integration.
  name: Descartes Systems Group Custom Integration API
  slug: descartes-custom-integration-api
- baseURL: https://macropoint-lite.com/api/1.0
  baseurl_source: declared
  description: The Export API API from Descartes Systems Group — 1 operation(s) for export api.
  name: Descartes Systems Group Export API
  slug: descartes-export-api-api
- baseURL: https://macropoint-lite.com/api/1.0
  baseurl_source: declared
  description: The FraudGuard Carrier and Load Lookup API from Descartes Systems Group — 2 operation(s) for fraudguard carrier and load lookup.
  name: Descartes Systems Group FraudGuard Carrier and Load Lookup API
  slug: descartes-fraudguard-carrier-and-load-lookup-api
- baseURL: https://macropoint-lite.com/api/1.0
  baseurl_source: declared
  description: The Import API API from Descartes Systems Group — 2 operation(s) for import api.
  name: Descartes Systems Group Import API
  slug: descartes-import-api-api
- baseURL: https://macropoint-lite.com/api/1.0
  baseurl_source: declared
  description: The Load Visibility Order Creation - XML API from Descartes Systems Group — 3 operation(s) for load visibility order creation - xml.
  name: Descartes Systems Group Load Visibility Order Creation - XML API
  slug: descartes-load-visibility-order-creation-xml-api
- baseURL: https://macropoint-lite.com/api/1.0
  baseurl_source: declared
  description: The Load Visibility URL and Data Export Retrieval API from Descartes Systems Group — 1 operation(s) for load visibility url and data export retrieval.
  name: Descartes Systems Group Load Visibility URL and Data Export Retrieval API
  slug: descartes-load-visibility-url-and-data-export-retrieval-api
- baseURL: https://macropoint-lite.com/api/1.0
  baseurl_source: declared
  description: The Search API API from Descartes Systems Group — 1 operation(s) for search api.
  name: Descartes Systems Group Search API
  slug: descartes-search-api-api
artifact_total: 20
common:
- group: other
  href: https://artifacts.apis.io/descartes/capabilities/descartes-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/descartes-capability-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: http://www.descartes.com/resources/blog/pricing-guide-to-denied-party-screening-software-solutions
- group: agent
  href: https://artifacts.apis.io/descartes/agentic-access/descartes-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/descartes-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/descartes/rules/descartes-rules.yml
  title: ''
  type: Spectral
  url: rules/descartes-rules.yml
- group: design
  href: https://artifacts.apis.io/descartes/vocabulary/descartes-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/descartes-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/descartes/authentication/descartes-authentication.yml
  title: ''
  type: Authentication
  url: authentication/descartes-authentication.yml
- group: design
  href: https://artifacts.apis.io/descartes/errors/descartes-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/descartes-error-codes.yml
- group: design
  href: https://artifacts.apis.io/descartes/conformance/descartes-conformance.yml
  title: ''
  type: Conformance
  url: conformance/descartes-conformance.yml
- group: other
  href: https://artifacts.apis.io/descartes/hosts/descartes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/descartes-hosts.yml
- group: build
  href: https://artifacts.apis.io/descartes/integrations/descartes-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/descartes-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/descartes/vendors/descartes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/descartes-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.descartes.com/solutions/transportation-management/carrier-onboarding-fraud-prevention
- group: company
  title: ''
  type: BlogRSS
  url: https://www.descartes.com/rss.xml
- group: auth
  href: https://artifacts.apis.io/descartes/security/descartes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/descartes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.descartes.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.descartes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.macropoint.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/descartes-systems-group
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/macropoint-telematics
- group: company
  title: ''
  type: Blog
  url: https://www.descartes.com/resources/blog
- group: start
  title: ''
  type: Login
  url: https://www.descartes.com/login-register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.descartes.com/privacy-center
- group: operate
  title: ''
  type: Support
  url: https://www.descartes.com/customer-success/customer-support-and-training/customer-service-desk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.descartes.com/legal/general-terms/terms-use-descartes-ideas-portals
- group: other
  title: ''
  type: Leadership
  url: https://www.descartes.com/who-we-are/leadership
- group: company
  title: ''
  type: Newsroom
  url: https://www.descartes.com/media
- group: commercial
  href: https://artifacts.apis.io/descartes/plans/descartes-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/descartes-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/descartes/rate-limits/descartes-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/descartes-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/descartes/finops/descartes-finops.yml
  title: ''
  type: FinOps
  url: finops/descartes-finops.yml
created: '2026-07-05'
description: 'The Descartes Systems Group is a global logistics and supply chain software company whose cloud-based Global Logistics Network connects manufacturers, distributors, carriers, brokers, and freight forwarders. Descartes delivers its capabilities across a large family of products - real-time freight visibility and carrier sourcing (Descartes MacroPoint), customs and regulatory compliance and trade content (Descartes CustomsInfo, NetCHB), global trade intelligence (Descartes Datamyne), routing and mobile, and B2B connectivity and messaging. Descartes exposes APIs on a per-product basis: the MacroPoint visibility, capacity, and carrier integration APIs are publicly documented (customer credentials required), while trade content, trade data, and B2B connectivity APIs are provisioned through the Descartes API portal or a sales/contract engagement. Most API access is customer/partner-gated rather than open self-service signup.'
finops:
- has_sources: true
  method: generated
  name: Descartes Finops
  primary_unit: ''
  service_category: Logistics and Supply Chain Software
  slug: descartes-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/descartes.png
layout: provider
modified: '2026-10-06'
name: Descartes Systems Group
nav: Providers
network: true
overview: 'Descartes Systems Group publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including 3rd Party TMS Integration API, API - XML API, Carrier Data Connection and Communication API, and 10 more. Tagged areas include Logistics, Supply Chain, Freight Visibility, Shipment Tracking, and Customs Compliance.


  The Descartes Systems Group catalog on APIs.io includes 1 Spectral governance ruleset.


  Descartes Systems Group''s developer surface includes pricing, authentication, getting-started guide, documentation, engineering blog, support, and 23 more developer resources.'
plans:
- name: Descartes Plans Pricing
  plan_count: 4
  slug: descartes-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 4
  name: Descartes Rate Limits
  slug: descartes-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Descartes Systems Group API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: descartes-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 30.3
    contract_governance: 19.7
    contract_quality: 50.2
    developer_ergonomics: 45.2
    discoverability: 64.3
    operational_transparency: 7.9
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/descartes/descartes-2026-07-25T211743.png
security:
- kind: authentication
  name: Descartes Authentication
  slug: descartes-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Descartes Domain Security
  slug: descartes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: descartes
tags:
- Logistics
- Supply Chain
- Freight Visibility
- Shipment Tracking
- Customs Compliance
- Global Trade
- Trade Content
- Carrier Sourcing
website: https://www.descartes.com
---

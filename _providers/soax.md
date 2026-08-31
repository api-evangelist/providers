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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Soax Agentic Access
  operation_count: 10
  slug: soax-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- description: 'The SOAX Web Data API extracts fully rendered HTML, screenshots, XHR responses, and structured data from any public website. It handles JavaScript rendering, CAPTCHA solving, fingerprinting, headless '
  name: SOAX Web Data API
  slug: soax-web-data-api
- description: E-commerce pricing and inventory data
  name: SOAX Ecommerce Data API
  slug: soax-ecommerce-data-api
- description: Retrieve available cities, regions, carriers, and ISPs for proxy targeting
  name: SOAX Geo Targeting API
  slug: soax-geo-targeting-api
- description: Manage whitelisted IP addresses for proxy authentication
  name: SOAX IP Whitelist API
  slug: soax-ip-whitelist-api
- description: Search engine result page extraction
  name: SOAX SERP Data API
  slug: soax-serp-data-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SOAX Proxy Management Ecommerce Data API
  slug: open-soax-ecommerce-data-api
- collection_type: open
  name: SOAX Proxy Management Ecommerce Data Geo Targeting API
  slug: open-soax-geo-targeting-api
- collection_type: open
  name: SOAX Proxy Management Ecommerce Data IP Whitelist API
  slug: open-soax-ip-whitelist-api
- collection_type: open
  name: SOAX Proxy Management API
  slug: open-soax-proxy-management-api
- collection_type: open
  name: SOAX Proxy Management Ecommerce Data SERP Data API
  slug: open-soax-serp-data-api
- collection_type: open
  name: SOAX Proxy Management Ecommerce Data Web Data API
  slug: open-soax-web-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/soax-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/soax-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soax-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soax-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/soax-network
- group: company
  title: ''
  type: Website
  url: https://soax.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.soax.com/
- group: operate
  title: ''
  type: Help Center
  url: https://helpcenter.soax.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://soax.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://soax.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://soax.com/blog/
- group: design
  title: ''
  type: SpectralRules
  url: rules/soax-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/soax-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/soax-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/soax-fetch-content-example.json
created: '2025-02-21'
description: SOAX provides enterprise-grade proxy infrastructure and web data extraction APIs for developers and data teams. With 155M+ residential IPs, 33M+ mobile IPs, and 300K+ datacenter IPs across 195+ countries, SOAX enables web scraping, CAPTCHA bypass, geo-targeted data collection, and anti-bot circumvention at scale. The Web Data API handles JavaScript rendering, session management, and headless browser automation automatically.
examples:
- key_count: 4
  name: Soax Fetch Content Example
  slug: soax-fetch-content-example
finops:
- name: Soax Finops
  service_category: API
  slug: soax-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soax.png
json_schemas:
- name: SOAX Fetch Content Request
  property_count: 4
  slug: soax-fetch-request
json_structures:
- name: Soax Fetch Request Structure
  property_count: 0
  slug: soax-fetch-request-structure
jsonld:
- class_count: 39
  name: Soax Context
  property_count: 0
  slug: soax-context
layout: provider
modified: '2026-05-19'
name: SOAX
nav: Providers
network: true
overview: 'SOAX publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Web Data API, Ecommerce Data API, Geo Targeting API, and 2 more. Tagged areas include Proxy, Web Scraping, Residential Proxies, Mobile Proxies, and Datacenter Proxies.


  The SOAX catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SOAX''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, code examples, and 9 more developer resources.'
plans:
- name: Soax Plans Pricing
  plan_count: 3
  slug: soax-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Soax Rate Limits
  slug: soax-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SOAX API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: soax-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: SOAX API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: soax-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 69.2
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soax/refs/heads/main/screenshots/soax-2026-06-20T194119.png
security:
- kind: authentication
  name: Soax Authentication
  slug: soax-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Soax Domain Security
  slug: soax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Soax Trust Center
  slug: soax-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: soax
tags:
- Proxy
- Web Scraping
- Residential Proxies
- Mobile Proxies
- Datacenter Proxies
- Data Extraction
- Anti-Bot Bypass
website: https://soax.com/
---

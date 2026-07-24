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
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Soax Agentic Access
  operation_count: 10
  slug: soax-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 5
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
artifact_total: 20
collections:
- collection_type: open
  name: SOAX Proxy Management API
  slug: open-soax-proxy-management-api
- collection_type: open
  name: SOAX Web Data API
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
- group: other
  title: ''
  type: Capabilities
  url: capabilities/data-collection.yaml
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


  SOAX''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, code examples, and 10 more developer resources.'
plans:
- name: Soax Plans Pricing
  plan_count: 3
  slug: soax-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Soax Rate Limits
  slug: soax-rate-limits
rules:
- name: SOAX API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: soax-jsonschema-spectral-rules
- name: SOAX API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: soax-rules
score:
  band: developing
  composite: 55.1
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 68.3
    developer_ergonomics: 26.1
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 31.6
  previous_composite: 55.1
  schema_version: 0.5
  scored_at: '2026-07-23'
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

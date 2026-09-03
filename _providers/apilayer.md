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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'The APILayer Marketplace API provides access to 100+ APIs across geolocation, currency, weather, dev tools, marketing, finance, security, and AI/ML categories. Individual APIs include IPstack, Fixer, '
  name: APILayer Marketplace API
  slug: apilayer-api
artifact_total: 32
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apilayer-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apilayer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apilayer
- group: company
  title: ''
  type: Website
  url: https://apilayer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apilayer.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://apilayer.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://apilayer.com/signup
- group: start
  title: ''
  type: Login
  url: https://apilayer.com/login
- group: company
  title: ''
  type: Blog
  url: https://blog.apilayer.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://apilayer.com/llms.txt
created: '2025-03-01'
description: APILayer is an API marketplace and hub that enables developers to discover, integrate, and build with high-quality, reliable API services. The platform hosts 100+ APIs across categories including geolocation, currency, weather, dev tools, marketing, finance, security, and AI/ML, serving 445,000+ developers with 30 million+ API calls monthly.
examples:
- key_count: 9
  name: Apilayer Api Example
  slug: apilayer-api-example
features:
- description: Browse and integrate 100+ high-quality APIs across categories including geolocation, currency, weather, dev tools, and more.
  name: API Marketplace
- description: Single API key management across multiple APIs from the APILayer platform.
  name: Unified Authentication
- description: High-performance, reliable API infrastructure with global CDN for low-latency responses.
  name: Low Latency Infrastructure
- description: Centralized dashboard to manage API subscriptions, monitor usage, and access documentation.
  name: Developer Dashboard
- description: Real-time usage tracking and analytics across all subscribed APIs.
  name: Usage Analytics
finops:
- name: Apilayer Finops
  service_category: API
  slug: apilayer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apilayer.png
integrations:
- description: IP geolocation API for geographic profiling and location intelligence.
  name: IPstack
- description: Real-time and historical currency exchange rate data API.
  name: Fixer
- description: Real-time weather data and forecasting API.
  name: Weatherstack
- description: Search engine results page scraping and SERP data API.
  name: Serpstack
- description: Live and historical news data API for media monitoring.
  name: Mediastack
- description: Global phone number validation and carrier lookup API.
  name: Numverify
- description: Real-time cryptocurrency exchange rate data API.
  name: Coinlayer
- description: HTML to PDF conversion and document generation API.
  name: Pdflayer
json_schemas:
- name: APILayer API
  property_count: 9
  slug: apilayer-api
json_structures:
- name: Apilayer Api Structure
  property_count: 9
  slug: apilayer-api-structure
jsonld:
- class_count: 12
  name: Apilayer Context
  property_count: 1
  slug: apilayer-context
layout: provider
modified: '2026-04-19'
name: APILayer
nav: Providers
network: true
overview: 'APILayer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Catalog, API Discovery, API Marketplace, Developer Tools, and SaaS APIs.


  The APILayer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APILayer''s developer surface includes documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
plans:
- name: Apilayer Plans Pricing
  plan_count: 3
  slug: apilayer-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Apilayer Rate Limits
  slug: apilayer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: APILayer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apilayer-jsonschema-spectral-rules
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 9.8
    contract_quality: 18.7
    developer_ergonomics: 10.7
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 21.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apilayer/refs/heads/main/screenshots/apilayer-2026-06-20T172242.png
security:
- kind: domain-security
  name: Apilayer Domain Security
  slug: apilayer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apilayer
solutions:
- description: Limited free tier for each API to explore and prototype integrations.
  name: Free Plan
- description: Entry-level paid plan with increased request limits for individual APIs.
  name: Basic Plan
- description: Higher volume plans for production applications requiring reliable API access.
  name: Professional Plan
- description: Custom volume and SLA guarantees for enterprise-scale API consumption.
  name: Enterprise Plan
tags:
- API Catalog
- API Discovery
- API Marketplace
- Developer Tools
- SaaS APIs
use_cases:
- description: Determine user location, timezone, and geographic data from IP addresses using IPstack or IPapi.
  name: IP Geolocation
- description: Access real-time and historical currency exchange rates using Fixer or Currencylayer APIs.
  name: Currency Conversion
- description: Integrate real-time weather forecasts and historical weather data using Weatherstack.
  name: Weather Data
- description: Scrape search engine results programmatically using the Serpstack API.
  name: Search Engine Data
- description: Validate and look up phone number details globally using Numverify.
  name: Phone Validation
website: https://apilayer.com/
---

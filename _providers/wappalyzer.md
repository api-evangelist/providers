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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Wappalyzer Agentic Access
  operation_count: 9
  slug: wappalyzer-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 8
apis:
- description: Analyze a single website URL for technology stack detection, returning a detailed breakdown of all identified technologies, frameworks, and platforms.
  name: Wappalyzer Analyze API
  slug: wappalyzer-analyze-api
- description: Deep crawl API that indexes multiple pages of a website to build a comprehensive technology profile, supporting asynchronous callbacks for results delivery.
  name: Wappalyzer Crawl API
  slug: wappalyzer-crawl-api
- description: Bulk access to pre-built technographic datasets covering technology installations across millions of websites, suitable for market research and lead list generation.
  name: Wappalyzer Dataset API
  slug: wappalyzer-dataset-api
- description: Shared authentication, billing, and response conventions.
  name: Wappalyzer Basics API
  slug: wappalyzer-basics-api
- description: Lead list creation, pricing, and download lifecycle.
  name: Wappalyzer Lists API
  slug: wappalyzer-lists-api
- description: Website technology lookup and asynchronous crawl callbacks.
  name: Wappalyzer Lookup API
  slug: wappalyzer-lookup-api
- description: Dataset-backed website-serving subdomain discovery.
  name: Wappalyzer Subdomains API
  slug: wappalyzer-subdomains-api
- description: Email verification and deliverability checks.
  name: Wappalyzer Verify API
  slug: wappalyzer-verify-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wappalyzer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wappalyzer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wappalyzer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.wappalyzer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wappalyzer.com/docs/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/wappalyzer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wappalyzer
- group: other
  title: ''
  type: X
  url: https://twitter.com/Wappalyzer
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wappalyzer.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wappalyzer.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/wappalyzer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wappalyzer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wappalyzer-finops.yml
created: '2026-06-13'
description: Technology detection REST API for identifying software, frameworks, CMS platforms, analytics tools, and other technologies used on any website. Provides programmatic access to technographic data via lookup, analyze, crawl, and dataset endpoints using a credit-based model.
examples:
- key_count: 3
  name: Wappalyzer Create List Example
  slug: wappalyzer-create-list-example
- key_count: 12
  name: Wappalyzer Verify Example
  slug: wappalyzer-verify-example
finops:
- name: Wappalyzer Finops
  service_category: ''
  slug: wappalyzer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wappalyzer.png
json_schemas:
- name: LookupResponse
  property_count: 0
  slug: wappalyzer-lookup-response
- name: Technology
  property_count: 7
  slug: wappalyzer-technology
- name: VerifyResult
  property_count: 12
  slug: wappalyzer-verify-result
jsonld:
- class_count: 7
  name: Wappalyzer Context
  property_count: 44
  slug: wappalyzer-context
layout: provider
modified: '2026-06-13'
name: Wappalyzer
nav: Providers
network: true
overview: 'Wappalyzer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Basics API, Lists API, Lookup API, and 2 more. Tagged areas include Technology Detection, Technographics, Website Analysis, CMS Detection, and Framework Detection.


  The Wappalyzer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wappalyzer''s developer surface includes authentication, documentation, pricing, and 10 more developer resources.'
plans:
- name: Wappalyzer Plans Pricing
  plan_count: 4
  slug: wappalyzer-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Wappalyzer Rate Limits
  slug: wappalyzer-rate-limits
rules:
- name: Wappalyzer API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: wappalyzer-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.5
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 65.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wappalyzer/refs/heads/main/screenshots/wappalyzer-2026-06-20T201222.png
security:
- kind: authentication
  name: Wappalyzer Authentication
  slug: wappalyzer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wappalyzer Domain Security
  slug: wappalyzer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wappalyzer
tags:
- Technology Detection
- Technographics
- Website Analysis
- CMS Detection
- Framework Detection
- Lead Enrichment
- Sales Intelligence
website: https://www.wappalyzer.com/
---

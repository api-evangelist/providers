---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonatus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sonatus.com/
- group: company
  title: ''
  type: About
  url: https://www.sonatus.com/company/
- group: company
  title: ''
  type: Blog
  url: https://www.sonatus.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.sonatus.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sonatus
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sonatus.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sonatus.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.sonatus.com/company/newsroom/
- group: other
  title: ''
  type: Resources
  url: https://www.sonatus.com/resources/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sonatus
- group: company
  title: ''
  type: Twitter
  url: https://x.com/sonatushq
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/sonatus_stock/
- group: commercial
  title: ''
  type: Plans
  url: plans/sonatus-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sonatus-llms.txt
coverage:
  checked: '2026-08-28'
  detail: Sonatus' documentation host docs.sonatus.com answers CloudFront "Request blocked" (AWS WAF deny) with HTTP 403 on every path — including paths that do not exist and with a browser User-Agent — and has never been captured by the Internet Archive, while the public www.sonatus.com sitemap index contains no developer, docs or API section at all; the SDK and APIs Sonatus markets ship only to contracted vehicle OEM customers.
  evidence:
  - status: 403
    url: https://docs.sonatus.com/
  - status: 200
    url: https://www.sonatus.com/sitemap_index.xml
  - status: 404
    url: https://www.sonatus.com/openapi.json
  - status: 0
    url: https://api.sonatus.com/
  reason: customer-only-docs
  state: gated
created: '2026-08-28'
description: 'Sonatus, Inc. is a Sunnyvale, California automotive software company, founded in 2018, that builds cloud-to-edge vehicle AI software for software-defined vehicles (SDVs). Its Fastlane platform pairs in-vehicle Fastlane Edge software with Fastlane Collector for dynamic, policy-driven vehicle data collection, Fastlane Insight for cloud-side analysis, and Fastlane Copilot for quick-start integration, alongside the Sonatus Automator vehicle-automation product. Sonatus states its technology is deployed in more than eight million vehicles worldwide, and it is backed by Hyundai Motor Group, Kia, LG, Marvell, NEC, Foxconn and Translink Capital. Sonatus sells to vehicle OEMs and tier-one suppliers rather than to individual developers: it markets an SDK comprising Sonatus Automator, APIs and documentation, but that developer surface is delivered to contracted OEM customers and is not published on any public developer portal.'
image: https://www.sonatus.com/wp-content/uploads/2023/05/sonatus-logo.svg
layout: provider
modified: '2026-08-28'
name: Sonatus
nav: Providers
network: true
overview: 'Sonatus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Software Defined Vehicle, Vehicle Data, and Connected Vehicles.


  Sonatus'' developer surface includes engineering blog, support, and 13 more developer resources.'
plans:
- name: Sonatus Plans Pricing
  plan_count: 0
  slug: sonatus-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Sonatus Rate Limits
  slug: sonatus-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sonatus/refs/heads/main/screenshots/sonatus-2026-09-02T160206.png
security:
- kind: domain-security
  name: Sonatus Domain Security
  slug: sonatus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sonatus
tags:
- Company
- Automotive
- Software Defined Vehicle
- Vehicle Data
- Connected Vehicles
- Automotive Software
- Edge AI
- Telematics
- Embedded Software
- Artificial Intelligence
website: https://www.sonatus.com/
---

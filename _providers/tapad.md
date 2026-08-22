---
access_model:
  confidence: high
  label: Partner Only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.tapad.com
  - https://tapestry.tapad.com/tapestry/1
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The Tapestry Web API is Tapad's cross-device identity and audience endpoint. A client sends a GET request carrying a Tapad-issued partner id plus one or more device or user identifiers, and Tapad reso
  name: Tapad Tapestry Web API
  slug: tapad-tapestry-web-api
- description: Tapad's app install and in-app event tracking beacon, documented in the company's own open-source mobile SDKs as the RESOURCE_URL for the event-tracking module. A client sends a GET request with a Tap
  name: Tapad Event Tracking API
  slug: tapad-event-tracking-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.tapad.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tapad.com/global-privacy-notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tapad
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tapad-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/tapad-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tapad-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tapad-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tapad-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tapad-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tapad-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tapad-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tapad-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tapad-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tapad-llms.txt
created: '2026-07-17'
description: Tapad is a digital identity and cross-device graph technology company, founded in 2010 and headquartered in New York City. Its flagship product, the Tapad Graph, is a probabilistic device graph that lets marketers, agencies, and platforms recognize a brand's customer or related household across the many devices they use, powering programmatic targeting, media measurement, attribution, and personalization. Tapad was acquired by the Norwegian telecom Telenor in 2016 and then by the credit-and-data company Experian in 2020, and by 2026 its product and company pages redirect into Experian's Consumer Sync marketing suite while docs.tapad.com redirects to Experian's client-only Marketing Knowledge Base. Tapad runs no public developer program — no portal, no OpenAPI, no pricing and no self-service signup — but it does still operate two live first-party HTTP endpoints, the Tapestry Web API and an event tracking beacon, both requiring a partner id that only Tapad can issue, and it published
  four open-source mobile SDKs that it has since archived as unmaintained. It was added to the API Evangelist network as a portfolio company of Battery Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tapad.png
layout: provider
modified: '2026-08-12'
name: TapAd
nav: Providers
network: true
overview: 'TapAd publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Identity, and Cross-Device.


  TapAd''s developer surface includes authentication and 13 more developer resources.'
plans:
- name: Tapad Plans Pricing
  plan_count: 0
  slug: tapad-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Tapad Rate Limits
  slug: tapad-rate-limits
score:
  band: emerging
  composite: 14.4
  delta: -1.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 15.4
  provenance:
    conformance: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Tapad Authentication
  slug: tapad-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tapad Domain Security
  slug: tapad-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tapad
tags:
- Company
- Advertising
- AdTech
- Identity
- Cross-Device
- Device Graph
- Marketing
- Data
- Attribution
- Audience
- Identity Resolution
website: https://www.tapad.com
---

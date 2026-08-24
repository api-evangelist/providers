---
access_model:
  confidence: medium
  label: Customer Only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.digitalremedy.com/contact-us/
  - https://platform.digitalremedy.com/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 168
  human_in_the_loop: 124
  name: Adready Cpxi Agentic Access
  operation_count: 367
  slug: adready-cpxi-agentic-access
  summary_line: 367 operations · 168 acting · 124 human-in-the-loop
api_count: 1
apis:
- description: The REST API behind the Digital Remedy Platform / AdReady+ web application. 285 paths and 355 operations covering accounts, organizations, agencies and advertisers; users and permissions; media plans,
  name: Digital Remedy Platform (Kickstart) API
  slug: digital-remedy-platform-kickstart-api
artifact_total: 8
collections:
- collection_type: open
  name: Kickstart API
  slug: open-adready-cpxi-kickstart
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adready-cpxi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/adready-cpxi-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.digitalremedy.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adready-cpxi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.digitalremedy.com/platform/
- group: start
  title: ''
  type: Login
  url: https://platform.digitalremedy.com/
- group: company
  title: ''
  type: Blog
  url: https://www.digitalremedy.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.digitalremedy.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digitalremedy.com/privacy-policy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/adready-cpxi-kickstart-openapi.yml
- group: docs
  title: ''
  type: APIReference
  url: https://platform.digitalremedy.com/swagger-ui.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/adready-cpxi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adready-cpxi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adready-cpxi-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adready-cpxi-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adready-cpxi-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adready-cpxi-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adready-cpxi-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/adready-cpxi-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adready-cpxi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adready-cpxi-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/adready-cpxi-kickstart-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adready-cpxi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digitalremedy.com/terms-and-conditions/
- group: company
  title: ''
  type: About
  url: https://www.digitalremedy.com/about/
created: '2026-07-17'
description: AdReady is a digital advertising execution brand operated by Digital Remedy (formerly CPX Interactive / CPXi). Digital Remedy runs an omnichannel advertising management platform - marketed as the Digital Remedy Platform and historically as AdReady+ - for independent agencies, brands and media companies, covering media planning, RFPs, insertion-order and line-item management, programmatic / CTV / DOOH / social execution, pixel-based attribution (Flip), incrementality and brand-lift measurement, white-label reporting and a RemyAI assistant, on top of 100+ martech integrations and 300+ inventory and data sources. AdReady originated as a Seattle self-serve ad-building tool and was acquired by CPXi in 2013; the brand and platform are today part of Digital Remedy, which has since combined with Compulse. The platform is powered by an internally-named Kickstart API - a Spring Boot / springdoc REST service whose OpenAPI 3.1 description is served anonymously at platform.digitalremedy.com/v3/api-docs
  with a browsable Swagger UI - but Digital Remedy publishes no public developer portal, no onboarding, and no partner API documentation, and every business operation on that API is authenticated (HTTP 401 without a session JWT). This company profile is independently maintained in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adready-cpxi.png
layout: provider
modified: '2026-08-12'
name: AdReady (CPXi)
nav: Providers
network: true
overview: 'AdReady (CPXi) publishes 1 API on the [APIs.io](https://apis.io/) network: Digital Remedy Platform (Kickstart) API. Tagged areas include Company, Commerce, Advertising, AdTech, and Marketing.


  AdReady (CPXi)''s developer surface includes engineering blog, support, API reference, authentication, changelog, and 21 more developer resources.'
plans:
- name: Adready Cpxi Plans Pricing
  plan_count: 0
  slug: adready-cpxi-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Adready Cpxi Rate Limits
  slug: adready-cpxi-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 16.7
    contract_quality: 45.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adready-cpxi/refs/heads/main/screenshots/adready-cpxi-2026-07-25T181701.png
security:
- kind: authentication
  name: Adready Cpxi Authentication
  slug: adready-cpxi-authentication
  summary_line: session-jwt · 1 scheme
- kind: domain-security
  name: Adready Cpxi Domain Security
  slug: adready-cpxi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Adready Cpxi Trust Center
  slug: adready-cpxi-trust-center
  summary_line: SOC 2
slug: adready-cpxi
tags:
- Company
- Commerce
- Advertising
- AdTech
- Marketing
- Programmatic
- Media
- Media Planning
- Campaign Management
- Attribution
- Connected TV
- Ad Operations
- Measurements
- Agencies
website: https://www.digitalremedy.com/platform/
---

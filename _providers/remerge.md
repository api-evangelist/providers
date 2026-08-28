---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: JSON reporting API that lets Remerge advertisers pull daily (or hourly) campaign performance for their active campaigns into their own BI systems. A POST to /report with a start_date and end_date retu
  name: Remerge Reporting API
  slug: remerge-reporting-api
- description: Server-to-server ingestion API that Remerge clients and measurement partners use to forward data into the Remerge platform. A single GET endpoint at remerge.events/event accepts four documented payloa
  name: Remerge Event Tracking API
  slug: remerge-event-tracking-api
artifact_total: 9
asyncapis:
- description: ''
  name: Remerge Webhooks
  slug: remerge-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.remerge.io
- group: operate
  title: ''
  type: Support
  url: https://help.remerge.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.remerge.io/blog-post
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/remerge
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.remerge.io/service-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.remerge.io/terms-and-conditions
- group: auth
  title: ''
  type: TrustCenter
  url: security/remerge-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.remerge.io/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/remerge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.remerge.io/remerge-vulnerability-disclosure-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/remerge-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/remerge-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.remerge.io/hc/en-us/categories/115000321013-Data-Exchange
- group: docs
  title: ''
  type: Documentation
  url: https://help.remerge.io/hc/en-us/sections/115000697994-API-Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://help.remerge.io/hc/en-us/articles/115003440434-Remerge-Reporting-API
- group: start
  title: ''
  type: Login
  url: https://admin.remerge.io
- group: auth
  title: ''
  type: Authentication
  url: authentication/remerge-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/remerge-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/remerge-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/remerge-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/remerge-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/remerge-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/remerge-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/remerge-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/remerge-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/remerge-webhooks.yml
created: '2026-07-17'
description: 'Remerge is a mobile demand-side platform (DSP) specializing in app retargeting, re-engagement, and user acquisition for mobile apps. The Berlin-based company (Remerge GmbH) helps advertisers in gaming, e-commerce, and delivery build in-app audience segments, run programmatic re-engagement and acquisition campaigns across millions of ad placements, and validate results with incrementality measurement. Onboarding is account-managed rather than self-service, but Remerge does publish two documented HTTP APIs: a JSON Reporting API at api.remerge.io for pulling daily campaign performance into a client''s BI stack, and an Event Tracking API at remerge.events for forwarding in-app event, attribution, BI and SKAdNetwork data into Remerge. It operates an ISO/IEC 27001:2022-aligned ISMS and publishes a public Trust Center and vulnerability disclosure policy.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/remerge.png
layout: provider
modified: '2026-08-12'
name: Remerge
nav: Providers
network: true
overview: 'Remerge publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Mobile, and Retargeting.


  The Remerge catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Remerge''s developer surface includes support, engineering blog, documentation, API reference, authentication, and 21 more developer resources.'
plans:
- name: Remerge Plans Pricing
  plan_count: 0
  slug: remerge-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Remerge Rate Limits
  slug: remerge-rate-limits
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 45.0
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/remerge/refs/heads/main/screenshots/remerge-2026-08-17T081511.png
security:
- kind: authentication
  name: Remerge Authentication
  slug: remerge-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Remerge Domain Security
  slug: remerge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Remerge Vulnerability Disclosure
  slug: remerge-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Remerge Trust Center
  slug: remerge-trust-center
  summary_line: ISO 27001, GDPR
slug: remerge
tags:
- Company
- Advertising
- AdTech
- Mobile
- Retargeting
- Demand-Side Platform
- User Acquisition
- Marketing
website: https://www.remerge.io
---

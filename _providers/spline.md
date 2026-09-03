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
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: Client SDK for embedding and interacting with Spline scenes from JavaScript.
  name: Spline Code API for Web
  slug: code-api-web
- description: iOS client SDK for embedding Spline scenes in SwiftUI apps.
  name: Spline Code API for SwiftUI
  slug: code-api-swiftui
- description: Android client SDK for embedding Spline scenes in Kotlin apps.
  name: Spline Code API for Kotlin
  slug: code-api-kotlin
- description: Real-time API for binding variables and data into live Spline scenes.
  name: Spline Real-time Variables and Data API
  slug: realtime-variables
- description: Webhook events for Spline integrations.
  name: Spline Webhooks
  slug: webhooks
artifact_total: 11
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/spline-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spline-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spline-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/splinetool
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/splinetool
- group: company
  title: ''
  type: Website
  url: https://spline.design/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spline.design/
- group: commercial
  title: ''
  type: Plans
  url: plans/spline-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spline-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spline-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.spline.design/llms.txt
created: '2026-05-08'
description: Spline is a real-time collaborative 3D design tool with AI-driven object generation, web embedding, and animation. Spline does NOT publish a REST API for 3D scene generation as of May 2026; instead it exposes Code APIs (Web, SwiftUI, Kotlin) for embedding scenes, plus a real-time API for variables/data and webhooks for event-driven integrations.
finops:
- name: Spline Finops
  service_category: 3D
  slug: spline-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spline.png
layout: provider
modified: '2026-05-08'
name: Spline
nav: Providers
network: true
overview: 'Spline publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 3D, Design, Artificial Intelligence, Collaboration, and Web.


  Spline''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Spline Plans Pricing
  plan_count: 4
  slug: spline-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Spline Rate Limits
  slug: spline-rate-limits
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spline/refs/heads/main/screenshots/spline-2026-06-20T194404.png
security:
- kind: domain-security
  name: Spline Domain Security
  slug: spline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spline Vulnerability Disclosure
  slug: spline-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Spline Trust Center
  slug: spline-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: spline
tags:
- 3D
- Design
- Artificial Intelligence
- Collaboration
- Web
- SDK
website: https://spline.design/
---

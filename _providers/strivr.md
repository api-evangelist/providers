---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 5.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The Strivr Software Development Kit for Unity makes Unity projects compatible with the Strivr Player in-headset software and with the Strivr Portal. It is used to create and score experiences, track c
  name: Strivr SDK for Unity
  slug: strivr-unity-sdk
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.strivr.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.strivr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.strivr.com/docs/sdk/latest/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.strivr.com/docs/sdk/latest/unity/getting-started.html
- group: start
  title: ''
  type: SignUp
  url: https://developer.strivr.com/contact.html
- group: start
  title: ''
  type: Login
  url: https://portal.strivr.com/
- group: operate
  title: ''
  type: Support
  url: https://support.strivr.com/
- group: company
  title: ''
  type: Blog
  url: https://www.strivr.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.strivr.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.strivr.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.strivr.com/
- group: auth
  title: ''
  type: Compliance
  url: security/strivr-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/strivr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/strivr-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/strivr-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/strivr-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/strivr-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/strivr-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/strivr-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/strivr-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/strivr-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/strivr-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/strivr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/strivr-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/strivr-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/strivr-domain-security.yml
created: '2026-08-29'
description: 'Strivr is an enterprise frontline-work platform founded in 2015 out of Stanford University''s Virtual Human Interaction Lab by Derek Belch. It began as immersive VR workforce training deployed at scale by Walmart, Bank of America and Verizon, and has since become an AI-native "Frontline Intelligence" layer that trains custom Visual Language Models on real-world workflows to detect, correct and guide task execution in real time through smart glasses. Its public developer surface is the Strivr SDK for Unity, which links a Unity project to a project in the Strivr Portal and streams experience, custom-event and gaze-tracking telemetry into Strivr''s performance analytics. Strivr publishes no OpenAPI, GraphQL SDL or Postman collection; the REST host api.strivr.com answers 401 WWW-Authenticate: Bearer on every path.'
image: https://developer.strivr.com/images/Logo.png
layout: provider
modified: '2026-08-29'
name: Strivr
nav: Providers
network: true
overview: 'Strivr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Immersive Learning, Virtual Reality, Workforce Training, Frontline Operations, and Artificial Intelligence.


  Strivr''s developer surface includes documentation, getting-started guide, signup flow, support, engineering blog, authentication, changelog, and 19 more developer resources.'
plans:
- name: Strivr Plans Pricing
  plan_count: 0
  slug: strivr-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Strivr Rate Limits
  slug: strivr-rate-limits
score:
  band: thin
  composite: 32.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 32.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/strivr/refs/heads/main/screenshots/strivr-2026-09-02T161019.png
security:
- kind: authentication
  name: Strivr Authentication
  slug: strivr-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Strivr Domain Security
  slug: strivr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Strivr Trust Center
  slug: strivr-trust-center
  summary_line: SOC 2 Type 2, CCPA, CPRA
slug: strivr
tags:
- Immersive Learning
- Virtual Reality
- Workforce Training
- Frontline Operations
- Artificial Intelligence
- Analytics
- Unity SDK
- Smart Glasses
- Enterprise
- Learning and Development
website: https://www.strivr.com/
---

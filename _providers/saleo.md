---
access_model:
  confidence: medium
  label: Sales-Gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://saleo.io/pricing/
  - https://saleo.io/request-a-demo/
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
  score: 7.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: SCIM 2.0 (RFC 7643 / RFC 7644) user and group provisioning endpoint for the Saleo platform. Documented for customers through the Saleo Okta Integration Network application, which supports Create Users
  name: Saleo SCIM 2.0 Provisioning API
  slug: saleo-scim-20-provisioning-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saleo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.saleo.io
- group: start
  title: ''
  type: Portal
  url: https://app.platform.saleo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.saleo.io/
- group: operate
  title: ''
  type: Support
  url: https://saleo.io/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.saleo.io/
- group: company
  title: ''
  type: Blog
  url: https://saleo.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://saleo.io/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.platform.saleo.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://saleo.io/about-us/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://saleo.io/about-us/privacy-policy/
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://saleo.io/about-us/acceptable-use-policy/
- group: auth
  title: ''
  type: Security
  url: https://saleo.io/platform/security/
- group: auth
  title: ''
  type: Compliance
  url: https://saleo.io/platform/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/saleo-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.saleo.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/saleo-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/saleo-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/saleo-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/saleo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/saleo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/saleo-problem-types.yml
- group: design
  title: ''
  type: Components
  url: components/saleo-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/saleo-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/saleo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/saleo-rate-limits.yml
created: '2026-07-17'
description: Saleo is an AI-native demo experience platform for go-to-market teams, enabling sales and pre-sales engineers to run high-stakes live demos inside their native product, build self-serve interactive product tours, and deliver autonomous AI-driven demos around the clock. Its products include Live (real demos backed by AI-generated demo data), AI Demo Agent (autonomous multi-lingual discovery and demo agents), Data Creation Agent, Capture (interactive product tours and embeddable sandboxes), and a Partner Portal for resellers. Saleo serves enterprise customers including SAP, Salesforce, 6sense, Seismic, and SailPoint, and is backed by Emergence Capital. Its only standards-based, externally documented API is a SCIM 2.0 user and group provisioning endpoint used by the Saleo app in the Okta Integration Network; the product API that backs the Saleo Portal, Chrome extension and tour viewer is customer-authenticated and undocumented.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saleo.png
layout: provider
modified: '2026-08-13'
name: Saleo
nav: Providers
network: true
overview: 'Saleo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales Tech, Demo Automation, Sales Enablement, and Presales.


  Saleo''s developer surface includes developer portal, documentation, support, engineering blog, pricing, authentication, and 20 more developer resources.'
plans:
- name: Saleo Plans Pricing
  plan_count: 0
  slug: saleo-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Saleo Rate Limits
  slug: saleo-rate-limits
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 20.5
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/saleo/refs/heads/main/screenshots/saleo-2026-09-02T154319.png
security:
- kind: authentication
  name: Saleo Authentication
  slug: saleo-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Saleo Domain Security
  slug: saleo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Saleo Trust Center
  slug: saleo-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, GDPR
slug: saleo
tags:
- Company
- Sales Tech
- Demo Automation
- Sales Enablement
- Presales
- Go-To-Market
- AI Agents
- SCIM
- Identity Provisioning
- Single Sign-On
- Interactive Demos
- Product Tours
website: https://www.saleo.io
---

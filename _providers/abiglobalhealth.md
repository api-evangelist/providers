---
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
    well_known_catalog: true
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-06'
api_count: 1
apis:
- description: Partner REST API for managing user accounts, subscriptions, text consultations, form-based prescriptions, Health Navigator AI conversations and outbound webhooks. Resource-oriented URLs, JSON response
  name: Abi API
  slug: abi-api
artifact_total: 6
asyncapis:
- description: ''
  name: Abiglobalhealth Webhooks
  slug: abiglobalhealth-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.abiglobalhealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.abi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.abi.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.abi.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.abiglobalhealth.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.abiglobalhealth.com/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/abiglobalhealth
- group: start
  title: ''
  type: SignUp
  url: https://www.abiglobalhealth.com/demo-form
- group: start
  title: ''
  type: Login
  url: https://partner.abi.ai/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abiglobalhealth.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abiglobalhealth-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/abiglobalhealth-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/abiglobalhealth-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/abiglobalhealth-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/abiglobalhealth-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/abiglobalhealth-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/abiglobalhealth-vocabulary.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abiglobalhealth-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/abiglobalhealth-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/abiglobalhealth-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/abiglobalhealth-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/abiglobalhealth-packages.yml
- group: design
  title: ''
  type: Components
  url: components/abiglobalhealth-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/abiglobalhealth-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/abiglobalhealth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abiglobalhealth-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abiglobalhealth-domain-security.yml
created: '2026-09-06'
description: Abi Global Health is an AI-native healthcare navigation, virtual care orchestration and clinical cost management platform founded in Dublin, Ireland in 2016. Abi sells to health insurers, employee benefits providers, TPAs, assistance companies, digital health organisations, pharmaceutical companies and public health programmes rather than direct to consumers, and delivers text, voice and video consultations, mental-health screening, form-based prescriptions and the Abi Navigator AI triage assistant through chat apps, an embeddable widget, a web app and a partner REST API. The Abi API (documented at docs.abi.ai, base https://client-api.abi.ai with Hong Kong and mainland-China regional bases) covers users, subscriptions, consultations, prescriptions, Health Navigator conversations and outbound webhooks, and is gated behind a partner account and an issued API key.
image: https://www.abiglobalhealth.com/hubfs/AbiLogoMark_314x262px_RGB.png
layout: provider
modified: '2026-09-06'
name: Abi Global Health
nav: Providers
network: true
overview: 'Abi Global Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telehealth, Virtual Care, Digital Health, and Health Insurance.


  The Abi Global Health catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Abi Global Health''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, sandbox, and 20 more developer resources.'
plans:
- name: Abiglobalhealth Plans Pricing
  plan_count: 0
  slug: abiglobalhealth-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Abiglobalhealth Rate Limits
  slug: abiglobalhealth-rate-limits
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.0
    catalog_earned_first_party: 5.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 33.3
    contract_quality: 41.6
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 40.0
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: authentication
  name: Abiglobalhealth Authentication
  slug: abiglobalhealth-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Abiglobalhealth Domain Security
  slug: abiglobalhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abiglobalhealth
tags:
- Company
- Telehealth
- Virtual Care
- Digital Health
- Health Insurance
- Healthcare Navigation
- Artificial Intelligence
- Prescriptions
- Webhooks
- Ireland
website: https://www.abiglobalhealth.com/
---

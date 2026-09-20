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
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-09-19'
api_count: 1
apis:
- description: 'The Integrately platform connects 1500+ SaaS applications through a catalog of 20 million+ pre-built one-click automations covering common business workflows such as lead capture, CRM sync, marketing '
  name: Integrately Platform
  slug: platform
artifact_total: 7
asyncapis:
- description: ''
  name: Integrately Webhooks
  slug: integrately-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.integrately.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/security/integrately-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/integrately-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://integrately.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://integrately.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://integrately.com/blog
- group: start
  title: ''
  type: Signup
  url: https://app.integrately.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.integrately.com/login
- group: commercial
  title: ''
  type: Privacy
  url: https://integrately.com/home/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://integrately.com/home/terms
- group: other
  title: ''
  type: X
  url: https://twitter.com/integratelyapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/integrately
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCtLeDvJ7HVKuZ6O5UtwgnMA
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/groups/integraters
- group: start
  title: ''
  type: GettingStarted
  url: https://integrately.com/docs#create-your-own-automations
- group: operate
  title: ''
  type: Community
  url: https://www.facebook.com/groups/integraters
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/plans/integrately-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/integrately-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/rate-limits/integrately-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/integrately-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/finops/integrately-finops.yml
  title: ''
  type: FinOps
  url: finops/integrately-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/rules/integrately-rules.yml
  title: ''
  type: SpectralRules
  url: rules/integrately-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/asyncapi/integrately-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/integrately-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/components/integrately-components.yml
  title: ''
  type: Components
  url: components/integrately-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/data-model/integrately-data-model.yml
  title: ''
  type: DataModel
  url: data-model/integrately-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/conventions/integrately-conventions.yml
  title: ''
  type: Conventions
  url: conventions/integrately-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/conformance/integrately-conformance.yml
  title: ''
  type: Conformance
  url: conformance/integrately-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/lifecycle/integrately-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/integrately-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/packages/integrately-packages.yml
  title: ''
  type: Packages
  url: packages/integrately-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/llms/integrately-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/integrately-llms.txt
created: '2026-03-27'
description: Integrately is a one-click workflow automation platform offering 20 million+ ready-to-use automations across 1500+ applications. It positions itself as a no-code, lower-cost alternative to other iPaaS and workflow tools, using SmartConnect technology to auto-detect connections between apps and bundle expert-built automations at no extra cost.
finops:
- name: Integrately Finops
  service_category: API
  slug: integrately-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/integrately.png
layout: provider
modified: '2026-09-13'
name: Integrately
nav: Providers
network: true
overview: 'Integrately publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Business Process Automation, iPaaS, No-Code, and SaaS Integration.


  The Integrately catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Integrately''s developer surface includes documentation, pricing, engineering blog, signup flow, privacy policy, YouTube channel, getting-started guide, and 20 more developer resources.'
plans:
- name: Integrately Plans Pricing
  plan_count: 5
  slug: integrately-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 10
  name: Integrately Rate Limits
  slug: integrately-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Integrately API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: integrately-rules
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 26.2
    discoverability: 75.9
    operational_transparency: 39.5
  previous_composite: 46.5
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/integrately/refs/heads/main/screenshots/integrately-2026-06-20T183428.png
security:
- kind: domain-security
  name: Integrately Domain Security
  slug: integrately-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: integrately
tags:
- Automation
- Business Process Automation
- iPaaS
- No-Code
- SaaS Integration
- SMB
- Triggers and Actions
- Webhook
- Workflow-Automation
- Workflows
website: https://www.integrately.com/
---

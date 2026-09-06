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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The Integrately platform connects 1500+ SaaS applications through a catalog of 20 million+ pre-built one-click automations covering common business workflows such as lead capture, CRM sync, marketing '
  name: Integrately Platform
  slug: platform
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/integrately-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://integrately.com
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
  url: https://facebook.com/groups/integraters
created: '2026-03-27'
description: Integrately is a one-click workflow automation platform offering 20 million+ ready-to-use automations across 1500+ applications. It positions itself as a no-code, lower-cost alternative to other iPaaS and workflow tools, using SmartConnect technology to auto-detect connections between apps and bundle expert-built automations at no extra cost.
finops:
- name: Integrately Finops
  service_category: API
  slug: integrately-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/integrately.png
layout: provider
modified: '2026-04-28'
name: Integrately
nav: Providers
network: true
overview: 'Integrately publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Business Process Automation, iPaaS, No-Code, and SaaS Integration.


  The Integrately catalog on APIs.io includes 1 Spectral governance ruleset.


  Integrately''s developer surface includes developer portal, documentation, pricing, engineering blog, signup flow, privacy policy, YouTube channel, and 6 more developer resources.'
plans:
- name: Integrately Plans Pricing
  plan_count: 3
  slug: integrately-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
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
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
website: https://integrately.com
---

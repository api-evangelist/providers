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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://praxispro.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.praxispro.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/praxispro-ai-changelog.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.praxispro.ai/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.praxispro.ai/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/praxispro-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.praxispro.ai/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/praxispro-ai-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/praxispro-ai-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/praxispro-ai-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/praxispro-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/praxispro-ai-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/praxispro-ai-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.praxispro.ai/contact-us
- group: start
  title: ''
  type: Login
  url: https://app.praxispro.ai/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/praxispro-ai/
coverage:
  checked: '2026-08-14'
  detail: PraxisPro ships an enterprise life-sciences training SaaS with no developer program at all — its own 20-URL sitemap has no docs, pricing or developer page, and the one host named api.praxispro.ai is a CNAME to the third-party vendor api.rev.ai rather than a PraxisPro API.
  evidence:
  - status: 200
    url: https://www.praxispro.ai/sitemap.xml
  - status: 404
    url: https://www.praxispro.ai/docs
  - status: 404
    url: https://app.praxispro.ai/openapi.json
  - status: 404
    url: https://api.praxispro.ai/openapi.json
  - status: 403
    url: https://tm4ggh1m3b.execute-api.us-east-1.amazonaws.com/
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: PraxisPro AI is an AI-powered training platform built to modernize pharmaceutical and medical device sales training for life sciences organizations. Its modules include PraxisPlay (AI roleplay simulations with realistic healthcare-provider agents), PraxisCertify (certification tracking and knowledge-gap identification), PraxisCoach (performance coaching and feedback), and PraxisIntelligence (analytics and insights for management). The platform serves sales reps, trainers, managers, MSLs, compliance, and marketing teams with personalized, AI-driven scenarios, immediate feedback, and performance tracking. Backed by Techstars. Delivered as a SaaS product; no public developer API surface is published at the time of enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/praxispro-ai.png
layout: provider
modified: '2026-08-14'
name: PraxisPro AI
nav: Providers
network: true
overview: 'PraxisPro AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Sales Training, Sales Enablement, and Life Sciences.


  PraxisPro AI''s developer surface includes engineering blog, changelog, support, and 13 more developer resources.'
plans:
- name: Praxispro Ai Plans Pricing
  plan_count: 0
  slug: praxispro-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Praxispro Ai Rate Limits
  slug: praxispro-ai-rate-limits
score:
  band: emerging
  composite: 21.2
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 21.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Praxispro Ai Domain Security
  slug: praxispro-ai-domain-security
  summary_line: no transport/DNS hardening detected
- kind: vulnerability-disclosure
  name: Praxispro Ai Vulnerability Disclosure
  slug: praxispro-ai-vulnerability-disclosure
  summary_line: contact published
slug: praxispro-ai
tags:
- Company
- Artificial Intelligence
- Sales Training
- Sales Enablement
- Life Sciences
- Pharmaceuticals
- Medical Devices
- Role-Play Simulation
- Learning and Development
website: https://praxispro.ai/
---

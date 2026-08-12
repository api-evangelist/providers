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
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.7
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://passes.com
- group: operate
  title: ''
  type: Support
  url: https://www.passes.com/help
- group: start
  title: ''
  type: SignUp
  url: https://www.passes.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.passes.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.passes.com/term
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.passes.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/passes-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/passes-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/passes-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/passes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.passes.com/help/bugs
- group: auth
  title: ''
  type: DomainSecurity
  url: security/passes-domain-security.yml
created: '2026-07-17'
description: Passes is a creator monetization and accelerator platform founded in 2022 by Lucy Guo and headquartered in Los Angeles. Creators use Passes to build direct, paid relationships with their audiences through subscriptions, paid DMs, livestreams, one-on-one video calls, merchandise, automated message sequences, and instant payouts, while keeping 90% of what they earn. Backed by Bond Capital and Multicoin Capital, the company rebranded in 2026 as a creator accelerator. Passes does not currently publish a public developer API; this profile captures its real public web surface — llms.txt, security.txt, mobile deep-link association files, and domain-security posture — harvested by the API Evangelist enrichment pipeline.
image: https://www.passes.com/assets/open-graph/1200x630.png
layout: provider
modified: '2026-07-20'
name: Passes
nav: Providers
network: true
overview: 'Passes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator, Creator Economy, Monetization, and Subscriptions.


  Passes'' developer surface includes support, signup flow, and 10 more developer resources.'
random_paper: 75
score:
  band: emerging
  composite: 17.3
  delta: -0.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/passes/refs/heads/main/screenshots/passes-2026-08-07T191536.png
security:
- kind: domain-security
  name: Passes Domain Security
  slug: passes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Passes Vulnerability Disclosure
  slug: passes-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: passes
tags:
- Company
- Creator
- Creator Economy
- Monetization
- Subscriptions
- Payments
- Content
- Social Media
website: https://passes.com
---

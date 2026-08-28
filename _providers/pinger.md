---
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pinger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pinger.com/
- group: company
  title: ''
  type: About
  url: https://www.pinger.com/about/
- group: operate
  title: ''
  type: Support
  url: https://www.pinger.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.sideline.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pinger.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pinger.com/privacy-policy/
- group: other
  title: ''
  type: Product
  url: https://textfree.com/
- group: other
  title: ''
  type: Product
  url: https://www.sideline.com/
- group: other
  title: ''
  type: Product
  url: https://getindex.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pinger-sideline-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/pinger-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pinger-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Pinger ships only end-user apps (TextFree, Sideline, Index) - there is no developer site (developer.pinger.com and docs.pinger.com do not resolve in DNS), and api.pinger.com is a retired or private mobile-app backend that 302s its root to the marketing site and returns 410 Gone for every path probed.
  evidence:
  - status: 410
    url: https://api.pinger.com/v1/
  - status: 404
    url: https://www.pinger.com/openapi.json
  - status: 404
    url: https://www.pinger.com/.well-known/api-catalog
  - status: 200
    url: https://www.sideline.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Pinger, Inc. is a San Jose, California mobile communications company founded in 2005 by former Palm managers Greg Woock and Joe Sipher. It builds consumer and small-business calling and texting apps rather than developer infrastructure: TextFree (launched 2009, the original free texting and calling app with a free US phone number), Sideline (a second phone number for work and privacy, with team number sharing, spam filtering, auto-reply and voicemail transcription) and Index (a dedicated business line with auto-reply, scheduling, broadcast messaging and payment collection). Sideline and TextFree have together been used by more than 100 million people. Pinger publishes no public developer program, API reference, OpenAPI definition or SDK — its integrations run the other way, with Index consuming third-party calendar (Google, iCloud, Outlook) and payment (PayPal, Venmo, Square) services. The one machine-readable artifact it publishes is an llms.txt information sheet on the Sideline
  domain.'
image: https://www.pinger.com/wp-content/uploads/2021/11/pinger_new@2x-277x300.png
layout: provider
modified: '2026-08-26'
name: Pinger
nav: Providers
network: true
overview: 'Pinger is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communications, Telecommunications, Messaging, and SMS.


  Pinger''s developer surface includes support and 12 more developer resources.'
plans:
- name: Pinger Plans Pricing
  plan_count: 0
  slug: pinger-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Pinger Rate Limits
  slug: pinger-rate-limits
score:
  band: minimal
  composite: 9.4
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Pinger Domain Security
  slug: pinger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pinger
tags:
- Company
- Communications
- Telecommunications
- Messaging
- SMS
- Voice
- Mobile Applications
- Phone Numbers
- Consumer Applications
- Small Business
website: https://www.pinger.com/
---

---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
  pricing: free
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/friend-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://friend.com/
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Friend_(product)
- group: other
  title: ''
  type: SacraProfile
  url: https://sacra.com/c/friend/
- group: commercial
  title: ''
  type: Plans
  url: plans/friend-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/friend-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/friend-com-finops.yml
created: '2026-05-23'
description: Friend is an AI companion pendant — a sub-two-inch wearable with a microphone that pairs with a phone app and communicates back to the user via text messages rather than speech. Originally announced at $99, the product shipped (after delays) in 2025 at $129 in North America. Friend is a consumer hardware company with no public developer API, SDK, or partner program; only the consumer site, an app, and the Wikipedia / press coverage exist as references.
finops:
- name: Friend Com Finops
  service_category: API
  slug: friend-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/friend-com.png
layout: provider
modified: '2026-07-25'
name: Friend
nav: Providers
network: true
overview: Friend is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Wearable, Pendant, Companion, and Consumer Hardware.
plans:
- name: Friend Com Plans Pricing
  plan_count: 1
  slug: friend-com-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 2
  name: Friend Com Rate Limits
  slug: friend-com-rate-limits
score:
  band: emerging
  composite: 13.5
  delta: -1.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/friend-com/refs/heads/main/screenshots/friend-com-2026-06-20T181547.png
security:
- kind: domain-security
  name: Friend Com Domain Security
  slug: friend-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: friend-com
tags:
- AI
- Wearable
- Pendant
- Companion
- Consumer Hardware
- No Public API
website: https://friend.com/
---

---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
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
api_count: 3
apis:
- description: RESTful API for managing Chameleon experiences including Tours, Tooltips, Launchers, Microsurveys, and Embeddables. Supports user profile management, segmentation, experience delivery, survey response
  name: Chameleon REST API
  slug: chameleon-rest-api
- description: Client-side JavaScript SDK for identifying users, tracking custom events, triggering experiences programmatically, and passing personalization variables to Chameleon from the browser. Enables single-p
  name: Chameleon JavaScript API
  slug: chameleon-javascript-api
- description: Outgoing webhooks that deliver real-time event notifications when users interact with Chameleon experiences such as completing tours, submitting survey responses, or dismissing modals. Chameleon deliv
  name: Chameleon Webhooks
  slug: chameleon-webhooks
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/chameleon-co-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chameleon-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chameleon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.chameleon.io/introduction
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/chamaeleonidae
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chameleon-io
- group: company
  title: ''
  type: Blog
  url: https://www.chameleon.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chameleon.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chameleon.io/
- group: other
  title: ''
  type: X
  url: https://x.com/trychameleon
- group: commercial
  title: ''
  type: Plans
  url: plans/chameleon-co-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chameleon-co-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chameleon-co-finops.yml
created: 2026-06-13
description: Chameleon is an in-product guidance platform that enables product and growth teams to build, manage, and optimize onboarding tours, tooltips, modals, launchers, and microsurveys without engineering effort. Its REST API and JavaScript SDK allow teams to programmatically manage experiences, target users by segment, trigger tours from custom events, and retrieve engagement analytics and survey responses. Webhooks provide real-time event delivery when users interact with any Chameleon experience. The platform scales across Startup, Growth, and Enterprise plans based on Monthly Tracked Users (MTUs), with deep integrations for Segment, Amplitude, Mixpanel, and other product analytics tools.
finops:
- name: Chameleon Co Finops
  service_category: ''
  slug: chameleon-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chameleon-co.png
jsonld:
- class_count: 0
  name: Chameleon Co Context
  property_count: 29
  slug: chameleon-co-context
layout: provider
modified: 2026-06-13
name: Chameleon
nav: Providers
network: true
overview: 'Chameleon publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Product Tours, In-Product Guidance, User Onboarding, Tooltips, and Modals.


  The Chameleon catalog on APIs.io includes 1 JSON-LD context.


  Chameleon''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Chameleon Co Plans Pricing
  plan_count: 4
  slug: chameleon-co-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Chameleon Co Rate Limits
  slug: chameleon-co-rate-limits
score:
  band: thin
  composite: 29.9
  delta: -3.1
  facets:
    commercial_clarity: 57.9
    contract_quality: 12.9
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 33.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chameleon-co/refs/heads/main/screenshots/chameleon-co-2026-06-20T174211.png
security:
- kind: domain-security
  name: Chameleon Co Domain Security
  slug: chameleon-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Chameleon Co Trust Center
  slug: chameleon-co-trust-center
  summary_line: SOC 2, GDPR
slug: chameleon-co
tags:
- Product Tours
- In-Product Guidance
- User Onboarding
- Tooltips
- Modals
- Microsurveys
- Digital Adoption
- SaaS
- Product Analytics
- User Engagement
website: https://www.chameleon.io/
---

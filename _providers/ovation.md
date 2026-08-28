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
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Ovation Olo Webhooks
  slug: ovation-olo-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ovation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ovationup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ovationup.com/integrations/
- group: docs
  title: Onboarding & Integration Guide
  type: Documentation
  url: https://ovation.gitbook.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ovationup
- group: start
  title: ''
  type: SignUp
  url: https://ovationup.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://v2.ovationup.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://ovationup.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://ovationup.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://ovationup.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ovationup
- group: other
  title: ''
  type: X
  url: https://x.com/ovationup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ovationup.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ovationup.com/privacy-policy/
- group: auth
  title: SOC 2 Type 2 certification stated in the Data Processing Agreement
  type: Compliance
  url: https://ovationup.com/data-processing-agreement/
- group: design
  title: ''
  type: Conformance
  url: conformance/ovation-conformance.yml
- group: operate
  title: Seasonal product release notes
  type: ChangeLog
  url: changelog/ovation-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ovation-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ovation-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ovation-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/ovation-packages.yml
- group: design
  title: Olo webhook event catalog Ovation subscribes to
  type: Webhooks
  url: asyncapi/ovation-olo-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ovation-llms.txt
created: '2026-06-02'
description: 'Ovation is an AI-first guest experience and feedback platform for restaurants, founded by Zack Oates and voted the #1 guest feedback platform in a RestaurantOwner.com survey. It uses a frictionless, SMS-based two-question survey to capture real-time guest sentiment on- and off-premise, then applies AI to categorize feedback across 35+ restaurant-specific topics, surface operational insights, generate guest-recovery responses, manage online reviews, and run text marketing campaigns. Ovation connects to 50+ POS, online ordering, and loyalty systems, including Olo, to source guest interactions. These are pre-built partner integrations. Ovation does operate an API — its Summer 2025 release announced API User Management, "easily create, edit, and remove users via API", and the API host api.ovationup.com is live — but no public API reference, OpenAPI definition, developer portal, or SDK is published anywhere, and anonymous calls to that host are refused. Where integration is technical
  it is inbound and partner-driven: for example, Ovation receives Olo webhook events (OrderPlaced, OrderClosed, OrderCancelled, GuestOptIn, UserOptOut, and similar) authenticated with a shared secret, and the connection is configured directly through the partner''s customer success and developer teams rather than via a self-serve Ovation API. Integration access is arranged directly with the company.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ovation.png
layout: provider
modified: '2026-08-13'
name: Ovation
nav: Providers
network: true
overview: 'Ovation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, Guest Feedback, Guest Experience, Reputation Management, and SMS Marketing.


  The Ovation catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ovation''s developer surface includes documentation, signup flow, pricing, support, engineering blog, changelog, and 17 more developer resources.'
plans:
- name: Ovation Plans Pricing
  plan_count: 0
  slug: ovation-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Ovation Rate Limits
  slug: ovation-rate-limits
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 35.9
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ovation/refs/heads/main/screenshots/ovation-2026-06-20T191237.png
security:
- kind: domain-security
  name: Ovation Domain Security
  slug: ovation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ovation
tags:
- Restaurant
- Guest Feedback
- Guest Experience
- Reputation Management
- SMS Marketing
- Analytics
website: https://ovationup.com/
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 19.2
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: ActivityHero's provider integration surface — outbound, HMAC-SHA256-signed JSON webhooks that sync registrations and activity schedules between ActivityHero and a provider's own systems (configured un
  name: ActivityHero Registration & Schedule Webhooks
  slug: activityhero-registration-schedule-webhooks
artifact_total: 4
asyncapis:
- description: ''
  name: Activityhero Webhooks
  slug: activityhero-webhooks
common:
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/activityhero-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/activityhero-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/activityhero-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/activityhero-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/activityhero-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/activityhero-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.activityhero.com/api
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.activityhero.com
- group: company
  title: ''
  type: Blog
  url: https://www.activityhero.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://business.activityhero.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://activityhero.com/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://activityhero.com/pages/privacy
- group: company
  title: ''
  type: Website
  url: https://activityhero.com
created: '2026-07-17'
description: ActivityHero is an online marketplace connecting families with kids' camps, classes, and enrichment activities — a one-stop shop to find top-rated summer camps, holiday camps, and after-school classes near you across categories like art, science, sports, dance, and online programs. For activity providers it offers marketing and registration software (MarketingHero and custom registration software) plus programs for school districts. ActivityHero's developer surface is a provider integration built on outbound, HMAC-SHA256 signed JSON webhooks (a Registration API and a Schedule API) rather than a public REST API; it was surfaced as a portfolio company of 500 Global and enriched into the API Evangelist network from its published help-center docs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/activityhero.png
layout: provider
modified: '2026-07-17'
name: ActivityHero
nav: Providers
network: true
overview: 'ActivityHero publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Kids Activities, Camps, Classes, and Marketplace.


  The ActivityHero catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ActivityHero''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 27.5
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 22.6
    developer_ergonomics: 26.1
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/activityhero/refs/heads/main/screenshots/activityhero-2026-07-25T181531.png
security:
- kind: authentication
  name: Activityhero Authentication
  slug: activityhero-authentication
  summary_line: signature · 1 scheme
- kind: domain-security
  name: Activityhero Domain Security
  slug: activityhero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: activityhero
tags:
- Company
- Kids Activities
- Camps
- Classes
- Marketplace
- Registration
- Webhooks
- Education
website: https://activityhero.com
---

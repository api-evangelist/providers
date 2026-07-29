---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: RESTful API for the Wild Apricot small-association product, secured with OAuth 2.0 against base https://api.wildapricot.org (versioned paths such as /v2.2/accounts/{accountId}/...). Split into an admi
  name: Personify Wild Apricot API
  slug: personify-wild-apricot-api
- description: JSON REST API for the MemberClicks MC Professional AMS, secured with OAuth 2.0. Base URL is organization-scoped (https://{orgId}.memberclicks.net) with resource paths under /api/v1, including member p
  name: Personify MemberClicks (MC Professional) API
  slug: personify-memberclicks-api
- description: Proprietary Novus API integration layer for the enterprise Personify360 / ThreeSixty AMS, documented with a Swagger (OpenAPI) interface for reporting, large-scale operations, and custom applications o
  name: Personify360 Novus API
  slug: personify360-novus-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/personifycorp-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/personify-corp
- group: company
  title: ''
  type: Website
  url: https://personifycorp.com
- group: docs
  title: ''
  type: Documentation
  url: https://gethelp.wildapricot.com/en/articles/182-using-wildapricot-s-api
- group: commercial
  title: ''
  type: Plans
  url: plans/personifycorp-plans-pricing.yml
created: '2026-07-05'
description: Personify (Personify Inc., part of Momentive Software as of January 2026) is a constituent and association management software provider for associations, nonprofits, and member-based organizations. Founded in 1996 and headquartered in Austin, Texas, Personify offers a family of products - the enterprise Personify360 / ThreeSixty AMS, MemberClicks (MC Professional) for mid-sized professional and trade associations, Wild Apricot for small associations and clubs, and A2Z Events for event management. Several products expose documented REST APIs secured with OAuth 2.0. Wild Apricot and MemberClicks publish public developer documentation, while Personify360's Novus APIs (Swagger-documented) are provisioned through a customer's account manager. API access generally requires being a paying customer of the respective product.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/personifycorp.png
layout: provider
modified: '2026-07-05'
name: Personify
nav: Providers
network: true
overview: 'Personify publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Association Management, AMS, Membership, Nonprofit, and Events.


  Personify''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Personifycorp Plans Pricing
  plan_count: 0
  slug: personifycorp-plans-pricing
random_paper: 41
score:
  band: minimal
  composite: 9.2
  delta: -2.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Personifycorp Domain Security
  slug: personifycorp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: personifycorp
tags:
- Association Management
- AMS
- Membership
- Nonprofit
- Events
- Constituent Management
- CRM
website: https://personifycorp.com
---

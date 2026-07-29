---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
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
    asyncapi_events: false
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: Provision and manage employees in an Awardco instance. Awardco's public documentation names Create User, Import Users (bulk), and Reset User Password endpoints, all flagged as sensitive and permission
  name: Awardco Users API
  slug: awardco-users-api
- description: Programmatically recognize employees and issue recognition tied to an organization's programs and values. Awardco documents that API keys with the appropriate permission can recognize employees; the e
  name: Awardco Recognition API
  slug: awardco-recognition-api
- description: Award, adjust, and reconcile employee point balances that fund redemptions in Awardco's rewards marketplace (Amazon Business, gift cards, swag, and service awards). Awarding and adjusting points are d
  name: Awardco Points and Awards API
  slug: awardco-points-api
- description: Retrieve reporting data and program activity over REST. Awardco documents that reporting templates can be exported to CSV or scheduled to send via its REST API, and that API keys can retrieve reports.
  name: Awardco Reporting API
  slug: awardco-reporting-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/awardco-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/awardco
- group: company
  title: ''
  type: Website
  url: https://www.awardco.com
- group: docs
  title: ''
  type: Documentation
  url: https://code.awardco.com/api
- group: auth
  title: ''
  type: Authentication
  url: https://awardco.my.site.com/Customerhelp/s/article/Managing-API-Keys
- group: commercial
  title: ''
  type: Plans
  url: plans/awardco-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/awardco-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/awardco-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.awardco.com/blog
created: '2026-07-10'
description: Awardco is an all-in-one employee recognition, rewards, and engagement platform built around a global rewards marketplace that includes a native Amazon Business integration, gift cards, service awards, and swag. Awardco exposes a documented public REST API at https://api.awardco.com/api for administrators and integration partners - callers authenticate with a permission-scoped API key passed as a request header, all responses are JSON with a success flag, and all timestamps are ISO 8601. The API is not open self-serve - it is gated behind an Awardco account and the API Key Management permission, and partners additionally send an X-Partner-Id header. Documented capabilities cover user provisioning (create, import, reset password), recognizing employees and awarding points, and retrieving or scheduling reports. Awardco also ships prebuilt HRIS, SSO/SAML, Slack, and Microsoft Teams integrations plus Awardco Connect for custom flows. Exact request and response schemas for individual
  methods are not published on the open web, so the API surfaces below are modeled from Awardco's public documentation and help center rather than a released OpenAPI definition.
finops:
- name: Awardco Finops
  service_category: ''
  slug: awardco-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/awardco.png
layout: provider
modified: '2026-07-10'
name: Awardco
nav: Providers
network: true
overview: 'Awardco publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Employee Recognition, Rewards, Engagement, HR Tech, and Incentives.


  Awardco''s developer surface includes documentation, authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Awardco Plans Pricing
  plan_count: 6
  slug: awardco-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 0
  name: Awardco Rate Limits
  slug: awardco-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/awardco/refs/heads/main/screenshots/awardco-2026-07-25T202020.png
security:
- kind: domain-security
  name: Awardco Domain Security
  slug: awardco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: awardco
tags:
- Employee Recognition
- Rewards
- Engagement
- HR Tech
- Incentives
- Points
website: https://www.awardco.com
---

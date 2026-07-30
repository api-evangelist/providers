---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Facebook Lead Ads Agentic Access
  operation_count: 9
  slug: facebook-lead-ads-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 7
apis:
- description: Graph API endpoints for managing Facebook and Instagram lead generation forms, retrieving captured leads, exporting bulk lead data, and subscribing to leadgen webhooks. Authentication uses Page access
  name: Meta Marketing API - Lead Ads
  slug: graph-api
- description: The Bulk Leads API from Facebook Lead Ads — 1 operation(s) for bulk leads.
  name: Facebook Lead Ads Bulk Leads API
  slug: facebook-lead-ads-bulk-leads-api
- description: The Leadgen Forms API from Facebook Lead Ads — 1 operation(s) for leadgen forms.
  name: Facebook Lead Ads Leadgen Forms API
  slug: facebook-lead-ads-leadgen-forms-api
- description: The Leads API from Facebook Lead Ads — 2 operation(s) for leads.
  name: Facebook Lead Ads Leads API
  slug: facebook-lead-ads-leads-api
- description: The Meta Marketing API Lead Ads API from Facebook Lead Ads — 2 operation(s) for meta marketing api lead ads.
  name: Facebook Lead Ads Meta Marketing API Lead Ads API
  slug: facebook-lead-ads-meta-marketing-api-lead-ads-api
- description: The Subscribed Apps API from Facebook Lead Ads — 1 operation(s) for subscribed apps.
  name: Facebook Lead Ads Subscribed Apps API
  slug: facebook-lead-ads-subscribed-apps-api
- description: The Subscriptions API from Facebook Lead Ads — 1 operation(s) for subscriptions.
  name: Facebook Lead Ads Subscriptions API
  slug: facebook-lead-ads-subscriptions-api
artifact_total: 11
collections:
- collection_type: open
  name: Meta Marketing API - Lead Ads
  slug: open-facebook-lead-ads
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/facebook-lead-ads-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/facebook-lead-ads-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/facebook-lead-ads-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.facebook.com/business/ads/lead-ads
- group: docs
  title: ''
  type: Documentation
  url: https://developers.facebook.com/docs/marketing-api/guides/lead-ads/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.facebook.com
- group: other
  title: ''
  type: Marketing API
  url: https://developers.facebook.com/docs/marketing-api/
- group: start
  title: ''
  type: Signup
  url: https://developers.facebook.com/async/registration/
- group: other
  title: ''
  type: App Dashboard
  url: https://developers.facebook.com/apps/
- group: operate
  title: ''
  type: Support
  url: https://developers.facebook.com/support/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.facebook.com/llms.txt
created: '2026-05-11'
description: Facebook Lead Ads (part of the Meta Marketing API) lets advertisers create instant lead-generation forms on Facebook and Instagram and programmatically retrieve the leads captured through those forms. Through the Meta Graph API developers can list lead generation forms on a Page, read submitted leads, download bulk lead exports, and subscribe to webhooks for real-time lead delivery. Authentication uses Page access tokens issued via Facebook Login / Meta Business Login with the leads_retrieval, pages_show_list, and pages_manage_ads permissions.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/facebook-lead-ads.png
layout: provider
modified: '2026-05-11'
name: Facebook Lead Ads
nav: Providers
network: true
overview: 'Facebook Lead Ads publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bulk Leads API, Leadgen Forms API, Leads API, and 3 more. Tagged areas include Advertising, Lead Generation, Lead Ads, Marketing API, and Facebook.


  Facebook Lead Ads'' developer surface includes authentication, documentation, signup flow, support, and 7 more developer resources.'
random_paper: 76
scopes:
- name: Facebook Lead Ads Scopes
  scope_count: 3
  slug: facebook-lead-ads-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: emerging
  composite: 27.3
  delta: -2.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 53.4
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/facebook-lead-ads/refs/heads/main/screenshots/facebook-lead-ads-2026-06-20T181004.png
security:
- kind: authentication
  name: Facebook Lead Ads Authentication
  slug: facebook-lead-ads-authentication
  summary_line: oauth2 · 1 scheme
slug: facebook-lead-ads
tags:
- Advertising
- Lead Generation
- Lead Ads
- Marketing API
- Facebook
- Instagram
- Meta
- Webhooks
website: https://www.facebook.com/business/ads/lead-ads
---

---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Clevertap Agentic Access
  operation_count: 10
  slug: clevertap-agentic-access
  summary_line: 10 operations · 8 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: Upload, retrieve, update, and delete user profiles in CleverTap with identity, demographic, and custom property data.
  name: CleverTap Profile API
  slug: profile-api
- description: Record user events with arbitrary properties for behavioral segmentation, funnels, and triggered messaging.
  name: CleverTap Event API
  slug: event-api
- description: Programmatically create and manage push, email, SMS, web, and in-app campaigns and retrieve message status reports.
  name: CleverTap Campaign API
  slug: campaign-api
- description: Raise a Bulletin in CleverTap when a business event is triggered, used to drive real-time campaign delivery from external systems.
  name: CleverTap Bulletins API
  slug: bulletins-api
- description: Manage product catalog data feeding personalization, recommendations, and product-aware messaging.
  name: CleverTap Catalog API
  slug: catalog-api
- description: Create and update custom lists used as audience segments in campaigns and journeys.
  name: CleverTap Custom List API
  slug: custom-list-api
- description: Manage feature flags and remote configuration variables delivered to mobile apps and websites.
  name: CleverTap Remote Config API
  slug: remote-config-api
- description: Query real-time counts and trends of events, profiles, and segments.
  name: CleverTap Real-Time Counts API
  slug: counts-api
- description: The Campaigns API from CleverTap — 3 operation(s) for campaigns.
  name: CleverTap Campaigns API
  slug: clevertap-campaigns-api
- description: The Events API from CleverTap — 2 operation(s) for events.
  name: CleverTap Events API
  slug: clevertap-events-api
- description: The Profiles API from CleverTap — 4 operation(s) for profiles.
  name: CleverTap Profiles API
  slug: clevertap-profiles-api
- description: The Reports API from CleverTap — 2 operation(s) for reports.
  name: CleverTap Reports API
  slug: clevertap-reports-api
artifact_total: 22
collections:
- collection_type: open
  name: CleverTap REST API
  slug: open-clevertap
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clevertap-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clevertap-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clevertap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clevertap-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CleverTap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clevertap
- group: company
  title: ''
  type: Website
  url: https://clevertap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clevertap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clevertap.com/docs
- group: auth
  title: ''
  type: Authentication
  url: https://developer.clevertap.com/docs/api-authentication
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clevertap.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://clevertap.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clevertap.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clevertap.com/terms-of-service/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clevertap-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clevertap-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.clevertap.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://clevertap.com/blog
created: '2024-11-14'
description: CleverTap is a customer engagement and retention platform that helps businesses understand user behavior, segment audiences, and deliver personalized experiences across mobile push, email, SMS, in-app, web push, and WhatsApp channels. CleverTap exposes a comprehensive REST API surface covering profiles, events, campaigns, real-time analytics, catalogs, feature flags, and more, authenticated via account ID and passcode headers.
finops:
- name: Clevertap Finops
  service_category: API
  slug: clevertap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clevertap.png
jsonld:
- class_count: 0
  name: Clevertap Context
  property_count: 6
  slug: clevertap-context
layout: provider
modified: '2026-04-26'
name: CleverTap
nav: Providers
network: true
overview: 'CleverTap publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Events API, Profiles API, and 1 more. Tagged areas include Audiences, Customer Engagement, Customer Retention, Marketing Automation, and Mobile Engagement.


  The CleverTap catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CleverTap''s developer surface includes authentication, documentation, pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Clevertap Plans Pricing
  plan_count: 3
  slug: clevertap-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Clevertap Rate Limits
  slug: clevertap-rate-limits
rules:
- name: CleverTap API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: clevertap-rules
score:
  band: developing
  composite: 53.2
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 62.0
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clevertap/refs/heads/main/screenshots/clevertap-2026-06-20T174517.png
security:
- kind: authentication
  name: Clevertap Authentication
  slug: clevertap-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Clevertap Domain Security
  slug: clevertap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clevertap Trust Center
  slug: clevertap-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, CSA STAR
slug: clevertap
tags:
- Audiences
- Customer Engagement
- Customer Retention
- Marketing Automation
- Mobile Engagement
- Push Notifications
- User Behavior
website: https://clevertap.com/
---

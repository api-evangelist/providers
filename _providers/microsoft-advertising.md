---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  score: 28.4
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: The Microsoft Advertising Campaign Management API enables programmatic management of advertising campaigns, ad groups, ads, keywords, and targeting. Developers can create and modify campaign structure
  name: Microsoft Advertising Campaign Management API
  slug: campaign-management-api
- description: The Microsoft Advertising Reporting API provides access to performance reports for campaigns, ad groups, ads, and keywords. Developers can request reports on impressions, clicks, conversions, spend, a
  name: Microsoft Advertising Reporting API
  slug: reporting-api
- description: The Microsoft Advertising Bulk API enables efficient management of large-scale advertising campaigns through batch upload and download operations. It supports CSV-based bulk operations for creating, u
  name: Microsoft Advertising Bulk API
  slug: bulk-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-advertising-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-advertising-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bingads
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-advertising
- group: start
  title: ''
  type: Portal
  url: https://ads.microsoft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/advertising/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/advertising/guides/client-libraries
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/advertising/guides/authentication-oauth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://about.ads.microsoft.com/en-us/blog/rss
created: '2024-01-15'
description: Microsoft Advertising provides APIs for managing ad campaigns, reporting on performance, and bulk operations across the Microsoft Advertising network including Bing, MSN, and partner sites. The platform offers programmatic access to campaign management, reporting, and bulk operations services for advertisers and developers.
finops:
- name: Microsoft Advertising Finops
  service_category: API
  slug: microsoft-advertising-finops
graphqls:
- description: Microsoft Advertising (Bing Ads) API covers campaign management, ad groups, keywords, audiences, bid strategies, extensions, reporting, and bulk operations for search and audience advertising.
  name: Microsoft Advertising GraphQL API
  slug: microsoft-advertising-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-advertising.png
layout: provider
modified: '2026-04-28'
name: Microsoft Advertising
nav: Providers
network: true
overview: 'Microsoft Advertising publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Analytics, Bing Ads, Bulk Operations, and Campaigns.


  Microsoft Advertising''s developer surface includes developer portal, authentication, support, engineering blog, and 8 more developer resources.'
plans:
- name: Microsoft Advertising Plans Pricing
  plan_count: 3
  slug: microsoft-advertising-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Microsoft Advertising Rate Limits
  slug: microsoft-advertising-rate-limits
score:
  band: thin
  composite: 33.8
  delta: -7.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 43.2
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 41.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-advertising/refs/heads/main/screenshots/microsoft-advertising-2026-06-20T185348.png
security:
- kind: domain-security
  name: Microsoft Advertising Domain Security
  slug: microsoft-advertising-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Advertising Vulnerability Disclosure
  slug: microsoft-advertising-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-advertising
tags:
- Advertising
- Analytics
- Bing Ads
- Bulk Operations
- Campaigns
- Microsoft
- Reporting
website: https://learn.microsoft.com/en-us/advertising/
---

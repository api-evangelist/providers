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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Umami Agentic Access
  operation_count: 23
  slug: umami-agentic-access
  summary_line: 23 operations · 10 acting
api_count: 7
apis:
- description: Login and token verification
  name: Umami Authentication API
  slug: umami-authentication-api
- description: Custom event tracking
  name: Umami Events API
  slug: umami-events-api
- description: Visitor session data
  name: Umami Sessions API
  slug: umami-sessions-api
- description: Team and access management
  name: Umami Teams API
  slug: umami-teams-api
- description: User account management
  name: Umami Users API
  slug: umami-users-api
- description: Analytics metrics, pageviews, and statistics
  name: Umami Website Statistics API
  slug: umami-website-statistics-api
- description: Website management and configuration
  name: Umami Websites API
  slug: umami-websites-api
artifact_total: 102
collections:
- collection_type: postman
  name: Umami Analytics Authentication API
  slug: postman-umami-authentication-api
- collection_type: postman
  name: Umami Analytics Authentication Events API
  slug: postman-umami-events-api
- collection_type: postman
  name: Umami Analytics Authentication Sessions API
  slug: postman-umami-sessions-api
- collection_type: postman
  name: Umami Analytics Authentication Teams API
  slug: postman-umami-teams-api
- collection_type: postman
  name: Umami Analytics Authentication Users API
  slug: postman-umami-users-api
- collection_type: postman
  name: Umami Analytics Authentication Website Statistics API
  slug: postman-umami-website-statistics-api
- collection_type: postman
  name: Umami Analytics Authentication Websites API
  slug: postman-umami-websites-api
- collection_type: open
  name: Umami Analytics API
  slug: open-umami
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/umami/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/umami-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/umami-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/umami-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/umami-software
- group: company
  title: ''
  type: Website
  url: https://umami.is
- group: docs
  title: ''
  type: Documentation
  url: https://umami.is/docs
- group: company
  title: ''
  type: Blog
  url: https://umami.is/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://umami.is/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/umami-software/umami
- group: start
  title: ''
  type: Login
  url: https://cloud.umami.is
- group: start
  title: ''
  type: Signup
  url: https://cloud.umami.is
- group: other
  title: ''
  type: SelfHosting
  url: https://umami.is/docs/install
- group: operate
  title: ''
  type: Support
  url: https://umami.is/docs/support
- group: design
  title: ''
  type: SpectralRules
  url: rules/umami-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/umami-vocabulary.yaml
created: '2026-03-26'
description: Umami is an open source, privacy-first web analytics platform that provides website traffic insights without cookies or personal data collection, serving as a simple and fast alternative to Google Analytics. The Umami API provides full programmatic access to analytics data, website management, session tracking, event data, and team collaboration features for both self-hosted and cloud instances.
examples:
- key_count: 1
  name: Umami Active Visitors Example
  slug: umami-active-visitors-example
- key_count: 2
  name: Umami Login Request Example
  slug: umami-login-request-example
- key_count: 2
  name: Umami Login Response Example
  slug: umami-login-response-example
- key_count: 2
  name: Umami Metric Example
  slug: umami-metric-example
- key_count: 1
  name: Umami Ok Response Example
  slug: umami-ok-response-example
- key_count: 2
  name: Umami Pageview Data Example
  slug: umami-pageview-data-example
- key_count: 9
  name: Umami Session Example
  slug: umami-session-example
- key_count: 4
  name: Umami Session List Example
  slug: umami-session-list-example
- key_count: 5
  name: Umami Session Stats Example
  slug: umami-session-stats-example
- key_count: 8
  name: Umami Team Example
  slug: umami-team-example
- key_count: 4
  name: Umami Team List Example
  slug: umami-team-list-example
- key_count: 6
  name: Umami Team Member Example
  slug: umami-team-member-example
- key_count: 2
  name: Umami Team Request Example
  slug: umami-team-request-example
- key_count: 6
  name: Umami User Example
  slug: umami-user-example
- key_count: 3
  name: Umami User Request Example
  slug: umami-user-request-example
- key_count: 10
  name: Umami Website Example
  slug: umami-website-example
- key_count: 4
  name: Umami Website List Example
  slug: umami-website-list-example
- key_count: 4
  name: Umami Website Request Example
  slug: umami-website-request-example
- key_count: 5
  name: Umami Website Stats Example
  slug: umami-website-stats-example
features:
- description: Tracks website traffic without cookies or personal data, fully GDPR compliant without consent banners.
  name: Privacy-First Analytics
- description: Live visitor counts and real-time pageview tracking for immediate traffic insights.
  name: Real-Time Data
- description: Track custom user interactions and conversions with a simple JavaScript API.
  name: Custom Events
- description: Share analytics access across teams with role-based access control.
  name: Team Collaboration
- description: Deploy on your own infrastructure for complete data ownership and control.
  name: Self-Hosting Support
- description: MIT-licensed open source software with active community development and full transparency.
  name: Open Source
- description: Manage and analyze multiple websites from a single Umami instance.
  name: Multi-Site Support
- description: Full REST API for programmatic access to all analytics data and management functions.
  name: API Access
finops:
- name: Umami Finops
  service_category: API
  slug: umami-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/umami.png
integrations:
- description: First-class integration with Next.js via the @umami/nextjs package for page view tracking.
  name: Next.js
- description: Track WordPress sites by adding the Umami tracking script via plugin or manual installation.
  name: WordPress
- description: Deploy Umami on Vercel with a one-click deployment for managed self-hosting.
  name: Vercel
- description: Run Umami in any environment using the official Docker container image.
  name: Docker
- description: Deploy tracking scripts behind Cloudflare for performance and abuse prevention.
  name: Cloudflare
json_schemas:
- name: ActiveVisitors
  property_count: 1
  slug: umami-active-visitors
- name: LoginRequest
  property_count: 2
  slug: umami-login-request
- name: LoginResponse
  property_count: 2
  slug: umami-login-response
- name: Metric
  property_count: 2
  slug: umami-metric
- name: OkResponse
  property_count: 1
  slug: umami-ok-response
- name: PageviewData
  property_count: 2
  slug: umami-pageview-data
- name: SessionList
  property_count: 4
  slug: umami-session-list
- name: Session
  property_count: 9
  slug: umami-session
- name: SessionStats
  property_count: 5
  slug: umami-session-stats
- name: TeamList
  property_count: 4
  slug: umami-team-list
- name: TeamMember
  property_count: 6
  slug: umami-team-member
- name: TeamRequest
  property_count: 2
  slug: umami-team-request
- name: Team
  property_count: 8
  slug: umami-team
- name: UserRequest
  property_count: 3
  slug: umami-user-request
- name: User
  property_count: 6
  slug: umami-user
- name: WebsiteList
  property_count: 4
  slug: umami-website-list
- name: WebsiteRequest
  property_count: 4
  slug: umami-website-request
- name: Website
  property_count: 10
  slug: umami-website
- name: WebsiteStats
  property_count: 5
  slug: umami-website-stats
json_structures:
- name: Umami Active Visitors Structure
  property_count: 1
  slug: umami-active-visitors-structure
- name: Umami Login Request Structure
  property_count: 2
  slug: umami-login-request-structure
- name: Umami Login Response Structure
  property_count: 2
  slug: umami-login-response-structure
- name: Umami Metric Structure
  property_count: 2
  slug: umami-metric-structure
- name: Umami Ok Response Structure
  property_count: 1
  slug: umami-ok-response-structure
- name: Umami Pageview Data Structure
  property_count: 2
  slug: umami-pageview-data-structure
- name: Umami Session List Structure
  property_count: 4
  slug: umami-session-list-structure
- name: Umami Session Stats Structure
  property_count: 5
  slug: umami-session-stats-structure
- name: Umami Session Structure
  property_count: 9
  slug: umami-session-structure
- name: Umami Team List Structure
  property_count: 4
  slug: umami-team-list-structure
- name: Umami Team Member Structure
  property_count: 6
  slug: umami-team-member-structure
- name: Umami Team Request Structure
  property_count: 2
  slug: umami-team-request-structure
- name: Umami Team Structure
  property_count: 8
  slug: umami-team-structure
- name: Umami User Request Structure
  property_count: 3
  slug: umami-user-request-structure
- name: Umami User Structure
  property_count: 6
  slug: umami-user-structure
- name: Umami Website List Structure
  property_count: 4
  slug: umami-website-list-structure
- name: Umami Website Request Structure
  property_count: 4
  slug: umami-website-request-structure
- name: Umami Website Stats Structure
  property_count: 5
  slug: umami-website-stats-structure
- name: Umami Website Structure
  property_count: 10
  slug: umami-website-structure
jsonld:
- class_count: 0
  name: Umami Context
  property_count: 0
  slug: umami-context
layout: provider
modified: '2026-05-19'
name: Umami
nav: Providers
network: true
overview: 'Umami publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Events API, Sessions API, and 4 more. Tagged areas include Cookieless Tracking, Open Source, Privacy, Web Analytics, and Website Analytics.


  The Umami catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Umami''s developer surface includes authentication, documentation, engineering blog, pricing, GitHub presence, signup flow, support, and 9 more developer resources.'
plans:
- name: Umami Plans Pricing
  plan_count: 3
  slug: umami-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Umami Rate Limits
  slug: umami-rate-limits
rules:
- name: Umami API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: umami-jsonschema-spectral-rules
- name: Umami API Rules
  rule_count: 37
  severity_counts:
    error: 13
    hint: 0
    info: 9
    warn: 15
  slug: umami-spectral-rules
score:
  band: developing
  composite: 46.1
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 27.7
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/umami/refs/heads/main/screenshots/umami-2026-06-20T200011.png
security:
- kind: authentication
  name: Umami Authentication
  slug: umami-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Umami Domain Security
  slug: umami-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: umami
solutions:
- description: Hosted Umami instance at cloud.umami.is with managed infrastructure and API key authentication.
  name: Umami Cloud
- description: Run your own Umami instance on any infrastructure with full data ownership and JWT authentication.
  name: Umami Self-Hosted
tags:
- Cookieless Tracking
- Open Source
- Privacy
- Web Analytics
- Website Analytics
use_cases:
- description: Track pageviews, unique visitors, bounce rates, and session duration for website optimization.
  name: Website Performance Monitoring
- description: Replace Google Analytics with a cookieless solution that requires no consent banners under GDPR.
  name: Privacy-Compliant Analytics
- description: Analyze traffic sources, referrers, and UTM campaign data to measure marketing effectiveness.
  name: Marketing Analytics
- description: Track button clicks, form submissions, and custom conversions using the Umami event API.
  name: Custom Event Tracking
- description: Build custom analytics dashboards using the REST API to display site metrics in your own apps.
  name: Developer Dashboards
- description: Provide analytics access to multiple clients or teams with shared infrastructure and access controls.
  name: Multi-Tenant Analytics
website: https://umami.is
---

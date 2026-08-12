---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Swetrix Agentic Access
  operation_count: 49
  slug: swetrix-agentic-access
  summary_line: 49 operations · 25 acting
api_count: 13
apis:
- description: The Swetrix Events API provides endpoints for recording pageview events, custom events, heartbeat events, error events, and revenue transactions. Used for sending analytics data from client or server-
  name: Swetrix Events API
  slug: swetrix-events-api
- description: Manage chart annotations
  name: Swetrix Annotations API
  slug: swetrix-annotations-api
- description: Custom event analytics
  name: Swetrix Custom Events API
  slug: swetrix-custom-events-api
- description: Record JavaScript error events
  name: Swetrix Errors API
  slug: swetrix-errors-api
- description: Feature flag evaluation statistics
  name: Swetrix Feature Flags API
  slug: swetrix-feature-flags-api
- description: Manage conversion funnels
  name: Swetrix Funnels API
  slug: swetrix-funnels-api
- description: Manage organisations and member access
  name: Swetrix Organisations API
  slug: swetrix-organisations-api
- description: Frontend and backend performance metrics
  name: Swetrix Performance API
  slug: swetrix-performance-api
- description: Manage analytics projects
  name: Swetrix Projects API
  slug: swetrix-projects-api
- description: Record revenue transactions (server-side only, requires API key)
  name: Swetrix Revenue API
  slug: swetrix-revenue-api
- description: Individual visitor session data
  name: Swetrix Sessions API
  slug: swetrix-sessions-api
- description: Aggregated traffic and pageview analytics
  name: Swetrix Traffic API
  slug: swetrix-traffic-api
- description: Manage saved dashboard views (segments)
  name: Swetrix Views API
  slug: swetrix-views-api
artifact_total: 44
collections:
- collection_type: postman
  name: Swetrix Admin Annotations API
  slug: postman-swetrix-annotations-api
- collection_type: postman
  name: Swetrix Admin Annotations Custom Events API
  slug: postman-swetrix-custom-events-api
- collection_type: postman
  name: Swetrix Admin Annotations Errors API
  slug: postman-swetrix-errors-api
- collection_type: postman
  name: Swetrix Admin Annotations Feature Flags API
  slug: postman-swetrix-feature-flags-api
- collection_type: postman
  name: Swetrix Admin Annotations Funnels API
  slug: postman-swetrix-funnels-api
- collection_type: postman
  name: Swetrix Admin Annotations Organisations API
  slug: postman-swetrix-organisations-api
- collection_type: postman
  name: Swetrix Admin Annotations Performance API
  slug: postman-swetrix-performance-api
- collection_type: postman
  name: Swetrix Admin Annotations Projects API
  slug: postman-swetrix-projects-api
- collection_type: postman
  name: Swetrix Admin Annotations Revenue API
  slug: postman-swetrix-revenue-api
- collection_type: postman
  name: Swetrix Admin Annotations Sessions API
  slug: postman-swetrix-sessions-api
- collection_type: postman
  name: Swetrix Admin Annotations Traffic API
  slug: postman-swetrix-traffic-api
- collection_type: postman
  name: Swetrix Admin Annotations Views API
  slug: postman-swetrix-views-api
- collection_type: open
  name: Swetrix Admin API
  slug: open-swetrix-admin-api
- collection_type: open
  name: Swetrix Events API
  slug: open-swetrix-events-api
- collection_type: open
  name: Swetrix Statistics API
  slug: open-swetrix-statistics-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/swetrix/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swetrix-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/swetrix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swetrix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swetrix-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swetrix
- group: company
  title: ''
  type: Website
  url: https://swetrix.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.swetrix.com
- group: company
  title: ''
  type: Blog
  url: https://swetrix.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://swetrix.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Swetrix/swetrix
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Swetrix
- group: start
  title: ''
  type: Login
  url: https://swetrix.com/login
- group: start
  title: ''
  type: Signup
  url: https://swetrix.com/signup
- group: operate
  title: ''
  type: Support
  url: https://swetrix.com/contact
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/Swetrix/swetrix-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Swetrix/swetrix-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Swetrix/swetrix-nextjs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Swetrix/swetrix-browser
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Swetrix/django-plugin
- group: operate
  title: ''
  type: StatusPage
  url: https://swetrix.com/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://swetrix.com/privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://swetrix.com/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://swetrix.com/llms.txt
created: '2026-03-26'
description: Swetrix is an open source, privacy-focused web analytics platform that provides cookieless tracking, real-time dashboards, and GDPR-compliant analytics without collecting personal data. It offers a fully-featured REST API for tracking events, querying statistics, managing projects, and integrating analytics into custom applications.
examples:
- key_count: 4
  name: Swetrix Create Project Example
  slug: swetrix-create-project-example
- key_count: 4
  name: Swetrix Get Traffic Log Example
  slug: swetrix-get-traffic-log-example
- key_count: 4
  name: Swetrix Record Pageview Example
  slug: swetrix-record-pageview-example
finops:
- name: Swetrix Finops
  service_category: Web Analytics
  slug: swetrix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swetrix.png
json_schemas:
- name: Swetrix Project
  property_count: 12
  slug: swetrix-project
- name: Swetrix Session
  property_count: 16
  slug: swetrix-session
json_structures:
- name: Swetrix Project Structure
  property_count: 0
  slug: swetrix-project-structure
jsonld:
- class_count: 30
  name: Swetrix Context
  property_count: 6
  slug: swetrix-context
layout: provider
modified: '2026-05-19'
name: Swetrix
nav: Providers
network: true
overview: 'Swetrix publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Events API, Annotations API, Custom Events API, and 10 more. Tagged areas include Analytics, Cookieless Tracking, GDPR Compliant, Open Source, and Privacy.


  The Swetrix catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Swetrix''s developer surface includes authentication, documentation, engineering blog, pricing, GitHub presence, signup flow, support, and 17 more developer resources.'
plans:
- name: Swetrix Plans Pricing
  plan_count: 10
  slug: swetrix-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 1
  name: Swetrix Rate Limits
  slug: swetrix-rate-limits
rules:
- name: Swetrix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: swetrix-jsonschema-spectral-rules
- name: Swetrix API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 6
  slug: swetrix-rules
score:
  band: strong
  composite: 57.1
  delta: -6.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 69.3
    developer_ergonomics: 45.7
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/swetrix/refs/heads/main/screenshots/swetrix-2026-06-20T194812.png
security:
- kind: authentication
  name: Swetrix Authentication
  slug: swetrix-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Swetrix Domain Security
  slug: swetrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Swetrix Vulnerability Disclosure
  slug: swetrix-vulnerability-disclosure
  summary_line: disclosure policy published
slug: swetrix
tags:
- Analytics
- Cookieless Tracking
- GDPR Compliant
- Open Source
- Privacy
- Real-Time Analytics
- Web Analytics
website: https://swetrix.com
---

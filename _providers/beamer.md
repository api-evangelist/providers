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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'The Beamer REST API provides programmatic access to changelog posts, user management, segmentation, and notification feeds. Key endpoints include unread count retrieval, post creation and management, '
  name: Beamer API
  slug: beamer
artifact_total: 21
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/beamer-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beamer-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.getbeamer.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getbeamer
- group: company
  title: ''
  type: Website
  url: https://www.getbeamer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.getbeamer.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.getbeamer.com/help/how-to-install-beamer-using-our-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getbeamer.com
created: '2026-03-29'
description: Beamer is a changelog and notification center tool for announcing product updates, new features, and API changes to end users. It provides an embeddable feed widget, push notifications, email digests, and a public changelog page. The Beamer REST API enables programmatic management of posts, users, segments, and notification delivery. Beamer is now part of the Userflow product suite. The API uses API key authentication and supports OpenAPI specifications and Postman collections.
features:
- description: Embeddable changelog widget that displays product updates to users within your application.
  name: Changelog Feed Widget
- description: In-app push notifications to alert users about new features and product updates.
  name: Push Notifications
- description: Automated email digest delivery of changelog posts to user segments.
  name: Email Digests
- description: Target changelog announcements and notifications to specific user segments based on attributes.
  name: User Segmentation
- description: REST API endpoint to retrieve unread notification count for individual users.
  name: Unread Count API
- description: Hosted public changelog page for external users, prospects, and documentation.
  name: Public Changelog
finops:
- name: Beamer Finops
  service_category: API
  slug: beamer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beamer.png
integrations:
- description: Automation integration connecting Beamer with thousands of apps via Zapier workflows.
  name: Zapier
- description: Customer data platform integration for sending Beamer user events and changelog views to Segment.
  name: Segment
- description: Customer messaging platform integration enabling Beamer notifications alongside Intercom conversations.
  name: Intercom
- description: Email marketing integration for delivering Beamer changelog digests through ActiveCampaign.
  name: ActiveCampaign
- description: WordPress plugin for embedding Beamer changelog feed in WordPress websites.
  name: WordPress
layout: provider
modified: '2026-04-19'
name: Beamer
nav: Providers
network: true
overview: 'Beamer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Changelog, Deprecation, Notifications, Product Updates, and User Engagement.


  Beamer''s developer surface includes engineering blog, documentation, getting-started guide, and 5 more developer resources.'
plans:
- name: Beamer Plans Pricing
  plan_count: 3
  slug: beamer-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 5
  name: Beamer Rate Limits
  slug: beamer-rate-limits
score:
  band: emerging
  composite: 18.5
  delta: 0.4
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 18.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/screenshots/beamer-2026-06-20T173106.png
security:
- kind: domain-security
  name: Beamer Domain Security
  slug: beamer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Beamer Trust Center
  slug: beamer-trust-center
  summary_line: SOC 2, GDPR
slug: beamer
tags:
- Changelog
- Deprecation
- Notifications
- Product Updates
- User Engagement
use_cases:
- description: Announce new product features, improvements, and bug fixes to end users via in-app notifications.
  name: Product Update Announcements
- description: Maintain a dedicated API changelog for developers tracking breaking changes, deprecations, and new endpoints.
  name: API Changelog
- description: Surface new features to relevant users through targeted notifications and changelog posts.
  name: User Onboarding
- description: Automate release note publishing from CI/CD pipelines using the Beamer API.
  name: Release Notes Automation
website: https://www.getbeamer.com/
---

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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: 'The Beamer REST API provides programmatic access to changelog posts, user management, segmentation, and notification feeds. Key endpoints include unread count retrieval, post creation and management, '
  name: Beamer API
  slug: beamer
artifact_total: 24
asyncapis:
- description: ''
  name: Beamer Webhooks
  slug: beamer-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/security/beamer-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/beamer-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/security/beamer-domain-security.yml
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
  url: https://help.userflow.com/beamer/docs/how-to-install-beamer-using-our-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getbeamer.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.userflow.com/beamer/docs/developer-documentation
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.userflow.com/beamer
- group: operate
  title: ''
  type: Support
  url: https://www.getbeamer.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getbeamer.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getbeamer.com/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getbeamer.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getbeamer.com/privacy-policy
- group: operate
  title: Beamer's own public roadmap, run on Beamer
  type: Roadmap
  url: https://app.getbeamer.com/beamer/roadmap/en
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/changelog/beamer-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/beamer-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/packages/beamer-packages.yml
  title: ''
  type: Packages
  url: packages/beamer-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/components/beamer-components.yml
  title: ''
  type: Components
  url: components/beamer-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/llms/beamer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beamer-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/conformance/beamer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beamer-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/conformance/beamer-conformance.yml
  title: SOC 2 and GDPR, published on getbeamer.com/security and the trust center
  type: Compliance
  url: conformance/beamer-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/security/beamer-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/beamer-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/security/beamer-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/beamer-vulnerability-disclosure.yml
created: '2026-03-29'
description: Beamer is a changelog and notification center tool for announcing product updates, new features, and API changes to end users. It provides an embeddable feed widget, push notifications, email digests, and a public changelog page. The Beamer REST API enables programmatic management of posts, users, segments, and notification delivery. Beamer and Userflow now operate as one company, and Beamer's knowledge base has moved to help.userflow.com/beamer. The REST API is versioned at https://api.getbeamer.com/v0, documents 49 operations across posts, comments, reactions, feature requests, users, NPS, team and GDPR erasure, and authenticates with a single account-scoped API key sent in the Beamer-Api-Key header. Four webhook event types are published. No OpenAPI document, Postman collection or MCP server is served on any Beamer host.
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
modified: '2026-09-14'
name: Beamer
nav: Providers
network: true
overview: 'Beamer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Changelog, Deprecation, Notification, Product Updates, and User Engagement.


  The Beamer catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Beamer''s developer surface includes engineering blog, documentation, getting-started guide, support, pricing, signup flow, changelog, and 17 more developer resources.'
plans:
- name: Beamer Plans Pricing
  plan_count: 5
  slug: beamer-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 6
  name: Beamer Rate Limits
  slug: beamer-rate-limits
score:
  band: strong
  composite: 60.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 75.9
    operational_transparency: 86.8
  previous_composite: 60.7
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/beamer/refs/heads/main/screenshots/beamer-2026-06-20T173106.png
security:
- kind: authentication
  name: Beamer Authentication
  slug: beamer-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Beamer Domain Security
  slug: beamer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Beamer Vulnerability Disclosure
  slug: beamer-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Beamer Trust Center
  slug: beamer-trust-center
  summary_line: SOC 2, GDPR
slug: beamer
tags:
- Changelog
- Deprecation
- Notification
- Product Updates
- User Engagement
- Webhook
- NPS
- Feedback
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

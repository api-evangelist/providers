---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    agentic_access: derived
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 80
  human_in_the_loop: 0
  name: Magicbell Agentic Access
  operation_count: 126
  slug: magicbell-agentic-access
  summary_line: 126 operations · 80 acting
api_count: 28
apis:
- description: The legacy MagicBell REST API (v1) for notification delivery, user management, and channel configuration. Supports API key and user external ID based authentication. Rate limits are lower than v2 (100
  name: MagicBell REST API v1
  slug: rest-api-v1
- description: The apns API from MagicBell — 6 operation(s) for apns.
  name: MagicBell apns API
  slug: magicbell-apns-api
- description: The awssns API from MagicBell — 3 operation(s) for awssns.
  name: MagicBell awssns API
  slug: magicbell-awssns-api
- description: The broadcasts API from MagicBell — 2 operation(s) for broadcasts.
  name: MagicBell broadcasts API
  slug: magicbell-broadcasts-api
- description: The channel/email API from MagicBell — 8 operation(s) for channel/email.
  name: MagicBell channel/email API
  slug: magicbell-channel-email-api
- description: The channel/mobile_push API from MagicBell — 6 operation(s) for channel/mobile_push.
  name: MagicBell channel/mobile_push API
  slug: magicbell-channel-mobile-push-api
- description: The channel/slack API from MagicBell — 2 operation(s) for channel/slack.
  name: MagicBell channel/slack API
  slug: magicbell-channel-slack-api
- description: The channel/sms API from MagicBell — 2 operation(s) for channel/sms.
  name: MagicBell channel/sms API
  slug: magicbell-channel-sms-api
- description: The channel/web_push API from MagicBell — 2 operation(s) for channel/web_push.
  name: MagicBell channel/web_push API
  slug: magicbell-channel-web-push-api
- description: The channels API from MagicBell — 25 operation(s) for channels.
  name: MagicBell channels API
  slug: magicbell-channels-api
- description: The expo API from MagicBell — 6 operation(s) for expo.
  name: MagicBell expo API
  slug: magicbell-expo-api
- description: The fcm API from MagicBell — 6 operation(s) for fcm.
  name: MagicBell fcm API
  slug: magicbell-fcm-api
- description: The github API from MagicBell — 3 operation(s) for github.
  name: MagicBell github API
  slug: magicbell-github-api
- description: The inbox API from MagicBell — 4 operation(s) for inbox.
  name: MagicBell inbox API
  slug: magicbell-inbox-api
- description: The integrations API from MagicBell — 42 operation(s) for integrations.
  name: MagicBell integrations API
  slug: magicbell-integrations-api
- description: The mailgun API from MagicBell — 2 operation(s) for mailgun.
  name: MagicBell mailgun API
  slug: magicbell-mailgun-api
- description: The mobile_push API from MagicBell — 12 operation(s) for mobile_push.
  name: MagicBell mobile_push API
  slug: magicbell-mobile-push-api
- description: The ping_email API from MagicBell — 2 operation(s) for ping_email.
  name: MagicBell ping_email API
  slug: magicbell-ping-email-api
- description: The project API from MagicBell — 52 operation(s) for project.
  name: MagicBell project API
  slug: magicbell-project-api
- description: The sendgrid API from MagicBell — 2 operation(s) for sendgrid.
  name: MagicBell sendgrid API
  slug: magicbell-sendgrid-api
- description: The ses API from MagicBell — 2 operation(s) for ses.
  name: MagicBell ses API
  slug: magicbell-ses-api
- description: The slack API from MagicBell — 9 operation(s) for slack.
  name: MagicBell slack API
  slug: magicbell-slack-api
- description: The stripe API from MagicBell — 3 operation(s) for stripe.
  name: MagicBell stripe API
  slug: magicbell-stripe-api
- description: The teams API from MagicBell — 4 operation(s) for teams.
  name: MagicBell teams API
  slug: magicbell-teams-api
- description: The templates API from MagicBell — 3 operation(s) for templates.
  name: MagicBell templates API
  slug: magicbell-templates-api
- description: The twilio API from MagicBell — 2 operation(s) for twilio.
  name: MagicBell twilio API
  slug: magicbell-twilio-api
- description: The user API from MagicBell — 20 operation(s) for user.
  name: MagicBell user API
  slug: magicbell-user-api
- description: The web_push API from MagicBell — 8 operation(s) for web_push.
  name: MagicBell web_push API
  slug: magicbell-web-push-api
artifact_total: 51
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/magicbell-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/magicbell-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magicbell-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.magicbell.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.magicbell.com/docs
- group: docs
  title: ''
  type: ReferenceDocumentation
  url: https://www.magicbell.com/docs/api/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magicbell
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/magicbell
- group: other
  title: ''
  type: X
  url: https://x.com/magicbell_io
- group: company
  title: ''
  type: Blog
  url: https://www.magicbell.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.magicbell.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.magicbell.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/orgs/magicbell/discussions/categories/product-changelog
- group: build
  title: ''
  type: SDKs
  url: https://www.magicbell.com/docs/libraries
- group: build
  title: ''
  type: DeveloperTools
  url: https://www.magicbell.com/tools
- group: commercial
  title: ''
  type: Plans
  url: plans/magicbell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/magicbell-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/magicbell-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/magicbell-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/magicbell-context.jsonld
created: '2026-06-12'
description: MagicBell is a multichannel push notification infrastructure platform that enables developers to deliver in-app, email, mobile push, web push, SMS, Slack, and Microsoft Teams notifications through a single unified REST API. The platform provides a ready-made notification inbox component, built-in user preference management, smart delivery workflows with fallback rules, and full delivery observability with event logging and debugging. MagicBell handles all channel routing and token management so product teams can focus on building rather than maintaining notification infrastructure. It is a Y Combinator (W21) company offering SDKs for JavaScript, React, Go, Swift, Java, and Android along with a CLI for project management.
examples:
- key_count: 14
  name: Magicbell Broadcast Example
  slug: magicbell-broadcast-example
- key_count: 4
  name: Magicbell Event Example
  slug: magicbell-event-example
- key_count: 6
  name: Magicbell Notification Send Example
  slug: magicbell-notification-send-example
- key_count: 9
  name: Magicbell User Example
  slug: magicbell-user-example
finops:
- name: Magicbell Finops
  service_category: ''
  slug: magicbell-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magicbell.png
json_schemas:
- name: AccessToken
  property_count: 4
  slug: magicbell-accesstoken
- name: APNSToken
  property_count: 3
  slug: magicbell-apnstoken
- name: Broadcast
  property_count: 11
  slug: magicbell-broadcast
- name: Event
  property_count: 7
  slug: magicbell-event
- name: FCMToken
  property_count: 2
  slug: magicbell-fcmtoken
- name: Integration
  property_count: 0
  slug: magicbell-integration
- name: SlackToken
  property_count: 2
  slug: magicbell-slacktoken
- name: TeamsToken
  property_count: 1
  slug: magicbell-teamstoken
- name: topic
  property_count: 1
  slug: magicbell-topic
- name: user
  property_count: 0
  slug: magicbell-user
- name: WebPushToken
  property_count: 2
  slug: magicbell-webpushtoken
jsonld:
- class_count: 2
  name: Magicbell Context
  property_count: 24
  slug: magicbell-context
layout: provider
modified: '2026-06-12'
name: MagicBell
nav: Providers
network: true
overview: 'MagicBell publishes 28 APIs on the [APIs.io](https://apis.io/) network, including REST API v1, apns API, awssns API, and 25 more. Tagged areas include notifications, push notifications, in-app notifications, email, and SMS.


  The MagicBell catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MagicBell''s developer surface includes documentation, engineering blog, pricing, changelog, and 16 more developer resources.'
plans:
- name: Magicbell Plans Pricing
  plan_count: 3
  slug: magicbell-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Magicbell Rate Limits
  slug: magicbell-rate-limits
rules:
- name: MagicBell API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: magicbell-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.4
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 53.5
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 22.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magicbell/refs/heads/main/screenshots/magicbell-2026-06-20T184842.png
security:
- kind: domain-security
  name: Magicbell Domain Security
  slug: magicbell-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Magicbell Trust Center
  slug: magicbell-trust-center
  summary_line: GDPR
slug: magicbell
tags:
- notifications
- push notifications
- in-app notifications
- email
- SMS
- Slack
- Microsoft Teams
- webhooks
- notification inbox
- multichannel
- mobile push
- web push
website: https://www.magicbell.com/
---

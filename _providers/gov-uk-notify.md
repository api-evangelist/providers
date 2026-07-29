---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Gov Uk Notify Agentic Access
  operation_count: 11
  slug: gov-uk-notify-agentic-access
  summary_line: 11 operations · 4 acting
api_count: 9
apis:
- description: Official Python client library for the GOV.UK Notify API. Wraps the REST API with idiomatic Python methods for sending SMS, email, and letter notifications; retrieving notification status; listing not
  name: GOV.UK Notify Python Client
  slug: python-client
- description: Official Java client library for the GOV.UK Notify API, providing methods for sending emails, SMS messages, and letters, as well as retrieving notification statuses and managing templates.
  name: GOV.UK Notify Java Client
  slug: java-client
- description: Official .NET client library for the GOV.UK Notify API supporting C# and other .NET languages for sending government notifications via email, SMS, and letters.
  name: GOV.UK Notify .NET Client
  slug: dotnet-client
- description: Official Node.js client library for the GOV.UK Notify API for sending government notifications via email, SMS, and letters from JavaScript and TypeScript applications.
  name: GOV.UK Notify Node.js Client
  slug: nodejs-client
- description: Official PHP client library for the GOV.UK Notify API for sending government notifications via email, SMS, and letters from PHP applications.
  name: GOV.UK Notify PHP Client
  slug: php-client
- description: Official Ruby client library for the GOV.UK Notify API for sending government notifications via email, SMS, and letters from Ruby and Ruby on Rails applications.
  name: GOV.UK Notify Ruby Client
  slug: ruby-client
- description: Send and retrieve notifications (email, SMS, letters)
  name: GOV.UK Notify Notifications API
  slug: gov-uk-notify-notifications-api
- description: Retrieve inbound text messages
  name: GOV.UK Notify Received Text Messages API
  slug: gov-uk-notify-received-text-messages-api
- description: Retrieve and preview notification templates
  name: GOV.UK Notify Templates API
  slug: gov-uk-notify-templates-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gov-uk-notify-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gov-uk-notify-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gov-uk-notify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gov-uk-notify-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.notifications.service.gov.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.notifications.service.gov.uk/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.notifications.service.gov.uk/pricing
- group: operate
  title: ''
  type: Status
  url: https://status.notifications.service.gov.uk/
- group: operate
  title: ''
  type: Support
  url: https://www.notifications.service.gov.uk/support
- group: company
  title: ''
  type: Blog
  url: https://gds.blog.gov.uk/category/gov-uk-notify/
- group: build
  title: ''
  type: x-github
  url: https://github.com/alphagov/notifications-api
- group: commercial
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/finops.yml
created: '2026-06-13'
description: GOV.UK Notify is a UK government notification service operated by the Government Digital Service (GDS) that enables central government, local authorities, NHS organisations, and other eligible public bodies to send emails, text messages, and letters to citizens on behalf of government services. The platform provides a REST API, a web-based sending interface, and official client libraries for Python, Java, .NET, Node.js, PHP, and Ruby. Emails are free and unlimited; SMS messages include an annual free allowance by organisation type with per-message overage at 2.4p; physical letters are priced by postage class and page count with print and postage included. The API uses JWT-based authentication, supports template-driven personalisation, and enforces a throughput limit of 3,000 messages per minute per API key type.
examples:
- key_count: 4
  name: Send Email
  slug: send-email
- key_count: 4
  name: Send Letter
  slug: send-letter
- key_count: 4
  name: Send Sms
  slug: send-sms
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gov-uk-notify.png
json_schemas:
- name: Notification
  property_count: 23
  slug: notification
- name: Send Email Request
  property_count: 7
  slug: send-email-request
- name: Send SMS Request
  property_count: 5
  slug: send-sms-request
layout: provider
modified: '2026-06-13'
name: GOV.UK Notify
nav: Providers
network: true
overview: 'GOV.UK Notify publishes 3 APIs on the [APIs.io](https://apis.io/) network: Notifications API, Received Text Messages API, and Templates API. Tagged areas include Notifications, Email, SMS, Text Messages, and Letters.


  The GOV.UK Notify catalog on APIs.io includes 1 Spectral governance ruleset.


  GOV.UK Notify''s developer surface includes authentication, documentation, pricing, status page, support, engineering blog, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 8
  slug: plans
random_paper: 15
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: GOV.UK Notify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: gov-uk-notify-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.5
  delta: -4.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 62.7
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 33.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gov-uk-notify/refs/heads/main/screenshots/gov-uk-notify-2026-06-20T182256.png
security:
- kind: authentication
  name: Gov Uk Notify Authentication
  slug: gov-uk-notify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gov Uk Notify Domain Security
  slug: gov-uk-notify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gov Uk Notify Vulnerability Disclosure
  slug: gov-uk-notify-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: gov-uk-notify
tags:
- Notifications
- Email
- SMS
- Text Messages
- Letters
- Government
- United Kingdom
- Public Sector
- GDS
- REST
website: https://www.notifications.service.gov.uk/
---

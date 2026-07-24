---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Mailmodo Agentic Access
  operation_count: 14
  slug: mailmodo-agentic-access
  summary_line: 14 operations · 10 acting
api_count: 5
apis:
- description: List campaigns, fetch reports, and trigger sends to individuals or lists
  name: Mailmodo Campaigns API
  slug: mailmodo-campaigns-api
- description: Manage the named contact lists used for segmentation and campaigns
  name: Mailmodo Contact Lists API
  slug: mailmodo-contact-lists-api
- description: Add, remove, archive, unsubscribe, resubscribe, and look up contacts
  name: Mailmodo Contacts API
  slug: mailmodo-contacts-api
- description: Send custom user events into Mailmodo journeys and segments
  name: Mailmodo Events API
  slug: mailmodo-events-api
- description: List interactive AMP email templates available on the workspace
  name: Mailmodo Templates API
  slug: mailmodo-templates-api
artifact_total: 56
collections:
- collection_type: open
  name: Mailmodo API
  slug: open-mailmodo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mailmodo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mailmodo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mailmodo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mailmodo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mailmodo.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.mailmodo.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.mailmodo.com/
- group: operate
  title: ''
  type: Support
  url: https://support.mailmodo.com/
- group: start
  title: ''
  type: Signup
  url: https://manage.mailmodo.com/auth/signup
- group: start
  title: ''
  type: Portal
  url: https://manage.mailmodo.com/
- group: start
  title: ''
  type: Console
  url: https://manage.mailmodo.com/app/settings/apikey
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mailmodo.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mailmodo.com/gdpr/termsandconditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mailmodo.com/gdpr/privacypolicy/
- group: company
  title: ''
  type: Blog
  url: https://www.mailmodo.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mailmodo
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/mailmodo/mailmodo-mcp
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/mailmodo/refs/heads/main/rules/mailmodo-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/mailmodo/refs/heads/main/vocabulary/mailmodo-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/mailmodo/refs/heads/main/plans/mailmodo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/mailmodo/refs/heads/main/rate-limits/mailmodo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/mailmodo/refs/heads/main/finops/mailmodo-finops.yml
created: '2026-05-25'
description: Mailmodo is an AI-powered interactive email marketing and automation platform headquartered in Bengaluru with a presence in San Francisco. It pioneered AMP-for-Email at scale, letting brands embed forms, quizzes, polls, carousels, and calendars directly inside the inbox to drive engagement and conversions without a landing-page round-trip. The platform layers AI assistance on top of campaigns, journeys, segmentation, and analytics, and exposes a REST API for contact management, transactional sends, broadcast and bulk triggers, custom event ingestion, and campaign reporting.
examples:
- key_count: 2
  name: Mailmodo Add Contact Example
  slug: mailmodo-add-contact-example
- key_count: 2
  name: Mailmodo Add Event Example
  slug: mailmodo-add-event-example
- key_count: 2
  name: Mailmodo Trigger Campaign Example
  slug: mailmodo-trigger-campaign-example
features:
- description: Embed forms, quizzes, polls, carousels, calendars, and other interactive widgets directly inside the email so recipients act without leaving the inbox.
  name: Interactive AMP-for-Email
- description: Generate on-brand HTML/AMP templates from a prompt.
  name: AI Email Template Generator
- description: Compose multi-step journeys from natural-language descriptions.
  name: AI Automation Builder
- description: Translate plain-language audience descriptions into contact segments.
  name: AI Segment Generator
- description: Summarize and recommend next steps from campaign metrics.
  name: AI Campaign Analyzer
- description: Trigger campaigns per recipient with merge data.
  name: Transactional Email API
- description: Send a campaign to many recipients in a single API call.
  name: Bulk Campaign Trigger
- description: Hands-on deliverability service for high-volume senders.
  name: Managed Deliverability
finops:
- name: Mailmodo Finops
  service_category: ''
  slug: mailmodo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mailmodo.png
integrations:
- description: Sync contacts and trigger Mailmodo campaigns from HubSpot.
  name: HubSpot
- description: CRM data sync and campaign triggers.
  name: Salesforce
- description: Ecommerce contact and order event sync.
  name: Shopify
- description: No-code automations across thousands of apps.
  name: Zapier
- description: Visual workflow automation.
  name: Make (Integromat)
- description: Customer messaging platform sync.
  name: Customer.io
- description: Cross-channel engagement platform sync.
  name: MoEngage
- description: Customer engagement platform sync.
  name: WebEngage
- description: CRM sync for SMB use cases.
  name: Zoho CRM
- description: Freshworks CRM and marketing automation sync.
  name: Freshsales / Freshmarketer
- description: Mobile-first engagement platform sync.
  name: CleverTap
- description: Booking event sync into journeys.
  name: Calendly
- description: Webinar registrant sync.
  name: Zoom
- description: Workflow automation integration.
  name: Pabbly
json_schemas:
- name: Mailmodo Campaign
  property_count: 10
  slug: mailmodo-campaign
- name: Mailmodo Contact
  property_count: 8
  slug: mailmodo-contact
- name: Mailmodo Custom Event
  property_count: 4
  slug: mailmodo-event
- name: Mailmodo Template
  property_count: 6
  slug: mailmodo-template
json_structures:
- name: Mailmodo Campaign Structure
  property_count: 0
  slug: mailmodo-campaign-structure
- name: Mailmodo Contact Structure
  property_count: 0
  slug: mailmodo-contact-structure
jsonld:
- class_count: 16
  name: Mailmodo Context
  property_count: 0
  slug: mailmodo-context
layout: provider
modified: '2026-05-25'
name: Mailmodo
nav: Providers
network: true
overview: 'Mailmodo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Contact Lists API, Contacts API, and 2 more. Tagged areas include Email, Interactive Email, AMP for Email, Marketing Automation, and Transactional Email.


  The Mailmodo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Mailmodo''s developer surface includes authentication, documentation, API reference, support, signup flow, developer portal, developer console, and 15 more developer resources.'
plans:
- name: Mailmodo Plans Pricing
  plan_count: 4
  slug: mailmodo-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 0
  name: Mailmodo Rate Limits
  slug: mailmodo-rate-limits
rules:
- name: Mailmodo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mailmodo-jsonschema-spectral-rules
- name: Mailmodo API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: mailmodo-rules
score:
  band: developing
  composite: 59.1
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 63.7
    developer_ergonomics: 47.8
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 5.3
  previous_composite: 59.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mailmodo/refs/heads/main/screenshots/mailmodo-2026-06-20T184904.png
security:
- kind: authentication
  name: Mailmodo Authentication
  slug: mailmodo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mailmodo Domain Security
  slug: mailmodo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Mailmodo Trust Center
  slug: mailmodo-trust-center
  summary_line: SOC 2, GDPR
slug: mailmodo
solutions:
- description: Cart recovery, product launches, post-purchase journeys with AMP forms.
  name: Ecommerce
- description: Onboarding, activation, NPS, and feature-adoption journeys.
  name: SaaS
- description: Interactive newsletters with embedded polls and content carousels.
  name: Media & Newsletter
- description: Managed deliverability with custom SLAs.
  name: Enterprise Marketing
tags:
- Email
- Interactive Email
- AMP for Email
- Marketing Automation
- Transactional Email
- Campaigns
- Journeys
- Customer Engagement
use_cases:
- description: Capture survey, lead, and feedback responses inline.
  name: Interactive Forms in Email
- description: Drive engagement and sales via in-email quizzes and games.
  name: Quizzes & Gamification
- description: Automate welcome, activation, and re-engagement flows.
  name: Lifecycle & Onboarding Journeys
- description: Order confirmations, receipts, password resets driven by API.
  name: Transactional & Triggered Email
- description: Send rich interactive newsletters to large contact lists.
  name: Newsletters & Broadcasts
website: https://www.mailmodo.com
---

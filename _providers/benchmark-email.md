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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 130
  human_in_the_loop: 3
  name: Benchmark Email Agentic Access
  operation_count: 296
  slug: benchmark-email-agentic-access
  summary_line: 296 operations · 130 acting · 3 human-in-the-loop
api_count: 29
apis:
- description: Create and manage A/B split tests
  name: Benchmark Email ABTest Creation API
  slug: benchmark-email-abtest-creation-api
- description: Manage account settings and configurations
  name: Benchmark Email Account Settings API
  slug: benchmark-email-account-settings-api
- description: Add and import contacts to lists
  name: Benchmark Email Add Contacts API
  slug: benchmark-email-add-contacts-api
- description: Manage linked agency accounts
  name: Benchmark Email Agency Account API
  slug: benchmark-email-agency-account-api
- description: Manage email archive and archive pages
  name: Benchmark Email Archive API
  slug: benchmark-email-archive-api
- description: Create and manage automation workflows
  name: Benchmark Email Automation Creation API
  slug: benchmark-email-automation-creation-api
- description: Configure and search contacts
  name: Benchmark Email Contact Configurations & Searches API
  slug: benchmark-email-contact-configurations-searches-api
- description: Contact reporting and metrics
  name: Benchmark Email Contact Reports & Metrics API
  slug: benchmark-email-contact-reports-metrics-api
- description: Email template and layout management
  name: Benchmark Email Email Editor API
  slug: benchmark-email-email-editor-api
- description: Email Email Rss Creation
  name: Benchmark Email Email  Email Rss Creation API
  slug: benchmark-email-email-email-rss-creation-api
- description: Engagement analytics and list building
  name: Benchmark Email Engagement API
  slug: benchmark-email-engagement-api
- description: General operations
  name: Benchmark Email General API
  slug: benchmark-email-general-api
- description: Help desk and support tickets
  name: Benchmark Email Help API
  slug: benchmark-email-help-api
- description: Manage image gallery
  name: Benchmark Email Image Gallery API
  slug: benchmark-email-image-gallery-api
- description: Test emails in inbox preview
  name: Benchmark Email Inbox Checker API
  slug: benchmark-email-inbox-checker-api
- description: Configure and search contact lists
  name: Benchmark Email List Configurations & Searches API
  slug: benchmark-email-list-configurations-searches-api
- description: List reporting and metrics
  name: Benchmark Email List Reporting or  Metrics API
  slug: benchmark-email-list-reporting-or-metrics-api
- description: Partner commission and referral management
  name: Benchmark Email Partner API
  slug: benchmark-email-partner-api
- description: Create and manage polls
  name: Benchmark Email Poll Creation API
  slug: benchmark-email-poll-creation-api
- description: Campaign reporting and analytics
  name: Benchmark Email Reports API
  slug: benchmark-email-reports-api
- description: Authentication and security operations
  name: Benchmark Email Security API
  slug: benchmark-email-security-api
- description: Manage contact segments
  name: Benchmark Email Segments API
  slug: benchmark-email-segments-api
- description: Manage signup forms
  name: Benchmark Email Signup Form API
  slug: benchmark-email-signup-form-api
- description: Manage sub-accounts and their settings
  name: Benchmark Email Sub-Account API
  slug: benchmark-email-sub-account-api
- description: Survey
  name: Benchmark Email Survey API
  slug: benchmark-email-survey-api
- description: Create and manage surveys
  name: Benchmark Email Survey Creation API
  slug: benchmark-email-survey-creation-api
- description: Third-party signup form integrations
  name: Benchmark Email Third Party Signup Forms API
  slug: benchmark-email-third-party-signup-forms-api
- description: Manage video gallery
  name: Benchmark Email Video Gallery API
  slug: benchmark-email-video-gallery-api
- description: Manage webhooks for event notifications
  name: Benchmark Email Webhooks API
  slug: benchmark-email-webhooks-api
artifact_total: 47
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/benchmark-email-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/benchmark-email-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/benchmark-email-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.benchmarkemail.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.benchmarkemail.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/BenchmarkEmail
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/benchmark-email/
- group: company
  title: ''
  type: Blog
  url: https://www.benchmarkemail.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.benchmarkemail.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.benchmarkemail.com/status/
- group: other
  title: ''
  type: X
  url: https://twitter.com/benchmarkemail
- group: commercial
  title: ''
  type: Plans
  url: plans/benchmark-email-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/benchmark-email-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/benchmark-email-finops.yml
created: '2026-06-13'
description: Benchmark Email is an email marketing platform with a REST API for managing contacts, lists, email campaigns, automations, reports, and transactional email delivery. The API supports contact synchronization, campaign management, reporting analytics, domain verification, and webhook notifications for real-time event handling.
examples:
- key_count: 4
  name: Add Contact
  slug: add-contact
- key_count: 4
  name: Create Contact List
  slug: create-contact-list
- key_count: 4
  name: Create Webhook
  slug: create-webhook
- key_count: 4
  name: Get Campaign Report
  slug: get-campaign-report
- key_count: 4
  name: Send Campaign
  slug: send-campaign
finops:
- name: Benchmark Email Finops
  service_category: ''
  slug: benchmark-email-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/benchmark-email.png
json_schemas:
- name: CampaignReport
  property_count: 12
  slug: campaign-report
- name: ContactList
  property_count: 8
  slug: contact-list
- name: Contact
  property_count: 8
  slug: contact
- name: EmailCampaign
  property_count: 12
  slug: email-campaign
- name: Webhook
  property_count: 6
  slug: webhook
jsonld:
- class_count: 17
  name: Benchmark Email Context
  property_count: 35
  slug: benchmark-email-context
layout: provider
modified: '2026-06-13'
name: Benchmark Email
nav: Providers
network: true
overview: 'Benchmark Email publishes 29 APIs on the [APIs.io](https://apis.io/) network, including ABTest Creation API, Account Settings API, Add Contacts API, and 26 more. Tagged areas include Email Marketing, Campaigns, Contacts, Automation, and Transactional Email.


  The Benchmark Email catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Benchmark Email''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Benchmark Email Plans Pricing
  plan_count: 3
  slug: benchmark-email-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 0
  name: Benchmark Email Rate Limits
  slug: benchmark-email-rate-limits
rules:
- name: Benchmark Email API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: benchmark-email-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.9
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/benchmark-email/refs/heads/main/screenshots/benchmark-email-2026-06-20T173133.png
security:
- kind: authentication
  name: Benchmark Email Authentication
  slug: benchmark-email-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Benchmark Email Domain Security
  slug: benchmark-email-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: benchmark-email
tags:
- Email Marketing
- Campaigns
- Contacts
- Automation
- Transactional Email
- Marketing
website: https://www.benchmarkemail.com/
---

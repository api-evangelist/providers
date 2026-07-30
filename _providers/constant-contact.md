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
- acting_count: 60
  human_in_the_loop: 2
  name: Constant Contact Agentic Access
  operation_count: 120
  slug: constant-contact-agentic-access
  summary_line: 120 operations · 60 acting · 2 human-in-the-loop
api_count: 17
apis:
- description: Use the account endpoints and methods to get account information.
  name: Constant Contact Account Services API
  slug: constant-contact-account-services-api
- description: Bulk activities endpoints are used to manage large numbers of contacts, lists, and tags.
  name: Constant Contact Bulk Activities API
  slug: constant-contact-bulk-activities-api
- description: Endpoints and methods to get, create, delete, and update one or more contact lists.
  name: Constant Contact Contact Lists API
  slug: constant-contact-contact-lists-api
- description: Endpoints and methods to get, create, delete, and update one or more contact tags.
  name: Constant Contact Contact Tags API
  slug: constant-contact-contact-tags-api
- description: Endpoints and methods to get, create, delete, and update one or more contacts.
  name: Constant Contact Contacts API
  slug: constant-contact-contacts-api
- description: Endpoints and methods to get, create, delete, and update on one or more custom fields.
  name: Constant Contact Contacts Custom Fields API
  slug: constant-contact-contacts-custom-fields-api
- description: Contact reporting endpoints are used to gather activity reports for campaigns sent to a contact.
  name: Constant Contact Contacts Reporting API
  slug: constant-contact-contacts-reporting-api
- description: Use email campaigns A/B Test endpoints and methods to get, create, delete and update A/B tests.
  name: Constant Contact Email Campaigns AB Tests API
  slug: constant-contact-email-campaigns-ab-tests-api
- description: Use email campaign endpoints and methods to get, create, and update email campaigns.
  name: Constant Contact Email Campaigns API
  slug: constant-contact-email-campaigns-api
- description: Use the email reporting endpoints and methods to get reporting data for email campaigns you sent to contacts.
  name: Constant Contact Email Reporting API
  slug: constant-contact-email-reporting-api
- description: Use email scheduling endpoints and methods to schedule an email campaign activity, unschedule an email campaign activity, and GET schedule information.
  name: Constant Contact Email Scheduling API
  slug: constant-contact-email-scheduling-api
- description: Endpoints and methods used to create and manage events.
  name: Constant Contact Events API
  slug: constant-contact-events-api
- description: Use landing pages reporting endpoints and methods to get reporting data about how a contact interacted with a campaign activity.
  name: Constant Contact Landing Pages Reporting API
  slug: constant-contact-landing-pages-reporting-api
- description: Use segments to target a subset of your contacts that are most likely to engage with a particular campaign.
  name: Constant Contact Segments API
  slug: constant-contact-segments-api
- description: Use SMS reporting endpoints and methods to get reporting data about SMS campaigns.
  name: Constant Contact SMS Reporting API
  slug: constant-contact-sms-reporting-api
- description: Use partner endpoints to manage client Constant Contact accounts under your partner account.
  name: Constant Contact Technology Partners API
  slug: constant-contact-technology-partners-api
- description: Use partner webhooks to subscribe to billing event notifications from Constant Contact.
  name: Constant Contact Technology Partners Webhooks API
  slug: constant-contact-technology-partners-webhooks-api
artifact_total: 47
collections:
- collection_type: open
  name: AppConnect V3
  slug: open-constant-contact-v3
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/constant-contact-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/constant-contact-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/constant-contact-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/constant-contact
- group: company
  title: ''
  type: Website
  url: https://www.constantcontact.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.constantcontact.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.constantcontact.com/api_guide/index.html
- group: auth
  title: ''
  type: Authentication
  url: https://developer.constantcontact.com/api_guide/auth_overview.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.constantcontact.com/api_reference/index.html
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.cc.email/v3/swagger.yaml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.constantcontact.com/
- group: operate
  title: ''
  type: Support
  url: https://www.constantcontact.com/help
- group: operate
  title: ''
  type: Community
  url: https://community.constantcontact.com/
- group: company
  title: ''
  type: Blog
  url: https://blogs.constantcontact.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/constantcontact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.constantcontact.com/legal/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.constantcontact.com/legal/terms-of-use
- group: design
  title: ''
  type: JSONLD
  url: json-ld/constant-contact-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/constant-contact-contact-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/constant-contact-campaign-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/constant-contact-rules.yml
created: '2025-03-01'
description: Constant Contact is a small-business email and digital marketing platform offering email campaigns, automation, SMS, contact management, surveys, and events. The Constant Contact V3 API is a REST + JSON, OAuth2-protected service published at api.cc.email/v3 covering accounts, contacts, lists, tags, custom fields, segments, email campaigns, A/B tests, schedules and tests, bulk activities (CSV/JSON import, export, list and tag mutations), events with registration and check-in, reporting, and partner provisioning.
features:
- 'Lite: $12/mo for 500 contacts (jumps to $50/mo at 1K)'
- 'Standard: mid-tier with A/B testing, segmentation'
- 'Premium: $80/mo at 500 contacts with 24x email ratio'
- 'Email overages: $0.002 per additional email'
- REST API v3 at api.cc.email/v3
- 'API limit: 4 req/sec, 10K req/day per app'
- OAuth 2.0
- Webhooks for contact and campaign events
- Contacts, lists, segments, custom fields
- Email Templates and Drag-and-Drop editor
- Marketing Automation (Standard+)
- Surveys, landing pages, social media posts
- Reporting on opens, clicks, bounces, conversions
- E-commerce integrations (Shopify, WooCommerce, etc.)
- Event marketing and registration
- List building tools and lead capture
finops:
- name: Constant Contact Finops
  service_category: Email Marketing
  slug: constant-contact-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Constant Contact V3 API. Constant Contact is a small-business email and digital marketing platform offering email campaigns, automation, SMS
  name: Constant Contact GraphQL Schema
  slug: constant-contact-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/constant-contact.png
json_schemas:
- name: Constant Contact Email Campaign
  property_count: 8
  slug: constant-contact-campaign
- name: Constant Contact Contact
  property_count: 17
  slug: constant-contact-contact
json_structures:
- name: Constant Contact Structure
  property_count: 0
  slug: constant-contact-structure
jsonld:
- class_count: 0
  name: Constant Contact Context
  property_count: 8
  slug: constant-contact-context
layout: provider
modified: '2026-05-19'
name: Constant Contact
nav: Providers
network: true
overview: 'Constant Contact publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Account Services API, Bulk Activities API, Contact Lists API, and 14 more. Tagged areas include Campaigns, Contacts, Email Marketing, Events, and Reporting.


  The Constant Contact catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Constant Contact''s developer surface includes authentication, developer portal, getting-started guide, API reference, support, engineering blog, and 15 more developer resources.'
plans:
- name: Constant Contact Plans Pricing
  plan_count: 3
  slug: constant-contact-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 3
  name: Constant Contact Rate Limits
  slug: constant-contact-rate-limits
rules:
- name: Constant Contact API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: constant-contact-jsonschema-spectral-rules
- name: Constant Contact API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: constant-contact-rules
score:
  band: developing
  composite: 51.4
  delta: -6.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 49.4
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 58.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/constant-contact/refs/heads/main/screenshots/constant-contact-2026-06-20T175012.png
security:
- kind: authentication
  name: Constant Contact Authentication
  slug: constant-contact-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Constant Contact Domain Security
  slug: constant-contact-domain-security
  summary_line: TLSv1.3 · DMARC
slug: constant-contact
tags:
- Campaigns
- Contacts
- Email Marketing
- Events
- Reporting
- SMS
- Surveys
website: https://www.constantcontact.com/
---

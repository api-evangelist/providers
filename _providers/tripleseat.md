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
    asyncapi_events: true
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
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Tripleseat Agentic Access
  operation_count: 15
  slug: tripleseat-agentic-access
  summary_line: 15 operations · 3 acting
api_count: 7
apis:
- description: Retrieve and update accounts.
  name: Tripleseat Accounts API
  slug: tripleseat-accounts-api
- description: Create and associate contacts with accounts.
  name: Tripleseat Contacts API
  slug: tripleseat-contacts-api
- description: Retrieve events and their bookings.
  name: Tripleseat Events API
  slug: tripleseat-events-api
- description: Capture and retrieve leads, including the public lead form.
  name: Tripleseat Leads API
  slug: tripleseat-leads-api
- description: Retrieve locations within a site.
  name: Tripleseat Locations API
  slug: tripleseat-locations-api
- description: Retrieve sites that group locations.
  name: Tripleseat Sites API
  slug: tripleseat-sites-api
- description: Retrieve Tripleseat users.
  name: Tripleseat Users API
  slug: tripleseat-users-api
artifact_total: 71
asyncapis:
- description: Tripleseat webhooks POST a JSON package to a subscriber URL when a lead or booking lifecycle event occurs. Each request carries an X-Signature header computed with SHA256-HMAC using the webhook endpoi
  name: Tripleseat Webhooks
  slug: tripleseat-webhooks-asyncapi
collections:
- collection_type: open
  name: Tripleseat API
  slug: open-tripleseat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tripleseat-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tripleseat-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tripleseat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tripleseat-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tripleseat-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://tripleseat.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.tripleseat.com/hc/en-us/sections/200821727-Tripleseat-API
- group: operate
  title: ''
  type: Support
  url: https://support.tripleseat.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tripleseat
- group: company
  title: ''
  type: Blog
  url: https://tripleseat.com/blog/
- group: other
  title: ''
  type: Marketplace
  url: https://tripleseat.com/partnermarketplace/
- group: company
  title: ''
  type: Partners
  url: https://tripleseat.com/partner-types/integrations/
- group: commercial
  title: ''
  type: Pricing
  url: https://support.tripleseat.com/hc/en-us/sections/24155934375191-Registration-and-Pricing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tripleseat-software/
- group: design
  title: ''
  type: SpectralRules
  url: rules/tripleseat-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tripleseat-vocabulary.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/tripleseat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tripleseat-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tripleseat-finops.yml
created: '2026-06-02'
description: Tripleseat is event management and catering sales software for restaurants, hotels, and unique venues, helping operators capture leads, book events, and manage the sales lifecycle. Tripleseat provides a public REST API and webhooks for partners and customers to integrate event and lead data with external systems. The API exposes endpoints for leads, events, accounts, contacts, locations, sites, and users, and supports a public lead form for capturing inquiries directly into Tripleseat. Webhooks emit trigger events such as CREATE_LEAD, CONVERT_LEAD, and CONVERT_LEAD_TO_BOOKING, signed with a SHA256-HMAC X-Signature header. Authentication moved from OAuth 1.0 to OAuth 2.0, with OAuth 1.0 discontinued on July 1, 2026, and v1 endpoints served from api.tripleseat.com.
examples:
- key_count: 10
  name: Tripleseat Api Account Example
  slug: tripleseat-api-account-example
- key_count: 7
  name: Tripleseat Api Account Update Example
  slug: tripleseat-api-account-update-example
- key_count: 5
  name: Tripleseat Api Contact Create Example
  slug: tripleseat-api-contact-create-example
- key_count: 8
  name: Tripleseat Api Contact Example
  slug: tripleseat-api-contact-example
- key_count: 11
  name: Tripleseat Api Event Example
  slug: tripleseat-api-event-example
- key_count: 12
  name: Tripleseat Api Lead Create Example
  slug: tripleseat-api-lead-create-example
- key_count: 16
  name: Tripleseat Api Lead Example
  slug: tripleseat-api-lead-example
- key_count: 7
  name: Tripleseat Api Location Example
  slug: tripleseat-api-location-example
- key_count: 2
  name: Tripleseat Api Site Example
  slug: tripleseat-api-site-example
- key_count: 5
  name: Tripleseat Api User Example
  slug: tripleseat-api-user-example
- key_count: 1
  name: Tripleseat Webhooks Webhook Headers Example
  slug: tripleseat-webhooks-webhook-headers-example
- key_count: 3
  name: Tripleseat Webhooks Webhook Payload Example
  slug: tripleseat-webhooks-webhook-payload-example
features:
- description: Capture inquiries through the public lead form API and the leads endpoints, routing leads to the correct location.
  name: Lead Capture
- description: Retrieve and manage events and bookings across the sales lifecycle.
  name: Event And Booking Management
- description: Maintain accounts and their associated contacts for customer records.
  name: Account And Contact CRM
- description: Subscribe to lead and booking lifecycle events, verified with a SHA256-HMAC X-Signature header.
  name: Webhooks
- description: Model sites that group multiple locations and target leads and events at specific locations.
  name: Multi-Location Support
finops:
- name: Tripleseat Finops
  service_category: Event Management
  slug: tripleseat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tripleseat.png
integrations:
- description: Reservation, seating, and guest management platform that shares reservation and event details with Tripleseat.
  name: SevenRooms
- description: Connect Tripleseat events to OpenTable guest center bookings to avoid double bookings.
  name: OpenTable Guest Center
- description: Collect private event leads from Tock and transfer them into Tripleseat.
  name: Tock
- description: Tripleseat integration available through the Square App Marketplace.
  name: Square
json_schemas:
- name: Account
  property_count: 10
  slug: tripleseat-api-account
- name: AccountUpdate
  property_count: 7
  slug: tripleseat-api-account-update
- name: ContactCreate
  property_count: 5
  slug: tripleseat-api-contact-create
- name: Contact
  property_count: 8
  slug: tripleseat-api-contact
- name: Event
  property_count: 11
  slug: tripleseat-api-event
- name: LeadCreate
  property_count: 12
  slug: tripleseat-api-lead-create
- name: Lead
  property_count: 16
  slug: tripleseat-api-lead
- name: Location
  property_count: 7
  slug: tripleseat-api-location
- name: Site
  property_count: 2
  slug: tripleseat-api-site
- name: User
  property_count: 5
  slug: tripleseat-api-user
- name: WebhookHeaders
  property_count: 1
  slug: tripleseat-webhooks-webhook-headers
- name: WebhookPayload
  property_count: 3
  slug: tripleseat-webhooks-webhook-payload
json_structures:
- name: Tripleseat Api Account Structure
  property_count: 10
  slug: tripleseat-api-account-structure
- name: Tripleseat Api Account Update Structure
  property_count: 7
  slug: tripleseat-api-account-update-structure
- name: Tripleseat Api Contact Create Structure
  property_count: 5
  slug: tripleseat-api-contact-create-structure
- name: Tripleseat Api Contact Structure
  property_count: 8
  slug: tripleseat-api-contact-structure
- name: Tripleseat Api Event Structure
  property_count: 11
  slug: tripleseat-api-event-structure
- name: Tripleseat Api Lead Create Structure
  property_count: 12
  slug: tripleseat-api-lead-create-structure
- name: Tripleseat Api Lead Structure
  property_count: 16
  slug: tripleseat-api-lead-structure
- name: Tripleseat Api Location Structure
  property_count: 7
  slug: tripleseat-api-location-structure
- name: Tripleseat Api Site Structure
  property_count: 2
  slug: tripleseat-api-site-structure
- name: Tripleseat Api User Structure
  property_count: 5
  slug: tripleseat-api-user-structure
- name: Tripleseat Webhooks Webhook Headers Structure
  property_count: 1
  slug: tripleseat-webhooks-webhook-headers-structure
- name: Tripleseat Webhooks Webhook Payload Structure
  property_count: 3
  slug: tripleseat-webhooks-webhook-payload-structure
jsonld:
- class_count: 10
  name: Tripleseat Api Context
  property_count: 25
  slug: tripleseat-api-context
- class_count: 2
  name: Tripleseat Webhooks Context
  property_count: 8
  slug: tripleseat-webhooks-context
layout: provider
modified: '2026-06-03'
name: Tripleseat
nav: Providers
network: true
overview: 'Tripleseat publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contacts API, Events API, and 4 more. Tagged areas include Restaurant, Events, Catering, Leads, and Webhooks.


  The Tripleseat catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Tripleseat''s developer surface includes authentication, documentation, support, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Tripleseat Plans Pricing
  plan_count: 5
  slug: tripleseat-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Tripleseat Rate Limits
  slug: tripleseat-rate-limits
rules:
- name: Tripleseat API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: tripleseat-asyncapi-spectral-rules
- name: Tripleseat API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tripleseat-jsonschema-spectral-rules
- name: Tripleseat API Rules
  rule_count: 39
  severity_counts:
    error: 7
    hint: 0
    info: 6
    warn: 26
  slug: tripleseat-spectral-rules
scopes:
- name: Tripleseat Scopes
  scope_count: 6
  slug: tripleseat-scopes
  summary_line: 6 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 57.3
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 84.1
    developer_ergonomics: 26.1
    discoverability: 67.5
    governance: 65.8
    operational_transparency: 36.8
  previous_composite: 57.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tripleseat/refs/heads/main/screenshots/tripleseat-2026-06-20T195730.png
security:
- kind: authentication
  name: Tripleseat Authentication
  slug: tripleseat-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tripleseat Domain Security
  slug: tripleseat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tripleseat Trust Center
  slug: tripleseat-trust-center
  summary_line: SOC 2, ISO 27001
slug: tripleseat
tags:
- Restaurant
- Events
- Catering
- Leads
- Webhooks
- Sales
use_cases:
- description: Embed a public lead form on a website to push inquiries directly into Tripleseat via the lead form API.
  name: Website Lead Forms
- description: Synchronize accounts, contacts, and events with external CRM and email marketing platforms.
  name: CRM And Marketing Sync
- description: React to lead creation and conversion in real time using webhooks to drive downstream automation.
  name: Real-Time Integrations
- description: Extract events and leads into data warehouses and dashboards for sales reporting.
  name: Reporting And Analytics
website: https://tripleseat.com
---

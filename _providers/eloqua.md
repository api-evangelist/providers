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
- acting_count: 63
  human_in_the_loop: 0
  name: Eloqua Agentic Access
  operation_count: 111
  slug: eloqua-agentic-access
  summary_line: 111 operations · 63 acting
api_count: 22
apis:
- description: Export account data in bulk
  name: Oracle Eloqua Account Exports API
  slug: eloqua-account-exports-api
- description: Retrieve available account fields for mapping
  name: Oracle Eloqua Account Fields API
  slug: eloqua-account-fields-api
- description: Import account data in bulk
  name: Oracle Eloqua Account Imports API
  slug: eloqua-account-imports-api
- description: Manage account records and groups
  name: Oracle Eloqua Accounts API
  slug: eloqua-accounts-api
- description: Export activity data in bulk
  name: Oracle Eloqua Activity Exports API
  slug: eloqua-activity-exports-api
- description: Import activity data in bulk
  name: Oracle Eloqua Activity Imports API
  slug: eloqua-activity-imports-api
- description: Create and manage marketing campaigns
  name: Oracle Eloqua Campaigns API
  slug: eloqua-campaigns-api
- description: Export contact data in bulk
  name: Oracle Eloqua Contact Exports API
  slug: eloqua-contact-exports-api
- description: Retrieve available contact fields for mapping
  name: Oracle Eloqua Contact Fields API
  slug: eloqua-contact-fields-api
- description: Import contact data in bulk
  name: Oracle Eloqua Contact Imports API
  slug: eloqua-contact-imports-api
- description: Create and manage contact lists
  name: Oracle Eloqua Contact Lists API
  slug: eloqua-contact-lists-api
- description: Create and manage contact segments
  name: Oracle Eloqua Contact Segments API
  slug: eloqua-contact-segments-api
- description: Manage contact records and data
  name: Oracle Eloqua Contacts API
  slug: eloqua-contacts-api
- description: Export custom object data in bulk
  name: Oracle Eloqua Custom Object Exports API
  slug: eloqua-custom-object-exports-api
- description: Import custom object data in bulk
  name: Oracle Eloqua Custom Object Imports API
  slug: eloqua-custom-object-imports-api
- description: Manage custom object definitions and data
  name: Oracle Eloqua Custom Objects API
  slug: eloqua-custom-objects-api
- description: Create and manage email assets
  name: Oracle Eloqua Emails API
  slug: eloqua-emails-api
- description: Create and manage forms and form data
  name: Oracle Eloqua Forms API
  slug: eloqua-forms-api
- description: Create and manage landing pages
  name: Oracle Eloqua Landing Pages API
  slug: eloqua-landing-pages-api
- description: Create and manage automation programs
  name: Oracle Eloqua Programs API
  slug: eloqua-programs-api
- description: Manage data synchronization operations
  name: Oracle Eloqua Syncs API
  slug: eloqua-syncs-api
- description: Manage system users
  name: Oracle Eloqua Users API
  slug: eloqua-users-api
artifact_total: 36
collections:
- collection_type: open
  name: Oracle Eloqua Bulk API
  slug: open-eloqua-bulk
- collection_type: open
  name: Oracle Eloqua REST API
  slug: open-eloqua-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eloqua-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eloqua-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eloqua-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/eloqua-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eloqua
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/GettingStarted.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/Authentication.html
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: build
  title: ''
  type: SDKs
  url: https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/SDKs.html
created: '2025-01-01'
description: Oracle Eloqua is a marketing automation platform that provides tools for lead management, email marketing, and marketing campaign management through comprehensive REST APIs. It enables marketing teams to create, execute, and measure the effectiveness of marketing programs and campaigns.
finops:
- name: Eloqua Finops
  service_category: API
  slug: eloqua-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eloqua.png
json_schemas:
- name: Eloqua Campaign
  property_count: 20
  slug: eloqua-campaign
- name: Eloqua Contact
  property_count: 36
  slug: eloqua-contact
- name: Eloqua Email
  property_count: 39
  slug: eloqua-email
jsonld:
- class_count: 0
  name: Eloqua Context
  property_count: 10
  slug: eloqua-context
layout: provider
modified: '2026-05-19'
name: Oracle Eloqua
nav: Providers
network: true
overview: 'Oracle Eloqua publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Account Exports API, Account Fields API, Account Imports API, and 19 more. Tagged areas include CRM, Email Marketing, Lead Management, and Marketing Automation.


  The Oracle Eloqua catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oracle Eloqua''s developer surface includes authentication, getting-started guide, support, and 8 more developer resources.'
plans:
- name: Eloqua Plans Pricing
  plan_count: 3
  slug: eloqua-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Eloqua Rate Limits
  slug: eloqua-rate-limits
rules:
- name: Oracle Eloqua API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: eloqua-jsonschema-spectral-rules
scopes:
- name: Eloqua Scopes
  scope_count: 1
  slug: eloqua-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 54.1
  delta: -3.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.6
    developer_ergonomics: 32.6
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eloqua/refs/heads/main/screenshots/eloqua-2026-06-20T180617.png
security:
- kind: authentication
  name: Eloqua Authentication
  slug: eloqua-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Eloqua Domain Security
  slug: eloqua-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eloqua
tags:
- CRM
- Email Marketing
- Lead Management
- Marketing Automation
website: https://www.oracle.com/marketingcloud/products/marketing-automation/
---

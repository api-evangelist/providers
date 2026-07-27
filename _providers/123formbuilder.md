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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: 123Formbuilder Agentic Access
  operation_count: 26
  slug: 123formbuilder-agentic-access
  summary_line: 26 operations · 17 acting
api_count: 5
apis:
- description: Create and update billable accounts.
  name: 123FormBuilder Accounts API
  slug: 123formbuilder-accounts-api
- description: Create, list, read, update, and delete forms, fields, and submissions.
  name: 123FormBuilder Forms API
  slug: 123formbuilder-forms-api
- description: Organize forms into groups and share groups with subusers.
  name: 123FormBuilder Groups API
  slug: 123formbuilder-groups-api
- description: JWT issuance, refresh, and invalidation.
  name: 123FormBuilder Login API
  slug: 123formbuilder-login-api
- description: Manage subusers, their permissions, and master account info.
  name: 123FormBuilder Users API
  slug: 123formbuilder-users-api
arazzos:
- description: Obtain a JWT token and list the forms available to the authenticated user.
  name: 123FormBuilder Authenticate and List Forms
  slug: 123formbuilder-authenticate-and-list-forms-workflow
- description: Authenticate, list groups, read a chosen group's details, and list the forms it contains.
  name: 123FormBuilder Browse a Group's Forms
  slug: 123formbuilder-browse-group-forms-workflow
- description: Authenticate, create a group, create a form within it, then list the group's forms.
  name: 123FormBuilder Create a Form Inside a New Group
  slug: 123formbuilder-create-form-in-group-workflow
- description: Authenticate, read a form's details, enumerate its fields, and pull its submissions.
  name: 123FormBuilder Inspect a Form End to End
  slug: 123formbuilder-inspect-form-workflow
- description: Read a single submission, then update its approval and payment status.
  name: 123FormBuilder Moderate a Submission
  slug: 123formbuilder-moderate-submission-workflow
- description: List a form's submissions and, when any exist, fetch the full detail of the first one.
  name: 123FormBuilder Review a Form Submission
  slug: 123formbuilder-review-submission-workflow
artifact_total: 90
collections:
- collection_type: postman
  name: 123FormBuilder REST API v2
  slug: postman-123formbuilder-rest-api-v2
- collection_type: open
  name: 123FormBuilder REST API v2
  slug: open-123formbuilder-rest-api-v2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/123formbuilder-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/123formbuilder-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/123formbuilder-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/123formbuilder-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/123formbuilder/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/123formbuilder-authenticate-and-list-forms-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/123formbuilder-browse-group-forms-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/123formbuilder-create-form-in-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/123formbuilder-inspect-form-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/123formbuilder-moderate-submission-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/123formbuilder-review-submission-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.123formbuilder.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/123formbuilder
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/123FormBuilder/123contacform-api-v1-php
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/123FormBuilder/wix-code
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/123formbuilder
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.123formbuilder.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.123formbuilder.com/developer/api-v2/
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://www.123formbuilder.com/docs/all-categories/developers/
- group: start
  title: ''
  type: Signup
  url: https://www.123formbuilder.com/sign-up/
- group: start
  title: ''
  type: Login
  url: https://www.123formbuilder.com/login/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.123formbuilder.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/123formbuilder-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.123formbuilder.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.123formbuilder.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.123formbuilder.com/gdpr-compliance/
- group: company
  title: ''
  type: Blog
  url: https://www.123formbuilder.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.123formbuilder.com/contact-us/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/123formbuilder-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/123formbuilder-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/123formbuilder-vocabulary.yaml
created: '2026-05-11'
description: 123FormBuilder is an online form, survey, and workflow builder used to collect, route, and integrate submission data across websites, customer portals, and back-office systems with no-code design and HIPAA-ready configurations. The 123FormBuilder REST API v2 enables programmatic access to forms, fields, submissions, groups, users, and accounts. Clients authenticate by exchanging credentials at POST /token for a JWT and pass the token as a query parameter on subsequent requests. Separate US and EU regional base URLs are provided.
examples:
- key_count: 6
  name: 123Formbuilder Rest Api V2 Account Example
  slug: 123formbuilder-rest-api-v2-account-example
- key_count: 8
  name: 123Formbuilder Rest Api V2 Field Example
  slug: 123formbuilder-rest-api-v2-field-example
- key_count: 11
  name: 123Formbuilder Rest Api V2 Form Example
  slug: 123formbuilder-rest-api-v2-form-example
- key_count: 6
  name: 123Formbuilder Rest Api V2 Group Example
  slug: 123formbuilder-rest-api-v2-group-example
- key_count: 8
  name: 123Formbuilder Rest Api V2 Submission Example
  slug: 123formbuilder-rest-api-v2-submission-example
- key_count: 2
  name: 123Formbuilder Rest Api V2 Token Example
  slug: 123formbuilder-rest-api-v2-token-example
- key_count: 10
  name: 123Formbuilder Rest Api V2 User Example
  slug: 123formbuilder-rest-api-v2-user-example
features:
- description: Drag-and-drop builder with 25+ field types including signature, file upload, formula, and product fields.
  name: No-Code Form Authoring
- description: Break long surveys into multiple pages with conditional logic to control flow.
  name: Multi-Page Forms
- description: Show, hide, or branch fields based on respondent answers.
  name: Conditional Logic
- description: Forward submissions to external endpoints via group-level webhook URLs (max 10 per form).
  name: Webhooks
- description: Manually review and approve submissions before they continue downstream.
  name: Submission Approvals
- description: Diamond and Enterprise tiers offer HIPAA-eligible form configurations for healthcare data collection.
  name: HIPAA-Ready Configurations
- description: Built-in consent fields, data retention controls, and EU regional residency.
  name: GDPR Controls
- description: Separate US (api.123formbuilder.com) and EU (eu-api.123formbuilder.com) base URLs.
  name: Regional Endpoints
- description: Granular per-subuser flags for create/duplicate/delete form, manage groups, and manage users.
  name: Subuser Permissions
- description: Custom form domains, branding removal, and theme editing on Diamond and Enterprise.
  name: White Label
- description: Publish forms in multiple languages from a single source.
  name: Multi-Language Forms
- description: Integrate PayPal, Stripe, Square, Authorize.Net, Braintree, and PayU as form fields.
  name: Payment Collection
finops:
- name: 123Formbuilder Finops
  service_category: SaaS / Online Forms
  slug: 123formbuilder-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/123formbuilder.png
integrations:
- description: Deep Salesforce Cloud integration on Platinum and above.
  name: Salesforce
- description: Sync form submissions to HubSpot CRM contacts and deals.
  name: HubSpot
- description: Add submitters to Mailchimp audiences and trigger automation flows.
  name: Mailchimp
- description: Push contacts and tags into ActiveCampaign for lifecycle marketing.
  name: ActiveCampaign
- description: Sync submissions to Campaign Monitor subscribers.
  name: Campaign Monitor
- description: Collect payments on payment-enabled forms via PayPal.
  name: PayPal
- description: Accept Stripe payments and charge cards from form submissions.
  name: Stripe
- description: Process payments via Square gateway.
  name: Square
- description: Accept Authorize.Net credit card payments.
  name: Authorize.Net
- description: Collect payments via Braintree.
  name: Braintree
- description: Accept PayU payments for global reach.
  name: PayU
- description: Connect to 4,000+ apps via Zapier triggers and actions.
  name: Zapier
- description: Generic webhook URLs registered at the group level for custom downstream processing.
  name: Webhooks
- description: Push leads into Marketo for marketing automation.
  name: Marketo
- description: Mirror form submissions into Google Sheets for analysis.
  name: Google Sheets
- description: Route file upload submissions to Dropbox folders.
  name: Dropbox
- description: Capture form responses as Evernote notes.
  name: Evernote
- description: Sync submissions to Smartsheet rows.
  name: Smartsheet
- description: Create Pipedrive deals from form responses.
  name: Pipedrive
- description: Open Zendesk tickets from form submissions.
  name: Zendesk
- description: Push submissions into Wix Code databases (see github.com/123FormBuilder/wix-code).
  name: Wix
- description: Sync contacts and orders to Shopify.
  name: Shopify
- description: Sync supporters and contacts to NationBuilder.
  name: NationBuilder
- description: Community-maintained Pipedream connector (@pipedream/a123formbuilder) for serverless workflows.
  name: Pipedream
json_schemas:
- name: Account
  property_count: 6
  slug: 123formbuilder-rest-api-v2-account
- name: Field
  property_count: 8
  slug: 123formbuilder-rest-api-v2-field
- name: Form
  property_count: 11
  slug: 123formbuilder-rest-api-v2-form
- name: Group
  property_count: 6
  slug: 123formbuilder-rest-api-v2-group
- name: Submission
  property_count: 8
  slug: 123formbuilder-rest-api-v2-submission
- name: User
  property_count: 10
  slug: 123formbuilder-rest-api-v2-user
json_structures:
- name: 123Formbuilder Rest Api V2 Account Structure
  property_count: 6
  slug: 123formbuilder-rest-api-v2-account-structure
- name: 123Formbuilder Rest Api V2 Field Structure
  property_count: 7
  slug: 123formbuilder-rest-api-v2-field-structure
- name: 123Formbuilder Rest Api V2 Form Structure
  property_count: 11
  slug: 123formbuilder-rest-api-v2-form-structure
- name: 123Formbuilder Rest Api V2 Group Structure
  property_count: 6
  slug: 123formbuilder-rest-api-v2-group-structure
- name: 123Formbuilder Rest Api V2 Submission Structure
  property_count: 8
  slug: 123formbuilder-rest-api-v2-submission-structure
- name: 123Formbuilder Rest Api V2 User Structure
  property_count: 10
  slug: 123formbuilder-rest-api-v2-user-structure
jsonld:
- class_count: 6
  name: 123Formbuilder Context
  property_count: 37
  slug: 123formbuilder-context
layout: provider
modified: '2026-05-28'
name: 123FormBuilder
nav: Providers
network: true
overview: '123FormBuilder publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Forms API, Groups API, and 2 more. Tagged areas include Online Forms, Form Builder, Surveys, Workflow, and Data Collection.


  The 123FormBuilder catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  123FormBuilder''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, support, and 25 more developer resources.'
plans:
- name: 123Formbuilder Plans Pricing
  plan_count: 5
  slug: 123formbuilder-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 7
  name: 123Formbuilder Rate Limits
  slug: 123formbuilder-rate-limits
rules:
- name: 123FormBuilder API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: 123formbuilder-jsonschema-spectral-rules
- name: 123FormBuilder API Rules
  rule_count: 27
  severity_counts:
    error: 13
    hint: 0
    info: 0
    warn: 14
  slug: 123formbuilder-rules
score:
  band: exemplar
  composite: 72.4
  delta: 4.6
  facets:
    commercial_clarity: 92.1
    contract_quality: 79.8
    developer_ergonomics: 39.1
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 67.8
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/123formbuilder/refs/heads/main/screenshots/123formbuilder-2026-06-20T162300.png
security:
- kind: authentication
  name: 123Formbuilder Authentication
  slug: 123formbuilder-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: 123Formbuilder Domain Security
  slug: 123formbuilder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 123Formbuilder Vulnerability Disclosure
  slug: 123formbuilder-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 123formbuilder
solutions:
- description: HIPAA-ready intake, consent, and patient-survey forms on Diamond/Enterprise.
  name: Healthcare Forms (HIPAA)
- description: Quizzes, course evaluations, and admissions forms with multi-language support.
  name: Education Surveys
- description: Donation forms with payment gateway integration and donor CRM sync.
  name: Nonprofit Donations
- description: Property inquiry forms with CRM and email-marketing integration.
  name: Real Estate Lead Capture
- description: SLA-backed Enterprise tier with SSO, dedicated account manager, and Virtual Database Manager.
  name: Enterprise Workflow
tags:
- Online Forms
- Form Builder
- Surveys
- Workflow
- Data Collection
- Submissions
- Webhooks
- HIPAA
- GDPR
- Payments
use_cases:
- description: Capture leads from web forms and route them to CRMs via webhook or native integrations.
  name: Lead Capture and CRM Sync
- description: Run NPS, CSAT, and Likert-scale surveys with conditional follow-up questions.
  name: Customer Feedback and NPS
- description: Collect attendee data, accept payments, and trigger confirmation workflows.
  name: Event Registration and Payment
- description: Capture patient intake data on Diamond/Enterprise configurations with HIPAA-ready settings.
  name: HIPAA-Eligible Intake Forms
- description: Build product configurators with formula fields and route requests to sales teams.
  name: Order and Quote Requests
- description: Standardize HR intake with permission-gated subuser access to specific groups.
  name: Employee and Job Application Forms
- description: Programmatically page submissions via REST API v2 into data warehouses and BI tools.
  name: Survey Data Pipelines
website: https://www.123formbuilder.com
---

---
access_model:
  confidence: high
  label: Self-serve signup, 14-day free trial
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://encharge.io/pricing
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Encharge Agentic Access
  operation_count: 69
  slug: encharge-agentic-access
  summary_line: 69 operations · 43 acting
api_count: 1
apis:
- description: REST API for sending transactional emails through Encharge. Accepts JSON at POST /v1/emails/send with exactly one of template, html or text, returns 202 Accepted, and authenticates via the same accoun
  name: Encharge Transactional Email API
  slug: transactional-email-api
- description: Single-endpoint Ingest API for creating/updating people and submitting product events into Encharge from an application backend. POSTs JSON to https://ingest.encharge.io/v1/ with the account write key
  name: Encharge Ingest API
  slug: ingest-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Account API from Encharge — 2 operation(s) for account information.
  name: Encharge Account API
  phrasing_intents:
  - id: GetInfo
    intent: Get my account information
    question: How do I see the details of my Encharge account?
  - id: GetAccountInfoByFormId
    intent: Look up public account info for a form
    question: Can I find out which account owns a signup form without authenticating?
  phrasing_ops: 2
  slug: encharge-account-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Broadcasts API from Encharge — 1 operation(s) for sending broadcasts.
  name: Encharge Broadcasts API
  phrasing_intents:
  - id: SendBroadcast
    intent: Confirm a broadcast for sending
    question: How do I mark a broadcast as ready to go out?
  phrasing_ops: 1
  slug: encharge-broadcasts-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Custom Objects Schema API from Encharge — 10 operation(s) for defining object types, their fields, and the associations between them.
  name: Encharge Custom Objects Schema API
  phrasing_intents:
  - id: GetCustomObjectsSchema
    intent: List custom object definitions
    question: What custom object types are defined in my account?
  - id: CreateCustomObjectSchema
    intent: Define a new custom object type
    question: How do I create a new custom object type like Invoices?
  - id: GetCustomObjectSchema
    intent: Get a custom object definition
    question: How do I see how a custom object type is defined?
  - id: UpdateCustomObjectSchema
    intent: Update a custom object definition
    question: How do I change which fields are searchable on a custom object?
  - id: DeleteCustomObjectSchema
    intent: Delete a custom object type and its data
    question: How do I remove a custom object type I no longer need?
  - id: CreateObjectFields
    intent: Add fields to a custom object
    question: How do I add new fields to a custom object type?
  - id: EditObjectField
    intent: Edit a field on a custom object
    question: How do I change the label or tooltip of a custom object field?
  - id: DeleteObjectField
    intent: Delete a field from a custom object
    question: How do I remove a field from a custom object type?
  phrasing_ops: 10
  slug: encharge-customobjectsschema-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Folders API from Encharge — 2 operation(s) for organizing assets into folders.
  name: Encharge Folders API
  phrasing_intents:
  - id: CreateFolder
    intent: Create a folder
    question: How do I create a folder to organize my items?
  - id: EditFolder
    intent: Edit a folder
    question: How do I change an existing folder?
  phrasing_ops: 2
  slug: encharge-folders-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The People API from Encharge — 5 operation(s) for creating, updating, reading, unsubscribing and archiving people.
  name: Encharge People API
  phrasing_intents:
  - id: ArchivePeople
    intent: Archive or delete people
    question: How do I archive contacts I no longer want to email?
  - id: GetSpecificPeople
    intent: Look up specific people
    question: How do I look up a contact by email?
  - id: CreateUpdatePeople
    intent: Create or update people
    question: How do I add new contacts or update existing ones in one call?
  - id: GetAllPeople
    intent: List all people in the account
    question: How do I export every contact in my account?
  - id: UnsubscribePerson
    intent: Unsubscribe a person from email
    question: How do I stop a contact from getting any more emails?
  phrasing_ops: 5
  slug: encharge-people-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Person Fields API from Encharge — 4 operation(s) for managing person fields.
  name: Encharge Person Fields API
  phrasing_intents:
  - id: GetFields
    intent: List person fields
    question: What person fields exist in my account?
  - id: CreateFields
    intent: Create person fields
    question: How do I add a new custom field to my contacts?
  - id: EditField
    intent: Modify a person field
    question: How do I change the type or format of a contact field?
  - id: DeleteField
    intent: Delete a person field
    question: How do I remove a custom field from my contacts?
  phrasing_ops: 4
  slug: encharge-personfields-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Segments API from Encharge — 4 operation(s) for dynamic segments.
  name: Encharge Segments API
  phrasing_intents:
  - id: GetSegments
    intent: List dynamic segments
    question: What segments have I set up?
  - id: CreateSegment
    intent: Create a dynamic segment
    question: How do I create a segment of contacts that match certain conditions?
  - id: GetPeopleInSegment
    intent: List people in a segment
    question: How do I get the contacts who are in a specific segment?
  - id: ModifySegment
    intent: Modify a dynamic segment
    question: How do I change the conditions of an existing segment?
  phrasing_ops: 4
  slug: encharge-segments-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The email settings API from Encharge — 5 operation(s) for adding and verifying sending domains.
  name: Encharge Email Domain Settings API
  phrasing_intents:
  - id: GetDomains
    intent: List email sending domains
    question: Which email domains have I added for sending?
  - id: CreateDomain
    intent: Add an email domain for verification
    question: How do I add my own domain to send email from?
  - id: GetDomain
    intent: Get an email domain
    question: How do I check the details of one sending domain?
  - id: DeleteDomain
    intent: Remove an email domain
    question: How do I remove a sending domain from my account?
  - id: VerifyDomain
    intent: Re-check an email domain's DNS
    question: I've added the DNS records, how do I trigger the domain check?
  phrasing_ops: 5
  slug: encharge-settings-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Tags API from Encharge — 2 operation(s) for tagging and untagging people.
  name: Encharge Tags API
  phrasing_intents:
  - id: AddTag
    intent: Tag a person
    question: How do I add a tag to a contact?
  - id: RemoveTag
    intent: Remove a tag from a person
    question: How do I take a tag off a contact?
  phrasing_ops: 2
  slug: encharge-tags-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Tags Management API from Encharge — 5 operation(s) for the account tag registry and tag counts.
  name: Encharge Tags Management API
  phrasing_intents:
  - id: GetAccountTags
    intent: List all tags in the account
    question: What tags exist in my account?
  - id: CreateAccountTags
    intent: Create new tags
    question: How do I create tags before applying them to anyone?
  - id: GetTagCounts
    intent: Get tags with people counts
    question: How many people have each tag?
  - id: UpdateAccountTag
    intent: Rename or update a tag
    question: How do I rename a tag across all flows and segments?
  - id: DeleteAccountTag
    intent: Delete a tag from the account
    question: How do I delete a tag everywhere in my account?
  phrasing_ops: 5
  slug: encharge-tags-management-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Webhooks API from Encharge — 2 operation(s) for creating and deleting event subscriptions against Encharge's event catalog.
  name: Encharge Webhooks API
  phrasing_intents:
  - id: CreateWebhook
    intent: Subscribe a webhook to events
    question: How do I get notified at my URL when something happens in Encharge?
  - id: DeleteWebhook
    intent: Delete a webhook subscription
    question: How do I stop sending events to a webhook?
  phrasing_ops: 2
  slug: encharge-webhooks-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Custom Objects API from Encharge — 11 operation(s) for custom objects.
  name: Encharge Custom Objects API
  phrasing_intents:
  - id: GetCustomObjects
    intent: List records of a custom object
    question: How do I list all my company records?
  - id: CreateCustomObjects
    intent: Create new custom object records
    question: How do I add brand-new company records?
  - id: CreateOrUpdateCustomObjects
    intent: Upsert a custom object record
    question: How do I create a company record or update it if it already exists?
  - id: GetCustomObjectsInSegment
    intent: List custom object records in a segment
    question: How do I see which companies fall into a particular segment?
  - id: GetCustomObjectsCount
    intent: Count records of a custom object
    question: How many company records do I have in total?
  - id: GetCustomObjectsInSegmentCount
    intent: Count custom object records in a segment
    question: How many companies are in a given segment?
  - id: SearchCustomObjects
    intent: Search custom object records
    question: How do I search my company records by name?
  - id: GetCustomObjectById
    intent: Get a custom object record by ID
    question: How do I fetch one company record by its Encharge ID?
  phrasing_ops: 18
  slug: encharge-custom-objects-api
- baseURL: https://api.encharge.io/v1
  baseurl_source: declared
  description: The Email Templates API from Encharge — 7 operation(s) for email templates.
  name: Encharge Email Templates API
  phrasing_intents:
  - id: GetEmail
    intent: Get an email template
    question: How do I fetch an email template's content and settings?
  - id: ModifyEmail
    intent: Modify an email template
    question: How do I change the subject line of an existing email template?
  - id: DeleteEmail
    intent: Delete an email template
    question: How do I delete an email template I don't use anymore?
  - id: CreateEmail
    intent: Create an email template
    question: How do I create a new email template with HTML content?
  - id: GetEmailVersions
    intent: List an email template's version history
    question: How do I see the past versions of an email template?
  - id: GetEmailVersion
    intent: Get a specific email template version
    question: How do I view what an email template looked like in an earlier version?
  - id: GetSelectedEmailVersion
    intent: Get the currently selected template version
    question: Which version of an email template is currently selected?
  - id: UpdateLatestEmailVersion
    intent: Update the latest version of a template
    question: How do I edit the newest version of an email template's HTML?
  phrasing_ops: 9
  slug: encharge-email-templates-api
artifact_total: 40
asyncapis:
- description: ''
  name: Encharge Webhooks
  slug: encharge-webhooks
collections:
- collection_type: open
  name: Encharge REST Account API
  slug: open-encharge-account-api
- collection_type: open
  name: Encharge REST Account Events API
  slug: open-encharge-events-api
- collection_type: open
  name: Encharge REST Account Fields API
  slug: open-encharge-fields-api
- collection_type: open
  name: Encharge REST Account Ingest API
  slug: open-encharge-ingest-api
- collection_type: open
  name: Encharge REST Account People API
  slug: open-encharge-people-api
- collection_type: open
  name: Encharge REST Account Segments API
  slug: open-encharge-segments-api
- collection_type: open
  name: Encharge REST Account Tags API
  slug: open-encharge-tags-api
- collection_type: open
  name: Encharge REST Account Transactional Email API
  slug: open-encharge-transactional-email-api
- collection_type: open
  name: Encharge REST API
  slug: open-encharge
common:
- group: other
  href: https://artifacts.apis.io/encharge/capabilities/encharge-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/encharge-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/encharge/scopes/encharge-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/encharge-scopes.yml
- group: agent
  href: https://artifacts.apis.io/encharge/agentic-access/encharge-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/encharge-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/encharge/security/encharge-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/encharge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://encharge.io/responsible-disclosure/
- group: auth
  href: https://artifacts.apis.io/encharge/security/encharge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/encharge-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/encharge/security/encharge-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/encharge-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://gdpr.encharge.io/
- group: auth
  href: https://artifacts.apis.io/encharge/authentication/encharge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/encharge-authentication.yml
- group: design
  href: https://artifacts.apis.io/encharge/conventions/encharge-conventions.yml
  title: ''
  type: Conventions
  url: conventions/encharge-conventions.yml
- group: design
  href: https://artifacts.apis.io/encharge/errors/encharge-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/encharge-problem-types.yml
- group: design
  href: https://artifacts.apis.io/encharge/lifecycle/encharge-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/encharge-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/encharge/conformance/encharge-conformance.yml
  title: ''
  type: Conformance
  url: conformance/encharge-conformance.yml
- group: design
  href: https://artifacts.apis.io/encharge/data-model/encharge-data-model.yml
  title: ''
  type: DataModel
  url: data-model/encharge-data-model.yml
- group: design
  href: https://artifacts.apis.io/encharge/components/encharge-components.yml
  title: ''
  type: Components
  url: components/encharge-components.yml
- group: build
  href: https://artifacts.apis.io/encharge/packages/encharge-packages.yml
  title: ''
  type: Packages
  url: packages/encharge-packages.yml
- group: agent
  href: https://artifacts.apis.io/encharge/well-known/encharge-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/encharge-well-known.yml
- group: commercial
  href: https://artifacts.apis.io/encharge/plans/encharge-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/encharge-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/encharge/rate-limits/encharge-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/encharge-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/encharge/changelog/encharge-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/encharge-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://encharge.noorahq.com/changelog
- group: operate
  title: ''
  type: Roadmap
  url: https://encharge.noorahq.com/roadmap
- group: design
  href: https://artifacts.apis.io/encharge/asyncapi/encharge-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/encharge-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/encharge/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/encharge/overlays/encharge-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/encharge-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/encharge/llms/encharge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/encharge-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.encharge.io/llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/encharge
- group: company
  title: ''
  type: Website
  url: https://encharge.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.encharge.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.encharge.io
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.encharge.io/api-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://app-encharge-resources.s3.amazonaws.com/redoc.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.encharge.io/getting-started/connecting-your-app-to-encharge
- group: operate
  title: ''
  type: Support
  url: https://help.encharge.io
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/460427/TVRj5o3E
- group: commercial
  title: ''
  type: Pricing
  url: https://encharge.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.encharge.io/signup
- group: start
  title: ''
  type: Signup
  url: https://app.encharge.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://encharge.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://encharge.io/privacy-policy/
- group: build
  title: ''
  type: API Integration
  url: https://encharge.io/integrations/api/
- group: company
  title: ''
  type: Blog
  url: https://encharge.io/feed/
created: '2026-05-11'
description: 'Encharge is a behavior-based marketing automation platform built for SaaS companies, with a visual flow builder, broadcasts, segments, lead scoring, A/B testing, native forms, custom objects, and 50+ native integrations (HubSpot, Stripe, Salesforce, Segment, Facebook Ads, and more). The platform combines email marketing automation, user profiles, and product-event tracking to send targeted emails based on what users do (or do not do) in a SaaS product. Encharge exposes three developer surfaces: a REST API of 69 operations covering people, person fields, segments, tags, broadcasts, email templates, sending domains, custom objects and event subscriptions, described by a published OpenAPI 3.0 definition; a prose-documented Transactional Email API; and an Ingest API for streaming people and product events from a backend. All three authenticate with the same account token, passed in the X-Encharge-Token header or a token query parameter, with OAuth 2 available for partner apps.'
finops:
- has_sources: true
  method: derived
  name: Encharge Finops
  primary_unit: up to 2,000 subscribers
  service_category: ''
  slug: encharge-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encharge.png
layout: provider
modified: '2026-08-13'
name: Encharge
nav: Providers
network: true
overview: 'Encharge publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Transactional Email API, Ingest API, Account API, and 12 more. Tagged areas include Email Marketing, Marketing Automation, Transactional Email, Software-as-a-Service, and Behavioral Email.


  The Encharge catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Encharge''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, pricing, and 36 more developer resources.'
plans:
- name: Encharge Plans Pricing
  plan_count: 5
  slug: encharge-plans-pricing
- name: Encharge Price Estimates
  plan_count: 0
  slug: encharge-price-estimates
random_paper: 13
rate_limits:
- limit_count: 0
  name: Encharge Rate Limits
  slug: encharge-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Encharge API Rules
  rule_count: 66
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 7
  slug: encharge-rules
scopes:
- name: Encharge Scopes
  scope_count: 8
  slug: encharge-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: exemplar
  composite: 71.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 57.3
    developer_ergonomics: 61.3
    discoverability: 73.2
    operational_transparency: 34.2
  previous_composite: 70.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://apis.io/screenshots/encharge/encharge-2026-06-20T180652.png
security:
- kind: authentication
  name: Encharge Authentication
  slug: encharge-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Encharge Domain Security
  slug: encharge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Encharge Vulnerability Disclosure
  slug: encharge-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Encharge Trust Center
  slug: encharge-trust-center
  summary_line: GDPR
skill_count: 4
skills:
- name: Model and populate Encharge custom objects
  slug: encharge-model-custom-objects
- name: Send a transactional email through Encharge
  slug: encharge-send-transactional-email
- name: Subscribe to Encharge events with webhooks
  slug: encharge-subscribe-to-events
- name: Sync people and tags into Encharge
  slug: encharge-sync-people-and-tags
slug: encharge
tags:
- Email Marketing
- Marketing Automation
- Transactional Email
- Software-as-a-Service
- Behavioral Email
- Customer Engagement
- Customer Data
- Webhook
website: https://encharge.io
---

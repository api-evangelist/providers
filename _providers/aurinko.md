---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 70
  human_in_the_loop: 1
  name: Aurinko Agentic Access
  operation_count: 134
  slug: aurinko-agentic-access
  summary_line: 134 operations · 70 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: An account corresponds to an email address, mailbox, and/or calendar. When connecting to the Aurinko API, a specific access token gives you access to a specific account’s data.
  name: Yoxel Account API
  slug: aurinko-account-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: These endpoints allow for account management outside the developer console interface. You can list, cancel, update, and delete accounts associated with your application.
  name: Yoxel Accounts API
  slug: aurinko-accounts-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Aurinko's Unified OAuth Flows are backed by providers’ OAuth2 flows (i.e. Google, Office 365, Salesforce, HubSpot,...) or by secure password-based authentications (i.e. MS Exchange, IMAP accounts). Th
  name: Yoxel Auth API
  slug: aurinko-auth-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: See meeting time availability according to the group booking profile configuration. Book a meeting for an account or one of users in a group.
  name: Yoxel Availability API
  slug: aurinko-availability-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Booking profiles allow you to build calendar availability and meeting scheduling apps. List, create, update, and delete booking profiles associated with a calendar (Aurinko account). Gather availabili
  name: Yoxel Booking API
  slug: aurinko-booking-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Each account connected to Aurino can have zero or more calendars, and each calendar has a collection of individual events.
  name: Yoxel Calendars API
  slug: aurinko-calendars-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Sync/delta methods.
  name: Yoxel Cal Sync API
  slug: aurinko-calsync-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Contacts are objects within an address book, containing several pieces of information, such as email addresses, phone numbers, postal addresses, work place details.
  name: Yoxel Contacts API
  slug: aurinko-contacts-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Sync/delta methods.
  name: Yoxel Cont Sync API
  slug: aurinko-contsync-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: A draft message is a message which has not been sent yet. The drafts endpoints let you create new drafts, read existing drafts, and send drafts.
  name: Yoxel Drafts API
  slug: aurinko-drafts-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: List email folders, their attributes, and messages.
  name: Yoxel Email Folders API
  slug: aurinko-emailfolders-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Sync/delta methods.
  name: Yoxel Email Sync API
  slug: aurinko-emailsync-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Track email opens.
  name: Yoxel Email Tracking API
  slug: aurinko-emailtracking-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Events are objects within a calendar, generally supporting all features of modern scheduling apps. Using the calendar APIs, your application can schedule events, send meeting invitations, RSVP, and mo
  name: Yoxel Events API
  slug: aurinko-events-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: 'Follow-up rules allow you to define automatic email follow-up (drip) sequences and email templates. List, create, update, and delete follow-up rules associated with a mailbox account. Check status of '
  name: Yoxel Follow Up Robot API
  slug: aurinko-followuprobot-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Check free/busy status for a calendar or available time slots for a meeting in multiple calendars.
  name: Yoxel Free Busy Schedule API
  slug: aurinko-freebusyschedule-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Group Booking profiles allow you to build calendar availability and meeting scheduling for a group of accounts. List, create, update, and delete booking profiles associated with a group. Gather availa
  name: Yoxel Group Booking API
  slug: aurinko-groupbooking-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Manage accounts rely on service accounts for their connections. List, cancel, update, and delete managed accounts associated with service accounts.
  name: Yoxel Managed accounts API
  slug: aurinko-managed-accounts-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Messages contain several pieces of information, such as when a message was sent, the sender's address, to whom it was sent, and the message body. They can also contain files (attachments), calendar ev
  name: Yoxel Messages API
  slug: aurinko-messages-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Service accounts represent admin/service/organization level connections. List, cancel, update, and delete service accounts associated with your application.
  name: Yoxel Services API
  slug: aurinko-services-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: TaskLists a container objects for tasks.
  name: Yoxel Task Lists API
  slug: aurinko-tasklists-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Tasks a work to be done.
  name: Yoxel Tasks API
  slug: aurinko-tasks-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Sync/delta methods.
  name: Yoxel Task Sync API
  slug: aurinko-tasksync-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: '`User` is an Aurinko managed entity that your app can leverage to implement user session management. Multiple regular Aurinko accounts can be linked to a `User` however there is always one primary acc'
  name: Yoxel User API
  slug: aurinko-user-api
- baseURL: https://api.aurinko.io
  baseurl_source: declared
  description: Webhooks allow your application to receive simple notifications when certain events occur. They essentially tell your application that it can run incremental syncs to obtain the changed records (updat
  name: Yoxel Webhooks API
  slug: aurinko-webhooks-api
artifact_total: 41
common:
- group: agent
  href: https://artifacts.apis.io/aurinko/agentic-access/aurinko-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aurinko-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aurinko/plans/aurinko-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aurinko-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aurinko/rules/aurinko-rules.yml
  title: ''
  type: Spectral
  url: rules/aurinko-rules.yml
- group: design
  href: https://artifacts.apis.io/aurinko/json-ld/aurinko-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aurinko-context.jsonld
- group: design
  href: https://artifacts.apis.io/aurinko/vocabulary/aurinko-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aurinko-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aurinko/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aurinko/data-model/aurinko-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aurinko-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aurinko/authentication/aurinko-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aurinko-authentication.yml
- group: design
  href: https://artifacts.apis.io/aurinko/errors/aurinko-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aurinko-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aurinko/conformance/aurinko-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aurinko-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aurinko/llms/aurinko-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aurinko-llms.txt
- group: agent
  href: https://artifacts.apis.io/aurinko/well-known/aurinko-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aurinko-well-known.yml
- group: other
  href: https://artifacts.apis.io/aurinko/hosts/aurinko-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aurinko-hosts.yml
- group: other
  href: https://artifacts.apis.io/aurinko/vendors/aurinko-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aurinko-vendors.yml
- group: build
  href: https://artifacts.apis.io/aurinko/packages/aurinko-packages.yml
  title: ''
  type: SDKs
  url: packages/aurinko-packages.yml
- group: build
  href: https://artifacts.apis.io/aurinko/packages/aurinko-packages.yml
  title: ''
  type: Packages
  url: packages/aurinko-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aurinko.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aurinko.io/privacy-policy
- group: docs
  title: ''
  type: APIReference
  url: https://apirefs.aurinko.io/
- group: auth
  href: https://artifacts.apis.io/aurinko/security/aurinko-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aurinko-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aurinko.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aurinko.io/
- group: company
  title: ''
  type: Blog
  url: https://www.aurinko.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aurinko.io/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aurinko.io/unified-api/
created: '2026-10-19'
description: Aurinko provides a unified API platform that integrates email, calendar, contacts, and tasks across major services. Their solution enables developers to streamline inbox integration, automate workflows, and enhance productivity for enterprises. With a free trial and trusted by leading companies, Aurinko aims to simplify communication management through a single, consistent API layer, reducing development overhead and improving user experience.
image: https://www.aurinko.io/images/image-logo.png
json_schemas:
- name: BookingInDto
  property_count: 14
  slug: aurinko-booking-in-dto
- name: BookingOutDto
  property_count: 15
  slug: aurinko-booking-out-dto
- name: EmailMessage
  property_count: 30
  slug: aurinko-email-message
- name: GroupBookingInDto
  property_count: 15
  slug: aurinko-group-booking-in-dto
- name: GroupBookingOutDto
  property_count: 16
  slug: aurinko-group-booking-out-dto
- name: GroupBookingUpdateDto
  property_count: 15
  slug: aurinko-group-booking-update-dto
jsonld:
- class_count: 120
  name: Aurinko Context
  property_count: 272
  slug: aurinko-context
layout: provider
modified: '2026-10-19'
name: Yoxel
nav: Providers
network: true
overview: 'Yoxel publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Accounts API, Auth API, and 22 more. Tagged areas include Company, Integration, Email, Calendar, and Contacts.


  The Yoxel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Yoxel''s developer surface includes authentication, API reference, documentation, engineering blog, pricing, getting-started guide, and 19 more developer resources.'
plans:
- name: Aurinko Plans Pricing
  plan_count: 6
  slug: aurinko-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Yoxel API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: aurinko-rules
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 61.3
    developer_ergonomics: 51.8
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aurinko Authentication
  slug: aurinko-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aurinko Domain Security
  slug: aurinko-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 4
skills:
- name: aurinko-create-meeting
  slug: aurinko-create-meeting
- name: aurinko-manage-contact
  slug: aurinko-manage-contact
- name: aurinko-manage-webhook-subscriptions
  slug: aurinko-manage-webhook-subscriptions
- name: aurinko-upsert-and-get-account
  slug: aurinko-upsert-and-get-account
slug: aurinko
tags:
- Company
- Integration
- Email
- Calendar
- Contacts
- Task
website: https://www.aurinko.io/
---

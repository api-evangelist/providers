---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 143
  human_in_the_loop: 4
  name: Clio Agentic Access
  operation_count: 286
  slug: clio-agentic-access
  summary_line: 286 operations · 143 acting · 4 human-in-the-loop
api_count: 85
apis:
- description: Clio Webhooks deliver near real-time notifications when matters, contacts, activities, tasks, calendar entries, bills, and other Clio resources are created, updated, or deleted. Subscriptions are mana
  name: Clio Webhooks
  slug: webhooks
- description: The Clio App Directory is the integration marketplace for certified third-party apps that connect to Clio Manage. Apps listed in the directory are reviewed by Clio's developer partnerships team and ma
  name: Clio App Directory
  slug: app-directory
- description: Activities (Time Entries and Expense Entries) track work done at a firm. Activities are recorded in Clio and then posted on bills to clients. Time Entries can be either be hourly-billable or flat-rate
  name: Clio Activities API
  slug: clio-activities-api
- description: Activity Descriptions are custom Time Entry templates. Activity Descriptions help firms expedite their process for recording Time Entries, and ensure that their Time Entry descriptions are consistent.
  name: Clio Activity Descriptions API
  slug: clio-activity-descriptions-api
- description: The Activity Rates API from Clio — 2 operation(s) for activity rates.
  name: Clio Activity Rates API
  slug: clio-activity-rates-api
- description: Once a [Payment](https://help.clio.com/hc/articles/9285641955355-Record-Edit-and-Delete-Payments) or [Credit Note](https://help.clio.com/hc/en-us/articles/9285299888539-Credit-Notes) has been recorded
  name: Clio Allocations API
  slug: clio-allocations-api
- description: These accounts are meant to mirror the firm’s accounts at their financial institution. Users can add a bank account to Clio to use with [Clio Payments](https://help.clio.com/hc/articles/9285631748507-
  name: Clio Bank Accounts API
  slug: clio-bank-accounts-api
- description: The Bank Transactions API from Clio — 2 operation(s) for bank transactions.
  name: Clio Bank Transactions API
  slug: clio-bank-transactions-api
- description: The Bank Transfers API from Clio — 1 operation(s) for bank transfers.
  name: Clio Bank Transfers API
  slug: clio-bank-transfers-api
- description: The Bill Themes API from Clio — 2 operation(s) for bill themes.
  name: Clio Bill Themes API
  slug: clio-bill-themes-api
- description: Users can view all Billable Clients, or clients with outstanding [Bills](https://help.clio.com/hc/en-us/articles/9285169278747-Generate-Bills), on the Billable Clients page, located under the Bills ta
  name: Clio Billable Clients API
  slug: clio-billable-clients-api
- description: Users can see all [Matters with outstanding bills](https://help.clio.com/hc/en-us/articles/9286116462747#filter-matters-clio-manage-0-0) attached to them by filtering out all non-billable Matters unde
  name: Clio Billable Matters API
  slug: clio-billable-matters-api
- description: The Billing Settings API from Clio — 1 operation(s) for billing settings.
  name: Clio Billing Settings API
  slug: clio-billing-settings-api
- description: Bills are statements of what a user’s client owes for their services over a particular billing period, including legal fees, expenses, and taxes. Users customize, preview, edit, and approve bills befo
  name: Clio Bills API
  slug: clio-bills-api
- description: Calendar Entries are used to track appointments or deadlines. Users can view Calendar Entries on any Calendar that they have “Viewer” or “Editor” permission for. Users can create Calendar Entries on a
  name: Clio Calendar Entries API
  slug: clio-calendar-entries-api
- description: The Calendar Entry Event Types API from Clio — 2 operation(s) for calendar entry event types.
  name: Clio Calendar Entry Event Types API
  slug: clio-calendar-entry-event-types-api
- description: The Calendar Visibilities API from Clio — 2 operation(s) for calendar visibilities.
  name: Clio Calendar Visibilities API
  slug: clio-calendar-visibilities-api
- description: Calendars contain Calendar Entries. All Clio accounts contain one firm Calendar ("AccountCalendar"), personal Calendars for each user ("UserCalendar"), and any number of manually created Calendars ("A
  name: Clio Calendars API
  slug: clio-calendars-api
- description: This endpoint provides the Legal Aid civil certificated rates, which are the prescribed reimbursement rates for legal services provided under the Legal Aid Scheme. [Support Link](https://help.clio.com
  name: Clio Civil Certificated Rates API
  slug: clio-civil-certificated-rates-api
- description: This endpoint provides the Legal Aid civil controlled rates, which are the prescribed reimbursement rates for legal services provided under the Legal Aid Scheme. [Support Link](https://help.clio.com/h
  name: Clio Civil Controlled Rates API
  slug: clio-civil-controlled-rates-api
- description: The Clients API from Clio — 1 operation(s) for clients.
  name: Clio Clients API
  slug: clio-clients-api
- description: The Clio Payments Links API from Clio — 2 operation(s) for clio payments links.
  name: Clio Clio Payments Links API
  slug: clio-clio-payments-links-api
- description: Payments allow users to record that funds (from checks, cash, credit cards, etc.) have been transferred from a client to the firm. In order to pay Bills, Payments must be [allocated](https://help.clio
  name: Clio Clio Payments Payments API
  slug: clio-clio-payments-payments-api
- description: Comments are short text messages which can be associated with either Documents or Folders. If the Comment is created in association with a Document, it will also be associated with the Document's late
  name: Clio Comments API
  slug: clio-comments-api
- description: Users can view all logged phone calls and emails under the Communications tab in Clio. This is also where they can use [Clio internal messages](https://help.clio.com/hc/en-us/articles/9125264015259-In
  name: Clio Communications API
  slug: clio-communications-api
- description: All clients, prospective clients, companies, and external co-counsels can be viewed as Contacts under the Contacts tab in Clio Manage. [Support Link](https://help.clio.com/hc/en-us/articles/9290486281
  name: Clio Contacts API
  slug: clio-contacts-api
- description: The Conversation Messages API from Clio — 2 operation(s) for conversation messages.
  name: Clio Conversation Messages API
  slug: clio-conversation-messages-api
- description: The Conversations API from Clio — 2 operation(s) for conversations.
  name: Clio Conversations API
  slug: clio-conversations-api
- description: 'Credit Memos allow users to write off amounts that clients owe on approved Bills. They can be added in two "ways": when viewing a Bill, or when making a payment on a Bill. [Support Link](https://help.'
  name: Clio Credit Memos API
  slug: clio-credit-memos-api
- description: This endpoint provides the Legal Aid criminal controlled rates, which are the prescribed reimbursement rates for legal services provided under the Legal Aid Scheme. [Support Link](https://help.clio.co
  name: Clio Criminal Controlled Rates API
  slug: clio-criminal-controlled-rates-api
- description: The Currencies API from Clio — 1 operation(s) for currencies.
  name: Clio Currencies API
  slug: clio-currencies-api
- description: 'In Clio, applications can create custom actions in our interface. Links are unique across an application, user, location in the UI (`ui_reference`) and label. When the user clicks on a custom action, '
  name: Clio Custom Actions API
  slug: clio-custom-actions-api
- description: The Custom Field Sets API from Clio — 2 operation(s) for custom field sets.
  name: Clio Custom Field Sets API
  slug: clio-custom-field-sets-api
- description: The Custom Fields API from Clio — 2 operation(s) for custom fields.
  name: Clio Custom Fields API
  slug: clio-custom-fields-api
- description: The Damages API from Clio — 2 operation(s) for damages.
  name: Clio Damages API
  slug: clio-damages-api
- description: The Document Archives API from Clio — 3 operation(s) for document archives.
  name: Clio Document Archives API
  slug: clio-document-archives-api
- description: Document Automation uses Document Templates to create standardized documents. Users select a Document Template (that they have created and uploaded) and a Matter to automatically create a document usi
  name: Clio Document Automations API
  slug: clio-document-automations-api
- description: Clio users can add Document Categories to their account to help organize their Documents. When a Document is uploaded or edited, a Document Category can be assigned. Users can filter by Document Categ
  name: Clio Document Categories API
  slug: clio-document-categories-api
- description: 'Document Templates are files used to create standardized documents using Clio’s Document Automation feature. Document Templates contain merge fields, which are used to pull information from Clio into '
  name: Clio Document Templates API
  slug: clio-document-templates-api
- description: Versions contain information about the version history of a document. Versioning allows users to track changes made to a document over time. [Support Link](https://help.clio.com/hc/en-us/articles/9290
  name: Clio Document Versions API
  slug: clio-document-versions-api
- description: Clio Documents are files uploaded to Clio. Files uploaded to Clio’s document integrations (e.g. Google Drive and Office365) are inaccessible through the API. [Support Link](https://help.clio.com/hc/en
  name: Clio Documents API
  slug: clio-documents-api
- description: Email Addresses are email addresses associated with a Contact. This endpoint returns all email addresses associated with a Contact.
  name: Clio Email Addresses API
  slug: clio-email-addresses-api
- description: Event metrics keep track of firm users' unread web and mobile [In-app notifications](https://help.clio.com/hc/en-us/articles/9290346939547-Set-Up-Clio-Manage#settings-0-3) and unread [Clio Internal Me
  name: Clio Event Metrics API
  slug: clio-event-metrics-api
- description: This endpoint provides the Legal Aid expense category rates, which are the prescribed reimbursement rates for legal services provided under the Legal Aid Scheme. [Support Link](https://help.clio.com/h
  name: Clio Expense Categories API
  slug: clio-expense-categories-api
- description: Files stored in Clio’s Documents section are organized in folders. Folders are automatically generated for new Contacts and Matters. Folders can also be manually created anywhere in the folder structu
  name: Clio Folders API
  slug: clio-folders-api
- description: The Grant Funding Sources API from Clio — 2 operation(s) for grant funding sources.
  name: Clio Grant Funding Sources API
  slug: clio-grant-funding-sources-api
- description: The Grants API from Clio — 2 operation(s) for grants.
  name: Clio Grants API
  slug: clio-grants-api
- description: In Clio, [permission levels](https://help.clio.com/hc/en-us/articles/9200279456667-Account-Users-and-Permissions#user-permissions-clio-manage--0-2) and [Matter permissions](https://help.clio.com/hc/en
  name: Clio Groups API
  slug: clio-groups-api
- description: The Interest Charges API from Clio — 2 operation(s) for interest charges.
  name: Clio Interest Charges API
  slug: clio-interest-charges-api
- description: There are over 1000 jurisdictions available to choose from when using Court Rules. These jurisdictions contain state, federal, appellate, and bankruptcy courts from across the United States. Jurisdict
  name: Clio Jurisdictions API
  slug: clio-jurisdictions-api
- description: Jurisdictions-to-Triggers calculates the effective dates of related court and agency rules that a lawyer must do for a Trigger. A Trigger is an activity or event which a lawyer or court does in a juri
  name: Clio Jurisdictions To Triggers API
  slug: clio-jurisdictions-to-triggers-api
- description: The Line Items API from Clio — 2 operation(s) for line items.
  name: Clio Line Items API
  slug: clio-line-items-api
- description: 'Log Entries populate the “Recents” dropdown in the header. The “Recent” section displays the ten Matters and Contacts that the user most recently accessed. When a user accesses a Contact or a Matter, '
  name: Clio Log Entries API
  slug: clio-log-entries-api
- description: All clients, prospective clients, companies, and external co-counsels can be viewed as Contacts under the Contacts tab in Clio Manage. [Support Link](https://help.clio.com/hc/en-us/articles/9290486281
  name: Clio Matter Contacts API
  slug: clio-matter-contacts-api
- description: A Matter Docket connects a Matter with a Court Rule (and all of the Calendar Entries associated with the Court Rule). Matter Dockets are viewable on the Matter Edit screen under the Court Rules headin
  name: Clio Matter Dockets API
  slug: clio-matter-dockets-api
- description: The Matter Stages API from Clio — 1 operation(s) for matter stages.
  name: Clio Matter Stages API
  slug: clio-matter-stages-api
- description: '[Matters](https://help.clio.com/hc/en-us/articles/9285920226075-Clio-Manage-Matters-Overview) in Clio represent a firm’s cases. All relevant information—Bills, Documents, Time Entries, etc.—are contai'
  name: Clio Matters API
  slug: clio-matters-api
- description: Medical Bills are a subset of Medical Records Details and can be used to keep track of documents, bill dates, and liens. Note that these endpoints only handle Updating and Destroying a record. Creatin
  name: Clio Medical Bills API
  slug: clio-medical-bills-api
- description: 'Medical Records are a subset of Medical Records Details and can be used to keep track of documents, start dates, and end dates. Note that these endpoints only handle Updating and Destroying a record. '
  name: Clio Medical Records API
  slug: clio-medical-records-api
- description: 'Medical Records Details allow you to track requests for medical records and medical bills, track treatment dates, follow up on requests, upload medical files, and track liens and outstanding balances '
  name: Clio Medical Records Details API
  slug: clio-medical-records-details-api
- description: In-app notifications are used to notify firm users of important events or changes in Clio, initiated by other firm users. These events are displayed in the **Your firm** tab of the notifications panel
  name: Clio My Events API
  slug: clio-my-events-api
- description: Notes can be added to Matters or Contacts in Clio to record meeting notes, research, or anything else a user might want. The field can hold hundreds of pages, so users can add plenty of information. N
  name: Clio Notes API
  slug: clio-notes-api
- description: The Outstanding Client Balances API from Clio — 1 operation(s) for outstanding client balances.
  name: Clio Outstanding Client Balances API
  slug: clio-outstanding-client-balances-api
- description: Phone Numbers are phone numbers associated with a Contact. This endpoint returns all phone numbers associated with a Contact.
  name: Clio Phone Numbers API
  slug: clio-phone-numbers-api
- description: The practice area field can be added to Matters and used for filtering purposes, or just for reference. Users can create their own practice areas in their [Firm Preferences settings](https://help.clio
  name: Clio Practice Areas API
  slug: clio-practice-areas-api
- description: The Related Contacts API from Clio — 1 operation(s) for related contacts.
  name: Clio Related Contacts API
  slug: clio-related-contacts-api
- description: Relationships are used on a Matter to track Contacts related to the Matter. Relationships are can be found on the Contacts sub tab of a Matter. [Support Link](https://help.clio.com/hc/en-us/articles/9
  name: Clio Relationships API
  slug: clio-relationships-api
- description: Reminders can be added to Tasks or Calendar Entries. Reminder emails can be sent by a User to themselves, other Users, Clio For Co-Counsel/Clio Connect Contacts, or [any authorized email](https://help
  name: Clio Reminders API
  slug: clio-reminders-api
- description: Report Presets can be created to streamline report generation workflow by saving report option parameters as a Preset. [Support Link](https://help.clio.com/hc/en-us/articles/9290078155803-Generate-Rep
  name: Clio Report Presets API
  slug: clio-report-presets-api
- description: Schedule report generation for an existing Report Preset using Report Schedules. A Report Schedule will generate reports from the specified Preset's report options on a daily, weekly or monthly basis.
  name: Clio Report Schedules API
  slug: clio-report-schedules-api
- description: The Reports API from Clio — 3 operation(s) for reports.
  name: Clio Reports API
  slug: clio-reports-api
- description: Service Types are used when creating new Court Rules involving the delivery of documents. In order to calculate the correct deadline to send the document, an account will specify their Service Type. C
  name: Clio Service Types API
  slug: clio-service-types-api
- description: With Task Template Lists, users can create groups of [Task Templates](https://docs.developers.clio.com/clio-manage/api-reference/#tag/Task-Templates) for the types of projects they work on most often.
  name: Clio Task Template Lists API
  slug: clio-task-template-lists-api
- description: Task Templates are the individual [Tasks](https://docs.developers.clio.com/clio-manage/api-reference/#tag/Tasks) which comprise a [Task Template List](https://docs.developers.clio.com/clio-manage/api-
  name: Clio Task Templates API
  slug: clio-task-templates-api
- description: Task Types are used to better categorize and filter tasks. This is a simple text field which is limited to 50 characters. Task Types are part of the Advanced Tasks feature which is not available to al
  name: Clio Task Types API
  slug: clio-task-types-api
- description: Tasks are used to assign and track work. Users can set priorities, due dates, and add reminders. Tasks can be assigned to firm users as well as Contacts (such as clients or co-counsel). [Support Link]
  name: Clio Tasks API
  slug: clio-tasks-api
- description: The Tax Rate Configurations API from Clio — 2 operation(s) for tax rate configurations.
  name: Clio Tax Rate Configurations API
  slug: clio-tax-rate-configurations-api
- description: 'Clio''s Text Snippets feature allows users to create a list of predefined abbreviations for commonly used phrases. For example, a user could configure their settings to have “meeting with client” show '
  name: Clio Text Snippets API
  slug: clio-text-snippets-api
- description: 'Timers are used to track time spent on billable work. They are used with hourly-billable [Time Entries](https://docs.developers.clio.com/clio-manage/api-reference/#tag/Activities). The Timer modal is '
  name: Clio Timers API
  slug: clio-timers-api
- description: The Trust Line Items API from Clio — 2 operation(s) for trust line items.
  name: Clio Trust Line Items API
  slug: clio-trust-line-items-api
- description: The Trust Requests API from Clio — 1 operation(s) for trust requests.
  name: Clio Trust Requests API
  slug: clio-trust-requests-api
- description: A User is anyone with the ability to log in to Clio. This does not include Clio for Co-Counsel/Clio Connect users. [Support Link](https://help.clio.com/hc/en-us/articles/9200279456667-Account-Users-an
  name: Clio Users API
  slug: clio-users-api
- description: '[UTBMS codes](http://utbms.com/) standardize Time and Expense entries across the legal profession. Clio users can enter their Activities using UTBMS codes in order to provide electronic invoices. [Sup'
  name: Clio Utbms Codes API
  slug: clio-utbms-codes-api
- description: '[UTBMS codes](https://docs.developers.clio.com/clio-manage/api-reference/#tag/Utbms-Codes) are divided into code sets. Each set includes Activities relevant to a certain type of law (for example, liti'
  name: Clio Utbms Sets API
  slug: clio-utbms-sets-api
- description: Webhooks are a way of detecting events in Clio without the need for polling. A webhook can be subscribed to a number of `events` on a model. Some events will be different depending on the chosen model
  name: Clio Webhooks API
  slug: clio-webhooks-api
artifact_total: 93
collections:
- collection_type: open
  name: Clio API Documentation
  slug: open-clio
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clio-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clio-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clio-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clio---cloud-based-legal-technology
- group: company
  title: ''
  type: Website
  url: https://www.clio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developers.clio.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clio.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.clio.com/sign-up
- group: start
  title: ''
  type: Portal
  url: https://docs.developers.clio.com/
- group: docs
  title: ''
  type: Reference
  url: https://docs.developers.clio.com/api-docs/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.developers.clio.com/api-docs/authorization/
- group: start
  title: ''
  type: Login
  url: https://app.clio.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.clio.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.clio.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clio.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clio.com/terms/
- group: other
  title: ''
  type: App Directory
  url: https://app.clio.com/companion
- group: build
  title: ''
  type: GitHub
  url: https://github.com/clio
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clio-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clio-rules.yml
created: '2026-05-11'
description: Clio is a cloud-based legal practice management platform used by law firms for matter management, contacts, calendaring, time and billing, trust accounting, document management, tasks, and client communications. The Clio Manage API is a REST/JSON API at app.clio.com/api/v4 that uses OAuth 2.0 (authorization code flow) for authentication and exposes the full data model behind Clio Manage, with regional endpoints for the U.S., Canada, EU/UK, and Australia. Webhooks deliver near real-time event notifications, and the Clio App Directory hosts certified third-party integrations.
graphqls:
- description: This document describes a conceptual GraphQL schema for the Clio Manage API v4. Clio is a cloud-based legal practice management platform used by law firms for matter management, contacts, calendaring,
  name: Clio GraphQL Schema
  slug: clio-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clio.png
jsonld:
- class_count: 0
  name: Clio Context
  property_count: 9
  slug: clio-context
layout: provider
modified: '2026-05-11'
name: Clio
nav: Providers
network: true
overview: 'Clio publishes 84 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Activities API, Activity Descriptions API, and 81 more. Tagged areas include Billing, Calendaring, Document Management, Law Firms, and Legal.


  The Clio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clio''s developer surface includes documentation, pricing, signup flow, developer portal, authentication, support, engineering blog, and 15 more developer resources.'
random_paper: 43
rules:
- name: Clio API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: clio-rules
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 74.8
    developer_ergonomics: 41.3
    discoverability: 50.0
    governance: 27.1
    operational_transparency: 21.1
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 83
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clio/refs/heads/main/screenshots/clio-2026-06-20T174526.png
security:
- kind: domain-security
  name: Clio Domain Security
  slug: clio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clio Vulnerability Disclosure
  slug: clio-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Clio Trust Center
  slug: clio-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: clio
tags:
- Billing
- Calendaring
- Document Management
- Law Firms
- Legal
- Matter Management
- OAuth 2.0
- Practice Management
- Time Tracking
- Trust Accounting
website: https://www.clio.com/
---

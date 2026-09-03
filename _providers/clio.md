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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 143
  human_in_the_loop: 4
  name: Clio Agentic Access
  operation_count: 286
  slug: clio-agentic-access
  summary_line: 286 operations · 143 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: Clio Webhooks deliver near real-time notifications when matters, contacts, activities, tasks, calendar entries, bills, and other Clio resources are created, updated, or deleted. Subscriptions are mana
  name: Clio Webhooks
  slug: webhooks
- description: The Clio App Directory is the integration marketplace for certified third-party apps that connect to Clio Manage. Apps listed in the directory are reviewed by Clio's developer partnerships team and ma
  name: Clio App Directory
  slug: app-directory
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Activities (Time Entries and Expense Entries) track work done at a firm. Activities are recorded in Clio and then posted on bills to clients. Time Entries can be either be hourly-billable or flat-rate
  name: Clio Activities API
  slug: clio-activities-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Activity Descriptions are custom Time Entry templates. Activity Descriptions help firms expedite their process for recording Time Entries, and ensure that their Time Entry descriptions are consistent.
  name: Clio Activity Descriptions API
  slug: clio-activity-descriptions-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Activity Rates API from Clio — 2 operation(s) for activity rates.
  name: Clio Activity Rates API
  slug: clio-activity-rates-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Once a [Payment](https://help.clio.com/hc/articles/9285641955355-Record-Edit-and-Delete-Payments) or [Credit Note](https://help.clio.com/hc/en-us/articles/9285299888539-Credit-Notes) has been recorded
  name: Clio Allocations API
  slug: clio-allocations-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: These accounts are meant to mirror the firm’s accounts at their financial institution. Users can add a bank account to Clio to use with [Clio Payments](https://help.clio.com/hc/articles/9285631748507-
  name: Clio Bank Accounts API
  slug: clio-bank-accounts-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Bank Transactions API from Clio — 2 operation(s) for bank transactions.
  name: Clio Bank Transactions API
  slug: clio-bank-transactions-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Bank Transfers API from Clio — 1 operation(s) for bank transfers.
  name: Clio Bank Transfers API
  slug: clio-bank-transfers-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Bill Themes API from Clio — 2 operation(s) for bill themes.
  name: Clio Bill Themes API
  slug: clio-bill-themes-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Users can view all Billable Clients, or clients with outstanding [Bills](https://help.clio.com/hc/en-us/articles/9285169278747-Generate-Bills), on the Billable Clients page, located under the Bills ta
  name: Clio Billable Clients API
  slug: clio-billable-clients-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Users can see all [Matters with outstanding bills](https://help.clio.com/hc/en-us/articles/9286116462747#filter-matters-clio-manage-0-0) attached to them by filtering out all non-billable Matters unde
  name: Clio Billable Matters API
  slug: clio-billable-matters-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Billing Settings API from Clio — 1 operation(s) for billing settings.
  name: Clio Billing Settings API
  slug: clio-billing-settings-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Bills are statements of what a user’s client owes for their services over a particular billing period, including legal fees, expenses, and taxes. Users customize, preview, edit, and approve bills befo
  name: Clio Bills API
  slug: clio-bills-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Calendar Entries are used to track appointments or deadlines. Users can view Calendar Entries on any Calendar that they have “Viewer” or “Editor” permission for. Users can create Calendar Entries on a
  name: Clio Calendar Entries API
  slug: clio-calendar-entries-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Calendar Entry Event Types API from Clio — 2 operation(s) for calendar entry event types.
  name: Clio Calendar Entry Event Types API
  slug: clio-calendar-entry-event-types-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Calendar Visibilities API from Clio — 2 operation(s) for calendar visibilities.
  name: Clio Calendar Visibilities API
  slug: clio-calendar-visibilities-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Calendars contain Calendar Entries. All Clio accounts contain one firm Calendar ("AccountCalendar"), personal Calendars for each user ("UserCalendar"), and any number of manually created Calendars ("A
  name: Clio Calendars API
  slug: clio-calendars-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: This endpoint provides the Legal Aid civil certificated rates, which are the prescribed reimbursement rates for legal services provided under the Legal Aid Scheme. [Support Link](https://help.clio.com
  name: Clio Civil Certificated Rates API
  slug: clio-civil-certificated-rates-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: This endpoint provides the Legal Aid civil controlled rates, which are the prescribed reimbursement rates for legal services provided under the Legal Aid Scheme. [Support Link](https://help.clio.com/h
  name: Clio Civil Controlled Rates API
  slug: clio-civil-controlled-rates-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Clients API from Clio — 1 operation(s) for clients.
  name: Clio Clients API
  slug: clio-clients-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Clio Payments Links API from Clio — 2 operation(s) for clio payments links.
  name: Clio Clio Payments Links API
  slug: clio-clio-payments-links-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Payments allow users to record that funds (from checks, cash, credit cards, etc.) have been transferred from a client to the firm. In order to pay Bills, Payments must be [allocated](https://help.clio
  name: Clio Clio Payments Payments API
  slug: clio-clio-payments-payments-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Comments are short text messages which can be associated with either Documents or Folders. If the Comment is created in association with a Document, it will also be associated with the Document's late
  name: Clio Comments API
  slug: clio-comments-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Users can view all logged phone calls and emails under the Communications tab in Clio. This is also where they can use [Clio internal messages](https://help.clio.com/hc/en-us/articles/9125264015259-In
  name: Clio Communications API
  slug: clio-communications-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: All clients, prospective clients, companies, and external co-counsels can be viewed as Contacts under the Contacts tab in Clio Manage. [Support Link](https://help.clio.com/hc/en-us/articles/9290486281
  name: Clio Contacts API
  slug: clio-contacts-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Conversation Messages API from Clio — 2 operation(s) for conversation messages.
  name: Clio Conversation Messages API
  slug: clio-conversation-messages-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Conversations API from Clio — 2 operation(s) for conversations.
  name: Clio Conversations API
  slug: clio-conversations-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: 'Credit Memos allow users to write off amounts that clients owe on approved Bills. They can be added in two "ways": when viewing a Bill, or when making a payment on a Bill. [Support Link](https://help.'
  name: Clio Credit Memos API
  slug: clio-credit-memos-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: This endpoint provides the Legal Aid criminal controlled rates, which are the prescribed reimbursement rates for legal services provided under the Legal Aid Scheme. [Support Link](https://help.clio.co
  name: Clio Criminal Controlled Rates API
  slug: clio-criminal-controlled-rates-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Currencies API from Clio — 1 operation(s) for currencies.
  name: Clio Currencies API
  slug: clio-currencies-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: 'In Clio, applications can create custom actions in our interface. Links are unique across an application, user, location in the UI (`ui_reference`) and label. When the user clicks on a custom action, '
  name: Clio Custom Actions API
  slug: clio-custom-actions-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Custom Field Sets API from Clio — 2 operation(s) for custom field sets.
  name: Clio Custom Field Sets API
  slug: clio-custom-field-sets-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Custom Fields API from Clio — 2 operation(s) for custom fields.
  name: Clio Custom Fields API
  slug: clio-custom-fields-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Damages API from Clio — 2 operation(s) for damages.
  name: Clio Damages API
  slug: clio-damages-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Document Archives API from Clio — 3 operation(s) for document archives.
  name: Clio Document Archives API
  slug: clio-document-archives-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Document Automation uses Document Templates to create standardized documents. Users select a Document Template (that they have created and uploaded) and a Matter to automatically create a document usi
  name: Clio Document Automations API
  slug: clio-document-automations-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Clio users can add Document Categories to their account to help organize their Documents. When a Document is uploaded or edited, a Document Category can be assigned. Users can filter by Document Categ
  name: Clio Document Categories API
  slug: clio-document-categories-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: 'Document Templates are files used to create standardized documents using Clio’s Document Automation feature. Document Templates contain merge fields, which are used to pull information from Clio into '
  name: Clio Document Templates API
  slug: clio-document-templates-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Versions contain information about the version history of a document. Versioning allows users to track changes made to a document over time. [Support Link](https://help.clio.com/hc/en-us/articles/9290
  name: Clio Document Versions API
  slug: clio-document-versions-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Clio Documents are files uploaded to Clio. Files uploaded to Clio’s document integrations (e.g. Google Drive and Office365) are inaccessible through the API. [Support Link](https://help.clio.com/hc/en
  name: Clio Documents API
  slug: clio-documents-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Email Addresses are email addresses associated with a Contact. This endpoint returns all email addresses associated with a Contact.
  name: Clio Email Addresses API
  slug: clio-email-addresses-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Event metrics keep track of firm users' unread web and mobile [In-app notifications](https://help.clio.com/hc/en-us/articles/9290346939547-Set-Up-Clio-Manage#settings-0-3) and unread [Clio Internal Me
  name: Clio Event Metrics API
  slug: clio-event-metrics-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: This endpoint provides the Legal Aid expense category rates, which are the prescribed reimbursement rates for legal services provided under the Legal Aid Scheme. [Support Link](https://help.clio.com/h
  name: Clio Expense Categories API
  slug: clio-expense-categories-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Files stored in Clio’s Documents section are organized in folders. Folders are automatically generated for new Contacts and Matters. Folders can also be manually created anywhere in the folder structu
  name: Clio Folders API
  slug: clio-folders-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Grant Funding Sources API from Clio — 2 operation(s) for grant funding sources.
  name: Clio Grant Funding Sources API
  slug: clio-grant-funding-sources-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Grants API from Clio — 2 operation(s) for grants.
  name: Clio Grants API
  slug: clio-grants-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: In Clio, [permission levels](https://help.clio.com/hc/en-us/articles/9200279456667-Account-Users-and-Permissions#user-permissions-clio-manage--0-2) and [Matter permissions](https://help.clio.com/hc/en
  name: Clio Groups API
  slug: clio-groups-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Interest Charges API from Clio — 2 operation(s) for interest charges.
  name: Clio Interest Charges API
  slug: clio-interest-charges-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: There are over 1000 jurisdictions available to choose from when using Court Rules. These jurisdictions contain state, federal, appellate, and bankruptcy courts from across the United States. Jurisdict
  name: Clio Jurisdictions API
  slug: clio-jurisdictions-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Jurisdictions-to-Triggers calculates the effective dates of related court and agency rules that a lawyer must do for a Trigger. A Trigger is an activity or event which a lawyer or court does in a juri
  name: Clio Jurisdictions To Triggers API
  slug: clio-jurisdictions-to-triggers-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Line Items API from Clio — 2 operation(s) for line items.
  name: Clio Line Items API
  slug: clio-line-items-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: 'Log Entries populate the “Recents” dropdown in the header. The “Recent” section displays the ten Matters and Contacts that the user most recently accessed. When a user accesses a Contact or a Matter, '
  name: Clio Log Entries API
  slug: clio-log-entries-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: All clients, prospective clients, companies, and external co-counsels can be viewed as Contacts under the Contacts tab in Clio Manage. [Support Link](https://help.clio.com/hc/en-us/articles/9290486281
  name: Clio Matter Contacts API
  slug: clio-matter-contacts-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: A Matter Docket connects a Matter with a Court Rule (and all of the Calendar Entries associated with the Court Rule). Matter Dockets are viewable on the Matter Edit screen under the Court Rules headin
  name: Clio Matter Dockets API
  slug: clio-matter-dockets-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Matter Stages API from Clio — 1 operation(s) for matter stages.
  name: Clio Matter Stages API
  slug: clio-matter-stages-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: '[Matters](https://help.clio.com/hc/en-us/articles/9285920226075-Clio-Manage-Matters-Overview) in Clio represent a firm’s cases. All relevant information—Bills, Documents, Time Entries, etc.—are contai'
  name: Clio Matters API
  slug: clio-matters-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Medical Bills are a subset of Medical Records Details and can be used to keep track of documents, bill dates, and liens. Note that these endpoints only handle Updating and Destroying a record. Creatin
  name: Clio Medical Bills API
  slug: clio-medical-bills-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: 'Medical Records are a subset of Medical Records Details and can be used to keep track of documents, start dates, and end dates. Note that these endpoints only handle Updating and Destroying a record. '
  name: Clio Medical Records API
  slug: clio-medical-records-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: 'Medical Records Details allow you to track requests for medical records and medical bills, track treatment dates, follow up on requests, upload medical files, and track liens and outstanding balances '
  name: Clio Medical Records Details API
  slug: clio-medical-records-details-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: In-app notifications are used to notify firm users of important events or changes in Clio, initiated by other firm users. These events are displayed in the **Your firm** tab of the notifications panel
  name: Clio My Events API
  slug: clio-my-events-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Notes can be added to Matters or Contacts in Clio to record meeting notes, research, or anything else a user might want. The field can hold hundreds of pages, so users can add plenty of information. N
  name: Clio Notes API
  slug: clio-notes-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Outstanding Client Balances API from Clio — 1 operation(s) for outstanding client balances.
  name: Clio Outstanding Client Balances API
  slug: clio-outstanding-client-balances-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Phone Numbers are phone numbers associated with a Contact. This endpoint returns all phone numbers associated with a Contact.
  name: Clio Phone Numbers API
  slug: clio-phone-numbers-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The practice area field can be added to Matters and used for filtering purposes, or just for reference. Users can create their own practice areas in their [Firm Preferences settings](https://help.clio
  name: Clio Practice Areas API
  slug: clio-practice-areas-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Related Contacts API from Clio — 1 operation(s) for related contacts.
  name: Clio Related Contacts API
  slug: clio-related-contacts-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Relationships are used on a Matter to track Contacts related to the Matter. Relationships are can be found on the Contacts sub tab of a Matter. [Support Link](https://help.clio.com/hc/en-us/articles/9
  name: Clio Relationships API
  slug: clio-relationships-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Reminders can be added to Tasks or Calendar Entries. Reminder emails can be sent by a User to themselves, other Users, Clio For Co-Counsel/Clio Connect Contacts, or [any authorized email](https://help
  name: Clio Reminders API
  slug: clio-reminders-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Report Presets can be created to streamline report generation workflow by saving report option parameters as a Preset. [Support Link](https://help.clio.com/hc/en-us/articles/9290078155803-Generate-Rep
  name: Clio Report Presets API
  slug: clio-report-presets-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Schedule report generation for an existing Report Preset using Report Schedules. A Report Schedule will generate reports from the specified Preset's report options on a daily, weekly or monthly basis.
  name: Clio Report Schedules API
  slug: clio-report-schedules-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Reports API from Clio — 3 operation(s) for reports.
  name: Clio Reports API
  slug: clio-reports-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Service Types are used when creating new Court Rules involving the delivery of documents. In order to calculate the correct deadline to send the document, an account will specify their Service Type. C
  name: Clio Service Types API
  slug: clio-service-types-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: With Task Template Lists, users can create groups of [Task Templates](https://docs.developers.clio.com/clio-manage/api-reference/#tag/Task-Templates) for the types of projects they work on most often.
  name: Clio Task Template Lists API
  slug: clio-task-template-lists-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Task Templates are the individual [Tasks](https://docs.developers.clio.com/clio-manage/api-reference/#tag/Tasks) which comprise a [Task Template List](https://docs.developers.clio.com/clio-manage/api-
  name: Clio Task Templates API
  slug: clio-task-templates-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Task Types are used to better categorize and filter tasks. This is a simple text field which is limited to 50 characters. Task Types are part of the Advanced Tasks feature which is not available to al
  name: Clio Task Types API
  slug: clio-task-types-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Tasks are used to assign and track work. Users can set priorities, due dates, and add reminders. Tasks can be assigned to firm users as well as Contacts (such as clients or co-counsel). [Support Link]
  name: Clio Tasks API
  slug: clio-tasks-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Tax Rate Configurations API from Clio — 2 operation(s) for tax rate configurations.
  name: Clio Tax Rate Configurations API
  slug: clio-tax-rate-configurations-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: 'Clio''s Text Snippets feature allows users to create a list of predefined abbreviations for commonly used phrases. For example, a user could configure their settings to have “meeting with client” show '
  name: Clio Text Snippets API
  slug: clio-text-snippets-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: 'Timers are used to track time spent on billable work. They are used with hourly-billable [Time Entries](https://docs.developers.clio.com/clio-manage/api-reference/#tag/Activities). The Timer modal is '
  name: Clio Timers API
  slug: clio-timers-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Trust Line Items API from Clio — 2 operation(s) for trust line items.
  name: Clio Trust Line Items API
  slug: clio-trust-line-items-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: The Trust Requests API from Clio — 1 operation(s) for trust requests.
  name: Clio Trust Requests API
  slug: clio-trust-requests-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: A User is anyone with the ability to log in to Clio. This does not include Clio for Co-Counsel/Clio Connect users. [Support Link](https://help.clio.com/hc/en-us/articles/9200279456667-Account-Users-an
  name: Clio Users API
  slug: clio-users-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: '[UTBMS codes](http://utbms.com/) standardize Time and Expense entries across the legal profession. Clio users can enter their Activities using UTBMS codes in order to provide electronic invoices. [Sup'
  name: Clio Utbms Codes API
  slug: clio-utbms-codes-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: '[UTBMS codes](https://docs.developers.clio.com/clio-manage/api-reference/#tag/Utbms-Codes) are divided into code sets. Each set includes Activities relevant to a certain type of law (for example, liti'
  name: Clio Utbms Sets API
  slug: clio-utbms-sets-api
- baseURL: https://app.clio.com/api/v4
  baseurl_source: declared
  description: Webhooks are a way of detecting events in Clio without the need for polling. A webhook can be subscribed to a number of `events` on a model. Some events will be different depending on the chosen model
  name: Clio Webhooks API
  slug: clio-webhooks-api
artifact_total: 177
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clio API Documentation Activities API
  slug: open-clio-activities-api
- collection_type: open
  name: Clio API Documentation Activities Activity Descriptions API
  slug: open-clio-activity-descriptions-api
- collection_type: open
  name: Clio API Documentation Activities Activity Rates API
  slug: open-clio-activity-rates-api
- collection_type: open
  name: Clio API Documentation Activities Allocations API
  slug: open-clio-allocations-api
- collection_type: open
  name: Clio API Documentation Activities Bank Accounts API
  slug: open-clio-bank-accounts-api
- collection_type: open
  name: Clio API Documentation Activities Bank Transactions API
  slug: open-clio-bank-transactions-api
- collection_type: open
  name: Clio API Documentation Activities Bank Transfers API
  slug: open-clio-bank-transfers-api
- collection_type: open
  name: Clio API Documentation Activities Bill Themes API
  slug: open-clio-bill-themes-api
- collection_type: open
  name: Clio API Documentation Activities Billable Clients API
  slug: open-clio-billable-clients-api
- collection_type: open
  name: Clio API Documentation Activities Billable Matters API
  slug: open-clio-billable-matters-api
- collection_type: open
  name: Clio API Documentation Activities Billing Settings API
  slug: open-clio-billing-settings-api
- collection_type: open
  name: Clio API Documentation Activities Bills API
  slug: open-clio-bills-api
- collection_type: open
  name: Clio API Documentation Activities Calendar Entries API
  slug: open-clio-calendar-entries-api
- collection_type: open
  name: Clio API Documentation Activities Calendar Entry Event Types API
  slug: open-clio-calendar-entry-event-types-api
- collection_type: open
  name: Clio API Documentation Activities Calendar Visibilities API
  slug: open-clio-calendar-visibilities-api
- collection_type: open
  name: Clio API Documentation Activities Calendars API
  slug: open-clio-calendars-api
- collection_type: open
  name: Clio API Documentation Activities Civil Certificated Rates API
  slug: open-clio-civil-certificated-rates-api
- collection_type: open
  name: Clio API Documentation Activities Civil Controlled Rates API
  slug: open-clio-civil-controlled-rates-api
- collection_type: open
  name: Clio API Documentation Activities Clients API
  slug: open-clio-clients-api
- collection_type: open
  name: Clio API Documentation Activities Clio Payments Links API
  slug: open-clio-clio-payments-links-api
- collection_type: open
  name: Clio API Documentation Activities Clio Payments Payments API
  slug: open-clio-clio-payments-payments-api
- collection_type: open
  name: Clio API Documentation Activities Comments API
  slug: open-clio-comments-api
- collection_type: open
  name: Clio API Documentation Activities Communications API
  slug: open-clio-communications-api
- collection_type: open
  name: Clio API Documentation Activities Contacts API
  slug: open-clio-contacts-api
- collection_type: open
  name: Clio API Documentation Activities Conversation Messages API
  slug: open-clio-conversation-messages-api
- collection_type: open
  name: Clio API Documentation Activities Conversations API
  slug: open-clio-conversations-api
- collection_type: open
  name: Clio API Documentation Activities Credit Memos API
  slug: open-clio-credit-memos-api
- collection_type: open
  name: Clio API Documentation Activities Criminal Controlled Rates API
  slug: open-clio-criminal-controlled-rates-api
- collection_type: open
  name: Clio API Documentation Activities Currencies API
  slug: open-clio-currencies-api
- collection_type: open
  name: Clio API Documentation Activities Custom Actions API
  slug: open-clio-custom-actions-api
- collection_type: open
  name: Clio API Documentation Activities Custom Field Sets API
  slug: open-clio-custom-field-sets-api
- collection_type: open
  name: Clio API Documentation Activities Custom Fields API
  slug: open-clio-custom-fields-api
- collection_type: open
  name: Clio API Documentation Activities Damages API
  slug: open-clio-damages-api
- collection_type: open
  name: Clio API Documentation Activities Document Archives API
  slug: open-clio-document-archives-api
- collection_type: open
  name: Clio API Documentation Activities Document Automations API
  slug: open-clio-document-automations-api
- collection_type: open
  name: Clio API Documentation Activities Document Categories API
  slug: open-clio-document-categories-api
- collection_type: open
  name: Clio API Documentation Activities Document Templates API
  slug: open-clio-document-templates-api
- collection_type: open
  name: Clio API Documentation Activities Document Versions API
  slug: open-clio-document-versions-api
- collection_type: open
  name: Clio API Documentation Activities Documents API
  slug: open-clio-documents-api
- collection_type: open
  name: Clio API Documentation Activities Email Addresses API
  slug: open-clio-email-addresses-api
- collection_type: open
  name: Clio API Documentation Activities Event Metrics API
  slug: open-clio-event-metrics-api
- collection_type: open
  name: Clio API Documentation Activities Expense Categories API
  slug: open-clio-expense-categories-api
- collection_type: open
  name: Clio API Documentation Activities Folders API
  slug: open-clio-folders-api
- collection_type: open
  name: Clio API Documentation Activities Grant Funding Sources API
  slug: open-clio-grant-funding-sources-api
- collection_type: open
  name: Clio API Documentation Activities Grants API
  slug: open-clio-grants-api
- collection_type: open
  name: Clio API Documentation Activities Groups API
  slug: open-clio-groups-api
- collection_type: open
  name: Clio API Documentation Activities Interest Charges API
  slug: open-clio-interest-charges-api
- collection_type: open
  name: Clio API Documentation Activities Jurisdictions API
  slug: open-clio-jurisdictions-api
- collection_type: open
  name: Clio API Documentation Activities Jurisdictions To Triggers API
  slug: open-clio-jurisdictions-to-triggers-api
- collection_type: open
  name: Clio API Documentation Activities Line Items API
  slug: open-clio-line-items-api
- collection_type: open
  name: Clio API Documentation Activities Log Entries API
  slug: open-clio-log-entries-api
- collection_type: open
  name: Clio API Documentation Activities Matter Contacts API
  slug: open-clio-matter-contacts-api
- collection_type: open
  name: Clio API Documentation Activities Matter Dockets API
  slug: open-clio-matter-dockets-api
- collection_type: open
  name: Clio API Documentation Activities Matter Stages API
  slug: open-clio-matter-stages-api
- collection_type: open
  name: Clio API Documentation Activities Matters API
  slug: open-clio-matters-api
- collection_type: open
  name: Clio API Documentation Activities Medical Bills API
  slug: open-clio-medical-bills-api
- collection_type: open
  name: Clio API Documentation Activities Medical Records API
  slug: open-clio-medical-records-api
- collection_type: open
  name: Clio API Documentation Activities Medical Records Details API
  slug: open-clio-medical-records-details-api
- collection_type: open
  name: Clio API Documentation Activities My Events API
  slug: open-clio-my-events-api
- collection_type: open
  name: Clio API Documentation Activities Notes API
  slug: open-clio-notes-api
- collection_type: open
  name: Clio API Documentation Activities Outstanding Client Balances API
  slug: open-clio-outstanding-client-balances-api
- collection_type: open
  name: Clio API Documentation Activities Phone Numbers API
  slug: open-clio-phone-numbers-api
- collection_type: open
  name: Clio API Documentation Activities Practice Areas API
  slug: open-clio-practice-areas-api
- collection_type: open
  name: Clio API Documentation Activities Related Contacts API
  slug: open-clio-related-contacts-api
- collection_type: open
  name: Clio API Documentation Activities Relationships API
  slug: open-clio-relationships-api
- collection_type: open
  name: Clio API Documentation Activities Reminders API
  slug: open-clio-reminders-api
- collection_type: open
  name: Clio API Documentation Activities Report Presets API
  slug: open-clio-report-presets-api
- collection_type: open
  name: Clio API Documentation Activities Report Schedules API
  slug: open-clio-report-schedules-api
- collection_type: open
  name: Clio API Documentation Activities Reports API
  slug: open-clio-reports-api
- collection_type: open
  name: Clio API Documentation Activities Service Types API
  slug: open-clio-service-types-api
- collection_type: open
  name: Clio API Documentation Activities Task Template Lists API
  slug: open-clio-task-template-lists-api
- collection_type: open
  name: Clio API Documentation Activities Task Templates API
  slug: open-clio-task-templates-api
- collection_type: open
  name: Clio API Documentation Activities Task Types API
  slug: open-clio-task-types-api
- collection_type: open
  name: Clio API Documentation Activities Tasks API
  slug: open-clio-tasks-api
- collection_type: open
  name: Clio API Documentation Activities Tax Rate Configurations API
  slug: open-clio-tax-rate-configurations-api
- collection_type: open
  name: Clio API Documentation Activities Text Snippets API
  slug: open-clio-text-snippets-api
- collection_type: open
  name: Clio API Documentation Activities Timers API
  slug: open-clio-timers-api
- collection_type: open
  name: Clio API Documentation Activities Trust Line Items API
  slug: open-clio-trust-line-items-api
- collection_type: open
  name: Clio API Documentation Activities Trust Requests API
  slug: open-clio-trust-requests-api
- collection_type: open
  name: Clio API Documentation Activities Users API
  slug: open-clio-users-api
- collection_type: open
  name: Clio API Documentation Activities Utbms Codes API
  slug: open-clio-utbms-codes-api
- collection_type: open
  name: Clio API Documentation Activities Utbms Sets API
  slug: open-clio-utbms-sets-api
- collection_type: open
  name: Clio API Documentation Activities Webhooks API
  slug: open-clio-webhooks-api
- collection_type: open
  name: Clio API Documentation
  slug: open-clio
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/clio-capability-edges.yml
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
overview: 'Clio publishes 83 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Activity Descriptions API, Activity Rates API, and 80 more. Tagged areas include Billing, Calendaring, Document-Management, Law Firms, and Legal.


  The Clio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clio''s developer surface includes documentation, pricing, signup flow, developer portal, authentication, support, engineering blog, and 16 more developer resources.'
random_paper: 3
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Clio API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: clio-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 54.5
    contract_quality: 64.3
    developer_ergonomics: 40.5
    discoverability: 44.4
    governance: 54.5
    operational_transparency: 21.1
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 83
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Document-Management
- Law Firms
- Legal
- Matter Management
- Authentication
- Practice Management
- Time Tracking
- Trust Accounting
website: https://www.clio.com/
---

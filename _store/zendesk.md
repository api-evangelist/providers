---
aid: zendesk
url: https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/apis.yml
apis:
  - aid: zendesk:assignables
    name: Zendesk Assignables API
    tags:
      - Assignables
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/introduction/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/introduction/
        type: Documentation
      - url: openapi/assignables-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Assignables API lets you find out who or what can be assigned to a piece of worktypically a ticketgiven your accounts permissions, groups, and routing rules. It returns the set of eligible assignees (such as agents or groups) for a particular context, so you can build assignee pickers in custom apps, validate that an assignment is allowed before updating a ticket, or automate routing workflows.
  - aid: zendesk:target-type
    name: Zendesk Target Type API
    tags:
      - Target Types
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/targets/targets/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/targets/targets/
        type: Documentation
      - url: openapi/target-type-openapi-original.yml
        type: OpenAPI
    description: 'The Zendesk Target Types API exposes a catalog of the legacy target integrations your Zendesk account supportssuch as email or HTTP/URL targetsthat triggers and automations can use to send notifications or payloads to external systems. Its primarily a discovery endpoint: it lets you list the available target types and see the fields each one requires, so you can correctly create target instances with the Targets API.'
  - aid: zendesk:account
    name: Zendesk Account API
    tags:
      - Accounts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/account/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/account/
        type: Documentation
      - url: openapi/account-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Account API lets you programmatically work with account-level records and settings so you can keep Zendesk in sync with the rest of your stack. In Zendesk Sell, it exposes endpoints to list, retrieve, create, update, and delete account objects (the companies you do business with), manage custom fields and tags, and relate accounts to contacts and deals, with search, filtering, and pagination for efficient data access.
  - aid: zendesk:accounts
    name: Zendesk Accounts API
    tags:
      - Accounts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/account/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/account/
        type: Documentation
      - url: openapi/accounts-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Sell Accounts API lets you programmatically manage the company records (accounts) in your CRM. It provides REST endpoints to create, read, update, and delete accounts; search and filter them; and work with related data such as associated contacts, deals, activities, notes, tags, and custom fields.
  - aid: zendesk:activities
    name: Zendesk Activities API
    tags:
      - Activities
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/activity_stream/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/activity_stream/
        type: Documentation
      - url: openapi/activities-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Sell Activities API lets you programmatically manage the work your sales team doessuch as calls, emails, meetings, and tasksby creating, reading, updating, and deleting activity records. Activities can be linked to leads, contacts, and deals, include details like due dates, reminders, outcomes, owners, and notes, and can be filtered and paginated by type, status, user, or timeframe.
  - aid: zendesk:any-channel
    name: Zendesk Any Channel API
    tags:
      - Channels
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/account-configuration/channel_framework/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/account-configuration/channel_framework/
        type: Documentation
      - url: openapi/any-channel-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Any Channel API (also called the Channel Framework) lets developers turn virtually any external communication sourcemessaging apps, social networks, SMS gateways, custom apps, or other platformsinto a firstclass Zendesk channel.
  - aid: zendesk:approval-workflow-instances
    name: Zendesk Approval Workflow Instances API
    tags:
      - Approvals
      - Instances
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/introduction/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/introduction/
        type: Documentation
      - url: openapi/approval-workflow-instances-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Approval Workflow Instances API lets you programmatically start, track, and manage approvals that are built with Zendesks workflow tools. Using REST endpoints, you can create an instance of a predefined approval workflow, associate it with a record such as a ticket, pass input data, and then query the instance to monitor its current state and steps.
  - aid: zendesk:attachments
    name: Zendesk Attachments API
    tags:
      - Attachments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/
        type: Documentation
      - url: openapi/attachments-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Attachments API lets you handle files that users add to Zendesk, primarily for ticket comments (and, via related endpoints, other content like help center articles). You upload a file to Zendesk storage to get an upload token, then reference that token when creating or updating a ticket comment so the file becomes an attachment.
  - aid: zendesk:audit-logs
    name: Zendesk Audit Logs API
    tags:
      - Audit Logs
      - Audits
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/account-configuration/audit_logs/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/account-configuration/audit_logs/
        type: Documentation
      - url: openapi/audit-logs-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Audit Logs API lets you programmatically retrieve a chronological record of important administrative and security-related events in your Zendesk accountsuch as configuration changes, user and role updates, authentications, and other actions that affect account settings.
  - aid: zendesk:autocomplete
    name: Zendesk Autocomplete API
    tags:
      - Autocomplete
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/
        type: Documentation
      - url: openapi/autocomplete-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Autocomplete API provides fast, typeahead-style suggestions for common Zendesk resourcesmost notably users and organizationsso your app can quickly find matches as someone types. You send a partial query (like a name or email) and get back a small, relevance-ordered list of candidates, limited to fields you need (for example, id, name, email) and filtered by the requesters permissions.
  - aid: zendesk:automations
    name: Zendesk Automations API
    tags:
      - Automations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/business-rules/automations/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/business-rules/automations/
        type: Documentation
      - url: openapi/automations-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Automations API lets you programmatically manage time-based business rules that keep Support tickets moving without manual work. Automations evaluate ticket conditions on a regular schedule (typically hourly) using time metrics like hours since creation, last update, or status change, and then perform actions such as changing status or priority, reassigning, adding tags, or sending notifications.
  - aid: zendesk:bookmarks
    name: Zendesk Bookmarks API
    tags:
      - Bookmarks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/bookmarks/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/bookmarks/
        type: Documentation
      - url: openapi/bookmarks-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Bookmarks API lets you programmatically manage an agents personal starred items in Zendesk, providing endpoints to list, create, and delete bookmarks. A bookmark is a lightweight record that points to another Zendesk resource (for example, something an agent wants quick access to in the interface), and its scoped to the user who created it. With the API you can fetch all of a users bookmarks, add new ones to surface important work, and remove those that are no longer relevant.
  - aid: zendesk:brand-agents
    name: Zendesk Brand Agents API
    tags:
      - Brand Agents
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/account-configuration/brand_agents/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/account-configuration/brand_agents/
        type: Documentation
      - url: openapi/brand-agents-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Brand Agents API lets you programmatically manage which agents have access to which brands in a multibrand Zendesk Support account. It provides endpoints to list the agents associated with a given brand and to add or remove agents from that brand, so you can automate onboarding/offboarding, sync brand access from external directories, and enforce leastprivilege access at scale.
  - aid: zendesk:brands
    name: Zendesk Brands API
    tags:
      - Brands
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/account-configuration/brands/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/account-configuration/brands/
        type: Documentation
      - url: openapi/brands-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Brands API is part of the Zendesk Support API that lets you programmatically manage a multibrand setup. It provides endpoints to list, create, update, delete, and fetch the default brand, along with brand-specific settings used across the agent workspace, Help Center, and email.
  - aid: zendesk:channels
    name: Zendesk Channels API
    tags:
      - Channels
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/account-configuration/channel_framework/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/account-configuration/channel_framework/
        type: Documentation
      - url: openapi/channels-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Channels API (Channel Framework) lets developers build custom integrations that bring messages from any external source into Zendesk and send agent replies back out to the original channel. With it, you can register and configure channel accounts, accept inbound messages and attachments, map senders to end users, create or update tickets/conversations, preserve threading and context with metadata, and use channelback to post agent replies to the thirdparty system.
  - aid: zendesk:chat-file-redactions
    name: Zendesk Chat File Redactions API
    tags:
      - Chats
      - Fiiles
      - Redactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/chats/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/chats/
        type: Documentation
      - url: openapi/chat-file-redactions-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Chat File Redactions API lets administrators and trusted tools permanently remove files that were shared in live chat conversations. By redacting a file, its asset is taken out of circulation so it can no longer be downloaded or accessed via its URL, helping teams remediate accidental sharing of sensitive information and meet privacy or compliance requirements (for example, GDPR or CCPA).
  - aid: zendesk:chat-redactions
    name: Zendesk Chat Redactions API
    tags:
      - Chats
      - Redactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/chats/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/chats/
        type: Documentation
      - url: openapi/chat-redactions-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Chat Redactions API lets you programmatically remove sensitive information from chat transcripts and any shared files, so teams can meet security and privacy requirements without deleting entire conversations. You can target specific parts of a message (for example, a credit card number or password), redact an entire message, or remove an attachment; the change is permanent and designed to preserve the rest of the transcript and its metadata.
  - aid: zendesk:comment-redactions
    name: Zendesk Comment Redactions API
    tags:
      - Comments
      - Redactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/
        type: Documentation
      - url: openapi/comment-redactions-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Comment Redactions API lets you programmatically and permanently remove sensitive information from ticket conversations without deleting the entire message. By targeting a specific ticket comment and supplying the text to scrub (for example, credit card numbers, passwords, or PII), the API replaces the matching content in both the plain text and HTML versions with a redacted placeholder and records a redaction event in the tickets audit trail.
  - aid: zendesk:custom-objects
    name: Zendesk Custom Objects API
    tags:
      - Custom Objects
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/custom-data/introduction/
    properties:
      - url: https://developer.zendesk.com/api-reference/custom-data/introduction/
        type: Documentation
      - url: openapi/custom-objects-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Custom Objects API lets you model and store your own business datasuch as orders, subscriptions, devices, or contractsdirectly in Zendesk and relate it to native resources like tickets, users, and organizations. With it, you define object types and fields, create, read, update, and delete records, and establish one-to-one or one-to-many relationships so agents and workflows can access rich context in the Agent Workspace.
  - aid: zendesk:custom-roles
    name: Zendesk Custom Roles API
    tags:
      - Custom Roles
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/account-configuration/custom_roles/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/account-configuration/custom_roles/
        type: Documentation
      - url: openapi/custom-roles-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Custom Roles API lets you programmatically manage the agent permission sets used in Zendesk Support (typically on Enterprise plans). Through it, you can list and fetch existing roles, create new ones, update their names, descriptions, and granular permissions, and delete roles you no longer need.
  - aid: zendesk:custom-status
    name: Zendesk Custom Status API
    tags:
      - Custom Status
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/custom_ticket_statuses/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/custom_ticket_statuses/
        type: Documentation
      - url: openapi/custom-status-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Custom Status API lets you programmatically manage the custom ticket statuses your account uses beyond the builtins. With it, you can list and retrieve statuses, create new ones, update labels and descriptions for agents and end users, localize translations, activate or deactivate statuses, and control their display order.
  - aid: zendesk:custom-statuses
    name: Zendesk Custom Statuses API
    tags:
      - Custom Statuses
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/custom_ticket_statuses/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/custom_ticket_statuses/
        type: Documentation
      - url: openapi/custom-statuses-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Custom Statuses API lets you programmatically create, read, update, delete, and reorder the custom ticket statuses your account uses, giving you more granular workflow states while still rolling up to Zendesks core status categories (like New, Open, Pending, On-hold, Solved, Closed) for SLAs and reporting.
  - aid: zendesk:deleted-tickets
    name: Zendesk Deleted Tickets API
    tags:
      - Deleted Tickets
      - Tickets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/
        type: Documentation
      - url: openapi/deleted-tickets-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Deleted Tickets API lets you manage tickets that have been soft-deleted in Zendesk Support. It provides endpoints to list and inspect deleted tickets, restore them to an active state if they were removed by mistake, or permanently delete them when you need to purge data. The API also supports bulk restore and bulk permanent deletion for handling many tickets at once.
  - aid: zendesk:deleted-users
    name: Zendesk Deleted Users API
    tags:
      - Deleted Users
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/users/users/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/users/users/
        type: Documentation
      - url: openapi/deleted-users-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Deleted Users API lets administrators manage users who have been soft-deleted in a Zendesk Support account. It provides endpoints to list and inspect deleted user records, restore a deleted user to an active state if the deletion was accidental, or permanently purge a user when you need to remove their personal data for compliance.
  - aid: zendesk:deletion-schedules
    name: Zendesk Deletion Schedules API
    tags:
      - Deletion Schedules
      - Schedules
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/business-rules/deletion_schedules/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/business-rules/deletion_schedules/
        type: Documentation
      - url: openapi/deletion-schedules-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Deletion Schedules API lets you programmatically plan and manage future-dated deletions of data in Zendesk to meet retention and privacy requirements (for example, GDPR/CCPA). Instead of deleting immediately, you create schedules that target specific records (such as user or ticket data), choose when the deletion should occur, and then monitor, update, or cancel those schedules before they run.
  - aid: zendesk:dynamic-content
    name: Zendesk Dynamic Content API
    tags:
      - Content
      - Dynamic Content
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/dynamic_content/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/dynamic_content/
        type: Documentation
      - url: openapi/dynamic-content-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Dynamic Content API lets you manage reusable, localized text snippetscalled dynamic content itemsso you can keep messages consistent across macros, triggers, automations, email notifications, and apps. With it, you can programmatically create, read, update, and delete items; add and edit language variants; set a default locale; and activate or deactivate content.
  - aid: zendesk:email-notifications
    name: Zendesk Email Notifications API
    tags:
      - Email
      - Notifications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/email_notifications/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/email_notifications/
        type: Documentation
      - url: openapi/email-notifications-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Email Notifications API (in Zendesk Support) lets admins and developers programmatically inspect the outbound emails Zendesk sendssuch as ticket update notifications. It exposes searchable delivery logs and metadata for each message, including recipient, subject, timestamps, delivery status (for example delivered, deferred, bounced, or complaint) and failure reasons, plus identifiers that help trace which ticket or business rule triggered the email.
  - aid: zendesk:group-memberships
    name: Zendesk Group Memberships API
    tags:
      - Groups
      - Memberships
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/groups/group_memberships/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/groups/group_memberships/
        type: Documentation
      - url: openapi/group-memberships-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Group Memberships API lets you programmatically manage the relationship between users (typically agents) and groups in a Zendesk Support account. With it, you can list memberships across the account or scoped to a specific user or group, add a user to a group, remove a user from a group, and set which group is an agents default. Each membership ties a user_id to a group_id and can indicate the default group that agent belongs to, which affects ticket routing and workflows.
  - aid: zendesk:group-slas
    name: Zendesk Group SLAs API
    tags:
      - Groups
      - Service Level Agreements
      - SLA
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/business-rules/group_sla_policies/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/business-rules/group_sla_policies/
        type: Documentation
      - url: openapi/group-slas-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Group SLAs API lets you manage and report on service-level targets that are scoped to support groups, not just to tickets overall. With it, you can programmatically create and update SLA policies that define different reply and resolution time targets per group, determine which policy and targets are applied to a given ticket as it moves between groups, and retrieve timing details such as remaining time, breach status, and pauses.
  - aid: zendesk:groups
    name: Zendesk Groups API
    tags:
      - Groups
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/groups/groups/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/groups/groups/
        type: Documentation
      - url: openapi/groups-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Groups API lets you programmatically manage the agent groups that power ticket routing and workflows in Zendesk Support. With it, you can create, list, retrieve, update, and delete groups, as well as fetch the set of groups a user can assign tickets to (assignable groups). Groups are used in ticket assignment, views, macros, and business rules like triggers and automations, so the API enables you to integrate group management into your provisioning and operations tooling.
  - aid: zendesk:imports
    name: Zendesk Imports API
    tags:
      - Imports
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_import/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_import/
        type: Documentation
      - url: openapi/imports-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Imports API lets you programmatically load large volumes of records into Zendesk in a controlled, asynchronous wayideal for migrations, initial seeding, or ongoing syncs. You submit a file or batched payload, define which object type to import (for example, users/organizations/tickets in Support or leads/contacts/deals in Sell), and map fields. The import runs as a background job you can monitor via status endpoints, with progress, per-row validation, and detailed error reporting.
  - aid: zendesk:incremental
    name: Zendesk Incremental API
    tags:
      - Incremental
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/incremental_exports/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/incremental_exports/
        type: Documentation
      - url: openapi/incremental-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Incremental API lets you export only the records that have changed since a specific point in time, making it easy to keep external systems in sync without repeatedly pulling full datasets. It supports core objects such as tickets, users, organizations, and ticket events, returning results in chronological order along with a checkpoint (an end_time or a cursor) you store and use on your next request to continue exactly where you left off.
  - aid: zendesk:job-statuses
    name: Zendesk Job Statuses
    tags:
      - Jobs
      - Statuses
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/job_statuses/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/job_statuses/
        type: Documentation
      - url: openapi/job-statuses-openapi-original.yml
        type: OpenAPI
    description: Zendesk Job Statuses is the mechanism and API resource that tracks long-running, asynchronous tasks kicked off in Zendesksuch as bulk ticket updates, user or organization imports, and other create/update many operations. Instead of waiting for a synchronous response, these endpoints return a job ID that you can poll to see whether the work is queued, in progress, or completed, along with progress counts, result details, and any errors.
  - aid: zendesk:locales
    name: Zendesk Locales API
    tags:
      - Locales
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/account-configuration/locales/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/account-configuration/locales/
        type: Documentation
      - url: openapi/locales-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Locales API is a read-only service that lets you discover which languages and regional variants Zendesk supports and which are enabled on your account. It provides lists of all supported locales, the subsets available to end users and to agents, and the current users locale, along with metadata such as the locale code (for example, en-US), display name, and whether the language is right-to-left.
  - aid: zendesk:macros
    name: Zendesk Macros API
    tags:
      - Macros
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/business-rules/macros/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/business-rules/macros/
        type: Documentation
      - url: openapi/macros-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Macros API lets you programmatically manage the reusable, predefined actions that agents apply to Support tickets. With it, you can list, create, update, delete, and reorder macros; fetch details and available action definitions to build editors; and determine which macros are available for a given ticket and user.
  - aid: zendesk:oauth
    name: Zendesk Oauth API
    tags:
      - Authentication
      - Authorization
      - Oauth
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/oauth/oauth_tokens/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/oauth/oauth_tokens/
        type: Documentation
      - url: openapi/oauth-openapi-original.yml
        type: OpenAPI
    description: The Zendesk OAuth API implements the OAuth 2.0 standard to let apps securely access Zendesk data on a users or accounts behalf without sharing passwords. Developers register an OAuth client in a Zendesk account, redirect users to Zendesk for signin and consent, and exchange the returned authorization code for access (and optionally refresh) tokens.
  - aid: zendesk:object-layouts
    name: Zendesk Object Layouts API
    tags:
      - Object Layouts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/introduction/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/introduction/
        type: Documentation
      - url: openapi/object-layouts-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Object Layouts API lets you programmatically control how record pages look and behave in Agent Workspace. It provides CRUD endpoints to define which fields and components appear for an object (such as tickets, users, organizations, and Sunshine custom objects), how theyre grouped and ordered into sections or panels, and any conditional visibility rules.
  - aid: zendesk:organization-fields
    name: Zendesk Organization Fields API
    tags:
      - Organization Fields
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/organizations/organization_fields/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/organizations/organization_fields/
        type: Documentation
      - url: openapi/organization-fields-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Organization Fields API lets you define and manage the custom fields that appear on organization records in Zendesk Support. You can list and inspect existing fields; create new ones with types like text, textarea, checkbox, date, integer, decimal, regexp-validated text, and dropdown (with custom options); update labels, descriptions, keys, active state, and position; reorder how fields appear; and delete fields you no longer need (system fields cant be removed).
  - aid: zendesk:organization-memberships
    name: Zendesk Organization Memberships API
    tags:
      - Organization Memberships
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/organizations/organization_memberships/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/organizations/organization_memberships/
        type: Documentation
      - url: openapi/organization-memberships-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Organization Memberships API lets you programmatically manage the links between users and organizations in Zendesk. With it, you can create, list, find, and delete organization membership records; query memberships for a specific user or organization or across the account; set a users default organization; and perform bulk create/destroy operations to keep memberships in sync with external directories.
  - aid: zendesk:organization-merges
    name: Zendesk Organization Merges API
    tags:
      - Organization Merges
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/
        type: Documentation
      - url: openapi/organization-merges-openapi-original.yml
        type: OpenAPI
    description: Zendesks Organization Merges API lets you consolidate two organizations into one clean record by merging a source organization into a target. During a merge, all users belonging to the source organization are moved to the target, and tickets associated with the source (as requester or via organization) are re-associated to the target, preserving ticket history and continuity.
  - aid: zendesk:organization-subscriptions
    name: Zendesk Organization Subscriptions API
    tags:
      - Organization Subscriptions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/organizations/organization_subscriptions/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/organizations/organization_subscriptions/
        type: Documentation
      - url: openapi/organization-subscriptions-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Organization Subscriptions API lets you programmatically manage which users follow an organization so they automatically receive notifications about that organizations ticket activity. Using it, you can create and delete subscriptions, list who is subscribed to a specific organization, list the organizations a user is subscribed to, and retrieve individual subscription records.
  - aid: zendesk:organizations
    name: Zendesk Organizations API
    tags:
      - Organizations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/organizations/organizations/
        type: Documentation
      - url: openapi/organizations-openapi-original.yml
        type: OpenAPI
      - url: openapi/zendesk-support-openapi.yml
        type: OpenAPI
      - url: json-ld/zendesk-context.jsonld
        type: JSON-LD
    description: The Zendesk Organizations API is a RESTful interface for managing the companies or groups that your users belong to in Zendesk Support. It lets you create, read, update, and delete organizations; set attributes like domains, notes, tags, external_id, and custom fields; and configure behaviors such as shared tickets and comments. You can search and list organizations, use autocomplete, merge duplicates, and perform bulk operations via asynchronous jobs to import or update many records at once.
  - aid: zendesk:problems
    name: Zendesk Problems API
    tags:
      - Problems
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/
        type: Documentation
      - url: openapi/problems-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Problems API helps you manage problem tickets and their relationship to incident tickets, so you can track and resolve widespread issues affecting multiple customers. It provides endpoints to list and query problem tickets and to retrieve the incidents linked to a specific problem (for example, to understand scope and impact).
  - aid: zendesk:push-notification-devices
    name: Zendesk Push Notification Devices API
    tags:
      - Devices
      - Push Notifications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/account-configuration/push_notification_devices/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/account-configuration/push_notification_devices/
        type: Documentation
      - url: openapi/push-notification-devices-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Push Notification Devices API lets you register and manage the mobile devices that should receive push notifications for a given Zendesk user. With it, you can create device records using the apps push token (APNs for iOS, FCM/GCM for Android), list the devices linked to a user, update or disable a device entry, and delete registrations when a user signs out or a device is replaced.
  - aid: zendesk:queues
    name: Zendesk Queues API
    tags:
      - Queues
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/agent-availability/omnichannel_routing_queues/omnichannel_routing_queues/
    properties:
      - url: https://developer.zendesk.com/api-reference/agent-availability/omnichannel_routing_queues/omnichannel_routing_queues/
        type: Documentation
      - url: openapi/queues-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Queues API provides programmatic control over the queues that route work to agents across channels, letting you define and manage how tickets, messages, or calls are prioritized and assigned, and monitor how those queues are performing.
  - aid: zendesk:recipient-addresses
    name: Zendesk Recipient Addresses API
    tags:
      - Addresses
      - Recipients
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/account-configuration/support_addresses/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/account-configuration/support_addresses/
        type: Documentation
      - url: openapi/recipient-addresses-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Recipient Addresses API lets you programmatically manage the email identities your Zendesk Support account can send from in ticket notifications. It allows you to list existing addresses, create new ones (often associated with specific brands), update properties like the display name, initiate or check verification status, set a default sender, and delete addresses.
  - aid: zendesk:relationships
    name: Zendesk Relationships API
    tags:
      - Relationships
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/lookup_relationships/lookup_relationships/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/lookup_relationships/lookup_relationships/
        type: Documentation
      - url: openapi/relationships-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Relationships API lets you model, create, and query links between data entities in Zendesk, spanning both standard resources (like users, organizations, and tickets) and Custom Objects. You define relationship types with explicit cardinality (one-to-one, one-to-many, or many-to-many), then create relationship records that connect specific instancesfor example, associating a customer with their devices, subscriptions, or locations, or tying tickets to assets or accounts.
  - aid: zendesk:requests
    name: Zendesk Requests API
    tags:
      - Requests
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-requests/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-requests/
        type: Documentation
      - url: openapi/requests-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Requests API is the end-userfacing interface for support tickets, designed for customers to create, view, and update their own requests from web or mobile apps without agent credentials. It provides endpoints to submit a new request, list a users existing requests, get details for a specific request, add comments, include attachments (via upload tokens), and check request counts or status.
  - aid: zendesk:resource-collections
    name: Zendesk Resource Collections API
    tags:
      - Collections
      - Resources
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/resource_collections/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/resource_collections/
        type: Documentation
      - url: openapi/resource-collections-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Resource Collections API provides a single, consistent way to list and retrieve Zendesk objectssuch as tickets, users, organizations, and knowledge contentwithout having to call productspecific endpoints. It exposes these objects as uniform collections that support filtering, sorting, field selection, and pagination, making it easier to fetch exactly the data your app or integration needs.
  - aid: zendesk:routing
    name: Zendesk Routing API
    tags:
      - Routing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/skill_based_routing/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/skill_based_routing/
        type: Documentation
      - url: openapi/routing-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Routing API gives you programmatic control over how customer work is distributed to agents across channels. It lets you create and update work items (from tickets, messaging conversations, calls, or external tasks), enrich them with attributes such as skills, priority, and required capacity, and have Zendesks omnichannel router match them to available agents based on unified agent status and capacity limits.
  - aid: zendesk:satisfaction-ratings
    name: Zendesk Satisfaction Ratings API
    tags:
      - Satisfaction Ratings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/satisfaction_ratings/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/satisfaction_ratings/
        type: Documentation
      - url: openapi/satisfaction-ratings-openapi-original.yml
        type: OpenAPI
    description: Zendesks Satisfaction Ratings API lets you programmatically work with customer satisfaction (CSAT) results tied to Support tickets. It provides endpoints to retrieve and page through ratings, fetch a single rating, and access details such as score (good/bad), optional comment, associated ticket, assignee, and timestampsso you can build custom reports, trigger automations, or sync CSAT data to other systems.
  - aid: zendesk:satisfaction-reasons
    name: Zendesk Satisfaction Reasons API
    tags:
      - Satisfaction Reasons
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/satisfaction_reasons/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/satisfaction_reasons/
        type: Documentation
      - url: openapi/satisfaction-reasons-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Satisfaction Reasons API lets you programmatically manage the predefined list of reasons customers can choose when they leave a bad satisfaction rating on a ticket. With it, admins can list, create, update, reorder, activate/deactivate, and delete reasons that appear in the followup survey, ensuring the choices align with current operations or policies.
  - aid: zendesk:search
    name: Zendesk Search API
    tags:
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/search/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/search/
        type: Documentation
      - url: openapi/search-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Search API lets you programmatically find records across your Zendesk Support accountprimarily tickets, users, and organizationsusing a flexible query language that mixes free text with field-based filters (for example, type:ticket, status, tags, assignee, requester, or date ranges).
  - aid: zendesk:sessions
    name: Zendesk Sessions API
    tags:
      - Sessions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/account-configuration/sessions/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/account-configuration/sessions/
        type: Documentation
      - url: openapi/sessions-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Sessions API lets you audit and control users active sign-in sessions in your Zendesk account. It provides endpoints to list current sessions (for the authenticated user or a specified user) and returns metadata such as device/user agent, IP, creation time, and last activity. You can revoke an individual session or all sessions for a user to force logouts across Zendesk web and mobile experiencesuseful for security incidents, offboarding, and SSO changes.
  - aid: zendesk:sharing-agreements
    name: Zendesk Sharing Agreements API
    tags:
      - Sharing Agreements
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/sharing_agreements/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/sharing_agreements/
        type: Documentation
      - url: openapi/sharing-agreements-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Sharing Agreements API lets you programmatically set up and manage ticketsharing relationships between separate Zendesk accounts so teams can collaborate on the same customer issues across instances. With it, you can create, list, update, and delete sharing agreements; send and respond to invitations; define rules and trust settings that control which tickets can be shared and what data is synchronized; and monitor or revoke agreements as needs change.
  - aid: zendesk:skips
    name: Zendesk Skips API
    tags:
      - Skips
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_skips/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_skips/
        type: Documentation
      - url: openapi/skips-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Skips API provides programmatic access to events where an agent doesnt accept or actively skips a routed work item (such as a ticket or conversation) in omnichannel routing. It records who skipped, what was skipped, when it happened, and (when available) the reason, so you can analyze agent behavior, finetune routing rules and capacity, and troubleshoot assignment flows.
  - aid: zendesk:slas
    name: Zendesk SLAs API
    tags:
      - Service Level Agreements
      - SLAs
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/business-rules/sla_policies/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/business-rules/sla_policies/
        type: Documentation
      - url: openapi/slas-openapi-original.yml
        type: OpenAPI
    description: The Zendesk SLAs API lets you programmatically manage and track service level agreement policies in Zendesk Support. It enables you to list, create, update, delete, and reorder SLA policies that set time targetsper priority and schedulefor metrics like first reply time, next reply time, periodic update, requester wait time, agent work time, and resolution time.
  - aid: zendesk:suspended-tickets
    name: Zendesk Suspended Tickets API
    tags:
      - Suspended Tickets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/suspended_tickets/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/suspended_tickets/
        type: Documentation
      - url: openapi/suspended-tickets-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Suspended Tickets API lets you programmatically find and manage inbound emails that Zendesk quarantines as suspended before they become tickets. You can list and inspect these messagesincluding subject, body, sender, recipients, and the machine-readable reason they were suspended (such as spam, auto-reply, bounces, or mail loops)and then either recover them to create normal tickets or permanently delete them, individually or in bulk.
  - aid: zendesk:tags
    name: Zendesk Tags API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/tags/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/tags/
        type: Documentation
      - url: openapi/tags-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Tags API (part of the Support API) lets you programmatically manage the freeform tags used to categorize records in Zendesk. It provides REST endpoints to list all tags in an account (including occurrence counts), retrieve the tags on a specific ticket, user, or organization, and add, remove, or replace those tags. It also supports tag name autocomplete to help maintain consistency.
  - aid: zendesk:target-failures
    name: Zendesk Target Failures API
    tags:
      - Target Failures
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/targets/targets/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/targets/targets/
        type: Documentation
      - url: openapi/target-failures-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Target Failures API helps you monitor and troubleshoot failed delivery attempts to legacy targets (such as HTTP, URL, or email targets) that triggers and automations use to send outbound notifications. It lets you list and inspect recent failures for a target, including details like when they occurred, how many times delivery was attempted, the error or HTTP status returned by the destination, and other diagnostic information.
  - aid: zendesk:targets
    name: Zendesk Targets API
    tags:
      - Targets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/targets/targets/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/targets/targets/
        type: Documentation
      - url: openapi/targets-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Targets API lets you programmatically manage targets, which are external destinations that Zendesk Support triggers and automations can notify when conditions are met. Using the API, you can create, list, update, activate/deactivate, and delete targets, configure details such as URLs, HTTP methods, authentication, and content types, and review delivery failures to troubleshoot outbound notifications.
  - aid: zendesk:ticket-audits
    name: Zendesk Ticket Audits API
    tags:
      - Audits
      - Ticket Audits
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_audits/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_audits/
        type: Documentation
      - url: openapi/ticket-audits-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Ticket Audits API exposes the complete, immutable change history of a Support ticket, letting you retrieve every audit generated whenever a ticket is created or updated. Each audit contains timestamped events that record who made a change and how it happened (agent, end user, trigger, automation, or API), along with metadata such as author, channel, and system details.
  - aid: zendesk:ticket-content-pins
    name: Zendesk Ticket Content Pins API
    tags:
      - Pins
      - Ticket Content
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/
        type: Documentation
      - url: openapi/ticket-content-pins-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Ticket Content Pins API lets you programmatically manage the pinned references that keep important information visible on a support ticket. With it, you can create, list, reorder, and remove pins that point to helpful resources (such as Help Center articles or other relevant content) or key pieces of ticket context, so agents and collaborators always see the most important guidance first.
  - aid: zendesk:ticket-fields
    name: Zendesk Ticket Fields API
    tags:
      - Ticket Fields
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_fields/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_fields/
        type: Documentation
      - url: openapi/ticket-fields-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Ticket Fields API lets you programmatically manage the structured fields that appear on Zendesk Support tickets.
  - aid: zendesk:ticket-form-statuses
    name: Zendesk Ticket Form Statuses API
    tags:
      - Statuses
      - Ticket Forms
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_form_statuses/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_form_statuses/
        type: Documentation
      - url: openapi/ticket-form-statuses-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Ticket Form Statuses API lets you control which ticket statuses (including custom ticket statuses) are available on each ticket form, so you can tailor status options to different request types or brands. With it, admins can retrieve the current status configuration for a form and update which statuses are enabled or hidden from agents and end users, helping simplify workflows and reduce confusion.
  - aid: zendesk:ticket-forms
    name: Zendesk Ticket Forms API
    tags:
      - Forms
      - Tickets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_forms/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_forms/
        type: Documentation
      - url: openapi/ticket-forms-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Ticket Forms API lets you programmatically create, read, update, delete, and reorder the ticket forms that shape how tickets are submitted and displayed in Zendesk Support. Each form defines which ticket fields appear and in what order, enabling you to tailor the submission experience for different request types, workflows, or brands. You can control properties such as the forms name and display name, whether its visible to end users, its default status, and its position.
  - aid: zendesk:ticket-metrics
    name: Zendesk Ticket Metrics API
    tags:
      - Metrics
      - Tickets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metrics/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_metrics/
        type: Documentation
      - url: openapi/ticket-metrics-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Ticket Metrics API lets you programmatically access the operational and SLA metrics that Zendesk calculates for each support ticket. It provides perticket summaries such as first reply time, full resolution time, requester and agent wait times, onhold time, number of replies and reopens, and key timestamps (for example, assigned and solved), often available in both calendar and business minutes.
  - aid: zendesk:tickets
    name: Zendesk Tickets API
    tags:
      - Tickets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/
        type: Documentation
      - url: openapi/tickets-openapi-original.yml
        type: OpenAPI
      - url: openapi/zendesk-support-openapi.yml
        type: OpenAPI
      - url: json-schema/zendesk-ticket-schema.json
        type: JSONSchema
      - url: json-ld/zendesk-context.jsonld
        type: JSON-LD
    description: The Zendesk Tickets API is the primary REST interface for managing support tickets programmatically. It lets you create, read, update, and delete tickets; set core and custom fields (status, priority, type, assignee, requester, organization, tags); and add public or internal comments with file attachments.
  - aid: zendesk:trigger-categories
    name: Zendesk Trigger Categories API
    tags:
      - Categories
      - Triggers
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/business-rules/triggers/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/business-rules/triggers/
        type: Documentation
      - url: openapi/trigger-categories-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Trigger Categories API lets you programmatically organize Zendesk Support triggers into logical groups, making large sets of business rules easier to manage at scale. It provides endpoints to list and retrieve categories, create, rename, reorder, and delete them, and to assign or move triggers between categories or fetch the triggers within a category.
  - aid: zendesk:triggers
    name: Zendesk Triggers API
    tags:
      - Triggers
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/business-rules/triggers/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/business-rules/triggers/
        type: Documentation
      - url: openapi/triggers-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Triggers API lets you programmatically manage the ticket triggers that power automation in Zendesk Support. Triggers are eventbased business rules that run immediately after a ticket is created or updated; when their conditions match, they perform actions like assigning or routing tickets, adding/removing tags, setting fields or status, sending notifications, and invoking webhooks.
  - aid: zendesk:uploads
    name: Zendesk Uploads API
    tags:
      - Uploads
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket-attachments/
        type: Documentation
      - url: openapi/uploads-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Uploads API lets you upload files to Zendesk Support so they can be attached to tickets or embedded inline in ticket comments. When you POST a file, the API creates an upload and returns metadata plus a short-lived token. You then include one or more of these tokens when creating or updating a ticket to add the files as attachments. The API supports single-shot and chunked uploads (for large files), and provides endpoints to check an uploads details or delete it.
  - aid: zendesk:user-fields
    name: Zendesk User Fields API
    tags:
      - User Fields
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/users/users/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/users/users/
        type: Documentation
      - url: openapi/user-fields-openapi-original.yml
        type: OpenAPI
    description: The Zendesk User Fields API lets you programmatically define and manage the custom attributes you store on users in Zendesk Support. You can list, create, update, and delete user fields (such as text, number, date, checkbox, or dropdown), which become part of your user schema and appear on user profiles for agents.
  - aid: zendesk:users
    name: Zendesk Users API
    tags:
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/users/users/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/users/users/
        type: Documentation
      - url: openapi/users-openapi-original.yml
        type: OpenAPI
      - url: openapi/zendesk-support-openapi.yml
        type: OpenAPI
      - url: json-schema/zendesk-user-schema.json
        type: JSONSchema
      - url: json-ld/zendesk-context.jsonld
        type: JSON-LD
    description: The Zendesk Users API is part of the Zendesk Support REST API and lets you programmatically manage the people in your accountend users, agents, and admins. It provides endpoints to list, search, create, update, and delete users; manage roles, tags, custom fields, organization and group memberships; handle user identities (such as email addresses and phone numbers) and verification; set avatars; suspend or reactivate accounts; and merge duplicate users.
  - aid: zendesk:views
    name: Zendesk Views API
    tags:
      - Views
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/business-rules/views/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/business-rules/views/
        type: Documentation
      - url: openapi/views-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Views API lets you programmatically manage and use ticket viewsthe saved sets of filtering, sorting, and column rules that define agent queues. With it, you can list and fetch views (personal or shared), create, update, delete, and reorder them, and execute a view to retrieve the current tickets that match its conditions along with counts.
  - aid: zendesk:workspaces
    name: Zendesk Workspaces API
    tags:
      - Workspaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/workspaces/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/workspaces/
        type: Documentation
      - url: openapi/workspaces-openapi-original.yml
        type: OpenAPI
    description: The Zendesk Workspaces API lets you programmatically create, read, update, delete, and prioritize contextual workspaces that shape the Agent Workspace experience. With it, admins define the conditions under which a workspace applies (for example by brand, channel, group, ticket form, or other ticket attributes) and configure what agents see and use when handling a ticketsuch as the ticket layout and fields, which sidebar apps open or are shown, and available tools or macros.
  - aid: zendesk:help-center-articles
    name: Zendesk Help Center Articles API
    tags:
      - Articles
      - Help Center
      - Knowledge Base
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/
        type: Documentation
    description: The Zendesk Help Center Articles API lets you programmatically manage knowledge base articles in your Help Center. You can create, read, update, and delete articles, manage their translations, set user segment permissions for viewing access, and organize articles within sections. The API supports searching articles, managing article labels, and controlling article visibility for agents and end users.
  - aid: zendesk:help-center-sections
    name: Zendesk Help Center Sections API
    tags:
      - Help Center
      - Knowledge Base
      - Sections
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/sections/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/sections/
        type: Documentation
    description: The Zendesk Help Center Sections API lets you create, read, update, and delete sections within your Help Center categories. Sections organize articles into logical groups and support multiple translations. You can specify user segment permissions to control viewing access and manage the ordering and placement of sections within categories.
  - aid: zendesk:help-center-categories
    name: Zendesk Help Center Categories API
    tags:
      - Categories
      - Help Center
      - Knowledge Base
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/categories/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/categories/
        type: Documentation
    description: The Zendesk Help Center Categories API lets you programmatically manage the top-level organizational structure of your knowledge base. You can create, read, update, and delete categories, specify names and locales, and optionally define multiple translations for each category to support multilingual Help Centers.
  - aid: zendesk:help-center-translations
    name: Zendesk Help Center Translations API
    tags:
      - Help Center
      - Localization
      - Translations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/translations/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/translations/
        type: Documentation
    description: The Zendesk Help Center Translations API lets you manage multilingual content for articles, sections, and categories. You can create, read, update, and delete translations for Help Center content, list available locales, and check which translations are missing, enabling automated localization workflows and integration with external translation management systems.
  - aid: zendesk:help-center-article-attachments
    name: Zendesk Help Center Article Attachments API
    tags:
      - Articles
      - Attachments
      - Help Center
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/article_attachments/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/article_attachments/
        type: Documentation
    description: The Zendesk Help Center Article Attachments API lets you manage file attachments associated with Help Center articles. You can upload new attachments, list existing ones for an article, and delete attachments that are no longer needed. The API supports multipart form data uploads for images, documents, and other file types used in knowledge base content.
  - aid: zendesk:help-center-article-comments
    name: Zendesk Help Center Article Comments API
    tags:
      - Articles
      - Comments
      - Help Center
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/article_comments/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/article_comments/
        type: Documentation
    description: The Zendesk Help Center Article Comments API lets you manage comments on knowledge base articles. Users can provide feedback by adding comments to articles, and the API provides endpoints to list, create, update, and delete comments. The user must have a Zendesk account and their requests must be authenticated to add comments.
  - aid: zendesk:help-center-article-labels
    name: Zendesk Help Center Article Labels API
    tags:
      - Articles
      - Help Center
      - Labels
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/article_labels/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/article_labels/
        type: Documentation
    description: The Zendesk Help Center Article Labels API lets you manage the labels applied to knowledge base articles. Labels help categorize and organize articles for easier discovery. You can list labels on an article, add new labels, and remove existing ones, enabling automated content tagging and organization of your knowledge base.
  - aid: zendesk:help-center-topics
    name: Zendesk Help Center Topics API
    tags:
      - Community
      - Help Center
      - Topics
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/topics/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/topics/
        type: Documentation
    description: The Zendesk Help Center Topics API lets you manage community discussion topics in your Help Center. A topic represents a collection of community posts on a subject. You can create, read, update, and delete topics, set user segment permissions to control access, and organize community content for your users.
  - aid: zendesk:help-center-posts
    name: Zendesk Help Center Posts API
    tags:
      - Community
      - Help Center
      - Posts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/posts/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/posts/
        type: Documentation
    description: The Zendesk Help Center Posts API lets you manage community posts within Help Center topics. You can list all posts, all posts in a given topic, or all posts by a specific user. The API provides endpoints to create, read, update, and delete community posts, enabling programmatic management of community discussions.
  - aid: zendesk:help-center-post-comments
    name: Zendesk Help Center Post Comments API
    tags:
      - Comments
      - Community
      - Help Center
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/post_comments/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/post_comments/
        type: Documentation
    description: The Zendesk Help Center Post Comments API lets you manage comments on community posts. You can list comments on a post, add new comments, update existing comments, and delete comments. This enables programmatic moderation and management of community discussions within Help Center.
  - aid: zendesk:help-center-votes
    name: Zendesk Help Center Votes API
    tags:
      - Help Center
      - Votes
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/votes/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/votes/
        type: Documentation
    description: The Zendesk Help Center Votes API lets you access vote data for knowledge base and community content. You can list all votes cast by a given user, or all votes cast for a given article, article comment, post, or post comment. This enables reporting on content quality and user engagement with your Help Center.
  - aid: zendesk:help-center-content-subscriptions
    name: Zendesk Help Center Content Subscriptions API
    tags:
      - Help Center
      - Subscriptions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/content_subscriptions/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/content_subscriptions/
        type: Documentation
    description: The Zendesk Help Center Content Subscriptions API lets users subscribe to sections, articles, community posts, and community topics to receive notifications when content is added or updated. Users are notified when articles are added to sections, comments are added to articles or posts, or posts are added to topics.
  - aid: zendesk:help-center-user-segments
    name: Zendesk Help Center User Segments API
    tags:
      - Help Center
      - Permissions
      - User Segments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/user_segments/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/user_segments/
        type: Documentation
    description: The Zendesk Help Center User Segments API lets you manage user segments that control access to Help Center content. User segments define groups of users who can view specific articles, sections, or topics. You can create, read, update, and delete segments, and apply them to content to restrict or grant viewing access based on user attributes.
  - aid: zendesk:help-center-permission-groups
    name: Zendesk Help Center Permission Groups API
    tags:
      - Help Center
      - Management
      - Permissions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/permission_groups/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/permission_groups/
        type: Documentation
    description: The Zendesk Help Center Permission Groups API lets you manage which agents can create, update, archive, and publish articles. A management permission group consists of a set of privileges, each mapped to a user segment. This enables fine-grained control over who can manage knowledge base content.
  - aid: zendesk:help-center-search
    name: Zendesk Help Center Search API
    tags:
      - Help Center
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/help_center/help-center-api/search/
    properties:
      - url: https://developer.zendesk.com/api-reference/help_center/help-center-api/search/
        type: Documentation
    description: The Zendesk Help Center Search API provides three different search endpoints for finding content in your knowledge base. The Search Articles and Search Posts endpoints enable you to search for articles and posts respectively, while the Unified Search endpoint allows you to search across articles, posts, and external content in a single query.
  - aid: zendesk:talk
    name: Zendesk Talk API
    tags:
      - Phone
      - Talk
      - Voice
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/voice/talk-api/introduction/
    properties:
      - url: https://developer.zendesk.com/api-reference/voice/talk-api/introduction/
        type: Documentation
    description: The Zendesk Talk API is the reference API for managing Zendesk voice capabilities. It provides endpoints for managing phone numbers, digital lines, greetings, greeting categories, IVRs, IVR routes and menus, call recordings, agent availabilities, voice settings, call stats, current queue activity, and incremental call exports. It is part of the Zendesk v2 API and uses the same authentication and pagination conventions.
  - aid: zendesk:talk-phone-numbers
    name: Zendesk Talk Phone Numbers API
    tags:
      - Phone Numbers
      - Talk
      - Voice
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/voice/talk-api/phone_numbers/
    properties:
      - url: https://developer.zendesk.com/api-reference/voice/talk-api/phone_numbers/
        type: Documentation
    description: The Zendesk Talk Phone Numbers API lets you manage the phone numbers in your Zendesk voice account. You can list existing phone numbers, search for available numbers to purchase, and manage phone number configurations for your Talk instance.
  - aid: zendesk:talk-greetings
    name: Zendesk Talk Greetings API
    tags:
      - Greetings
      - Talk
      - Voice
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/voice/talk-api/greetings/
    properties:
      - url: https://developer.zendesk.com/api-reference/voice/talk-api/greetings/
        type: Documentation
    description: The Zendesk Talk Greetings API lets you manage the greetings used in your Zendesk voice account. Zendesk provides default greetings, but you can replace them with custom greetings by uploading mp3 or wav files. Greetings are assigned to greeting categories and used in IVR menus and call routing flows.
  - aid: zendesk:talk-ivrs
    name: Zendesk Talk IVRs API
    tags:
      - IVR
      - Talk
      - Voice
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/voice/talk-api/ivrs/
    properties:
      - url: https://developer.zendesk.com/api-reference/voice/talk-api/ivrs/
        type: Documentation
    description: The Zendesk Talk IVRs API lets you manage Interactive Voice Response systems that use keypad tones to route customers to the right agent or department, provide recorded responses for frequently asked questions, and deflect calls. IVR is available on Talk Professional and Enterprise plans. The API covers IVRs, IVR menus, and IVR routes.
  - aid: zendesk:talk-recordings
    name: Zendesk Talk Recordings API
    tags:
      - Recordings
      - Talk
      - Voice
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/voice/talk-api/recordings/
    properties:
      - url: https://developer.zendesk.com/api-reference/voice/talk-api/recordings/
        type: Documentation
    description: The Zendesk Talk Recordings API lets you manage call recordings stored by Talk. Recordings are exposed in the corresponding ticket in a voice comment. The API provides endpoints to retrieve and delete recordings associated with calls, supporting compliance and data retention requirements.
  - aid: zendesk:talk-stats
    name: Zendesk Talk Stats API
    tags:
      - Statistics
      - Talk
      - Voice
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/voice/talk-api/stats/
    properties:
      - url: https://developer.zendesk.com/api-reference/voice/talk-api/stats/
        type: Documentation
    description: The Zendesk Talk Stats API provides access to call statistics and current queue activity for your voice account. You can retrieve agent overview metrics including average talk time, available time, and accepted transfers. The current queue activity endpoint provides real-time visibility into call volume, wait times, and agent activity.
  - aid: zendesk:talk-availabilities
    name: Zendesk Talk Availabilities API
    tags:
      - Availabilities
      - Talk
      - Voice
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/voice/talk-api/availabilities/
    properties:
      - url: https://developer.zendesk.com/api-reference/voice/talk-api/availabilities/
        type: Documentation
    description: The Zendesk Talk Availabilities API lets you manage and query agent availability for voice calls. It provides information about agent state, call status, and connection method, enabling real-time monitoring of which agents are available to take calls and their current activity status.
  - aid: zendesk:talk-lines
    name: Zendesk Talk Lines API
    tags:
      - Lines
      - Talk
      - Voice
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/voice/talk-api/lines/
    properties:
      - url: https://developer.zendesk.com/api-reference/voice/talk-api/lines/
        type: Documentation
    description: The Zendesk Talk Lines API lets you list the available lines, including both phone numbers and digital lines, in your Zendesk voice account. This provides a unified view of all voice communication channels configured for your Talk instance.
  - aid: zendesk:talk-digital-lines
    name: Zendesk Talk Digital Lines API
    tags:
      - Digital Lines
      - Talk
      - Voice
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/voice/talk-api/digital_lines/
    properties:
      - url: https://developer.zendesk.com/api-reference/voice/talk-api/digital_lines/
        type: Documentation
    description: The Zendesk Talk Digital Lines API lets you manage the digital lines in your Zendesk voice account. Digital lines enable browser-based calling without traditional phone numbers, providing an additional channel for voice communications within your Talk setup.
  - aid: zendesk:talk-voice-settings
    name: Zendesk Talk Voice Settings API
    tags:
      - Settings
      - Talk
      - Voice
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/voice/talk-api/voice_settings/
    properties:
      - url: https://developer.zendesk.com/api-reference/voice/talk-api/voice_settings/
        type: Documentation
    description: The Zendesk Talk Voice Settings API lets you view and manage the account settings of your Zendesk voice account. It provides endpoints to retrieve and update configuration options that control how your Talk instance operates.
  - aid: zendesk:talk-partner-edition
    name: Zendesk Talk Partner Edition API
    tags:
      - Partner Edition
      - Talk
      - Voice
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/voice/talk-partner-edition-api/introduction/
    properties:
      - url: https://developer.zendesk.com/api-reference/voice/talk-partner-edition-api/introduction/
        type: Documentation
    description: The Zendesk Talk Partner Edition API includes a Standard Call Object with endpoints to save, read, and update call-related data in Zendesk. It enables telephony partners to integrate their calling solutions with Zendesk by providing a standardized way to create and manage call records associated with support tickets.
  - aid: zendesk:chat-accounts
    name: Zendesk Chat Accounts API
    tags:
      - Accounts
      - Chat
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/accounts/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/accounts/
        type: Documentation
    description: The Zendesk Chat Accounts API lets you get or set account information for your Zendesk Chat instance. If you created your Zendesk Chat account in Zendesk Support, access to the Chat Accounts and Agents APIs is restricted to GET requests. You can still use the other Chat APIs normally.
  - aid: zendesk:chat-agents
    name: Zendesk Chat Agents API
    tags:
      - Agents
      - Chat
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/agents/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/agents/
        type: Documentation
    description: The Zendesk Chat Agents API lets you get or set agent information for your Zendesk Chat instance. If you created your Zendesk Chat account in Zendesk Support, access to the Agents API is restricted to GET requests, but you can still use other Chat APIs normally.
  - aid: zendesk:chat-visitors
    name: Zendesk Chat Visitors API
    tags:
      - Chat
      - Visitors
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/visitors/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/visitors/
        type: Documentation
    description: The Zendesk Chat Visitors API lets you get or set visitor information for your Zendesk Chat instance. Visitors represent end users who initiate chat sessions through the Zendesk Chat widget on your website or application.
  - aid: zendesk:chat-chats
    name: Zendesk Chat Chats API
    tags:
      - Chat
      - Conversations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/chats/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/chats/
        type: Documentation
    description: The Zendesk Chat Chats API provides access to individual chat records with information including agent IDs, agent names, department information, chat history, conversions, and goal attributions. You can list and search chat transcripts for reporting, compliance, and quality assurance purposes.
  - aid: zendesk:chat-departments
    name: Zendesk Chat Departments API
    tags:
      - Chat
      - Departments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/departments/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/departments/
        type: Documentation
    description: The Zendesk Chat Departments API lets you get or set department information for your Chat instance. Departments enable you to route chats to specific groups of agents, configure operating hours, and organize your chat support by team or function.
  - aid: zendesk:chat-shortcuts
    name: Zendesk Chat Shortcuts API
    tags:
      - Chat
      - Shortcuts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/shortcuts/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/shortcuts/
        type: Documentation
    description: The Zendesk Chat Shortcuts API lets you manage canned responses that agents can use during live chat conversations. You can list all shortcuts for the account, create new ones, update existing shortcuts, and delete them, with support for scoping by departments and agents.
  - aid: zendesk:chat-triggers
    name: Zendesk Chat Triggers API
    tags:
      - Chat
      - Triggers
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/triggers/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/triggers/
        type: Documentation
    description: The Zendesk Chat Triggers API lets you manage proactive chat triggers that automatically engage visitors based on specified conditions. You can list triggers, add new triggers, update, and delete them. Chat triggers can be set to run when a visitor loads the chat widget or based on other visitor activity.
  - aid: zendesk:chat-bans
    name: Zendesk Chat Bans API
    tags:
      - Bans
      - Chat
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/bans/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/bans/
        type: Documentation
    description: The Zendesk Chat Bans API lets you manage banned visitors in your Chat account. You can list banned visitors with cursor-based pagination, create new bans, and remove existing bans to control which visitors can access your live chat.
  - aid: zendesk:chat-roles
    name: Zendesk Chat Roles API
    tags:
      - Chat
      - Roles
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/roles/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/roles/
        type: Documentation
    description: The Zendesk Chat Roles API lets you manage agent roles and permissions within your Chat account. You can retrieve role definitions and manage role assignments to control what actions different agents can perform in the chat interface.
  - aid: zendesk:chat-skills
    name: Zendesk Chat Skills API
    tags:
      - Chat
      - Skills
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/skills/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/skills/
        type: Documentation
    description: The Zendesk Chat Skills API lets you manage skills used for routing chats to qualified agents. You can get or set skill information, enabling skills-based routing where chats are directed to agents with specific expertise or language capabilities.
  - aid: zendesk:chat-goals
    name: Zendesk Chat Goals API
    tags:
      - Chat
      - Goals
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/goals/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/goals/
        type: Documentation
    description: The Zendesk Chat Goals API lets you manage conversion goals for your Chat account. Goals track specific visitor actions such as page visits or purchases that occur during or after a chat session, enabling you to measure the impact of chat on business outcomes.
  - aid: zendesk:chat-routing-settings
    name: Zendesk Chat Routing Settings API
    tags:
      - Chat
      - Routing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://www.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-api/routing_settings/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-api/routing_settings/
        type: Documentation
    description: The Zendesk Chat Routing Settings API lets you get or modify chat routing settings for your account. It controls how incoming chats are distributed to available agents based on configured rules and policies.
  - aid: zendesk:real-time-chat
    name: Zendesk Real-Time Chat API
    tags:
      - Chat
      - Real-Time
      - Streaming
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://rtm.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/real-time-chat-api/introduction/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/real-time-chat-api/introduction/
        type: Documentation
    description: The Zendesk Real-Time Chat API provides streaming access to real-time chat metrics and activity data. It enables building live dashboards and monitoring tools that display current chat volume, agent activity, and visitor information as events occur.
  - aid: zendesk:chat-conversations
    name: Zendesk Chat Conversations API
    tags:
      - Chat
      - Conversations
      - GraphQL
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://chat-api.zopim.com
    humanURL: https://developer.zendesk.com/api-reference/live-chat/chat-conversations-api/conversations-api/
    properties:
      - url: https://developer.zendesk.com/api-reference/live-chat/chat-conversations-api/conversations-api/
        type: Documentation
    description: The Zendesk Chat Conversations API lets your application act as a Zendesk Chat agent and interact with customers. It is a GraphQL API that supports WebSocket connections for real-time message exchange. Note that this API is in maintenance mode and is not receiving new features.
  - aid: zendesk:webhooks
    name: Zendesk Webhooks API
    tags:
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/webhooks/webhooks-api/webhooks/
    properties:
      - url: https://developer.zendesk.com/api-reference/webhooks/webhooks-api/webhooks/
        type: Documentation
      - url: asyncapi/zendesk-webhooks-asyncapi.yml
        type: AsyncAPI
    description: The Zendesk Webhooks API lets you create, manage, and monitor webhooks that send HTTP requests to specified URLs in response to events in Zendesk. It is the modern replacement for legacy targets, supporting event types for tickets, users, organizations, and messaging. You can create, list, update, test, and delete webhooks, and inspect invocation logs for troubleshooting.
  - aid: zendesk:sell-contacts
    name: Zendesk Sell Contacts API
    tags:
      - Contacts
      - CRM
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/contacts/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/contacts/
        type: Documentation
    description: The Zendesk Sell Contacts API provides a simple interface to manage your contacts. A contact represents an individual or an organization. Each contact has customer_status and prospect_status fields describing the relationship to your business. You can create, read, update, and delete contacts.
  - aid: zendesk:sell-leads
    name: Zendesk Sell Leads API
    tags:
      - CRM
      - Leads
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/leads/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/leads/
        type: Documentation
    description: The Zendesk Sell Leads API provides a simple interface to manage leads. A lead represents an individual or organization that expresses interest in your goods or services. You can create, read, update, and delete leads, and retrieve individual leads as well as lists of all leads.
  - aid: zendesk:sell-deals
    name: Zendesk Sell Deals API
    tags:
      - CRM
      - Deals
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/deals/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/deals/
        type: Documentation
    description: The Zendesk Sell Deals API provides a simple interface to manage deals. You can create, delete, and update deals, retrieve individual deals or lists of all deals. Every deal can have multiple associated contacts with different roles, and deals progress through pipeline stages.
  - aid: zendesk:sell-pipelines
    name: Zendesk Sell Pipelines API
    tags:
      - CRM
      - Pipelines
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/pipelines/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/pipelines/
        type: Documentation
    description: The Zendesk Sell Pipelines API provides a read-only interface to your sales pipeline definitions. Sales pipelines consist of a sequence of stages that deals progress through as they move toward closing.
  - aid: zendesk:sell-stages
    name: Zendesk Sell Stages API
    tags:
      - CRM
      - Sell
      - Stages
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/stages/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/stages/
        type: Documentation
    description: The Zendesk Sell Stages API provides read-only access to details of your sales pipeline stages. Stages are key components of a sales pipeline, and each stage can have any number of deals associated with it.
  - aid: zendesk:sell-tasks
    name: Zendesk Sell Tasks API
    tags:
      - CRM
      - Sell
      - Tasks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/tasks/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/tasks/
        type: Documentation
    description: The Zendesk Sell Tasks API provides a simple interface to manage tasks. A task can be either floating (associated only with a user) or related (associated with a lead, contact, or deal). You can create, read, update, and delete tasks.
  - aid: zendesk:sell-notes
    name: Zendesk Sell Notes API
    tags:
      - CRM
      - Notes
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/notes/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/notes/
        type: Documentation
    description: The Zendesk Sell Notes API provides a simple interface to manage notes. You can create, read, update, and delete notes associated with leads, contacts, and deals in your CRM.
  - aid: zendesk:sell-calls
    name: Zendesk Sell Calls API
    tags:
      - Calls
      - CRM
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/calls/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/calls/
        type: Documentation
    description: The Zendesk Sell Calls API lets you create, read, and delete call records in your CRM. Calls can be associated with leads, contacts, and deals to maintain a complete activity history for your sales team.
  - aid: zendesk:sell-text-messages
    name: Zendesk Sell Text Messages API
    tags:
      - CRM
      - Sell
      - Text Messages
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/text-messages/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/text-messages/
        type: Documentation
    description: The Zendesk Sell Text Messages API provides read-only access to text messages sent and received within Zendesk Sell. You can retrieve individual messages and list all text messages for reporting and integration purposes.
  - aid: zendesk:sell-products
    name: Zendesk Sell Products API
    tags:
      - CRM
      - Products
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/products/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/products/
        type: Documentation
    description: The Zendesk Sell Products API lets you manage your product catalog. You can create, read, update, and delete products. To add products to a deal, create an Order and then populate it with Line Items referencing products from the catalog.
  - aid: zendesk:sell-orders
    name: Zendesk Sell Orders API
    tags:
      - CRM
      - Orders
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/orders/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/orders/
        type: Documentation
    description: The Zendesk Sell Orders API provides a simple interface to manage orders. An order is a list of line items associated with a deal. You can create, read, update, and delete orders to track products and pricing within your deals.
  - aid: zendesk:sell-line-items
    name: Zendesk Sell Line Items API
    tags:
      - CRM
      - Line Items
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/line-items/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/line-items/
        type: Documentation
    description: The Zendesk Sell Line Items API lets you manage individual line items within orders. Line items correspond to products in your catalog and include quantity, pricing, and currency information for each product associated with a deal.
  - aid: zendesk:sell-collaborations
    name: Zendesk Sell Collaborations API
    tags:
      - Collaborations
      - CRM
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/collaborations/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/collaborations/
        type: Documentation
    description: The Zendesk Sell Collaborations API provides a simple interface to manage collaborations. You can create, read, and delete collaborations to enable team members to work together on leads, contacts, and deals.
  - aid: zendesk:sell-sequences
    name: Zendesk Sell Sequences API
    tags:
      - CRM
      - Sell
      - Sequences
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/sequences/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/sequences/
        type: Documentation
    description: The Zendesk Sell Sequences API provides a read-only interface to sequences. A sequence is a set of steps with timeliness of their execution, where each step can be either an automated email or a task, enabling automated sales outreach workflows.
  - aid: zendesk:sell-lead-sources
    name: Zendesk Sell Lead Sources API
    tags:
      - CRM
      - Lead Sources
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/lead-sources/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/lead-sources/
        type: Documentation
    description: The Zendesk Sell Lead Sources API provides a simple interface to manage lead sources. You can create, read, update, and delete sources to track where your leads originate from.
  - aid: zendesk:sell-deal-sources
    name: Zendesk Sell Deal Sources API
    tags:
      - CRM
      - Deal Sources
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/deal-sources/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/deal-sources/
        type: Documentation
    description: The Zendesk Sell Deal Sources API provides a simple interface to manage deal sources. You can create, read, update, and delete sources to track where your deals originate from.
  - aid: zendesk:sell-lead-conversions
    name: Zendesk Sell Lead Conversions API
    tags:
      - CRM
      - Lead Conversions
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/lead-conversions/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/lead-conversions/
        type: Documentation
    description: The Zendesk Sell Lead Conversions API provides a simple interface to manage lead conversions. You can create or read lead conversions that transform leads into contacts and optionally create associated deals.
  - aid: zendesk:sell-tags
    name: Zendesk Sell Tags API
    tags:
      - CRM
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/tags/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/tags/
        type: Documentation
    description: The Zendesk Sell Tags API provides a simple interface to manage tags. You can create, read, update, and delete tags used to categorize and organize leads, contacts, and deals in your CRM.
  - aid: zendesk:sell-custom-fields
    name: Zendesk Sell Custom Fields API
    tags:
      - CRM
      - Custom Fields
      - Sell
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.getbase.com
    humanURL: https://developer.zendesk.com/api-reference/sales-crm/resources/custom-fields/
    properties:
      - url: https://developer.zendesk.com/api-reference/sales-crm/resources/custom-fields/
        type: Documentation
    description: The Zendesk Sell Custom Fields API lets you manage custom fields for leads, contacts, and deals. You can assign any number of custom fields as key-value pairs. Custom fields must first be created in the user interface before they can be managed via the API.
  - aid: zendesk:sunshine-conversations
    name: Zendesk Sunshine Conversations API
    tags:
      - Conversations
      - Messaging
      - Sunshine
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.smooch.io
    humanURL: https://developer.zendesk.com/api-reference/conversations/
    properties:
      - url: https://developer.zendesk.com/api-reference/conversations/
        type: Documentation
    description: The Zendesk Sunshine Conversations API is a messaging platform that lets you unify messages from every channel into a single conversation and build interactive experiences. You can programmatically manage users and conversations, send messages, use webhooks for real-time events, send targeted outbound messages on WhatsApp or SMS, and customize switchboard for bot orchestration flows.
  - aid: zendesk:omnichannel
    name: Zendesk Omnichannel API
    tags:
      - Agent Availability
      - Omnichannel
      - Routing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/agent-availability/introduction/
    properties:
      - url: https://developer.zendesk.com/api-reference/agent-availability/introduction/
        type: Documentation
    description: The Zendesk Omnichannel API provides access to agent availability and status information across Zendesk channels. It includes unified and custom agent statuses, per-channel agent statuses, assigned work items per channel, and agent max capacity per channel. This enables real-time monitoring and management of agent availability for omnichannel routing.
  - aid: zendesk:unified-agent-statuses
    name: Zendesk Unified Agent Statuses API
    tags:
      - Agent Status
      - Omnichannel
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/agent-availability/unified-agent-status-api/unified_agent_statuses/
    properties:
      - url: https://developer.zendesk.com/api-reference/agent-availability/unified-agent-status-api/unified_agent_statuses/
        type: Documentation
    description: The Zendesk Unified Agent Statuses API lets you manage and query unified agent statuses that span across all channels in omnichannel routing. It provides a single view of each agent's availability state, enabling consistent status management and monitoring across Support, Messaging, and Talk channels.
  - aid: zendesk:omnichannel-engagements
    name: Zendesk Omnichannel Engagements API
    tags:
      - Engagements
      - Omnichannel
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/agent-availability/omnichannel-engagements/omnichannel_engagements/
    properties:
      - url: https://developer.zendesk.com/api-reference/agent-availability/omnichannel-engagements/omnichannel_engagements/
        type: Documentation
    description: The Zendesk Omnichannel Engagements API provides access to engagement data for agents across all channels. It enables tracking and reporting on how agents interact with work items, including assignment history, response metrics, and engagement patterns across Support, Messaging, and Talk.
  - aid: zendesk:apps
    name: Zendesk Apps API
    tags:
      - Apps
      - Marketplace
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/apps/apps/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/apps/apps/
        type: Documentation
    description: The Zendesk Apps API lets you manage apps installed on your Zendesk account. It lists all public apps on the Zendesk Marketplace, and for authenticated agents and admins, also lists private apps. You can install, update, and remove apps, and manage app configurations.
  - aid: zendesk:account-settings
    name: Zendesk Account Settings API
    tags:
      - Account Settings
      - Configuration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/account-configuration/account_settings/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/account-configuration/account_settings/
        type: Documentation
    description: The Zendesk Account Settings API lets you view and manage the configuration settings for your Zendesk Support account, including settings for tickets, agents, security, branding, and other account-wide options that control how your Zendesk instance operates.
  - aid: zendesk:schedules
    name: Zendesk Schedules API
    tags:
      - Business Hours
      - Schedules
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/schedules/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/schedules/
        type: Documentation
    description: The Zendesk Schedules API lets you manage business hour schedules that define when your support team is available. Schedules are used by SLA policies, triggers, automations, and other business rules to calculate response and resolution times based on business hours rather than calendar hours.
  - aid: zendesk:user-identities
    name: Zendesk User Identities API
    tags:
      - Identities
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/users/user_identities/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/users/user_identities/
        type: Documentation
    description: The Zendesk User Identities API lets you manage the email addresses, phone numbers, X (Twitter) handles, and other identities associated with a user. You can list, create, update, verify, and delete identities, set a primary identity, and manage how users are identified across channels.
  - aid: zendesk:ticket-comments
    name: Zendesk Ticket Comments API
    tags:
      - Comments
      - Tickets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/tickets/ticket_comments/
        type: Documentation
    description: The Zendesk Ticket Comments API lets you manage comments on support tickets. Comments are the public and internal messages exchanged between agents, end users, and collaborators on a ticket. You can list comments, add new public or internal comments with attachments, and redact sensitive information from existing comments.
  - aid: zendesk:skill-based-routing
    name: Zendesk Skill-Based Routing API
    tags:
      - Routing
      - Skills
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{subdomain}.zendesk.com
    humanURL: https://developer.zendesk.com/api-reference/ticketing/ticket-management/skill_based_routing/
    properties:
      - url: https://developer.zendesk.com/api-reference/ticketing/ticket-management/skill_based_routing/
        type: Documentation
    description: The Zendesk Skill-Based Routing API lets you manage skills and skill-based routing rules that match tickets to agents with the right expertise. You can define skills such as language fluency or product knowledge, assign them to agents, and create routing rules that ensure tickets are directed to qualified agents.
name: Zendesk
tags:
  - Chat
  - CRM
  - Help Center
  - Sell
  - Support
  - T1
  - Talk
  - Ticketing
  - Tickets
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.zendesk.com/company/agreements-and-terms/privacy-notice/
    name: Privacy Notice
    type: PrivacyPolicy
    description: 'null'
  - url: https://status.zendesk.com/
    name: Zendesk Status
    type: StatusPage
    description: 'null'
  - url: https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/
    name: Zendesk Customer Agreement
    type: TermsOfService
    description: 'null'
  - url: https://www.zendesk.com/help-center-closed/?utm_source=helpcenter-closed&utm_medium=poweredbyzendesk&utm_campaign=text&utm_content=developerblog.zendesk.com
    name: Help Center Closed
    type: Blog
    description: 'null'
  - url: https://www.zendesk.com/marketplace/
    name: Zendesk Marketplace - Find Apps, Integrations & Partners
    type: Marketplace
    description: 'null'
  - url: https://www.zendesk.com/pricing/featured/?variant=518&targetRedirect=true
    name: Zendesk Pricing | Plans starting from just $55/month
    type: Pricing
    description: 'null'
  - url: https://www.zendesk.com/register/
    name: Register
    type: SignUp
    description: 'null'
  - url: https://www.zendesk.com/trust-center/
    name: Security, Privacy and Legal | Zendesk Trust Center
    type: Security
    description: 'null'
  - url: https://www.zendesk.com/blog/
    name: Customer experience, support and sales blog | Zendesk
    type: Blog
    description: 'null'
  - url: https://training.zendesk.com/?_gl=1*bjm8lh*_gcl_au*NzkzMDYzNTc4LjE3NTQzMzc4ODI.*_ga*ODQ3OTgwMzk0LjE3NTQzMzc4NDA.*_ga_FBP7C61M6Z*czE3NTQzMzc4ODkkbzEkZzEkdDE3NTQzMzgwODckajQ0JGwwJGgw
    name: Zendesk Training
    type: Training
    description: 'null'
  - url: https://www.zendesk.com/partner/
    name: Partner with Zendesk | Sell, deploy, and build custom solutions
    type: Partners
    description: 'null'
  - url: https://www.zendesk.com/
    name: 'Zendesk: The Complete Customer Service Solution'
    type: Documentation
    description: 'null'
  - url: https://support.zendesk.com/hc/en-us/community/topics
    name: Topics  Zendesk help
    type: Support
    description: 'null'
  - url: https://developer.zendesk.com/documentation/webhooks/
    name: Webhooks | Zendesk Developer Docs
    type: Documentation
    description: 'null'
  - url: https://developer.zendesk.com/documentation
    name: Documentation Home | Zendesk Developer Docs
    type: Portal
    description: 'null'
  - url: https://developer.zendesk.com/api-reference/
    name: API Reference Home | Zendesk Developer Docs
    type: Documentation
    description: 'null'
  - url: https://www.zendesk.com/login/
    name: Login | Zendesk
    type: Login
    description: 'null'
  - url: https://developer.zendesk.com/api-reference/changelog/changelog/
    name: Changelog | Zendesk Developer Docs
    type: ChangeLog
    description: 'null'
  - url: https://developer.zendesk.com/api-reference/introduction/rate-limits/
    name: Rate Limits | Zendesk Developer Docs
    type: RateLimits
    description: 'null'
  - url: https://developer.zendesk.com/api-reference/introduction/security-and-auth/
    name: Security and Authentication | Zendesk Developer Docs
    type: Authentication
    description: 'null'
  - url: https://support.zendesk.com/hc/en-us
    name: Zendesk Support | Help Center
    type: Support
    description: 'null'
  - url: https://developer.zendesk.com/documentation/api-basics/getting-started/zendesk-api-resources/
    name: Zendesk API Resources | Getting Started
    type: GettingStarted
    description: 'null'
  - url: https://www.postman.com/zendesk-redback/zendesk-public-api/overview
    name: Zendesk Public API Workspace | Postman
    type: Documentation
    description: 'null'
  - url: https://github.com/zendesk
    type: GitHubOrganization
  - url: https://github.com/zendesk/zcli
    name: Zendesk CLI
    type: CLI
  - url: https://github.com/zendesk/sunshine-conversations-api-spec
    name: Sunshine Conversations OpenAPI Spec
    type: GitHubRepository
  - type: Features
    data:
      - name: Omnichannel Ticketing
        description: Unified ticket management across email, chat, phone, social media, and messaging channels in a single workspace.
      - name: Help Center and Knowledge Base
        description: Self-service help center with articles, sections, categories, community topics, and full-text search.
      - name: Live Chat and Messaging
        description: Real-time chat with visitors and customers including proactive triggers, routing, departments, and chat history.
      - name: Automations and Triggers
        description: Time-based automations and event-driven triggers to route, escalate, and resolve tickets without manual intervention.
      - name: CRM with Zendesk Sell
        description: Sales CRM with contacts, leads, deals, pipelines, sequences, and activity tracking for sales teams.
      - name: Talk Voice Support
        description: Cloud-based call center with IVR, call recording, voicemail, phone number management, and real-time analytics.
      - name: Custom Objects and Fields
        description: Extend the data model with custom objects, fields, and relationships to fit unique business requirements.
      - name: Webhooks and Integrations
        description: Event-driven webhooks and a marketplace of integrations for connecting Zendesk with third-party tools.
  - type: UseCases
    data:
      - name: Customer Support Operations
        description: Manage the full lifecycle of customer support tickets from creation through resolution across all channels.
      - name: Self-Service Knowledge Management
        description: Build and maintain a searchable knowledge base for customers and agents to reduce ticket volume.
      - name: Sales Pipeline Management
        description: Track leads, contacts, and deals through customizable sales pipelines with activity logging and forecasting.
      - name: Workforce Routing and Optimization
        description: Route tickets to the right agents based on skills, availability, and workload using skill-based routing rules.
      - name: Compliance and Data Privacy
        description: Redact sensitive information from tickets and chats, manage audit logs, and enforce data retention policies.
  - type: Integrations
    data:
      - name: Salesforce
        description: Bidirectional sync between Zendesk Support and Salesforce CRM for unified customer data.
      - name: Slack
        description: Create and manage Zendesk tickets directly from Slack channels with real-time notifications.
      - name: Jira
        description: Link Zendesk tickets to Jira issues for seamless collaboration between support and engineering teams.
      - name: Shopify
        description: View customer order data and manage e-commerce support directly within the Zendesk agent workspace.
      - name: Zendesk Marketplace
        description: Ecosystem of over 1,000 pre-built apps and integrations available through the Zendesk Marketplace.
created: 2025-01-08T00:00:00.000Z
modified: '2026-04-18'
position: Consuming
description: Zendesk provides customer service and engagement software that helps businesses manage support tickets, automate workflows, and offer multi-channel supportincluding email, chat, social media, and phonethrough a unified platform.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---

---
aid: zendesk
url: >-
  https://raw.githubusercontent.com/api-evangelist/zendesk/refs/heads/main/apis.yml
apis:
  - aid: zendesk:assignables
    name: Zendesk Assignables API
    tags:
      - Assignables
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/assignables-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Assignables API lets you find out who or what can be assigned
      to a piece of work—typically a ticket—given your account’s permissions,
      groups, and routing rules. It returns the set of eligible assignees (such
      as agents or groups) for a particular context, so you can build assignee
      pickers in custom apps, validate that an assignment is allowed before
      updating a ticket, or automate routing workflows. By reflecting factors
      like agent roles, group membership, brand or ticket context, and other
      assignment policies, it helps ensure your integrations only propose valid
      assignees and keep assignments consistent with how your Zendesk is
      configured.
  - aid: zendesk:target-type
    name: Zendesk Target Type API
    tags:
      - Target Types
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/target-type-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Target Types API exposes a catalog of the legacy “target”
      integrations your Zendesk account supports—such as email or HTTP/URL
      targets—that triggers and automations can use to send notifications or
      payloads to external systems. It’s primarily a discovery endpoint: it lets
      you list the available target types and see the fields each one requires,
      so you can correctly create target instances with the Targets API. This
      helps tooling and admin workflows know which destinations are supported
      and how to configure them. Note that targets are deprecated in favor of
      Webhooks; the Target Types API mainly exists to support existing
      installations.
  - aid: zendesk:account
    name: Zendesk Account API
    tags:
      - Accounts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/account-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Account API lets you programmatically work with account-level
      records and settings so you can keep Zendesk in sync with the rest of your
      stack. In Zendesk Sell, it exposes endpoints to list, retrieve, create,
      update, and delete “account” objects (the companies you do business with),
      manage custom fields and tags, and relate accounts to contacts and deals,
      with search, filtering, and pagination for efficient data access. In other
      Zendesk products, account-oriented endpoints provide read/write access to
      selected account settings and metadata. The API uses JSON over HTTPS,
      OAuth-based authentication, and enforced rate limits, enabling use cases
      like CRM/ERP synchronization, data enrichment, workflow automation, and
      reporting.
  - aid: zendesk:accounts
    name: Zendesk Accounts API
    tags:
      - Accounts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/accounts-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Sell Accounts API lets you programmatically manage the company
      records (accounts) in your CRM. It provides REST endpoints to create,
      read, update, and delete accounts; search and filter them; and work with
      related data such as associated contacts, deals, activities, notes, tags,
      and custom fields. The API supports pagination for large result sets,
      returns JSON over HTTPS, and authenticates via OAuth or API tokens, making
      it straightforward to keep account data in sync across systems and
      automate sales workflows.
  - aid: zendesk:activities
    name: Zendesk Activities API
    tags:
      - Activities
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/activities-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Sell Activities API lets you programmatically manage the work
      your sales team does—such as calls, emails, meetings, and tasks—by
      creating, reading, updating, and deleting activity records. Activities can
      be linked to leads, contacts, and deals, include details like due dates,
      reminders, outcomes, owners, and notes, and can be filtered and paginated
      by type, status, user, or timeframe. Teams use it to log rep activity from
      external tools (for example, telephony or calendars), keep CRM timelines
      up to date, and power automations and reporting based on completed and
      scheduled work.
  - aid: zendesk:any-channel
    name: Zendesk Any Channel API
    tags:
      - Channels
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/any-channel-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Any Channel API (also called the Channel Framework) lets
      developers turn virtually any external communication source—messaging
      apps, social networks, SMS gateways, custom apps, or other platforms—into
      a first‑class Zendesk channel. It provides endpoints to create and update
      tickets from inbound messages with proper channel attribution, threading,
      attachments, and user identity mapping, plus a “channelback” callback so
      agent replies and updates in Zendesk are delivered back to the original
      channel. It also includes installation and configuration endpoints for
      provisioning, authentication, and per‑brand settings. The result is that
      conversations from unsupported channels flow through Zendesk just like
      native ones, benefiting from routing, SLAs, macros, and reporting while
      your integration handles the translation to and from the external service.
  - aid: zendesk:approval-workflow-instances
    name: Zendesk Approval Workflow Instances API
    tags:
      - Approvals
      - Workflows
      - Instances
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/approval-workflow-instances-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Approval Workflow Instances API lets you programmatically
      start, track, and manage approvals that are built with Zendesk’s workflow
      tools. Using REST endpoints, you can create an instance of a predefined
      approval workflow, associate it with a record such as a ticket, pass input
      data, and then query the instance to monitor its current state and steps.
      The API supports listing and retrieving instances, inspecting pending
      approval tasks and assigned approvers, recording approve/deny decisions,
      and canceling or restarting an approval when needed. It also provides a
      complete audit trail of state changes, making it easy to embed approvals
      into custom apps, automate handoffs between systems, and keep external
      tools in sync with the status of approvals in Zendesk.
  - aid: zendesk:attachments
    name: Zendesk Attachments API
    tags:
      - Attachments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/attachments-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Attachments API lets you handle files that users add to
      Zendesk, primarily for ticket comments (and, via related endpoints, other
      content like help center articles). You upload a file to Zendesk storage
      to get an upload token, then reference that token when creating or
      updating a ticket comment so the file becomes an attachment. The API
      allows you to retrieve attachment metadata (such as filename, size,
      content type, thumbnails, and whether it’s inline), and provides secure
      download URLs that respect your account’s attachment security settings. It
      supports large files and images (including inline images), enforces size
      and type limits, and benefits from Zendesk’s virus scanning. You can also
      clean up or remove attachments subject to permissions and product rules.
      In short, it’s the set of tools for uploading, associating, fetching, and
      managing files that accompany Zendesk records.
  - aid: zendesk:audit-logs
    name: Zendesk Audit Logs API
    tags:
      - Audit Logs
      - Audits
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/audit-logs-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Audit Logs API lets you programmatically retrieve a
      chronological record of important administrative and security-related
      events in your Zendesk account—such as configuration changes, user and
      role updates, authentications, and other actions that affect account
      settings. Each log entry includes who performed the action, what changed,
      when it happened, and contextual details like IP address and event source,
      enabling compliance reporting, forensic investigation, and monitoring in
      external tools (for example, a SIEM). The API returns JSON, supports
      pagination and time-based or type-based filtering, and requires
      appropriate admin-level credentials.
  - aid: zendesk:autocomplete
    name: Zendesk Autocomplete API
    tags:
      - Autocomplete
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/autocomplete-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Autocomplete API provides fast, typeahead-style suggestions
      for common Zendesk resources—most notably users and organizations—so your
      app can quickly find matches as someone types. You send a partial query
      (like a name or email) and get back a small, relevance-ordered list of
      candidates, limited to fields you need (for example, id, name, email) and
      filtered by the requester’s permissions. It’s designed to power UI pickers
      such as Requester, CC, or Organization fields in tickets and admin tools,
      enabling quick selection without running full searches. Because it’s
      optimized for frequent, lightweight calls, it pairs well with client-side
      debouncing and caching and respects Zendesk’s standard rate limits.
  - aid: zendesk:automations
    name: Zendesk Automations API
    tags:
      - Automations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/automations-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Automations API lets you programmatically manage time-based
      business rules that keep Support tickets moving without manual work.
      Automations evaluate ticket conditions on a regular schedule (typically
      hourly) using time metrics like hours since creation, last update, or
      status change, and then perform actions such as changing status or
      priority, reassigning, adding tags, or sending notifications. Via REST
      endpoints you can list, create, update, activate/deactivate, and delete
      automations, enabling you to version, deploy, and audit your rules from
      code. Common uses include escalating aging tickets, sending reminders
      after periods of inactivity, and automatically closing solved tickets
      after a set time, helping teams enforce consistent workflows at scale.
  - aid: zendesk:bookmarks
    name: Zendesk Bookmarks API
    tags:
      - Bookmarks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/bookmarks-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Bookmarks API lets you programmatically manage an agent’s
      personal “starred” items in Zendesk, providing endpoints to list, create,
      and delete bookmarks. A bookmark is a lightweight record that points to
      another Zendesk resource (for example, something an agent wants quick
      access to in the interface), and it’s scoped to the user who created it.
      With the API you can fetch all of a user’s bookmarks, add new ones to
      surface important work, and remove those that are no longer relevant. This
      is useful for automating onboarding defaults, keeping favorites in sync
      across tools, or cleaning up stale shortcuts without manual clicks.
  - aid: zendesk:brand-agents
    name: Zendesk Brand Agents API
    tags:
      - Brand Agents
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/brand-agents-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Brand Agents API lets you programmatically manage which agents
      have access to which brands in a multibrand Zendesk Support account. It
      provides endpoints to list the agents associated with a given brand and to
      add or remove agents from that brand, so you can automate
      onboarding/offboarding, sync brand access from external directories, and
      enforce least‑privilege access at scale. By controlling brand–agent
      associations, you influence which brand’s tickets and communications an
      agent can view and work on, helping keep workflows, routing, and
      compliance clean across multiple brands.
  - aid: zendesk:brands
    name: Zendesk Brands API
    tags:
      - Brands
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/brands-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Brands API is part of the Zendesk Support API that lets you
      programmatically manage a multibrand setup. It provides endpoints to list,
      create, update, delete, and fetch the default brand, along with
      brand-specific settings used across the agent workspace, Help Center, and
      email. Using it, you can provision new brands, set names and visual
      identifiers (like logos), link brands to support addresses and host
      mappings, and control which brand a ticket or end-user experience is
      associated with. This enables automation such as spinning up new branded
      support experiences, keeping branding consistent across channels, and
      segmenting routing and reporting by brand.
  - aid: zendesk:channels
    name: Zendesk Channels API
    tags:
      - Channels
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/channels-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Channels API (Channel Framework) lets developers build custom
      integrations that bring messages from any external source into Zendesk and
      send agent replies back out to the original channel. With it, you can
      register and configure channel accounts, accept inbound messages and
      attachments, map senders to end users, create or update
      tickets/conversations, preserve threading and context with metadata, and
      use channelback to post agent replies to the third‑party system. The
      result is that email, social, messaging, or proprietary platforms become
      first‑class Zendesk channels, so agents work in one workspace while
      customers stay on their channel of choice.
  - aid: zendesk:chat-file-redactions
    name: Zendesk Chat File Redactions API
    tags:
      - Chats
      - Fiiles
      - Redactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/chat-file-redactions-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Chat File Redactions API lets administrators and trusted tools
      permanently remove files that were shared in live chat conversations. By
      redacting a file, its asset is taken out of circulation so it can no
      longer be downloaded or accessed via its URL, helping teams remediate
      accidental sharing of sensitive information and meet privacy or compliance
      requirements (for example, GDPR or CCPA). The redaction targets the file
      itself rather than the entire message, so the conversation history remains
      intact while the file reference is rendered inaccessible or marked as
      removed. Actions are irreversible and are intended for programmatic,
      at-scale cleanups and audit-friendly workflows.
  - aid: zendesk:chat-redactions
    name: Zendesk Chat Redactions API
    tags:
      - Chats
      - Redactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/chat-redactions-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Chat Redactions API lets you programmatically remove sensitive
      information from chat transcripts and any shared files, so teams can meet
      security and privacy requirements without deleting entire conversations.
      You can target specific parts of a message (for example, a credit card
      number or password), redact an entire message, or remove an attachment;
      the change is permanent and designed to preserve the rest of the
      transcript and its metadata. Organizations use it to automate compliance
      tasks such as scrubbing PII, supporting data subject requests, and
      reducing PCI exposure, and to integrate redaction into post-chat
      workflows, bots, or QA processes under role-based access and API rate
      limits.
  - aid: zendesk:comment-redactions
    name: Zendesk Comment Redactions API
    tags:
      - Comments
      - Redactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/comment-redactions-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Comment Redactions API lets you programmatically and
      permanently remove sensitive information from ticket conversations without
      deleting the entire message. By targeting a specific ticket comment and
      supplying the text to scrub (for example, credit card numbers, passwords,
      or PII), the API replaces the matching content in both the plain text and
      HTML versions with a redacted placeholder and records a redaction event in
      the ticket’s audit trail. It can also redact attachments referenced in
      comments, making them inaccessible while preserving the rest of the
      conversation. Redactions are irreversible, apply to search and exports,
      and help teams meet security and compliance requirements (such as PCI or
      privacy policies) by ensuring sensitive data is not retained in Zendesk.
  - aid: zendesk:custom-objects
    name: Zendesk Custom Objects API
    tags:
      - Custom Objects
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/custom-objects-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Custom Objects API lets you model and store your own business
      data—such as orders, subscriptions, devices, or contracts—directly in
      Zendesk and relate it to native resources like tickets, users, and
      organizations. With it, you define object types and fields, create, read,
      update, and delete records, and establish one-to-one or one-to-many
      relationships so agents and workflows can access rich context in the Agent
      Workspace. This enables use cases like surfacing a customer’s order
      history next to a ticket, triggering automations based on object changes,
      and powering custom apps or integrations without maintaining a separate
      data store. It provides permissions and schema management, relationship
      APIs, and record querying to make bespoke data first-class within your
      support platform.
  - aid: zendesk:custom-roles
    name: Zendesk Custom Roles API
    tags:
      - Custom Roles
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/custom-roles-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Custom Roles API lets you programmatically manage the agent
      permission sets used in Zendesk Support (typically on Enterprise plans).
      Through it, you can list and fetch existing roles, create new ones, update
      their names, descriptions, and granular permissions, and delete roles you
      no longer need. A custom role defines what agents can do across areas like
      tickets, users and organizations, business rules, channels, and reporting;
      assigning a role to an agent is done by setting the user’s custom_role_id
      via the Users API. This makes it possible to automate provisioning,
      standardize least‑privilege access across multiple instances, and audit or
      version control your help desk governance, with changes taking effect for
      assigned agents as soon as the role is updated.
  - aid: zendesk:custom-status
    name: Zendesk Custom Status API
    tags:
      - Custom Status
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/custom-status-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Custom Status API lets you programmatically manage the custom
      ticket statuses your account uses beyond the built‑ins. With it, you can
      list and retrieve statuses, create new ones, update labels and
      descriptions for agents and end users, localize translations, activate or
      deactivate statuses, and control their display order. Each custom status
      maps to a standard status category (such as open, pending, on‑hold,
      solved, or closed) so SLAs, views, triggers, automations, and reporting
      continue to work as expected. The API also exposes a custom_status_id
      field on tickets, allowing you to set or change a ticket’s specific custom
      status in workflows and integrations.
  - aid: zendesk:custom-statuses
    name: Zendesk Custom Statuses API
    tags:
      - Custom Statuses
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/custom-statuses-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Custom Statuses API lets you programmatically create, read,
      update, delete, and reorder the custom ticket statuses your account uses,
      giving you more granular workflow states while still rolling up to
      Zendesk’s core status categories (like New, Open, Pending, On-hold,
      Solved, Closed) for SLAs and reporting. With it, you can define agent- and
      end‑user‑facing labels and descriptions, manage which statuses are active,
      set per‑category defaults, and localize labels for different languages.
      You can also retrieve which custom statuses exist, apply a specific custom
      status when updating a ticket, and build business rules or integrations
      that react to or set those statuses—enabling clearer handoffs, queues, and
      reporting without breaking existing triggers, views, or analytics based on
      status categories.
  - aid: zendesk:deleted-tickets
    name: Zendesk Deleted Tickets API
    tags:
      - Deleted Tickets
      - Tickets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/deleted-tickets-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Deleted Tickets API lets you manage tickets that have been
      soft-deleted in Zendesk Support. It provides endpoints to list and inspect
      deleted tickets, restore them to an active state if they were removed by
      mistake, or permanently delete them when you need to purge data. The API
      also supports bulk restore and bulk permanent deletion for handling many
      tickets at once. This is useful for audit and recovery workflows,
      spam/test cleanup, and meeting data-retention or privacy requirements,
      with irreversible results when you hard-delete.
  - aid: zendesk:deleted-users
    name: Zendesk Deleted Users API
    tags:
      - Deleted Users
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/deleted-users-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Deleted Users API lets administrators manage users who have
      been soft-deleted in a Zendesk Support account. It provides endpoints to
      list and inspect deleted user records, restore a deleted user to an active
      state if the deletion was accidental, or permanently purge a user when you
      need to remove their personal data for compliance. Think of it as a
      recycle bin for user accounts: once deleted, a user is inactive and can’t
      access the account, but can still be restored; a purge is irreversible and
      removes the record completely. Access is restricted to authorized roles
      and follows standard Zendesk API authentication and rate limits, making it
      suitable for admin workflows and cleanup scripts.
  - aid: zendesk:deletion-schedules
    name: Zendesk Deletion Schedules API
    tags:
      - Deletion Schedules
      - Schedules
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/deletion-schedules-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Deletion Schedules API lets you programmatically plan and
      manage future-dated deletions of data in Zendesk to meet retention and
      privacy requirements (for example, GDPR/CCPA). Instead of deleting
      immediately, you create schedules that target specific records (such as
      user or ticket data), choose when the deletion should occur, and then
      monitor, update, or cancel those schedules before they run. When a
      schedule reaches its date, Zendesk processes the deletion asynchronously,
      permanently removing or redacting the targeted data and related references
      where required. The API exposes endpoints to create, list, retrieve, and
      manage schedules, surface status and error details, and provide an
      auditable, safer alternative to immediate deletion.
  - aid: zendesk:dynamic-content
    name: Zendesk Dynamic Content API
    tags:
      - Dynamic Content
      - Content
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/dynamic-content-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Dynamic Content API lets you manage reusable, localized text
      snippets—called dynamic content items—so you can keep messages consistent
      across macros, triggers, automations, email notifications, and apps. With
      it, you can programmatically create, read, update, and delete items; add
      and edit language variants; set a default locale; and activate or
      deactivate content. Each item exposes a placeholder (for example, a dc
      token) that you insert in business rules or templates, and Zendesk
      resolves the correct variant at runtime based on the requester’s or
      agent’s locale, falling back to the default when needed. Teams use the API
      to automate translation workflows, bulk-edit copy, and sync content with
      external CMS or localization systems.
  - aid: zendesk:email-notifications
    name: Zendesk Email Notifications API
    tags:
      - Email
      - Notifications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/email-notifications-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Email Notifications API (in Zendesk Support) lets admins and
      developers programmatically inspect the outbound emails Zendesk sends—such
      as ticket update notifications. It exposes searchable delivery logs and
      metadata for each message, including recipient, subject, timestamps,
      delivery status (for example delivered, deferred, bounced, or complaint)
      and failure reasons, plus identifiers that help trace which ticket or
      business rule triggered the email. This makes it easier to audit
      communications, troubleshoot deliverability issues, and pipe notification
      logs into external monitoring or data platforms. The API is read-only—it
      doesn’t send emails itself; sending is still controlled by triggers,
      automations, and other Zendesk workflows.
  - aid: zendesk:group-memberships
    name: Zendesk Group Memberships API
    tags:
      - Groups
      - Memberships
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/group-memberships-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Group Memberships API lets you programmatically manage the
      relationship between users (typically agents) and groups in a Zendesk
      Support account. With it, you can list memberships across the account or
      scoped to a specific user or group, add a user to a group, remove a user
      from a group, and set which group is an agent’s default. Each membership
      ties a user_id to a group_id and can indicate the default group that agent
      belongs to, which affects ticket routing and workflows. The API is
      commonly used to automate onboarding and offboarding, keep teams in sync
      with external directories, and maintain accurate group assignments at
      scale. Admin-level permissions are required for most write operations,
      while agents can generally read their own memberships.
  - aid: zendesk:group-slas
    name: Zendesk Group SLAs API
    tags:
      - Groups
      - Service Level Agreements
      - SLA
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/group-slas-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Group SLAs API lets you manage and report on service-level
      targets that are scoped to support groups, not just to tickets overall.
      With it, you can programmatically create and update SLA policies that
      define different reply and resolution time targets per group, determine
      which policy and targets are applied to a given ticket as it moves between
      groups, and retrieve timing details such as remaining time, breach status,
      and pauses. It also exposes historical and per-segment metrics so you can
      track compliance for each group, power custom dashboards and alerts,
      automate policy rollouts, and export SLA data to your BI tools—all subject
      to plan features that support SLAs and Group SLAs.
  - aid: zendesk:groups
    name: Zendesk Groups API
    tags:
      - Groups
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/groups-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Groups API lets you programmatically manage the agent groups
      that power ticket routing and workflows in Zendesk Support. With it, you
      can create, list, retrieve, update, and delete groups, as well as fetch
      the set of groups a user can assign tickets to (assignable groups). Groups
      are used in ticket assignment, views, macros, and business rules like
      triggers and automations, so the API enables you to integrate group
      management into your provisioning and operations tooling. In conjunction
      with the related Group Memberships endpoints, you can also add or remove
      agents from groups and set a user’s default group to keep team structures
      in sync with your org.
  - aid: zendesk:imports
    name: Zendesk Imports API
    tags:
      - Imports
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/imports-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Imports API lets you programmatically load large volumes of
      records into Zendesk in a controlled, asynchronous way—ideal for
      migrations, initial seeding, or ongoing syncs. You submit a file or
      batched payload, define which object type to import (for example,
      users/organizations/tickets in Support or leads/contacts/deals in Sell),
      and map fields. The import runs as a background job you can monitor via
      status endpoints, with progress, per-row validation, and detailed error
      reporting. It supports creating or updating records at scale, helps
      maintain data consistency (often via external IDs for upserts), and
      removes the need for manual CSV uploads while respecting product-specific
      limits and behaviors.
  - aid: zendesk:incremental
    name: Zendesk Incremental API
    tags:
      - Incremental
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/incremental-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Incremental API lets you export only the records that have
      changed since a specific point in time, making it easy to keep external
      systems in sync without repeatedly pulling full datasets. It supports core
      objects such as tickets, users, organizations, and ticket events,
      returning results in chronological order along with a checkpoint (an
      end_time or a cursor) you store and use on your next request to continue
      exactly where you left off. The cursor-based variant is recommended for
      reliability, minimizing gaps or duplicates during paging. This approach
      reduces bandwidth and API calls, is well-suited for ETL and data
      warehousing, and typically involves polling on a schedule with a small
      delay to account for eventual consistency and rate limits.
  - aid: zendesk:job-statuses
    name: Zendesk Job Statuses
    tags:
      - Jobs
      - Statuses
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/job-statuses-openapi-original.yml
        type: OpenAPI
    description: >-
      Zendesk Job Statuses is the mechanism and API resource that tracks
      long-running, asynchronous tasks kicked off in Zendesk—such as bulk ticket
      updates, user or organization imports, and other “create/update many”
      operations. Instead of waiting for a synchronous response, these endpoints
      return a job ID that you can poll to see whether the work is queued, in
      progress, or completed, along with progress counts, result details, and
      any errors. This approach prevents timeouts on large operations and makes
      them easier to monitor, letting you capture per-record successes and
      failures and trigger retries or follow-up actions. In short, Job Statuses
      gives you visibility and control over bulk operations so you can run them
      safely at scale.
  - aid: zendesk:locales
    name: Zendesk Locales API
    tags:
      - Locales
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/locales-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Locales API is a read-only service that lets you discover
      which languages and regional variants Zendesk supports and which are
      enabled on your account. It provides lists of all supported locales, the
      subsets available to end users and to agents, and the current user’s
      locale, along with metadata such as the locale code (for example, en-US),
      display name, and whether the language is right-to-left. Developers use it
      to drive language pickers, select the correct translations in apps and
      integrations, and coordinate with features like Dynamic Content, Ticket
      Translations, and Help Center localization. The API does not create or
      manage translations or enable languages—that configuration is handled in
      Zendesk admin settings.
  - aid: zendesk:macros
    name: Zendesk Macros API
    tags:
      - Macros
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/macros-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Macros API lets you programmatically manage the reusable,
      predefined actions that agents apply to Support tickets. With it, you can
      list, create, update, delete, and reorder macros; fetch details and
      available action “definitions” to build editors; and determine which
      macros are available for a given ticket and user. It also supports
      previewing or applying a macro’s effects to a ticket, so you can see or
      enact changes like setting fields and status, adding comments, assigning
      agents or groups, adding tags, and updating custom fields. The API
      respects agent permissions and macro visibility (personal vs. shared),
      enabling teams to automate ticket workflows at scale and embed macro
      management into custom tools and integrations.
  - aid: zendesk:oauth
    name: Zendesk Oauth API
    tags:
      - Oauth
      - Authentication
      - Authorization
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/oauth-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk OAuth API implements the OAuth 2.0 standard to let apps
      securely access Zendesk data on a user’s or account’s behalf without
      sharing passwords. Developers register an OAuth client in a Zendesk
      account, redirect users to Zendesk for sign‑in and consent, and exchange
      the returned authorization code for access (and optionally refresh)
      tokens. Those tokens, scoped to specific permissions, are then used as
      Bearer credentials when calling Zendesk REST APIs (for example to read or
      update tickets, users, or help center content). The OAuth flow centralizes
      consent and auditing, supports least‑privilege access, and allows admins
      to revoke or rotate tokens at any time—making it the recommended way to
      authorize third‑party integrations, custom apps, and backend services that
      need ongoing, controlled access to Zendesk resources.
  - aid: zendesk:object-layouts
    name: Zendesk Object Layouts API
    tags:
      - Object Layouts
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/object-layouts-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Object Layouts API lets you programmatically control how
      record pages look and behave in Agent Workspace. It provides CRUD
      endpoints to define which fields and components appear for an object (such
      as tickets, users, organizations, and Sunshine custom objects), how
      they’re grouped and ordered into sections or panels, and any conditional
      visibility rules. You can assign layouts to specific audiences and
      contexts—like ticket forms, brands, roles, or groups—so different users or
      records see the most relevant view. This enables teams to standardize the
      agent experience, automate layout changes, and promote configurations
      between sandbox and production as part of CI/CD.
  - aid: zendesk:organization-fields
    name: Zendesk Organization Fields API
    tags:
      - Organization Fields
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/organization-fields-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Organization Fields API lets you define and manage the custom
      fields that appear on organization records in Zendesk Support. You can
      list and inspect existing fields; create new ones with types like text,
      textarea, checkbox, date, integer, decimal, regexp-validated text, and
      dropdown (with custom options); update labels, descriptions, keys, active
      state, and position; reorder how fields appear; and delete fields you no
      longer need (system fields can’t be removed). The API manages the
      schema—the field definitions—while actual values for each organization are
      set via the Organizations API by writing to the organization_fields
      object. These fields can be used in the agent interface, business rules,
      and reporting.
  - aid: zendesk:organization-memberships
    name: Zendesk Organization Memberships API
    tags:
      - Organization Memberships
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/organization-memberships-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Organization Memberships API lets you programmatically manage
      the links between users and organizations in Zendesk. With it, you can
      create, list, find, and delete organization membership records; query
      memberships for a specific user or organization or across the account; set
      a user’s default organization; and perform bulk create/destroy operations
      to keep memberships in sync with external directories. These memberships
      determine which organization a user belongs to (users can belong to
      multiple orgs) and power organization-based ticket association, routing,
      visibility, and reporting, making it useful for provisioning,
      onboarding/offboarding, and segmenting support workflows.
  - aid: zendesk:organization-merges
    name: Zendesk Organization Merges API
    tags:
      - Organization Merges
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/organization-merges-openapi-original.yml
        type: OpenAPI
    description: >-
      Zendesk’s Organization Merges API lets you consolidate two organizations
      into one clean record by merging a “source” organization into a “target.”
      During a merge, all users belonging to the source organization are moved
      to the target, and tickets associated with the source (as requester or via
      organization) are re-associated to the target, preserving ticket history
      and continuity. The target organization’s profile and settings remain the
      canonical record after the merge, while the source organization is
      removed. This is typically used to eliminate duplicates or combine
      companies after changes like acquisitions, and it’s an irreversible
      operation designed to keep your data tidy without disrupting ongoing
      support activity.
  - aid: zendesk:organization-subscriptions
    name: Zendesk Organization Subscriptions API
    tags:
      - Organization Subscriptions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/organization-subscriptions-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Organization Subscriptions API lets you programmatically
      manage which users “follow” an organization so they automatically receive
      notifications about that organization’s ticket activity. Using it, you can
      create and delete subscriptions, list who is subscribed to a specific
      organization, list the organizations a user is subscribed to, and retrieve
      individual subscription records. It’s commonly used to keep account
      managers or support teams informed about all tickets from a given customer
      organization without manually adding followers to every ticket.
  - aid: zendesk:organizations
    name: Zendesk Organizations API
    tags:
      - Organizations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/organizations-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Organizations API is a RESTful interface for managing the
      companies or groups that your users belong to in Zendesk Support. It lets
      you create, read, update, and delete organizations; set attributes like
      domains, notes, tags, external_id, and custom fields; and configure
      behaviors such as shared tickets and comments. You can search and list
      organizations, use autocomplete, merge duplicates, and perform bulk
      operations via asynchronous jobs to import or update many records at once.
      The API also manages organization memberships, allowing you to add or
      remove users from organizations and set a user’s default organization.
      Typical uses include syncing accounts from a CRM, automatically mapping
      users to organizations by email domain, enforcing ticket-sharing rules,
      and driving routing, SLA, and reporting by account. All endpoints use JSON
      over HTTPS and support pagination and standard Zendesk rate limiting.
  - aid: zendesk:problems
    name: Zendesk Problems API
    tags:
      - Problems
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/problems-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Problems API helps you manage “problem” tickets and their
      relationship to “incident” tickets, so you can track and resolve
      widespread issues affecting multiple customers. It provides endpoints to
      list and query problem tickets and to retrieve the incidents linked to a
      specific problem (for example, to understand scope and impact). While you
      create or update problems and incidents through the standard Tickets API
      by setting the ticket type (problem or incident) and linking incidents via
      a problem_id, the Problems API offers convenient ways to discover existing
      problems (including auto-complete style lookup) and to pull the full set
      of related incidents for reporting, triage, and coordination of fixes.
  - aid: zendesk:push-notification-devices
    name: Zendesk Push Notification Devices API
    tags:
      - Push Notifications
      - Devices
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/push-notification-devices-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Push Notification Devices API lets you register and manage the
      mobile devices that should receive push notifications for a given Zendesk
      user. With it, you can create device records using the app’s push token
      (APNs for iOS, FCM/GCM for Android), list the devices linked to a user,
      update or disable a device entry, and delete registrations when a user
      signs out or a device is replaced. Your mobile app typically calls this
      API to send its current push token to Zendesk, and Zendesk uses the stored
      records to route ticket, messaging, and other product notifications to the
      right devices; invalid or expired tokens are detected and can be
      deactivated to keep the registry accurate.
  - aid: zendesk:queues
    name: Zendesk Queues API
    tags:
      - Queues
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/queues-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Queues API provides programmatic control over the queues that
      route work to agents across channels, letting you define and manage how
      tickets, messages, or calls are prioritized and assigned, and monitor how
      those queues are performing. In practice, it’s used to create and
      configure queues (for example, eligibility rules, skills or group routing,
      and priority), manage membership and capacity, move or reprioritize items,
      and surface operational telemetry like queue size, wait times, oldest item
      age, SLA risk, and agent availability. Teams use it to automate routing
      policies, build real-time dashboards, trigger staffing or workflow
      adjustments, and integrate Zendesk with workforce management or custom
      operations tools. The exact endpoints and data available can vary by
      product area (e.g., Support, Messaging, or Talk) and plan.
  - aid: zendesk:recipient-addresses
    name: Zendesk Recipient Addresses API
    tags:
      - Recipients
      - Addresses
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/recipient-addresses-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Recipient Addresses API lets you programmatically manage the
      email identities your Zendesk Support account can send from in ticket
      notifications. It allows you to list existing addresses, create new ones
      (often associated with specific brands), update properties like the
      display name, initiate or check verification status, set a default sender,
      and delete addresses. By maintaining a verified set of recipient
      addresses, you control which “From” address appears on outbound emails
      from triggers, automations, and agent replies, enabling multi-brand or
      department-specific sender identities while ensuring proper domain
      ownership and email authentication.
  - aid: zendesk:relationships
    name: Zendesk Relationships API
    tags:
      - Relationships
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/relationships-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Relationships API lets you model, create, and query links
      between data entities in Zendesk, spanning both standard resources (like
      users, organizations, and tickets) and Custom Objects. You define
      relationship types with explicit cardinality (one-to-one, one-to-many, or
      many-to-many), then create relationship records that connect specific
      instances—for example, associating a customer with their devices,
      subscriptions, or locations, or tying tickets to assets or accounts. The
      API provides endpoints to manage relationship types and records, and to
      fetch related records from either side of a relationship, enabling
      graph-like traversal of your data. This makes it easier to build apps and
      workflows that surface rich context to agents, power automation, and
      support reporting across interconnected business objects.
  - aid: zendesk:requests
    name: Zendesk Requests API
    tags:
      - Requests
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/requests-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Requests API is the end-user–facing interface for support
      tickets, designed for customers to create, view, and update their own
      requests from web or mobile apps without agent credentials. It provides
      endpoints to submit a new request, list a user’s existing requests, get
      details for a specific request, add comments, include attachments (via
      upload tokens), and check request counts or status. Unlike the Tickets
      API, it enforces end-user permissions—users can access only their own
      requests (or their organization’s if allowed)—and exposes a simplified set
      of fields that are safe for customers to see or edit. It’s commonly used
      to power Help Center contact forms, mobile app support flows, and custom
      portals where customers can submit and track support issues.
  - aid: zendesk:resource-collections
    name: Zendesk Resource Collections API
    tags:
      - Resources
      - Collections
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/resource-collections-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Resource Collections API provides a single, consistent way to
      list and retrieve Zendesk objects—such as tickets, users, organizations,
      and knowledge content—without having to call product‑specific endpoints.
      It exposes these objects as uniform “collections” that support filtering,
      sorting, field selection, and pagination, making it easier to fetch
      exactly the data your app or integration needs. The API enforces agent and
      end‑user permissions automatically and returns standardized response
      shapes and metadata, so you can build list views, dashboards, and
      workflows with less custom logic. It’s designed for efficient, scalable
      reads and can include related resources to reduce the number of network
      calls. In short, it unifies and streamlines read access to Zendesk data
      across products.
  - aid: zendesk:routing
    name: Zendesk Routing API
    tags:
      - Routing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/routing-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Routing API gives you programmatic control over how customer
      work is distributed to agents across channels. It lets you create and
      update “work items” (from tickets, messaging conversations, calls, or
      external tasks), enrich them with attributes such as skills, priority, and
      required capacity, and have Zendesk’s omnichannel router match them to
      available agents based on unified agent status and capacity limits.
      Through the API you can manage skills and queues, define or influence
      routing policies, retrieve assignment candidates and reservations, accept
      or decline assignments, requeue or escalate items, and track routing
      events for auditing and reporting. In short, it enables skills‑based,
      priority‑based, and capacity‑aware routing and makes it possible to extend
      Zendesk’s built‑in routing to custom workflows and channels.
  - aid: zendesk:satisfaction-ratings
    name: Zendesk Satisfaction Ratings API
    tags:
      - Satisfaction Ratings
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/satisfaction-ratings-openapi-original.yml
        type: OpenAPI
    description: >-
      Zendesk’s Satisfaction Ratings API lets you programmatically work with
      customer satisfaction (CSAT) results tied to Support tickets. It provides
      endpoints to retrieve and page through ratings, fetch a single rating, and
      access details such as score (good/bad), optional comment, associated
      ticket, assignee, and timestamps—so you can build custom reports, trigger
      automations, or sync CSAT data to other systems. You can filter and sort
      results to focus on specific time periods, agents, groups, or outcomes,
      enabling deeper analysis of post‑resolution feedback and trends without
      relying solely on the Zendesk UI.
  - aid: zendesk:satisfaction-reasons
    name: Zendesk Satisfaction Reasons API
    tags:
      - Satisfaction Reasons
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/satisfaction-reasons-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Satisfaction Reasons API lets you programmatically manage the
      predefined list of reasons customers can choose when they leave a bad
      satisfaction rating on a ticket. With it, admins can list, create, update,
      reorder, activate/deactivate, and delete reasons that appear in the
      follow‑up survey, ensuring the choices align with current operations or
      policies. Each reason has metadata (such as title, position, and status),
      and selections made by customers are stored with the ticket’s satisfaction
      rating, enabling more granular reporting and analysis of negative
      feedback. This makes it easy to standardize reasons across environments,
      localize text, and automate changes as your support workflows evolve.
  - aid: zendesk:search
    name: Zendesk Search API
    tags:
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/search-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Search API lets you programmatically find records across your
      Zendesk Support account—primarily tickets, users, and organizations—using
      a flexible query language that mixes free text with field-based filters
      (for example, type:ticket, status, tags, assignee, requester, or date
      ranges). It returns a paginated, relevance-ranked set of matches,
      identifies the object type for each result, supports scoping searches to a
      single type and basic sorting, and respects the permissions of the
      authenticated user. Teams use it to power custom lookups, embed context in
      apps, and drive automations or reports that need to locate the right
      Zendesk records quickly.
  - aid: zendesk:sessions
    name: Zendesk Sessions API
    tags:
      - Sessions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/sessions-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Sessions API lets you audit and control users’ active sign-in
      sessions in your Zendesk account. It provides endpoints to list current
      sessions (for the authenticated user or a specified user) and returns
      metadata such as device/user agent, IP, creation time, and last activity.
      You can revoke an individual session or all sessions for a user to force
      logouts across Zendesk web and mobile experiences—useful for security
      incidents, offboarding, and SSO changes. Access is limited to
      appropriately permissioned admins or OAuth tokens with the required
      scopes, and it governs interactive login sessions rather than API tokens.
  - aid: zendesk:sharing-agreements
    name: Zendesk Sharing Agreements API
    tags:
      - Sharing Agreements
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/sharing-agreements-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Sharing Agreements API lets you programmatically set up and
      manage ticket‑sharing relationships between separate Zendesk accounts so
      teams can collaborate on the same customer issues across instances. With
      it, you can create, list, update, and delete sharing agreements; send and
      respond to invitations; define rules and trust settings that control which
      tickets can be shared and what data is synchronized; and monitor or revoke
      agreements as needs change. Once in place, an agreement keeps shared
      tickets in sync (for example, comments and status), enabling partners,
      vendors, or subsidiaries running their own Zendesk to work together
      securely without merging accounts.
  - aid: zendesk:skips
    name: Zendesk Skips API
    tags:
      - Skips
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/skips-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Skips API provides programmatic access to events where an
      agent doesn’t accept or actively skips a routed work item (such as a
      ticket or conversation) in omnichannel routing. It records who skipped,
      what was skipped, when it happened, and (when available) the reason, so
      you can analyze agent behavior, fine‑tune routing rules and capacity, and
      troubleshoot assignment flows. By querying skips over time or by
      agent/queue, teams can spot patterns like frequent timeouts, identify
      training or staffing needs, and build custom dashboards or automation that
      reacts to repeated skips. In short, it turns “skip” actions into
      structured data you can use to monitor, report, and optimize your
      assignment process.
  - aid: zendesk:slas
    name: Zendesk SLAs API
    tags:
      - SLAs
      - Service Level Agreements
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slas-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk SLAs API lets you programmatically manage and track service
      level agreement policies in Zendesk Support. It enables you to list,
      create, update, delete, and reorder SLA policies that set time targets—per
      priority and schedule—for metrics like first reply time, next reply time,
      periodic update, requester wait time, agent work time, and resolution
      time. You can also fetch the SLA targets and live status applied to
      individual tickets (such as target timestamps, remaining time, and whether
      a target is active, paused, or breached). This makes it possible to build
      custom dashboards, alerts, and automations, and to report on SLA
      compliance and breaches over time, with support for business hours and
      multiple schedules.
  - aid: zendesk:suspended-tickets
    name: Zendesk Suspended Tickets API
    tags:
      - Suspended Tickets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/suspended-tickets-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Suspended Tickets API lets you programmatically find and
      manage inbound emails that Zendesk quarantines as “suspended” before they
      become tickets. You can list and inspect these messages—including subject,
      body, sender, recipients, and the machine-readable reason they were
      suspended (such as spam, auto-reply, bounces, or mail loops)—and then
      either recover them to create normal tickets or permanently delete them,
      individually or in bulk. This enables automated monitoring and triage of
      false positives and keeps the queue clean without using the web interface.
      Suspended items have their own IDs and don’t become tickets until
      recovered, at which point a new ticket with a different ID is created,
      subject to the appropriate permissions in Zendesk Support.
  - aid: zendesk:tags
    name: Zendesk Tags API
    tags:
      - Tags
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/tags-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Tags API (part of the Support API) lets you programmatically
      manage the free‑form tags used to categorize records in Zendesk. It
      provides REST endpoints to list all tags in an account (including
      occurrence counts), retrieve the tags on a specific ticket, user, or
      organization, and add, remove, or replace those tags. It also supports tag
      name autocomplete to help maintain consistency. By automating tag
      management, you can drive routing and prioritization, power triggers and
      automations, build targeted views and reports, and keep your data labeled
      consistently across tickets, users, and organizations.
  - aid: zendesk:target-failures
    name: Zendesk Target Failures API
    tags:
      - Target Failures
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/target-failures-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Target Failures API helps you monitor and troubleshoot failed
      delivery attempts to legacy “targets” (such as HTTP, URL, or email
      targets) that triggers and automations use to send outbound notifications.
      It lets you list and inspect recent failures for a target, including
      details like when they occurred, how many times delivery was attempted,
      the error or HTTP status returned by the destination, and other diagnostic
      information. This makes it easier to identify issues such as misconfigured
      endpoints, authentication problems, or downtime on the receiving service.
      You can use the API to review and clear failures so you can restore
      delivery if a target has been automatically suspended after repeated
      errors. Note: Zendesk targets have been superseded by webhooks in many
      accounts, but the Target Failures API remains useful where targets are
      still in use.
  - aid: zendesk:targets
    name: Zendesk Targets API
    tags:
      - Targets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/targets-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Targets API lets you programmatically manage “targets,” which
      are external destinations that Zendesk Support triggers and automations
      can notify when conditions are met. Using the API, you can create, list,
      update, activate/deactivate, and delete targets, configure details such as
      URLs, HTTP methods, authentication, and content types, and review delivery
      failures to troubleshoot outbound notifications. Targets enable Zendesk to
      push ticket events or custom payloads to systems outside Zendesk (for
      example, HTTP endpoints or email). Note that targets are a legacy feature
      and have been superseded by Zendesk Webhooks; for new integrations,
      Zendesk recommends using the Webhooks API.
  - aid: zendesk:ticket-audits
    name: Zendesk Ticket Audits API
    tags:
      - Ticket Audits
      - Audits
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/ticket-audits-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Ticket Audits API exposes the complete, immutable change
      history of a Support ticket, letting you retrieve every audit generated
      whenever a ticket is created or updated. Each audit contains timestamped
      events that record who made a change and how it happened (agent, end user,
      trigger, automation, or API), along with metadata such as author, channel,
      and system details. By reading audits you can reconstruct a ticket’s state
      over time, including comments and attachments, field and status/assignee
      changes, tag edits, notifications, satisfaction ratings, and voice
      comments—useful for troubleshooting workflows, compliance/forensics,
      analytics, and integrations. The API lets you list all audits for a ticket
      or fetch a specific audit, and it also supports redacting sensitive text
      or attachments from comments when necessary.
  - aid: zendesk:ticket-content-pins
    name: Zendesk Ticket Content Pins API
    tags:
      - Ticket Content
      - Pins
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/ticket-content-pins-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Ticket Content Pins API lets you programmatically manage the
      “pinned” references that keep important information visible on a support
      ticket. With it, you can create, list, reorder, and remove pins that point
      to helpful resources (such as Help Center articles or other relevant
      content) or key pieces of ticket context, so agents and collaborators
      always see the most important guidance first. This enables teams to
      automate pinning based on business rules, surface consistent answers
      across escalations, and analyze which content is most often pinned to
      improve knowledge quality. The API respects existing permissions and
      records metadata (for example, who pinned an item and when), making it
      easier to govern and audit knowledge-use on tickets.
  - aid: zendesk:ticket-fields
    name: Zendesk Ticket Fields API
    tags:
      - Ticket Fields
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/ticket-fields-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Ticket Fields API lets you programmatically manage the
      structured fields that appear on Zendesk Support tickets. With it, you can
      list, create, update, delete, and reorder ticket fields; define field
      types (such as text, textarea, checkbox, date, dropdown, or multiselect)
      and options for picklists; control properties like title and description,
      position, active/required status, and visibility/editability for agents
      and end users; localize labels; and retrieve both custom and system
      fields. Teams use it to standardize data capture, automate configuration
      across environments, and keep field definitions in sync with external
      tools and workflows.
  - aid: zendesk:ticket-form-statuses
    name: Zendesk Ticket Form Statuses API
    tags:
      - Ticket Forms
      - Statuses
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/ticket-form-statuses-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Ticket Form Statuses API lets you control which ticket
      statuses (including custom ticket statuses) are available on each ticket
      form, so you can tailor status options to different request types or
      brands. With it, admins can retrieve the current status configuration for
      a form and update which statuses are enabled or hidden from agents and end
      users, helping simplify workflows and reduce confusion. The API returns
      details such as status IDs, names, and their category (for example, New,
      Open, Pending, On-hold, Solved), making it clear how each status maps to
      broader lifecycle stages. It doesn’t create or manage the statuses
      themselves—that’s handled by the Ticket Statuses/Custom Ticket Statuses
      API—rather, it manages the association between forms and statuses. Typical
      uses include limiting irrelevant statuses on specific forms, ensuring
      consistent agent experiences, and aligning form behavior with business
      processes, all under standard admin permissions and rate limits.
  - aid: zendesk:ticket-forms
    name: Zendesk Ticket Forms API
    tags:
      - Tickets
      - Forms
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/ticket-forms-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Ticket Forms API lets you programmatically create, read,
      update, delete, and reorder the ticket forms that shape how tickets are
      submitted and displayed in Zendesk Support. Each form defines which ticket
      fields appear and in what order, enabling you to tailor the submission
      experience for different request types, workflows, or brands. You can
      control properties such as the form’s name and display name, whether it’s
      visible to end users, its default status, and its position. The API also
      supports assigning forms to brands and specifying the set of
      ticket_field_ids a form uses, so you can maintain distinct configurations
      across products or audiences. In short, it provides end-to-end management
      of the forms that drive consistent, contextual data collection from both
      customers and agents.
  - aid: zendesk:ticket-metrics
    name: Zendesk Ticket Metrics API
    tags:
      - Tickets
      - Metrics
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/ticket-metrics-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Ticket Metrics API lets you programmatically access the
      operational and SLA metrics that Zendesk calculates for each support
      ticket. It provides per‑ticket summaries such as first reply time, full
      resolution time, requester and agent wait times, on‑hold time, number of
      replies and reopens, and key timestamps (for example, assigned and
      solved), often available in both calendar and business minutes. In
      addition to these summaries, an incremental Ticket Metric Events endpoint
      streams metric changes over time, enabling near‑real‑time monitoring and
      reliable ETL into analytics tools. Teams use the API to build custom
      dashboards, track SLA compliance, analyze trends, and join metrics to
      tickets by ticket_id for full context.
  - aid: zendesk:tickets
    name: Zendesk Tickets API
    tags:
      - Tickets
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/tickets-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Tickets API is the primary REST interface for managing support
      tickets programmatically. It lets you create, read, update, and delete
      tickets; set core and custom fields (status, priority, type, assignee,
      requester, organization, tags); and add public or internal comments with
      file attachments. You can manage participants (CCs,
      followers/collaborators), retrieve full ticket audits to see change and
      comment history, access satisfaction ratings, perform bulk updates or
      merges via asynchronous jobs, and keep external systems in sync using
      incremental ticket and ticket-event exports. Many endpoints support
      sideloading related users, groups, and organizations to reduce round
      trips, and standard features like pagination, sorting, and rate limits
      apply. The API uses JSON over HTTPS and supports authentication with OAuth
      or API tokens, making it a common backbone for integrating CRMs, issue
      trackers, custom portals, and automation workflows with Zendesk Support.
  - aid: zendesk:trigger-categories
    name: Zendesk Trigger Categories API
    tags:
      - Triggers
      - Categories
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/trigger-categories-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Trigger Categories API lets you programmatically organize
      Zendesk Support triggers into logical groups, making large sets of
      business rules easier to manage at scale. It provides endpoints to list
      and retrieve categories, create, rename, reorder, and delete them, and to
      assign or move triggers between categories or fetch the triggers within a
      category. This enables automated provisioning and cleanup, consistent
      organization across environments (such as staging and production), and
      bulk maintenance of triggers without relying on the Admin Center UI.
  - aid: zendesk:triggers
    name: Zendesk Triggers API
    tags:
      - Triggers
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/triggers-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Triggers API lets you programmatically manage the ticket
      triggers that power automation in Zendesk Support. Triggers are
      event‑based business rules that run immediately after a ticket is created
      or updated; when their conditions match, they perform actions like
      assigning or routing tickets, adding/removing tags, setting fields or
      status, sending notifications, and invoking webhooks. Through the API you
      can list and retrieve triggers, create and update them (including their
      all/any conditions and actions), enable or disable them, delete them, and
      reorder their execution priority; you can also organize triggers via
      categories. It’s a REST/JSON interface that requires admin credentials
      (API token or OAuth), making it useful for versioning and deploying
      workflows, syncing configurations across environments, or integrating
      Zendesk ticket flows with external systems.
  - aid: zendesk:uploads
    name: Zendesk Uploads API
    tags:
      - Uploads
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/uploads-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Uploads API lets you upload files to Zendesk Support so they
      can be attached to tickets or embedded inline in ticket comments. When you
      POST a file, the API creates an upload and returns metadata plus a
      short-lived token. You then include one or more of these tokens when
      creating or updating a ticket to add the files as attachments. The API
      supports single-shot and chunked uploads (for large files), and provides
      endpoints to check an upload’s details or delete it. It’s commonly used to
      handle user-provided screenshots, logs, and other assets, and to insert
      inline images in rich-text comments via the returned content URLs.
  - aid: zendesk:user-fields
    name: Zendesk User Fields API
    tags:
      - User Fields
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/user-fields-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk User Fields API lets you programmatically define and manage
      the custom attributes you store on users in Zendesk Support. You can list,
      create, update, and delete user fields (such as text, number, date,
      checkbox, or dropdown), which become part of your user schema and appear
      on user profiles for agents. After defining fields, you read and write
      their values through the Users API (in the user_fields object) to enrich
      profiles with data like plan, region, lifecycle stage, or account owner.
      These attributes can then be surfaced in the agent experience and used by
      business rules, views, and reporting to segment users, personalize
      workflows, and drive routing and automation.
  - aid: zendesk:users
    name: Zendesk Users API
    tags:
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/users-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Users API is part of the Zendesk Support REST API and lets you
      programmatically manage the people in your account—end users, agents, and
      admins. It provides endpoints to list, search, create, update, and delete
      users; manage roles, tags, custom fields, organization and group
      memberships; handle user identities (such as email addresses and phone
      numbers) and verification; set avatars; suspend or reactivate accounts;
      and merge duplicate users. It also supports bulk create/update/delete and
      incremental exports for large-scale synchronization. Common uses include
      keeping your user directory in sync with external systems, automating
      provisioning and deprovisioning, and enriching support workflows that
      depend on requester or assignee data.
  - aid: zendesk:views
    name: Zendesk Views API
    tags:
      - Views
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/views-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Views API lets you programmatically manage and use ticket
      views—the saved sets of filtering, sorting, and column rules that define
      agent queues. With it, you can list and fetch views (personal or shared),
      create, update, delete, and reorder them, and “execute” a view to retrieve
      the current tickets that match its conditions along with counts. It also
      supports previewing a set of conditions before saving a view, exporting
      view results (e.g., for reporting), and accessing metadata like counts for
      dashboards. This enables automation of queue setup, custom dashboards,
      scheduled exports, and other workflow integrations, all under Zendesk’s
      authentication and permission model (e.g., admins managing shared views,
      agents managing personal views).
  - aid: zendesk:workspaces
    name: Zendesk Workspaces API
    tags:
      - Workspaces
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/workspaces-openapi-original.yml
        type: OpenAPI
    description: >-
      The Zendesk Workspaces API lets you programmatically create, read, update,
      delete, and prioritize contextual workspaces that shape the Agent
      Workspace experience. With it, admins define the conditions under which a
      workspace applies (for example by brand, channel, group, ticket form, or
      other ticket attributes) and configure what agents see and use when
      handling a ticket—such as the ticket layout and fields, which sidebar apps
      open or are shown, and available tools or macros. This makes it easier to
      standardize, version, and automate agent UI configurations across teams,
      brands, and environments.
name: Zendesk
tags:
  - Support
  - Tickets
  - Ticketing
  - T1
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
    type: Status
    description: 'null'
  - url: >-
      https://www.zendesk.com/company/agreements-and-terms/zendesk-customer-agreement/
    name: Zendesk Customer Agreement
    type: TermsOfService
    description: 'null'
  - url: >-
      https://www.zendesk.com/help-center-closed/?utm_source=helpcenter-closed&utm_medium=poweredbyzendesk&utm_campaign=text&utm_content=developerblog.zendesk.com
    name: Help Center Closed
    type: Blog
    description: 'null'
  - url: https://www.zendesk.com/marketplace/
    name: Zendesk Marketplace - Find Apps, Integrations & Partners
    type: Integrations
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
  - url: >-
      https://training.zendesk.com/?_gl=1*bjm8lh*_gcl_au*NzkzMDYzNTc4LjE3NTQzMzc4ODI.*_ga*ODQ3OTgwMzk0LjE3NTQzMzc4NDA.*_ga_FBP7C61M6Z*czE3NTQzMzc4ODkkbzEkZzEkdDE3NTQzMzgwODckajQ0JGwwJGgw
    name: Zendesk Training
    type: Training
    description: 'null'
  - url: https://www.zendesk.com/partner/
    name: Partner with Zendesk | Sell, deploy, and build custom solutions
    type: Partners
    description: 'null'
  - url: https://www.zendesk.com/
    name: 'Zendesk: The Complete Customer Service Solution'
    type: Website
    description: 'null'
  - url: https://support.zendesk.com/hc/en-us/community/topics
    name: Topics  Zendesk help
    type: Forums
    description: 'null'
  - url: https://developer.zendesk.com/documentation/webhooks/
    name: Webhooks | Zendesk Developer Docs
    type: Webhooks
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
created: '2025-01-08'
modified: '2025-10-18'
position: Consuming
description: >-
  Zendesk provides customer service and engagement software that helps
  businesses manage support tickets, automate workflows, and offer multi-channel
  supportincluding email, chat, social media, and phonethrough a unified
  platform.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---
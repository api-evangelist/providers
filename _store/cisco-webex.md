---
aid: cisco-webex
name: Cisco Webex
description: Cisco Webex is a comprehensive collaboration platform that provides video conferencing, team messaging, file sharing, and calling capabilities for businesses and teams. The Webex developer platform offers REST APIs, SDKs, and integrations for extending and automating collaboration workflows across meetings, messaging, calling, devices, administration, and contact center scenarios. Authentication uses OAuth 2.0 access tokens, personal access tokens, or service apps and all endpoints are served from the webexapis.com base.
image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
url: https://raw.githubusercontent.com/api-evangelist/cisco-webex/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consumer
created: '2024-01-01'
modified: '2026-04-23'
specificationVersion: '0.19'
tags:
  - Collaboration
  - Communications
  - Meetings
  - Messaging
  - Teams
  - Video Conferencing
apis:
  - aid: cisco-webex:webex-meetings-api
    name: Webex Meetings API
    description: Enables scheduling, managing, and controlling Webex meetings programmatically. Provides endpoints for creating meetings, managing attendees, preferences, and retrieving meeting details.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/meetings
    baseURL: https://webexapis.com/v1
    tags:
      - Attendees
      - Conferencing
      - Meetings
      - Scheduling
      - Video
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/meetings
      - type: OpenAPI
        url: openapi/cisco-webex-meetings-openapi.yml
      - type: Authentication
        url: https://developer.webex.com/docs/getting-started#authentication
  - aid: cisco-webex:webex-messaging-api
    name: Webex Messaging API
    description: Send and receive messages, manage spaces and teams, and share files within the Webex messaging platform. Supports rich text, file attachments, and adaptive cards.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/messaging
    baseURL: https://webexapis.com/v1
    tags:
      - Chat
      - Collaboration
      - Messaging
      - Spaces
      - Teams
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/messaging
      - type: OpenAPI
        url: openapi/cisco-webex-messaging-openapi.yml
      - type: Webhooks
        url: https://developer.webex.com/docs/webhooks
      - type: Getting Started
        url: https://developer.webex.com/messaging/docs/getting-started
  - aid: cisco-webex:webex-people-api
    name: Webex People API
    description: Access user profile information, manage contacts, and administer user accounts within an organization. Supports listing, creating, updating, and deleting people records.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/people
    baseURL: https://webexapis.com/v1
    tags:
      - Contacts
      - Directory
      - People
      - Profiles
      - Users
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/people
      - type: OpenAPI
        url: openapi/cisco-webex-people-openapi.yml
  - aid: cisco-webex:webex-teams-api
    name: Webex Teams API
    description: Create and manage teams and team memberships within Webex. Teams group people and spaces together for organized collaboration across projects and departments.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/teams
    baseURL: https://webexapis.com/v1
    tags:
      - Collaboration
      - Groups
      - Membership
      - Organization
      - Teams
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/teams
      - type: OpenAPI
        url: openapi/cisco-webex-teams-openapi.yml
  - aid: cisco-webex:webex-rooms-api
    name: Webex Rooms API
    description: Create and manage Webex spaces (rooms) for collaboration. Rooms are virtual meeting places where people post messages and collaborate, and can be organized within teams.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/rooms
    baseURL: https://webexapis.com/v1
    tags:
      - Channels
      - Collaboration
      - Messaging
      - Rooms
      - Spaces
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/rooms
      - type: OpenAPI
        url: openapi/cisco-webex-rooms-openapi.yml
  - aid: cisco-webex:webex-webhooks-api
    name: Webex Webhooks API
    description: Register webhooks to receive real-time HTTP callbacks when specific events occur in Webex. Supports filtering by resource type, event type, and other criteria for efficient event-driven integrations.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/webhooks
    baseURL: https://webexapis.com/v1
    tags:
      - Callbacks
      - Events
      - Notifications
      - Real-Time
      - Webhooks
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/webhooks
      - type: OpenAPI
        url: openapi/cisco-webex-webhooks-openapi.yml
  - aid: cisco-webex:webex-devices-api
    name: Webex Devices API
    description: Manage and control Webex devices and room systems. Provides endpoints for listing, creating, and managing device configurations, activations, and workspace assignments.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/devices
    baseURL: https://webexapis.com/v1
    tags:
      - Devices
      - Hardware
      - Management
      - Room Systems
      - Workspaces
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/devices
      - type: OpenAPI
        url: openapi/cisco-webex-devices-openapi.yml
  - aid: cisco-webex:webex-memberships-api
    name: Webex Memberships API
    description: Manage room memberships representing a person's relationship to a room. Use this API to list members of any room, create memberships to invite users, and update or remove memberships.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/memberships
    baseURL: https://webexapis.com/v1
    tags:
      - Access Control
      - Memberships
      - Permissions
      - Rooms
      - Users
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/memberships
      - type: OpenAPI
        url: openapi/cisco-webex-memberships-openapi.yml
  - aid: cisco-webex:webex-team-memberships-api
    name: Webex Team Memberships API
    description: Manage team memberships representing a person's relationship to a team. Use this API to add and remove people from teams and manage team membership roles.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/team-memberships
    baseURL: https://webexapis.com/v1
    tags:
      - Access Control
      - Collaboration
      - Roles
      - Team Memberships
      - Teams
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/team-memberships
      - type: OpenAPI
        url: openapi/cisco-webex-team-memberships-openapi.yml
  - aid: cisco-webex:webex-events-api
    name: Webex Events API
    description: Access events representing activities within a Webex organization such as message posts, file shares, and membership changes. Provides a historical log of activities for compliance and auditing purposes.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/events
    baseURL: https://webexapis.com/v1
    tags:
      - Activity
      - Auditing
      - Compliance
      - Events
      - Monitoring
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/events
      - type: OpenAPI
        url: openapi/cisco-webex-events-openapi.yml
  - aid: cisco-webex:webex-recordings-api
    name: Webex Recordings API
    description: List and manage meeting recordings. Provides access to recording details, download links, and metadata. Includes separate endpoints for admin and compliance officer access with extended filtering capabilities.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/recordings
    baseURL: https://webexapis.com/v1
    tags:
      - Compliance
      - Media
      - Meetings
      - Recordings
      - Storage
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/recordings
      - type: OpenAPI
        url: openapi/cisco-webex-recordings-openapi.yml
  - aid: cisco-webex:webex-call-controls-api
    name: Webex Call Controls API
    description: Control active calls in Webex Calling including dial, answer, hold, transfer, and pickup operations. Supports third-party call control for building custom calling experiences and integrations.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/call-controls
    baseURL: https://webexapis.com/v1
    tags:
      - Call Control
      - Calling
      - Communications
      - Telephony
      - Voice
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/call-controls
      - type: OpenAPI
        url: openapi/cisco-webex-call-controls-openapi.yml
  - aid: cisco-webex:webex-attachment-actions-api
    name: Webex Attachment Actions API
    description: Create and retrieve attachment actions for adaptive card interactions. Used with Buttons and Cards to capture user input from interactive card elements submitted in Webex messaging spaces.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/attachment-actions
    baseURL: https://webexapis.com/v1
    tags:
      - Attachment Actions
      - Buttons
      - Cards
      - Interactive
      - Messaging
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/attachment-actions
      - type: OpenAPI
        url: openapi/cisco-webex-attachment-actions-openapi.yml
  - aid: cisco-webex:webex-organizations-api
    name: Webex Organizations API
    description: Retrieve organization details for Webex administration. Provides access to organization-level information and settings, available only to organization administrators.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/organizations
    baseURL: https://webexapis.com/v1
    tags:
      - Administration
      - Enterprise
      - Management
      - Organizations
      - Settings
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/organizations
      - type: OpenAPI
        url: openapi/cisco-webex-organizations-openapi.yml
  - aid: cisco-webex:webex-licenses-api
    name: Webex Licenses API
    description: Manage and retrieve Webex licenses for an organization. Provides endpoints to list available licenses, view license details, and assign or modify license allocations for users.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/licenses
    baseURL: https://webexapis.com/v1
    tags:
      - Administration
      - Entitlements
      - Licenses
      - Management
      - Provisioning
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/licenses
      - type: OpenAPI
        url: openapi/cisco-webex-licenses-openapi.yml
  - aid: cisco-webex:webex-roles-api
    name: Webex Roles API
    description: Retrieve roles available within a Webex organization. Roles define the level of access and permissions granted to users, such as full administrator or read-only administrator.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/roles
    baseURL: https://webexapis.com/v1
    tags:
      - Access Control
      - Administration
      - Permissions
      - Roles
      - Security
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/roles
      - type: OpenAPI
        url: openapi/cisco-webex-roles-openapi.yml
  - aid: cisco-webex:webex-workspaces-api
    name: Webex Workspaces API
    description: Manage workspaces representing physical locations with Webex devices. Provides endpoints to create, list, update, and delete workspaces and manage their associated device configurations.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/workspaces
    baseURL: https://webexapis.com/v1
    tags:
      - Devices
      - Facilities
      - Locations
      - Management
      - Workspaces
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/workspaces
      - type: OpenAPI
        url: openapi/cisco-webex-workspaces-openapi.yml
  - aid: cisco-webex:webex-admin-audit-events-api
    name: Webex Admin Audit Events API
    description: Access admin audit events for tracking administrative actions performed in Webex Control Hub. Available to full administrators for compliance monitoring and security auditing purposes.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/admin-audit-events
    baseURL: https://webexapis.com/v1
    tags:
      - Administration
      - Audit
      - Compliance
      - Events
      - Security
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/admin-audit-events
      - type: OpenAPI
        url: openapi/cisco-webex-admin-audit-events-openapi.yml
  - aid: cisco-webex:webex-converged-recordings-api
    name: Webex Converged Recordings API
    description: Access converged recording capabilities across Webex Meetings and Webex Calling. Provides unified endpoints for listing, retrieving, and managing recordings from multiple Webex services.
    image: https://www.webex.com/content/dam/wbx/us/images/webex-logo.svg
    humanURL: https://developer.webex.com/docs/api/v1/converged-recordings
    baseURL: https://webexapis.com/v1
    tags:
      - Calling
      - Compliance
      - Media
      - Meetings
      - Recordings
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/api/v1/converged-recordings
      - type: OpenAPI
        url: openapi/cisco-webex-converged-recordings-openapi.yml
common:
  - type: Portal
    url: https://developer.webex.com
  - type: Documentation
    url: https://developer.webex.com/docs/basics
  - type: Getting Started
    url: https://developer.webex.com/docs/getting-started
  - type: Authentication
    url: https://developer.webex.com/docs/getting-started#authentication
  - type: SDKs
    url: https://developer.webex.com/docs/sdks
  - type: Change Log
    url: https://developer.webex.com/docs/api/changelog
  - type: Blog
    url: https://developer.webex.com/blog
  - type: Support
    url: https://developer.webex.com/support
  - type: Status
    url: https://status.webex.com
  - type: Rate Limits
    url: https://developer.webex.com/docs/api-rate-limits
  - type: Community
    url: https://community.cisco.com/t5/webex-developers/bd-p/4416j-disc-dev-webex
  - type: Terms of Service
    url: https://developer.webex.com/terms-of-service
  - type: Privacy Policy
    url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
  - type: GitHub Organization
    url: https://github.com/webex
  - type: Website
    url: https://www.webex.com
  - type: Login
    url: https://developer.webex.com/login
  - type: Sign Up
    url: https://developer.webex.com/signup
  - type: JSON-LD Context
    url: json-ld/cisco-webex-context.jsonld
  - type: JSON Schema
    url: json-schema/
  - type: Spectral
    url: rules/cisco-webex-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cisco-webex-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://developer.webex.com
---

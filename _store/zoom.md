---
aid: zoom
url: https://raw.githubusercontent.com/api-search/videos/main/_apis/zoom/apis.md
name: Zoom
description: Zoom is a communications platform that allows users to connect with video, audio, phone, and chat. The Zoom API provides programmatic access to Zoom's core features including meetings, webinars, recordings, users, and more.
image: https://st1.zoom.us/static/5.16.6-1642/image/new/ZoomLogo.png
tags:
  - Chat
  - Collaboration
  - Communications
  - Meetings
  - Video Conferencing
  - Videos
  - Webinars
created: '2024-04-14'
modified: '2026-05-04'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
position: Consumer
apis:
  - aid: zoom:zoom-chat-api
    name: Zoom Chat API
    description: Developers can use the Zoom Chat API to access chat and chat channel data to build private services or public applications on the Zoom App Marketplace.
    humanURL: https://developers.zoom.us/docs/api/rest/chat-api/
    baseURL: https://api.zoom.us/v2
    tags:
      - Chat
    properties:
      - type: OpenAPI
        url: openapi/zoom-chat--openapi-original.yml
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/chat-api/
  - aid: zoom:zoom-group-api
    name: Zoom Group API
    description: For managing Zoom groups.
    humanURL: https://developers.zoom.us/docs/api/
    baseURL: https://api.zoom.us/v2
    tags:
      - Edit
      - Groups
      - Members
    properties:
      - type: OpenAPI
        url: openapi/zoom-group--openapi-original.yml
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/user/methods/
  - aid: zoom:zoom-device-api
    name: Zoom Device API
    description: You can access information from Zoom with Zoom Phone APIs to build private services or public applications on the Zoom App Marketplace.
    humanURL: https://developers.zoom.us/docs/api/rest/zoom-phone-api/
    baseURL: https://api.zoom.us/v2
    tags:
      - Device
      - H323
    properties:
      - type: OpenAPI
        url: openapi/zoom-device--openapi-original.yml
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/zoom-phone-api/
  - aid: zoom:zoom-instant-message-api
    name: Zoom Instant Message API
    description: Provides the ability to instant message.
    humanURL: https://developers.zoom.us/docs/api/
    baseURL: https://api.zoom.us/v2
    tags:
      - Edit
      - Groups
      - Members
    properties:
      - type: OpenAPI
        url: openapi/zoom-im--openapi-original.yml
      - type: Documentation
        url: https://developers.zoom.us/docs/api/
  - aid: zoom:zoom-account-api
    name: Zoom Account API
    description: The Zoom Account API lets developers access data related to Accounts, Dashboards, Information Barriers, and Roles. Use this API to build private services or public applications on the Zoom App Marketplace. Learn how to get your credentials and create private/public applications in our Authorization Guide.
    humanURL: https://developers.zoom.us/docs/api/rest/account/
    baseURL: https://api.zoom.us/v2
    tags:
      - Accounts
      - Billing
      - Plan
      - Subscribe
    properties:
      - type: OpenAPI
        url: openapi/zoom-account--openapi-original.yml
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/account/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/reference/account/methods/
  - aid: zoom:zoom-recording-api
    name: Zoom Recording API
    description: Manage the recordings made of Zoom calls.
    humanURL: https://developers.zoom.us/docs/video-sdk/web/recording/
    baseURL: https://api.zoom.us/v2
    tags:
      - Mc
      - Recording
    properties:
      - type: OpenAPI
        url: openapi/zoom-recording--openapi-original.yml
      - type: Documentation
        url: https://developers.zoom.us/docs/video-sdk/web/recording/
  - aid: zoom:zoom-meeting-api
    name: Zoom Meeting API
    description: The Zoom Meeting API lets developers access meeting and webinar data from Zoom Meeting. Use this API to build private services or public applications on the Zoom App Marketplace.
    humanURL: https://developers.zoom.us/docs/api/rest/meeting/
    baseURL: https://api.zoom.us/v2
    tags:
      - Live
      - Meetings
      - Register
    properties:
      - type: OpenAPI
        url: openapi/zoom-meeting--openapi-original.yml
      - type: OpenAPI
        url: openapi/zoom-meeting-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/zoom-meeting-webhooks-asyncapi.yml
      - type: JSONSchema
        url: json-schema/zoom-meeting-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-meeting-list-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-meeting-summary-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-meeting-type-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-meeting-create-request-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-meeting-create-response-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-meeting-update-request-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-meeting-details-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-meeting-settings-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-recurrence-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-occurrence-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-registrant-create-request-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-registrant-create-response-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-registrant-list-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-registrant-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-poll-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-poll-question-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-poll-create-request-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-participant-list-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-participant-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-live-stream-update-request-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-past-meeting-details-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-recording-list-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-recording-file-schema.json
      - type: JSONSchema
        url: json-schema/zoom-meeting-error-response-schema.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-meeting-list-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-meeting-summary-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-meeting-type-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-meeting-create-request-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-meeting-create-response-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-meeting-update-request-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-meeting-details-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-meeting-settings-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-recurrence-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-occurrence-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-registrant-create-request-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-registrant-create-response-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-registrant-list-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-registrant-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-poll-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-poll-question-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-poll-create-request-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-participant-list-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-participant-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-live-stream-update-request-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-past-meeting-details-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-recording-list-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-recording-file-structure.json
      - type: JSONStructure
        url: json-structure/zoom-meeting-error-response-structure.json
      - type: Example
        url: examples/zoom-meeting-meeting-list-example.json
      - type: Example
        url: examples/zoom-meeting-meeting-summary-example.json
      - type: Example
        url: examples/zoom-meeting-meeting-type-example.json
      - type: Example
        url: examples/zoom-meeting-meeting-create-request-example.json
      - type: Example
        url: examples/zoom-meeting-meeting-create-response-example.json
      - type: Example
        url: examples/zoom-meeting-meeting-update-request-example.json
      - type: Example
        url: examples/zoom-meeting-meeting-details-example.json
      - type: Example
        url: examples/zoom-meeting-meeting-settings-example.json
      - type: Example
        url: examples/zoom-meeting-recurrence-example.json
      - type: Example
        url: examples/zoom-meeting-occurrence-example.json
      - type: Example
        url: examples/zoom-meeting-registrant-create-request-example.json
      - type: Example
        url: examples/zoom-meeting-registrant-create-response-example.json
      - type: Example
        url: examples/zoom-meeting-registrant-list-example.json
      - type: Example
        url: examples/zoom-meeting-registrant-example.json
      - type: Example
        url: examples/zoom-meeting-poll-example.json
      - type: Example
        url: examples/zoom-meeting-poll-question-example.json
      - type: Example
        url: examples/zoom-meeting-poll-create-request-example.json
      - type: Example
        url: examples/zoom-meeting-participant-list-example.json
      - type: Example
        url: examples/zoom-meeting-participant-example.json
      - type: Example
        url: examples/zoom-meeting-live-stream-update-request-example.json
      - type: Example
        url: examples/zoom-meeting-past-meeting-details-example.json
      - type: Example
        url: examples/zoom-meeting-recording-list-example.json
      - type: Example
        url: examples/zoom-meeting-recording-file-example.json
      - type: Example
        url: examples/zoom-meeting-error-response-example.json
      - type: JSONLD
        url: json-ld/zoom-meeting-context.jsonld
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/meeting/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/
  - aid: zoom:zoom-metrics-api
    name: Zoom Metrics API
    description: Access and manage all of the metrics associate with operating on Zoom.
    humanURL: https://developers.zoom.us/docs/api/
    baseURL: https://api.zoom.us/v2
    tags:
      - Crc
      - Meetingdetail
      - Meetings
      - Metrics
      - Qos
      - Webinardetail
      - Webinars
      - Zoomroomdetail
      - Zoomrooms
    properties:
      - type: OpenAPI
        url: openapi/zoom-metrics--openapi-original.yml
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/
  - aid: zoom:zoom-report-api
    name: Zoom Report API
    description: Access and manage reports associated with using Zoom.
    humanURL: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#tag/Reports
    baseURL: https://api.zoom.us/v2
    tags:
      - Reports
    properties:
      - type: OpenAPI
        url: openapi/zoom-report--openapi-original.yml
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/
  - aid: zoom:zoom-user-api
    name: Zoom User API
    description: The Zoom User API lets developers access data related to Contact Groups, Groups, and Users. Use this API to build private services or public applications on the Zoom App Marketplace. Learn how to get your credentials and create private/public applications in our Authorization Guide.
    humanURL: https://developers.zoom.us/docs/api/rest/user/
    baseURL: https://api.zoom.us/v2
    tags:
      - Activate
      - Assistants
      - Autocreate
      - Checkemail
      - Checkzpk
      - Custcreate
      - Deactivate
      - Getbyemail
      - Pending
      - Permanentdelete
      - Revoketoken
      - Scheduleforhost
      - Sets
      - Ssocreate
      - Updatepassword
      - Users
    properties:
      - type: OpenAPI
        url: openapi/zoom-user--openapi-original.yml
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/user/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/reference/user/methods/
  - aid: zoom:zoom-webinar-api
    name: Zoom Webinar API
    description: Provides the ability to manage details of webinars operated via Zoom.
    humanURL: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#tag/Webinars
    baseURL: https://api.zoom.us/v2
    tags:
      - Approve
      - Attendees
      - Cancel
      - Panelists
      - Polls
      - Questions
      - Register
      - Registrants
      - Registrations
      - Uu
      - Webinar
    properties:
      - type: OpenAPI
        url: openapi/zoom-webinar--openapi-original.yml
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/
  - aid: zoom:zoom-phone-api
    name: Zoom Phone API
    description: The Zoom Phone API allows developers to access Zoom Phone functionality to build private services or public applications on the Zoom App Marketplace, including account management, caller ID management, alert configuration, and integration capabilities.
    humanURL: https://developers.zoom.us/docs/api/phone/
    baseURL: https://api.zoom.us/v2
    tags:
      - Calling
      - Phone
      - Voice
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/phone/methods/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/zoom-phone-api/
  - aid: zoom:zoom-team-chat-api
    name: Zoom Team Chat API
    description: The Zoom Team Chat API enables developers to integrate messaging into applications and automate workflows within Zoom Team Chat, including channel management, member operations, mention groups, and activity tracking.
    humanURL: https://developers.zoom.us/docs/api/team-chat/
    baseURL: https://api.zoom.us/v2
    tags:
      - Channels
      - Chat
      - Collaboration
      - Messaging
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/team-chat/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/reference/chat/methods/
  - aid: zoom:zoom-contact-center-api
    name: Zoom Contact Center API
    description: The Zoom Contact Center API enables developers to programmatically interface with Contact Center features including address book management, agent status tracking, and contact information handling to build integrated customer service solutions.
    humanURL: https://developers.zoom.us/docs/api/contact-center/
    baseURL: https://api.zoom.us/v2
    tags:
      - Agents
      - Contact Center
      - Customer Service
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/contact-center/methods/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/contact-center-api/
  - aid: zoom:zoom-events-api
    name: Zoom Webinars Plus and Events API
    description: The Zoom Webinars Plus and Events API enables developers to create, manage, and customize virtual event experiences including single-session, multi-session conference, or recurring events with attendee management, access control, and communication capabilities.
    humanURL: https://developers.zoom.us/docs/api/events/
    baseURL: https://api.zoom.us/v2
    tags:
      - Conferences
      - Events
      - Registrations
      - Webinars
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/event/methods/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/zoom-events-api/
      - type: GettingStarted
        url: https://developers.zoom.us/docs/events/api-guides/getting-started/
  - aid: zoom:zoom-marketplace-api
    name: Zoom Marketplace API
    description: The Zoom Marketplace API enables developers to access and manage application data within the Zoom ecosystem, including app management, event subscriptions, user notifications, monitoring, and analytics.
    humanURL: https://developers.zoom.us/docs/api/marketplace/
    baseURL: https://api.zoom.us/v2
    tags:
      - Apps
      - Integrations
      - Marketplace
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/marketplace/methods/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/marketplace-api/
  - aid: zoom:zoom-revenue-accelerator-api
    name: Zoom Revenue Accelerator API
    description: The Zoom Revenue Accelerator API enables developers to interface with conversation intelligence features including engagement scores, sentiment analysis, CRM integration, and sales indicators to help sales organizations improve deal outcomes.
    humanURL: https://developers.zoom.us/docs/api/iq/
    baseURL: https://api.zoom.us/v2
    tags:
      - Analytics
      - CRM
      - Revenue
      - Sales
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/iq/methods/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/zoom-iq-api/
  - aid: zoom:zoom-whiteboard-api
    name: Zoom Whiteboard API
    description: The Zoom Whiteboard API empowers interactive collaboration by enabling integration with whiteboard features for brainstorming sessions, interactive training, and educational experiences with remote participants.
    humanURL: https://developers.zoom.us/docs/api/whiteboard/
    baseURL: https://api.zoom.us/v2
    tags:
      - Collaboration
      - Drawing
      - Whiteboard
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/whiteboard/
  - aid: zoom:zoom-rooms-api
    name: Zoom Rooms API
    description: The Zoom Rooms REST API enables developers to manage Zoom Rooms programmatically, including creating new rooms, reading configurations, performing active control operations, managing workspace reservations, and handling visitor management.
    humanURL: https://developers.zoom.us/docs/api/rooms/
    baseURL: https://api.zoom.us/v2
    tags:
      - Conference Rooms
      - Devices
      - Rooms
      - Workspaces
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rooms/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/reference/zoom-rooms/methods/
  - aid: zoom:zoom-clips-api
    name: Zoom Clips API
    description: The Zoom Clips API allows developers to interface with Zoom Clips features programmatically, enabling content creation, management, and distribution of short video recordings for collaboration and documentation workflows.
    humanURL: https://developers.zoom.us/docs/api/clips/
    baseURL: https://api.zoom.us/v2
    tags:
      - Clips
      - Recording
      - Sharing
      - Video
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/clips/
  - aid: zoom:zoom-mail-api
    name: Zoom Mail API
    description: The Zoom Mail API enables developers to programmatically access and manage mailbox data including draft management, label organization, history tracking, and message operations to build private and public offerings on the Zoom App Marketplace.
    humanURL: https://developers.zoom.us/docs/api/mail/
    baseURL: https://api.zoom.us/v2
    tags:
      - Email
      - Mail
      - Messaging
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/mail/
  - aid: zoom:zoom-calendar-api
    name: Zoom Calendar API
    description: The Zoom Calendar API enables developers to manage calendar events, automate scheduling, sync across platforms, and integrate Zoom Calendar with third-party apps for seamless event management.
    humanURL: https://developers.zoom.us/docs/api/calendar/
    baseURL: https://api.zoom.us/v2
    tags:
      - Calendar
      - Events
      - Scheduling
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/calendar/
  - aid: zoom:zoom-scheduler-api
    name: Zoom Scheduler API
    description: The Zoom Scheduler API enables developers to schedule, manage, and retrieve details about meetings, webinars, and other events on the Zoom platform, including availability scheduling, analytics, and routing forms.
    humanURL: https://developers.zoom.us/docs/api/scheduler/
    baseURL: https://api.zoom.us/v2
    tags:
      - Appointments
      - Booking
      - Scheduler
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/zoom-scheduler-api/
  - aid: zoom:zoom-chatbot-api
    name: Zoom Chatbot API
    description: The Zoom Chatbot API enables chatbots to send and receive messages, respond to user inputs, and perform actions within Zoom Team Chat, allowing developers to automate tasks, send notifications, and integrate third-party services.
    humanURL: https://developers.zoom.us/docs/api/chatbot/
    baseURL: https://api.zoom.us/v2
    tags:
      - Automation
      - Bots
      - Chatbot
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/chatbot/methods/
  - aid: zoom:zoom-ai-companion-api
    name: Zoom AI Companion API
    description: The Zoom AI Companion API enables developers to manage user interactions with the AI Companion across various Zoom services, supporting archiving prompts and responses and retrieving conversation archives for compliance and record-keeping purposes.
    humanURL: https://developers.zoom.us/docs/api/ai-companion/
    baseURL: https://api.zoom.us/v2
    tags:
      - AI
      - Artificial Intelligence
      - Companion
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/ai-companion/
  - aid: zoom:zoom-docs-api
    name: Zoom Docs API
    description: The Zoom Docs API enables developers to programmatically manage documents and collaborative files including file operations, collaboration management, file sharing, import/export in multiple formats, and file organization with folder structures.
    humanURL: https://developers.zoom.us/docs/api/zoom-docs/
    baseURL: https://api.zoom.us/v2
    tags:
      - Collaboration
      - Documents
      - Files
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/zoom-docs/
  - aid: zoom:zoom-tasks-api
    name: Zoom Tasks API
    description: The Zoom Tasks API enables developers to manage and automate tasks within the Zoom ecosystem, including creating, viewing, updating, and deleting tasks with support for collaborators, assignees, and comments.
    humanURL: https://developers.zoom.us/docs/api/tasks/
    baseURL: https://api.zoom.us/v2
    tags:
      - Productivity
      - Project Management
      - Tasks
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/tasks/
  - aid: zoom:zoom-crc-api
    name: Zoom CRC API
    description: The Zoom Conference Room Connector API allows developers to programmatically manage Cisco and Polycom conference room devices, including room management, account settings, API connectors, and device control for SIP and H.323 protocols.
    humanURL: https://developers.zoom.us/docs/api/crc/
    baseURL: https://api.zoom.us/v2
    tags:
      - Conference Room Connector
      - Devices
      - H323
      - SIP
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/crc/
  - aid: zoom:zoom-virtual-agent-api
    name: Zoom Virtual Agent API
    description: The Zoom Virtual Agent API enables developers to build AI-powered chatbot solutions for websites, providing immediate customer support, reducing workload on human agents, and accelerating customer support delivery through automation.
    humanURL: https://developers.zoom.us/docs/api/virtual-agent/
    baseURL: https://api.zoom.us/v2
    tags:
      - AI
      - Chatbot
      - Customer Support
      - Virtual Agent
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/virtual-agent/methods/
  - aid: zoom:zoom-number-management-api
    name: Zoom Number Management API
    description: The Zoom Number Management API lets developers manage and provision phone numbers in Zoom Phone, Contact Center, or Meetings accounts programmatically, automating phone number operations at scale including BYOC numbers and SMS campaigns.
    humanURL: https://developers.zoom.us/docs/api/number-management/
    baseURL: https://api.zoom.us/v2
    tags:
      - BYOC
      - Phone Numbers
      - Provisioning
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/number-management/
  - aid: zoom:zoom-quality-management-api
    name: Zoom Quality Management API
    description: The Zoom Quality Management API is designed to help contact centers track and analyze customer interactions, measure agent performance, provide actionable insights, and proactively identify areas for improvement while maintaining organizational compliance.
    humanURL: https://developers.zoom.us/docs/api/quality-management/
    baseURL: https://api.zoom.us/v2
    tags:
      - Analytics
      - Contact Center
      - Evaluation
      - Quality Management
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/quality-management/
  - aid: zoom:zoom-workforce-management-api
    name: Zoom Workforce Management API
    description: The Zoom Workforce Management API enables developers to build applications that manage workforce scheduling and forecasting operations, including demand predictions, agent schedules, historical data import, and adherence reporting.
    humanURL: https://developers.zoom.us/docs/api/workforce-management/
    baseURL: https://api.zoom.us/v2
    tags:
      - Forecasting
      - Scheduling
      - Workforce Management
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/workforce-management/
  - aid: zoom:zoom-commerce-api
    name: Zoom Commerce API
    description: The Zoom Commerce API allows partners to manage subscriptions, enable integrations, and handle business operations including account management, billing operations, and deal registration within the Zoom ecosystem.
    humanURL: https://developers.zoom.us/docs/api/commerce/
    baseURL: https://api.zoom.us/v2
    tags:
      - Billing
      - Commerce
      - Partners
      - Subscriptions
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/commerce/
  - aid: zoom:zoom-healthcare-api
    name: Zoom Healthcare API
    description: The Zoom Healthcare API allows developers to get, list, and update clinical notes programmatically, designed for healthcare professionals using Zoom for telehealth appointments to integrate clinical note management into their workflows and EHR systems.
    humanURL: https://developers.zoom.us/docs/api/healthcare/
    baseURL: https://api.zoom.us/v2
    tags:
      - Clinical Notes
      - Healthcare
      - Telehealth
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/healthcare/
  - aid: zoom:zoom-video-management-api
    name: Zoom Video Management API
    description: The Zoom Video Management API enables developers to manage channels, channel permissions, playlists, and videos for organizing and distributing video content within the Zoom platform.
    humanURL: https://developers.zoom.us/docs/api/video-management/
    baseURL: https://api.zoom.us/v2
    tags:
      - Channels
      - Playlists
      - Video Management
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/video-management/
  - aid: zoom:zoom-auto-dialer-api
    name: Zoom Auto Dialer API
    description: The Zoom Auto Dialer API enables developers to programmatically manage call lists and prospect data for automated outreach campaigns, including call list management, prospect management, call history, and reporting.
    humanURL: https://developers.zoom.us/docs/api/auto-dialer/
    baseURL: https://api.zoom.us/v2
    tags:
      - Auto Dialer
      - Calling
      - Outreach
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/auto-dialer/
  - aid: zoom:zoom-qss-api
    name: Zoom QSS API
    description: The Zoom Quality of Service Subscription API enables developers to receive details about network traffic in near real-time for meetings, webinars, and phone calls, helping proactively identify and troubleshoot network-related issues.
    humanURL: https://developers.zoom.us/docs/api/qss/
    baseURL: https://api.zoom.us/v2
    tags:
      - Monitoring
      - Network
      - Quality of Service
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/qss/
  - aid: zoom:zoom-scim2-api
    name: Zoom SCIM2 API
    description: The Zoom SCIM2 API automates user and group identity provisioning across cloud applications using SSO services and Identity Providers, enabling organizations to synchronize user and group information automatically.
    humanURL: https://developers.zoom.us/docs/api/scim2/
    baseURL: https://api.zoom.us/v2
    tags:
      - Identity
      - Provisioning
      - SCIM
      - SSO
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/zoom-scim-api/
  - aid: zoom:zoom-video-sdk-api
    name: Zoom Video SDK API
    description: The Zoom Video SDK API enables developers to build custom video applications with session management, cloud recording, storage control, event controls, and analytics using Zoom's video platform infrastructure.
    humanURL: https://developers.zoom.us/docs/api/video-sdk/
    baseURL: https://api.zoom.us/v2
    tags:
      - Cloud Recording
      - Sessions
      - Video SDK
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/video-sdk/
      - type: APIReference
        url: https://developers.zoom.us/docs/api/rest/zoom-video-sdk-api/
      - type: SDK
        url: https://developers.zoom.us/docs/video-sdk/
  - aid: zoom:zoom-meeting-sdk
    name: Zoom Meeting SDK
    description: The Zoom Meeting SDK allows developers to embed Zoom meetings and webinars directly into applications with platform support for web, iOS, Android, macOS, Windows, and Linux, offering UI customization options and both client and component view modes.
    humanURL: https://developers.zoom.us/docs/meeting-sdk/
    baseURL: https://api.zoom.us/v2
    tags:
      - Embed
      - Integration
      - Meeting SDK
      - Web
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/meeting-sdk/
      - type: SDK
        url: https://developers.zoom.us/docs/meeting-sdk/web/
  - aid: zoom:zoom-cobrowse-sdk-api
    name: Zoom Cobrowse SDK API
    description: The Zoom Cobrowse SDK API enables real-time collaborative browsing with annotation tools, data masking, and secure screen sharing, allowing users to share their web browsing experience with an organization without compromising privacy and security.
    humanURL: https://developers.zoom.us/docs/api/cobrowse-sdk/
    baseURL: https://api.zoom.us/v2
    tags:
      - Cobrowse
      - Customer Support
      - Screen Sharing
    properties:
      - type: Documentation
        url: https://developers.zoom.us/docs/api/cobrowse-sdk/
common:
  - type: GettingStarted
    url: https://developers.zoom.us/docs/api/rest/getting-started/
  - type: Authentication
    url: https://developers.zoom.us/docs/api/rest/authentication/
  - type: RateLimits
    url: https://developers.zoom.us/docs/api/rest/rate-limits/
  - type: ChangeLog
    url: https://developers.zoom.us/docs/api/rest/changelog/
  - type: SDK
    url: https://developers.zoom.us/docs/api/rest/sdks/
  - type: Support
    url: https://devsupport.zoom.us/hc/en-us
  - type: StatusPage
    url: https://status.zoom.us/
  - type: TermsOfService
    url: https://explore.zoom.us/en/terms/
  - type: PrivacyPolicy
    url: https://explore.zoom.us/en/privacy/
  - type: Portal
    url: https://developers.zoom.us/
  - type: Documentation
    url: https://developers.zoom.us/docs/
  - type: Blog
    url: https://developers.zoom.us/blog/
  - type: Marketplace
    url: https://marketplace.zoom.us/
  - type: SignUp
    url: https://developers.zoom.us/docs/build/account/
  - type: Errors
    url: https://developers.zoom.us/docs/api/errors/
  - type: GitHubRepository
    url: https://github.com/zoom/api
  - type: JSONLD
    url: json-ld/zoom-context.jsonld
  - type: SpectralRules
    url: rules/zoom-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/meeting-management.yaml
  - type: Features
    data:
      - Basic free with 40-min meeting cap, 100 participants
      - Pro at $13.33/user/mo with 30-hr meetings, 5 GB cloud recording
      - Business at $18.33/user/mo with 300 participants, SSO, managed domains
      - Enterprise at $19.99/user/mo with unlimited cloud, 1,000 participants
      - Zoom Phone, Webinars, Events as add-ons
      - REST API tiered by Light/Medium/Heavy categories
      - 30/60/80 req/sec by category; 100K req/day per app
      - OAuth 2.0 (account-level and user-level)
      - Server-to-Server OAuth for backend apps
      - Webhooks via Marketplace Apps
      - Meeting SDK (Web/iOS/Android/Windows/macOS)
      - Video SDK for custom video apps
      - Chat API for team messaging
      - Phone API for cloud PBX
      - AI Companion for meeting summaries (Pro+)
      - Marketplace for distributable apps
    sources:
      - https://zoom.us/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Remote Work
        description: Enable distributed teams to collaborate effectively with video meetings, chat, and shared workspaces.
      - name: Telehealth
        description: Provide HIPAA-compliant virtual healthcare appointments with clinical note integration.
      - name: Virtual Events
        description: Host conferences, webinars, and large-scale events with registration and attendee engagement tools.
      - name: Education
        description: Deliver online classes and training sessions with breakout rooms, polling, and whiteboard collaboration.
      - name: Customer Support
        description: Build omnichannel contact centers with AI-powered virtual agents and quality management.
      - name: Sales Enablement
        description: Accelerate revenue with conversation intelligence, engagement scoring, and CRM integration.
  - type: Integrations
    data:
      - name: Salesforce
        description: Sync meeting data, recordings, and conversation intelligence with Salesforce CRM.
      - name: Microsoft 365
        description: Integrate Zoom with Outlook calendar, Teams, and OneDrive for seamless scheduling.
      - name: Google Workspace
        description: Connect with Google Calendar, Gmail, and Google Drive for unified collaboration.
      - name: Slack
        description: Start Zoom meetings directly from Slack channels and receive meeting notifications.
      - name: HubSpot
        description: Automatically log meeting activities and conversation insights in HubSpot CRM.
      - name: Zapier
        description: Automate workflows between Zoom and 5,000+ apps with no-code integrations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

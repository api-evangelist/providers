---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 206
  human_in_the_loop: 2
  name: Zoom Agentic Access
  operation_count: 217
  slug: zoom-agentic-access
  summary_line: 217 operations · 206 acting · 2 human-in-the-loop
api_count: 12
apis:
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Zoom Meeting API lets developers access meeting and webinar data from Zoom Meeting. Use this API to build private services or public applications on the Zoom App Marketplace.
  name: Zoom Meeting API
  slug: zoom-meeting-api
- description: The Zoom Phone API allows developers to access Zoom Phone functionality to build private services or public applications on the Zoom App Marketplace, including account management, caller ID management
  name: Zoom Phone API
  slug: zoom-phone-api
- description: The Zoom Team Chat API enables developers to integrate messaging into applications and automate workflows within Zoom Team Chat, including channel management, member operations, mention groups, and ac
  name: Zoom Team Chat API
  slug: zoom-team-chat-api
- description: 'The Zoom Contact Center API enables developers to programmatically interface with Contact Center features including address book management, agent status tracking, and contact information handling to '
  name: Zoom Contact Center API
  slug: zoom-contact-center-api
- description: The Zoom Webinars Plus and Events API enables developers to create, manage, and customize virtual event experiences including single-session, multi-session conference, or recurring events with attende
  name: Zoom Webinars Plus and Events API
  slug: zoom-events-api
- description: The Zoom Marketplace API enables developers to access and manage application data within the Zoom ecosystem, including app management, event subscriptions, user notifications, monitoring, and analytic
  name: Zoom Marketplace API
  slug: zoom-marketplace-api
- description: 'The Zoom Revenue Accelerator API enables developers to interface with conversation intelligence features including engagement scores, sentiment analysis, CRM integration, and sales indicators to help '
  name: Zoom Revenue Accelerator API
  slug: zoom-revenue-accelerator-api
- description: The Zoom Whiteboard API empowers interactive collaboration by enabling integration with whiteboard features for brainstorming sessions, interactive training, and educational experiences with remote pa
  name: Zoom Whiteboard API
  slug: zoom-whiteboard-api
- description: The Zoom Rooms REST API enables developers to manage Zoom Rooms programmatically, including creating new rooms, reading configurations, performing active control operations, managing workspace reserva
  name: Zoom Rooms API
  slug: zoom-rooms-api
- description: The Zoom Clips API allows developers to interface with Zoom Clips features programmatically, enabling content creation, management, and distribution of short video recordings for collaboration and doc
  name: Zoom Clips API
  slug: zoom-clips-api
- description: The Zoom Mail API enables developers to programmatically access and manage mailbox data including draft management, label organization, history tracking, and message operations to build private and pu
  name: Zoom Mail API
  slug: zoom-mail-api
- description: The Zoom Calendar API enables developers to manage calendar events, automate scheduling, sync across platforms, and integrate Zoom Calendar with third-party apps for seamless event management.
  name: Zoom Calendar API
  slug: zoom-calendar-api
- description: The Zoom Scheduler API enables developers to schedule, manage, and retrieve details about meetings, webinars, and other events on the Zoom platform, including availability scheduling, analytics, and r
  name: Zoom Scheduler API
  slug: zoom-scheduler-api
- description: The Zoom Chatbot API enables chatbots to send and receive messages, respond to user inputs, and perform actions within Zoom Team Chat, allowing developers to automate tasks, send notifications, and in
  name: Zoom Chatbot API
  slug: zoom-chatbot-api
- description: The Zoom AI Companion API enables developers to manage user interactions with the AI Companion across various Zoom services, supporting archiving prompts and responses and retrieving conversation arch
  name: Zoom AI Companion API
  slug: zoom-ai-companion-api
- description: 'The Zoom Docs API enables developers to programmatically manage documents and collaborative files including file operations, collaboration management, file sharing, import/export in multiple formats, '
  name: Zoom Docs API
  slug: zoom-docs-api
- description: The Zoom Tasks API enables developers to manage and automate tasks within the Zoom ecosystem, including creating, viewing, updating, and deleting tasks with support for collaborators, assignees, and c
  name: Zoom Tasks API
  slug: zoom-tasks-api
- description: The Zoom Conference Room Connector API allows developers to programmatically manage Cisco and Polycom conference room devices, including room management, account settings, API connectors, and device c
  name: Zoom CRC API
  slug: zoom-crc-api
- description: The Zoom Virtual Agent API enables developers to build AI-powered chatbot solutions for websites, providing immediate customer support, reducing workload on human agents, and accelerating customer sup
  name: Zoom Virtual Agent API
  slug: zoom-virtual-agent-api
- description: The Zoom Number Management API lets developers manage and provision phone numbers in Zoom Phone, Contact Center, or Meetings accounts programmatically, automating phone number operations at scale incl
  name: Zoom Number Management API
  slug: zoom-number-management-api
- description: 'The Zoom Quality Management API is designed to help contact centers track and analyze customer interactions, measure agent performance, provide actionable insights, and proactively identify areas for '
  name: Zoom Quality Management API
  slug: zoom-quality-management-api
- description: The Zoom Workforce Management API enables developers to build applications that manage workforce scheduling and forecasting operations, including demand predictions, agent schedules, historical data i
  name: Zoom Workforce Management API
  slug: zoom-workforce-management-api
- description: The Zoom Commerce API allows partners to manage subscriptions, enable integrations, and handle business operations including account management, billing operations, and deal registration within the Zo
  name: Zoom Commerce API
  slug: zoom-commerce-api
- description: The Zoom Healthcare API allows developers to get, list, and update clinical notes programmatically, designed for healthcare professionals using Zoom for telehealth appointments to integrate clinical n
  name: Zoom Healthcare API
  slug: zoom-healthcare-api
- description: The Zoom Video Management API enables developers to manage channels, channel permissions, playlists, and videos for organizing and distributing video content within the Zoom platform.
  name: Zoom Video Management API
  slug: zoom-video-management-api
- description: The Zoom Auto Dialer API enables developers to programmatically manage call lists and prospect data for automated outreach campaigns, including call list management, prospect management, call history,
  name: Zoom Auto Dialer API
  slug: zoom-auto-dialer-api
- description: The Zoom Quality of Service Subscription API enables developers to receive details about network traffic in near real-time for meetings, webinars, and phone calls, helping proactively identify and tro
  name: Zoom QSS API
  slug: zoom-qss-api
- description: 'The Zoom SCIM2 API automates user and group identity provisioning across cloud applications using SSO services and Identity Providers, enabling organizations to synchronize user and group information '
  name: Zoom SCIM2 API
  slug: zoom-scim2-api
- description: The Zoom Video SDK API enables developers to build custom video applications with session management, cloud recording, storage control, event controls, and analytics using Zoom's video platform infras
  name: Zoom Video SDK API
  slug: zoom-video-sdk-api
- description: 'The Zoom Meeting SDK allows developers to embed Zoom meetings and webinars directly into applications with platform support for web, iOS, Android, macOS, Windows, and Linux, offering UI customization '
  name: Zoom Meeting SDK
  slug: zoom-meeting-sdk
- description: The Zoom Cobrowse SDK API enables real-time collaborative browsing with annotation tools, data masking, and secure screen sharing, allowing users to share their web browsing experience with an organiz
  name: Zoom Cobrowse SDK API
  slug: zoom-cobrowse-sdk-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Account API from Zoom — 10 operation(s) for account.
  name: Zoom Account API
  slug: zoom-account-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Chat API from Zoom — 2 operation(s) for chat.
  name: Zoom Chat API
  slug: zoom-chat-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Cloud Recording operations
  name: Zoom Cloud Recording API
  slug: zoom-cloud-recording-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Dashboard API from Zoom — 9 operation(s) for dashboard.
  name: Zoom Dashboard API
  slug: zoom-dashboard-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Device API from Zoom — 4 operation(s) for device.
  name: Zoom Device API
  slug: zoom-device-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Group API from Zoom — 8 operation(s) for group.
  name: Zoom Group API
  slug: zoom-group-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The IM Group API from Zoom — 7 operation(s) for im group.
  name: Zoom IM Group API
  slug: zoom-im-group-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Manage live streaming for Zoom meetings.
  name: Zoom Meeting Live Stream API
  slug: zoom-meeting-live-stream-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Manage participants in Zoom meetings.
  name: Zoom Meeting Participants API
  slug: zoom-meeting-participants-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Create and manage polls for Zoom meetings.
  name: Zoom Meeting Polls API
  slug: zoom-meeting-polls-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Access and manage meeting recordings.
  name: Zoom Meeting Recordings API
  slug: zoom-meeting-recordings-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Manage meeting registration and registrants.
  name: Zoom Meeting Registrants API
  slug: zoom-meeting-registrants-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Create and manage Zoom meetings.
  name: Zoom Meetings API
  slug: zoom-meetings-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Report operations
  name: Zoom Report API
  slug: zoom-report-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: User operations
  name: Zoom User API
  slug: zoom-user-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Webinar operations
  name: Zoom Webinar API
  slug: zoom-webinar-api
arazzos:
- description: Pull an account usage report, then drill into the first user's meeting report.
  name: Zoom Account Report Then User Drill-Down
  slug: zoom-account-then-user-report-workflow
- description: Find pending meeting registrants and approve them, branching when none are pending.
  name: Zoom Approve Pending Meeting Registrants
  slug: zoom-approve-meeting-registrants-workflow
- description: List pending webinar registrants and approve them, branching when none are pending.
  name: Zoom Approve Pending Webinar Registrants
  slug: zoom-approve-webinar-registrants-workflow
- description: Add a batch of registrants to a meeting and confirm the roster.
  name: Zoom Batch Register Meeting Attendees
  slug: zoom-batch-register-attendees-workflow
- description: List archived chat sessions, then read the messages of the first session, branching when none exist.
  name: Zoom Archived Chat History Drill-Down
  slug: zoom-chat-history-workflow
- description: Schedule a meeting for a user and read it back to confirm the saved details.
  name: Zoom Create and Confirm a Meeting
  slug: zoom-create-and-confirm-meeting-workflow
- description: Schedule a webinar, read it back, and list its panelists.
  name: Zoom Create and Confirm a Webinar
  slug: zoom-create-and-confirm-webinar-workflow
- description: Create a Zoom user and read the new user back to confirm provisioning.
  name: Zoom Provision and Confirm a User
  slug: zoom-create-and-get-user-workflow
- description: Schedule a meeting, attach a poll to it, and read the poll back.
  name: Zoom Create and Confirm a Meeting Poll
  slug: zoom-create-meeting-poll-workflow
- description: Fetch a meeting's recording, confirm its files, then delete it.
  name: Zoom Inspect and Delete a Recording
  slug: zoom-delete-recording-workflow
- description: End an in-progress meeting and confirm its status changed.
  name: Zoom End a Live Meeting
  slug: zoom-end-meeting-workflow
- description: List a host's cloud recordings and fetch the first one's files, branching when none exist.
  name: Zoom List and Retrieve a Cloud Recording
  slug: zoom-list-and-get-recording-workflow
- description: List a user's meetings and fetch the first meeting's details, branching when none exist.
  name: Zoom List Meetings and Inspect the First
  slug: zoom-list-meetings-detail-workflow
- description: Set a meeting's live stream destination and then start streaming.
  name: Zoom Configure and Start a Meeting Live Stream
  slug: zoom-meeting-live-stream-workflow
- description: Fetch a meeting's cloud recordings and branch when no recordings exist.
  name: Zoom Retrieve Meeting Recordings
  slug: zoom-meeting-recordings-workflow
- description: Create a registration-required meeting, register an attendee, and list registrants.
  name: Zoom Meeting Registration
  slug: zoom-meeting-registration-workflow
- description: Provision a new user and schedule their first meeting in one flow.
  name: Zoom Onboard a User With a First Meeting
  slug: zoom-onboard-user-with-meeting-workflow
- description: Read a past meeting's summary and then list everyone who attended.
  name: Zoom Past Meeting Attendance Report
  slug: zoom-past-meeting-report-workflow
- description: Look up a user by email address and fetch their full profile by id.
  name: Zoom Resolve a User by Email
  slug: zoom-resolve-user-by-email-workflow
- description: Patch a meeting's topic and schedule, then read it back to confirm.
  name: Zoom Update a Meeting
  slug: zoom-update-meeting-workflow
- description: Pull a user's meeting report and list that same user's cloud recordings.
  name: Zoom User Report With Recordings
  slug: zoom-user-report-recordings-workflow
- description: Create a webinar, register an attendee, and list the registrants.
  name: Zoom Webinar Registration
  slug: zoom-webinar-registration-workflow
artifact_total: 215
asyncapis:
- description: Zoom delivers webhook event notifications to your application when meeting-related events occur on the Zoom platform. These webhooks enable real-time integration with meeting lifecycle events includin
  name: Zoom Meeting Webhooks
  slug: zoom-meeting-webhooks-asyncapi
collections:
- collection_type: postman
  name: Zoom account/
  slug: postman-zoom-account--openapi-original
- collection_type: postman
  name: Zoom chat/
  slug: postman-zoom-chat--openapi-original
- collection_type: postman
  name: Zoom device/
  slug: postman-zoom-device--openapi-original
- collection_type: postman
  name: Zoom group/
  slug: postman-zoom-group--openapi-original
- collection_type: postman
  name: Zoom im/
  slug: postman-zoom-im--openapi-original
- collection_type: postman
  name: Zoom meeting/
  slug: postman-zoom-meeting--openapi-original
- collection_type: postman
  name: Zoom Meeting API
  slug: postman-zoom-meeting-api
- collection_type: postman
  name: Zoom metrics/
  slug: postman-zoom-metrics--openapi-original
- collection_type: postman
  name: Zoom recording/
  slug: postman-zoom-recording--openapi-original
- collection_type: postman
  name: Zoom report/
  slug: postman-zoom-report--openapi-original
- collection_type: postman
  name: Zoom user/
  slug: postman-zoom-user--openapi-original
- collection_type: postman
  name: Zoom webinar/
  slug: postman-zoom-webinar--openapi-original
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zoom / Account API
  slug: open-zoom-account-api
- collection_type: open
  name: Zoom / Account Chat API
  slug: open-zoom-chat-api
- collection_type: open
  name: Zoom / Account Cloud Recording API
  slug: open-zoom-cloud-recording-api
- collection_type: open
  name: Zoom / Account Dashboard API
  slug: open-zoom-dashboard-api
- collection_type: open
  name: Zoom / Account Device API
  slug: open-zoom-device-api
- collection_type: open
  name: Zoom / Account Group API
  slug: open-zoom-group-api
- collection_type: open
  name: Zoom / Account IM Group API
  slug: open-zoom-im-group-api
- collection_type: open
  name: Zoom / Account Meeting API
  slug: open-zoom-meeting-api
- collection_type: open
  name: Zoom / Account Meeting Live Stream API
  slug: open-zoom-meeting-live-stream-api
- collection_type: open
  name: Zoom / Account Meeting Participants API
  slug: open-zoom-meeting-participants-api
- collection_type: open
  name: Zoom / Account Meeting Polls API
  slug: open-zoom-meeting-polls-api
- collection_type: open
  name: Zoom / Account Meeting Recordings API
  slug: open-zoom-meeting-recordings-api
- collection_type: open
  name: Zoom / Account Meeting Registrants API
  slug: open-zoom-meeting-registrants-api
- collection_type: open
  name: Zoom / Account Meetings API
  slug: open-zoom-meetings-api
- collection_type: open
  name: Zoom / Account Report API
  slug: open-zoom-report-api
- collection_type: open
  name: Zoom / Account User API
  slug: open-zoom-user-api
- collection_type: open
  name: Zoom / Account Webinar API
  slug: open-zoom-webinar-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/zoom-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/zoom/api/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoom-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoom-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoom-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zoom/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-account-then-user-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-approve-meeting-registrants-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-approve-webinar-registrants-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-batch-register-attendees-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-chat-history-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-create-and-confirm-meeting-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-create-and-confirm-webinar-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-create-and-get-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-create-meeting-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-delete-recording-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-end-meeting-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-list-and-get-recording-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-list-meetings-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-meeting-live-stream-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-meeting-recordings-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-meeting-registration-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-onboard-user-with-meeting-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-past-meeting-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-resolve-user-by-email-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-update-meeting-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-user-report-recordings-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zoom-webinar-registration-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zoom-video-communications
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.zoom.us/docs/api/rest/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.zoom.us/docs/api/rest/authentication/
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.zoom.us/docs/api/rest/rate-limits/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.zoom.us/docs/api/rest/changelog/
- group: build
  title: ''
  type: SDKs
  url: https://developers.zoom.us/docs/api/rest/sdks/
- group: operate
  title: ''
  type: Support
  url: https://devsupport.zoom.us/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoom.us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://explore.zoom.us/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://explore.zoom.us/en/privacy/
- group: start
  title: ''
  type: Portal
  url: https://developers.zoom.us/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zoom.us/docs/
- group: company
  title: ''
  type: Blog
  url: https://developers.zoom.us/blog/
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.zoom.us/
- group: start
  title: ''
  type: Signup
  url: https://developers.zoom.us/docs/build/account/
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.zoom.us/docs/api/errors/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/zoom/api
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zoom-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/zoom-spectral-rules.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://developers.zoom.us/blog/announcing-agent-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.zoom.us/llms.txt
created: '2024-04-14'
description: Zoom is a communications platform that allows users to connect with video, audio, phone, and chat. The Zoom API provides programmatic access to Zoom's core features including meetings, webinars, recordings, users, and more.
examples:
- key_count: 3
  name: Zoom Meeting Error Response Example
  slug: zoom-meeting-error-response-example
- key_count: 4
  name: Zoom Meeting Live Stream Update Request Example
  slug: zoom-meeting-live-stream-update-request-example
- key_count: 11
  name: Zoom Meeting Meeting Create Request Example
  slug: zoom-meeting-meeting-create-request-example
- key_count: 18
  name: Zoom Meeting Meeting Create Response Example
  slug: zoom-meeting-meeting-create-response-example
- key_count: 0
  name: Zoom Meeting Meeting Details Example
  slug: zoom-meeting-meeting-details-example
- key_count: 6
  name: Zoom Meeting Meeting List Example
  slug: zoom-meeting-meeting-list-example
- key_count: 40
  name: Zoom Meeting Meeting Settings Example
  slug: zoom-meeting-meeting-settings-example
- key_count: 10
  name: Zoom Meeting Meeting Summary Example
  slug: zoom-meeting-meeting-summary-example
- key_count: 0
  name: Zoom Meeting Meeting Type Example
  slug: zoom-meeting-meeting-type-example
- key_count: 8
  name: Zoom Meeting Meeting Update Request Example
  slug: zoom-meeting-meeting-update-request-example
- key_count: 4
  name: Zoom Meeting Occurrence Example
  slug: zoom-meeting-occurrence-example
- key_count: 10
  name: Zoom Meeting Participant Example
  slug: zoom-meeting-participant-example
- key_count: 5
  name: Zoom Meeting Participant List Example
  slug: zoom-meeting-participant-list-example
- key_count: 11
  name: Zoom Meeting Past Meeting Details Example
  slug: zoom-meeting-past-meeting-details-example
- key_count: 4
  name: Zoom Meeting Poll Create Request Example
  slug: zoom-meeting-poll-create-request-example
- key_count: 6
  name: Zoom Meeting Poll Example
  slug: zoom-meeting-poll-example
- key_count: 12
  name: Zoom Meeting Poll Question Example
  slug: zoom-meeting-poll-question-example
- key_count: 11
  name: Zoom Meeting Recording File Example
  slug: zoom-meeting-recording-file-example
- key_count: 12
  name: Zoom Meeting Recording List Example
  slug: zoom-meeting-recording-list-example
- key_count: 8
  name: Zoom Meeting Recurrence Example
  slug: zoom-meeting-recurrence-example
- key_count: 19
  name: Zoom Meeting Registrant Create Request Example
  slug: zoom-meeting-registrant-create-request-example
- key_count: 6
  name: Zoom Meeting Registrant Create Response Example
  slug: zoom-meeting-registrant-create-response-example
- key_count: 20
  name: Zoom Meeting Registrant Example
  slug: zoom-meeting-registrant-example
- key_count: 6
  name: Zoom Meeting Registrant List Example
  slug: zoom-meeting-registrant-list-example
features:
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
finops:
- name: Zoom Finops
  service_category: Video Conferencing
  slug: zoom-finops
graphqls:
- description: 'Zoom does not currently offer a native public GraphQL API. All programmatic access to Zoom''s platform is provided through its REST APIs available at `https://api.zoom.us/v2`. This GraphQL schema is a '
  name: Zoom GraphQL Schema
  slug: zoom-graphql
image: https://st1.zoom.us/static/5.16.6-1642/image/new/ZoomLogo.png
integrations:
- description: Sync meeting data, recordings, and conversation intelligence with Salesforce CRM.
  name: Salesforce
- description: Integrate Zoom with Outlook calendar, Teams, and OneDrive for seamless scheduling.
  name: Microsoft 365
- description: Connect with Google Calendar, Gmail, and Google Drive for unified collaboration.
  name: Google Workspace
- description: Start Zoom meetings directly from Slack channels and receive meeting notifications.
  name: Slack
- description: Automatically log meeting activities and conversation insights in HubSpot CRM.
  name: HubSpot
- description: Automate workflows between Zoom and 5,000+ apps with no-code integrations.
  name: Zapier
json_schemas:
- name: ErrorResponse
  property_count: 3
  slug: zoom-meeting-error-response
- name: LiveStreamUpdateRequest
  property_count: 4
  slug: zoom-meeting-live-stream-update-request
- name: MeetingCreateRequest
  property_count: 11
  slug: zoom-meeting-meeting-create-request
- name: MeetingCreateResponse
  property_count: 18
  slug: zoom-meeting-meeting-create-response
- name: MeetingDetails
  property_count: 0
  slug: zoom-meeting-meeting-details
- name: MeetingList
  property_count: 6
  slug: zoom-meeting-meeting-list
- name: MeetingSettings
  property_count: 40
  slug: zoom-meeting-meeting-settings
- name: MeetingSummary
  property_count: 10
  slug: zoom-meeting-meeting-summary
- name: MeetingType
  property_count: 0
  slug: zoom-meeting-meeting-type
- name: MeetingUpdateRequest
  property_count: 8
  slug: zoom-meeting-meeting-update-request
- name: Occurrence
  property_count: 4
  slug: zoom-meeting-occurrence
- name: ParticipantList
  property_count: 5
  slug: zoom-meeting-participant-list
- name: Participant
  property_count: 10
  slug: zoom-meeting-participant
- name: PastMeetingDetails
  property_count: 11
  slug: zoom-meeting-past-meeting-details
- name: PollCreateRequest
  property_count: 4
  slug: zoom-meeting-poll-create-request
- name: PollQuestion
  property_count: 12
  slug: zoom-meeting-poll-question
- name: Poll
  property_count: 6
  slug: zoom-meeting-poll
- name: RecordingFile
  property_count: 11
  slug: zoom-meeting-recording-file
- name: RecordingList
  property_count: 12
  slug: zoom-meeting-recording-list
- name: Recurrence
  property_count: 8
  slug: zoom-meeting-recurrence
- name: RegistrantCreateRequest
  property_count: 19
  slug: zoom-meeting-registrant-create-request
- name: RegistrantCreateResponse
  property_count: 6
  slug: zoom-meeting-registrant-create-response
- name: RegistrantList
  property_count: 6
  slug: zoom-meeting-registrant-list
- name: Registrant
  property_count: 20
  slug: zoom-meeting-registrant
- name: Zoom Meeting API Core Models
  property_count: 0
  slug: zoom-meeting
json_structures:
- name: Zoom Meeting Error Response Structure
  property_count: 3
  slug: zoom-meeting-error-response-structure
- name: Zoom Meeting Live Stream Update Request Structure
  property_count: 4
  slug: zoom-meeting-live-stream-update-request-structure
- name: Zoom Meeting Meeting Create Request Structure
  property_count: 11
  slug: zoom-meeting-meeting-create-request-structure
- name: Zoom Meeting Meeting Create Response Structure
  property_count: 18
  slug: zoom-meeting-meeting-create-response-structure
- name: Zoom Meeting Meeting Details Structure
  property_count: 0
  slug: zoom-meeting-meeting-details-structure
- name: Zoom Meeting Meeting List Structure
  property_count: 6
  slug: zoom-meeting-meeting-list-structure
- name: Zoom Meeting Meeting Settings Structure
  property_count: 40
  slug: zoom-meeting-meeting-settings-structure
- name: Zoom Meeting Meeting Summary Structure
  property_count: 10
  slug: zoom-meeting-meeting-summary-structure
- name: Zoom Meeting Meeting Type Structure
  property_count: 0
  slug: zoom-meeting-meeting-type-structure
- name: Zoom Meeting Meeting Update Request Structure
  property_count: 8
  slug: zoom-meeting-meeting-update-request-structure
- name: Zoom Meeting Occurrence Structure
  property_count: 4
  slug: zoom-meeting-occurrence-structure
- name: Zoom Meeting Participant List Structure
  property_count: 5
  slug: zoom-meeting-participant-list-structure
- name: Zoom Meeting Participant Structure
  property_count: 10
  slug: zoom-meeting-participant-structure
- name: Zoom Meeting Past Meeting Details Structure
  property_count: 11
  slug: zoom-meeting-past-meeting-details-structure
- name: Zoom Meeting Poll Create Request Structure
  property_count: 4
  slug: zoom-meeting-poll-create-request-structure
- name: Zoom Meeting Poll Question Structure
  property_count: 12
  slug: zoom-meeting-poll-question-structure
- name: Zoom Meeting Poll Structure
  property_count: 6
  slug: zoom-meeting-poll-structure
- name: Zoom Meeting Recording File Structure
  property_count: 11
  slug: zoom-meeting-recording-file-structure
- name: Zoom Meeting Recording List Structure
  property_count: 12
  slug: zoom-meeting-recording-list-structure
- name: Zoom Meeting Recurrence Structure
  property_count: 8
  slug: zoom-meeting-recurrence-structure
- name: Zoom Meeting Registrant Create Request Structure
  property_count: 19
  slug: zoom-meeting-registrant-create-request-structure
- name: Zoom Meeting Registrant Create Response Structure
  property_count: 6
  slug: zoom-meeting-registrant-create-response-structure
- name: Zoom Meeting Registrant List Structure
  property_count: 6
  slug: zoom-meeting-registrant-list-structure
- name: Zoom Meeting Registrant Structure
  property_count: 20
  slug: zoom-meeting-registrant-structure
jsonld:
- class_count: 0
  name: Zoom Context
  property_count: 11
  slug: zoom-context
- class_count: 0
  name: Zoom Meeting Context
  property_count: 0
  slug: zoom-meeting-context
layout: provider
modified: '2026-05-19'
name: Zoom
nav: Providers
network: true
overview: 'Zoom publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Meeting API, Account API, Chat API, and 14 more. Tagged areas include Chat, Collaboration, Communications, Meetings, and Video Conferencing.


  The Zoom catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Zoom''s developer surface includes authentication, getting-started guide, changelog, support, developer portal, documentation, engineering blog, and 44 more developer resources.'
plans:
- name: Zoom Plans Pricing
  plan_count: 4
  slug: zoom-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Zoom Rate Limits
  slug: zoom-rate-limits
rules:
- effective_rule_count: 37
  extends:
  - spectral:asyncapi
  name: Zoom API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 9
  slug: zoom-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Zoom API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: zoom-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Zoom API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: zoom-spectral-rules
scopes:
- name: Zoom Scopes
  scope_count: 19
  slug: zoom-scopes
  summary_line: 19 scopes · authorizationCode
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 25
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 71.9
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 0.0
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoom/refs/heads/main/screenshots/zoom-2026-06-20T165938.png
security:
- kind: authentication
  name: Zoom Authentication
  slug: zoom-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Zoom Domain Security
  slug: zoom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoom Vulnerability Disclosure
  slug: zoom-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoom
tags:
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
- Videos
- Webinars
use_cases:
- description: Enable distributed teams to collaborate effectively with video meetings, chat, and shared workspaces.
  name: Remote Work
- description: Provide HIPAA-compliant virtual healthcare appointments with clinical note integration.
  name: Telehealth
- description: Host conferences, webinars, and large-scale events with registration and attendee engagement tools.
  name: Virtual Events
- description: Deliver online classes and training sessions with breakout rooms, polling, and whiteboard collaboration.
  name: Education
- description: Build omnichannel contact centers with AI-powered virtual agents and quality management.
  name: Customer Support
- description: Accelerate revenue with conversation intelligence, engagement scoring, and CRM integration.
  name: Sales Enablement
website: https://developers.zoom.us/
---

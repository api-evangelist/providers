---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.2
  scored_at: '2026-11-06'
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
  phrasing_intents:
  - id: meetingCreate
    intent: Schedule a meeting for a host
    question: How do I create a meeting and get back its join URL?
  - id: meetingDelete
    intent: Delete a meeting
    question: Can I delete a single occurrence of a recurring meeting?
  - id: meetingEnd
    intent: End a meeting in progress
    question: Is there a way to force a running meeting to end for everyone?
  - id: meetingGet
    intent: Get a meeting's info
    question: What are the settings and schedule of a particular meeting?
  - id: meetingList
    intent: List a host's scheduled meetings
    question: What meetings does a host have scheduled?
  - id: meetingLive
    intent: List meetings that are live now
    question: Which meetings are happening on the account right now?
  - id: meetingRegister
    intent: Register someone for a meeting
    question: How can I sign a person up for a meeting that needs registration?
  - id: meetingUpdate
    intent: Update an existing meeting
    question: Can I reschedule a meeting that's already on the calendar?
  phrasing_ops: 8
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
  phrasing_intents:
  - id: accountBillingUpdate
    intent: Update a sub account's billing information
    question: Can a master account change the billing address on one of its sub accounts?
  - id: accountCreate
    intent: Create a sub account under the master account
    question: How do I create a new sub account under my master account?
  - id: accountDelete
    intent: Delete a sub account
    question: Can I remove a sub account from under my master account?
  - id: accountGet
    intent: Get a sub account's details
    question: Who owns a particular sub account under my master account?
  - id: accountList
    intent: List all sub accounts
    question: Which sub accounts sit under my master account?
  - id: accountPlanAdd
    intent: Add an additional plan to a sub account
    question: Can I add an extra plan to a sub account that the master account pays for?
  - id: accountPlanGet
    intent: Get a sub account's plans
    question: What plans is a sub account currently on?
  - id: accountPlanSubscribe
    intent: Subscribe a sub account to plans
    question: How do I start a paid subscription for a sub account?
  phrasing_ops: 10
  slug: zoom-account-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Chat API from Zoom — 2 operation(s) for chat.
  name: Zoom Chat API
  phrasing_intents:
  - id: chatGet
    intent: Get messages from one chat session
    question: Can I read the actual messages from a chat conversation over a date range?
  - id: chatList
    intent: List chat history sessions for a period
    question: Which chat conversations happened during a given time period?
  phrasing_ops: 2
  slug: zoom-chat-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Cloud Recording operations
  name: Zoom Cloud Recording API
  phrasing_intents:
  - id: mcRecordingList
    intent: List recordings on a Meeting Connector
    question: Which meetings were recorded on our on-premise Meeting Connector?
  - id: recordingDelete
    intent: Delete a meeting recording
    question: Can I delete a recorded meeting whether it's in the cloud or on-premise?
  - id: recordingGet
    intent: Get a meeting's recording
    question: Where can I find the recording of a particular meeting?
  - id: recordingList
    intent: List a host's cloud recordings
    question: What cloud recordings does a host have?
  phrasing_ops: 4
  slug: zoom-cloud-recording-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Dashboard API from Zoom — 9 operation(s) for dashboard.
  name: Zoom Dashboard API
  phrasing_intents:
  - id: dashboardCrc
    intent: Get hourly CRC port usage
    question: How busy were our Cloud Room Connector ports hour by hour?
  - id: dashboardIm
    intent: Get IM usage statistics
    question: How much are people using instant messaging on our account?
  - id: dashboardMeetingdetail
    intent: Get dashboard details for one meeting
    question: What does the dashboard show for a single live or past meeting?
  - id: dashboardMeetings
    intent: List live or past meetings in a period
    question: Which meetings are running right now across the account?
  - id: dashboardQos
    intent: Get participants' quality of service in a meeting
    question: Why did a meeting have bad audio or video, and whose connection was it?
  - id: dashboardWebinardetail
    intent: Get dashboard details for one webinar
    question: What does the dashboard report for a single live or past webinar?
  - id: dashboardWebinars
    intent: List live or past webinars in a period
    question: Which webinars are live on our account right now?
  - id: dashboardZoomroomdetail
    intent: Get dashboard details for one Zoom Room
    question: How has one particular Zoom Room been used over a period?
  phrasing_ops: 9
  slug: zoom-dashboard-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Device API from Zoom — 4 operation(s) for device.
  name: Zoom Device API
  phrasing_intents:
  - id: deviceDeviceCreate
    intent: Add an H.323/SIP room device
    question: How do I register a H.323 or SIP conference room system with my account?
  - id: deviceDeviceDelete
    intent: Delete an H.323/SIP device
    question: Can I remove a SIP or H.323 device from the account?
  - id: deviceDeviceList
    intent: List H.323/SIP devices
    question: Which H.323 and SIP devices are registered on my account?
  - id: deviceDeviceUpdate
    intent: Update an H.323/SIP device
    question: Can I change the IP address of a registered room device?
  phrasing_ops: 4
  slug: zoom-device-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The Group API from Zoom — 8 operation(s) for group.
  name: Zoom Group API
  phrasing_intents:
  - id: groupCreate
    intent: Create a user group
    question: How do I set up a new group of users on my account?
  - id: groupDelete
    intent: Delete a user group
    question: Can I remove a group I no longer need?
  - id: groupEdit
    intent: Rename a user group
    question: Can I change the name of an existing group?
  - id: groupGet
    intent: Get a user group's info
    question: What information is stored for a particular group?
  - id: groupList
    intent: List all user groups
    question: Which groups exist on my Zoom account?
  - id: groupMemberAdd
    intent: Add members to a user group
    question: How can I put several users into a group at once?
  - id: groupMemberDelete
    intent: Remove members from a user group
    question: Can I take users out of a group without deleting the group?
  - id: groupMemberList
    intent: List a user group's members
    question: Who belongs to a particular group?
  phrasing_ops: 8
  slug: zoom-group-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: The IM Group API from Zoom — 7 operation(s) for im group.
  name: Zoom IM Group API
  phrasing_intents:
  - id: imGroupGroupCreate
    intent: Create an IM group
    question: How do I set up a new instant messaging group for my team?
  - id: imGroupGroupDelete
    intent: Delete an IM group
    question: Can I remove an instant messaging group we don't use anymore?
  - id: imGroupGroupEdit
    intent: Edit an IM group's name and search settings
    question: Can I rename an existing IM group or change its type?
  - id: imGroupGroupGet
    intent: Get an IM group's info
    question: What settings does a particular IM group have?
  - id: imGroupGroupList
    intent: List all IM groups
    question: Which instant messaging groups exist on our account?
  - id: imGroupGroupMemberDelete
    intent: Remove members from an IM group
    question: Can I take people out of an instant messaging group?
  - id: imGroupGroupMemberList
    intent: List an IM group's members
    question: Who is in a particular instant messaging group?
  phrasing_ops: 7
  slug: zoom-im-group-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Manage live streaming for Zoom meetings.
  name: Zoom Meeting Live Stream API
  phrasing_intents:
  - id: updateMeetingLiveStream
    intent: Configure a meeting's live stream
    question: How do I set up a meeting to stream to a custom streaming service?
  - id: updateMeetingLiveStreamStatus
    intent: Start or stop a meeting's live stream
    question: Can I start live streaming while a meeting is already running?
  - id: getMeetingJoinTokenForLiveStreaming
    intent: Get a join token for live streaming a meeting
    question: How does a streaming service or recording bot get permission to join a meeting?
  phrasing_ops: 3
  slug: zoom-meeting-live-stream-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Manage participants in Zoom meetings.
  name: Zoom Meeting Participants API
  phrasing_intents:
  - id: listMeetingParticipants
    intent: List participants via the Dashboard for a meeting
    question: Do I need the Dashboard feature on a paid plan to see who joined a meeting instance?
  - id: listPastMeetingParticipants
    intent: List participants of a past meeting
    question: Who attended a meeting that already ended?
  phrasing_ops: 2
  slug: zoom-meeting-participants-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Create and manage polls for Zoom meetings.
  name: Zoom Meeting Polls API
  phrasing_intents:
  - id: listMeetingPolls
    intent: List a meeting's polls
    question: What polls are set up for a meeting?
  - id: createMeetingPoll
    intent: Create a poll for a scheduled meeting
    question: How do I add a poll to a meeting ahead of time?
  - id: getMeetingPoll
    intent: Get a meeting poll's details
    question: What questions are in a specific poll on my meeting?
  - id: updateMeetingPoll
    intent: Update a meeting poll
    question: Can I edit the questions of a poll I already created?
  - id: deleteMeetingPoll
    intent: Delete a meeting poll
    question: Can I remove a poll from a meeting?
  phrasing_ops: 5
  slug: zoom-meeting-polls-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Access and manage meeting recordings.
  name: Zoom Meeting Recordings API
  phrasing_intents:
  - id: getMeetingRecordings
    intent: Get all recordings for a meeting
    question: Where do I find the cloud recording files from my meeting?
  - id: deleteMeetingRecordings
    intent: Delete all recording files of a meeting
    question: Can I delete every recording file from a meeting at once?
  phrasing_ops: 2
  slug: zoom-meeting-recordings-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Manage meeting registration and registrants.
  name: Zoom Meeting Registrants API
  phrasing_intents:
  - id: listMeetingRegistrants
    intent: List a meeting's registrants
    question: Who has registered for my meeting so far?
  - id: addMeetingRegistrant
    intent: Register one participant for a meeting
    question: How can a host register someone else for a meeting?
  - id: updateMeetingRegistrantStatus
    intent: Approve, deny or cancel meeting registrants
    question: How do I approve or deny people who registered for my meeting?
  - id: batchAddMeetingRegistrants
    intent: Register up to 30 people for a meeting at once
    question: Can I bulk-register a list of attendees for a meeting?
  phrasing_ops: 4
  slug: zoom-meeting-registrants-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Create and manage Zoom meetings.
  name: Zoom Meetings API
  phrasing_intents:
  - id: listMeetings
    intent: List a user's meetings
    question: What meetings are scheduled for a given user?
  - id: createMeeting
    intent: Create a meeting for a user
    question: How do I schedule a meeting for a user?
  - id: getMeeting
    intent: Get a meeting's details
    question: What are the settings, recurrence and tracking fields on a meeting?
  - id: updateMeeting
    intent: Update a meeting's details
    question: Can I change the topic or start time of a meeting already scheduled?
  - id: deleteMeeting
    intent: Delete a meeting
    question: Can I cancel a meeting and notify the registrants?
  - id: updateMeetingStatus
    intent: End a meeting or recover a deleted one
    question: Can I end a meeting by changing its status?
  - id: getPastMeetingDetails
    intent: Get details of a past meeting
    question: What information is available about a meeting that already happened?
  - id: getMeetingInvitation
    intent: Get a meeting's invitation text
    question: Where do I get the invitation note to send to attendees?
  phrasing_ops: 8
  slug: zoom-meetings-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Report operations
  name: Zoom Report API
  phrasing_intents:
  - id: reportGetaccountreport
    intent: Get the account usage report for a period
    question: How much has our whole account used Zoom over a date range?
  - id: reportGetaudioreport
    intent: Get the toll audio report for a period
    question: What were our phone dial-in toll charges for a period?
  - id: reportGetdailyreport
    intent: Get the daily usage report for a month
    question: What did daily usage look like for a given month?
  - id: reportGetuserreport
    intent: Get one user's usage report for a period
    question: How many meetings did a specific user host over a period?
  phrasing_ops: 4
  slug: zoom-report-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: User operations
  name: Zoom User API
  phrasing_intents:
  - id: userAssistantDelete
    intent: Remove a host's scheduling assistant
    question: Can I take away someone's assistant access so they stop scheduling meetings for a host?
  - id: userAssistantSet
    intent: Assign a scheduling assistant to a host
    question: How can I let an assistant schedule meetings on behalf of a host?
  - id: userAutocreate
    intent: Auto-create a user with a password on a managed domain
    question: Can an enterprise account on a managed domain create users with a password set up front?
  - id: userCheckemail
    intent: Check whether a user email already exists
    question: Is there already a Zoom user registered with this email address?
  - id: userCheckzpk
    intent: Check whether a user's zpk token has expired
    question: What is a zpk and how can I tell if it has expired?
  - id: userCreate
    intent: Provision a new user as a trusted partner
    question: Which privilege does my account need to provision users through the API?
  - id: userCustcreate
    intent: Create a passwordless API-plan user
    question: Can I create users who have no password and never log in to the web site or client?
  - id: userActivate
    intent: Activate a user
    question: How do I reactivate a Zoom user who was deactivated?
  phrasing_ops: 20
  slug: zoom-user-api
- baseURL: https://api.zoom.us/v2
  baseurl_source: declared
  description: Webinar operations
  name: Zoom Webinar API
  phrasing_intents:
  - id: webinarAttendeesList
    intent: List attendees of an ended webinar
    question: Who actually showed up to a webinar after it ended?
  - id: webinarCreate
    intent: Schedule a webinar
    question: How do I schedule a new webinar and get its start and join links?
  - id: webinarDelete
    intent: Delete a webinar
    question: Can I delete just one occurrence of a recurring webinar?
  - id: webinarEnd
    intent: End a running webinar
    question: Is there a way to force a live webinar to end for everyone?
  - id: webinarGet
    intent: Get a webinar's details
    question: What settings and schedule does a particular webinar have?
  - id: webinarList
    intent: List a host's registrationless webinars
    question: Which webinars that don't need registration does a host have?
  - id: webinarListRegistration
    intent: List a host's upcoming registration webinars
    question: What upcoming webinars require attendees to register first?
  - id: webinarPanelists
    intent: List a webinar's panelists
    question: Who are the panelists on a given webinar?
  phrasing_ops: 17
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
artifact_total: 214
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
- group: commercial
  href: https://artifacts.apis.io/zoom/plans/zoom-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zoom-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/zoom/finops/zoom-finops.yml
  title: ''
  type: FinOps
  url: finops/zoom-finops.yml
- group: company
  title: ''
  type: Website
  url: https://zoom.us
- group: other
  href: https://artifacts.apis.io/zoom/capabilities/zoom-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zoom-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/zoom/api/issues
- group: agent
  href: https://artifacts.apis.io/zoom/agentic-access/zoom-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zoom-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/zoom/security/zoom-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoom-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zoom/security/zoom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zoom-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/zoom/authentication/zoom-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zoom-authentication.yml
- group: auth
  href: https://artifacts.apis.io/zoom/scopes/zoom-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/zoom-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zoom/overview
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-account-then-user-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-account-then-user-report-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-approve-meeting-registrants-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-approve-meeting-registrants-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-approve-webinar-registrants-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-approve-webinar-registrants-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-batch-register-attendees-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-batch-register-attendees-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-chat-history-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-chat-history-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-create-and-confirm-meeting-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-create-and-confirm-meeting-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-create-and-confirm-webinar-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-create-and-confirm-webinar-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-create-and-get-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-create-and-get-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-create-meeting-poll-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-create-meeting-poll-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-delete-recording-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-delete-recording-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-end-meeting-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-end-meeting-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-list-and-get-recording-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-list-and-get-recording-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-list-meetings-detail-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-list-meetings-detail-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-meeting-live-stream-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-meeting-live-stream-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-meeting-recordings-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-meeting-recordings-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-meeting-registration-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-meeting-registration-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-onboard-user-with-meeting-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-onboard-user-with-meeting-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-past-meeting-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-past-meeting-report-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-resolve-user-by-email-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-resolve-user-by-email-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-update-meeting-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-update-meeting-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-user-report-recordings-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/zoom-user-report-recordings-workflow.yml
- group: design
  href: https://artifacts.apis.io/zoom/arazzo/zoom-webinar-registration-workflow.yml
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
  href: https://artifacts.apis.io/zoom/json-ld/zoom-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zoom-context.jsonld
- group: design
  href: https://artifacts.apis.io/zoom/rules/zoom-spectral-rules.yml
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
- has_sources: true
  method: generated
  name: Zoom Finops
  primary_unit: ''
  service_category: Video Conferencing
  slug: zoom-finops
  template: false
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
mcp_servers:
- description: Remote MCP server at mcp.zoom.us over HTTP.
  name: Zoom MCP Server
  slug: zoom
modified: '2026-09-16'
name: Zoom
nav: Providers
network: true
overview: 'Zoom publishes 47 API contracts indexed on the [APIs.io](https://apis.io/) network, including Meeting API, Account API, Chat API, and 44 more. Tagged areas include Video, Zoom, Chat, Collaboration, and Communications.


  The Zoom catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Zoom''s developer surface includes authentication, getting-started guide, changelog, support, developer portal, documentation, engineering blog, and 47 more developer resources.'
plans:
- name: Zoom Plans Pricing
  plan_count: 4
  slug: zoom-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Zoom Rate Limits
  slug: zoom-rate-limits
rules:
- authorship: generated
  effective_rule_count: 37
  extends:
  - spectral:asyncapi
  name: Zoom — asyncapi rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 9
  slug: zoom-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Zoom — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: zoom-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 57
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
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 67.5
    catalog_earned_first_party: 0.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 13.6
    contract_quality: 68.0
    developer_ergonomics: 64.8
    discoverability: 80.0
    operational_transparency: 39.5
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/zoom/zoom-2026-06-20T165938.png
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
- Video
- Zoom
- Chat
- Collaboration
- Communications
- Meetings
- Video Conferencing
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
website: https://zoom.us
---

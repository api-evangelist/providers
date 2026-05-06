---
aid: webex
name: Webex
description: Cisco Webex is a comprehensive collaboration platform offering APIs for messaging, meetings, calling, devices, and contact center workflows. The Webex Developer Platform enables developers to build integrations, bots, embedded apps, and automations using REST APIs, SDKs, and webhooks. Webex supports OAuth 2.0 authentication and provides separate API surfaces for messaging, video conferencing, cloud calling, admin management, and more.
type: Index
position: Consumer
access: 3rd-Party
image: https://developer.webex.com/images/webex-logo.png
tags:
  - Calling
  - Collaboration
  - Communication
  - Enterprise
  - Messaging
  - Video Conferencing
url: https://raw.githubusercontent.com/api-evangelist/webex/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: webex:messaging
    name: Webex Messaging
    description: Webex Messaging API for creating and managing rooms, messages, attachments, teams, memberships, and real-time collaboration. Supports text, markdown, file sharing, and webhook event subscriptions.
    humanURL: https://developer.webex.com/docs/messaging
    tags:
      - Bots
      - Collaboration
      - Messaging
      - Rooms
      - Teams
      - Webhooks
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/messaging
      - type: OpenAPI
        url: openapi/webex-messaging-openapi.json
  - aid: webex:meetings
    name: Webex Meetings
    description: Webex Meetings API for scheduling, managing, and reporting on video meetings. Provides endpoints for meeting lifecycle management, invitees, participants, recordings, transcripts, and meeting templates.
    humanURL: https://developer.webex.com/docs/meetings
    tags:
      - Meetings
      - Recordings
      - Scheduling
      - Video Conferencing
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/meetings
      - type: OpenAPI
        url: openapi/webex-meeting-openapi.json
  - aid: webex:admin
    name: Webex Admin
    description: Webex Admin API for managing organizations, users, licenses, locations, workspaces, devices, and organization settings. Provides administrative control over Webex deployments including PSTN settings and call policies.
    humanURL: https://developer.webex.com/docs/admin
    tags:
      - Administration
      - Devices
      - Licenses
      - Organizations
      - Users
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/admin
      - type: OpenAPI
        url: openapi/webex-admin-openapi.json
  - aid: webex:cloud-calling
    name: Webex Cloud Calling
    description: Webex Cloud Calling API with 633 endpoints for managing users, locations, call settings, hunt groups, auto-attendants, voicemail, call queues, and PSTN configurations for cloud-based telephony.
    humanURL: https://developer.webex.com/docs/cloud-calling
    tags:
      - Auto Attendant
      - Call Management
      - Calling
      - Cloud Telephony
      - PSTN
      - Voicemail
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/cloud-calling
      - type: OpenAPI
        url: openapi/webex-cloud-calling-openapi.json
  - aid: webex:contact-center
    name: Webex Contact Center
    description: Webex Contact Center API for managing customer service operations including agents, queues, routing strategies, skills, and reporting. Enables programmatic control of contact center configurations and workflows.
    humanURL: https://developer.webex.com/docs/contact-center
    tags:
      - Agents
      - Contact Center
      - Customer Service
      - Queues
      - Routing
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/contact-center
      - type: OpenAPI
        url: openapi/webex-contact-center-openapi.json
  - aid: webex:devices
    name: Webex Devices
    description: Webex Device API for managing Webex hardware devices, workspaces, and device configurations. Includes endpoints for device inventory, activation, workspace assignments, and device-specific settings.
    humanURL: https://developer.webex.com/docs/devices
    tags:
      - Devices
      - Hardware
      - Workspaces
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/devices
      - type: OpenAPI
        url: openapi/webex-device-openapi.json
  - aid: webex:broadworks
    name: Webex Broadworks Calling
    description: Webex Broadworks Calling API for managing BroadWorks subscriber provisioning and migration to Webex. Enables service providers to integrate BroadWorks telephony infrastructure with Webex cloud services.
    humanURL: https://developer.webex.com/docs/broadworks
    tags:
      - BroadWorks
      - Calling
      - Service Provider
      - Telephony
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/broadworks
      - type: OpenAPI
        url: openapi/webex-broadworks-openapi.json
  - aid: webex:ucm
    name: Webex for UCM
    description: Webex for Unified CM (UCM) API for managing on-premises Cisco Unified Communications Manager integration with Webex cloud services. Supports hybrid calling configurations.
    humanURL: https://developer.webex.com/docs/ucm
    tags:
      - Calling
      - On-Premises
      - Unified CM
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/ucm
      - type: OpenAPI
        url: openapi/webex-ucm-openapi.json
  - aid: webex:wholesale
    name: Webex Wholesale
    description: Webex Wholesale API for service provider partners to provision and manage Webex Wholesale (RTM) customers and subscriptions at scale. Enables white-label Webex deployment workflows.
    humanURL: https://developer.webex.com/docs/wholesale
    tags:
      - Partner
      - Provisioning
      - Service Provider
      - Wholesale
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/wholesale
      - type: OpenAPI
        url: openapi/webex-wholesale-openapi.json
common:
  - url: https://developer.webex.com/
    name: Webex Developer Portal
    type: Portal
    description: Main developer portal for Webex APIs, documentation, and sandbox.
  - url: https://developer.webex.com/docs/getting-started
    name: Getting Started with Webex APIs
    type: GettingStarted
    description: Quick start guide for authenticating and making your first Webex API call.
  - url: https://developer.webex.com/docs/authentication
    name: Webex Authentication
    type: Authentication
    description: OAuth 2.0 authentication flows and personal access tokens for Webex APIs.
  - url: https://developer.webex.com/docs/sdks
    name: Webex SDKs
    type: SDK
    description: Official Webex SDKs for JavaScript, iOS, Android, and other platforms.
  - url: https://github.com/webex/webex-js-sdk
    name: Webex JavaScript SDK
    type: SDK
    title: JavaScript SDK
    description: Official JavaScript SDK for Webex APIs.
  - url: https://github.com/webex/webex-ios-sdk
    name: Webex iOS SDK
    type: SDK
    title: iOS SDK
    description: Official iOS SDK for Webex APIs.
  - url: https://github.com/webex/webex-android-sdk
    name: Webex Android SDK
    type: SDK
    title: Android SDK
    description: Official Android SDK for Webex APIs.
  - url: https://developer.webex.com/blog
    name: Webex Developer Blog
    type: Blog
    description: Updates, tutorials, and announcements from the Webex developer team.
  - url: https://status.webex.com
    name: Webex Status
    type: StatusPage
    description: Real-time status and incident reports for Webex services.
  - url: https://developer.webex.com/support
    name: Webex Developer Support
    type: Support
    description: Developer community and support resources.
  - url: https://www.cisco.com/c/en/us/about/legal/terms-conditions.html
    name: Webex Terms of Service
    type: TermsOfService
    description: Terms and conditions for Cisco Webex services.
  - url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
    name: Webex Privacy Policy
    type: PrivacyPolicy
    description: Privacy policy for Cisco Webex services.
  - url: https://developer.webex.com/docs/rate-limiting
    name: Webex Rate Limits
    type: RateLimits
    description: API rate limiting policies for Webex developer APIs.
  - url: https://github.com/webex
    name: Webex GitHub Organization
    type: GitHubOrganization
    description: Official Webex GitHub organization with SDKs, samples, and specs.
  - url: https://github.com/webex/webex-openapi-specs
    name: Webex OpenAPI Specifications
    type: GitHubRepository
    description: Official repository of all public Webex API OpenAPI specifications.
  - type: SpectralRules
    url: rules/webex-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/webex-vocabulary.yml
  - type: NaftikoCapability
    url: capabilities/team-collaboration.yaml
  - type: JSONLD
    url: json-ld/webex-messaging-context.jsonld
  - type: JSONLD
    url: json-ld/webex-meeting-context.jsonld
  - type: JSONLD
    url: json-ld/webex-admin-context.jsonld
  - type: JSONLD
    url: json-ld/webex-device-context.jsonld
  - name: Webex Features
    type: Features
    data:
      - 'Cisco Webex: hundreds of services across Collaboration'
      - 'Detailed pricing: see https://www.webex.com/pricing/index.html'
      - 'Service: Webex Meetings'
      - 'Service: Webex Calling'
      - 'Service: Webex Messaging'
      - 'Service: Webex Events'
      - 'Service: Webex Webinars'
      - 'Service: Webex Contact Center'
      - 'Service: Webex Connect (CPaaS)'
      - 'Service: Free / Webex Plus / Webex Suite / Enterprise tiers'
    sources:
      - https://www.webex.com/pricing/index.html
      - https://focus.finops.org/
    updated: '2026-05-04'
  - name: Webex Use Cases
    type: UseCases
    data:
      - name: Collaboration Automation
        description: Automate room creation, messaging workflows, and team management using the Messaging API.
      - name: Meeting Scheduling Integration
        description: Integrate Webex meeting scheduling into CRM, calendar, or project management applications.
      - name: Custom Bot Development
        description: Build intelligent chatbots that respond to user commands and integrate with business systems.
      - name: Contact Center Automation
        description: Programmatically configure contact center queues, routing strategies, and agent assignments.
      - name: Unified Communications Administration
        description: Automate user provisioning, license assignment, and calling configuration at scale.
      - name: Event-Driven Workflows
        description: Use webhooks to trigger business workflows when messages are sent, meetings start, or rooms change.
  - name: Webex Integrations
    type: Integrations
    data:
      - name: Salesforce
        description: Webex for Salesforce integration for CRM-embedded collaboration.
      - name: Microsoft Teams
        description: Interoperability integration between Webex and Microsoft Teams.
      - name: Slack
        description: Webex integration with Slack for cross-platform notifications and workflows.
      - name: Jira
        description: Webex App Hub integration with Atlassian Jira for project tracking.
      - name: ServiceNow
        description: Webex integration with ServiceNow for IT service management workflows.
      - name: Google Workspace
        description: Webex integration with Google Calendar and Gmail.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

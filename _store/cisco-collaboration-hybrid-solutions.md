---
aid: cisco-collaboration-hybrid-solutions
url: https://raw.githubusercontent.com/api-evangelist/cisco-collaboration-hybrid-solutions/refs/heads/main/apis.yml
name: Cisco Collaboration Hybrid Solutions
tags:
  - Calling
  - Collaboration
  - Hybrid Cloud
  - Meetings
  - Messaging
  - Unified Communications
  - Webex
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-15'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: APIs for Cisco's hybrid collaboration solutions that combine Webex cloud services with on-premises Unified Communications Manager (CUCM), Expressway, and supporting infrastructure. Hybrid Services let an organization keep calling, calendaring, and identity on-premises while using Webex for meetings, messaging, devices, and management.
apis:
  - aid: cisco-collaboration-hybrid-solutions:webex-api
    name: Webex APIs
    tags:
      - Collaboration
      - Meetings
      - Messaging
      - Spaces
      - Teams
    humanURL: https://developer.webex.com/
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/getting-started
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
      - url: https://developer.webex.com/docs/integrations
        type: Authentication
      - url: https://developer.webex.com/docs/sdks
        type: SDKs
    description: Core Webex platform APIs for messaging, meetings, teams, spaces, memberships, attachments, and webhooks.
  - aid: cisco-collaboration-hybrid-solutions:webex-meetings
    name: Webex Meetings API
    tags:
      - Meetings
      - Recordings
      - Scheduling
    humanURL: https://developer.cisco.com/docs/webex-meetings/
    baseURL: https://webexapis.com/v1/meetings
    properties:
      - url: https://developer.cisco.com/docs/webex-meetings/
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/meetings
        type: Reference
    description: Schedule, list, update, and cancel Webex meetings; manage participants, recordings, transcripts, and meeting templates.
  - aid: cisco-collaboration-hybrid-solutions:webex-hybrid-services
    name: Webex Hybrid Services API
    tags:
      - Calendar
      - Connectors
      - Hybrid
      - Media
    humanURL: https://developer.cisco.com/docs/webex-hybrid-services/
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.cisco.com/docs/webex-hybrid-services/
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/hybrid-clusters
        type: Reference
    description: Manage Webex Hybrid Calendar, Hybrid Call Service, Hybrid Message, Video Mesh nodes, and other connectors that bridge on-premises collaboration infrastructure to the Webex cloud.
  - aid: cisco-collaboration-hybrid-solutions:webex-calling
    name: Webex Calling API
    tags:
      - Call Control
      - Calling
      - Telephony
      - Voicemail
    humanURL: https://developer.webex.com/docs/api/v1/webex-calling
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/webex-calling
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/call-controls
        type: Reference
    description: Cloud calling capabilities including call control, dial plans, voicemail, voice portals, queues, hunt groups, and number provisioning.
  - aid: cisco-collaboration-hybrid-solutions:control-hub
    name: Control Hub API
    tags:
      - Administration
      - Management
      - Organizations
      - Users
    humanURL: https://developer.webex.com/docs/api/v1/organizations
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/organizations
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/admin-audit-events
        type: Reference
    description: Administer Webex organizations, users, licenses, audit events, and service settings programmatically.
  - aid: cisco-collaboration-hybrid-solutions:webex-devices
    name: Webex Devices API
    tags:
      - Devices
      - Endpoints
      - Room Systems
    humanURL: https://developer.webex.com/docs/api/v1/devices
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/devices
        type: Documentation
      - url: https://roomos.cisco.com/xapi
        type: xAPI Reference
    description: Manage and control Webex Room and Desk Devices including remote configuration, status queries, and the device-side xAPI.
  - aid: cisco-collaboration-hybrid-solutions:webex-events
    name: Webex Events API
    tags:
      - Events
      - Virtual Events
      - Webinars
    humanURL: https://developer.webex.com/docs/api/v1/events
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/events
        type: Documentation
    description: Create and manage Webex Webinars and large-format virtual events, including registration, panelists, and analytics.
common:
  - type: Portal
    url: https://developer.cisco.com/collaboration/
  - type: Webex Developer Portal
    url: https://developer.webex.com/
  - type: Getting Started
    url: https://developer.webex.com/docs/getting-started
  - type: Authentication
    url: https://developer.webex.com/docs/integrations
  - type: Webhooks
    url: https://developer.webex.com/docs/api/guides/webhooks
  - type: Change Log
    url: https://developer.webex.com/changelog
  - type: Status
    url: https://status.webex.com/
  - type: Community
    url: https://community.cisco.com/t5/collaboration-voice-and-video/bd-p/discussions-collaboration
  - type: GitHub Organization
    url: https://github.com/WebexSamples
  - type: Privacy Policy
    url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
  - type: Terms of Service
    url: https://www.cisco.com/c/en/us/about/legal/terms-conditions.html
  - type: JSON-LD
    url: json-ld/cisco-collaboration-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

---
aid: cisco-control-hub
url: https://raw.githubusercontent.com/api-evangelist/cisco-control-hub/refs/heads/main/apis.yml
name: Cisco Control Hub
tags:
  - Administration
  - Calling
  - Collaboration
  - Communications
  - Device Management
  - Identity Management
  - Licenses
  - Reporting
  - Webex
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-01'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: Cisco Control Hub is the administration console for Webex services. Programmatic access is delivered through the Webex Admin and adjacent REST APIs at webexapis.com — covering people, organizations, locations, workspaces, devices, licenses, calling configuration, audit events, and analytics reports. Authentication uses OAuth 2.0 access tokens or service-app tokens scoped to the organization.
apis:
  - aid: cisco-control-hub:webex-admin-api
    name: Webex Admin API
    tags:
      - Administration
      - Audit
      - Organizations
      - Users
    humanURL: https://developer.webex.com/docs/api/v1/admin-audit-events
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/admin-audit-events
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
      - url: https://developer.webex.com/docs/getting-started#accounts-and-authentication
        type: Authentication
    description: Manage users, licenses, organization settings, and admin audit events for a Webex organization.
  - aid: cisco-control-hub:webex-calling-api
    name: Webex Calling API
    tags:
      - Calling
      - Phone Numbers
      - Telephony
      - Voice
    humanURL: https://developer.webex.com/docs/api/v1/webex-calling-organization-settings
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/webex-calling-organization-settings
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
    description: Manage Webex Calling features, phone numbers, dial plans, voice portals, and other organization-wide voice settings.
  - aid: cisco-control-hub:webex-devices-api
    name: Webex Devices API
    tags:
      - Configuration
      - Devices
      - Endpoints
      - Room Systems
    humanURL: https://developer.webex.com/docs/api/v1/devices
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/devices
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
    description: Manage Webex Room and Desk Devices, MPP phones, and headsets; query device status and push configuration.
  - aid: cisco-control-hub:webex-workspaces-api
    name: Webex Workspaces API
    tags:
      - Locations
      - Meeting Rooms
      - Workspaces
    humanURL: https://developer.webex.com/docs/api/v1/workspaces
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/workspaces
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
    description: Manage physical and virtual workspaces, meeting rooms, and shared-mode devices.
  - aid: cisco-control-hub:webex-people-api
    name: Webex People API
    tags:
      - Directory
      - People
      - Profiles
      - Users
    humanURL: https://developer.webex.com/docs/api/v1/people
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/people
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
    description: Manage user profiles, status, presence, and directory information.
  - aid: cisco-control-hub:webex-organizations-api
    name: Webex Organizations API
    tags:
      - Configuration
      - Organizations
      - Settings
    humanURL: https://developer.webex.com/docs/api/v1/organizations
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/organizations
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
    description: Inspect and manage Webex organization metadata and global settings.
  - aid: cisco-control-hub:webex-licenses-api
    name: Webex Licenses API
    tags:
      - Entitlements
      - Licenses
      - Subscriptions
    humanURL: https://developer.webex.com/docs/api/v1/licenses
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/licenses
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
    description: List and assign Webex licenses and subscription entitlements to users.
  - aid: cisco-control-hub:webex-locations-api
    name: Webex Locations API
    tags:
      - Calling
      - Geography
      - Locations
    humanURL: https://developer.webex.com/docs/api/v1/locations
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/locations
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
    description: Manage geographic locations used by Webex Calling for emergency services routing, time zones, and number assignments.
  - aid: cisco-control-hub:webex-reports-api
    name: Webex Reports API
    tags:
      - Analytics
      - Metrics
      - Reports
      - Usage
    humanURL: https://developer.webex.com/docs/api/v1/reports
    baseURL: https://webexapis.com/v1
    properties:
      - url: https://developer.webex.com/docs/api/v1/reports
        type: Documentation
      - url: https://developer.webex.com/docs/api/v1/openapi.json
        type: OpenAPI
    description: Generate and download analytics and usage reports for Webex services.
common:
  - type: Portal
    url: https://developer.webex.com
  - type: Console
    url: https://admin.webex.com
  - type: Authentication
    url: https://developer.webex.com/docs/getting-started#accounts-and-authentication
  - type: Rate Limits
    url: https://developer.webex.com/docs/api-guidelines#rate-limiting
  - type: Status
    url: https://status.webex.com
  - type: Support
    url: https://developer.webex.com/support
  - type: Change Log
    url: https://developer.webex.com/changelog
  - type: GitHub Organization
    url: https://github.com/WebexSamples
  - type: Terms of Service
    url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end-user-license-agreement.html
  - type: Privacy Policy
    url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
  - type: JSON-LD
    url: json-ld/cisco-control-hub-context.jsonld
  - type: Spectral
    url: rules/cisco-control-hub-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

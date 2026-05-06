---
aid: opsgenie
name: OpsGenie
description: OpsGenie is an incident management and alerting platform, now part of Atlassian, that helps operations teams manage on-call schedules, route alerts, and coordinate incident response. The OpsGenie developer platform provides a comprehensive set of REST APIs for programmatically managing alerts, incidents, teams, schedules, escalations, integrations, heartbeats, services, notification rules, accounts, and maintenance windows.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Alerts
  - Incident Management
  - Monitoring
  - On-Call
  - Operations
created: '2025-03-01'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/opsgenie/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: opsgenie:opsgenie-alert
    name: OpsGenie Alert API
    description: Programmatically create, update, close, and manage alerts within the OpsGenie incident management platform. Alert creation, deletion, and action requests are processed asynchronously to provide higher availability and scalability. Supports alert priorities, responders, tags, custom details, notes, and acknowledgments.
    humanURL: https://docs.opsgenie.com/docs/alert-api
    baseURL: https://api.opsgenie.com
    tags:
      - Alerts
      - Incident Management
      - Monitoring
      - Notifications
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/alert-api
      - type: OpenAPI
        url: openapi/opsgenie-alert-openapi.yml
      - type: JSONSchema
        url: json-schema/opsgenie-alert-schema.json
  - aid: opsgenie:opsgenie-incident
    name: OpsGenie Incident API
    description: Create and manage incidents programmatically. Supports defining responders, tags, custom details, priority levels, and impacted services for each incident. Available to Standard and Enterprise plan users with endpoints for creating, updating, closing, and resolving incidents in a structured response workflow.
    humanURL: https://docs.opsgenie.com/docs/incident-api
    baseURL: https://api.opsgenie.com
    tags:
      - Incidents
      - Incident Management
      - Operations
      - Response
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/incident-api
      - type: OpenAPI
        url: openapi/opsgenie-incident-openapi.yml
      - type: JSONSchema
        url: json-schema/opsgenie-incident-schema.json
  - aid: opsgenie:opsgenie-user
    name: OpsGenie User API
    description: Manage user accounts within the OpsGenie platform. Create, retrieve, update, and delete users, list users, and retrieve escalations associated with specific users. Supports managing user roles, contact methods, and notification preferences.
    humanURL: https://docs.opsgenie.com/docs/user-api
    baseURL: https://api.opsgenie.com
    tags:
      - Users
      - Accounts
      - Identity
      - Management
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/user-api
      - type: OpenAPI
        url: openapi/opsgenie-user-openapi.yml
  - aid: opsgenie:opsgenie-team
    name: OpsGenie Team API
    description: Manage teams within the OpsGenie platform. Create, update, retrieve, and delete teams, manage team members and their roles. Teams are a core organizational unit used to route alerts and assign on-call responsibilities to groups of users.
    humanURL: https://docs.opsgenie.com/docs/team-api
    baseURL: https://api.opsgenie.com
    tags:
      - Teams
      - Groups
      - Collaboration
      - Management
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/team-api
      - type: OpenAPI
        url: openapi/opsgenie-team-openapi.yml
  - aid: opsgenie:opsgenie-schedule
    name: OpsGenie Schedule API
    description: Programmatically manage on-call schedules and rotations. Create, update, and delete schedules, manage rotations and overrides, and query who is currently on call. Enables custom dashboards and integrations that reflect real-time on-call status.
    humanURL: https://docs.opsgenie.com/docs/schedule-api
    baseURL: https://api.opsgenie.com
    tags:
      - Schedules
      - On-Call
      - Rotations
      - Planning
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/schedule-api
      - type: OpenAPI
        url: openapi/opsgenie-schedule-openapi.yml
  - aid: opsgenie:opsgenie-escalation
    name: OpsGenie Escalation API
    description: Manage escalation policies that define how alerts are routed when initial responders do not acknowledge them. Create, update, retrieve, and delete escalation configurations with rules defining sequence of notifications and configurable delay intervals.
    humanURL: https://docs.opsgenie.com/docs/escalation-api
    baseURL: https://api.opsgenie.com
    tags:
      - Escalations
      - Routing
      - Alerts
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/escalation-api
      - type: OpenAPI
        url: openapi/opsgenie-escalation-openapi.yml
  - aid: opsgenie:opsgenie-integration
    name: OpsGenie Integration API
    description: Programmatically manage integrations that connect OpsGenie with third-party monitoring, ticketing, and communication tools. Create, enable, disable, and configure integrations and their associated actions. Note that Zendesk, Slack, and Incoming Call integrations must be configured through the OpsGenie web interface.
    humanURL: https://docs.opsgenie.com/docs/integration-api
    baseURL: https://api.opsgenie.com
    tags:
      - Integrations
      - Connections
      - Third Party
      - Automation
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/integration-api
      - type: OpenAPI
        url: openapi/opsgenie-integration-openapi.yml
      - type: AsyncAPI
        url: asyncapi/opsgenie-webhook-asyncapi.yml
  - aid: opsgenie:opsgenie-heartbeat
    name: OpsGenie Heartbeat API
    description: Set up and manage heartbeat monitors that track the health and availability of systems and services. Heartbeats expect periodic pings from monitored systems and generate an alert when a ping is not received within the configured interval.
    humanURL: https://docs.opsgenie.com/docs/heartbeat-api
    baseURL: https://api.opsgenie.com
    tags:
      - Heartbeat
      - Health Checks
      - Monitoring
      - Uptime
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/heartbeat-api
      - type: OpenAPI
        url: openapi/opsgenie-heartbeat-openapi.yml
      - type: JSONSchema
        url: json-schema/opsgenie-heartbeat-schema.json
  - aid: opsgenie:opsgenie-service
    name: OpsGenie Service API
    description: Manage services within the OpsGenie platform. Services represent business-critical applications and components that can be associated with incidents to track impact. Used in conjunction with the Incident API to identify which services are affected during an outage.
    humanURL: https://docs.opsgenie.com/docs/service-api
    baseURL: https://api.opsgenie.com
    tags:
      - Services
      - Service Catalog
      - Operations
      - Management
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/service-api
      - type: OpenAPI
        url: openapi/opsgenie-service-openapi.yml
  - aid: opsgenie:opsgenie-notification-rule
    name: OpsGenie Notification Rule API
    description: Manage notification rules that control how and when users receive alert notifications. Create, update, and delete notification rules, including conditions, time restrictions, and notification channels such as email, SMS, push notifications, and voice calls.
    humanURL: https://docs.opsgenie.com/docs/notification-rule-api
    baseURL: https://api.opsgenie.com
    tags:
      - Notifications
      - Rules
      - Alerts
      - Configuration
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/notification-rule-api
      - type: OpenAPI
        url: openapi/opsgenie-notification-rule-openapi.yml
  - aid: opsgenie:opsgenie-account
    name: OpsGenie Account API
    description: Retrieve account-level information and configuration settings. Access details about an OpsGenie account including plan information and account metadata. Foundational API for administrative operations and account management.
    humanURL: https://docs.opsgenie.com/docs/account-api
    baseURL: https://api.opsgenie.com
    tags:
      - Accounts
      - Administration
      - Settings
      - Configuration
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/account-api
      - type: OpenAPI
        url: openapi/opsgenie-account-openapi.yml
  - aid: opsgenie:opsgenie-maintenance
    name: OpsGenie Maintenance API
    description: Manage maintenance windows that suppress alert notifications during planned maintenance periods. Create, update, list, and delete maintenance windows with configurable time ranges and rules for which integrations or policies are affected.
    humanURL: https://docs.opsgenie.com/docs/maintenance-api
    baseURL: https://api.opsgenie.com
    tags:
      - Maintenance
      - Windows
      - Scheduling
      - Operations
    properties:
      - type: Documentation
        url: https://docs.opsgenie.com/docs/maintenance-api
      - type: OpenAPI
        url: openapi/opsgenie-maintenance-openapi.yml
common:
  - type: Portal
    name: OpsGenie Documentation Portal
    url: https://docs.opsgenie.com/
  - type: Documentation
    name: OpsGenie Documentation
    url: https://docs.opsgenie.com/docs
  - type: Website
    name: OpsGenie Website
    url: https://www.atlassian.com/software/opsgenie
  - type: PrivacyPolicy
    name: Atlassian Privacy Policy
    url: https://www.atlassian.com/legal/privacy-policy
  - type: TermsOfService
    name: Atlassian Terms of Service
    url: https://www.atlassian.com/legal/software-license-agreement
  - type: Support
    name: Atlassian OpsGenie Support
    url: https://support.atlassian.com/opsgenie/
  - type: Blog
    name: Atlassian Blog
    url: https://www.atlassian.com/blog
  - type: Login
    name: OpsGenie Login
    url: https://app.opsgenie.com/auth/login
  - type: Features
    data:
      - 'Free: 5 users, 1 schedule, 1 escalation policy'
      - 'Essentials: $9.45/user/mo'
      - 'Standard: $19.95/user/mo with stakeholder comms + dashboards'
      - 'Enterprise: $31.90/user/mo with PIRs, audit logs, ServiceNow'
      - 'End-of-life: new sales ended 2025-06-04; migrate to JSM/Compass by 2027-04-05'
      - REST API at api.opsgenie.com (eu/us regions)
      - 'Alerts API: 60 req/min standard, up to 10K req/min for HV integrations'
      - 'Other endpoints: 600 req/min/key'
      - 200+ integrations with monitoring tools
      - On-call schedules with rotations
      - Escalation policies with multi-channel notification
      - Heartbeat monitoring (Standard+)
      - Status pages built-in (Essentials+)
      - Post-incident reviews (Enterprise)
      - Audit logs (Enterprise)
      - GenieKey-based authentication (per integration)
    sources:
      - https://www.atlassian.com/software/opsgenie/pricing
    updated: '2026-05-04'
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---

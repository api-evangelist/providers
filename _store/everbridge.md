---
aid: everbridge
url: https://raw.githubusercontent.com/api-evangelist/everbridge/refs/heads/main/apis.yml
apis:
- name: Everbridge Suite API
  description: The Everbridge Suite REST API enables developers to integrate Everbridge's critical event management platform into their applications. It provides endpoints for managing contacts, groups, organizations, notifications, incidents, calendars, conference bridges, locations, and more.
  image: https://www.everbridge.com/wp-content/uploads/2021/01/everbridge-logo.svg
  humanURL: https://developers.everbridge.net/home
  baseURL: https://api.everbridge.net/rest
  tags:
  - Contacts
  - Groups
  - Incidents
  - Mass Notification
  - Notifications
  - Organizations
  properties:
  - type: Documentation
    url: https://developers.everbridge.net/home/docs/overview
  - type: OpenAPI
    url: https://api.everbridge.net/rest/swagger.json
  - type: Reference
    url: https://api.everbridge.net/
  - type: Authentication
    url: https://developers.everbridge.net/home/docs/ebs-gs-guide-authentication-types
  - type: Getting Started
    url: https://developers.everbridge.net/home/docs/ebs-gs-guide
  - type: Rate Limits
    url: https://developers.everbridge.net/home/docs/ebs-gs-guide-throttling-limits
  - type: Change Log
    url: https://developers.everbridge.net/home/changelog
- name: Everbridge Asset Management API
  description: The Everbridge Asset Management API allows organizations to manage assets, asset types, asset associations, and related templates. It supports batch operations for bulk asset management and provides license limit statistics for asset tracking within the Everbridge platform.
  image: https://www.everbridge.com/wp-content/uploads/2021/01/everbridge-logo.svg
  humanURL: https://developers.everbridge.net/home
  baseURL: https://api.everbridge.net/rest
  tags:
  - Asset Management
  - Assets
  - Critical Events
  properties:
  - type: Documentation
    url: https://developers.everbridge.net/home
  - type: Reference
    url: https://api.everbridge.net/
- name: Everbridge Asset Query API
  description: The Everbridge Asset Query API provides endpoints for streaming, listing, searching, paginating, and aggregating asset data. It enables organizations to query and retrieve asset information for reporting and analysis purposes.
  image: https://www.everbridge.com/wp-content/uploads/2021/01/everbridge-logo.svg
  humanURL: https://developers.everbridge.net/home
  baseURL: https://api.everbridge.net/rest
  tags:
  - Assets
  - Queries
  - Search
  properties:
  - type: Documentation
    url: https://developers.everbridge.net/home
  - type: Reference
    url: https://api.everbridge.net/
- name: Everbridge CEM Alerts API
  description: The Everbridge CEM Alerts API provides GraphQL-based endpoints for querying public alerts and streaming alert data from the Critical Event Management platform. It enables organizations to programmatically access risk event and alert information for situational awareness and response automation.
  image: https://www.everbridge.com/wp-content/uploads/2021/01/everbridge-logo.svg
  humanURL: https://developers.everbridge.net/home
  baseURL: https://api.everbridge.net
  tags:
  - Alerts
  - Critical Events
  - GraphQL
  - Risk Intelligence
  properties:
  - type: Documentation
    url: https://developers.everbridge.net/home
  - type: Reference
    url: https://api.everbridge.net/
- name: Everbridge SnapComms API
  description: The Everbridge SnapComms API enables targeted internal communications broadcasting through the Everbridge Engage platform. It supports authentication, group and attribute targeting, content templates, user management, and reporting for delivering desktop alerts, tickers, and other employee communications.
  image: https://www.everbridge.com/wp-content/uploads/2021/01/everbridge-logo.svg
  humanURL: https://developers.everbridge.net/home
  baseURL: https://api.snapcomms.com
  tags:
  - Desktop Alerts
  - Employee Communications
  - Internal Communications
  properties:
  - type: Documentation
    url: https://developers.everbridge.net/home
  - type: Reference
    url: https://api.everbridge.net/
  - type: Getting Started
    url: https://support.snapcomms.com/hc/en-us/articles/19361020051867-Integration-Through-API-Overview
- name: Everbridge Digital Apps API
  description: The Everbridge Digital Apps API provides integration capabilities for mobile, desktop, and web applications from the perspective of an Everbridge contact. It supports receiving and responding to notifications, device registration for push notifications, contact management, incident access, scheduling, and single sign-on for third-party applications.
  image: https://www.everbridge.com/wp-content/uploads/2021/01/everbridge-logo.svg
  humanURL: https://developers.everbridge.net/home/docs/overview
  baseURL: https://api.everbridge.net
  tags:
  - Contacts
  - Digital Apps
  - Mobile
  - Push Notifications
  properties:
  - type: Documentation
    url: https://developers.everbridge.net/home/docs/overview
  - type: Reference
    url: https://api.everbridge.net/
  - type: Getting Started
    url: https://developers.everbridge.net/home/docs/notifications
- name: Everbridge Communications API
  description: The Everbridge Communications API provides endpoints for managing communication templates, categories, reservations, contact builders, message builders, plans, schedules, and variables. It enables organizations to programmatically create and manage multi-channel communications within the Everbridge platform.
  image: https://www.everbridge.com/wp-content/uploads/2021/01/everbridge-logo.svg
  humanURL: https://developers.everbridge.net/home
  baseURL: https://api.everbridge.net
  tags:
  - Communications
  - Messaging
  - Templates
  properties:
  - type: Documentation
    url: https://developers.everbridge.net/home
  - type: Reference
    url: https://api.everbridge.net/
- name: Everbridge iPaaS API
  description: The Everbridge iPaaS (Integration Platform as a Service) API enables IT organizations to build integrations with monitoring and service management tools such as APM, NPM, ITOM, SIEM, DevOps, and ITSM systems. It provides a no-code to low-code approach for automatically mapping technology integrations to existing workflows and triggering Everbridge IT Alerting notifications.
  image: https://www.everbridge.com/wp-content/uploads/2021/01/everbridge-logo.svg
  humanURL: https://www.everbridge.com/products/it-alerting/integrations/ipaas-self-service-integration-guide/
  baseURL: https://ipaas-ingestion.everbridge.net
  tags:
  - Integration
  - iPaaS
  - IT Alerting
  - ITSM
  properties:
  - type: Documentation
    url: https://www.everbridge.com/products/it-alerting/integrations/ipaas-self-service-integration-guide/
  - type: Reference
    url: https://developers.everbridge.net/home
- name: Everbridge Safety Devices API
  description: The Everbridge Safety Devices API provides event management capabilities for safety devices integrated with the Everbridge platform. It uses OAuth 2.0 client credential grant type authentication and enables organizations to manage safety device events programmatically.
  image: https://www.everbridge.com/wp-content/uploads/2021/01/everbridge-logo.svg
  humanURL: https://developers.everbridge.net/home
  baseURL: https://api.everbridge.net
  tags:
  - Devices
  - IoT
  - Safety
  properties:
  - type: Documentation
    url: https://developers.everbridge.net/home
  - type: Reference
    url: https://api.everbridge.net/
name: Everbridge
tags:
- Critical Event Management
- Emergency Management
- Incident Management
- IT Alerting
- Mass Notification
type: Contract
image: https://www.everbridge.com/wp-content/uploads/2021/01/everbridge-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Everbridge is a global software company that provides enterprise software applications that automate and accelerate organizations' operational response to critical events in order to keep people safe and businesses running.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


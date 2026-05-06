---
aid: hp
name: HP
description: HP Inc. is a global technology company that provides personal computing devices, printers, 3D printing solutions, hyperscale computing solutions, and related supplies, services, and software.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Computer Hardware
  - Device Management
  - Printing
  - Technology
created: '2026-03-21'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/hp/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: hp:hp-workforce-solutions-analytics-api
    name: HP Workforce Solutions Analytics API
    description: The HP Workforce Solutions Analytics API (formerly TechPulse Analytics API) provides insightful analytics on planning, cost optimization, and service management capabilities for devices enrolled in HP Proactive Insights. It supports OAuth2 authentication.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.hp.com/hp-proactive-insights/api/hp-workforce-solutions-analytics-api
    baseURL: https://daas.api.hp.com
    tags:
      - Analytics
      - Device Management
      - TechPulse
      - Workforce
    properties:
      - type: Documentation
        url: https://developers.hp.com/hp-proactive-insights/api/hp-workforce-solutions-analytics-api
      - type: OpenAPI
        url: openapi/hp-workforce-solutions-analytics-api-openapi.yml
  - aid: hp:hp-printos-device-api
    name: HP PrintOS Device API
    description: The HP PrintOS Device API enables device manufacturers and print shop IT developers to attach their devices to the PrintOS Cloud Platform. Once provisioned, devices can make secure REST calls to interact with the platform APIs to send device status and perform operations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developers.hp.com/printos-hp-indigo-sdks-and-apis/device-api
    baseURL: https://printos.api.hp.com
    tags:
      - Cloud
      - Devices
      - Printing
      - PrintOS
    properties:
      - type: Documentation
        url: https://developers.hp.com/printos-hp-indigo-sdks-and-apis/device-api
      - type: OpenAPI
        url: openapi/hp-printos-device-api-openapi.yml
common:
  - type: Website
    name: HP Website
    url: https://www.hp.com/
  - type: DeveloperPortal
    name: HP Developer Portal
    url: https://developers.hp.com/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---

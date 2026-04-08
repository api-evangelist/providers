---
aid: cisco-voice-portal
url: https://raw.githubusercontent.com/api-evangelist/cisco-voice-portal/refs/heads/main/apis.yml
apis:
- name: Cisco Voice Portal Call Control API
  description: Provides programmatic access to call control functions on the CVP Call Server including active call management, call routing, transfers, SIP session monitoring, and health status of the call processing component.
  image: https://www.cisco.com/c/en/us/products/customer-collaboration/voice-portal/index.html
  humanURL: https://developer.cisco.com/docs/voice-portal/
  baseURL: https://cvp-callserver.example.com:8000/cvp/rest
  tags:
  - Call Control
  - Routing
  - Session Management
  - SIP
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/support/customer-collaboration/voice-portal/products-programming-reference-guides-list.html
  - type: OpenAPI
    url: openapi/cisco-voice-portal-call-control-openapi.yml
- name: Cisco Voice Portal Reporting API
  description: Access to call detail records (CDRs), real-time call statistics, historical reporting data, and report template execution through the CVP Reporting Server.
  image: https://www.cisco.com/c/en/us/products/customer-collaboration/voice-portal/index.html
  humanURL: https://developer.cisco.com/docs/voice-portal/
  baseURL: https://cvp-reporting.example.com:8111/cvp-reporting/rest
  tags:
  - Analytics
  - CDR
  - Reporting
  - Statistics
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/support/customer-collaboration/voice-portal/products-programming-reference-guides-list.html
  - type: OpenAPI
    url: openapi/cisco-voice-portal-reporting-openapi.yml
- name: Cisco Voice Portal Administration API
  description: The CVP OAMP (Operations, Administration, Maintenance, and Provisioning) REST API for managing devices, applications, dialed number patterns, SIP server groups, system configuration, user management, and deployment operations.
  image: https://www.cisco.com/c/en/us/products/customer-collaboration/voice-portal/index.html
  humanURL: https://developer.cisco.com/docs/voice-portal/
  baseURL: https://cvp-oamp.example.com:9443/oamp/rest
  tags:
  - Administration
  - Configuration
  - Management
  - OAMP
  - Provisioning
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/support/customer-collaboration/voice-portal/products-programming-reference-guides-list.html
  - type: OpenAPI
    url: openapi/cisco-voice-portal-administration-openapi.yml
- name: Cisco Voice Portal VXML Services API
  description: Management and monitoring of the CVP VXML Server including application deployment, activation, configuration, session monitoring, micro-application management, media file management, and grammar management.
  image: https://www.cisco.com/c/en/us/products/customer-collaboration/voice-portal/index.html
  humanURL: https://developer.cisco.com/docs/voice-portal/
  baseURL: https://cvp-vxmlserver.example.com:7443/CVP/rest
  tags:
  - Call Studio
  - IVR
  - Micro-Applications
  - Voice Applications
  - VXML
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/support/customer-collaboration/voice-portal/products-programming-reference-guides-list.html
  - type: OpenAPI
    url: openapi/cisco-voice-portal-vxml-services-openapi.yml
- name: Cisco Voice Portal Call Events API
  description: Event-driven interface for consuming real-time CVP call lifecycle events, system alerts, device status changes, and operational notifications via JMS messaging and syslog.
  image: https://www.cisco.com/c/en/us/products/customer-collaboration/voice-portal/index.html
  humanURL: https://developer.cisco.com/docs/voice-portal/
  baseURL: tcp://cvp-callserver.example.com:61616
  tags:
  - Call Lifecycle
  - Events
  - JMS
  - Monitoring
  - Notifications
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/support/customer-collaboration/voice-portal/products-programming-reference-guides-list.html
  - type: AsyncAPI
    url: asyncapi/cisco-voice-portal-call-events-asyncapi.yml
name: Cisco Voice Portal
tags:
- Contact Center
- IVR
- Telephony
- Voice
- VXML
type: Contract
image: https://www.cisco.com/c/en/us/products/customer-collaboration/unified-contact-center-enterprise/index.html
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Cisco Voice Portal (CVP) is an enterprise-class Voice XML (VXML) browser and call control platform that enables self-service applications for voice, video, and multimodal interactions.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


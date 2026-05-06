---
aid: qradar
name: IBM QRadar Security Intelligence Platform
description: IBM QRadar is a security information and event management (SIEM) platform that provides real-time monitoring, threat detection, and security analytics capabilities through comprehensive REST APIs.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/qradar/refs/heads/main/apis.yml
tags:
  - Analytics
  - Log Management
  - Security
  - SIEM
  - Threat Detection
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: qradar:qradar-rest-api
    name: QRadar REST API
    description: Core REST API for managing QRadar SIEM functionality including offenses, assets, rules, and searches.
    humanURL: https://www.ibm.com/docs/en/qradar-common
    tags:
      - Analytics
      - Log Management
      - Security
      - SIEM
      - Threat Detection
    properties:
      - type: Documentation
        url: https://www.ibm.com/docs/en/qsip/7.5?topic=api-restful-overview
      - type: Authentication
        url: https://www.ibm.com/docs/en/qradar-common?topic=api-authentication-methods
  - aid: qradar:qradar-gui-app-framework-api
    name: QRadar GUI App Framework API
    description: API for developing and managing QRadar apps and extensions.
    humanURL: https://www.ibm.com/docs/en/qradar-common?topic=framework-qradar-app-overview
    tags:
      - Apps
      - Development
      - Extensions
    properties:
      - type: Documentation
        url: https://www.ibm.com/docs/en/qradar-common?topic=framework-qradar-app-overview
common:
  - type: Documentation
    url: https://www.ibm.com/docs/en/qradar-common
  - type: Authentication
    url: https://www.ibm.com/docs/en/qradar-common?topic=api-authentication-methods
  - type: Support
    url: https://www.ibm.com/mysupport
  - type: Status
    url: https://www.ibm.com/cloud/status
  - type: TermsOfService
    url: https://www.ibm.com/legal
  - type: PrivacyPolicy
    url: https://www.ibm.com/privacy
  - type: Community
    url: https://community.ibm.com/community/user/security/communities/community-home?CommunityKey=d0b01247-b4d8-4466-8605-dc5c7d30c58f
  - type: Website
    url: https://www.ibm.com/security/qradar
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

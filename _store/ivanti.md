---
aid: ivanti
name: Ivanti
description: Ivanti is an IT asset management and security platform providing unified endpoint management, patch management, and IT service management. The Ivanti Neurons product family exposes REST APIs across People & Devices, MDM, ITSM, and Zero-Trust Access, alongside Endpoint Manager APIs for patch and software distribution.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Endpoint Management
  - IT Asset Management
  - IT Service Management
  - Patch Management
  - Mobile Device Management
  - Zero Trust
url: https://raw.githubusercontent.com/api-evangelist/ivanti/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ivanti:neurons-people-devices
    name: Ivanti Neurons for People and Devices
    description: REST APIs for the Ivanti Neurons platform covering inventory, patch management, and bots.
    humanURL: https://help.ivanti.com/ht/help/en_US/CLOUD/api/Shared-Content/welcome.htm
    tags:
      - Inventory
      - Patch Management
      - Bots
    properties:
      - type: Documentation
        url: https://help.ivanti.com/ht/help/en_US/CLOUD/api/Shared-Content/welcome.htm
  - aid: ivanti:neurons-mdm
    name: Ivanti Neurons for MDM
    description: REST API for Ivanti Neurons for MDM, providing programmatic access to mobile device management capabilities.
    humanURL: https://help.ivanti.com/mi/help/en_us/CLD/8x/api/LandingPage.htm
    tags:
      - Mobile Device Management
    properties:
      - type: Documentation
        url: https://help.ivanti.com/mi/help/en_us/CLD/8x/api/LandingPage.htm
  - aid: ivanti:neurons-itsm
    name: Ivanti Neurons for ITSM
    description: REST API for Ivanti Neurons for ITSM, exposing IT service management data and operations.
    humanURL: https://help.ivanti.com/ht/help/en_US/ISM/2022/admin/Content/Configure/API/RestAPI-Introduction.htm
    tags:
      - IT Service Management
    properties:
      - type: Documentation
        url: https://help.ivanti.com/ht/help/en_US/ISM/2022/admin/Content/Configure/API/RestAPI-Introduction.htm
  - aid: ivanti:neurons-zta
    name: Ivanti Neurons for Zero-Trust Access
    description: REST API for Ivanti Neurons for Zero-Trust Access, providing programmatic configuration of zero-trust policies.
    humanURL: https://help.ivanti.com/ps/help/en_US/nSA/22.x/nsa-zta/api/landingpage.htm
    tags:
      - Zero Trust
      - Network Access
    properties:
      - type: Documentation
        url: https://help.ivanti.com/ps/help/en_US/nSA/22.x/nsa-zta/api/landingpage.htm
  - aid: ivanti:endpoint-manager
    name: Ivanti Endpoint Manager
    description: Patch and software distribution APIs for Ivanti Endpoint Manager (EPM).
    humanURL: https://forums.ivanti.com/s/article/How-to-connect-to-EPM-APIs
    tags:
      - Endpoint Management
      - Patch Management
      - Software Distribution
    properties:
      - type: Documentation
        url: https://forums.ivanti.com/s/article/How-to-connect-to-EPM-APIs
common:
  - type: Website
    url: https://www.ivanti.com
  - type: API Support
    url: https://www.ivanti.com/support/api
  - type: Resources
    url: https://www.ivanti.com/resources
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

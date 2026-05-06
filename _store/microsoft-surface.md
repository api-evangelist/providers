---
aid: microsoft-surface
name: Microsoft Surface
description: Microsoft Surface is a line of touchscreen-based personal computers and accessories designed and developed by Microsoft. Surface provides enterprise management APIs through UEFI configuration and Intune integration for managing Surface devices at scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Device Management
  - Hardware
  - Microsoft
  - Surface
url: https://raw.githubusercontent.com/api-evangelist/microsoft-surface/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-surface:management-api
    name: Surface Management API
    tags:
      - Device Management
      - Firmware
      - Surface
      - UEFI
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/surface/surface-enterprise-management-mode
    properties:
      - url: https://learn.microsoft.com/en-us/surface/surface-enterprise-management-mode
        type: Documentation
    description: The Surface Management API provides enterprise management capabilities for Surface devices through UEFI configuration, firmware updates, and Intune integration. IT administrators can configure device settings, manage security features, deploy firmware updates, and control hardware components programmatically.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Website
    url: https://www.microsoft.com/en-us/surface
  - type: Documentation
    url: https://learn.microsoft.com/en-us/surface/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/surface
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

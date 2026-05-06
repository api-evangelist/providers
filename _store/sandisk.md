---
aid: sandisk
name: SanDisk
description: SanDisk, a Western Digital brand, is a leading manufacturer of flash memory products including memory cards, USB flash drives, solid-state drives, and embedded storage solutions. SanDisk provides developer SDKs for integrating iXpand storage devices into iOS applications, enabling third-party app developers to access and manage iXpand Flash Drive storage through the Lightning interface. Western Digital also maintains the My Cloud Home platform with RESTful APIs for building off-device cloud storage applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Flash Memory
  - Storage
  - SDK
  - Mobile
  - Consumer Electronics
created: '2026-05-02'
modified: '2026-05-02'
x-profiled: 2026-05
url: https://raw.githubusercontent.com/api-evangelist/sandisk/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sandisk:sandisk-ixpand-sdk
    name: SanDisk iXpand SDK
    description: The SanDisk iXpand SDK enables third-party iOS application developers to access and manage iXpand Flash Drive storage through the Lightning interface. It provides File System APIs with a familiar filesystem interface for managing storage operations, and System APIs that provide access to administration functionality. The SDK is available as an iOS framework file and requires a free Western Digital Developer Portal account to download.
    humanURL: https://developer.westerndigital.com/develop/sandisk/ixpand-sdk-home-main.html
    tags:
      - iOS
      - SDK
      - Flash Drive
      - Storage
      - Mobile
    properties:
      - type: Documentation
        url: https://developer.westerndigital.com/develop/sandisk/ixpand-sdk-home-main.html
      - type: Getting Started
        url: https://developer.westerndigital.com/develop/sandisk/get-the-sdk.html
      - type: Developer Portal
        url: https://developer.sandisk.com
  - aid: sandisk:sandisk-hqme-sdk
    name: SanDisk HQME SDK
    description: The SanDisk HQME (Home Quality Media Experience) SDK is based on the IEEE P2200/D2 draft standard for content storage and retrieval. It provides additional APIs beyond the standard to support advanced media management functionality on Android devices. This SDK enables developers to build applications that leverage SanDisk storage for media caching and delivery.
    humanURL: https://github.com/HQME-developer/SanDisk-HQME-SDK
    tags:
      - Android
      - SDK
      - Media
      - Storage
      - IEEE Standard
    properties:
      - type: GitHubRepository
        url: https://github.com/HQME-developer/SanDisk-HQME-SDK
      - type: Documentation
        url: https://github.com/HQME-developer/SanDisk-HQME-SDK
common:
  - type: Website
    url: https://www.sandisk.com
  - type: Developer Portal
    url: https://developer.westerndigital.com
  - type: GitHub Organization
    url: https://github.com/SanDisk-Open-Source
  - type: GitHub Organization
    url: https://github.com/westerndigitalcorporation
  - type: Support
    url: https://support-en.sandisk.com
  - type: Vocabulary
    url: vocabulary/sandisk-vocabulary.yml
  - type: JSONLD
    url: json-ld/sandisk-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

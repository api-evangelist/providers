---
aid: whatfix
name: Whatfix
description: Whatfix is a digital adoption platform providing in-app contextual guidance, SaaS management, workflow automation, and product analytics to help organizations accelerate software adoption, improve employee onboarding, and optimize digital transformation. Its platform combines guided walkthroughs, self-help content, AI-powered authoring agents, task lists, surveys, and usage analytics for web, desktop, mobile, and VDI environments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Digital Adoption
  - SaaS Management
  - User Onboarding
  - In-App Guidance
  - Analytics
  - Change Management
url: https://raw.githubusercontent.com/api-evangelist/whatfix/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: whatfix:whatfix-api
    name: Whatfix API
    description: The Whatfix REST API enables programmatic access to end-user management, content management, flow analytics, segmentation, and report downloads. The API is stateless, uses JSON output, and authenticates via the x-whatfix-integration-key header with your account API token.
    humanURL: https://developer.whatfix.com
    baseURL: https://whatfix.com/api/v1
    tags:
      - Digital Adoption
      - Analytics
      - Content Management
      - User Segmentation
    properties:
      - type: Documentation
        url: https://developer.whatfix.com
      - type: Developer Guide
        url: https://support.whatfix.com/docs/developer-guide
      - type: Authentication
        url: https://support.whatfix.com/docs/generatingtheapitoken
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/whatfix/refs/heads/main/openapi/whatfix-openapi.yml
      - type: Analytics API
        url: https://support.whatfix.com/docs/downloading-report-analytics-data-using-api
  - aid: whatfix:whatfix-android-sdk
    name: Whatfix Android SDK
    description: The Whatfix Android SDK provides DAP (Digital Adoption Platform) capabilities for Android mobile applications, enabling in-app guidance, onboarding flows, and user engagement analytics on native Android apps.
    humanURL: https://github.com/whatfix/whatfix-android
    tags:
      - Android
      - Mobile SDK
      - DAP
    properties:
      - type: Source Code
        url: https://github.com/whatfix/whatfix-android
      - type: SDK
        url: https://github.com/whatfix/whatfix-android
  - aid: whatfix:whatfix-ios-sdk
    name: Whatfix iOS SDK
    description: The Whatfix iOS SDK provides DAP capabilities for native iOS applications, enabling in-app guidance, walkthroughs, and analytics on iPhone and iPad apps.
    humanURL: https://github.com/whatfix/Whatfix-iOS
    tags:
      - iOS
      - Mobile SDK
      - DAP
    properties:
      - type: Source Code
        url: https://github.com/whatfix/Whatfix-iOS
      - type: SDK
        url: https://github.com/whatfix/Whatfix-iOS
common:
  - type: Website
    url: https://whatfix.com
  - type: Developer Portal
    url: https://developer.whatfix.com
  - type: Documentation
    url: https://support.whatfix.com
  - type: GitHub Organization
    url: https://github.com/whatfix
  - type: Blog
    url: https://whatfix.com/blog/
  - type: Pricing
    url: https://whatfix.com/pricing/
  - type: Integrations
    url: https://whatfix.com/integrations/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/whatfix/refs/heads/main/openapi/whatfix-openapi.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/whatfix/refs/heads/main/vocabulary/whatfix-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/whatfix/refs/heads/main/json-ld/whatfix-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/whatfix/refs/heads/main/rules/whatfix-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/whatfix/refs/heads/main/capabilities/digital-adoption.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

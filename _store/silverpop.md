---
name: Silverpop
description: Silverpop (now Acoustic, formerly IBM Watson Campaign Automation) is a digital marketing automation platform offering email marketing, marketing automation, mobile messaging, and campaign management. The platform provides XML and REST APIs for list management, contact data, campaign execution, transactional messaging, and reporting.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/silverpop/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Email Marketing
  - Marketing Automation
  - Campaign Management
  - Digital Marketing
apis:
  - name: Silverpop Engage XML API
    description: The Silverpop Engage XML API (now Acoustic Campaign) provides XML-based endpoints for managing contact lists, sending email campaigns, tracking engagement, and administering marketing automation workflows. Supports OAuth 2.0 authentication with client credentials.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.goacoustic.com/acoustic-campaign/reference/overview
    baseURL: https://api-campaign-us-1.goacoustic.com
    tags:
      - Email Marketing
      - Campaign Management
      - Contact Management
      - Marketing Automation
    properties:
      - type: Documentation
        url: https://developer.goacoustic.com/acoustic-campaign/reference/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/silverpop/refs/heads/main/openapi/silverpop-openapi.yml
      - type: GitHubOrganization
        url: https://github.com/Silverpop
      - type: NodeJSSDK
        url: https://github.com/Silverpop/node-engage
      - type: Authentication
        url: https://developer.goacoustic.com/acoustic-campaign/docs/authentication
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/silverpop/refs/heads/main/rules/silverpop-rules.yml
    contact:
      - FN: Acoustic (Silverpop) Support
        url: https://developer.goacoustic.com
common:
  - type: GitHubOrganization
    url: https://github.com/Silverpop
  - type: DeveloperPortal
    url: https://developer.goacoustic.com
  - type: Documentation
    url: https://developer.goacoustic.com/acoustic-campaign/reference/overview
  - type: Authentication
    url: https://developer.goacoustic.com/acoustic-campaign/docs/authentication
  - type: TermsOfService
    url: https://www.goacoustic.com/terms-of-use
  - type: PrivacyPolicy
    url: https://www.goacoustic.com/privacy-notice
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
    email: info@apievangelist.com
---

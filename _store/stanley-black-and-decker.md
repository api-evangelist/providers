---
aid: stanley-black-and-decker
url: https://raw.githubusercontent.com/api-evangelist/stanley-black-and-decker/refs/heads/main/apis.yml
name: Stanley Black & Decker
tags:
  - Tools
  - Hardware
  - Manufacturing
  - IoT
  - Connected Tools
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-01-01'
modified: '2026-05-02'
description: Stanley Black & Decker is a global manufacturer and marketer of hand tools, power tools, and related accessories. Through brands like DEWALT, Stanley, Craftsman, and Black+Decker, the company provides connected tool management platforms, IoT solutions, and partner integrations for jobsite productivity.
apis:
  - aid: stanley-black-and-decker:dewalt-tool-connect-api
    name: DEWALT Tool Connect API
    tags:
      - Connected Tools
      - IoT
      - Tool Management
      - Jobsite
    properties:
      - url: https://sitemanager.dewalt.com/
        type: Portal
      - url: https://www.dewalt.com/systems/tool-connect
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/stanley-black-and-decker/refs/heads/main/openapi/stanley-black-and-decker-tool-connect-api-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/stanley-black-and-decker/refs/heads/main/rules/stanley-black-and-decker-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/stanley-black-and-decker/refs/heads/main/capabilities/jobsite-tool-management.yaml
        type: NaftikoCapabilities
    description: The DEWALT Tool Connect API enables integration with DEWALT's connected tool management platform, allowing partners to access tool inventory, track assets, manage Bluetooth-connected products, and synchronize jobsite data. Used by fleet management and construction software providers.
  - aid: stanley-black-and-decker:stanley-x-iot-api
    name: Stanley X IoT API
    tags:
      - IoT
      - Smart Factory
      - Industrial
      - Manufacturing
    properties:
      - url: https://www.stanleyblackanddecker.com/
        type: Website
    description: Stanley X is the innovation arm of Stanley Black & Decker that provides IoT connectivity APIs enabling smart factory solutions, equipment management, and digital manufacturing workflows. Partners integrate via REST APIs to connect hardware systems with digital management platforms.
common:
  - url: https://www.stanleyblackanddecker.com/
    type: Website
  - url: https://www.dewalt.com/
    type: Website
  - url: https://developer.stanley.com/
    type: Portal
  - url: https://sitemanager.dewalt.com/
    type: Portal
  - url: https://www.stanleyblackanddecker.com/news-stories
    type: Blog
  - url: https://www.stanleyblackanddecker.com/privacy-notice
    type: PrivacyPolicy
  - url: https://www.stanleyblackanddecker.com/terms-use
    type: TermsOfService
  - url: https://github.com/StanleyInnovation
    type: GitHubOrg
  - url: https://x.com/SBDinnovates
    type: X
  - url: https://www.linkedin.com/company/stanley-black-and-decker
    type: LinkedIn
---

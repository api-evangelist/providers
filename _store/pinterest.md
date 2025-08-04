---
aid: pinterest
url: >-
  https://raw.githubusercontent.com/api-search/images/main/_apis/pinterest/apis.md
apis:
  - aid: pinterest:pinterest-api
    name: Pinterest API
    tags:
      - Images
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developers.pinterest.com/
    properties:
      - url: https://developers.pinterest.com/docs/api/v5/
        type: Documentation
      - url: properties/pinterest-api-openapi.yml
        type: OpenAPI
    description: This is the description of your API.
name: Pinterest
tags:
  - Images
  - Social Media
  - Videos
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://www.pinterest.com/_/_/policy/developer-guidelines
    type: Guidelines
  - url: https://www.pinterest.com/_/_/newsroom/
    type: News
  - url: https://medium.com/pinterest-engineering
    type: Blog
  - url: https://help.pinterest.com/contact
    type: Support
  - url: https://developers.pinterest.com/terms/
    type: Terms of Service
  - url: https://github.com/pinterest/api-description
    type: OpenAPI
  - url: https://github.com/pinterest
    type: GitHub Org
  - url: properties/api-description
    name: OpenAPI
    type: OpenAPI
  - url: https://www.pintereststatus.com/
    name: Sttus
    type: Status
  - url: https://developers.pinterest.com/
    name: Pinterest Developers
    type: Portal
    description: 'null'
  - url: https://developers.pinterest.com/docs/overview/welcome/
    name: Pinterest Developers
    type: Documentation
    description: 'null'
  - url: https://developers.pinterest.com/docs/changelog/changelog/
    name: Pinterest Developers
    type: ChangeLog
    description: 'null'
  - url: https://developers.pinterest.com/docs/getting-started/connect-app/
    name: Pinterest Developers
    type: GettingStarted
    description: 'null'
  - url: >-
      https://developers.pinterest.com/docs/api-features/track-conversion-events/
    name: Pinterest Developers
    type: Features
    description: 'null'
  - url: https://developers.pinterest.com/docs/developer-tools/sdk/
    name: Pinterest Developers
    type: SDKs
    description: Developer
  - url: https://developers.pinterest.com/docs/developer-tools/sandbox/
    name: Pinterest Developers
    type: Sandbox
    description: Developer
  - url: https://developers.pinterest.com/docs/developer-tools/quickstart-tools/
    name: Pinterest Developers
    type: GettingStarted
    description: Developer
  - url: https://developers.pinterest.com/docs/reference/rate-limits/
    name: Pinterest Developers
    type: RateLimits
    description: 'null'
  - url: https://developers.pinterest.com/docs/reference/error-codes/
    name: Pinterest Developers
    type: Errors
    description: 'null'
  - url: https://developers.pinterest.com/docs/reference/pagination/
    name: Pinterest Developers
    type: Pagination
    description: 'null'
  - url: https://developers.pinterest.com/docs/reference/help-and-feedback/
    name: Pinterest Developers
    type: Support
    description: 'null'
  - url: https://developers.pinterest.com/terms/
    name: Pinterest Developers | Terms
    type: TermsOfService
    description: 'null'
  - url: https://policy.pinterest.com/en/privacy-policy
    name: Privacy Policy | Pinterest Policy
    type: PrivacyPolicy
    description: 'null'
  - url: https://business.pinterest.com/pinterest-business-partners/
    name: Work with Approved Pinterest Partners | Pinterest Business
    type: Partners
    description: 'null'
  - name: Plans
    type: Plans
    url: https://example.com/plans
    data:
      - id: trial
        name: Trial
        description: The temporary access.
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Trial tier.
      - id: standard
        name: Standard
        description: The standard access.
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Standard tier.
created: 2023/11/23
modified: '2025-07-29'
position: Consuming
description: |-

  Pinterest is an American image sharing and social media service designed to
  enable saving and discovery of information like recipes, home, style,
  motivation, and inspiration on the internet using images and, on a smaller
  scale, animated GIFs and videos, in the form of pinboards.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.18'
---
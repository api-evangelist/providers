---
aid: apis-io-linter
url: https://github.com/api-search/linter-api/blob/main/apis.yml
apis:
  - aid: apis-io-linter:linter-api
    name: APIs.io Linter API
    tags:
      - Linter
    image: https://kinlane-productions2.s3.amazonaws.com/apis-io/apis-io-api-logo.jpg
    baseURL: https://linter-api.apis.io
    contact:
      - FN: APIs.io
        email: info@apis.io
    humanURL: https://developer.apis.io/documentation
    properties:
      - url: https://github.com/api-search/linter-api
        type: GitHubRepository
      - url: >-
          https://github.com/api-search/linter-api/blob/main/.github/workflows/pipeline.yml
        type: GitHubActions
      - url: https://developer.apis.io/documentation/
        type: Documentation
      - url: properties/openapi.yml
        type: OpenAPI
    description: This is the API for powering APIs.io.
name: APIs.io Linter API
tags:
  - Linter
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-io/apis-io-api-logo.jpg
access: 1st-Party
common:
  - url: https://github.com/api-search/
    type: GitHubOrganization
  - url: https://www.postman.com/api-evangelist/apis-io-api-search-linter/overview
    type: PostmanPublicWorkspace
  - url: https://developer.apis.io
    type: Portals
  - url: https://developer.apis.io/getting-started/
    type: GettingStarted
  - url: https://developer.apis.io/plans/
    type: Plans
  - url: https://developer.apis.io/linter/
    type: Linter
  - url: https://developer.apis.io/road-map/
    type: RoadMap
  - url: https://developer.apis.io/change-log/
    type: ChangeLog
  - url: https://developer.apis.io/versioning/
    type: Versioning
  - url: https://developer.apis.io/sdks/
    type: SDKs
  - url: https://developer.apis.io/blog/
    type: Blogs
  - url: https://developer.apis.io/atom.xml
    type: BlogFeeds
  - url: https://developer.apis.io/videos/
    type: Videos
  - url: https://developer.apis.io/support/
    type: Support
  - url: https://github.com/orgs/api-search/discussions
    type: Forums
  - url: >-
      https://github.com/api-search/linter-api/issues?q=is%3Aissue+is%3Aopen+label%3Asupport
    type: SupportGitHubIssues
  - url: info@apievangelist.com
    type: SupportEmail
  - url: >-
      https://github.com/api-search/linter-api/issues?q=is%3Aissue+is%3Aopen+label%3Afeedback
    type: FeedbackGitHubIssues
  - url: info@apievangelist.com
    type: FeedbackEmail
  - url: >-
      https://github.com/api-search/linter-api/issues?q=is%3Aissue+is%3Aopen+label%3Aquestion
    type: QuestionsGitHubIssues
  - url: https://github.com/api-search/policies/blob/main/policies.yml
    type: Policies
  - url: https://github.com/api-search/rules/blob/main/operational-rules.yml
    type: OperationalRules
  - url: https://github.com/api-search/rules/blob/main/api-rules.yml
    type: ApiRules
  - url: https://github.com/api-search/lifecycle/blob/main/lifecycle.yml
    type: Lifecycle
  - url: https://github.com/api-search/vocabulary/blob/main/vocabulary.yml
    type: Vocabulary
  - url: https://developer.apis.io/terms-of-service/
    type: TermsOfService
  - url: https://developer.apis.io/privacy-policy/
    type: PrivacyPolicy
  - url: https://developer.apis.io/licensing/
    type: InterfaceLicense
  - url: >-
      https://api-evangelist-tools.github.io/apis-io-linter-api-operational-validator/
    type: OperationalValidation
  - url: https://api-evangelist-tools.github.io/apis-io-linter-api-api-validator/
    type: APIValidation
created: '2024-08-20'
modified: '2024-11-26'
position: Producing
description: >-
  This is the contract for the APIs.io Linter API used to govern the APIs.io
  search linter.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-github: kinlane
specificationVersion: '0.18'

---
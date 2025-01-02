---
aid: mastercard-fdx
url: https://github.com/api-search/mastercard-developer-hub-for-fdx-apis/apis.yml
apis:
  - aid: mastercard-fdx:authorization-api
    name: Mastercard FDX Authorization API
    tags:
      - FDX
      - Authorization
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: http://api.example.com
    humanURL: http://example.com
    properties:
      - url: >-

          https://developer.mastercard.com/fdx-dev-hub/documentation/api-reference/#authorization-server
        type: Documentation
      - url: fdx-authorization-api-openapi.yaml
        type: OpenAPI
      - url: >-

          https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#fdx-mock-authorization-server
        type: MockServer
      - url: https://github.com/Mastercard/Fdx-Mock-Auth-Server
        type: GitHubRepository
    description: Dynamic Client Registration, Token, Introspection, Authorize API.
  - aid: mastercard-fdx:resource-api
    name: Mastercard FDX Resource API
    tags:
      - FDX
      - Payments
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: http://api.example.com
    humanURL: http://example.com
    properties:
      - url: >-

          https://developer.mastercard.com/fdx-dev-hub/documentation/api-reference/#resource-server
        type: Documentation
      - url: fdx-resource-api-openapi.yaml
        type: OpenAPI
      - url: >-

          https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#fdx-mock-resource-server
        type: MockServer
      - url: https://github.com/Mastercard/Fdx-Mock-Resource-Server
        type: GitHubRepository
    description: FDX Mock Resource Server API reference for developers.
name: Mastercard Developer Hub for FDX APIs
tags:
  - Banking
  - Open Banking
  - FDX
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://developer.mastercard.com/fdx-dev-hub/documentation
    type: Portal
  - url: >-

      https://developer.mastercard.com/fdx-dev-hub/documentation/sequence-diagrams/
    type: SequenceDiagrams
  - url: https://developer.mastercard.com/fdx-dev-hub/documentation/user-exp/
    type: UserJourney
  - url: >-

      https://developer.mastercard.com/fdx-dev-hub/documentation/implementation-checklist/
    type: Implementation Checklist
  - url: https://developer.mastercard.com/account/sign-up
    type: Signup
  - url: https://developer.mastercard.com/account/log-in
    type: Login
  - url: >-

      https://developer.mastercard.com/fdx-dev-hub/documentation/auth-server/#oauth-20-vs-openid-connect-oidc
    type: Authentication
  - url: >-

      https://developer.mastercard.com/fdx-dev-hub/documentation/auth-server/#dynamic-client-registration
    type: DynamicClientRegistration
  - url: >-

      https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#run-in-postman
    type: Simulator
  - url: https://openid.net/wg/fapi/
    type: FAPI
  - url: https://financialdataexchange.org/
    type: FDX
  - url: https://openid.net/specs/openid-connect-core-1_0.html
    type: OpenID
  - url: https://datatracker.ietf.org/doc/html/rfc8414
    type: OAuth20AuthorizationServerMetadata
  - url: https://datatracker.ietf.org/doc/html/rfc6749
    type: OAuth20AuthorizationFramework
  - url: https://datatracker.ietf.org/doc/html/rfc7591
    type: OAuth20DynamicClientRegistrationProtocol
  - url: https://datatracker.ietf.org/doc/html/rfc7636
    type: ProofKeyforCodeExchangebyOAuth PublicClients
  - url: https://datatracker.ietf.org/doc/html/rfc9126
    type: OAuth20PushedAuthorizationRequests
  - url: https://datatracker.ietf.org/doc/html/rfc9396
    type: OAuth20RichAuthorizationRequests
  - url: >-

      https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#run-in-postman
    type: RuninPostman
  - url: >-

      https://www.postman.com/ma-fdx-dev-hub/fdx-developer-hub/collection/p928zhg/mastercard-developer-hub-for-fdx-apis
    type: PostmanCollection
  - url: https://www.postman.com/ma-fdx-dev-hub/fdx-developer-hub/overview
    type: PostmanWorkspace
  - url: >-

      https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#instructions-for-building-a-docker-image
    type: DockerContainer
  - url: >-

      https://developer.mastercard.com/fdx-dev-hub/documentation/links-resources/
    type: Resources
  - url: >-

      https://developer.mastercard.com/fdx-dev-hub/documentation/code-and-formats/
    type: ErrorCodes
  - url: https://developer.mastercard.com/fdx-dev-hub/documentation/fdx-enums/
    type: Enumerators
  - url: >-

      https://developer.mastercard.com/fdx-dev-hub/documentation/implementation-checklist/#test-user-profiles
    type: TestUserProfiles
  - url: https://developer.mastercard.com/api-status
    type: Status
  - url: >-

      https://developer.mastercard.com/fdx-dev-hub/documentation/release-history/
    type: ReleaseHistory
  - url: https://developer.mastercard.com/fdx-dev-hub/documentation/support/#faq
    type: FAQ
  - url: https://developer.mastercard.com/support
    type: Support
  - url: https://forum.developer.mastercard.com/s/
    type: Forum
  - url: https://developer.mastercard.com/blog
    type: Blog
  - url: https://developer.mastercard.com/terms-of-use
    type: TermsOfService
  - url: https://www.mastercard.us/en-us/about-mastercard/what-we-do/privacy.html
    type: PrivacyPolicy
  - url: >-

      https://www.consumerfinance.gov/about-us/newsroom/cfpb-proposes-rule-to-jumpstart-competition-and-accelerate-shift-to-open-banking/
    type: Regulations
created: '2024-10-25T00:00:00.000Z'
modified: '2025-01-02'
position: Consuming
description: |-
  The Financial Data Exchange (FDX) is a nonprofit industry standards body that
  created the FDX API, a technical standard for user-permissioned financial data
  sharing. The FDX API standard, like other data sharing methods used in open
  banking, gives consumers more control over who can access their financial
  data. The open banking industry is founded on the principles of
  interoperability, which are being advanced by forthcoming rulemaking from the
  The Consumer Financial Protection Bureau (CFPB).
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X-twitter: apievangelist
specificationVersion: '0.18'

---
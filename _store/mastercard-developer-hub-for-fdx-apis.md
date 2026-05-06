---
aid: mastercard-fdx
name: Mastercard Developer Hub for FDX APIs
type: Index
description: The Financial Data Exchange (FDX) is a nonprofit industry standards body that created the FDX API, a technical standard for user-permissioned financial data sharing. The FDX API standard, like other data sharing methods used in open banking, gives consumers more control over who can access their financial data. The open banking industry is founded on the principles of interoperability, which are being advanced by forthcoming rulemaking from the The Consumer Financial Protection Bureau (CFPB).
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - FDX
  - Open Banking
created: 2024-10-25T00:00:00.000Z
modified: '2026-04-28'
url: https://github.com/api-search/mastercard-developer-hub-for-fdx-apis/apis.yml
specificationVersion: '0.18'
apis:
  - aid: mastercard-fdx:authorization-api
    name: Mastercard FDX Authorization API
    description: Dynamic Client Registration, Token, Introspection, Authorize API.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: http://example.com
    baseURL: http://api.example.com
    tags:
      - Authorization
      - FDX
    properties:
      - type: Documentation
        url: https://developer.mastercard.com/fdx-dev-hub/documentation/api-reference/#authorization-server
      - type: OpenAPI
        url: openapi/fdx-authorization-api-openapi.yaml
      - type: MockServer
        url: https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#fdx-mock-authorization-server
      - type: GitHubRepository
        url: https://github.com/Mastercard/Fdx-Mock-Auth-Server
  - aid: mastercard-fdx:resource-api
    name: Mastercard FDX Resource API
    description: FDX Mock Resource Server API reference for developers.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: http://example.com
    baseURL: http://api.example.com
    tags:
      - FDX
      - Payments
    properties:
      - type: Documentation
        url: https://developer.mastercard.com/fdx-dev-hub/documentation/api-reference/#resource-server
      - type: OpenAPI
        url: openapi/fdx-resource-api-openapi.yaml
      - type: MockServer
        url: https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#fdx-mock-resource-server
      - type: GitHubRepository
        url: https://github.com/Mastercard/Fdx-Mock-Resource-Server
common:
  - type: Portal
    url: https://developer.mastercard.com/fdx-dev-hub/documentation
  - type: SequenceDiagrams
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/sequence-diagrams/
  - type: UserJourney
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/user-exp/
  - type: Implementation Checklist
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/implementation-checklist/
  - type: Signup
    url: https://developer.mastercard.com/account/sign-up
  - type: Login
    url: https://developer.mastercard.com/account/log-in
  - type: Authentication
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/auth-server/#oauth-20-vs-openid-connect-oidc
  - type: DynamicClientRegistration
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/auth-server/#dynamic-client-registration
  - type: Simulator
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#run-in-postman
  - type: FAPI
    url: https://openid.net/wg/fapi/
  - type: FDX
    url: https://financialdataexchange.org/
  - type: OpenID
    url: https://openid.net/specs/openid-connect-core-1_0.html
  - type: OAuth20AuthorizationServerMetadata
    url: https://datatracker.ietf.org/doc/html/rfc8414
  - type: OAuth20AuthorizationFramework
    url: https://datatracker.ietf.org/doc/html/rfc6749
  - type: OAuth20DynamicClientRegistrationProtocol
    url: https://datatracker.ietf.org/doc/html/rfc7591
  - type: ProofKeyforCodeExchangebyOAuth PublicClients
    url: https://datatracker.ietf.org/doc/html/rfc7636
  - type: OAuth20PushedAuthorizationRequests
    url: https://datatracker.ietf.org/doc/html/rfc9126
  - type: OAuth20RichAuthorizationRequests
    url: https://datatracker.ietf.org/doc/html/rfc9396
  - type: RuninPostman
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#run-in-postman
  - type: PostmanCollection
    url: https://www.postman.com/ma-fdx-dev-hub/fdx-developer-hub/collection/p928zhg/mastercard-developer-hub-for-fdx-apis
  - type: PostmanWorkspace
    url: https://www.postman.com/ma-fdx-dev-hub/fdx-developer-hub/overview
  - type: DockerContainer
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#instructions-for-building-a-docker-image
  - type: Resources
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/links-resources/
  - type: ErrorCodes
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/code-and-formats/
  - type: Enumerators
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/fdx-enums/
  - type: TestUserProfiles
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/implementation-checklist/#test-user-profiles
  - type: Status
    url: https://developer.mastercard.com/api-status
  - type: ReleaseHistory
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/release-history/
  - type: FAQ
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/support/#faq
  - type: Support
    url: https://developer.mastercard.com/support
  - type: Forum
    url: https://forum.developer.mastercard.com/s/
  - type: Blog
    url: https://developer.mastercard.com/blog
  - type: TermsOfService
    url: https://developer.mastercard.com/terms-of-use
  - type: PrivacyPolicy
    url: https://www.mastercard.us/en-us/about-mastercard/what-we-do/privacy.html
  - type: Regulations
    url: https://www.consumerfinance.gov/about-us/newsroom/cfpb-proposes-rule-to-jumpstart-competition-and-accelerate-shift-to-open-banking/
maintainers:
  - FN: Kin Lane
    X-twitter: apievangelist
    email: info@apievangelist.com
---

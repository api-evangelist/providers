---
aid: paragon
url: >-
  https://raw.githubusercontent.com/api-evangelist/paragon/refs/heads/main/apis.yml
apis:
  - aid: paragon:proxy-api
    name: Proxy API
    tags: []
    humanURL: https://docs.useparagon.com/apis/making-api-requests
    properties:
      - url: https://docs.useparagon.com/apis/making-api-requests
        type: Documentation
    description: >-
      Once your users have connected their third-party app accounts in the
      Connect Portal, you can access their app account via the Proxy API. The
      Proxy API allows you to directly access any of the third-party provider’s
      API methods. With the SDK, you can use paragon.request to send an API
      request to a third-party app on behalf of one of your Connected Users.
      Along with Workflows, the Proxy API is one of two primary ways to build
      integrations with Paragon.
  - aid: paragon:users-api
    name: Users API
    tags: []
    humanURL: https://docs.useparagon.com/apis/users
    properties:
      - url: https://docs.useparagon.com/apis/users
        type: Documentation
    description: >-
      The Users API allows you to query and modify the state of your Connected
      Users and their integrations. The API includes REST endpoints (and
      matching SDK functions) for identifying what integrations your user has
      enabled, disconnecting integrations, and disabling workflows. The API also
      allows your application to associate metadata with a Connected User.
  - aid: paragon:task-history-api
    name: Task History API
    tags: []
    humanURL: https://docs.useparagon.com/apis/task-history
    properties:
      - url: https://docs.useparagon.com/apis/task-history
        type: Documentation
    description: >-
      The Task History API allows you to query your users’ usage of integration
      workflows and access data from historical workflow executions. The Task
      History API can be used to analyze integration usage or pull information
      about historical workflow executions into your application.
name: Paragon
tags:
  - Integrations
  - Embedded SaaS Integration
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://github.com/useparagon
    name: GitHub Organization
    type: GitHubOrganization
  - url: https://www.useparagon.com/integrations
    name: Paragon | Embedded Integration Platform for Developers
    type: Integrations
    description: 'null'
  - url: https://docs.useparagon.com/overview
    name: Paragon Documentation
    type: Documentation
    description: 'null'
  - url: https://www.useparagon.com/blog
    name: Paragon Embedded iPaaS | Blog
    type: Blog
    description: 'null'
  - url: https://status.useparagon.com/
    name: Paragon Status
    type: Status
    description: 'null'
  - url: https://www.useparagon.com/use-case/library
    name: Powered by Paragon | Embedded iPaaS
    type: UseCases
    description: 'null'
  - url: https://docs.useparagon.com/getting-started/installing-the-connect-sdk
    name: Installing the SDK - Paragon Documentation
    type: SDKs
    description: 'null'
  - url: https://docs.useparagon.com/connect-portal/overview
    name: Overview - Paragon Documentation
    type: Authentication
    description: 'null'
  - url: https://docs.useparagon.com/resources/custom-webhooks
    name: Custom Webhooks - Paragon Documentation
    type: Webhooks
    description: 'null'
  - url: https://docs.useparagon.com/managing-account/role-based-access-control
    name: Role Based Access Control - Paragon Documentation
    type: RBAC
    description: 'null'
  - url: https://docs.useparagon.com/billing/concurrency-limits
    name: Concurrency SLA - Paragon Documentation
    type: ServiceLevelAgreement
    description: 'null'
  - url: https://docs.useparagon.com/security/security
    name: Security - Paragon Documentation
    type: Security
    description: 'null'
  - url: https://security.useparagon.com/
    name: Trust Center - Paragon
    type: Trust
    description: 'null'
  - url: https://docs.useparagon.com/security/gdpr
    name: GDPR - Paragon Documentation
    type: GDPR
    description: 'null'
  - url: https://docs.useparagon.com/support/contacting-support
    name: Contacting Support - Paragon Documentation
    type: Support
    description: 'null'
  - url: https://docs.useparagon.com/support/contacting-support
    name: Contacting Support - Paragon Documentation
    type: Support
    description: 'null'
  - url: https://docs.useparagon.com/workflows/overview
    name: Overview - Paragon Documentation
    type: Workflows
    description: 'null'
  - url: https://docs.useparagon.com/resources/integrations
    name: Overview - Paragon Documentation
    type: Integrations
    description: 'null'
  - url: https://docs.useparagon.com/changelog/product-updates
    name: Product Updates - Paragon Documentation
    type: ChangeLog
    description: 'null'
  - url: https://dashboard.useparagon.com/signup
    name: Paragon
    type: SignUp
    description: 'null'
  - url: https://dashboard.useparagon.com/login
    name: Paragon
    type: Login
    description: 'null'
  - url: https://www.useparagon.com/terms-of-service
    name: Paragon Embedded iPaaS | Terms of Service
    type: TermsOfService
    description: 'null'
  - url: https://www.useparagon.com/customers
    name: Paragon Embedded iPaaS | Customer Stories
    type: Customers
    description: 'null'
  - url: https://www.useparagon.com/pricing
    name: Paragon | Embedded Integration Platform for Developers
    type: Pricing
    description: 'null'
created: '2025-06-05'
modified: '2025-06-05'
position: Consuming
description: >-
  Paragon enables companies to build products that integrate with the SaaS
  ecosystem. With Paragon, software companies can integrate with hundreds of
  different SaaS apps in minutes while providing their customers with a
  seamless, unified integration experience.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---
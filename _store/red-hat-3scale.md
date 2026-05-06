---
aid: red-hat-3scale
name: Red Hat 3scale
description: Red Hat 3scale API Management is an enterprise-grade API management platform that enables organizations to share, secure, distribute, control, and monetize APIs across internal and external teams. It provides a developer portal, analytics, access control, policy enforcement, and billing for REST, SOAP, GraphQL, and other API types. 3scale runs on-premises via OpenShift or as a hosted managed service, and is fully Kubernetes-native.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - API Management
  - Developer Portal
  - Enterprise
  - Red Hat
url: https://raw.githubusercontent.com/api-evangelist/red-hat-3scale/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: red-hat-3scale:service-management-api
    name: Red Hat 3scale Service Management API
    description: The 3scale Service Management API allows API providers to control and manage access to their APIs, track usage, and enforce traffic policies. It is used by the API gateway (APIcast) to authorize and report API calls in real time. The API supports both API key and OAuth 2.0 based authorization flows. Calls are made from the API gateway on behalf of the API consumer application.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management
    baseURL: https://su1.3scale.net
    tags:
      - Access Control
      - API Management
      - Authorization
      - Traffic Management
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/api_authentication/index
      - type: Reference
        url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/index
      - type: OpenAPI
        url: openapi/red-hat-3scale-service-management-openapi.yml
  - aid: red-hat-3scale:account-management-api
    name: Red Hat 3scale Account Management API
    description: The 3scale Account Management API provides programmatic access to manage developer accounts, applications, application plans, keys, and API subscriptions within the 3scale platform. It enables automation of developer onboarding, subscription management, and application lifecycle operations from external systems or scripts. The API is accessible on the admin domain and requires admin API credentials.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/index
    baseURL: https://{your-domain}-admin.3scale.net
    tags:
      - Account Management
      - API Management
      - Applications
      - Developer Portal
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/index
      - type: Reference
        url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/accounts
      - type: OpenAPI
        url: openapi/red-hat-3scale-account-management-openapi.yml
  - aid: red-hat-3scale:analytics-api
    name: Red Hat 3scale Analytics API
    description: The 3scale Analytics API provides access to API usage data, traffic metrics, hit counts, and reporting for APIs managed through the 3scale platform. It enables operators to retrieve usage statistics, query by time period and granularity, and integrate analytics data into external dashboards or monitoring systems.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/analytics
    baseURL: https://{your-domain}-admin.3scale.net
    tags:
      - Analytics
      - API Management
      - Metrics
      - Reporting
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/analytics
      - type: OpenAPI
        url: openapi/red-hat-3scale-analytics-openapi.yml
  - aid: red-hat-3scale:billing-api
    name: Red Hat 3scale Billing API
    description: The 3scale Billing API enables management of billing and invoicing for API usage within the 3scale platform. It supports creating and managing invoices, payment transactions, and monetization of API subscriptions based on usage plans and application metrics. Billing is integrated with the account management system.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/billing
    baseURL: https://{your-domain}-admin.3scale.net
    tags:
      - API Management
      - Billing
      - Invoices
      - Monetization
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/billing
      - type: OpenAPI
        url: openapi/red-hat-3scale-billing-openapi.yml
  - aid: red-hat-3scale:webhooks-api
    name: Red Hat 3scale Webhooks
    description: 3scale Webhooks allow API providers to receive real-time HTTP callbacks about account, application, user, and plan events within the 3scale platform. Webhooks can be configured to trigger external systems when subscriptions change, new developers sign up, applications are updated, or keys are created or deleted.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/webhooks
    tags:
      - API Management
      - Events
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/webhooks
  - aid: red-hat-3scale:apicast-management-api
    name: Red Hat 3scale APIcast Management API
    description: The APIcast Management API is an HTTP REST interface exposed by the APIcast API gateway on port 8090 for debugging and runtime configuration. It provides endpoints to retrieve and update the gateway configuration, inspect DNS cache, trigger boot/initialization, and check readiness and liveness health status. Access is controlled via the APICAST_MANAGEMENT_API environment variable.
    humanURL: https://github.com/3scale/APIcast/blob/master/doc/management-api.md
    baseURL: http://localhost:8090
    tags:
      - API Gateway
      - Configuration
      - Health Checks
      - Management
    properties:
      - type: Documentation
        url: https://github.com/3scale/APIcast/blob/master/doc/management-api.md
      - type: OpenAPI
        url: openapi/red-hat-3scale-apicast-management-openapi.yml
  - aid: red-hat-3scale:toolbox-cli
    name: Red Hat 3scale Toolbox CLI
    description: The 3scale Toolbox is a command-line interface for automating 3scale configuration tasks. It wraps the 3scale Admin REST API to support copying APIs between tenants, promoting configurations between staging and production environments, importing OpenAPI specifications, and managing application plans and policies from the command line or CI/CD pipelines.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/operating_3scale/the-threescale-toolbox
    tags:
      - API Management
      - Automation
      - CLI
      - DevOps
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/operating_3scale/the-threescale-toolbox
      - type: GitHub
        url: https://github.com/3scale/3scale_toolbox
common:
  - type: Website
    url: https://www.redhat.com/en/technologies/jboss-middleware/3scale
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management
  - type: Getting Started
    url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/getting_started/index
  - type: Portal
    url: https://access.redhat.com/products/red-hat-3scale-api-management
  - type: GitHub Organization
    url: https://github.com/3scale
  - type: GitHubRepository
    url: https://github.com/3scale/APIcast
  - type: GitHubRepository
    url: https://github.com/3scale/porta
  - type: GitHubRepository
    url: https://github.com/3scale/3scale_toolbox
  - type: Blog
    url: https://www.redhat.com/en/blog/channel/red-hat-middleware
  - type: Support
    url: https://access.redhat.com/support
  - type: Terms of Service
    url: https://www.redhat.com/en/about/agreements
  - type: Privacy Policy
    url: https://www.redhat.com/en/about/privacy-policy
  - type: Status
    url: https://status.redhat.com/
  - type: Changelog
    url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/release_notes/index
  - type: OpenAPI
    url: openapi/red-hat-3scale-service-management-openapi.yml
  - type: OpenAPI
    url: openapi/red-hat-3scale-account-management-openapi.yml
  - type: OpenAPI
    url: openapi/red-hat-3scale-analytics-openapi.yml
  - type: OpenAPI
    url: openapi/red-hat-3scale-billing-openapi.yml
  - type: OpenAPI
    url: openapi/red-hat-3scale-apicast-management-openapi.yml
  - type: JSONLDContext
    url: json-ld/red-hat-3scale-context.jsonld
  - type: JSONSchema
    url: json-schema/red-hat-3scale-account-schema.json
  - type: JSONSchema
    url: json-schema/red-hat-3scale-application-schema.json
  - type: JSONStructure
    url: json-structure/red-hat-3scale-account-structure.json
  - type: SpectralRuleset
    url: rules/red-hat-3scale-rules.yml
  - type: NaftikoCapability
    url: capabilities/api-management.yaml
  - type: Vocabulary
    url: vocabulary/red-hat-3scale-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

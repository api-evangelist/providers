---
aid: red-hat-3scale
url: https://raw.githubusercontent.com/api-evangelist/red-hat-3scale/refs/heads/main/apis.yml
apis:
- aid: red-hat-3scale:service-management-api
  name: Red Hat 3scale Service Management API
  description: The 3scale Service Management API allows API providers to control and manage access to their APIs, track usage, and enforce traffic policies. It is used by the API gateway to authorize and report API calls in real time.
  humanURL: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management
  baseURL: https://su1.3scale.net
  tags:
  - Access Control
  - API Management
  - Traffic Management
  properties:
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/api_authentication/index
  - type: Reference
    url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/index
- aid: red-hat-3scale:account-management-api
  name: Red Hat 3scale Account Management API
  description: The 3scale Account Management API provides programmatic access to manage developer accounts, applications, and API keys within the 3scale platform. It enables automation of developer onboarding, subscription management, and application lifecycle operations.
  humanURL: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/index
  baseURL: https://{your-domain}-admin.3scale.net
  tags:
  - Account Management
  - API Management
  - Developer Portal
  properties:
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/index
  - type: Reference
    url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/accounts
- aid: red-hat-3scale:analytics-api
  name: Red Hat 3scale Analytics API
  description: The 3scale Analytics API provides access to API usage data, traffic metrics, and reporting for APIs managed through the 3scale platform. It enables operators to retrieve usage statistics and integrate analytics data into external systems.
  humanURL: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/analytics
  baseURL: https://{your-domain}-admin.3scale.net
  tags:
  - Analytics
  - API Management
  - Reporting
  properties:
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/analytics
- aid: red-hat-3scale:billing-api
  name: Red Hat 3scale Billing API
  description: The 3scale Billing API enables management of billing and invoicing for API usage within the 3scale platform. It supports creating and managing invoices, payment transactions, and monetization of API subscriptions.
  humanURL: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/billing
  baseURL: https://{your-domain}-admin.3scale.net
  tags:
  - API Management
  - Billing
  - Monetization
  properties:
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/billing
- aid: red-hat-3scale:webhooks-api
  name: Red Hat 3scale Webhooks
  description: 3scale Webhooks allow API providers to receive real-time notifications about account, application, and user events within the 3scale platform. Webhooks can be configured to trigger external systems when subscriptions change or new developers sign up.
  humanURL: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/webhooks
  tags:
  - API Management
  - Events
  - Webhooks
  properties:
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.14/html/admin_portal_guide/webhooks
name: Red Hat 3scale
tags:
- API Gateway
- API Management
- Enterprise
- Red Hat
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Red Hat 3scale API Management is an enterprise-grade API management platform that enables organizations to share, secure, distribute, control, and monetize APIs across internal and external teams. It provides a developer portal, analytics, access control, and policy enforcement for REST, SOAP, and other API types.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


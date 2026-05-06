---
aid: ibm-api-connect
name: IBM API Connect
description: IBM API Connect is a comprehensive end-to-end API management solution that enables organizations to create, secure, manage, share, monetize, and analyze APIs across clouds. It provides an API gateway, developer portal, and lifecycle management capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - API Management
  - Developer Portal
  - IBM
url: https://raw.githubusercontent.com/api-evangelist/ibm-api-connect/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ibm-api-connect:ibm-api-connect-management-api
    name: IBM API Connect Management API
    description: The IBM API Connect Management API provides programmatic access to manage APIs, products, catalogs, organizations, and other platform resources in the API Connect platform. It is used to automate API lifecycle management tasks including publishing, versioning, and subscription management.
    humanURL: https://cloud.ibm.com/apidocs/apiconnect/apic-management-api
    baseURL: https://api.us-south.apiconnect.cloud.ibm.com
    tags:
      - Administration
      - API Management
      - Lifecycle
      - REST API
    properties:
      - type: Documentation
        url: https://cloud.ibm.com/apidocs/apiconnect/apic-management-api
      - type: Getting Started
        url: https://cloud.ibm.com/docs/apiconnect?topic=apiconnect-getting-started
      - type: Reference
        url: https://cloud.ibm.com/apidocs/apiconnect/apic-management-api
      - type: Authentication
        url: https://cloud.ibm.com/docs/apiconnect?topic=apiconnect-getting-started#getting-started-prereqs
  - aid: ibm-api-connect:ibm-api-connect-consumer-api
    name: IBM API Connect Consumer API
    description: The IBM API Connect Consumer API provides programmatic access to the developer portal capabilities, allowing consumer organizations and applications to discover APIs, manage subscriptions, and retrieve credentials. It is used by application developers who consume APIs published through the API Connect platform.
    humanURL: https://cloud.ibm.com/apidocs/apiconnect/apic-consumer-api
    baseURL: https://api.us-south.apiconnect.cloud.ibm.com
    tags:
      - Consumer
      - Developer Portal
      - REST API
      - Subscriptions
    properties:
      - type: Documentation
        url: https://cloud.ibm.com/apidocs/apiconnect/apic-consumer-api
      - type: Reference
        url: https://cloud.ibm.com/apidocs/apiconnect/apic-consumer-api
  - aid: ibm-api-connect:ibm-api-connect-v1-api
    name: IBM API Connect V1 API
    description: The IBM API Connect V1 API is the earlier generation management REST API for the API Connect platform, providing access to organizations, catalogs, APIs, and products. It is retained for backward compatibility with integrations built against the v1 interface.
    humanURL: https://cloud.ibm.com/apidocs/apiconnect/apiconnect-v1
    baseURL: https://api.us-south.apiconnect.cloud.ibm.com
    tags:
      - API Management
      - Legacy
      - REST API
      - V1
    properties:
      - type: Documentation
        url: https://cloud.ibm.com/apidocs/apiconnect/apiconnect-v1
      - type: Reference
        url: https://cloud.ibm.com/apidocs/apiconnect/apiconnect-v1
common:
  - type: Website
    url: https://www.ibm.com/products/api-connect
  - type: Documentation
    url: https://www.ibm.com/docs/en/api-connect/
  - type: Getting Started
    url: https://cloud.ibm.com/docs/apiconnect?topic=apiconnect-getting-started
  - type: Support
    url: https://www.ibm.com/mysupport
  - type: Pricing
    url: https://www.ibm.com/products/api-connect/pricing
  - type: Blog
    url: https://developer.ibm.com/blogs/
  - type: Change Log
    url: https://www.ibm.com/docs/en/api-connect/saas?topic=overview-whats-new
  - type: GitHub Organization
    url: https://github.com/ibm-apiconnect
  - type: Community
    url: https://community.ibm.com/community/user/integration/communities/community-home?CommunityKey=2106cca0-a9f9-45c6-9b28-01a28f39ce47
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/ibm-api-connect
  - type: YouTube
    url: https://www.youtube.com/@IBMTechnology
  - type: Terms of Service
    url: https://www.ibm.com/support/customer/csol/terms/
  - type: Privacy Policy
    url: https://www.ibm.com/privacy
  - type: Status
    url: https://cloud.ibm.com/status
  - type: Rules
    url: rules/ibm-api-connect-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

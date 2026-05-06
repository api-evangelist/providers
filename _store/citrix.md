---
aid: citrix
name: Citrix
description: Citrix is a global software company providing virtualization, networking, workspace, and digital experience products that allow organizations to deliver applications and desktops securely from data centers and clouds to any device. Citrix exposes its programmable surface through the Citrix Cloud platform and developer.citrix.com / developer-docs.citrix.com, with REST APIs spanning Virtual Apps and Desktops, DaaS, Workspace, Citrix Cloud, ADC (NetScaler) NITRO, Endpoint Management, Secure Private Access, and Analytics. Authentication uses OAuth 2.0 bearer tokens issued through Citrix Cloud customer-id-scoped credentials.
image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
url: https://raw.githubusercontent.com/api-evangelist/citrix/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
tags:
  - Application Delivery
  - Desktop-As-A-Service
  - Networking
  - Virtualization
  - Workspace
apis:
  - name: Citrix Virtual Apps and Desktops REST API
    description: Manage and monitor Citrix Virtual Apps and Desktops deployments.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://developer.citrix.com/citrix-virtual-apps-and-desktops
    baseURL: https://{customer-id}.xendesktop.net
    tags:
      - Remote Access
      - VDI
      - Virtual Desktop
    properties:
      - type: Documentation
        url: https://developer.citrix.com/citrix-virtual-apps-and-desktops/citrix-cvad-rest-apis
      - type: OpenAPI
        url: https://developer.citrix.com/citrix-virtual-apps-and-desktops/citrix-cvad-rest-apis/docs/openapi
      - type: Authentication
        url: https://developer.citrix.com/citrix-virtual-apps-and-desktops/citrix-cvad-rest-apis/docs/how-to-get-started
      - type: OpenAPI
        url: openapi/citrix-daas-openapi.yml
  - name: Citrix Workspace API
    description: Integrate and customize Citrix Workspace for end users.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://developer.citrix.com/citrix-workspace
    baseURL: https://api.cloud.com
    tags:
      - SSO
      - User Experience
      - Workspace
    properties:
      - type: Documentation
        url: https://developer.citrix.com/citrix-workspace/citrix-workspace-platform
      - type: API Reference
        url: https://developer.citrix.com/citrix-workspace/citrix-workspace-platform/build/api-reference
  - name: Citrix ADC (NetScaler) NITRO API
    description: Configure and monitor Citrix ADC application delivery controllers.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://developer.citrix.com/citrix-adc
    baseURL: https://{netscaler-ip}/nitro/v1
    tags:
      - ADC
      - Application Delivery
      - Load Balancing
      - Networking
    properties:
      - type: Documentation
        url: https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/latest/
      - type: API Reference
        url: https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/latest/api-reference/
      - type: SDK
        url: https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/latest/getting-started/
      - type: OpenAPI
        url: openapi/citrix-adc-nitro-openapi.yml
  - name: Citrix DaaS REST API
    description: Manage Citrix Desktop as a Service (DaaS) cloud deployments.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://developer.citrix.com/citrix-daas
    baseURL: https://api.cloud.com/cvad
    tags:
      - Cloud
      - DaaS
      - Desktop as a Service
    properties:
      - type: Documentation
        url: https://developer.citrix.com/citrix-daas/citrix-daas-rest-apis
      - type: OpenAPI
        url: https://developer.citrix.com/citrix-daas/citrix-daas-rest-apis/docs/openapi
      - type: Getting Started
        url: https://developer.citrix.com/citrix-daas/citrix-daas-rest-apis/docs/getting-started
      - type: OpenAPI
        url: openapi/citrix-daas-openapi.yml
  - name: Citrix Analytics API
    description: Access analytics data for security and performance insights.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://developer.citrix.com/citrix-analytics
    baseURL: https://api.analytics.cloud.com
    tags:
      - Analytics
      - Insights
      - Monitoring
      - Security
    properties:
      - type: Documentation
        url: https://developer.citrix.com/citrix-analytics/api-overview
      - type: API Reference
        url: https://developer.citrix.com/citrix-analytics/api-reference
  - name: Citrix Cloud API
    description: Platform-level API for managing Citrix Cloud services, including authentication, service principals, resource locations, and notifications across the Citrix Cloud platform.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://developer-docs.citrix.com/en-us/citrix-cloud/citrix-cloud-api-overview/get-started-with-citrix-cloud-apis.html
    baseURL: https://api.cloud.com
    tags:
      - Cloud
      - Identity
      - Management
      - Platform
    properties:
      - type: Documentation
        url: https://developer-docs.citrix.com/en-us/citrix-cloud/citrix-cloud-api-overview/get-started-with-citrix-cloud-apis.html
      - type: Getting Started
        url: https://developer-docs.citrix.com/en-us/citrix-cloud/citrix-cloud-api-overview/citrix-cloud-api-walkthrough.html
      - type: Authentication
        url: https://developer-docs.citrix.com/en-us/citrix-cloud/citrix-cloud-api-overview/get-started-with-citrix-cloud-apis.html
      - type: OpenAPI
        url: openapi/citrix-cloud-openapi.yml
  - name: Citrix Monitor Service OData API
    description: OData-based API for querying monitoring data from Citrix Virtual Apps and Desktops deployments, including session, connection, machine, and application usage data for reporting and analytics.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://developer-docs.citrix.com/en-us/monitor-service-odata-api/overview.html
    baseURL: https://{delivery-controller}/Citrix/Monitor/OData/v4/Data
    tags:
      - Analytics
      - Monitoring
      - OData
      - Reporting
    properties:
      - type: Documentation
        url: https://developer-docs.citrix.com/en-us/monitor-service-odata-api/overview.html
      - type: Reference
        url: https://developer-docs.citrix.com/en-us/monitor-service-odata-api/monitor-service-resources.html
      - type: Getting Started
        url: https://developer-docs.citrix.com/en-us/monitor-service-odata-api/access-methods.html
  - name: Citrix StoreFront Web API
    description: HTTP API for building custom client applications that authenticate users, enumerate available applications and desktops, manage HDX sessions, and launch resources from Citrix StoreFront.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://developer-docs.citrix.com/en-us/storefront/storefront-web-api/overview.html
    baseURL: https://{storefront-server}/Citrix/Store
    tags:
      - Client
      - Resources
      - Sessions
      - StoreFront
    properties:
      - type: Documentation
        url: https://developer-docs.citrix.com/en-us/storefront/storefront-web-api/overview.html
      - type: Getting Started
        url: https://developer-docs.citrix.com/en-us/storefront/storefront-web-api/getting-started.html
      - type: Reference
        url: https://developer-docs.citrix.com/en-us/storefront/storefront-web-api/apis/
      - type: OpenAPI
        url: openapi/citrix-storefront-web-openapi.yml
  - name: Citrix StoreFront Store Services API
    description: Server-side API for customizing and extending the Citrix StoreFront store services, including endpoint management, authentication, and resource enumeration behaviors.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://developer-docs.citrix.com/en-us/storefront/storefront-store-services-api/overview.html
    baseURL: https://{storefront-server}/Citrix/Store
    tags:
      - Customization
      - Server
      - StoreFront
    properties:
      - type: Documentation
        url: https://developer-docs.citrix.com/en-us/storefront/storefront-store-services-api/overview.html
      - type: Reference
        url: https://developer-docs.citrix.com/en-us/storefront/storefront-store-services-api/endpoints-service/
  - name: Citrix StoreFront Authentication SDK
    description: SDK for building custom authentication methods for Citrix StoreFront, allowing integration with third-party identity providers and custom authentication workflows.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://developer-docs.citrix.com/en-us/storefront/citrix-storefront-authentication-sdk/overview.html
    baseURL: https://{storefront-server}
    tags:
      - Authentication
      - Identity
      - StoreFront
    properties:
      - type: Documentation
        url: https://developer-docs.citrix.com/en-us/storefront/citrix-storefront-authentication-sdk/overview.html
  - name: Citrix Endpoint Management REST API
    description: REST API for managing mobile devices, applications, and policies in Citrix Endpoint Management, enabling integration with external systems for device lifecycle management and compliance.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://docs.citrix.com/en-us/citrix-endpoint-management/rest-apis.html
    baseURL: https://{xms-server}:4443/xenmobile/api/v1
    tags:
      - Endpoint Management
      - MDM
      - Mobile
      - UEM
    properties:
      - type: Documentation
        url: https://docs.citrix.com/en-us/citrix-endpoint-management/rest-apis.html
      - type: OpenAPI
        url: openapi/citrix-endpoint-management-openapi.yml
  - name: Citrix Secure Private Access API
    description: REST API for managing zero trust network access policies, applications, application domains, and certificates in Citrix Secure Private Access, providing secure access to internal web and SaaS applications.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.png
    humanURL: https://developer-docs.citrix.com/en-us/secure-private-access/access-security/overview.html
    baseURL: https://api.cloud.com/accessSecurity
    tags:
      - Access Control
      - Security
      - Zero Trust
      - ZTNA
    properties:
      - type: Documentation
        url: https://developer-docs.citrix.com/en-us/secure-private-access/access-security/overview.html
      - type: Getting Started
        url: https://developer-docs.citrix.com/en-us/secure-private-access/access-security/getting-started.html
      - type: OpenAPI
        url: openapi/citrix-secure-private-access-openapi.yml
common:
  - type: Portal
    url: https://developer-docs.citrix.com/
  - type: Getting Started
    url: https://developer-docs.citrix.com/en-us/citrix-cloud/citrix-cloud-api-overview/get-started-with-citrix-cloud-apis.html
  - type: Authentication
    url: https://developer-docs.citrix.com/en-us/citrix-cloud/citrix-cloud-api-overview/get-started-with-citrix-cloud-apis.html
  - type: Blog
    url: https://www.citrix.com/blogs/
  - type: Status
    url: https://status.cloud.com/
  - type: Support
    url: https://support.citrix.com/
  - type: Terms of Service
    url: https://developer.cloud.com/citrix-developer-terms-of-use
  - type: Privacy Policy
    url: https://www.citrix.com/about/legal/privacy/plain.html
  - type: GitHub Organization
    url: https://github.com/citrix
  - type: Community
    url: https://discussions.citrix.com/
  - type: SDKs
    url: https://docs.citrix.com/en-us/citrix-cloud/sdk-api.html
  - type: Website
    url: https://www.citrix.com
  - type: Login
    url: https://accounts.cloud.com/
  - type: JSON-LD
    url: json-ld/citrix-context.jsonld
  - type: JSONSchema
    url: json-schema/citrix-machine-catalog-schema.json
  - type: JSONSchema
    url: json-schema/citrix-session-schema.json
  - type: Spectral
    url: rules/citrix-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/citrix-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

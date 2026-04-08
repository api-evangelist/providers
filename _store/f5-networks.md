---
aid: f5-networks
url: https://raw.githubusercontent.com/api-evangelist/f5-networks/refs/heads/main/apis.yml
apis:
- name: F5 BIG-IP iControl REST API
  description: The iControl REST API provides programmatic access to manage and configure F5 BIG-IP devices. Enables automation of network, security, and application delivery services.
  image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
  humanURL: https://www.f5.com/services/resources/api
  baseURL: https://{{bigip_host}}/mgmt/tm
  tags:
  - ADC
  - Application Delivery
  - Load Balancing
  - Network Management
  - Security
  properties:
  - type: Documentation
    url: https://clouddocs.f5.com/api/icontrol-rest/
  - type: OpenAPI
    url: openapi/bigip-icontrol-rest.yml
  - type: OpenAPI
    url: https://clouddocs.f5.com/api/icontrol-rest/APIRef_tm_ltm.html
  - type: JSONSchema
    url: json-schema/f5-virtual-server-schema.json
  - type: JSONLD
    url: json-ld/f5-networks-context.jsonld
  - type: Authentication
    url: https://clouddocs.f5.com/api/icontrol-rest/Authentication.html
  - type: API Reference
    url: https://clouddocs.f5.com/api/icontrol-rest/APIRef.html
  - type: Getting Started
    url: https://clouddocs.f5.com/api/
  - type: SDK
    url: https://github.com/F5Networks/f5-icontrol-rest-python
  - type: SDK
    url: https://f5-sdk.readthedocs.io/
  contact:
  - FN: F5 Support
    email: support@f5.com
    url: https://www.f5.com/company/contact/regional-offices
- name: F5 Distributed Cloud API
  description: API for F5 Distributed Cloud Services providing multi-cloud networking, application security, and edge computing capabilities.
  image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
  humanURL: https://docs.cloud.f5.com/docs/api
  baseURL: https://{{tenant}}.console.ves.volterra.io/api
  tags:
  - API Security
  - CDN
  - Edge Computing
  - Multi-Cloud
  - WAF
  properties:
  - type: Documentation
    url: https://docs.cloud.f5.com/docs/api
  - type: Swagger
    url: https://docs.cloud.f5.com/docs/api/swagger
  - type: API Console
    url: https://console.ves.volterra.io/
  - type: Getting Started
    url: https://docs.cloud.f5.com/docs/how-to/api-how-to
  - type: API Reference
    url: https://docs.cloud.f5.com/docs-v2/reference/api-ref
  - type: Authentication
    url: https://docs.cloud.f5.com/docs-v2/api/authentication
  - type: Change Log
    url: https://docs.cloud.f5.com/docs-v2/platform/changelogs/saas-release-notes
  contact:
  - FN: F5 Distributed Cloud Support
    email: support@f5.com
- name: F5 NGINX Management Suite API
  description: REST API for managing NGINX instances, monitoring performance, and configuring application delivery through NGINX Management Suite.
  image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
  humanURL: https://docs.nginx.com/nginx-management-suite/
  baseURL: https://{{nms-host}}/api
  tags:
  - API Gateway
  - Application Delivery
  - Configuration Management
  - Monitoring
  - NGINX
  properties:
  - type: Documentation
    url: https://docs.nginx.com/nginx-management-suite/admin-guides/api/
  - type: API Reference
    url: https://docs.nginx.com/nginx-management-suite/api-reference/
  - type: Getting Started
    url: https://docs.nginx.com/nginx-management-suite/getting-started/
  contact:
  - FN: NGINX Support
    email: nginx-support@f5.com
- name: F5 Essential App Protect API
  description: API for managing F5's application security services including WAF policies, bot defense, and API protection.
  image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
  humanURL: https://docs.f5.com/en-us/app-protect
  baseURL: https://api.f5.com/app-protect
  tags:
  - API Protection
  - Bot Defense
  - DDoS Protection
  - Security
  - WAF
  properties:
  - type: Documentation
    url: https://docs.f5.com/en-us/app-protect/api-reference
  - type: Security Policies
    url: https://docs.f5.com/en-us/app-protect/security-policies
- name: F5 BIG-IQ Centralized Management API
  description: REST API for BIG-IQ Centralized Management providing programmatic control over BIG-IP device management, licensing, monitoring, and analytics across your F5 infrastructure.
  image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
  humanURL: https://clouddocs.f5.com/products/big-iq/mgmt-api/v0.0/
  baseURL: https://{{bigiq_host}}/mgmt
  tags:
  - Analytics
  - Centralized Management
  - Device Management
  - Licensing
  - Monitoring
  properties:
  - type: Documentation
    url: https://clouddocs.f5.com/products/big-iq/mgmt-api/v0.0/
  - type: API Reference
    url: https://clouddocs.f5.com/products/big-iq/mgmt-api/v0.0/ApiReferences/bigiq_public_api_ref/r_public_api_references.html
  - type: Getting Started
    url: https://clouddocs.f5.com/products/big-iq/mgmt-api/v0.0/HowToSamples/bigiq_public_api_wf/t_bigiq_public_api_workflows.html
  contact:
  - FN: F5 Support
    email: support@f5.com
- name: F5 BIG-IP Application Services 3 Extension API
  description: Declarative API for automating layer 4-7 application services on BIG-IP using JSON declarations. AS3 enables infrastructure-as-code for application delivery configuration.
  image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
  humanURL: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/
  baseURL: https://{{bigip_host}}/mgmt/shared/appsvcs
  tags:
  - Application Delivery
  - Application Services
  - Automation
  - Declarative
  - Infrastructure as Code
  properties:
  - type: Documentation
    url: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/
  - type: API Reference
    url: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/refguide/as3-api.html
  - type: Getting Started
    url: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/userguide/
  - type: GitHubOrg
    url: https://github.com/F5Networks/f5-appsvcs-extension
  contact:
  - FN: F5 Support
    email: support@f5.com
- name: F5 Declarative Onboarding API
  description: Declarative API for automating layer 1-3 BIG-IP onboarding and initial device configuration using JSON declarations, making BIG-IP available on the network and ready for application services.
  image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
  humanURL: https://clouddocs.f5.com/products/extensions/f5-declarative-onboarding/latest/
  baseURL: https://{{bigip_host}}/mgmt/shared/declarative-onboarding
  tags:
  - Automation
  - Declarative
  - Device Configuration
  - Infrastructure as Code
  - Onboarding
  properties:
  - type: Documentation
    url: https://clouddocs.f5.com/products/extensions/f5-declarative-onboarding/latest/
  - type: API Reference
    url: https://clouddocs.f5.com/products/extensions/f5-declarative-onboarding/latest/apidocs.html
  - type: Getting Started
    url: https://clouddocs.f5.com/products/extensions/f5-declarative-onboarding/latest/using-do.html
  contact:
  - FN: F5 Support
    email: support@f5.com
- name: F5 Telemetry Streaming API
  description: Declarative API for aggregating, normalizing, and forwarding BIG-IP statistics and events to third-party analytics consumers including Splunk, Azure Log Analytics, AWS CloudWatch, and more.
  image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
  humanURL: https://clouddocs.f5.com/products/extensions/f5-telemetry-streaming/latest/
  baseURL: https://{{bigip_host}}/mgmt/shared/telemetry
  tags:
  - Analytics
  - Monitoring
  - Observability
  - Streaming
  - Telemetry
  properties:
  - type: Documentation
    url: https://clouddocs.f5.com/products/extensions/f5-telemetry-streaming/latest/
  - type: API Reference
    url: https://clouddocs.f5.com/products/extensions/f5-telemetry-streaming/latest/rest-api-endpoints.html
  - type: GitHubOrg
    url: https://github.com/F5Networks/f5-telemetry-streaming
  contact:
  - FN: F5 Support
    email: support@f5.com
- name: F5 NGINX Plus API
  description: REST API for NGINX Plus providing real-time live activity monitoring, dynamic upstream configuration, key-value store management, and server health statistics without requiring configuration reloads.
  image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
  humanURL: https://docs.nginx.com/nginx/
  baseURL: https://{{nginx_host}}/api
  tags:
  - Dynamic Configuration
  - Load Balancing
  - Monitoring
  - NGINX
  - Reverse Proxy
  properties:
  - type: Documentation
    url: https://docs.nginx.com/nginx/
  - type: API Reference
    url: https://docs.nginx.com/nginx/admin-guide/monitoring/live-activity-monitoring/
  - type: Getting Started
    url: https://docs.nginx.com/nginx/admin-guide/load-balancer/dynamic-configuration-api/
  contact:
  - FN: NGINX Support
    email: nginx-support@f5.com
- name: F5 NGINX One Console API
  description: API for managing and monitoring NGINX instances across environments from a single console, including configuration management, performance metrics, security vulnerability tracking, and SSL certificate management.
  image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
  humanURL: https://docs.nginx.com/nginx-one-console/
  baseURL: https://{{nginx-one-host}}/api
  tags:
  - Configuration Management
  - Fleet Management
  - Monitoring
  - NGINX
  - Security
  properties:
  - type: Documentation
    url: https://docs.nginx.com/nginx-one-console/
  - type: API Reference
    url: https://docs.nginx.com/nginx-one-console/api/api-reference-guide/
  - type: Authentication
    url: https://docs.nginx.com/nginx-one-console/api/authentication/
  contact:
  - FN: NGINX Support
    email: nginx-support@f5.com
- name: F5 NGINX Ingress Controller API
  description: Kubernetes Ingress Controller implementation for NGINX and NGINX Plus providing load balancing, SSL/TLS termination, content-based routing, and advanced traffic management for containerized applications.
  image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
  humanURL: https://docs.nginx.com/nginx-ingress-controller/
  baseURL: https://{{kubernetes_host}}
  tags:
  - Containers
  - Ingress Controller
  - Kubernetes
  - Load Balancing
  - NGINX
  properties:
  - type: Documentation
    url: https://docs.nginx.com/nginx-ingress-controller/
  - type: GitHubOrg
    url: https://github.com/nginx/kubernetes-ingress
  contact:
  - FN: NGINX Support
    email: nginx-support@f5.com
name: F5 Networks
tags:
- API Gateway
- Application Delivery
- Automation
- Edge Computing
- Kubernetes
- Load Balancing
- Multi-Cloud
- NGINX
- Security
- WAF
type: Contract
image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: F5 Networks is a leader in application delivery networking technology that specializes in application availability, acceleration, and security solutions.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


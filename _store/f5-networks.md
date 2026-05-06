---
name: F5 Networks
description: F5 Networks is a leader in application delivery networking technology that specializes in application availability, acceleration, and security solutions.
image: https://www.f5.com/content/dam/f5-com/global-assets/images/f5-logo.svg
url: https://www.f5.com/apis
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.18'
type: Index
access: 3rd-Party
position: Consumer
segments:
  - Gateways
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
      - type: JSONLD
        url: json-ld/bigip-icontrol-rest-context.jsonld
      - type: Authentication
        url: https://clouddocs.f5.com/api/icontrol-rest/Authentication.html
      - type: APIReference
        url: https://clouddocs.f5.com/api/icontrol-rest/APIRef.html
      - type: GettingStarted
        url: https://clouddocs.f5.com/api/
      - type: SDK
        url: https://github.com/F5Networks/f5-icontrol-rest-python
        title: Python SDK
      - type: SDK
        url: https://f5-sdk.readthedocs.io/
        title: Python SDK Docs
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
      - type: OpenAPI
        url: https://docs.cloud.f5.com/docs/api/swagger
      - type: Console
        url: https://console.ves.volterra.io/
      - type: GettingStarted
        url: https://docs.cloud.f5.com/docs/how-to/api-how-to
      - type: APIReference
        url: https://docs.cloud.f5.com/docs-v2/reference/api-ref
      - type: Authentication
        url: https://docs.cloud.f5.com/docs-v2/api/authentication
      - type: ChangeLog
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
      - type: APIReference
        url: https://docs.nginx.com/nginx-management-suite/api-reference/
      - type: GettingStarted
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
      - type: Security
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
      - type: APIReference
        url: https://clouddocs.f5.com/products/big-iq/mgmt-api/v0.0/ApiReferences/bigiq_public_api_ref/r_public_api_references.html
      - type: GettingStarted
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
      - type: APIReference
        url: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/refguide/as3-api.html
      - type: GettingStarted
        url: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/userguide/
      - type: GitHubRepository
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
      - type: APIReference
        url: https://clouddocs.f5.com/products/extensions/f5-declarative-onboarding/latest/apidocs.html
      - type: GettingStarted
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
      - type: APIReference
        url: https://clouddocs.f5.com/products/extensions/f5-telemetry-streaming/latest/rest-api-endpoints.html
      - type: GitHubRepository
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
      - type: APIReference
        url: https://docs.nginx.com/nginx/admin-guide/monitoring/live-activity-monitoring/
      - type: GettingStarted
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
      - type: APIReference
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
      - type: GitHubRepository
        url: https://github.com/nginx/kubernetes-ingress
    contact:
      - FN: NGINX Support
        email: nginx-support@f5.com
common:
  - type: Documentation
    url: https://docs.nginx.com/
  - type: DeveloperPortal
    url: https://clouddocs.f5.com/
  - type: Blog
    url: https://www.f5.com/company/blog
  - type: GitHubOrganization
    url: https://github.com/F5Networks
  - type: GitHubOrganization
    url: https://github.com/f5devcentral/
    title: F5 DevCentral
  - type: Support
    url: https://support.f5.com/
  - type: StatusPage
    url: https://www.f5cloudstatus.com/
  - type: TermsOfService
    url: https://www.f5.com/company/policies/terms-of-use
  - type: PrivacyPolicy
    url: https://www.f5.com/company/policies/privacy-notice
  - type: SignUp
    url: https://account.f5.com/myf5
  - type: Login
    url: https://identity.account.f5.com/
  - type: LinkedIn
    url: https://www.linkedin.com/company/f5
  - type: X
    url: https://twitter.com/f5networks
  - type: YouTube
    url: https://www.f5.com/resources/videos
  - type: Features
    data:
      - name: Multi-Cloud Networking
        description: Connect and secure applications across any cloud, data center, or edge environment with consistent policy and visibility.
      - name: Application Delivery Controller
        description: Advanced load balancing, traffic management, and application acceleration for high availability and performance.
      - name: Web Application Firewall
        description: Comprehensive protection against OWASP Top 10 threats, bot attacks, and API vulnerabilities.
      - name: Infrastructure as Code
        description: Declarative APIs (AS3, DO, TS) for automating BIG-IP configuration and application delivery.
      - name: NGINX Reverse Proxy
        description: High-performance reverse proxy, load balancing, and web serving for modern applications.
      - name: API Gateway
        description: Secure and manage API traffic with rate limiting, authentication, and traffic shaping.
      - name: DDoS Protection
        description: Volumetric and application-layer DDoS mitigation with always-on or on-demand protection.
      - name: SSL/TLS Offloading
        description: Centralized SSL/TLS certificate management and encryption offloading for improved performance.
  - type: UseCases
    data:
      - name: Application Load Balancing
        description: Distribute application traffic across servers for high availability, performance, and fault tolerance.
      - name: Zero Trust Security
        description: Implement zero trust architecture with identity-aware proxy, micro-segmentation, and continuous verification.
      - name: Kubernetes Ingress
        description: Manage ingress traffic for containerized applications with NGINX Ingress Controller in Kubernetes clusters.
      - name: Multi-Cloud Application Delivery
        description: Deliver applications consistently across AWS, Azure, GCP, and on-premises with unified policy management.
      - name: API Security
        description: Protect APIs from abuse, injection attacks, and unauthorized access with granular security policies.
      - name: DevOps Automation
        description: Automate network and security infrastructure provisioning using declarative APIs and CI/CD pipelines.
  - type: Integrations
    data:
      - name: AWS
        description: Deploy BIG-IP and Distributed Cloud services natively on AWS with CloudFormation templates and marketplace offerings.
      - name: Azure
        description: Integrate F5 solutions with Azure services including AKS, App Gateway, and Azure AD for cloud-native security.
      - name: Google Cloud
        description: Deploy F5 solutions on GCP with support for GKE, Cloud Load Balancing, and Anthos.
      - name: Kubernetes
        description: Native Kubernetes integration through NGINX Ingress Controller, Container Ingress Services, and Helm charts.
      - name: Terraform
        description: Infrastructure as Code support with official Terraform providers for BIG-IP and Distributed Cloud.
      - name: Ansible
        description: Ansible modules and roles for automating BIG-IP configuration, deployment, and orchestration.
      - name: Splunk
        description: Forward telemetry data to Splunk for centralized logging, analytics, and security monitoring.
      - name: ServiceNow
        description: ITSM integration for automated incident management and change control of F5 infrastructure.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

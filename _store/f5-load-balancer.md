---
aid: f5-load-balancer
name: F5 Load Balancer
description: APIs for managing F5 BIG-IP Load Balancer configuration, monitoring, and operations. F5 BIG-IP is an application delivery controller that provides intelligent traffic management, load balancing, and application security.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Application Delivery
  - BIG-IP
  - Load Balancer
  - Networking
  - Traffic Management
url: https://www.f5.com
created: '2024-01-01'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: f5-load-balancer:f5-bigip-icontrol-rest-api
    name: F5 BIG-IP iControl REST API
    description: Primary REST API for managing F5 BIG-IP systems including virtual servers, pools, nodes, and policies for application delivery and load balancing.
    humanURL: https://clouddocs.f5.com/api/icontrol-rest/
    baseURL: https://bigip-host/mgmt/tm
    tags:
      - Configuration
      - Management
      - REST API
    properties:
      - type: Documentation
        url: https://clouddocs.f5.com/api/icontrol-rest/
      - type: Authentication
        url: https://clouddocs.f5.com/api/icontrol-rest/Authentication.html
      - type: OpenAPI
        url: openapi/f5-load-balancer-icontrol-rest-openapi.yml
  - aid: f5-load-balancer:f5-bigip-as3-api
    name: F5 BIG-IP AS3 API
    description: Application Services 3 Extension for declarative API-based application deployment using JSON declarations.
    humanURL: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/
    baseURL: https://bigip-host/mgmt/shared/appsvcs
    tags:
      - AS3
      - Automation
      - Declarative
    properties:
      - type: Documentation
        url: https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/
      - type: OpenAPI
        url: openapi/f5-load-balancer-as3-openapi.yml
  - aid: f5-load-balancer:f5-bigip-declarative-onboarding-api
    name: F5 BIG-IP Declarative Onboarding API
    description: Declarative Onboarding (DO) extension for initial BIG-IP system configuration and provisioning via JSON declarations covering licensing, networking, user management, and module provisioning.
    humanURL: https://clouddocs.f5.com/products/extensions/f5-declarative-onboarding/latest/
    baseURL: https://bigip-host/mgmt/shared/declarative-onboarding
    tags:
      - Declarative
      - Onboarding
      - Provisioning
    properties:
      - type: Documentation
        url: https://clouddocs.f5.com/products/extensions/f5-declarative-onboarding/latest/
      - type: OpenAPI
        url: openapi/f5-load-balancer-declarative-onboarding-openapi.yml
common:
  - type: Portal
    url: https://clouddocs.f5.com/
  - type: Documentation
    url: https://clouddocs.f5.com/api/
  - type: Support
    url: https://www.f5.com/services/support
  - type: TermsOfService
    url: https://www.f5.com/company/policies/terms-of-use
  - type: PrivacyPolicy
    url: https://www.f5.com/company/policies/privacy-notice
  - type: Blog
    url: https://www.f5.com/company/blog
  - type: GitHubOrganization
    url: https://github.com/F5Networks
  - type: Website
    url: https://www.f5.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

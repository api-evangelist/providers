---
aid: f5-load-balancer
url: https://raw.githubusercontent.com/api-evangelist/f5-load-balancer/refs/heads/main/apis.yml
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
name: F5 Load Balancer
tags:
- Application Delivery
- BIG-IP
- Load Balancer
- Networking
- Traffic Management
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for managing F5 BIG-IP Load Balancer configuration, monitoring, and operations. F5 BIG-IP is an application delivery controller that provides intelligent traffic management, load balancing, and application security.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


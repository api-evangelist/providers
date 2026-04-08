---
aid: juniper
url: https://raw.githubusercontent.com/api-evangelist/juniper/refs/heads/main/apis.yml
apis:
- name: Junos Space API
  description: RESTful API for managing Juniper devices through Junos Space Network Management Platform.
  humanURL: https://www.juniper.net/documentation/product/us/en/junos-space-network-management-platform/
  baseURL: https://[space-server]/api/space
  tags:
  - Configuration
  - Device Management
  - Network Management
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/us/en/software/junos-space/
  - type: OpenAPI
    url: https://[space-server]/api/space/api-explorer
  - type: OpenAPI
    url: openapi/juniper-junos-space-openapi.yml
  contact:
  - FN: Juniper Support
    email: support@juniper.net
- name: Juniper Apstra API
  description: Intent-based networking API for data center automation and multivendor network management.
  humanURL: https://www.juniper.net/us/en/products/network-automation/apstra.html
  baseURL: https://[apstra-server]/api
  tags:
  - Automation
  - Data Center
  - Intent-Based Networking
  - Multi-Vendor
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/us/en/software/apstra/
  - type: API Reference
    url: https://www.juniper.net/documentation/us/en/software/apstra/apstra-user-guide/topics/concept/apstra-api-overview.html
  - type: OpenAPI
    url: openapi/juniper-apstra-openapi.yml
  contact:
  - FN: Juniper Support
    email: support@juniper.net
- name: Junos PyEZ (Python API)
  description: Python library for automating Junos devices using NETCONF.
  humanURL: https://www.juniper.net/documentation/us/en/software/junos-pyez/
  baseURL: netconf://[device-ip]:830
  tags:
  - Automation
  - Device Management
  - NETCONF
  - Python
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/us/en/software/junos-pyez/
  - type: GitHub
    url: https://github.com/Juniper/py-junos-eznc
  - type: PyPI
    url: https://pypi.org/project/junos-eznc/
  contact:
  - FN: Juniper Support
    email: support@juniper.net
- name: Junos REST API
  description: RESTful interface for configuring and monitoring Junos devices.
  humanURL: https://www.juniper.net/documentation/us/en/software/junos/rest-api/
  baseURL: https://[device-ip]/rpc
  tags:
  - Device Configuration
  - Monitoring
  - REST API
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/us/en/software/junos/rest-api/
  - type: API Explorer
    url: https://[device-ip]/api-explorer
  - type: OpenAPI
    url: openapi/juniper-junos-rest-api-openapi.yml
  contact:
  - FN: Juniper Support
    email: support@juniper.net
- name: Juniper Mist API
  description: Cloud-native AI-driven networking API for wireless, wired, and SD-WAN management.
  humanURL: https://www.mist.com/documentation/mist-api/
  baseURL: https://api.mist.com/api/v1
  tags:
  - AI
  - Analytics
  - Cloud
  - SD-WAN
  - Wireless
  properties:
  - type: Documentation
    url: https://www.mist.com/documentation/mist-api/
  - type: API Reference
    url: https://doc.mist-lab.fr/
  - type: Swagger
    url: https://api.mist.com/api/v1/docs
  - type: OpenAPI
    url: openapi/juniper-mist-openapi.yml
  contact:
  - FN: Mist Support
    email: support@mist.com
- name: Contrail Networking API
  description: SDN controller API for cloud and NFV orchestration.
  humanURL: https://www.juniper.net/documentation/product/us/en/contrail-networking/
  baseURL: https://[contrail-controller]:8082
  tags:
  - Cloud
  - NFV
  - Orchestration
  - SDN
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/us/en/software/contrail/
  - type: GitHub
    url: https://github.com/Juniper/contrail-controller
  - type: OpenAPI
    url: openapi/juniper-contrail-openapi.yml
  contact:
  - FN: Juniper Support
    email: support@juniper.net
- name: Juniper ATP Cloud API
  description: Advanced Threat Prevention API for threat intelligence and security analytics.
  humanURL: https://www.juniper.net/us/en/products/security/advanced-threat-prevention.html
  baseURL: https://[atp-appliance]/api
  tags:
  - Analytics
  - Security
  - Threat Intelligence
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/us/en/software/atp/
  - type: OpenAPI
    url: openapi/juniper-atp-cloud-openapi.yml
  contact:
  - FN: Juniper Support
    email: support@juniper.net
- name: JSNAPy API
  description: Python-based snapshot and test framework for Junos devices.
  humanURL: https://github.com/Juniper/jsnapy
  baseURL: N/A
  tags:
  - Automation
  - Python
  - Testing
  - Validation
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/us/en/software/jsnapy/
  - type: GitHub
    url: https://github.com/Juniper/jsnapy
  contact:
  - FN: Juniper Support
    email: support@juniper.net
name: Juniper Networks
tags:
- AI
- Automation
- Cloud
- Enterprise
- Networking
- SDN
- Security
type: Contract
image: https://www.juniper.net/content/dam/www/assets/images/juniper-networks-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Juniper Networks provides high-performance networking and cybersecurity solutions for service providers, enterprises, and public sector organizations.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


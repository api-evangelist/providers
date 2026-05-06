---
name: Juniper Networks
description: Juniper Networks provides high-performance networking and cybersecurity solutions for service providers, enterprises, and public sector organizations.
url: https://www.juniper.net
image: https://www.juniper.net/content/dam/www/assets/images/juniper-networks-logo.png
created: 2024-01-15T00:00:00.000Z
modified: '2026-04-28'
specificationVersion: '0.18'
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
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - AI
  - Automation
  - Cloud
  - Enterprise
  - Networking
  - SDN
  - Security
common:
  - type: Portal
    url: https://developer.juniper.net/
  - type: Website
    url: https://www.juniper.net/
  - type: Documentation
    url: https://www.juniper.net/documentation/
  - type: Support
    url: https://support.juniper.net/
  - type: GitHub Organization
    url: https://github.com/Juniper
  - type: Community
    url: https://community.juniper.net/
  - type: Blog
    url: https://blogs.juniper.net/
  - type: Terms of Service
    url: https://www.juniper.net/us/en/legal-notices.html
  - type: Privacy Policy
    url: https://www.juniper.net/us/en/privacy-policy.html
  - type: YouTube
    url: https://www.youtube.com/user/JuniperNetworks
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/juniper
  - type: JSON-LD
    url: json-ld/juniper-context.jsonld
  - type: JSONSchema
    url: json-schema/juniper-network-device.json
  - type: JSONSchema
    url: json-schema/juniper-virtual-network.json
  - type: JSONSchema
    url: json-schema/juniper-security-threat.json
  - type: JSONSchema
    url: json-schema/juniper-site.json
  - type: JSONSchema
    url: json-schema/juniper-blueprint.json
include: []
---

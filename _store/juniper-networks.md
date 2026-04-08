---
aid: juniper-networks
url: https://raw.githubusercontent.com/api-evangelist/juniper-networks/refs/heads/main/apis.yml
apis:
- name: Juniper Apstra API
  description: Intent-based networking API for data center automation and orchestration.
  image: https://www.juniper.net/content/dam/juniper/images/products/apstra.png
  humanURL: https://www.juniper.net/documentation/product/us/en/juniper-apstra/
  baseURL: https://<apstra-server>/api
  tags:
  - Automation
  - Data Center
  - Intent-Based Networking
  - Networking
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/product/us/en/juniper-apstra/
  - type: OpenAPI
    url: openapi/juniper-networks-apstra-openapi.yml
  - type: JSONSchema
    url: json-schema/juniper-networks-apstra-blueprint-schema.json
  - type: Authentication
    url: https://www.juniper.net/documentation/us/en/software/apstra4.1/apstra-user-guide/topics/topic-map/api-authentication.html
- name: Junos PyEZ
  description: Python library for automating Junos devices using NETCONF.
  image: https://www.juniper.net/content/dam/juniper/images/logos/junos-logo.png
  humanURL: https://www.juniper.net/documentation/product/us/en/junos-pyez/
  baseURL: netconf://device:830
  tags:
  - Automation
  - Junos
  - NETCONF
  - Python
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/product/us/en/junos-pyez/
  - type: GitHub
    url: https://github.com/Juniper/py-junos-eznc
  - type: Getting Started
    url: https://www.juniper.net/documentation/us/en/software/junos-pyez/junos-pyez-developer/topics/concept/junos-pyez-overview.html
- name: Junos XML API
  description: NETCONF-based XML API for programmatic access to Junos devices.
  image: https://www.juniper.net/content/dam/juniper/images/logos/junos-logo.png
  humanURL: https://www.juniper.net/documentation/us/en/software/junos/netconf/index.html
  baseURL: netconf://device:830
  tags:
  - Automation
  - Junos
  - NETCONF
  - XML
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/us/en/software/junos/netconf/index.html
  - type: XML API Guide
    url: https://www.juniper.net/documentation/us/en/software/junos/netconf/topics/concept/netconf-xml-api-overview.html
  - type: JSONSchema
    url: json-schema/juniper-networks-junos-security-policy-schema.json
  - type: AsyncAPI
    url: asyncapi/juniper-networks-junos-telemetry-asyncapi.yml
- name: Juniper Mist API
  description: Cloud-based AI-driven networking API for wireless, wired, and SD-WAN management.
  image: https://www.mist.com/wp-content/uploads/mist-logo.png
  humanURL: https://api.mist.com/api/v1/docs/
  baseURL: https://api.mist.com/api/v1
  tags:
  - AI
  - Cloud
  - Network Management
  - SD-WAN
  - Wireless
  properties:
  - type: Documentation
    url: https://api.mist.com/api/v1/docs/
  - type: API Reference
    url: https://doc.mist-lab.fr/
  - type: Authentication
    url: https://api.mist.com/api/v1/docs/Auth.html
  - type: OpenAPI
    url: openapi/juniper-networks-mist-openapi.yml
  - type: AsyncAPI
    url: asyncapi/juniper-networks-mist-webhooks-asyncapi.yml
  - type: JSONSchema
    url: json-schema/juniper-networks-mist-site-schema.json
  - type: JSONSchema
    url: json-schema/juniper-networks-mist-device-schema.json
- name: Juniper Contrail API
  description: SDN controller API for network virtualization and orchestration.
  image: https://www.juniper.net/content/dam/juniper/images/products/contrail.png
  humanURL: https://www.juniper.net/documentation/product/us/en/contrail-networking/
  baseURL: https://<contrail-controller>:8082
  tags:
  - NFV
  - Orchestration
  - SDN
  - Virtual Networks
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/product/us/en/contrail-networking/
  - type: API Guide
    url: https://github.com/Juniper/contrail-controller/wiki/Contrail-REST-API
  - type: OpenAPI
    url: openapi/juniper-networks-contrail-openapi.yml
  - type: JSONSchema
    url: json-schema/juniper-networks-contrail-virtual-network-schema.json
- name: Junos Space REST API
  description: Network management platform API for Junos devices.
  image: https://www.juniper.net/content/dam/juniper/images/products/junos-space.png
  humanURL: https://www.juniper.net/documentation/product/us/en/junos-space-network-management-platform/
  baseURL: https://<space-server>/api/space
  tags:
  - Network Management
  - Orchestration
  - REST
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/us/en/software/junos-space/
  - type: API Developer Guide
    url: https://www.juniper.net/documentation/us/en/software/junos-space/junos-space-platform/topics/concept/junos-space-rest-api-overview.html
  - type: OpenAPI
    url: openapi/juniper-networks-junos-space-openapi.yml
- name: Juniper JSNAPy
  description: Python-based tool for snapshot and verification of network device configurations.
  image: https://www.juniper.net/content/dam/juniper/images/logos/junos-logo.png
  humanURL: https://github.com/Juniper/jsnapy
  baseURL: https://github.com/Juniper/jsnapy
  tags:
  - Automation
  - Configuration Management
  - Python
  - Testing
  properties:
  - type: GitHub
    url: https://github.com/Juniper/jsnapy
  - type: Documentation
    url: https://www.juniper.net/documentation/us/en/software/jsnapy/index.html
- name: Juniper vSRX REST API
  description: RESTful API for managing virtual firewall instances.
  image: https://www.juniper.net/content/dam/juniper/images/products/vsrx.png
  humanURL: https://www.juniper.net/documentation/product/us/en/vsrx/
  baseURL: https://<vsrx-device>/api
  tags:
  - Firewall
  - REST
  - Security
  - Virtual
  properties:
  - type: Documentation
    url: https://www.juniper.net/documentation/product/us/en/vsrx/
  - type: OpenAPI
    url: openapi/juniper-networks-vsrx-openapi.yml
name: Juniper Networks
tags:
- Automation
- Cloud
- Data Center
- Enterprise
- Networking
- SDN
- Security
type: Contract
image: https://www.juniper.net/content/dam/juniper/images/logos/juniper-networks-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs and developer resources for Juniper Networks networking products and services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


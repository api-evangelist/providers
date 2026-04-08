---
aid: geneos
url: https://raw.githubusercontent.com/api-evangelist/geneos/refs/heads/main/apis.yml
apis:
- aid: geneos:gateway-rest
  name: Geneos Gateway REST API
  description: RESTful API for interacting with Geneos Gateway to retrieve monitoring data, manage dataviews, samplers, and entities programmatically.
  humanURL: https://docs.itrsgroup.com/docs/geneos/current/Gateway_Reference_Guide/geneos_commands_tr.html
  tags:
  - Monitoring
  - REST
  properties:
  - type: Documentation
    url: https://docs.itrsgroup.com/docs/geneos/current/Gateway_Reference_Guide/gateway_rest_api.html
  - type: Authentication
    url: https://docs.itrsgroup.com/docs/geneos/current/Gateway_Reference_Guide/rest_api_authentication.html
- aid: geneos:xml-rpc
  name: Geneos XML-RPC API
  description: XML-RPC interface for programmatic control of Geneos Gateway including executing commands, managing configuration, and retrieving monitoring data.
  humanURL: https://docs.itrsgroup.com/docs/geneos/current/Gateway_Reference_Guide/geneos_xml-rpc_api.html
  tags:
  - Automation
  - XML-RPC
  properties:
  - type: Documentation
    url: https://docs.itrsgroup.com/docs/geneos/current/Gateway_Reference_Guide/geneos_xml-rpc_api.html
- aid: geneos:toolkit
  name: Geneos Toolkit API
  description: Java and Python APIs provided through Geneos Toolkit for building custom integrations, plugins, and automation scripts.
  humanURL: https://docs.itrsgroup.com/docs/geneos/current/Toolkit/toolkit.html
  tags:
  - Java
  - Python
  - SDK
  properties:
  - type: Documentation
    url: https://docs.itrsgroup.com/docs/geneos/current/Toolkit/toolkit_api.html
  - type: SDKs
    url: https://docs.itrsgroup.com/docs/geneos/current/Toolkit/java_api.html
  - type: GitHub Organization
    url: https://github.com/ITRS-Group/geneos-toolkit
name: Geneos
tags:
- APM
- Infrastructure
- Monitoring
- Observability
- Real-Time
- Trading Systems
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Geneos is ITRS's real-time monitoring platform that provides comprehensive observability for trading systems, applications, and infrastructure. It offers APIs for programmatic access to monitoring data, configuration, and automation.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


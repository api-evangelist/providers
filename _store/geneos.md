---
aid: geneos
name: Geneos
description: Geneos is ITRS Group's real-time monitoring platform that provides comprehensive observability for trading systems, applications, and infrastructure. Widely deployed across investment banks, hedge funds, and exchanges, Geneos collects high-frequency telemetry from custom samplers and toolkits, aggregates it through Gateways, and exposes that data through REST, XML-RPC, streaming, and SDK interfaces for programmatic access, automation, and dashboarding.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-01-15'
modified: '2026-04-28'
position: Consumer
url: https://raw.githubusercontent.com/api-evangelist/geneos/refs/heads/main/apis.yml
specificationVersion: '0.19'
tags:
  - APM
  - Capital Markets
  - Infrastructure
  - ITRS
  - Monitoring
  - Observability
  - Real-Time
  - Trading Systems
apis:
  - aid: geneos:gateway-rest
    name: Geneos Gateway REST API
    description: RESTful API exposed by the Geneos Gateway for retrieving monitoring data and managing dataviews, samplers, entities, and snooze states programmatically. Authenticated and typically deployed inside enterprise networks.
    humanURL: https://docs.itrsgroup.com/docs/geneos/current/Gateway_Reference_Guide/gateway_rest_api.html
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
    description: XML-RPC interface for programmatic control of Geneos Gateway including executing commands, managing configuration, publishing data into Gateways from external samplers, and retrieving monitoring data.
    humanURL: https://docs.itrsgroup.com/docs/geneos/current/Gateway_Reference_Guide/geneos_xml-rpc_api.html
    tags:
      - Automation
      - XML-RPC
    properties:
      - type: Documentation
        url: https://docs.itrsgroup.com/docs/geneos/current/Gateway_Reference_Guide/geneos_xml-rpc_api.html
  - aid: geneos:web-dashboard
    name: Geneos Web Dashboard API
    description: API for integrating with the Geneos Web Dashboard, enabling custom dashboards, data visualization, and user interface extensions on top of Geneos monitoring data.
    humanURL: https://docs.itrsgroup.com/docs/geneos/current/Web_Dashboard/web-dashboard.html
    tags:
      - Dashboard
      - UI
      - Visualization
      - Web
    properties:
      - type: Documentation
        url: https://docs.itrsgroup.com/docs/geneos/current/Web_Dashboard/web-dashboard.html
  - aid: geneos:toolkit
    name: Geneos Toolkit API
    description: Java and Python APIs delivered through the Geneos Toolkit for building custom integrations, samplers, plugins, and automation scripts that publish data into and pull data out of Geneos.
    humanURL: https://docs.itrsgroup.com/docs/geneos/current/Toolkit/toolkit.html
    tags:
      - Java
      - Python
      - SDK
    properties:
      - type: Documentation
        url: https://docs.itrsgroup.com/docs/geneos/current/Toolkit/toolkit.html
      - type: SDK
        url: https://github.com/ITRS-Group/geneos-toolkit
      - type: GitHubOrganization
        url: https://github.com/ITRS-Group
common:
  - type: Website
    url: https://www.itrsgroup.com/
  - type: ProductPage
    url: https://www.itrsgroup.com/products/geneos
  - type: Documentation
    url: https://docs.itrsgroup.com/docs/geneos/
  - type: Support
    url: https://www.itrsgroup.com/support
  - type: Community
    url: https://community.itrsgroup.com/
  - type: KnowledgeBase
    url: https://kb.itrsgroup.com/
  - type: Training
    url: https://www.itrsgroup.com/training
  - type: Contact
    url: https://www.itrsgroup.com/contact
  - type: TermsOfService
    url: https://www.itrsgroup.com/terms
  - type: PrivacyPolicy
    url: https://www.itrsgroup.com/privacy
  - type: GitHubOrganization
    url: https://github.com/ITRS-Group
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

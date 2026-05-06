---
name: Azure Traffic Manager
description: Azure Traffic Manager is a DNS-based traffic load balancer that enables you to distribute traffic optimally to services across global Azure regions, while providing high availability and responsiveness. It supports configurable routing methods including priority, weighted, performance, geographic, multivalue, and subnet routing.
image: https://azure.microsoft.com/svghandler/traffic-manager/
tags:
  - DNS Load Balancing
  - Failover
  - Global Routing
  - Networking
  - Traffic Distribution
  - Traffic Manager
created: '2026-03-13'
modified: '2026-04-28'
url: https://azure.microsoft.com/en-us/services/traffic-manager/
specificationVersion: '0.18'
apis:
  - name: Azure Traffic Manager Profiles REST API
    description: REST API for creating, configuring, and managing Traffic Manager profiles. Profiles define the global DNS-based load balancing configuration including routing method, monitoring settings, and the collection of endpoints participating in the profile.
    image: https://azure.microsoft.com/svghandler/traffic-manager/
    humanURL: https://learn.microsoft.com/en-us/rest/api/trafficmanager/profiles
    baseURL: https://management.azure.com
    tags:
      - Profiles
      - Routing
      - Traffic Manager
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/trafficmanager/profiles
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/trafficmanager/resource-manager/Microsoft.Network/stable/2022-04-01/trafficmanager.json
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/trafficmanager/profiles?view=rest-trafficmanager-2022-04-01
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/traffic-manager/quickstart-create-traffic-manager-profile
  - name: Azure Traffic Manager Endpoints REST API
    description: REST API for managing endpoints within a Traffic Manager profile. Supports adding, updating, and removing Azure, external, and nested endpoints that receive traffic according to the profile's routing method and health monitoring configuration.
    image: https://azure.microsoft.com/svghandler/traffic-manager/
    humanURL: https://learn.microsoft.com/en-us/rest/api/trafficmanager/endpoints
    baseURL: https://management.azure.com
    tags:
      - Endpoints
      - Health Monitoring
      - Traffic Manager
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/trafficmanager/endpoints
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/trafficmanager/endpoints?view=rest-trafficmanager-2022-04-01
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-endpoint-types
  - name: Azure Traffic Manager Heatmap REST API
    description: REST API for retrieving Traffic Manager heatmap data, which provides geographic visualization of DNS query volumes and endpoint selection by region. Useful for analyzing traffic distribution and routing decisions across the global user base.
    image: https://azure.microsoft.com/svghandler/traffic-manager/
    humanURL: https://learn.microsoft.com/en-us/rest/api/trafficmanager/heat-map
    baseURL: https://management.azure.com
    tags:
      - Analytics
      - Heatmap
      - Traffic Analytics
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/trafficmanager/heat-map
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/trafficmanager/heat-map/get?view=rest-trafficmanager-2022-04-01
  - name: Azure Traffic Manager User Metrics REST API
    description: REST API for managing real user measurements (RUM) keys used by Traffic Manager performance routing. User metrics enable Traffic Manager to make more accurate latency-based routing decisions using telemetry from end users.
    image: https://azure.microsoft.com/svghandler/traffic-manager/
    humanURL: https://learn.microsoft.com/en-us/rest/api/trafficmanager/traffic-manager-user-metrics-keys
    baseURL: https://management.azure.com
    tags:
      - Performance
      - Real User Measurements
      - User Metrics
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/trafficmanager/traffic-manager-user-metrics-keys
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/trafficmanager/traffic-manager-user-metrics-keys?view=rest-trafficmanager-2022-04-01
  - name: Azure Traffic Manager Geographic Hierarchies REST API
    description: REST API for retrieving the geographic hierarchy used by Traffic Manager for geographic routing. Returns the supported regions, countries, and subdivisions that can be configured as endpoint geo-mappings within geographic routing profiles.
    image: https://azure.microsoft.com/svghandler/traffic-manager/
    humanURL: https://learn.microsoft.com/en-us/rest/api/trafficmanager/geographic-hierarchies
    baseURL: https://management.azure.com
    tags:
      - Geographic Hierarchy
      - Geographic Routing
      - Regions
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/trafficmanager/geographic-hierarchies
      - type: Reference
        url: https://learn.microsoft.com/en-us/rest/api/trafficmanager/geographic-hierarchies/get-default?view=rest-trafficmanager-2022-04-01
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Website
    url: https://azure.microsoft.com/en-us/products/traffic-manager
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/traffic-manager/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/traffic-manager/quickstart-create-traffic-manager-profile
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-scenarios
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/traffic-manager/
  - type: SLA
    url: https://azure.microsoft.com/en-us/support/legal/sla/traffic-manager/
  - type: Status
    url: https://status.azure.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/topics/networking/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/options/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Sign Up
    url: https://azure.microsoft.com/en-us/free
  - type: Login
    url: https://portal.azure.com
  - type: SDKs
    url: https://azure.microsoft.com/en-us/downloads/
  - type: SDK - Python
    url: https://pypi.org/project/azure-mgmt-trafficmanager/
  - type: SDK - .NET
    url: https://www.nuget.org/packages/Azure.ResourceManager.TrafficManager
  - type: SDK - JavaScript
    url: https://www.npmjs.com/package/@azure/arm-trafficmanager
  - type: SDK - Java
    url: https://learn.microsoft.com/en-us/java/api/overview/azure/resourcemanager-trafficmanager-readme
  - type: CLI Tools
    url: https://learn.microsoft.com/en-us/cli/azure/network/traffic-manager
  - type: Change Log
    url: https://azure.microsoft.com/en-us/updates/?product=traffic-manager
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: GitHub REST API Specs
    url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/trafficmanager
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azure-traffic-manager
  - type: Community
    url: https://learn.microsoft.com/en-us/answers/tags/175/azure-traffic-manager
  - type: FAQ
    url: https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-FAQs
  - type: Training
    url: https://learn.microsoft.com/en-us/training/modules/distribute-load-with-traffic-manager/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

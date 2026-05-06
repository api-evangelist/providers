---
aid: cisco-systems
name: Cisco Systems
url: https://raw.githubusercontent.com/api-evangelist/cisco-systems/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-04'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
tags:
  - Collaboration
  - Infrastructure
  - Networking
  - Security
description: Cisco Systems is a global technology company providing networking, security, collaboration, and cloud infrastructure products. Cisco exposes its programmable surface through Cisco DevNet, a single developer portal that aggregates documentation, sandboxes, code exchange, and learning labs across the company's hardware and software portfolio. Major API domains include Catalyst Center and Meraki for network management, IOS XE RESTCONF for device-level programmability, Webex for collaboration, Secure Firewall and ISE for security, ThousandEyes and AppDynamics for observability, and Intersight for cloud-managed infrastructure. Authentication models vary by product line and include OAuth 2.0, API keys, basic-auth token exchange, and HTTP signature authentication.
apis:
  - aid: cisco-systems:devnet-api
    name: Cisco DevNet API Catalog
    tags:
      - Collaboration
      - DevNet
      - Infrastructure
      - Networking
      - Security
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://developer.cisco.com/api
    humanURL: https://developer.cisco.com/
    properties:
      - url: https://developer.cisco.com/
        type: Documentation
      - url: https://developer.cisco.com/docs/
        type: API Reference
      - url: openapi/cisco-systems-cisco-api-openapi.yml
        type: OpenAPI
    description: Cisco DevNet is the unified developer portal for Cisco Systems products, exposing APIs, SDKs, sandboxes, and learning resources for networking, security, collaboration, and cloud infrastructure. The DevNet catalog is the entry point for discovering and authenticating against the broader Cisco API surface.
  - aid: cisco-systems:catalyst-center
    name: Cisco Catalyst Center
    tags:
      - Catalyst
      - DNA Center
      - Network Management
      - SDN
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cisco.com/docs/dna-center/
    properties:
      - url: https://developer.cisco.com/docs/dna-center/
        type: Documentation
    description: Cisco Catalyst Center (formerly Cisco DNA Center) provides programmable management of Cisco enterprise networks, including discovery, inventory, provisioning, and assurance.
  - aid: cisco-systems:meraki
    name: Cisco Meraki Dashboard
    tags:
      - Cloud Managed
      - Dashboard
      - Wireless
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.meraki.com/api/v1
    humanURL: https://developer.cisco.com/meraki/
    properties:
      - url: https://developer.cisco.com/meraki/api-latest/
        type: Documentation
      - url: https://api.meraki.com/api/v1/openapiSpec
        type: OpenAPI
    description: The Meraki Dashboard API exposes Cisco's cloud-managed networking hardware including switches, access points, security appliances, cameras, and sensors.
  - aid: cisco-systems:webex
    name: Cisco Webex Platform
    tags:
      - Collaboration
      - Meetings
      - Messaging
      - Webex
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://webexapis.com/v1
    humanURL: https://developer.webex.com/
    properties:
      - url: https://developer.webex.com/docs
        type: Documentation
    description: The Cisco Webex platform provides REST APIs for meetings, messaging, calling, devices, webhooks, and administrative operations across the Webex collaboration suite.
  - aid: cisco-systems:secure-firewall
    name: Cisco Secure Firewall Management Center
    tags:
      - Firewall
      - FTD
      - Security
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cisco.com/docs/secure-firewall-management-center-api/
    properties:
      - url: https://developer.cisco.com/docs/secure-firewall-management-center-api/
        type: Documentation
    description: The Cisco Secure Firewall Management Center API configures ASA/FTD firewall policies, access rules, and remote-access VPN gateways across managed firewall fleets.
  - aid: cisco-systems:thousandeyes
    name: Cisco ThousandEyes API
    tags:
      - Digital Experience
      - Network Monitoring
      - Observability
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.thousandeyes.com/v7
    humanURL: https://developer.thousandeyes.com/
    properties:
      - url: https://developer.thousandeyes.com/v7/
        type: Documentation
    description: The Cisco ThousandEyes API provides programmatic access to digital experience, internet, and cloud network monitoring data across enterprise environments.
  - aid: cisco-systems:appdynamics
    name: Cisco AppDynamics API
    tags:
      - APM
      - Application Monitoring
      - Observability
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.appdynamics.com/appd/24.x/latest/en/extend-cisco-appdynamics
    properties:
      - url: https://docs.appdynamics.com/appd/24.x/latest/en/extend-cisco-appdynamics
        type: Documentation
    description: The Cisco AppDynamics API provides REST endpoints for application performance monitoring, business transaction analytics, and controller administration.
  - aid: cisco-systems:intersight
    name: Cisco Intersight API
    tags:
      - Cloud Management
      - HyperFlex
      - Infrastructure
      - UCS
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://intersight.com/api/v1
    humanURL: https://intersight.com/apidocs/
    properties:
      - url: https://intersight.com/apidocs/introduction/overview/
        type: Documentation
    description: The Cisco Intersight API is a cloud-based control plane for managing Cisco UCS, HyperFlex, and partner infrastructure with OData-flavored REST endpoints.
common:
  - type: Website
    url: https://www.cisco.com
  - type: Portal
    url: https://developer.cisco.com/
  - type: Documentation
    url: https://developer.cisco.com/docs/
  - type: Sandbox
    url: https://devnetsandbox.cisco.com/
  - type: Learning
    url: https://developer.cisco.com/learning/
  - type: Code Exchange
    url: https://developer.cisco.com/codeexchange/
  - type: Community
    url: https://community.cisco.com/
  - type: Support
    url: https://www.cisco.com/c/en/us/support/index.html
  - type: Status
    url: https://status.cisco.com/
  - type: Blog
    url: https://blogs.cisco.com/
  - type: Terms of Service
    url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end-user-license-agreement.html
  - type: Privacy Policy
    url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
  - type: JSON-LD
    url: json-ld/cisco-systems-context.jsonld
  - type: Spectral
    url: rules/cisco-systems-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cisco-systems-capabilities.yml
  - type: Features
    data:
      - 'Cisco Systems: hundreds of services across Networking + Security'
      - 'Detailed pricing: see https://www.cisco.com/c/en/us/products/index.html'
      - 'Service: Meraki Dashboard API'
      - 'Service: Webex API'
      - 'Service: Catalyst SDK'
      - 'Service: DNA Center API'
    sources:
      - https://www.cisco.com/c/en/us/products/index.html
      - https://focus.finops.org/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

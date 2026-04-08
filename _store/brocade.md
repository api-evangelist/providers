---
aid: brocade
url: https://raw.githubusercontent.com/api-evangelist/brocade/refs/heads/main/apis.yml
apis:
- name: Brocade Fabric OS REST API
  description: The Brocade Fabric OS REST API provides a programmable web-service interface for managing Brocade SAN switches across a fabric. It supports YANG-based modules for configuring and monitoring switch resources including chassis, ports, zoning, security, logging, MAPS, and Fibre Channel features. Supported on Fabric OS 8.2.0 and later.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://techdocs.broadcom.com/us/en/fibre-channel-networking/fabric-os/fabric-os-rest-api/9-2-x.html
  baseURL: https://{switch-ip}/rest
  tags:
  - Fabric OS
  - Fibre Channel
  - Network Management
  - SAN
  - Switches
  properties:
  - type: Documentation
    url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/fabric-os/fabric-os-rest-api/9-2-x.html
  - type: Reference
    url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/fabric-os/fabric-os-rest-api/10-0-x.html
  - type: Authentication
    url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/fabric-os/fabric-os-rest-api/9-2-x/v26395730/v24190001.html
  - type: Getting Started
    url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/fabric-os/fabric-os-rest-api/9-2-x/v26395730/v24190001.html
  - type: SDKs
    url: https://github.com/brocade/pyfos
- name: Brocade SANnav Management Portal REST API
  description: The Brocade SANnav Management Portal REST API provides a programmable web-service interface for accessing and managing the SANnav Management Portal server. REST API services include Login, Discovery, FCR, Fault, Inventory, Health Summary, User Management, RBAC, Zoning, and Proxy to Fabric OS REST API. SANnav is the successor to Brocade Network Advisor for SAN management.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://techdocs.broadcom.com/us/en/fibre-channel-networking/sannav/management-portal-rest-api/3-0-0x.html
  baseURL: https://{sannav-host}/external-api/v1
  tags:
  - Discovery
  - Fibre Channel
  - Monitoring
  - SAN Management
  - Zoning
  properties:
  - type: Documentation
    url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/sannav/management-portal-rest-api/3-0-0x.html
  - type: Reference
    url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/sannav/management-portal-rest-api/3-0-0x/SANnav-Overview.html
  - type: Getting Started
    url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/sannav/management-portal-rest-api/3-0-0x/SANnav-Overview.html
- name: Brocade SANnav Northbound Streaming API
  description: The Brocade SANnav Northbound Streaming API enables real-time streaming of SAN telemetry and event data from the SANnav Management Portal to external systems. It provides northbound streaming of fault events, performance metrics, and inventory changes for integration with third-party monitoring and analytics platforms.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://techdocs.broadcom.com/us/en/fibre-channel-networking/sannav/management-portal-rest-api-and-nb-streaming/2-3-0x.html
  baseURL: https://{sannav-host}/external-api/v1/stream
  tags:
  - Events
  - Monitoring
  - SAN Management
  - Streaming
  - Telemetry
  properties:
  - type: Documentation
    url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/sannav/management-portal-rest-api-and-nb-streaming/2-3-0x.html
  - type: Reference
    url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/sannav/management-portal-rest-api/2-4-0x/Resources-REST-API/Stream-REST-API/GET--external-api-v1-stream-servers-REST-API.html
- name: Brocade Network Advisor REST API
  description: The Brocade Network Advisor REST API provided a web-services interface for configuring and monitoring Brocade SAN switches, including fabric management, topology, zoning, and performance data retrieval. Network Advisor reached end of life in March 2019 and has been replaced by SANnav Management Portal.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://docs.broadcom.com/doc/12395099
  baseURL: https://{bna-host}/rest
  tags:
  - Analytics
  - Deprecated
  - Monitoring
  - SAN Management
  properties:
  - type: Documentation
    url: https://docs.broadcom.com/doc/12395099
  - type: Deprecation Notice
    url: https://docs.broadcom.com/doc/12395099
- name: Brocade Workflow Composer API
  description: The Brocade Workflow Composer was a network automation platform based on StackStorm for event-driven automation and orchestration workflows. The product was transferred to Extreme Networks as part of the IP networking business acquisition and is now known as Extreme Workflow Composer.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://bwc-docs.brocade.com/
  baseURL: https://{bwc-host}/api/v1
  tags:
  - Automation
  - Deprecated
  - Orchestration
  - Workflow
  properties:
  - type: Documentation
    url: https://bwc-docs.brocade.com/
- name: Brocade VCS Fabric API
  description: The Brocade VCS Fabric API provided REST interfaces for Virtual Cluster Switching fabric configuration on Brocade VDX switches. The VCS Fabric product line was transferred to Extreme Networks as part of the data center networking business acquisition and is no longer part of the Broadcom Brocade portfolio.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://www.extremenetworks.com/support/end-of-sale-and-end-of-support-products
  baseURL: https://{switch-ip}/rest
  tags:
  - Deprecated
  - Fabric
  - Switching
  - VCS
  properties:
  - type: Documentation
    url: https://www.extremenetworks.com/support/end-of-sale-and-end-of-support-products
  - type: Deprecation Notice
    url: https://www.extremenetworks.com/support/end-of-sale-and-end-of-support-products
name: Brocade
tags:
- Data Center
- Directors
- Fibre Channel
- Network Automation
- Networking
- SAN
- Storage Area Networks
- Switches
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Brocade, now part of Broadcom, provides Fibre Channel networking solutions for storage area networks (SANs). The Brocade portfolio includes SAN switches, directors, Fabric OS software, and the SANnav management platform, all offering REST APIs for programmable management and automation of SAN infrastructure.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


---
aid: brocade-communications-systems
name: Brocade Communications Systems
url: https://raw.githubusercontent.com/api-evangelist/brocade-communications-systems/refs/heads/main/apis.yml
description: Brocade Communications Systems was a provider of data networking and storage networking products and services, including SAN switches, IP networking equipment, routers, and network management software for enterprises and service providers. Brocade was acquired by Broadcom in 2017. The IP networking business was sold to Extreme Networks, while the Fibre Channel SAN portfolio was retained by Broadcom under the Brocade brand.
tags:
  - Data Networking
  - Fibre Channel
  - IP Networking
  - Networking
  - SAN
  - Storage Networking
  - Switches
x-type: company
apis:
  - aid: brocade-communications-systems:fabric-os-rest-api
    name: Brocade Fabric OS REST API
    description: The Brocade Fabric OS REST API provides programmable management of Brocade SAN switches and directors running Fabric OS. YANG-based REST modules support chassis, port, zoning, security, and performance configuration and monitoring for Fibre Channel SAN environments.
    humanURL: https://techdocs.broadcom.com/us/en/fibre-channel-networking/fabric-os/fabric-os-rest-api/9-2-x.html
    baseURL: https://{switch-ip}/rest
    tags:
      - Fabric OS
      - Fibre Channel
      - Network Management
      - SAN
    properties:
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/fabric-os/fabric-os-rest-api/9-2-x.html
      - type: GettingStarted
        url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/fabric-os/fabric-os-rest-api/9-2-x/v26395730/v24190001.html
  - aid: brocade-communications-systems:sannav-rest-api
    name: Brocade SANnav Management Portal REST API
    description: The Brocade SANnav Management Portal REST API provides programmable access to the SANnav SAN management platform. REST services include discovery, inventory, fault management, health summary, user management, zoning, and proxy to Fabric OS REST API.
    humanURL: https://techdocs.broadcom.com/us/en/fibre-channel-networking/sannav/management-portal-rest-api/3-0-0x.html
    baseURL: https://{sannav-host}/external-api/v1
    tags:
      - Monitoring
      - SAN Management
      - SANnav
      - Zoning
    properties:
      - type: Documentation
        url: https://techdocs.broadcom.com/us/en/fibre-channel-networking/sannav/management-portal-rest-api/3-0-0x.html
common:
  - type: Website
    url: https://www.broadcom.com/products/fibre-channel-networking
  - type: Documentation
    url: https://techdocs.broadcom.com/us/en/fibre-channel-networking.html
  - type: Portal
    url: https://techdocs.broadcom.com/us/en/fibre-channel-networking.html
  - type: Support
    url: https://www.broadcom.com/support/fibre-channel-networking
  - type: TermsOfService
    url: https://www.broadcom.com/company/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://www.broadcom.com/company/legal/privacy/policy
  - type: GitHubOrg
    url: https://github.com/brocade
  - type: Community
    url: https://community.broadcom.com/t5/Fibre-Channel-SAN-Forums/bd-p/fibre
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
created: '2026-03-23'
modified: '2026-04-21'
specificationVersion: '0.19'
---

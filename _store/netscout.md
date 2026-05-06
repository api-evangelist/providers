---
aid: netscout
name: Netscout
description: Netscout provides service assurance, cybersecurity, and DDoS protection solutions. Their products enable network visibility, threat intelligence, and performance monitoring across hybrid and cloud environments. Several Netscout products expose REST APIs and integration interfaces for observability, security automation, and analytics workflows.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/netscout/refs/heads/main/apis.yml
created: '2025-01-20'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Cybersecurity
  - DDoS Protection
  - Network Monitoring
  - Network Performance
  - Service Assurance
  - Threat Intelligence
apis:
  - aid: netscout:ngeniusone
    name: Netscout nGeniusONE API
    description: RESTful interface for the nGeniusONE platform, enabling network performance monitoring, analytics, and service assurance automation.
    humanURL: https://www.netscout.com/product/ngenius-one
    tags:
      - Analytics
      - Monitoring
      - Network Performance
      - Service Assurance
    properties:
      - type: Documentation
        url: https://www.netscout.com/product/ngenius-one
      - type: Reference
        url: https://www.netscout.com/product/ngeniusone-solution
    contact:
      - FN: Netscout Support
        url: https://www.netscout.com/support-services
  - aid: netscout:arbor-sightline
    name: Netscout Arbor Sightline SP REST API
    description: REST API for DDoS detection, mitigation, and threat intelligence on the Arbor Sightline platform. Provides programmatic access to alerts, mitigations, routers, managed objects, and annotations via a JSON:API-style REST interface, with cookbook examples and tutorials maintained on GitHub.
    humanURL: https://www.netscout.com/product/arbor-sightline
    tags:
      - DDoS Protection
      - Security
      - SIEM Integration
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://www.netscout.com/product/arbor-sightline
      - type: Getting Started
        url: https://arbor.github.io/sp-rest-api-cookbook/sp-rest-api-tutorial.html
      - type: GitHubRepository
        url: https://github.com/arbor/sp-rest-api-cookbook
  - aid: netscout:omnis-cyber-intelligence
    name: Netscout Omnis Cyber Intelligence API
    description: Open API surface for the Omnis Cyber Intelligence NDR platform, enabling network investigation and adding network context to third-party alerts from SIEM and EDR systems using historical network metadata and packet data.
    humanURL: https://www.netscout.com/product/cyber-intelligence
    tags:
      - Attack Detection
      - Cybersecurity
      - IOC
      - Network Detection and Response
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://www.netscout.com/product/cyber-intelligence
      - type: Reference
        url: https://www.netscout.com/resources/data-sheets/omnis-cyberstream-and-omnis-cyber-intelligence
  - aid: netscout:infinistreamng
    name: Netscout InfiniStreamNG API
    description: Programmatic interface to deep packet inspection data and network flow analytics from InfiniStreamNG appliances. Feeds ASI Smart Data metadata to analytics stacks for service assurance, application performance management, cybersecurity, and business intelligence.
    humanURL: https://www.netscout.com/product/isng-platform
    tags:
      - Deep Packet Inspection
      - Network Flow
      - Packet Analysis
      - Service Assurance
    properties:
      - type: Documentation
        url: https://www.netscout.com/product/isng-platform
      - type: Reference
        url: https://www.netscout.com/resources/data-sheets/infinistream-platform
  - aid: netscout:arbor-edge-defense
    name: Netscout Arbor Edge Defense API
    description: REST API for Arbor Edge Defense (AED), an inline security appliance deployed at the network perimeter that provides stateless, on-premises DDoS protection. Enables programmatic management of inbound and outbound block/allow lists, protection groups, and mitigation policies, with integration via REST, STIX/TAXII, and Syslog. An Ansible collection is published for automation.
    humanURL: https://www.netscout.com/product/arbor-aed-aem
    tags:
      - DDoS Protection
      - Inline Defense
      - Network Security
      - Threat Mitigation
    properties:
      - type: Documentation
        url: https://www.netscout.com/product/arbor-aed-aem
      - type: Reference
        url: https://www.netscout.com/resources/data-sheets/netscout-aed-and-aem
      - type: GitHubRepository
        url: https://github.com/arbor/aedansible
  - aid: netscout:arbor-tms
    name: Netscout Arbor Threat Mitigation System API
    description: API for the Arbor Threat Mitigation System (TMS), the carrier-class DDoS mitigation solution that works with Arbor Sightline to surgically remove DDoS attack traffic from network flows. Provides programmatic control of mitigation operations, countermeasure configuration, and attack response automation.
    humanURL: https://www.netscout.com/product/arbor-threat-mitigation-system
    tags:
      - Attack Response
      - DDoS Mitigation
      - Network Security
      - Threat Management
    properties:
      - type: Documentation
        url: https://www.netscout.com/product/arbor-threat-mitigation-system
      - type: Reference
        url: https://www.netscout.com/resources/data-sheets/arbor-threat-mitigation-system-tms
  - aid: netscout:ngeniuspulse
    name: Netscout nGeniusPULSE API
    description: API surface for nGeniusPULSE, Netscout's synthetic testing and active monitoring platform. nGeniusPULSE uses nPoint test agents deployed across LAN, WAN, Wi-Fi, VPN, data centers, and cloud environments to run scheduled and on-demand tests for HTTP/HTTPS, DNS, DHCP, ICMP, TCP, and voice/collaboration transactions.
    humanURL: https://www.netscout.com/product/ngeniuspulse
    tags:
      - Active Testing
      - Application Performance
      - Network Testing
      - Synthetic Monitoring
    properties:
      - type: Documentation
        url: https://www.netscout.com/product/ngeniuspulse
      - type: Reference
        url: https://www.netscout.com/demo/application-and-infrastructure-health
  - aid: netscout:ngenius-business-analytics
    name: Netscout nGenius Business Analytics API
    description: REST and Kafka interfaces for the nGenius Business Analytics platform, enabling service providers to export enriched ASI Smart Data to third-party data lakes, applications, and analytics platforms for business intelligence and data monetization.
    humanURL: https://www.netscout.com/product/ngenius-business-analytics
    tags:
      - Business Analytics
      - Data Streaming
      - Kafka
      - Service Provider
      - Smart Data
    properties:
      - type: Documentation
        url: https://www.netscout.com/product/ngenius-business-analytics
      - type: Reference
        url: https://www.netscout.com/resources/data-sheets/ngenius-business-analytics
common:
  - type: Portal
    url: https://my.netscout.com/Pages/overview.aspx
  - type: Documentation
    url: https://www.netscout.com/resources
  - type: Terms of Service
    url: https://www.netscout.com/legal/terms-and-conditions
  - type: Website Terms of Use
    url: https://www.netscout.com/legal/website-terms-of-use
  - type: Privacy Policy
    url: https://www.netscout.com/legal/privacy-policy
  - type: Legal
    url: https://www.netscout.com/legal
  - type: Contact
    url: https://www.netscout.com/contact-us
  - type: Blog
    url: https://www.netscout.com/blog
  - type: Support
    url: https://www.netscout.com/support-services
  - type: Website
    url: https://www.netscout.com
  - type: Login
    url: https://my.netscout.com/Pages/overview.aspx
  - type: GitHub Organization
    url: https://github.com/arbor
  - type: Security
    url: https://www.netscout.com/data-privacy-and-trust-center
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

---
aid: netscout
url: https://raw.githubusercontent.com/api-evangelist/netscout/refs/heads/main/apis.yml
apis:
- name: Netscout nGeniusONE API
  description: RESTful API for programmatic access to nGeniusONE platform data, enabling network performance monitoring, analytics, and service assurance automation.
  image: https://www.netscout.com/sites/default/files/ngenius-one-logo.png
  humanURL: https://www.netscout.com/product/ngenius-one
  baseURL: https://api.netscout.com/ngenius
  tags:
  - Analytics
  - Monitoring
  - Network Performance
  - Service Assurance
  properties:
  - type: Documentation
    url: https://www.netscout.com/support/documentation
  - type: OpenAPI
    url: https://api.netscout.com/ngenius/openapi.json
  - type: Authentication
    url: https://www.netscout.com/support/api-authentication
  - type: Reference
    url: https://www.netscout.com/product/ngeniusone-solution
  contact:
  - FN: Netscout API Support
    email: support@netscout.com
    url: https://www.netscout.com/support
- name: Netscout Arbor Sightline API
  description: API for DDoS detection, mitigation, and threat intelligence. Provides programmatic access to Arbor Sightline data for security automation and integration with SIEM and orchestration platforms. Supports alerts, mitigations, routers, managed objects, and annotations via a JSON:API compliant REST interface.
  image: https://www.netscout.com/sites/default/files/arbor-logo.png
  humanURL: https://www.netscout.com/product/arbor-sightline
  baseURL: https://api.netscout.com/arbor
  tags:
  - DDoS Protection
  - Security
  - SIEM Integration
  - Threat Intelligence
  properties:
  - type: Documentation
    url: https://www.netscout.com/support/arbor-api-guide
  - type: OpenAPI
    url: https://api.netscout.com/arbor/openapi.json
  - type: Swagger UI
    url: https://api.netscout.com/arbor/swagger
  - type: Authentication
    url: https://www.netscout.com/support/api-authentication
  - type: Getting Started
    url: https://arbor.github.io/sp-rest-api-cookbook/sp-rest-api-tutorial.html
  - type: GitHubRepository
    url: https://github.com/arbor/sp-rest-api-cookbook
  contact:
  - FN: Netscout Arbor Support
    email: arbor-support@netscout.com
    url: https://www.netscout.com/arbor/support
- name: Netscout Omnis Cyber Intelligence API
  description: API for accessing threat intelligence data, including indicators of compromise, attack patterns, and security analytics from the Omnis Cyber Intelligence NDR platform. The open API enables network investigation and adds network context to third-party alerts from SIEM and EDR systems using historical network metadata and packet data.
  image: https://www.netscout.com/sites/default/files/netscout-logo.png
  humanURL: https://www.netscout.com/product/cyber-intelligence
  baseURL: https://api.netscout.com/omnis
  tags:
  - Attack Detection
  - Cybersecurity
  - IOC
  - Network Detection and Response
  - Threat Intelligence
  properties:
  - type: Documentation
    url: https://www.netscout.com/support/omnis-api-docs
  - type: OpenAPI
    url: https://api.netscout.com/omnis/openapi.json
  - type: Rate Limits
    url: https://www.netscout.com/support/api-rate-limits
  - type: Reference
    url: https://www.netscout.com/resources/data-sheets/omnis-cyberstream-and-omnis-cyber-intelligence
  contact:
  - FN: Netscout Security Team
    email: security@netscout.com
- name: Netscout InfiniStreamNG API
  description: API for accessing deep packet inspection data and network flow analytics from InfiniStreamNG appliances. InfiniStreamNG provides borderless enterprise visibility needed to manage business services, feeding ASI Smart Data metadata to analytics stacks for service assurance, application performance management, cybersecurity, and business intelligence.
  image: https://www.netscout.com/sites/default/files/netscout-logo.png
  humanURL: https://www.netscout.com/product/isng-platform
  baseURL: https://api.netscout.com/infinistream
  tags:
  - Deep Packet Inspection
  - Network Flow
  - Packet Analysis
  - Service Assurance
  properties:
  - type: Documentation
    url: https://www.netscout.com/support/infinistream-api
  - type: SDK
    url: https://github.com/netscout/infinistream-sdk
  - type: Reference
    url: https://www.netscout.com/resources/data-sheets/infinistream-platform
  contact:
  - FN: InfiniStream Support
    email: infinistream-support@netscout.com
- name: Netscout Arbor Edge Defense API
  description: REST API for Netscout Arbor Edge Defense (AED), an inline security appliance deployed at the network perimeter that provides stateless, on-premises DDoS protection. The API enables programmatic management of inbound and outbound block and allow lists, protection groups, and mitigation policies. Supports integration with SIEM, SOAR, and XDR platforms via REST, STIX/TAXII, and Syslog.
  image: https://www.netscout.com/sites/default/files/netscout-logo.png
  humanURL: https://www.netscout.com/product/arbor-aed-aem
  baseURL: https://api.netscout.com/aed
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
  contact:
  - FN: Netscout Security Support
    email: support@netscout.com
    url: https://www.netscout.com/support-services
- name: Netscout Arbor Sightline Threat Mitigation System API
  description: API for the Arbor Threat Mitigation System (TMS), the carrier-class DDoS mitigation solution that works in conjunction with Arbor Sightline to surgically remove DDoS attack traffic from network flows. Provides programmatic control of mitigation operations, countermeasure configuration, and attack response automation.
  image: https://www.netscout.com/sites/default/files/netscout-logo.png
  humanURL: https://www.netscout.com/product/arbor-threat-mitigation-system
  baseURL: https://api.netscout.com/tms
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
  contact:
  - FN: Netscout Security Support
    email: support@netscout.com
    url: https://www.netscout.com/support-services
- name: Netscout nGeniusPULSE API
  description: API for nGeniusPULSE, Netscout's synthetic testing and active monitoring platform. nGeniusPULSE uses nPoint test agents deployed across LAN, WAN, Wi-Fi, VPN, data centers, and cloud environments to run scheduled and on-demand tests for HTTP/HTTPS, DNS, DHCP, ICMP, TCP, and voice/collaboration transactions, providing measurements for reachability, response time, and service quality.
  image: https://www.netscout.com/sites/default/files/netscout-logo.png
  humanURL: https://www.netscout.com/product/ngeniuspulse
  baseURL: https://api.netscout.com/pulse
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
  contact:
  - FN: Netscout Support
    email: support@netscout.com
    url: https://www.netscout.com/support-services
- name: Netscout nGenius Business Analytics API
  description: REST and Kafka APIs for the nGenius Business Analytics platform, enabling service providers to export enriched ASI Smart Data to third-party data lakes, applications, and analytics platforms. Industry-standard Kafka and REST APIs enable secure, scalable, and fault-tolerant delivery of network performance, subscriber, and service quality data for business intelligence and data monetization.
  image: https://www.netscout.com/sites/default/files/netscout-logo.png
  humanURL: https://www.netscout.com/product/ngenius-business-analytics
  baseURL: https://api.netscout.com/nba
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
  contact:
  - FN: Netscout Support
    email: support@netscout.com
    url: https://www.netscout.com/support-services
name: Netscout
tags:
- Cybersecurity
- DDoS Protection
- Network Monitoring
- Network Performance
- Service Assurance
- Threat Intelligence
type: Contract
image: https://www.netscout.com/sites/default/files/netscout-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Netscout provides service assurance, cybersecurity, and DDoS protection solutions. Their APIs enable network visibility, threat intelligence, and performance monitoring across hybrid and cloud environments.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


---
aid: druva
name: Druva
description: Druva is a cloud data protection and management platform providing SaaS backup, disaster recovery, and data governance for endpoints, data centers, and SaaS applications. Druva exposes a public REST API across its Cyber Resilience, Endpoint Data Governance, Enterprise Workloads, CloudRanger, MSP, and Legal Hold products, using token-based authentication and JSON over HTTPS.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Backup
  - Cyber Resilience
  - Data Protection
  - Disaster Recovery
  - SaaS Backup
url: https://raw.githubusercontent.com/api-evangelist/druva/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: druva:cyber-resilience
    name: Druva Cyber Resilience API
    description: The Druva Cyber Resilience REST API provides programmatic access to reports and events across the Druva Data Resiliency Cloud, supporting ransomware recovery, anomaly detection, and security posture monitoring.
    humanURL: https://developer.druva.com
    baseURL: https://apis.druva.com
    tags:
      - Cyber Resilience
      - Reports
      - Events
      - REST
    properties:
      - type: Documentation
        url: https://developer.druva.com
      - type: Authentication
        url: https://developer.druva.com
  - aid: druva:endpoints-data-governance
    name: Druva Endpoints and Data Governance API
    description: The Druva Endpoints and Data Governance API exposes Reports and Events endpoints for visibility into endpoint backups, user activity, and governance posture across managed devices and SaaS workloads.
    humanURL: https://developer.druva.com
    baseURL: https://apis.druva.com
    tags:
      - Endpoints
      - Data Governance
      - Reports
      - Events
    properties:
      - type: Documentation
        url: https://developer.druva.com
  - aid: druva:enterprise-workloads
    name: Druva Enterprise Workloads API
    description: The Druva Enterprise Workloads Events API provides programmatic access to events generated across protected enterprise workloads such as servers, virtual machines, and databases inside the Druva Data Resiliency Cloud.
    humanURL: https://developer.druva.com
    baseURL: https://apis.druva.com
    tags:
      - Enterprise Workloads
      - Events
      - Backup
  - aid: druva:cloudranger
    name: Druva CloudRanger Native Workloads API
    description: The Druva CloudRanger Native Workloads API provides automated backup, disaster recovery, and lifecycle management for AWS-native workloads including EC2, EBS, RDS, Redshift, and DynamoDB.
    humanURL: https://developer.druva.com
    baseURL: https://apis.druva.com
    tags:
      - CloudRanger
      - AWS
      - Native Workloads
      - Backup
  - aid: druva:msp
    name: Druva MSP API
    description: The Druva MSP API enables managed service providers to programmatically manage tenants, customers, and reporting across the Druva platform from a single MSP console integration.
    humanURL: https://developer.druva.com
    baseURL: https://apis.druva.com
    tags:
      - MSP
      - Managed Service Providers
      - Multi-Tenant
  - aid: druva:legal-hold
    name: Druva Legal Hold Targeted Download API
    description: The Druva Legal Hold Targeted Download API supports legal and compliance teams in initiating targeted downloads of preserved data from devices placed under legal hold within Druva.
    humanURL: https://developer.druva.com
    baseURL: https://apis.druva.com
    tags:
      - Legal Hold
      - Compliance
      - eDiscovery
common:
  - type: Website
    url: https://www.druva.com
  - type: Documentation
    url: https://docs.druva.com/
  - type: DeveloperPortal
    url: https://developer.druva.com
  - type: APIReference
    url: https://developer.druva.com/reference
  - type: Support
    url: https://support.druva.com
  - type: GitHub
    url: https://github.com/druvainc
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

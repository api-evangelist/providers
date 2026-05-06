---
aid: cohesity
url: https://raw.githubusercontent.com/api-evangelist/cohesity/refs/heads/main/apis.yml
name: Cohesity
tags:
  - Automation
  - Backup
  - Cyber Resilience
  - Data Management
  - Data Protection
  - Data Security
  - DataProtect
  - Disaster Recovery
  - Helios
  - Orchestration
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-28'
position: Consumer
description: Cohesity is a data security and management company providing backup, disaster recovery, archive, and cyber resilience capabilities across on-premises, cloud, and SaaS workloads. Following the merger with Veritas, the combined company protects enterprise data while powering automation, orchestration, and AI- driven recovery. The Cohesity developer surface centers on the Cohesity REST API, exposed both per-cluster (DataProtect/cluster API) and via the Helios global control plane, with versioned v1 and v2 endpoints, API-key authentication, and SDKs for Python, PowerShell, Ansible, Terraform, and ServiceNow.
apis:
  - aid: cohesity:helios-rest-api
    name: Cohesity Helios REST API
    tags:
      - Automation
      - Cluster Management
      - DataProtect
      - Helios
      - Orchestration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://helios.cohesity.com/irisservices/api/v1/public/
    humanURL: https://developer.cohesity.com/helios-api.html
    properties:
      - url: https://developer.cohesity.com/helios-api.html
        type: Documentation
      - url: https://developer.cohesity.com/docs/helios-getting-started
        type: GettingStarted
      - url: https://developer.cohesity.com/apidocs/versions/
        type: APIReference
    description: Helios is Cohesity's SaaS-based control plane that manages a fleet of Cohesity clusters from a single global pane of glass. The Helios REST API authenticates via an apiKey generated from the Helios UI and passed in the request header, supports both v1 and v2 endpoint families, and lets customers list and operate registered clusters, run protection jobs, manage policies, and access reporting and analytics globally.
    x-features:
      - apiKey-based authentication via Helios UI
      - v1 and v2 API surfaces under /irisservices/api/
      - Manage protection groups, policies, and recovery operations
      - Reporting and global analytics across clusters
      - Multi-cluster operations from a single endpoint
    x-use-cases:
      - Centralize backup and recovery automation across many Cohesity clusters
      - Drive policy and SLA enforcement from CI/CD pipelines
      - Trigger or schedule recoveries from external orchestration tools
      - Export reporting data into SIEM or BI dashboards
  - aid: cohesity:dataprotect-rest-api
    name: Cohesity DataProtect REST API
    tags:
      - Backup
      - DataProtect
      - Disaster Recovery
      - Per-Cluster
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cohesity.com/apidocs/versions/
    properties:
      - url: https://developer.cohesity.com/apidocs/versions/
        type: Documentation
      - url: https://developers.cohesity.com/page/api-reference
        type: APIReference
    description: The DataProtect REST API is the per-cluster RESTful interface exposed by every Cohesity cluster, providing programmatic control over data management operations including backups, restores, replication, archival, cloud tiering, and storage domain management. Authentication is performed via API keys for automation users or username/password for interactive sessions.
    x-features:
      - Per-cluster REST endpoint
      - API key and session authentication
      - Backup, restore, replication, and archive operations
      - Storage domain and view management
      - Versioned API generations available concurrently
    x-use-cases:
      - Automate cluster registration and configuration
      - Trigger ad-hoc backups and recoveries from runbooks
      - Integrate with vRealize, ServiceNow, Ansible, and Terraform workflows
      - Build custom dashboards over per-cluster operational data
common:
  - type: Website
    url: https://www.cohesity.com/
  - type: Developer Portal
    url: https://developer.cohesity.com/
  - type: Developers Site
    url: https://developers.cohesity.com/
  - type: API Reference
    url: https://developer.cohesity.com/apidocs/versions/
  - type: GitHub
    url: https://github.com/cohesity
  - type: Documentation
    url: https://docs.cohesity.com/
  - type: Support
    url: https://www.cohesity.com/support/
  - type: Status
    url: https://status.cohesity.com/
  - type: Privacy Policy
    url: https://www.cohesity.com/legal/privacy-policy/
  - type: Terms of Use
    url: https://www.cohesity.com/agreements/website-terms-of-use/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---

---
aid: tufin
url: https://raw.githubusercontent.com/api-evangelist/tufin/refs/heads/main/apis.yml
apis:
- name: Tufin SecureTrack API
  description: API for querying network topology, security policies, and performing policy analysis across multi-vendor firewall infrastructure.
  image: https://www.tufin.com/themes/custom/tufin/logo.svg
  humanURL: https://www.tufin.com/products/securetrack
  baseURL: https://securetrack.example.com/securetrack/api
  tags:
  - Compliance
  - Firewall Rules
  - Network Topology
  - Policy Analysis
  properties:
  - type: Documentation
    url: https://forum.tufin.com/support/kc/securetrack/Content/Suite/API/index.htm
  - type: OpenAPI
    url: https://securetrack.example.com/securetrack/api/swagger.json
  - type: Authentication
    url: https://forum.tufin.com/support/kc/securetrack/Content/Suite/API/Authentication.htm
  - type: Reference
    url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/4420.htm
  - type: Getting Started
    url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/4423.htm
- name: Tufin SecureChange API
  description: API for automating security policy change workflows, approvals, and implementation across network infrastructure.
  image: https://www.tufin.com/themes/custom/tufin/logo.svg
  humanURL: https://www.tufin.com/products/securechange
  baseURL: https://securechange.example.com/securechangeworkflow/api
  tags:
  - Approvals
  - Change Management
  - Policy Changes
  - Workflow Automation
  properties:
  - type: Documentation
    url: https://forum.tufin.com/support/kc/securechange/Content/Suite/API/index.htm
  - type: OpenAPI
    url: https://securechange.example.com/securechangeworkflow/api/swagger.json
  - type: Reference
    url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/12309.htm
  - type: Authentication
    url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/4423.htm
- name: Tufin SecureApp API
  description: API for application-centric security policy management and micro-segmentation.
  image: https://www.tufin.com/themes/custom/tufin/logo.svg
  humanURL: https://www.tufin.com/products/secureapp
  baseURL: https://secureapp.example.com/api
  tags:
  - Application Security
  - Micro-Segmentation
  - Zero Trust
  properties:
  - type: Documentation
    url: https://forum.tufin.com/support/kc/secureapp/
  - type: Reference
    url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/6481.htm
- name: Tufin Orchestration Suite REST API
  description: Unified REST API for the Tufin Orchestration Suite providing comprehensive security policy lifecycle management.
  image: https://www.tufin.com/themes/custom/tufin/logo.svg
  humanURL: https://www.tufin.com/products/tufin-orchestration-suite
  baseURL: https://tufin.example.com/api/v1
  tags:
  - Automation
  - Orchestration
  - Policy Management
  properties:
  - type: Documentation
    url: https://forum.tufin.com/support/kc
  - type: Reference
    url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/securetrack_api.htm
  - type: Getting Started
    url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/4423.htm
  - type: Authentication
    url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/4423.htm
- name: Tufin SecureTrack GraphQL API
  description: GraphQL API for the Tufin Orchestration Suite providing flexible querying capabilities for security policy data, network topology, and compliance information. Uses OAuth2 authentication and supports complex nested queries across SecureTrack resources.
  image: https://www.tufin.com/themes/custom/tufin/logo.svg
  humanURL: https://forum.tufin.com/support/kc/latest/Content/ST2/API/API_Introduction.htm
  baseURL: https://{tos_ip}/v2/api/sync/graphql
  tags:
  - GraphQL
  - Network Topology
  - Policy Analysis
  - Security Data
  properties:
  - type: Documentation
    url: https://forum.tufin.com/support/kc/latest/Content/ST2/API/API_Introduction.htm
  - type: Authentication
    url: https://forum.tufin.com/support/kc/latest/Content/ST2/API/OAuth2.htm
- name: Tufin SecureCloud API
  description: REST API for Tufin SecureCloud, the cloud-native security policy management platform. Provides endpoints for managing cloud accounts, applications, assets, Kubernetes clusters, and security policies across AWS, Azure, and GCP environments.
  image: https://www.tufin.com/themes/custom/tufin/logo.svg
  humanURL: https://www.tufin.com/tufin-orchestration-suite/securecloud
  baseURL: https://{account}.securecloud.tufin.io/api/v1
  tags:
  - Cloud Security
  - Kubernetes
  - Multi-Cloud
  - Policy Management
  properties:
  - type: Documentation
    url: https://forum.tufin.com/support/kc/securecloud/
  - type: Reference
    url: https://securecloud.tufin.io/api-documentation/index.html
name: Tufin
tags:
- Cloud Security
- Compliance
- Firewall Management
- Network Security
- Risk Management
- Security Policy Management
type: Contract
image: https://www.tufin.com/themes/custom/tufin/logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Tufin provides security policy orchestration solutions for managing network security policies across hybrid cloud environments, including firewalls, SDN, and cloud security controls.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---


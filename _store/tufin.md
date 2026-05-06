---
name: Tufin
description: Tufin provides security policy orchestration solutions for managing network security policies across hybrid cloud environments, including firewalls, SDN, and cloud security controls. The Tufin Orchestration Suite (TOS) includes SecureTrack for network topology and policy analysis, SecureChange for automated policy change workflows, SecureApp for application-centric policy management, and SecureCloud for cloud-native security posture management. Tufin offers comprehensive REST APIs and GraphQL APIs for integrating with ITSM, SIEM, and other security tools.
image: https://www.tufin.com/themes/custom/tufin/logo.svg
url: https://www.tufin.com
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.18'
tags:
  - Cloud Security
  - Compliance
  - Firewall Management
  - Network Security
  - Network Topology
  - Policy Orchestration
  - Risk Management
  - Security Policy Management
  - Zero Trust
apis:
  - name: Tufin SecureTrack API
    description: The SecureTrack REST API enables programmatic access to Tufin's network security policy management platform. It supports querying network devices and firewall rules, analyzing network topology and path queries, retrieving policy compliance data, performing risk and cleanup analysis, managing rule documentation and recertification, and searching for network objects, services, and interfaces across multi-vendor firewall infrastructure. Authentication uses HTTP Basic Auth with TOS credentials.
    image: https://www.tufin.com/themes/custom/tufin/logo.svg
    humanURL: https://www.tufin.com/products/securetrack
    baseURL: https://{tos_host}/securetrack/api
    tags:
      - Compliance
      - Firewall Rules
      - Network Devices
      - Network Topology
      - Policy Analysis
      - Risk Analysis
    properties:
      - type: Documentation
        url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/securetrack_api.htm
      - type: SwaggerUI
        url: https://forum.tufin.com/support/kc/rest-api/R24-1/securetrack/apidoc/
      - type: Authentication
        url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/4423.htm
      - type: Reference
        url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/4420.htm
      - type: GettingStarted
        url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/4423.htm
      - type: OpenAPI
        url: openapi/tufin-securetrack-openapi.yml
    features:
      - name: Device and Policy Management
        description: Retrieve, add, and update firewall devices and security policies across multi-vendor environments.
      - name: Network Topology Analysis
        description: Query network paths, retrieve topology maps, and analyze traffic flows across the managed network.
      - name: Risk and Compliance Analysis
        description: Identify policy violations, clean up unused rules, and generate compliance reports.
      - name: Rule Search and Documentation
        description: Search for rules, network objects, and services across all managed devices with full documentation support.
  - name: Tufin SecureChange API
    description: The SecureChange REST API automates security policy change workflows, enabling programmatic submission and management of access request tickets, approval workflows, and change implementation across network infrastructure. Supports integration with ITSM platforms including ServiceNow, Jira, and Remedy for end-to-end change automation.
    image: https://www.tufin.com/themes/custom/tufin/logo.svg
    humanURL: https://www.tufin.com/products/securechange
    baseURL: https://{tos_host}/securechangeworkflow/api
    tags:
      - Approvals
      - Change Management
      - ITSM Integration
      - Policy Changes
      - Ticketing
      - Workflow Automation
    properties:
      - type: Documentation
        url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/12309.htm
      - type: SwaggerUI
        url: https://forum.tufin.com/support/kc/rest-api/R24-1/securechangeworkflow/apidoc/
      - type: Reference
        url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/12309.htm
      - type: Authentication
        url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/4423.htm
      - type: OpenAPI
        url: openapi/tufin-securechange-openapi.yml
    features:
      - name: Access Request Tickets
        description: Create, retrieve, and update security access request tickets programmatically.
      - name: Workflow Automation
        description: Automate the full lifecycle of security policy changes from request through approval to implementation.
      - name: ITSM Integration
        description: Integrate with ServiceNow, Jira, and other ITSM platforms for unified change management.
  - name: Tufin SecureApp API
    description: API for application-centric security policy management and micro-segmentation. SecureApp enables teams to manage security policies at the application level, define connectivity requirements, and automate policy changes for application deployments.
    image: https://www.tufin.com/themes/custom/tufin/logo.svg
    humanURL: https://www.tufin.com/products/secureapp
    baseURL: https://{tos_host}/securechangeworkflow/api
    tags:
      - Application Security
      - Micro-Segmentation
      - Policy Management
      - Zero Trust
    properties:
      - type: Documentation
        url: https://forum.tufin.com/support/kc/secureapp/
      - type: Reference
        url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/6481.htm
  - name: Tufin SecureTrack GraphQL API
    description: GraphQL API for the Tufin Orchestration Suite providing flexible querying capabilities for security policy data, network topology, and compliance information. Uses OAuth2 authentication and supports complex nested queries across SecureTrack resources including devices, policies, rules, and topology.
    image: https://www.tufin.com/themes/custom/tufin/logo.svg
    humanURL: https://forum.tufin.com/support/kc/latest/Content/ST2/API/API_Introduction.htm
    baseURL: https://{tos_ip}/v2/api/sync/graphql
    tags:
      - GraphQL
      - Network Topology
      - OAuth2
      - Policy Analysis
      - Security Data
    properties:
      - type: Documentation
        url: https://forum.tufin.com/support/kc/latest/Content/ST2/API/API_Introduction.htm
      - type: Authentication
        url: https://forum.tufin.com/support/kc/latest/Content/ST2/API/OAuth2.htm
  - name: Tufin SecureCloud API
    description: REST API for Tufin SecureCloud, the cloud-native security policy management platform. Provides endpoints for managing cloud accounts, applications, assets, Kubernetes clusters, and security policies across AWS, Azure, and GCP environments. Enables cloud security posture management (CSPM) and Kubernetes network policy enforcement through API integration.
    image: https://www.tufin.com/themes/custom/tufin/logo.svg
    humanURL: https://www.tufin.com/tufin-orchestration-suite/securecloud
    baseURL: https://{account}.securecloud.tufin.io/api/v1
    tags:
      - Cloud Security
      - CSPM
      - Kubernetes
      - Multi-Cloud
      - Policy Management
    properties:
      - type: Documentation
        url: https://forum.tufin.com/support/kc/securecloud/
      - type: Reference
        url: https://securecloud.tufin.io/api-documentation/index.html
common:
  - type: Portal
    url: https://forum.tufin.com/
  - type: Support
    url: https://www.tufin.com/support
  - type: Documentation
    url: https://forum.tufin.com/support/kc
  - type: Blog
    url: https://www.tufin.com/blog
  - type: Login
    url: https://portal.tufin.io/
  - type: Contact
    url: https://www.tufin.com/company/contact-us
  - type: Privacy Policy
    url: https://www.tufin.com/privacy-policy
  - type: Terms of Service
    url: https://www.tufin.com/terms-of-use
  - type: Website
    url: https://www.tufin.com
  - type: GettingStarted
    url: https://forum.tufin.com/support/kc/latest/Content/Suite/RESTAPI/4423.htm
  - type: Community
    url: https://community.tufin.com/
  - type: GitHub Organization
    url: https://github.com/Tufin
  - type: SDK
    url: https://gitlab.com/tufinps/pytos2-ce
  - type: SDK
    url: https://github.com/Tufin/pytos
  - type: PostmanCollection
    url: https://github.com/Tufin/postman
  - type: Sign Up
    url: https://www.tufin.com/demo
  - type: Videos
    url: https://www.tufin.com/resources/type/videos
  - type: Developers
    url: https://www.tufin.com/developers
  - type: OpenAPI
    url: openapi/tufin-securetrack-openapi.yml
  - type: OpenAPI
    url: openapi/tufin-securechange-openapi.yml
  - type: Vocabulary
    url: vocabulary/tufin-vocabulary.yml
  - type: JSON-LD
    url: json-ld/tufin-context.jsonld
  - type: JSONSchema
    url: json-schema/tufin-device-schema.json
  - type: JSONSchema
    url: json-schema/tufin-ticket-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

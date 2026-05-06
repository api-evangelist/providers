---
aid: puppet
name: Puppet
description: Puppet provides infrastructure automation and configuration management for hybrid and cloud environments. Puppet Enterprise exposes a collection of service APIs (Orchestrator, RBAC, Node Classifier, Code Manager, Activity, Status, Inventory, Value) that enable programmatic management of nodes, users, classifications, code deployments, and operational events.
type: Index
position: Consumer
access: 3rd-Party
image: https://puppet.com/sites/default/files/2021-09/puppet-logo.png
url: https://raw.githubusercontent.com/api-evangelist/puppet/refs/heads/main/apis.yml
tags:
  - Automation
  - Configuration Management
  - DevOps
  - Enterprise
  - Infrastructure as Code
  - Orchestration
  - RBAC
created: '2025-02-24'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: puppet:orchestrator
    name: Puppet Enterprise Orchestrator API
    description: The Orchestrator API enables you to gather details about orchestrator jobs you run and inspect application instances. It powers running tasks and orchestration workflows across PE-managed nodes.
    humanURL: https://help.puppet.com/pe/2025.10/topics/orchestrator_api.htm
    tags:
      - Orchestration
      - Tasks
    properties:
      - type: Documentation
        url: https://help.puppet.com/pe/2025.10/topics/orchestrator_api.htm
  - aid: puppet:rbac
    name: Puppet Enterprise RBAC Service API
    description: The RBAC Service API manages access to PE, generates authentication tokens, and provides user, role, group, and permission management. v2 adds user retrieval with filters, token revocation, and LDAP admin.
    humanURL: https://help.puppet.com/pe/2025.10/topics/rbac_service_api_v1.htm
    tags:
      - RBAC
      - Authentication
      - Users
    properties:
      - type: Documentation
        url: https://help.puppet.com/pe/2025.10/topics/rbac_service_api_v1.htm
      - type: Documentation
        url: https://help.puppet.com/pe/2025.10/topics/rbac_service_api_v2.htm
  - aid: puppet:node-classifier
    name: Puppet Enterprise Node Classifier Service API
    description: The Node Classifier API enables querying node group matches, assigned classes and parameters, and environment assignments. Used to manage how nodes are classified and configured.
    humanURL: https://help.puppet.com/pe/2025.10/topics/classifier_api.htm
    tags:
      - Classification
      - Nodes
    properties:
      - type: Documentation
        url: https://help.puppet.com/pe/2025.10/topics/classifier_api.htm
  - aid: puppet:code-manager
    name: Puppet Enterprise Code Manager API
    description: The Code Manager API supports webhook creation, deployment queueing, and status monitoring for Puppet code, enabling Git-driven control of Puppet environments.
    humanURL: https://help.puppet.com/pe/2025.10/topics/code_mgr_api.htm
    tags:
      - Code
      - Deployment
      - Webhooks
    properties:
      - type: Documentation
        url: https://help.puppet.com/pe/2025.10/topics/code_mgr_api.htm
  - aid: puppet:activity
    name: Puppet Enterprise Activity Service API
    description: The Activity Service API queries PE service and user events logged by the activity service, supporting audit and operational visibility.
    humanURL: https://help.puppet.com/pe/2025.10/topics/activity_api.htm
    tags:
      - Activity
      - Audit
    properties:
      - type: Documentation
        url: https://help.puppet.com/pe/2025.10/topics/activity_api.htm
  - aid: puppet:status
    name: Puppet Enterprise Status API
    description: The Status API checks the health status of PE services.
    humanURL: https://help.puppet.com/pe/2025.10/topics/status_api.htm
    tags:
      - Health
      - Monitoring
    properties:
      - type: Documentation
        url: https://help.puppet.com/pe/2025.10/topics/status_api.htm
  - aid: puppet:inventory
    name: Puppet Enterprise Node Inventory API
    description: The Node Inventory API manages inventory service database operations including connection entries and listings.
    humanURL: https://help.puppet.com/pe/2025.10/topics/inventory_api.htm
    tags:
      - Inventory
      - Nodes
    properties:
      - type: Documentation
        url: https://help.puppet.com/pe/2025.10/topics/inventory_api.htm
  - aid: puppet:value
    name: Puppet Enterprise Value API
    description: The Value API generates automation impact reports on time and cost savings.
    humanURL: https://help.puppet.com/pe/2025.10/topics/value_api.htm
    tags:
      - Reports
      - Analytics
    properties:
      - type: Documentation
        url: https://help.puppet.com/pe/2025.10/topics/value_api.htm
  - aid: puppet:forge
    name: Puppet Forge
    description: Puppet Forge is the public module repository providing thousands of downloadable Puppet modules.
    humanURL: https://forge.puppet.com/
    tags:
      - Modules
      - Registry
    properties:
      - type: Website
        url: https://forge.puppet.com/
common:
  - type: Website
    url: https://www.puppet.com/
  - type: Documentation
    url: https://help.puppet.com/
  - type: Blog
    url: https://www.puppet.com/blog
  - type: GitHub Organization
    url: https://github.com/puppetlabs
  - type: Forge
    url: https://forge.puppet.com/
  - type: Status
    url: https://status.puppet.com/
  - type: Support
    url: https://support.puppet.com/
  - type: Pricing
    url: https://www.puppet.com/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---

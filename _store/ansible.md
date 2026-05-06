---
name: Ansible
description: Ansible is an open-source IT automation platform developed by Red Hat that provides agentless configuration management, application deployment, cloud provisioning, and orchestration. Using YAML-based playbooks and an SSH-native architecture, Ansible automates infrastructure at scale without requiring agents or custom security infrastructure on managed nodes.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Ansible
  - Automation
  - Configuration Management
  - DevOps
  - Infrastructure As Code
  - Open Source
  - Orchestration
  - Red Hat
created: '2024-01-01'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/ansible/refs/heads/main/apis.yml
specificationVersion: '0.16'
apis:
  - name: Ansible Automation Platform API
    description: RESTful API for Ansible Automation Platform (formerly Ansible Tower) that provides programmatic access to job templates, inventories, credentials, workflow templates, schedules, notifications, and job execution. Supports OAuth2 authentication and delivers a comprehensive management interface for enterprise-scale Ansible deployments.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.ansible.com/automation-controller/latest/html/controllerapi/
    baseURL: https://your-controller-host/api/v2/
    tags:
      - Ansible
      - Automation
      - Enterprise
      - Inventories
      - Jobs
      - Red Hat
      - Workflows
    properties:
      - type: Documentation
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/
      - type: APIReference
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/api_ref.html
      - type: Authentication
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/authentication.html
      - type: GettingStarted
        url: https://docs.ansible.com/automation-controller/latest/html/quickstart/
    contact:
      - FN: Ansible Support
        url: https://access.redhat.com/support
  - name: AWX API
    description: AWX is the open-source upstream project for Ansible Automation Platform, providing a web-based UI, REST API, and task engine for Ansible under the Apache 2.0 license. The AWX API mirrors the AAP API surface for job management, inventory, credentials, workflow templates, and scheduling.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/ansible/awx
    baseURL: https://your-awx-host/api/v2/
    tags:
      - Ansible
      - Automation
      - AWX
      - Jobs
      - Open Source
    properties:
      - type: Documentation
        url: https://ansible.readthedocs.io/projects/awx/en/latest/
      - type: APIReference
        url: https://github.com/ansible/awx/blob/devel/docs/rest_api.md
      - type: GitHubRepository
        url: https://github.com/ansible/awx
      - type: GettingStarted
        url: https://github.com/ansible/awx/blob/devel/INSTALL.md
    contact:
      - FN: AWX Community
        url: https://github.com/ansible/awx/discussions
  - name: Ansible Galaxy API
    description: REST API for Ansible Galaxy — the community hub for sharing and downloading Ansible roles and collections. The v1 API covers roles and the v3 API covers collections with namespace management, versioning, search, and content download capabilities.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://galaxy.ansible.com/
    baseURL: https://galaxy.ansible.com/api/
    tags:
      - Ansible
      - Collections
      - Community
      - Galaxy
      - Roles
    properties:
      - type: Documentation
        url: https://galaxy.ansible.com/docs/
      - type: APIReference
        url: https://galaxy.ansible.com/api/v3/
      - type: GitHubRepository
        url: https://github.com/ansible/galaxy
    contact:
      - FN: Ansible Galaxy Team
        url: https://github.com/ansible/galaxy/issues
  - name: Ansible Automation Hub API
    description: The Red Hat Ansible Automation Hub API provides access to certified Ansible collections and roles curated by Red Hat and partners. Available through console.redhat.com, it serves certified content for enterprise Ansible Automation Platform deployments.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://console.redhat.com/ansible/automation-hub
    baseURL: https://console.redhat.com/api/automation-hub/v3/
    tags:
      - Ansible
      - Certified Content
      - Collections
      - Enterprise
      - Red Hat
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/
      - type: APIReference
        url: https://console.redhat.com/api/automation-hub/v3/
      - type: Portal
        url: https://console.redhat.com/ansible/automation-hub
    contact:
      - FN: Red Hat Support
        url: https://access.redhat.com/support
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X: apievangelist
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://www.ansible.com
  - type: GettingStarted
    url: https://docs.ansible.com/ansible/latest/getting_started/
  - type: Documentation
    url: https://docs.ansible.com/
  - type: Blog
    url: https://www.ansible.com/blog
  - type: GitHubOrganization
    url: https://github.com/ansible
  - type: Forum
    url: https://forum.ansible.com/
  - type: Support
    url: https://access.redhat.com/products/red-hat-ansible-automation-platform/
  - type: Training
    url: https://www.ansible.com/products/training-certification
  - type: TermsOfService
    url: https://www.redhat.com/en/about/terms-use
  - type: PrivacyPolicy
    url: https://www.redhat.com/en/about/privacy-policy
  - type: SDK
    url: https://pypi.org/project/ansible/
    title: Ansible Python Package
  - type: SDK
    url: https://pypi.org/project/ansible-runner/
    title: Ansible Runner Python Package
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/ansible/refs/heads/main/json-schema/ansible-playbook-schema.json
    title: Playbook Schema
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/ansible/refs/heads/main/vocabulary/ansible-vocabulary.yaml
  - type: Features
    data:
      - name: Agentless Architecture
        description: Ansible connects to managed nodes via SSH or WinRM without requiring any agent software, simplifying deployment and reducing attack surface.
      - name: YAML Playbooks
        description: Automation is defined in human-readable YAML playbooks that describe the desired state of managed systems without complex programming.
      - name: Idempotent Execution
        description: Ansible tasks are idempotent — running the same playbook multiple times produces the same result, making deployments safe to rerun.
      - name: Module Ecosystem
        description: Over 3,000 built-in modules covering cloud providers, network devices, databases, containers, storage, and operating system tasks.
      - name: Collection System
        description: The Ansible Collections packaging format bundles related modules, roles, plugins, and documentation for modular content distribution.
      - name: Dynamic Inventory
        description: Query cloud providers, CMDBs, and external systems dynamically to build host inventories at execution time rather than static files.
  - type: UseCases
    data:
      - name: Configuration Management
        description: Ensure servers and services remain in a consistent desired state by applying configuration playbooks across fleets of hosts.
      - name: Application Deployment
        description: Deploy and update applications across development, staging, and production environments with zero-downtime rolling strategies.
      - name: Cloud Provisioning
        description: Provision cloud resources on AWS, Azure, GCP, and other providers using cloud-specific Ansible modules and dynamic inventory.
      - name: Network Automation
        description: Configure routers, switches, and firewalls from Cisco, Juniper, Arista, and Palo Alto using vendor-specific Ansible collections.
      - name: Security and Compliance
        description: Enforce security baselines, CIS benchmarks, and STIG compliance across infrastructure using Ansible hardening playbooks.
  - type: Integrations
    data:
      - name: Red Hat Enterprise Linux
        description: Ansible is the primary configuration management tool for Red Hat Enterprise Linux systems with deep integration into the RHEL platform.
      - name: Kubernetes / OpenShift
        description: Manage Kubernetes clusters, namespaces, deployments, and OpenShift workloads using the kubernetes.core collection.
      - name: Terraform
        description: Combine Terraform for cloud resource provisioning with Ansible for post-provisioning OS and application configuration.
      - name: Jenkins / GitHub Actions
        description: Integrate Ansible playbook execution into CI/CD pipelines using the AAP Action for GitHub or Ansible Tower Plugin for Jenkins.
      - name: ServiceNow
        description: Trigger Ansible automation from ServiceNow ITSM workflows using the ServiceNow ITX collection for change management automation.
---

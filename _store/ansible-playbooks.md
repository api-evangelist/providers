---
name: Ansible Playbooks
description: A curated collection of APIs, tools, and platforms for managing and executing Ansible playbooks for IT automation, configuration management, and orchestration. Covers the Ansible Automation Platform, AWX, Galaxy, Automation Hub, Runner, and Semaphore APIs that power modern infrastructure automation workflows.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/ansible-playbooks/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.16'
tags:
  - Ansible
  - Automation
  - Configuration Management
  - DevOps
  - Infrastructure As Code
  - Orchestration
  - Playbooks
apis:
  - name: Ansible Automation Platform API
    description: REST API for Ansible Automation Platform (formerly Ansible Tower/AWX) to manage playbooks, inventories, credentials, job templates, and job execution at enterprise scale. Supports RBAC, workflows, schedules, notifications, and survey prompts. Available as a self-hosted deployment or managed via Red Hat's cloud.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.ansible.com/automation-controller/latest/html/controllerapi/
    baseURL: https://your-aap-instance/api/v2/
    tags:
      - Ansible
      - Automation
      - Enterprise
      - Jobs
      - Orchestration
      - Playbooks
      - Red Hat
    properties:
      - type: Documentation
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/
      - type: APIReference
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/api_ref.html
      - type: Authentication
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/authentication.html
      - type: Pricing
        url: https://www.ansible.com/products/pricing
      - type: GettingStarted
        url: https://docs.ansible.com/automation-controller/latest/html/quickstart/
    contact:
      - FN: Red Hat Ansible Support
        url: https://access.redhat.com/support
  - name: AWX API
    description: AWX is the open-source upstream project for Ansible Automation Platform, providing a web-based UI, REST API, and task engine for Ansible. The AWX API offers programmatic access to job execution, inventory management, credential storage, workflow templates, and scheduling. Self-hosted and free under the Apache 2.0 license.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/ansible/awx
    baseURL: https://your-awx-instance/api/v2/
    tags:
      - Ansible
      - Automation
      - AWX
      - Open Source
      - Playbooks
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
  - name: Ansible Runner API
    description: Ansible Runner is a Python library and CLI tool that provides a stable and consistent interface for executing Ansible playbooks programmatically from within other applications and tools. Used by AWX, Automation Platform, and CI/CD pipelines to launch Ansible with structured input and output handling.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://ansible-runner.readthedocs.io/
    baseURL: https://pypi.org/project/ansible-runner/
    tags:
      - Ansible
      - Automation
      - Library
      - Playbooks
      - Python
    properties:
      - type: Documentation
        url: https://ansible-runner.readthedocs.io/en/stable/
      - type: APIReference
        url: https://ansible-runner.readthedocs.io/en/stable/python_interface.html
      - type: GitHubRepository
        url: https://github.com/ansible/ansible-runner
      - type: SDK
        url: https://pypi.org/project/ansible-runner/
    contact:
      - FN: Ansible Community
        url: https://github.com/ansible/ansible-runner/issues
  - name: Ansible Galaxy API
    description: Ansible Galaxy is the community hub for sharing Ansible roles and collections. The Galaxy REST API enables searching, downloading, and publishing Ansible content. Supports v1 (roles), v2 (mixed), and v3 (collections) API versions with namespace management, search, versioning, and download statistics.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://galaxy.ansible.com
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
      - type: GettingStarted
        url: https://docs.ansible.com/ansible/latest/galaxy/user_guide.html
    contact:
      - FN: Ansible Galaxy Team
        url: https://github.com/ansible/galaxy/issues
  - name: Ansible Automation Hub API
    description: Red Hat Ansible Automation Hub is the enterprise content hub for certified Ansible collections, roles, and execution environments. The API provides access to Red Hat certified and partner-validated Ansible content for use in production Ansible Automation Platform deployments.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://console.redhat.com/ansible/automation-hub
    baseURL: https://console.redhat.com/api/automation-hub/
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
  - name: Ansible Semaphore API
    description: Ansible Semaphore is an open-source modern web UI and REST API for running Ansible playbooks. It provides project management, task scheduling, access control, and a clean interface for teams using Ansible without the complexity of Automation Platform. The REST API supports full task and project management.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.ansible-semaphore.com/
    baseURL: https://your-semaphore-instance/api/
    tags:
      - Ansible
      - Open Source
      - Playbooks
      - Semaphore
      - Workflow
    properties:
      - type: Documentation
        url: https://docs.ansible-semaphore.com/
      - type: APIReference
        url: https://docs.ansible-semaphore.com/api-reference
      - type: GitHubRepository
        url: https://github.com/ansible-semaphore/semaphore
    contact:
      - FN: Semaphore Community
        url: https://github.com/ansible-semaphore/semaphore/issues
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X: apievangelist
    url: https://apievangelist.com
common:
  - type: GettingStarted
    url: https://docs.ansible.com/ansible/latest/getting_started/
  - type: BestPractices
    url: https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html
  - type: Blog
    url: https://www.ansible.com/blog
  - type: TermsOfService
    url: https://www.redhat.com/en/about/terms-use
  - type: PrivacyPolicy
    url: https://www.redhat.com/en/about/privacy-policy
  - type: GitHubOrganization
    url: https://github.com/ansible
  - type: Forum
    url: https://forum.ansible.com/
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/ansible-playbooks/refs/heads/main/json-schema/ansible-playbooks-playbook-job-schema.json
    title: Playbook Job Schema
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/ansible-playbooks/refs/heads/main/json-schema/ansible-playbooks-inventory-schema.json
    title: Inventory Schema
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/ansible-playbooks/refs/heads/main/vocabulary/ansible-playbooks-vocabulary.yaml
  - type: Features
    data:
      - name: Playbook Execution via API
        description: Launch, monitor, and cancel Ansible playbook runs programmatically via REST API with support for extra vars, limits, and tags.
      - name: Inventory Management
        description: Create and manage dynamic and static inventories with groups, hosts, and host variables through the API.
      - name: Credential Storage
        description: Securely store SSH keys, cloud credentials, and vault passwords in encrypted credential objects accessible to jobs.
      - name: Workflow Templates
        description: Chain multiple job templates into orchestrated workflows with conditional success/failure branching.
      - name: Scheduling
        description: Schedule playbook runs on recurring schedules using rrule-based calendar expressions.
      - name: Collections and Role Management
        description: Discover, download, and manage Ansible collections and roles from Galaxy, Automation Hub, or private repositories.
  - type: UseCases
    data:
      - name: Infrastructure Provisioning
        description: Automate the provisioning of cloud resources, VMs, and bare-metal servers using Ansible playbooks triggered via API.
      - name: Configuration Management
        description: Enforce consistent configuration state across server fleets by scheduling and executing configuration playbooks via API.
      - name: CI/CD Pipeline Integration
        description: Trigger Ansible playbook runs as deployment steps within Jenkins, GitLab CI, GitHub Actions, and other CI/CD platforms.
      - name: Compliance and Remediation
        description: Run compliance playbooks on demand or on schedule to detect and remediate drift from desired security baseline states.
      - name: Network Automation
        description: Automate network device configuration, firmware upgrades, and compliance checks using Ansible network collections via the API.
  - type: Integrations
    data:
      - name: Red Hat OpenShift
        description: Deploy and configure OpenShift clusters and workloads using Ansible Automation Platform integrated with OpenShift pipelines.
      - name: ServiceNow
        description: Trigger Ansible job templates from ServiceNow ITSM workflows for automated ticket remediation and change management.
      - name: GitHub Actions
        description: Use the Ansible Automation Platform GitHub Action to trigger playbook runs as part of GitHub CI/CD workflows.
      - name: Terraform
        description: Combine Terraform for infrastructure provisioning with Ansible for post-provisioning configuration management.
      - name: Splunk
        description: Use Ansible collections to configure Splunk deployments and automate security alert remediation workflows.
---

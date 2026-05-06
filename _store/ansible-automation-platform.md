---
aid: ansible-automation-platform
name: Ansible Automation Platform
description: Ansible Automation Platform (formerly Ansible Tower) provides a REST API for managing automation workflows, job templates, inventories, credentials, and projects. The API enables programmatic access to the automation controller for launching jobs, managing infrastructure inventory, and orchestrating complex multi-tier deployments across hybrid cloud environments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/ansible-automation-platform/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Automation
  - Configuration Management
  - DevOps
  - Infrastructure as Code
  - Orchestration
apis:
  - aid: ansible-automation-platform:controller-api
    name: Ansible Automation Controller API
    description: RESTful API for the Ansible Automation Controller (formerly Ansible Tower) providing programmatic access to job templates, workflows, inventories, credentials, projects, and job execution. Supports CRUD operations on all controller resources with token-based and session authentication.
    humanURL: https://docs.ansible.com/automation-controller/latest/html/controllerapi/
    baseURL: https://controller-host/api/v2/
    tags:
      - Automation
      - Controller
      - Jobs
      - REST
    properties:
      - type: Documentation
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/
      - type: APIReference
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/api_ref.html
      - type: Authentication
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/authentication.html
      - type: GettingStarted
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/intro.html
  - aid: ansible-automation-platform:hub-api
    name: Ansible Automation Hub API
    description: REST API for Ansible Automation Hub providing access to certified and validated Ansible content collections, roles, and execution environments. Supports searching, downloading, and publishing automation content.
    humanURL: https://docs.ansible.com/automation-hub/
    baseURL: https://hub-host/api/galaxy/
    tags:
      - Collections
      - Content Hub
      - REST
      - Roles
    properties:
      - type: Documentation
        url: https://docs.ansible.com/automation-hub/
  - aid: ansible-automation-platform:event-driven-api
    name: Ansible Event-Driven Automation API
    description: API for Event-Driven Ansible (EDA) Controller enabling management of rulebooks, activations, and event sources for automated response to infrastructure and application events.
    humanURL: https://docs.ansible.com/automation-controller/latest/html/userguide/eda.html
    baseURL: https://eda-host/api/eda/v1/
    tags:
      - EDA
      - Event-Driven
      - REST
      - Rulebooks
    properties:
      - type: Documentation
        url: https://docs.ansible.com/automation-controller/latest/html/userguide/eda.html
  - aid: ansible-automation-platform:galaxy-api
    name: Ansible Galaxy API
    description: REST API for Ansible Galaxy, the community hub for sharing Ansible roles and collections. Supports searching, downloading, and rating community automation content.
    humanURL: https://galaxy.ansible.com/docs/
    baseURL: https://galaxy.ansible.com/api/v3/
    tags:
      - Collections
      - Community
      - Galaxy
      - REST
      - Roles
    properties:
      - type: Documentation
        url: https://galaxy.ansible.com/docs/
      - type: APIReference
        url: https://galaxy.ansible.com/api/
common:
  - type: Portal
    url: https://docs.ansible.com/
  - type: Documentation
    url: https://docs.ansible.com/automation-controller/
  - type: GettingStarted
    url: https://docs.ansible.com/ansible/latest/getting_started/
  - type: Blog
    url: https://www.ansible.com/blog
  - type: GitHubOrganization
    url: https://github.com/ansible
  - type: Support
    url: https://access.redhat.com/products/ansible-automation-platform
  - type: TermsOfService
    url: https://www.redhat.com/en/about/agreements
  - type: PrivacyPolicy
    url: https://www.redhat.com/en/about/privacy-policy
  - type: Training
    url: https://www.ansible.com/products/training-certification
  - type: YouTube
    url: https://www.youtube.com/ansibleautomation
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/ansible
  - type: Pricing
    url: https://www.redhat.com/en/technologies/management/ansible/pricing
  - type: Features
    data:
      - name: Job Template Management
        description: Define and manage reusable automation job templates with variables, credentials, and inventory assignments.
      - name: Workflow Orchestration
        description: Build multi-step automation workflows with conditional logic, error handling, and approval gates.
      - name: Inventory Management
        description: Manage dynamic and static inventories of infrastructure hosts with grouping and variable assignment.
      - name: Role-Based Access Control
        description: Fine-grained access control for automation resources with teams, users, and permission assignments.
      - name: Event-Driven Automation
        description: Automatically respond to infrastructure events with rulebook-driven automation triggers.
      - name: Content Collections
        description: Discover, install, and manage certified Ansible content collections from Automation Hub.
  - type: UseCases
    data:
      - name: Infrastructure Provisioning
        description: Automate provisioning of servers, networks, and cloud resources across hybrid environments.
      - name: Configuration Management
        description: Maintain consistent configuration across thousands of servers with idempotent automation.
      - name: Application Deployment
        description: Automate application deployment pipelines with rolling updates and rollback capabilities.
      - name: Security Compliance
        description: Enforce security policies and compliance standards through automated remediation workflows.
      - name: Network Automation
        description: Automate network device configuration and management across multi-vendor environments.
  - type: Integrations
    data:
      - name: Red Hat Satellite
        description: Integration with Red Hat Satellite for content management and patch automation.
      - name: ServiceNow
        description: ITSM integration for change management approval workflows and incident remediation.
      - name: AWS
        description: Cloud automation modules for AWS services including EC2, S3, RDS, and CloudFormation.
      - name: Azure
        description: Cloud automation modules for Azure services including VMs, AKS, and Azure Resource Manager.
      - name: Terraform
        description: Infrastructure as code integration for provisioning with Terraform and configuring with Ansible.
      - name: Jenkins
        description: CI/CD pipeline integration for automated deployment workflows triggered by Jenkins.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---

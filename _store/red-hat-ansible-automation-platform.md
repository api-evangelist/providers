---
aid: red-hat-ansible-automation-platform
name: Red Hat Ansible Automation Platform
description: Red Hat Ansible Automation Platform is an enterprise automation solution that provides a framework for building and operating IT automation at scale. It includes the Automation Controller, Automation Hub, Event-Driven Ansible, and Ansible Lightspeed with IBM watsonx Code Assistant, providing REST APIs for managing automation across hybrid cloud infrastructure.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Automation
  - Configuration Management
  - DevOps
  - Enterprise
  - Red Hat
apis:
  - aid: red-hat-ansible-automation-platform:controller-api
    name: Red Hat Ansible Automation Controller API
    description: Enterprise REST API for the Red Hat Ansible Automation Controller providing centralized management of automation jobs, workflows, inventories, credentials, and RBAC with enterprise authentication and audit logging.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/
    baseURL: https://controller-host/api/v2/
    tags:
      - Automation
      - Controller
      - Enterprise
      - REST
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/
      - type: APIReference
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/api_ref.html
      - type: Authentication
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/authentication.html
  - aid: red-hat-ansible-automation-platform:private-hub-api
    name: Red Hat Ansible Private Automation Hub API
    description: REST API for managing a private instance of Ansible Automation Hub, enabling organizations to curate, publish, and distribute certified and custom Ansible content collections within their enterprise.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/2.4/html/managing_red_hat_certified_and_ansible_galaxy_collections_in_automation_hub/
    baseURL: https://hub-host/api/galaxy/
    tags:
      - Collections
      - Content Hub
      - Enterprise
      - REST
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/2.4/html/managing_red_hat_certified_and_ansible_galaxy_collections_in_automation_hub/
  - aid: red-hat-ansible-automation-platform:eda-controller-api
    name: Red Hat Event-Driven Ansible Controller API
    description: REST API for the Event-Driven Ansible Controller enabling management of event sources, rulebook activations, decision environments, and automated response workflows for infrastructure and application events.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/2.4/html/event-driven_ansible_controller_user_guide/
    baseURL: https://eda-host/api/eda/v1/
    tags:
      - EDA
      - Event-Driven
      - REST
      - Rulebooks
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/2.4/html/event-driven_ansible_controller_user_guide/
  - aid: red-hat-ansible-automation-platform:services-catalog-api
    name: Red Hat Automation Services Catalog API
    description: REST API for the Automation Services Catalog providing a self-service portal where users can order and manage pre-approved automation services with governance controls and approval workflows.
    humanURL: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/
    baseURL: https://catalog-host/api/v1/
    tags:
      - Catalog
      - Governance
      - REST
      - Self-Service
    properties:
      - type: Documentation
        url: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/
common:
  - type: Portal
    url: https://www.redhat.com/en/technologies/management/ansible
  - type: Documentation
    url: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/
  - type: GettingStarted
    url: https://www.redhat.com/en/technologies/management/ansible/trial
  - type: Blog
    url: https://www.ansible.com/blog
  - type: GitHubOrganization
    url: https://github.com/ansible
  - type: Support
    url: https://access.redhat.com/support/
  - type: TermsOfService
    url: https://www.redhat.com/en/about/agreements
  - type: PrivacyPolicy
    url: https://www.redhat.com/en/about/privacy-policy
  - type: Training
    url: https://www.redhat.com/en/services/training/do007-ansible-essentials-simplicity-automation-technical-overview
  - type: Pricing
    url: https://www.redhat.com/en/technologies/management/ansible/pricing
  - type: StatusPage
    url: https://status.redhat.com/
  - type: Features
    data:
      - name: Enterprise Automation Controller
        description: Centralized management of automation with RBAC, audit logging, and credential management.
      - name: Private Automation Hub
        description: Curate and distribute certified and custom Ansible content collections within the enterprise.
      - name: Event-Driven Automation
        description: Automated response to infrastructure events using rulebook activations and event sources.
      - name: Ansible Lightspeed
        description: AI-powered automation content generation with IBM watsonx Code Assistant.
      - name: Execution Environments
        description: Containerized automation runtime environments for consistent and portable execution.
      - name: Automation Mesh
        description: Distributed automation execution architecture for scaling across global infrastructure.
  - type: UseCases
    data:
      - name: Enterprise IT Automation
        description: Standardize and scale IT automation across the enterprise with governance and compliance controls.
      - name: Hybrid Cloud Management
        description: Automate infrastructure provisioning and management across on-premises and multi-cloud environments.
      - name: Security Automation
        description: Automated security response and compliance enforcement with event-driven remediation.
      - name: Edge Computing
        description: Manage and automate edge infrastructure at scale with automation mesh and execution environments.
      - name: Self-Service IT
        description: Enable self-service automation ordering through the services catalog with approval workflows.
  - type: Integrations
    data:
      - name: Red Hat OpenShift
        description: Container platform integration for deploying and managing Ansible on Kubernetes.
      - name: Red Hat Satellite
        description: Content management and patching integration for RHEL infrastructure automation.
      - name: ServiceNow
        description: ITSM integration for change management and incident remediation workflows.
      - name: AWS
        description: Cloud automation for AWS services with certified content collections.
      - name: Microsoft Azure
        description: Cloud automation for Azure services with certified content collections.
      - name: Google Cloud
        description: Cloud automation for GCP services with certified content collections.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---

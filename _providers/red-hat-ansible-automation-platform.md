---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: 'Enterprise REST API for the Red Hat Ansible Automation Controller providing centralized management of automation jobs, workflows, inventories, credentials, and RBAC with enterprise authentication and '
  name: Red Hat Ansible Automation Controller API
  slug: controller-api
- description: REST API for managing a private instance of Ansible Automation Hub, enabling organizations to curate, publish, and distribute certified and custom Ansible content collections within their enterprise.
  name: Red Hat Ansible Private Automation Hub API
  slug: private-hub-api
- description: 'REST API for the Event-Driven Ansible Controller enabling management of event sources, rulebook activations, decision environments, and automated response workflows for infrastructure and application '
  name: Red Hat Event-Driven Ansible Controller API
  slug: eda-controller-api
- description: REST API for the Automation Services Catalog providing a self-service portal where users can order and manage pre-approved automation services with governance controls and approval workflows.
  name: Red Hat Automation Services Catalog API
  slug: services-catalog-api
artifact_total: 26
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/red-hat-ansible-automation-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/red-hat-ansible-automation-platform-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ansible
- group: start
  title: ''
  type: Portal
  url: https://www.redhat.com/en/technologies/management/ansible
- group: docs
  title: ''
  type: Documentation
  url: https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.redhat.com/en/technologies/management/ansible/trial
- group: company
  title: ''
  type: Blog
  url: https://www.ansible.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ansible
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- group: learn
  title: ''
  type: Training
  url: https://www.redhat.com/en/services/training/do007-ansible-essentials-simplicity-automation-technical-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.redhat.com/en/technologies/management/ansible/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redhat.com/
created: '2024-01-01'
description: Red Hat Ansible Automation Platform is an enterprise automation solution that provides a framework for building and operating IT automation at scale. It includes the Automation Controller, Automation Hub, Event-Driven Ansible, and Ansible Lightspeed with IBM watsonx Code Assistant, providing REST APIs for managing automation across hybrid cloud infrastructure.
features:
- description: Centralized management of automation with RBAC, audit logging, and credential management.
  name: Enterprise Automation Controller
- description: Curate and distribute certified and custom Ansible content collections within the enterprise.
  name: Private Automation Hub
- description: Automated response to infrastructure events using rulebook activations and event sources.
  name: Event-Driven Automation
- description: AI-powered automation content generation with IBM watsonx Code Assistant.
  name: Ansible Lightspeed
- description: Containerized automation runtime environments for consistent and portable execution.
  name: Execution Environments
- description: Distributed automation execution architecture for scaling across global infrastructure.
  name: Automation Mesh
finops:
- name: Red Hat Ansible Automation Platform Finops
  service_category: API
  slug: red-hat-ansible-automation-platform-finops
image: /assets/icons/red-hat-ansible-automation-platform.png
integrations:
- description: Container platform integration for deploying and managing Ansible on Kubernetes.
  name: Red Hat OpenShift
- description: Content management and patching integration for RHEL infrastructure automation.
  name: Red Hat Satellite
- description: ITSM integration for change management and incident remediation workflows.
  name: ServiceNow
- description: Cloud automation for AWS services with certified content collections.
  name: AWS
- description: Cloud automation for Azure services with certified content collections.
  name: Microsoft Azure
- description: Cloud automation for GCP services with certified content collections.
  name: Google Cloud
layout: provider
modified: '2026-04-18'
name: Red Hat Ansible Automation Platform
nav: Providers
network: true
overview: 'Red Hat Ansible Automation Platform publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Configuration Management, DevOps, Enterprise, and Red Hat.


  Red Hat Ansible Automation Platform''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, support, training material, pricing, and 7 more developer resources.'
plans:
- name: Red Hat Ansible Automation Platform Plans Pricing
  plan_count: 3
  slug: red-hat-ansible-automation-platform-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Red Hat Ansible Automation Platform Rate Limits
  slug: red-hat-ansible-automation-platform-rate-limits
score:
  band: thin
  composite: 27.4
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 27.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/screenshots/red-hat-ansible-automation-platform-2026-06-20T192716.png
security:
- kind: domain-security
  name: Red Hat Ansible Automation Platform Domain Security
  slug: red-hat-ansible-automation-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Red Hat Ansible Automation Platform Vulnerability Disclosure
  slug: red-hat-ansible-automation-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: red-hat-ansible-automation-platform
tags:
- Automation
- Configuration Management
- DevOps
- Enterprise
- Red Hat
use_cases:
- description: Standardize and scale IT automation across the enterprise with governance and compliance controls.
  name: Enterprise IT Automation
- description: Automate infrastructure provisioning and management across on-premises and multi-cloud environments.
  name: Hybrid Cloud Management
- description: Automated security response and compliance enforcement with event-driven remediation.
  name: Security Automation
- description: Manage and automate edge infrastructure at scale with automation mesh and execution environments.
  name: Edge Computing
- description: Enable self-service automation ordering through the services catalog with approval workflows.
  name: Self-Service IT
website: https://www.redhat.com/en/technologies/management/ansible
---

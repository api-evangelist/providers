---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ansible Automation Platform Agentic Access
  operation_count: 5
  slug: ansible-automation-platform-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 8
apis:
- description: RESTful API for the Ansible Automation Controller (formerly Ansible Tower) providing programmatic access to job templates, workflows, inventories, credentials, projects, and job execution. Supports CR
  name: Ansible Automation Controller API
  slug: controller-api
- description: REST API for Ansible Automation Hub providing access to certified and validated Ansible content collections, roles, and execution environments. Supports searching, downloading, and publishing automati
  name: Ansible Automation Hub API
  slug: hub-api
- description: API for Event-Driven Ansible (EDA) Controller enabling management of rulebooks, activations, and event sources for automated response to infrastructure and application events.
  name: Ansible Event-Driven Automation API
  slug: event-driven-api
- description: REST API for Ansible Galaxy, the community hub for sharing Ansible roles and collections. Supports searching, downloading, and rating community automation content.
  name: Ansible Galaxy API
  slug: galaxy-api
- description: Manage inventories
  name: Ansible Automation Platform Inventories API
  slug: ansible-automation-platform-inventories-api
- description: Manage job templates
  name: Ansible Automation Platform Job Templates API
  slug: ansible-automation-platform-job-templates-api
- description: Manage and execute jobs
  name: Ansible Automation Platform Jobs API
  slug: ansible-automation-platform-jobs-api
- description: Manage projects
  name: Ansible Automation Platform Projects API
  slug: ansible-automation-platform-projects-api
artifact_total: 33
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ansible-automation-platform-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ansible-automation-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ansible-automation-platform-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ansible
- group: start
  title: ''
  type: Portal
  url: https://docs.ansible.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ansible.com/automation-controller/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ansible.com/ansible/latest/getting_started/
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
  url: https://access.redhat.com/products/ansible-automation-platform
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
  url: https://www.ansible.com/products/training-certification
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/ansibleautomation
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/ansible
- group: commercial
  title: ''
  type: Pricing
  url: https://www.redhat.com/en/technologies/management/ansible/pricing
created: '2024-01-01'
description: Ansible Automation Platform (formerly Ansible Tower) provides a REST API for managing automation workflows, job templates, inventories, credentials, and projects. The API enables programmatic access to the automation controller for launching jobs, managing infrastructure inventory, and orchestrating complex multi-tier deployments across hybrid cloud environments.
features:
- description: Define and manage reusable automation job templates with variables, credentials, and inventory assignments.
  name: Job Template Management
- description: Build multi-step automation workflows with conditional logic, error handling, and approval gates.
  name: Workflow Orchestration
- description: Manage dynamic and static inventories of infrastructure hosts with grouping and variable assignment.
  name: Inventory Management
- description: Fine-grained access control for automation resources with teams, users, and permission assignments.
  name: Role-Based Access Control
- description: Automatically respond to infrastructure events with rulebook-driven automation triggers.
  name: Event-Driven Automation
- description: Discover, install, and manage certified Ansible content collections from Automation Hub.
  name: Content Collections
finops:
- name: Ansible Automation Platform Finops
  service_category: API
  slug: ansible-automation-platform-finops
image: /assets/icons/ansible-automation-platform.png
integrations:
- description: Integration with Red Hat Satellite for content management and patch automation.
  name: Red Hat Satellite
- description: ITSM integration for change management approval workflows and incident remediation.
  name: ServiceNow
- description: Cloud automation modules for AWS services including EC2, S3, RDS, and CloudFormation.
  name: AWS
- description: Cloud automation modules for Azure services including VMs, AKS, and Azure Resource Manager.
  name: Azure
- description: Infrastructure as code integration for provisioning with Terraform and configuring with Ansible.
  name: Terraform
- description: CI/CD pipeline integration for automated deployment workflows triggered by Jenkins.
  name: Jenkins
jsonld:
- class_count: 3
  name: Ansible Automation Platform Context
  property_count: 9
  slug: ansible-automation-platform-context
layout: provider
modified: '2026-05-19'
name: Ansible Automation Platform
nav: Providers
network: true
overview: 'Ansible Automation Platform publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Inventories API, Job Templates API, Jobs API, and 1 more. Tagged areas include Automation, Configuration Management, DevOps, Infrastructure as Code, and Orchestration.


  The Ansible Automation Platform catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ansible Automation Platform''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, training material, and 9 more developer resources.'
plans:
- name: Ansible Automation Platform Plans Pricing
  plan_count: 3
  slug: ansible-automation-platform-plans-pricing
random_paper: 114
rate_limits:
- limit_count: 5
  name: Ansible Automation Platform Rate Limits
  slug: ansible-automation-platform-rate-limits
rules:
- name: Ansible Automation Platform API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 7
  slug: ansible-automation-platform-spectral-rules
score:
  band: thin
  composite: 34.6
  delta: -8.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 17.4
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 20.8
    operational_transparency: 13.2
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ansible-automation-platform/refs/heads/main/screenshots/ansible-automation-platform-2026-06-20T172017.png
security:
- kind: authentication
  name: Ansible Automation Platform Authentication
  slug: ansible-automation-platform-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ansible Automation Platform Domain Security
  slug: ansible-automation-platform-domain-security
  summary_line: TLSv1.3
slug: ansible-automation-platform
tags:
- Automation
- Configuration Management
- DevOps
- Infrastructure as Code
- Orchestration
use_cases:
- description: Automate provisioning of servers, networks, and cloud resources across hybrid environments.
  name: Infrastructure Provisioning
- description: Maintain consistent configuration across thousands of servers with idempotent automation.
  name: Configuration Management
- description: Automate application deployment pipelines with rolling updates and rollback capabilities.
  name: Application Deployment
- description: Enforce security policies and compliance standards through automated remediation workflows.
  name: Security Compliance
- description: Automate network device configuration and management across multi-vendor environments.
  name: Network Automation
website: https://docs.ansible.com/
---

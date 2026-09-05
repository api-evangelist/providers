---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
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
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: Manage inventories
  name: Ansible Automation Platform Inventories API
  slug: ansible-automation-platform-inventories-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: Manage job templates
  name: Ansible Automation Platform Job Templates API
  slug: ansible-automation-platform-job-templates-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: Manage and execute jobs
  name: Ansible Automation Platform Jobs API
  slug: ansible-automation-platform-jobs-api
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: Manage projects
  name: Ansible Automation Platform Projects API
  slug: ansible-automation-platform-projects-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ansible Automation Controller Inventories API
  slug: open-ansible-automation-platform-inventories-api
- collection_type: open
  name: Ansible Automation Controller Inventories Job Templates API
  slug: open-ansible-automation-platform-job-templates-api
- collection_type: open
  name: Ansible Automation Controller Inventories Jobs API
  slug: open-ansible-automation-platform-jobs-api
- collection_type: open
  name: Ansible Automation Controller Inventories Projects API
  slug: open-ansible-automation-platform-projects-api
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
random_paper: 10
rate_limits:
- limit_count: 5
  name: Ansible Automation Platform Rate Limits
  slug: ansible-automation-platform-rate-limits
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Ansible Automation Platform API Rules
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
  coverage:
    artifact_dirs: 12
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 11.4
    contract_quality: 16.2
    developer_ergonomics: 54.8
    discoverability: 74.1
    governance: 11.4
    operational_transparency: 10.5
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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

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
  band: agent-ready
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Ansible Agentic Access
  operation_count: 33
  slug: ansible-agentic-access
  summary_line: 33 operations · 15 acting
api_count: 16
apis:
- description: RESTful API for Ansible Automation Platform (formerly Ansible Tower) that provides programmatic access to job templates, inventories, credentials, workflow templates, schedules, notifications, and job
  name: Ansible Automation Platform API
  slug: ansible-automation-platform-api
- description: AWX is the open-source upstream project for Ansible Automation Platform, providing a web-based UI, REST API, and task engine for Ansible under the Apache 2.0 license. The AWX API mirrors the AAP API s
  name: AWX API
  slug: awx-api
- description: REST API for Ansible Galaxy — the community hub for sharing and downloading Ansible roles and collections. The v1 API covers roles and the v3 API covers collections with namespace management, versioni
  name: Ansible Galaxy API
  slug: ansible-galaxy-api
- description: The Red Hat Ansible Automation Hub API provides access to certified Ansible collections and roles curated by Red Hat and partners. Available through console.redhat.com, it serves certified content for
  name: Ansible Automation Hub API
  slug: ansible-automation-hub-api
- description: OAuth2 token management.
  name: Ansible Auth API
  slug: ansible-auth-api
- description: The Credentials API from Ansible — 1 operation(s) for credentials.
  name: Ansible Credentials API
  slug: ansible-credentials-api
- description: The Hosts API from Ansible — 1 operation(s) for hosts.
  name: Ansible Hosts API
  slug: ansible-hosts-api
- description: The Inventories API from Ansible — 2 operation(s) for inventories.
  name: Ansible Inventories API
  slug: ansible-inventories-api
- description: The Job Templates API from Ansible — 3 operation(s) for job templates.
  name: Ansible Job Templates API
  slug: ansible-job-templates-api
- description: The Jobs API from Ansible — 4 operation(s) for jobs.
  name: Ansible Jobs API
  slug: ansible-jobs-api
- description: The Organizations API from Ansible — 2 operation(s) for organizations.
  name: Ansible Organizations API
  slug: ansible-organizations-api
- description: The Projects API from Ansible — 3 operation(s) for projects.
  name: Ansible Projects API
  slug: ansible-projects-api
- description: The Schedules API from Ansible — 1 operation(s) for schedules.
  name: Ansible Schedules API
  slug: ansible-schedules-api
- description: The Users API from Ansible — 1 operation(s) for users.
  name: Ansible Users API
  slug: ansible-users-api
- description: The Workflow Job Templates API from Ansible — 2 operation(s) for workflow job templates.
  name: Ansible Workflow Job Templates API
  slug: ansible-workflow-job-templates-api
- description: The Workflow Jobs API from Ansible — 1 operation(s) for workflow jobs.
  name: Ansible Workflow Jobs API
  slug: ansible-workflow-jobs-api
artifact_total: 58
collections:
- collection_type: postman
  name: Ansible Automation Controller Auth API
  slug: postman-ansible-auth-api
- collection_type: postman
  name: Ansible Automation Controller Auth Credentials API
  slug: postman-ansible-credentials-api
- collection_type: postman
  name: Ansible Automation Controller Auth Hosts API
  slug: postman-ansible-hosts-api
- collection_type: postman
  name: Ansible Automation Controller Auth Inventories API
  slug: postman-ansible-inventories-api
- collection_type: postman
  name: Ansible Automation Controller Auth Job Templates API
  slug: postman-ansible-job-templates-api
- collection_type: postman
  name: Ansible Automation Controller Auth Jobs API
  slug: postman-ansible-jobs-api
- collection_type: postman
  name: Ansible Automation Controller Auth Organizations API
  slug: postman-ansible-organizations-api
- collection_type: postman
  name: Ansible Automation Controller Auth Projects API
  slug: postman-ansible-projects-api
- collection_type: postman
  name: Ansible Automation Controller Auth Schedules API
  slug: postman-ansible-schedules-api
- collection_type: postman
  name: Ansible Automation Controller Auth Users API
  slug: postman-ansible-users-api
- collection_type: postman
  name: Ansible Automation Controller Auth Workflow Job Templates API
  slug: postman-ansible-workflow-job-templates-api
- collection_type: postman
  name: Ansible Automation Controller Auth Workflow Jobs API
  slug: postman-ansible-workflow-jobs-api
- collection_type: open
  name: Ansible Automation Controller API
  slug: open-ansible
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ansible/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ansible-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ansible-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ansible-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ansible-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ansible
- group: start
  title: ''
  type: Portal
  url: https://www.ansible.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ansible.com/ansible/latest/getting_started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ansible.com/
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
  type: Forums
  url: https://forum.ansible.com/
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/products/red-hat-ansible-automation-platform/
- group: learn
  title: ''
  type: Training
  url: https://www.ansible.com/products/training-certification
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- group: build
  title: Ansible Python Package
  type: SDKs
  url: https://pypi.org/project/ansible/
- group: build
  title: Ansible Runner Python Package
  type: SDKs
  url: https://pypi.org/project/ansible-runner/
- group: docs
  title: Playbook Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ansible/refs/heads/main/json-schema/ansible-playbook-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ansible/refs/heads/main/vocabulary/ansible-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/ansible/aap-mcp-server
created: '2024-01-01'
description: Ansible is an open-source IT automation platform developed by Red Hat that provides agentless configuration management, application deployment, cloud provisioning, and orchestration. Using YAML-based playbooks and an SSH-native architecture, Ansible automates infrastructure at scale without requiring agents or custom security infrastructure on managed nodes.
examples:
- key_count: 10
  name: Ansible Playbook Example
  slug: ansible-playbook-example
features:
- description: Ansible connects to managed nodes via SSH or WinRM without requiring any agent software, simplifying deployment and reducing attack surface.
  name: Agentless Architecture
- description: Automation is defined in human-readable YAML playbooks that describe the desired state of managed systems without complex programming.
  name: YAML Playbooks
- description: Ansible tasks are idempotent — running the same playbook multiple times produces the same result, making deployments safe to rerun.
  name: Idempotent Execution
- description: Over 3,000 built-in modules covering cloud providers, network devices, databases, containers, storage, and operating system tasks.
  name: Module Ecosystem
- description: The Ansible Collections packaging format bundles related modules, roles, plugins, and documentation for modular content distribution.
  name: Collection System
- description: Query cloud providers, CMDBs, and external systems dynamically to build host inventories at execution time rather than static files.
  name: Dynamic Inventory
finops:
- name: Ansible Finops
  service_category: API
  slug: ansible-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ansible.png
integrations:
- description: Ansible is the primary configuration management tool for Red Hat Enterprise Linux systems with deep integration into the RHEL platform.
  name: Red Hat Enterprise Linux
- description: Manage Kubernetes clusters, namespaces, deployments, and OpenShift workloads using the kubernetes.core collection.
  name: Kubernetes / OpenShift
- description: Combine Terraform for cloud resource provisioning with Ansible for post-provisioning OS and application configuration.
  name: Terraform
- description: Integrate Ansible playbook execution into CI/CD pipelines using the AAP Action for GitHub or Ansible Tower Plugin for Jenkins.
  name: Jenkins / GitHub Actions
- description: Trigger Ansible automation from ServiceNow ITSM workflows using the ServiceNow ITX collection for change management automation.
  name: ServiceNow
json_schemas:
- name: Playbook
  property_count: 10
  slug: ansible-playbook
json_structures:
- name: Ansible Playbook Structure
  property_count: 10
  slug: ansible-playbook-structure
jsonld:
- class_count: 4
  name: Ansible Context
  property_count: 10
  slug: ansible-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Ansible
nav: Providers
network: true
overview: 'Ansible publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Credentials API, Hosts API, and 9 more. Tagged areas include Ansible, Automation, Configuration Management, DevOps, and Infrastructure As Code.


  The Ansible catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ansible''s developer surface includes authentication, developer portal, getting-started guide, documentation, engineering blog, support, training material, and 14 more developer resources.'
plans:
- name: Ansible Plans Pricing
  plan_count: 3
  slug: ansible-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 5
  name: Ansible Rate Limits
  slug: ansible-rate-limits
rules:
- name: Ansible API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ansible-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 59.7
    developer_ergonomics: 65.2
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 60.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ansible/refs/heads/main/screenshots/ansible-2026-06-20T172015.png
security:
- kind: authentication
  name: Ansible Authentication
  slug: ansible-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Ansible Domain Security
  slug: ansible-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Ansible Vulnerability Disclosure
  slug: ansible-vulnerability-disclosure
  summary_line: disclosure policy published
slug: ansible
tags:
- Ansible
- Automation
- Configuration Management
- DevOps
- Infrastructure As Code
- Open Source
- Orchestration
- Red Hat
use_cases:
- description: Ensure servers and services remain in a consistent desired state by applying configuration playbooks across fleets of hosts.
  name: Configuration Management
- description: Deploy and update applications across development, staging, and production environments with zero-downtime rolling strategies.
  name: Application Deployment
- description: Provision cloud resources on AWS, Azure, GCP, and other providers using cloud-specific Ansible modules and dynamic inventory.
  name: Cloud Provisioning
- description: Configure routers, switches, and firewalls from Cisco, Juniper, Arista, and Palo Alto using vendor-specific Ansible collections.
  name: Network Automation
- description: Enforce security baselines, CIS benchmarks, and STIG compliance across infrastructure using Ansible hardening playbooks.
  name: Security and Compliance
website: https://www.ansible.com
---

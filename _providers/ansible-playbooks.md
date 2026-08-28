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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Ansible Playbooks Agentic Access
  operation_count: 33
  slug: ansible-playbooks-agentic-access
  summary_line: 33 operations · 15 acting
api_count: 18
apis:
- description: REST API for Ansible Automation Platform (formerly Ansible Tower/AWX) to manage playbooks, inventories, credentials, job templates, and job execution at enterprise scale. Supports RBAC, workflows, sch
  name: Ansible Automation Platform API
  slug: ansible-automation-platform-api
- description: AWX is the open-source upstream project for Ansible Automation Platform, providing a web-based UI, REST API, and task engine for Ansible. The AWX API offers programmatic access to job execution, inven
  name: AWX API
  slug: awx-api
- description: 'Ansible Runner is a Python library and CLI tool that provides a stable and consistent interface for executing Ansible playbooks programmatically from within other applications and tools. Used by AWX, '
  name: Ansible Runner API
  slug: ansible-runner-api
- description: 'Ansible Galaxy is the community hub for sharing Ansible roles and collections. The Galaxy REST API enables searching, downloading, and publishing Ansible content. Supports v1 (roles), v2 (mixed), and '
  name: Ansible Galaxy API
  slug: ansible-galaxy-api
- description: Red Hat Ansible Automation Hub is the enterprise content hub for certified Ansible collections, roles, and execution environments. The API provides access to Red Hat certified and partner-validated An
  name: Ansible Automation Hub API
  slug: ansible-automation-hub-api
- description: Ansible Semaphore is an open-source modern web UI and REST API for running Ansible playbooks. It provides project management, task scheduling, access control, and a clean interface for teams using Ans
  name: Ansible Semaphore API
  slug: ansible-semaphore-api
- description: OAuth2 token management.
  name: Ansible Playbooks Auth API
  slug: ansible-playbooks-auth-api
- description: The Credentials API from Ansible Playbooks — 1 operation(s) for credentials.
  name: Ansible Playbooks Credentials API
  slug: ansible-playbooks-credentials-api
- description: The Hosts API from Ansible Playbooks — 1 operation(s) for hosts.
  name: Ansible Playbooks Hosts API
  slug: ansible-playbooks-hosts-api
- description: The Inventories API from Ansible Playbooks — 2 operation(s) for inventories.
  name: Ansible Playbooks Inventories API
  slug: ansible-playbooks-inventories-api
- description: The Job Templates API from Ansible Playbooks — 3 operation(s) for job templates.
  name: Ansible Playbooks Job Templates API
  slug: ansible-playbooks-job-templates-api
- description: The Jobs API from Ansible Playbooks — 4 operation(s) for jobs.
  name: Ansible Playbooks Jobs API
  slug: ansible-playbooks-jobs-api
- description: The Organizations API from Ansible Playbooks — 2 operation(s) for organizations.
  name: Ansible Playbooks Organizations API
  slug: ansible-playbooks-organizations-api
- description: The Projects API from Ansible Playbooks — 3 operation(s) for projects.
  name: Ansible Playbooks Projects API
  slug: ansible-playbooks-projects-api
- description: The Schedules API from Ansible Playbooks — 1 operation(s) for schedules.
  name: Ansible Playbooks Schedules API
  slug: ansible-playbooks-schedules-api
- description: The Users API from Ansible Playbooks — 1 operation(s) for users.
  name: Ansible Playbooks Users API
  slug: ansible-playbooks-users-api
- description: The Workflow Job Templates API from Ansible Playbooks — 2 operation(s) for workflow job templates.
  name: Ansible Playbooks Workflow Job Templates API
  slug: ansible-playbooks-workflow-job-templates-api
- description: The Workflow Jobs API from Ansible Playbooks — 1 operation(s) for workflow jobs.
  name: Ansible Playbooks Workflow Jobs API
  slug: ansible-playbooks-workflow-jobs-api
artifact_total: 62
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth API
  slug: open-ansible-playbooks-auth-api
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth Credentials API
  slug: open-ansible-playbooks-credentials-api
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth Hosts API
  slug: open-ansible-playbooks-hosts-api
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth Inventories API
  slug: open-ansible-playbooks-inventories-api
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth Job Templates API
  slug: open-ansible-playbooks-job-templates-api
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth Jobs API
  slug: open-ansible-playbooks-jobs-api
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth Organizations API
  slug: open-ansible-playbooks-organizations-api
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth Projects API
  slug: open-ansible-playbooks-projects-api
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth Schedules API
  slug: open-ansible-playbooks-schedules-api
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth Users API
  slug: open-ansible-playbooks-users-api
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth Workflow Job Templates API
  slug: open-ansible-playbooks-workflow-job-templates-api
- collection_type: open
  name: Ansible Automation Controller Playbooks Auth Workflow Jobs API
  slug: open-ansible-playbooks-workflow-jobs-api
- collection_type: open
  name: Ansible Automation Controller Playbooks API
  slug: open-ansible-playbooks
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ansible/awx/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/ansible/awx/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/ansible/awx/blob/devel/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/ansible/awx/blob/devel/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/ansible/awx/blob/devel/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ansible-playbooks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ansible-playbooks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ansible-playbooks-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ansible.com/ansible/latest/getting_started/
- group: other
  title: ''
  type: BestPractices
  url: https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html
- group: company
  title: ''
  type: Blog
  url: https://www.ansible.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ansible
- group: operate
  title: ''
  type: Forums
  url: https://forum.ansible.com/
- group: docs
  title: Playbook Job Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ansible-playbooks/refs/heads/main/json-schema/ansible-playbooks-playbook-job-schema.json
- group: docs
  title: Inventory Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ansible-playbooks/refs/heads/main/json-schema/ansible-playbooks-inventory-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ansible-playbooks/refs/heads/main/vocabulary/ansible-playbooks-vocabulary.yaml
created: '2024-01-15'
description: A curated collection of APIs, tools, and platforms for managing and executing Ansible playbooks for IT automation, configuration management, and orchestration. Covers the Ansible Automation Platform, AWX, Galaxy, Automation Hub, Runner, and Semaphore APIs that power modern infrastructure automation workflows.
examples:
- key_count: 13
  name: Ansible Playbooks Inventory Example
  slug: ansible-playbooks-inventory-example
- key_count: 17
  name: Ansible Playbooks Playbook Job Example
  slug: ansible-playbooks-playbook-job-example
features:
- description: Launch, monitor, and cancel Ansible playbook runs programmatically via REST API with support for extra vars, limits, and tags.
  name: Playbook Execution via API
- description: Create and manage dynamic and static inventories with groups, hosts, and host variables through the API.
  name: Inventory Management
- description: Securely store SSH keys, cloud credentials, and vault passwords in encrypted credential objects accessible to jobs.
  name: Credential Storage
- description: Chain multiple job templates into orchestrated workflows with conditional success/failure branching.
  name: Workflow Templates
- description: Schedule playbook runs on recurring schedules using rrule-based calendar expressions.
  name: Scheduling
- description: Discover, download, and manage Ansible collections and roles from Galaxy, Automation Hub, or private repositories.
  name: Collections and Role Management
finops:
- name: Ansible Playbooks Finops
  service_category: API
  slug: ansible-playbooks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ansible-playbooks.png
integrations:
- description: Deploy and configure OpenShift clusters and workloads using Ansible Automation Platform integrated with OpenShift pipelines.
  name: Red Hat OpenShift
- description: Trigger Ansible job templates from ServiceNow ITSM workflows for automated ticket remediation and change management.
  name: ServiceNow
- description: Use the Ansible Automation Platform GitHub Action to trigger playbook runs as part of GitHub CI/CD workflows.
  name: GitHub Actions
- description: Combine Terraform for infrastructure provisioning with Ansible for post-provisioning configuration management.
  name: Terraform
- description: Use Ansible collections to configure Splunk deployments and automate security alert remediation workflows.
  name: Splunk
json_schemas:
- name: Inventory
  property_count: 13
  slug: ansible-playbooks-inventory
- name: PlaybookJob
  property_count: 17
  slug: ansible-playbooks-playbook-job
json_structures:
- name: Ansible Playbooks Inventory Structure
  property_count: 13
  slug: ansible-playbooks-inventory-structure
- name: Ansible Playbooks Playbook Job Structure
  property_count: 17
  slug: ansible-playbooks-playbook-job-structure
jsonld:
- class_count: 4
  name: Ansible Playbooks Context
  property_count: 20
  slug: ansible-playbooks-context
layout: provider
modified: '2026-04-19'
name: Ansible Playbooks
nav: Providers
network: true
overview: 'Ansible Playbooks publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Credentials API, Hosts API, and 9 more. Tagged areas include Ansible, Automation, Configuration Management, DevOps, and Infrastructure as Code.


  The Ansible Playbooks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ansible Playbooks'' developer surface includes authentication, getting-started guide, engineering blog, and 15 more developer resources.'
plans:
- name: Ansible Playbooks Plans Pricing
  plan_count: 3
  slug: ansible-playbooks-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Ansible Playbooks Rate Limits
  slug: ansible-playbooks-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Ansible Playbooks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ansible-playbooks-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.4
  delta: 6.7
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 25.0
    contract_quality: 53.7
    developer_ergonomics: 61.9
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/ansible-playbooks/refs/heads/main/screenshots/ansible-playbooks-2026-06-20T172018.png
security:
- kind: authentication
  name: Ansible Playbooks Authentication
  slug: ansible-playbooks-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Ansible Playbooks Domain Security
  slug: ansible-playbooks-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ansible-playbooks
tags:
- Ansible
- Automation
- Configuration Management
- DevOps
- Infrastructure as Code
- Orchestration
- Playbooks
use_cases:
- description: Automate the provisioning of cloud resources, VMs, and bare-metal servers using Ansible playbooks triggered via API.
  name: Infrastructure Provisioning
- description: Enforce consistent configuration state across server fleets by scheduling and executing configuration playbooks via API.
  name: Configuration Management
- description: Trigger Ansible playbook runs as deployment steps within Jenkins, GitLab CI, GitHub Actions, and other CI/CD platforms.
  name: CI/CD Pipeline Integration
- description: Run compliance playbooks on demand or on schedule to detect and remediate drift from desired security baseline states.
  name: Compliance and Remediation
- description: Automate network device configuration, firmware upgrades, and compliance checks using Ansible network collections via the API.
  name: Network Automation
---

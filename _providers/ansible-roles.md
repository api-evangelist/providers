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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ansible Roles Agentic Access
  operation_count: 18
  slug: ansible-roles-agentic-access
  summary_line: 18 operations · 3 acting
api_count: 10
apis:
- description: The Ansible Galaxy v1 and v2 REST API enables searching, discovering, and downloading Ansible roles contributed by the community. Supports searching roles by keyword, author, or tag; retrieving role d
  name: Ansible Galaxy Roles API
  slug: ansible-galaxy-roles-api
- description: The Ansible Galaxy v3 API provides enhanced support for Ansible collections — the modern packaging format that bundles roles, modules, plugins, and documentation together. Supports listing, searching,
  name: Ansible Galaxy Collections API
  slug: ansible-galaxy-collections-api
- description: The Red Hat Ansible Automation Hub provides certified and partner-validated Ansible collections and roles for enterprise use. The API enables access to Red Hat-certified content with SLA-backed qualit
  name: Ansible Automation Hub Roles API
  slug: ansible-automation-hub-roles-api
- description: The Ansible Galaxy Roles & Collections API API from Ansible Roles — 2 operation(s) for ansible galaxy roles & collections api.
  name: Ansible Roles Ansible Galaxy Roles & Collections API API
  slug: ansible-roles-ansible-galaxy-roles-collections-api-api
- description: Modern v3 collections (Galaxy NG / Pulp).
  name: Ansible Roles Collections API
  slug: ansible-roles-collections-api
- description: Track role import job status.
  name: Ansible Roles Imports API
  slug: ansible-roles-imports-api
- description: Legacy v1 namespaces (mapped from GitHub orgs/users).
  name: Ansible Roles Namespaces API
  slug: ansible-roles-namespaces-api
- description: Legacy v1 community roles API.
  name: Ansible Roles Roles API
  slug: ansible-roles-roles-api
- description: Trigger legacy content sync.
  name: Ansible Roles Sync API
  slug: ansible-roles-sync-api
- description: Legacy v1 users API.
  name: Ansible Roles Users API
  slug: ansible-roles-users-api
artifact_total: 37
collections:
- collection_type: open
  name: Ansible Galaxy Roles & Collections API
  slug: open-ansible-roles
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ansible-roles-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ansible-roles-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ansible-roles-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ansible.com/ansible/latest/galaxy/user_guide.html
- group: auth
  title: ''
  type: Authentication
  url: https://galaxy.ansible.com/docs/authentication/
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
  type: GitHubRepository
  url: https://github.com/ansible/galaxy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ansible
- group: docs
  title: Role Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ansible-roles/refs/heads/main/json-schema/ansible-roles-role-schema.json
- group: docs
  title: Collection Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ansible-roles/refs/heads/main/json-schema/ansible-roles-collection-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ansible-roles/refs/heads/main/vocabulary/ansible-roles-vocabulary.yaml
created: '2024-01-01'
description: A curated collection of APIs and resources for discovering, managing, and consuming Ansible roles — the primary unit of reusable automation content in the Ansible ecosystem. Covers the Galaxy and Automation Hub APIs for role discovery, download, and publishing, as well as the Ansible Collections framework that has extended the role model into full-featured content packages.
examples:
- key_count: 13
  name: Ansible Roles Collection Example
  slug: ansible-roles-collection-example
- key_count: 15
  name: Ansible Roles Role Example
  slug: ansible-roles-role-example
features:
- description: Search Galaxy for community-contributed roles by keyword, author, namespace, or tag to find reusable automation content.
  name: Role Search and Discovery
- description: Bundle roles, modules, plugins, and documentation into distributable collection packages versioned and published via the Galaxy API.
  name: Collection Packaging
- description: Access specific versions of roles and collections, enabling pinned dependency management in Ansible projects.
  name: Version Management
- description: Access Red Hat-certified and partner-validated Ansible collections with enterprise-grade quality assurance via Automation Hub.
  name: Certified Content
- description: Manage author namespaces on Galaxy to publish and maintain role and collection content under a consistent identity.
  name: Namespace Management
finops:
- name: Ansible Roles Finops
  service_category: API
  slug: ansible-roles-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ansible-roles.png
integrations:
- description: Use roles discovered via the Galaxy API directly in Ansible playbooks with the roles directive or include_role task.
  name: Ansible Playbooks
- description: Synchronize collections from Galaxy or Automation Hub into Ansible Automation Platform for use in job templates.
  name: Ansible Automation Platform
- description: Define role and collection dependencies in requirements.yml and install them automatically via ansible-galaxy CLI using the API.
  name: Requirements Files
json_schemas:
- name: Collection
  property_count: 13
  slug: ansible-roles-collection
- name: Role
  property_count: 15
  slug: ansible-roles-role
json_structures:
- name: Ansible Roles Collection Structure
  property_count: 13
  slug: ansible-roles-collection-structure
- name: Ansible Roles Role Structure
  property_count: 15
  slug: ansible-roles-role-structure
jsonld:
- class_count: 4
  name: Ansible Roles Context
  property_count: 16
  slug: ansible-roles-context
layout: provider
modified: '2026-04-19'
name: Ansible Roles
nav: Providers
network: true
overview: 'Ansible Roles publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Ansible Galaxy Roles & Collections API API, Collections API, Imports API, and 4 more. Tagged areas include Ansible, Automation, Collections, Configuration Management, and DevOps.


  The Ansible Roles catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ansible Roles'' developer surface includes authentication, getting-started guide, and 10 more developer resources.'
plans:
- name: Ansible Roles Plans Pricing
  plan_count: 3
  slug: ansible-roles-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Ansible Roles Rate Limits
  slug: ansible-roles-rate-limits
rules:
- name: Ansible Roles API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ansible-roles-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.5
  delta: -4.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 58.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ansible-roles/refs/heads/main/screenshots/ansible-roles-2026-06-20T172023.png
security:
- kind: authentication
  name: Ansible Roles Authentication
  slug: ansible-roles-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ansible Roles Domain Security
  slug: ansible-roles-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ansible-roles
tags:
- Ansible
- Automation
- Collections
- Configuration Management
- DevOps
- Infrastructure As Code
- Roles
use_cases:
- description: Discover and install community roles from Galaxy to avoid reinventing automation logic for common tasks like nginx, MySQL, or Kubernetes setup.
  name: Role Reuse Across Projects
- description: Use Red Hat-certified collections from Automation Hub in production environments where quality assurance and support are required.
  name: Certified Enterprise Automation
- description: Publish internal roles and collections to a private Automation Hub instance for controlled distribution within an organization.
  name: Private Content Distribution
- description: Pin role and collection versions in requirements.yml files and install them via the Galaxy API in CI/CD pipelines.
  name: Dependency Management
---

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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.0
  scored_at: '2026-09-02'
api_count: 7
apis:
- baseURL: https://controller-host/api/v2/
  baseurl_source: declared
  description: 'Enterprise REST API for the Red Hat Ansible Automation Controller providing centralized management of automation jobs, workflows, inventories, credentials, and RBAC with enterprise authentication and '
  name: Red Hat Ansible Automation Controller API
  slug: controller-api
- baseURL: https://hub-host/api/galaxy/
  baseurl_source: declared
  description: REST API for managing a private instance of Ansible Automation Hub, enabling organizations to curate, publish, and distribute certified and custom Ansible content collections within their enterprise.
  name: Red Hat Ansible Private Automation Hub API
  slug: private-hub-api
- baseURL: https://eda-host/api/eda/v1/
  baseurl_source: declared
  description: 'REST API for the Event-Driven Ansible Controller enabling management of event sources, rulebook activations, decision environments, and automated response workflows for infrastructure and application '
  name: Red Hat Event-Driven Ansible Controller API
  slug: eda-controller-api
- description: REST API for the Automation Services Catalog providing a self-service portal where users can order and manage pre-approved automation services with governance controls and approval workflows.
  name: Red Hat Automation Services Catalog API
  slug: services-catalog-api
- baseURL: https://gateway-host/api/gateway/v1/
  baseurl_source: declared
  description: REST API for the Ansible Automation Platform Gateway, the single front door introduced in AAP 2.5 that fronts every platform component. Manages users, teams, organizations, role definitions and assign
  name: Red Hat Ansible Automation Platform Gateway API
  slug: platform-gateway-api
- baseURL: https://lightspeed-instance/api/v1
  baseurl_source: declared
  description: REST API for Ansible Lightspeed, the generative AI service that produces and explains Ansible content. Provides playbook and role generation, content explanations, chat and streaming chat, content-mat
  name: Red Hat Ansible Lightspeed with IBM watsonx Code Assistant API
  slug: ansible-lightspeed-api
- baseURL: https://console.redhat.com/api/automation-hub/
  baseurl_source: declared
  description: The Red Hat-hosted Automation Hub on console.redhat.com, where subscribers consume Red Hat certified and validated Ansible Content Collections. Same galaxy_ng/Pulp contract as a private hub, served fr
  name: Red Hat Automation Hub API (Hybrid Cloud Console)
  slug: hosted-automation-hub-api
artifact_total: 34
asyncapis:
- description: ''
  name: Red Hat Ansible Automation Platform Webhooks
  slug: red-hat-ansible-automation-platform-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.redhat.com/en/technologies/management/ansible
- group: build
  title: ''
  type: SDKs
  url: packages/red-hat-ansible-automation-platform-packages.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/red-hat-ansible-automation-platform-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: security/red-hat-ansible-automation-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://access.redhat.com/compliance
- group: start
  title: ''
  type: Console
  url: https://www.redhat.com/en/interactive-labs/ansible
- group: commercial
  title: ''
  type: Plans
  url: plans/red-hat-ansible-automation-platform-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/red-hat-ansible-automation-platform-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/red-hat-ansible-automation-platform-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/red-hat-ansible-automation-platform-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/red-hat-ansible-automation-platform-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/red-hat-ansible-automation-platform-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/red-hat-ansible-automation-platform-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/red-hat-ansible-automation-platform-conventions.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/red-hat-ansible-automation-platform-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/red-hat-ansible-automation-platform-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/red-hat-ansible-automation-platform-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/red-hat-ansible-automation-platform-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/red-hat-ansible-automation-platform-llms.txt
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/red-hat-ansible-automation-platform-tool-crosswalk.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/red-hat-ansible-automation-platform-mcp.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/red-hat-ansible-automation-platform-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/red-hat-ansible-automation-platform-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/red-hat-ansible-automation-platform-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/red-hat-ansible-automation-platform-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/red-hat-ansible-automation-platform-scopes.yml
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
  url: https://www.redhat.com/en/blog/channel/red-hat-ansible-automation
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
mcp_servers:
- description: 'Red Hat ships a first-party Model Context Protocol server for Ansible Automation Platform. It is a Node.js service (Apache-2.0, github.com/ansible/aap-mcp-server) that reads the AAP component OpenAPI '
  name: AAP MCP Service
  slug: aap-mcp-service
modified: '2026-08-29'
name: Red Hat Ansible Automation Platform
nav: Providers
network: true
overview: 'Red Hat Ansible Automation Platform publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Red Hat Ansible Automation Controller API, Red Hat Ansible Private Automation Hub API, Red Hat Event-Driven Ansible Controller API, and 3 more. Tagged areas include Automation, Configuration Management, DevOps, Enterprise, and Red Hat.


  The Red Hat Ansible Automation Platform catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Red Hat Ansible Automation Platform''s developer surface includes developer console, sandbox, CLI, changelog, authentication, developer portal, documentation, and 34 more developer resources.'
plans:
- name: Red Hat Ansible Automation Platform Plans Pricing
  plan_count: 2
  slug: red-hat-ansible-automation-platform-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Red Hat Ansible Automation Platform Rate Limits
  slug: red-hat-ansible-automation-platform-rate-limits
scopes:
- name: Red Hat Ansible Automation Platform Scopes
  scope_count: 3
  slug: red-hat-ansible-automation-platform-scopes
  summary_line: 3 scopes · authorizationCode/password
score:
  band: strong
  composite: 62.8
  coverage:
    artifact_dirs: 24
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.9
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 52.9
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 61.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 16.7
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/red-hat-ansible-automation-platform/refs/heads/main/screenshots/red-hat-ansible-automation-platform-2026-06-20T192716.png
security:
- kind: authentication
  name: Red Hat Ansible Automation Platform Authentication
  slug: red-hat-ansible-automation-platform-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
- kind: domain-security
  name: Red Hat Ansible Automation Platform Domain Security
  slug: red-hat-ansible-automation-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Red Hat Ansible Automation Platform Vulnerability Disclosure
  slug: red-hat-ansible-automation-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Red Hat Ansible Automation Platform Trust Center
  slug: red-hat-ansible-automation-platform-trust-center
  summary_line: Common Criteria, FIPS 140, ISO/IEC 27001, ISO/IEC 27018, ISO 42001, ISO/SAE 21434, DISA STIG, HIPAA, HDS, CIS Benchmarks, BSI, CCN-STIC / ENS, EU Cyber Resilience Act, EU AI Act, Accessibility Conformance Reports (VPAT)
slug: red-hat-ansible-automation-platform
tags:
- Automation
- Configuration Management
- DevOps
- Enterprise
- Red Hat
- Ansible
- IT Operations
- Event-Driven Architecture
- Infrastructure as Code
- MCP
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

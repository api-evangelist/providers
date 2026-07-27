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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 7
  human_in_the_loop: 2
  name: Puppet Agentic Access
  operation_count: 12
  slug: puppet-agentic-access
  summary_line: 12 operations · 7 acting · 2 human-in-the-loop
api_count: 11
apis:
- description: The Orchestrator API enables you to gather details about orchestrator jobs you run and inspect application instances. It powers running tasks and orchestration workflows across PE-managed nodes.
  name: Puppet Enterprise Orchestrator API
  slug: orchestrator
- description: The RBAC Service API manages access to PE, generates authentication tokens, and provides user, role, group, and permission management. v2 adds user retrieval with filters, token revocation, and LDAP a
  name: Puppet Enterprise RBAC Service API
  slug: rbac
- description: The Node Classifier API enables querying node group matches, assigned classes and parameters, and environment assignments. Used to manage how nodes are classified and configured.
  name: Puppet Enterprise Node Classifier Service API
  slug: node-classifier
- description: The Code Manager API supports webhook creation, deployment queueing, and status monitoring for Puppet code, enabling Git-driven control of Puppet environments.
  name: Puppet Enterprise Code Manager API
  slug: code-manager
- description: The Activity Service API queries PE service and user events logged by the activity service, supporting audit and operational visibility.
  name: Puppet Enterprise Activity Service API
  slug: activity
- description: The Status API checks the health status of PE services.
  name: Puppet Enterprise Status API
  slug: status
- description: The Node Inventory API manages inventory service database operations including connection entries and listings.
  name: Puppet Enterprise Node Inventory API
  slug: inventory
- description: The Value API generates automation impact reports on time and cost savings.
  name: Puppet Enterprise Value API
  slug: value
- description: Puppet Forge is the public module repository providing thousands of downloadable Puppet modules.
  name: Puppet Forge
  slug: forge
- description: POST endpoints that trigger orchestrator actions.
  name: Puppet Commands API
  slug: puppet-commands-api
- description: GET endpoints that return information about known orchestrator jobs.
  name: Puppet Jobs API
  slug: puppet-jobs-api
artifact_total: 19
collections:
- collection_type: open
  name: Puppet Enterprise Orchestrator API
  slug: open-puppet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/puppet-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/puppet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/puppet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/puppet-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/puppet
- group: company
  title: ''
  type: Website
  url: https://www.puppet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.puppet.com/
- group: company
  title: ''
  type: Blog
  url: https://www.puppet.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/puppetlabs
- group: other
  title: ''
  type: Forge
  url: https://forge.puppet.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.puppet.com/
- group: operate
  title: ''
  type: Support
  url: https://support.puppet.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.puppet.com/pricing
created: '2025-02-24'
description: Puppet provides infrastructure automation and configuration management for hybrid and cloud environments. Puppet Enterprise exposes a collection of service APIs (Orchestrator, RBAC, Node Classifier, Code Manager, Activity, Status, Inventory, Value) that enable programmatic management of nodes, users, classifications, code deployments, and operational events.
finops:
- name: Puppet Finops
  service_category: API
  slug: puppet-finops
image: https://puppet.com/sites/default/files/2021-09/puppet-logo.png
layout: provider
modified: '2026-04-28'
name: Puppet
nav: Providers
network: true
overview: 'Puppet publishes 2 APIs on the [APIs.io](https://apis.io/) network: Commands API and Jobs API. Tagged areas include Automation, Configuration Management, DevOps, Enterprise, and Infrastructure as Code.


  Puppet''s developer surface includes authentication, documentation, engineering blog, support, pricing, and 8 more developer resources.'
plans:
- name: Puppet Plans Pricing
  plan_count: 3
  slug: puppet-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 5
  name: Puppet Rate Limits
  slug: puppet-rate-limits
score:
  band: developing
  composite: 45.9
  delta: 2.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.2
    developer_ergonomics: 26.1
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 43.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/puppet/refs/heads/main/screenshots/puppet-2026-06-20T192311.png
security:
- kind: authentication
  name: Puppet Authentication
  slug: puppet-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Puppet Domain Security
  slug: puppet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Puppet Vulnerability Disclosure
  slug: puppet-vulnerability-disclosure
  summary_line: disclosure policy published
slug: puppet
tags:
- Automation
- Configuration Management
- DevOps
- Enterprise
- Infrastructure as Code
- Orchestration
- RBAC
website: https://www.puppet.com/
---

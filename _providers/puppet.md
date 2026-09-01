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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 2
  name: Puppet Agentic Access
  operation_count: 12
  slug: puppet-agentic-access
  summary_line: 12 operations · 7 acting · 2 human-in-the-loop
api_count: 1
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
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Puppet Enterprise Orchestrator Commands API
  slug: open-puppet-commands-api
- collection_type: open
  name: Puppet Enterprise Orchestrator Commands Jobs API
  slug: open-puppet-jobs-api
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
random_paper: 19
rate_limits:
- limit_count: 5
  name: Puppet Rate Limits
  slug: puppet-rate-limits
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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

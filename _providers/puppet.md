---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
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
- baseURL_template: https://{pe_host}:8143/orchestrator/v1
  baseurl_source: spec_template
  description: POST endpoints that trigger orchestrator actions.
  name: Puppet Commands API
  slug: puppet-commands-api
- baseURL_template: https://{pe_host}:8143/orchestrator/v1
  baseurl_source: spec_template
  description: GET endpoints that return information about known orchestrator jobs.
  name: Puppet Jobs API
  slug: puppet-jobs-api
artifact_total: 22
collections:
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
- group: commercial
  href: https://artifacts.apis.io/puppet/plans/puppet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/puppet-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/puppet/rate-limits/puppet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/puppet-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/puppet/finops/puppet-finops.yml
  title: ''
  type: FinOps
  url: finops/puppet-finops.yml
- group: other
  href: https://artifacts.apis.io/puppet/capabilities/puppet-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/puppet-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/puppet/agentic-access/puppet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/puppet-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/puppet/security/puppet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/puppet-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/puppet/security/puppet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/puppet-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/puppet/authentication/puppet-authentication.yml
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
- group: docs
  title: ''
  type: APIReference
  url: https://forgeapi.puppet.com/
created: '2025-02-24'
description: Puppet provides infrastructure automation and configuration management for hybrid and cloud environments. Puppet Enterprise exposes a collection of service APIs (Orchestrator, RBAC, Node Classifier, Code Manager, Activity, Status, Inventory, Value) that enable programmatic management of nodes, users, classifications, code deployments, and operational events.
finops:
- has_sources: false
  method: generated
  name: Puppet Finops
  primary_unit: request
  service_category: API
  slug: puppet-finops
  template: true
image: https://puppet.com/sites/default/files/2021-09/puppet-logo.png
layout: provider
modified: '2026-04-28'
name: Puppet
nav: Providers
network: true
overview: 'Puppet publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Commands API, Jobs API, and 9 more. Tagged areas include Automation, Configuration Management, DevOps, Enterprise, and Infrastructure as Code.


  The Puppet catalog on APIs.io includes 1 Spectral governance ruleset.


  Puppet''s developer surface includes authentication, documentation, engineering blog, support, pricing, API reference, and 12 more developer resources.'
plans:
- name: Puppet Plans Pricing
  plan_count: 3
  slug: puppet-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Puppet Rate Limits
  slug: puppet-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Puppet API Rules
  rule_count: 57
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 1
  slug: puppet-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 13.6
    contract_quality: 48.4
    developer_ergonomics: 31.0
    discoverability: 57.1
    operational_transparency: 28.9
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/puppet/puppet-2026-06-20T192311.png
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
  summary_line: no policy recorded
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

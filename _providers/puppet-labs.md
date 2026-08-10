---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-08-10'
api_count: 4
apis:
- description: The Module Operations API from Puppet — 2 operation(s) for module operations.
  name: Puppet Module Operations API
  slug: puppet-labs-module-operations-api
- description: The Release Operations API from Puppet — 5 operation(s) for release operations.
  name: Puppet Release Operations API
  slug: puppet-labs-release-operations-api
- description: The Search Filter Operations API from Puppet — 2 operation(s) for search filter operations.
  name: Puppet Search Filter Operations API
  slug: puppet-labs-search-filter-operations-api
- description: The User Operations API from Puppet — 2 operation(s) for user operations.
  name: Puppet User Operations API
  slug: puppet-labs-user-operations-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/puppet-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/puppet-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.puppet.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.puppet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.puppet.com/
- group: docs
  title: ''
  type: APIReference
  url: https://forgeapi.puppet.com/
- group: other
  title: ''
  type: Forge
  url: https://forge.puppet.com/
- group: company
  title: ''
  type: Blog
  url: https://www.puppet.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/puppetlabs
- group: operate
  title: ''
  type: Support
  url: https://portal.perforce.com/s/product/a3g4X000009wMFBQA2/puppet
- group: operate
  title: ''
  type: Community
  url: https://www.puppet.com/community
- group: commercial
  title: ''
  type: Pricing
  url: https://www.puppet.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.perforce.com/website-terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.perforce.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.perforce.com/
- group: auth
  title: ''
  type: Security
  url: https://www.puppet.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/puppet-labs-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/puppet-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/puppet-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/puppet-labs-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Puppet (Perforce Puppet, formerly Puppet Labs) is an infrastructure automation and configuration-management platform used by more than 40,000 organizations to manage servers, networks, cloud, and edge infrastructure through desired-state, policy-driven automation. Its products include Puppet Enterprise, Puppet Core, the Bolt orchestration tool, and the Puppet Forge module registry. The public Puppet Forge v3 API provides RESTful access to the modules, releases, users, and release plans published on Forge; Puppet Enterprise additionally exposes REST APIs for orchestration, node classification, RBAC, and PuppetDB querying. Puppet was acquired by Perforce Software in 2022.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/puppet-labs.png
layout: provider
modified: '2026-07-20'
name: Puppet
nav: Providers
network: true
overview: 'Puppet publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Module Operations API, Release Operations API, Search Filter Operations API, and 1 more. Tagged areas include Company, Enterprise, Infrastructure Automation, Configuration Management, and DevOps.


  Puppet''s developer surface includes documentation, API reference, engineering blog, support, pricing, CLI, and 15 more developer resources.'
random_paper: 89
score:
  band: developing
  composite: 44.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.4
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 44.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Puppet Labs Authentication
  slug: puppet-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Puppet Labs Domain Security
  slug: puppet-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Puppet Labs Vulnerability Disclosure
  slug: puppet-labs-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Puppet Labs Trust Center
  slug: puppet-labs-trust-center
  summary_line: trust center published
slug: puppet-labs
tags:
- Company
- Enterprise
- Infrastructure Automation
- Configuration Management
- DevOps
- Module Registry
- Compliance
website: https://www.puppet.com
---

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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: OpenTofu is a CLI-driven infrastructure-as-code tool forked from Terraform. The opentofu binary reads HashiCorp Configuration Language (HCL) configuration, plans changes, and applies them against clou
  name: OpenTofu CLI
  slug: opentofu-cli
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/opentofu/opentofu/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/opentofu/opentofu/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/opentofu/opentofu/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/opentofu/opentofu/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/opentofu/opentofu/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/opentofu/opentofu/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opentofu-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opentofuorg
- group: company
  title: ''
  type: Website
  url: https://opentofu.org/
- group: docs
  title: ''
  type: Documentation
  url: https://opentofu.org/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://opentofu.org/docs/intro/install/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/opentofu/opentofu
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opentofu
- group: company
  title: ''
  type: Blog
  url: https://opentofu.org/blog/
- group: operate
  title: ''
  type: Community
  url: https://opentofu.org/community/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/opentofu/opentofu/blob/main/CHANGELOG.md
- group: auth
  title: ''
  type: Security
  url: https://github.com/opentofu/opentofu/security/policy
- group: other
  title: ''
  type: Downloads
  url: https://opentofu.org/docs/intro/install/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/opentofu/opentofu-mcp-server
created: '2025-01-01'
description: Open-source infrastructure as code tool forked from Terraform, providing a community-driven alternative for provisioning and managing cloud infrastructure using declarative configuration files.
finops:
- name: Opentofu Finops
  service_category: API
  slug: opentofu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opentofu.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: OpenTofu
nav: Providers
network: true
overview: 'OpenTofu publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, DevOps, Infrastructure as Code, and Open-Source.


  OpenTofu''s developer surface includes documentation, getting-started guide, engineering blog, changelog, and 15 more developer resources.'
plans:
- name: Opentofu Plans Pricing
  plan_count: 3
  slug: opentofu-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Opentofu Rate Limits
  slug: opentofu-rate-limits
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 31.0
    catalog_earned_first_party: 0.0
    catalog_gap: 84.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 27.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opentofu/refs/heads/main/screenshots/opentofu-2026-06-20T191043.png
security:
- kind: domain-security
  name: Opentofu Domain Security
  slug: opentofu-domain-security
  summary_line: TLSv1.3
slug: opentofu
tags:
- Cloud
- DevOps
- Infrastructure as Code
- Open-Source
website: https://opentofu.org/
---

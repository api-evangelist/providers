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
  band: human-only
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: OpenTofu is a CLI-driven infrastructure-as-code tool forked from Terraform. The opentofu binary reads HashiCorp Configuration Language (HCL) configuration, plans changes, and applies them against clou
  name: OpenTofu CLI
  slug: opentofu-cli
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/opentofu/plans/opentofu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opentofu-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/opentofu/rate-limits/opentofu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/opentofu-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/opentofu/finops/opentofu-finops.yml
  title: ''
  type: FinOps
  url: finops/opentofu-finops.yml
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
  href: https://artifacts.apis.io/opentofu/security/opentofu-domain-security.yml
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
- has_sources: false
  method: generated
  name: Opentofu Finops
  primary_unit: request
  service_category: API
  slug: opentofu-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opentofu.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: Remote MCP server at mcp.opentofu.org over HTTP; 7 tools listed.
  name: OpenTofu MCP Server
  slug: opentofu
modified: '2026-05-19'
name: OpenTofu
nav: Providers
network: true
overview: 'OpenTofu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud, DevOps, Infrastructure as Code, and Open Source.


  OpenTofu''s developer surface includes documentation, getting-started guide, engineering blog, changelog, and 18 more developer resources.'
plans:
- name: Opentofu Plans Pricing
  plan_count: 3
  slug: opentofu-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Opentofu Rate Limits
  slug: opentofu-rate-limits
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 28.0
    catalog_earned_first_party: 0.0
    catalog_gap: 87.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 40.0
    operational_transparency: 39.5
  previous_composite: 16.5
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/opentofu/opentofu-2026-06-20T191043.png
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
- Open Source
website: https://opentofu.org/
---

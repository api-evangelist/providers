---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 8.5
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'The Stacklet Platform GraphQL API is the control plane for the governance platform: cloud accounts and account groups, policies and policy collections, bindings (the deployment of a policy collection '
  name: Stacklet Platform API
  slug: stacklet-platform-api
- description: 'An open-source Model Context Protocol server, published by Stacklet and distributed on PyPI as stacklet-mcp, that grants an LLM three toolsets against a Stacklet deployment: AssetDB SQL queries (ad ho'
  name: Stacklet MCP Server
  slug: stacklet-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://stacklet.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://registry.terraform.io/providers/stacklet/stacklet/latest/docs
- group: company
  title: ''
  type: Blog
  url: https://stacklet.ai/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://stacklet.ai/feed/
- group: operate
  title: ''
  type: Support
  url: https://stacklet.ai/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stacklet.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stacklet.ai/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stacklet
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/stacklet/mcp-server
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stacklet-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/stacklet-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stacklet-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/stacklet-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stacklet-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stacklet-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stacklet-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stacklet-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stacklet-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stacklet-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stacklet-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/stacklet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stacklet-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stacklet-domain-security.yml
created: '2026-08-29'
description: Stacklet is a cloud governance company founded by the creators of Cloud Custodian, the open-source rules engine it stewards. Its Governance-as-Code platform runs Cloud Custodian policies as a managed service across AWS, Azure and GCP and adds AssetDB, a SQL-queryable warehouse of cloud resources, costs, tags and relationships; IaC governance for shift-left policy scanning; and the Jun0 agentic layer. The platform is driven by a per-customer GraphQL API served at https://api.<instance>.stacklet.io, a first-party Python CLI (stacklet-admin), an official Terraform provider, and an open-source Model Context Protocol server that exposes AssetDB SQL, Platform GraphQL and documentation tools to AI agents. The company operates its marketing surface at stacklet.ai, to which stacklet.io redirects.
image: https://stacklet.ai/wp-content/uploads/2024/09/Social-Share-1.jpg
layout: provider
mcp_servers:
- description: 'Official open-source MCP server published by Stacklet that exposes a Stacklet deployment to an LLM through three toolsets: AssetDB SQL, Platform GraphQL, and deployment documentation.'
  name: Stacklet MCP Server
  slug: stacklet-mcp-server
modified: '2026-08-29'
name: Stacklet
nav: Providers
network: true
overview: 'Stacklet publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Governance, Cloud Custodian, Policy as Code, and FinOps.


  Stacklet''s developer surface includes documentation, engineering blog, support, CLI, authentication, changelog, and 17 more developer resources.'
plans:
- name: Stacklet Plans Pricing
  plan_count: 0
  slug: stacklet-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Stacklet Rate Limits
  slug: stacklet-rate-limits
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 23.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stacklet/refs/heads/main/screenshots/stacklet-2026-09-02T160730.png
security:
- kind: authentication
  name: Stacklet Authentication
  slug: stacklet-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Stacklet Domain Security
  slug: stacklet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stacklet
tags:
- Company
- Cloud Governance
- Cloud Custodian
- Policy as Code
- FinOps
- Cloud Security
- Compliance
- Infrastructure as Code
- Terraform
- GraphQL
- MCP
- Azure
- Google Cloud
- Agents
website: https://stacklet.ai/
---

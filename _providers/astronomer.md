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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 43
  human_in_the_loop: 2
  name: Astronomer Agentic Access
  operation_count: 75
  slug: astronomer-agentic-access
  summary_line: 75 operations · 43 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.astronomer.io/v1
  baseurl_source: declared
  description: The Mux Create Upload API from Astronomer — 1 operation(s) for mux create upload.
  name: Astronomer Mux Create Upload API
  slug: astronomer-mux-create-upload-api
- baseURL: https://api.astronomer.io/v1
  baseurl_source: declared
  description: The Mux Get Playback Id API from Astronomer — 1 operation(s) for mux get playback id.
  name: Astronomer Mux Get Playback Id API
  slug: astronomer-mux-get-playback-id-api
artifact_total: 30
collections:
- collection_type: open
  name: Astro Platform AgentToken API
  slug: open-astronomer-agenttoken-api
- collection_type: open
  name: Astro Platform AgentToken AllowedIpAddressRange API
  slug: open-astronomer-allowedipaddressrange-api
- collection_type: open
  name: Astro Platform AgentToken ApiToken API
  slug: open-astronomer-apitoken-api
- collection_type: open
  name: Astro Platform AgentToken Authorization API
  slug: open-astronomer-authorization-api
- collection_type: open
  name: Astro Platform AgentToken Cluster API
  slug: open-astronomer-cluster-api
- collection_type: open
  name: Astro Platform AgentToken Deploy API
  slug: open-astronomer-deploy-api
- collection_type: open
  name: Astro Platform AgentToken Deployment API
  slug: open-astronomer-deployment-api
- collection_type: open
  name: Astro Platform AgentToken Environment API
  slug: open-astronomer-environment-api
- collection_type: open
  name: Astro Platform AgentToken Invite API
  slug: open-astronomer-invite-api
- collection_type: open
  name: Astro Platform AgentToken Options API
  slug: open-astronomer-options-api
- collection_type: open
  name: Astro Platform AgentToken Organization API
  slug: open-astronomer-organization-api
- collection_type: open
  name: Astro Platform AgentToken Role API
  slug: open-astronomer-role-api
- collection_type: open
  name: Astro Platform AgentToken Team API
  slug: open-astronomer-team-api
- collection_type: open
  name: Astro Platform AgentToken User API
  slug: open-astronomer-user-api
- collection_type: open
  name: Astro Platform AgentToken Workspace API
  slug: open-astronomer-workspace-api
common:
- group: commercial
  href: https://artifacts.apis.io/astronomer/plans/astronomer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/astronomer-plans-pricing.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/astronomer/overview
- group: company
  title: ''
  type: Blog
  url: https://www.astronomer.io/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.astronomer.io/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/astronomer/capabilities/astronomer-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/astronomer-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/astronomer/overlays/astronomer-astro-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/astronomer-astro-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/astronomer/security/astronomer-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/astronomer-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://astronomer.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.astronomer.io/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.astronomer.io/docs/astro/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.astronomer.io/docs/astro/api/v-1/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.astronomer.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/astronomer
- group: commercial
  title: ''
  type: Pricing
  url: https://www.astronomer.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.astronomer.io/try-astro/
- group: start
  title: ''
  type: Login
  url: https://cloud.astronomer.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.astronomer.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astronomer.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.astronomer.io
- group: auth
  title: ''
  type: Compliance
  url: https://trust.astronomer.io
- group: auth
  title: ''
  type: Security
  url: https://www.astronomer.io/vulnerability-disclosure/
- group: agent
  href: https://artifacts.apis.io/astronomer/mcp/astronomer-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/astronomer-mcp.yml
- group: agent
  href: https://artifacts.apis.io/astronomer/llms/astronomer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/astronomer-llms.txt
- group: build
  href: https://artifacts.apis.io/astronomer/packages/astronomer-packages.yml
  title: ''
  type: Packages
  url: packages/astronomer-packages.yml
- group: build
  href: https://artifacts.apis.io/astronomer/packages/astronomer-packages.yml
  title: ''
  type: SDKs
  url: packages/astronomer-packages.yml
- group: build
  href: https://artifacts.apis.io/astronomer/cli/astronomer-cli.yml
  title: ''
  type: CLI
  url: cli/astronomer-cli.yml
- group: design
  href: https://artifacts.apis.io/astronomer/lifecycle/astronomer-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/astronomer-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.astronomer.io/docs/astro/api/v-1/versioning-and-support
- group: operate
  href: https://artifacts.apis.io/astronomer/changelog/astronomer-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/astronomer-changelog.yml
- group: design
  href: https://artifacts.apis.io/astronomer/conformance/astronomer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/astronomer-conformance.yml
- group: auth
  href: https://artifacts.apis.io/astronomer/authentication/astronomer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/astronomer-authentication.yml
- group: auth
  href: https://artifacts.apis.io/astronomer/security/astronomer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astronomer-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/astronomer/security/astronomer-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/astronomer-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/astronomer/well-known/astronomer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/astronomer-well-known.yml
- group: agent
  href: https://artifacts.apis.io/astronomer/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Astronomer is the company behind Astro, a fully managed data operations platform powered by Apache Airflow. Astro lets data teams author, orchestrate, run, and observe data pipelines (DAGs) at scale across a managed control plane and data plane. The Astro Platform API is a production-ready REST API for programmatic control of Astro resources — Organizations, Workspaces, Deployments, Clusters, Users, Teams, role-based access control, API tokens, deploys, and environment objects — authenticated with bearer API tokens. Astronomer also ships the Astro CLI, an official Terraform provider, the Astro Python SDK, a documentation MCP server, and Astro Runtime, its distribution of Apache Airflow.
finops:
- has_sources: true
  method: derived
  name: Astronomer Finops
  primary_unit: hour
  service_category: ''
  slug: astronomer-finops
  template: false
image: https://www.astronomer.io/img/logos/astronomer-logo.png
layout: provider
mcp_servers:
- description: Official documentation MCP server for https://www.astronomer.io/docs (Fern-hosted). Provides AI-powered search over the Astronomer documentation. Referenced from the Astronomer docs llms.txt for AI cl
  name: Astronomer MCP Server
  slug: fern-docs-mcp-server
modified: '2026-10-06'
name: Astronomer
nav: Providers
network: true
overview: 'Astronomer publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Mux Create Upload API and Mux Get Playback Id API. Tagged areas include Company, Data Orchestration, Apache Airflow, Data Pipeline, and Data Engineering.


  The Astronomer catalog on APIs.io includes 1 Spectral governance ruleset.


  Astronomer''s developer surface includes engineering blog, documentation, getting-started guide, pricing, signup flow, CLI, changelog, and 28 more developer resources.'
plans:
- name: Astronomer Plans Pricing
  plan_count: 8
  slug: astronomer-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Astronomer API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: astronomer-rules
score:
  band: strong
  composite: 61.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 60.1
    discoverability: 73.2
    operational_transparency: 52.6
  previous_composite: 61.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 11.1
      total: 18
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/astronomer/astronomer-2026-07-25T201511.png
security:
- kind: authentication
  name: Astronomer Authentication
  slug: astronomer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Astronomer Domain Security
  slug: astronomer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Astronomer Vulnerability Disclosure
  slug: astronomer-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Astronomer Trust Center
  slug: astronomer-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
skill_count: 4
skills:
- name: Deploy an image or DAGs to a Deployment
  slug: astronomer-deploy-to-deployment
- name: Create, scope, rotate, and revoke API tokens
  slug: astronomer-manage-api-tokens
- name: Manage Teams, membership, and RBAC roles
  slug: astronomer-manage-teams-rbac
- name: Provision an Astro Deployment in a Workspace
  slug: astronomer-provision-deployment
slug: astronomer
tags:
- Company
- Data Orchestration
- Apache Airflow
- Data Pipeline
- Data Engineering
- Workflow Automation
- MLOps
- Managed Platform
website: https://astronomer.io
---

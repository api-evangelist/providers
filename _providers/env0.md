---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://www.env0.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.envzero.com/ — a different registrable domain (env0.com -> envzero.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.2
  scored_at: '2026-09-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Env0 Agentic Access
  operation_count: 21
  slug: env0-agentic-access
  summary_line: 21 operations · 8 acting
api_count: 1
apis:
- description: env0 is an infrastructure-as-code automation platform providing cost estimation, policy enforcement, and self-service environments. The public REST API is available at https://api.env0.com/ and uses H
  name: Env0
  slug: env0
- baseURL: https://api.env0.com/
  baseurl_source: declared
  description: The Agents API from Env0 — 1 operation(s) for agents.
  name: Env0 Agents API
  slug: env0-agents-api
- baseURL: https://api.env0.com/
  baseurl_source: declared
  description: The ApprovalPolicies API from Env0 — 1 operation(s) for approvalpolicies.
  name: Env0 ApprovalPolicies API
  slug: env0-approvalpolicies-api
- baseURL: https://api.env0.com/
  baseurl_source: declared
  description: The Configuration API from Env0 — 1 operation(s) for configuration.
  name: Env0 Configuration API
  slug: env0-configuration-api
- baseURL: https://api.env0.com/
  baseurl_source: declared
  description: The Deployments API from Env0 — 2 operation(s) for deployments.
  name: Env0 Deployments API
  slug: env0-deployments-api
- baseURL: https://api.env0.com/
  baseurl_source: declared
  description: The Environments API from Env0 — 2 operation(s) for environments.
  name: Env0 Environments API
  slug: env0-environments-api
- baseURL: https://api.env0.com/
  baseurl_source: declared
  description: The Modules API from Env0 — 1 operation(s) for modules.
  name: Env0 Modules API
  slug: env0-modules-api
- baseURL: https://api.env0.com/
  baseurl_source: declared
  description: The Organizations API from Env0 — 1 operation(s) for organizations.
  name: Env0 Organizations API
  slug: env0-organizations-api
- baseURL: https://api.env0.com/
  baseurl_source: declared
  description: The Projects API from Env0 — 2 operation(s) for projects.
  name: Env0 Projects API
  slug: env0-projects-api
- baseURL: https://api.env0.com/
  baseurl_source: declared
  description: The Templates API from Env0 — 1 operation(s) for templates.
  name: Env0 Templates API
  slug: env0-templates-api
- baseURL: https://api.env0.com/
  baseurl_source: declared
  description: The Users API from Env0 — 1 operation(s) for users.
  name: Env0 Users API
  slug: env0-users-api
- baseURL: https://api.env0.com/
  baseurl_source: declared
  description: The Webhooks API from Env0 — 1 operation(s) for webhooks.
  name: Env0 Webhooks API
  slug: env0-webhooks-api
artifact_total: 34
asyncapis:
- description: ''
  name: Env0 Webhooks
  slug: env0-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: env0 Agents API
  slug: open-env0-agents-api
- collection_type: open
  name: env0 Agents ApprovalPolicies API
  slug: open-env0-approvalpolicies-api
- collection_type: open
  name: env0 Agents Configuration API
  slug: open-env0-configuration-api
- collection_type: open
  name: env0 Agents Deployments API
  slug: open-env0-deployments-api
- collection_type: open
  name: env0 Agents Environments API
  slug: open-env0-environments-api
- collection_type: open
  name: env0 Agents Modules API
  slug: open-env0-modules-api
- collection_type: open
  name: env0 Agents Organizations API
  slug: open-env0-organizations-api
- collection_type: open
  name: env0 Agents Projects API
  slug: open-env0-projects-api
- collection_type: open
  name: env0 Agents Templates API
  slug: open-env0-templates-api
- collection_type: open
  name: env0 Agents Users API
  slug: open-env0-users-api
- collection_type: open
  name: env0 Agents Webhooks API
  slug: open-env0-webhooks-api
- collection_type: open
  name: env0 API
  slug: open-env0
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/env0-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/env0-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/env0-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/env0
- group: company
  title: ''
  type: Website
  url: https://www.envzero.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.envzero.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.envzero.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.envzero.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.envzero.com/guides/getting-started/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.envzero.com/guides/community-and-resources/support-and-help/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.envzero.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.env0.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.envzero.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.envzero.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.envzero.com/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/env0
- group: operate
  title: ''
  type: StatusPage
  url: https://status.env0.com
- group: auth
  title: ''
  type: Compliance
  url: https://docs.envzero.com/guides/overview/security-overview
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/env0-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/env0-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/env0-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/env0-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/env0-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/env0-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/env0-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/env0-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/env0-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/env0-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/env0-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/env0-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/env0-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/env0-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/env0-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/env0-rate-limits.yml
created: '2026-03-27'
description: env0 -- now trading as "env zero" -- is an infrastructure-as-code automation and cloud governance platform for Terraform, OpenTofu, Terragrunt, Pulumi, CloudFormation, Kubernetes and Helm. It provisions and manages cloud environments from reusable templates, orchestrates multi-environment workflows with dependencies, enforces custom approval and guardrail policies, detects and remediates infrastructure drift, runs a private module and provider registry, and adds cost estimation, actual-cost visibility and budget thresholds on top. The public REST API at https://api.env0.com publishes 327 operations across 30 areas and authenticates with HTTP Basic using an API Key ID and Secret. env zero also ships a first-party CLI, a Terraform provider, an official MCP server, a published Agent Skill and a conformant A2A agent card.
finops:
- name: Env0 Finops
  service_category: API
  slug: env0-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/env0.png
layout: provider
mcp_servers:
- description: ''
  name: Env0 MCP Server
  slug: env0-mcp-server
modified: '2026-09-06'
name: Env0
nav: Providers
network: true
overview: 'Env0 publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Agents API, ApprovalPolicies API, Configuration API, and 8 more. Tagged areas include FinOps, Infrastructure as Code, DevOps, Cloud, and Terraform.


  The Env0 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Env0''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Env0 Plans Pricing
  plan_count: 3
  slug: env0-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Env0 Rate Limits
  slug: env0-rate-limits
score:
  band: strong
  composite: 64.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 31.6
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 60.3
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: first-party
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/env0/refs/heads/main/screenshots/env0-2026-06-20T180838.png
security:
- kind: authentication
  name: Env0 Authentication
  slug: env0-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Env0 Domain Security
  slug: env0-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Env0 Trust Center
  slug: env0-trust-center
  summary_line: SOC 2 Type II
slug: env0
tags:
- FinOps
- Infrastructure as Code
- DevOps
- Cloud
- Terraform
- OpenTofu
- Platform Engineering
- Cloud Governance
- Drift Detection
website: https://www.envzero.com/
---

---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/branch-deploy-dev/plans/branch-deploy-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/branch-deploy-dev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/branch-deploy-dev/changelog/branch-deploy-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/branch-deploy-dev-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://branch-deploy.dev/security/
- group: design
  href: https://artifacts.apis.io/branch-deploy-dev/conformance/branch-deploy-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/branch-deploy-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/branch-deploy-dev/llms/branch-deploy-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/branch-deploy-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/branch-deploy-dev/mcp/branch-deploy-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/branch-deploy-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/branch-deploy-dev/well-known/branch-deploy-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/branch-deploy-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/branch-deploy-dev/well-known/branch-deploy-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/branch-deploy-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/branch-deploy-dev/hosts/branch-deploy-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branch-deploy-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/branch-deploy-dev/vendors/branch-deploy-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/branch-deploy-dev-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://branch-deploy.dev/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://branch-deploy.dev/docs/release-notes/
- group: start
  title: ''
  type: GettingStarted
  url: https://branch-deploy.dev/docs/deploy/
- group: auth
  href: https://artifacts.apis.io/branch-deploy-dev/security/branch-deploy-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/branch-deploy-dev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/branch-deploy-dev/security/branch-deploy-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/branch-deploy-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/branch-deploy-dev/security/branch-deploy-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branch-deploy-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://branch-deploy.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://branch-deploy.dev/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://branch-deploy.dev/pricing/
- group: operate
  title: ''
  type: Support
  url: https://branch-deploy.dev/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://branch-deploy.dev/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://branch-deploy.dev/terms/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the provider's documented hosts.
  evidence:
  - status: 404
    url: https://api.branch-deploy.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BranchDeploy provides a seamless way to deploy Azure DevOps branches directly from Azure Boards work items. It adds a Deploy button to work items, allowing users to confirm the linked Azure Repos branch or pull request and queue the existing Azure Pipeline without leaving the ticket. The service supports branch allowlists, audit logs, Microsoft Teams integration, and AI‑assistant deployments via MCP, offering both free and paid Pro plans for advanced features.
image: https://branch-deploy.dev/branchdeploy-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.branch-deploy.dev requiring OAuth.
  name: BranchDeploy MCP Server
  slug: branch-deploy-dev-mcp-yml
modified: '2026-11-02'
name: BranchDeploy
nav: Providers
network: true
overview: 'BranchDeploy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Software-as-a-Service, Microsoft Azure, DevOps, Deployment, and Automation.


  BranchDeploy''s developer surface includes changelog, getting-started guide, documentation, pricing, support, and 17 more developer resources.'
plans:
- name: Branch Deploy Dev Plans Pricing
  plan_count: 2
  slug: branch-deploy-dev-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.3
    operational_transparency: 13.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Branch Deploy Dev Domain Security
  slug: branch-deploy-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Branch Deploy Dev Vulnerability Disclosure
  slug: branch-deploy-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Branch Deploy Dev Trust Center
  slug: branch-deploy-dev-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: branch-deploy-dev
tags:
- Software-as-a-Service
- Microsoft Azure
- DevOps
- Deployment
- Automation
website: https://branch-deploy.dev/
---

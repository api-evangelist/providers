---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.8
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: REST API covering the whole CoreStack governance surface — authorization, identity and RBAC, guardrail policies, account governance, operations and automation, security, cost and budgets, access, reso
  name: CoreStack External API
  slug: corestack-external-api
- description: Hosted, unified Model Context Protocol server exposing 100 documented tools across five domains — Common/Auth (10), FinOps (24), Graphion (45), Assessment (15) and Workload (6) — at a single /mcp endp
  name: CoreStack MCP Server
  slug: corestack-mcp-server
artifact_total: 11
asyncapis:
- description: ''
  name: Corestack Webhooks
  slug: corestack-webhooks
collections:
- collection_type: open
  name: CoreStack External API
  slug: open-corestack-external-api-openapi-original
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corestack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.corestack.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.corestack.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.corestack.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.corestack.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.corestack.io/docs/corestack-api-modules
- group: operate
  title: ''
  type: Support
  url: https://support.corestack.io/portal/en/home
- group: company
  title: ''
  type: Blog
  url: https://www.corestack.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.corestack.io/solutions/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.corestack.io/contact-us/
- group: start
  title: ''
  type: Login
  url: https://cloud.corestack.io/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.corestack.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.corestack.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://corestack.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.corestack.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/corestack-changelog.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.corestack.io/docs/external-apis-62-2603
- group: auth
  title: ''
  type: Compliance
  url: https://www.corestack.io/blog/corestack-achieves-soc-2-type-ii-certification/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/corestack-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/corestack-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/corestack-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/corestack-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/corestack-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/corestack-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/corestack-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/corestack-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/corestack-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/corestack-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/corestack-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/corestack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/corestack-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/corestack-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/corestack-external-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/corestack-packages.yml
created: '2026-08-11'
description: CoreStack is a multi-cloud governance and security platform that unifies FinOps (cost visibility, budgets, anomaly detection, rightsizing and commitment optimization), CloudOps (workload lifecycle, tagging, automation and self-service), SecOps/compliance (policy guardrails, posture management and continuous assessment against ISO, NIST, HIPAA, PCI DSS, CIS and the AWS Well-Architected Framework), and Graphion, its AI-native CNAPP layer covering SBOM, container findings and vulnerability intelligence, across AWS, Microsoft Azure, Google Cloud and Oracle Cloud Infrastructure. Every one of those capabilities is exposed through the CoreStack External API — a Swagger 2.0 contract of 838 operations across 767 paths, published live at the API host — and, since 2026, through a hosted unified MCP server that surfaces 100 documented tools to AI clients over OAuth or API key headers.
image: https://www.corestack.io/wp-content/uploads/Agentic-Governance-OS-Unified-Governance-Across-Cloud-SaaS-and-AI.png
layout: provider
mcp_servers:
- description: ''
  name: CoreStack MCP Server
  slug: corestack-mcp-server
- description: ''
  name: CoreStack MCP Server
  slug: corestack-mcp-server-2
modified: '2026-08-11'
name: CoreStack
nav: Providers
network: true
overview: 'CoreStack publishes 1 API on the [APIs.io](https://apis.io/) network: External API. Tagged areas include Cloud Governance, FinOps, Cloud Cost Management, Cloud Security Posture Management, and Compliance.


  The CoreStack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CoreStack''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Corestack Plans Pricing
  plan_count: 6
  slug: corestack-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Corestack Rate Limits
  slug: corestack-rate-limits
scopes:
- name: Corestack Scopes
  scope_count: 0
  slug: corestack-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.8
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 16.7
    contract_quality: 45.1
    developer_ergonomics: 39.9
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 34.2
  previous_composite: 57.8
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corestack/refs/heads/main/screenshots/corestack-2026-08-17T080832.png
security:
- kind: authentication
  name: Corestack Authentication
  slug: corestack-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Corestack Domain Security
  slug: corestack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: corestack
tags:
- Cloud Governance
- FinOps
- Cloud Cost Management
- Cloud Security Posture Management
- Compliance
- Multi-Cloud
- CNAPP
- Policy as Code
- cloudops
- MCP
- agent-native
- Kubernetes
website: https://www.corestack.io/
---

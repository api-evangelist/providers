---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 98
  human_in_the_loop: 5
  name: Aembit Agentic Access
  operation_count: 167
  slug: aembit-agentic-access
  summary_line: 167 operations · 98 acting · 5 human-in-the-loop
api_count: 2
apis:
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Aembit Cloud API is the management and control plane contract for the Aembit platform. It exposes 165 operations across 74 paths for Access Policies, Access Conditions, Client and Server Workloads
  name: Aembit Cloud API
  slug: aembit-cloud-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Aembit Edge API is the workload-facing runtime contract. Two operations let a Client Workload bootstrap a session by presenting attestation evidence to a configured Trust Provider (POST /edge/v1/a
  name: Aembit Edge API
  slug: aembit-edge-api
- description: A first-party hosted Model Context Protocol server that gives AI agents and MCP clients read-only access to a tenant's Aembit event logs. Three tools — get_audit_logs, get_auth_events and get_workload
  name: Aembit MCP Server
  slug: aembit-mcp-server
artifact_total: 12
asyncapis:
- description: ''
  name: Aembit Event Surface
  slug: aembit-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://aembit.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aembit.io/dev-guide/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aembit.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aembit.io/dev-guide/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aembit.io/get-started/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://support.aembit.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://aembit.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aembit
- group: commercial
  title: ''
  type: Pricing
  url: https://aembit.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://useast2.aembit.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aembit.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aembit.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aembit.io/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/aembit-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.aembit.io/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.aembit.io/get-started/security-posture/security-compliance/
- group: auth
  title: ''
  type: Security
  url: https://docs.aembit.io/get-started/security-posture/security-compliance/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aembit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aembit-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aembit.io/changelog/
- group: build
  title: ''
  type: CLI
  url: cli/aembit-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/aembit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aembit-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aembit-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aembit-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aembit-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aembit-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aembit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aembit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aembit-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aembit-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aembit-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aembit-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aembit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aembit-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aembit-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://useast2.aembit.io/
- group: other
  title: ''
  type: Overlay
  url: overlays/aembit-cloud-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/aembit-edge-overlay.yaml
created: '2026-09-09'
description: Aembit is a Workload Identity and Access Management (Workload IAM) platform for non-human identities — AI agents, applications, microservices, CI/CD pipelines, scripts and service accounts. Instead of long-lived, hard-coded secrets, Aembit cryptographically attests a workload against a Trust Provider (AWS, Azure, GCP, GitHub Actions, GitLab, Kubernetes, Terraform Cloud, OIDC, SPIFFE, Kerberos), evaluates an Access Policy with optional conditional-access signals from CrowdStrike and Wiz, and injects a short-lived credential just-in-time so the application never stores one. The platform is delivered as a SaaS control plane (Aembit Cloud) plus a distributed enforcement layer (Aembit Edge — Agent Proxy, Agent Injector, AWS Lambda extension, CLI and Edge SDKs). Aembit publishes two OpenAPI 3.1.1 contracts — the Aembit Cloud API for managing every platform resource and the Aembit Edge API for workload authentication and credential retrieval — alongside a hosted, read-only MCP Server
  for querying audit, authorization and workload events, an MCP Identity Gateway and an MCP Authorization Server for governing AI-agent access to MCP servers.
image: https://aembit.io/wp-content/uploads/2023/08/aembit-favicon-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: Aembit MCP Server
  slug: aembit-mcp-server
modified: '2026-09-09'
name: Aembit
nav: Providers
network: true
overview: 'Aembit publishes 2 APIs on the [APIs.io](https://apis.io/) network: Cloud API and Edge API. Tagged areas include Security, Identity, Access Management, Workload Identity, and Non-Human Identity.


  The Aembit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aembit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Aembit Plans Pricing
  plan_count: 6
  slug: aembit-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Aembit Rate Limits
  slug: aembit-rate-limits
score:
  band: exemplar
  composite: 71.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 65.1
    developer_ergonomics: 76.8
    discoverability: 75.9
    operational_transparency: 84.2
  previous_composite: 71.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Aembit Authentication
  slug: aembit-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Aembit Domain Security
  slug: aembit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aembit Vulnerability Disclosure
  slug: aembit-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Aembit Trust Center
  slug: aembit-trust-center
  summary_line: SOC 2, ISO 27001
slug: aembit
tags:
- Security
- Identity
- Access Management
- Workload Identity
- Non-Human Identity
- Secrets Management
- Zero Trust
- Agentic AI
- Model Context Protocol
- Authentication
- Authorization
- DevSecOps
- Cloud Security
website: https://aembit.io/
---

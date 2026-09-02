---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - https://secureframe.com/pricing
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API providing programmatic access to Secureframe controls, frameworks, framework requirements, tests, evidence, policies, tasks, risks, personnel, devices, cloud resources, repositories, third-pa
  name: Secureframe Public API
  slug: public-api
- description: First-party hosted (remote) Model Context Protocol server exposing the Secureframe compliance platform as 112 tools across 41 categories — 63 read, 49 write — mapped one-for-one onto the Public API op
  name: Secureframe MCP Server
  slug: mcp-server
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://secureframe.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.secureframe.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.secureframe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.secureframe.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.secureframe.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://secureframe.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/secureframe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/secureframe-rate-limits.yml
- group: start
  title: ''
  type: Login
  url: https://app.secureframe.com/login
- group: start
  title: ''
  type: SignUp
  url: https://secureframe.com/request-demo
- group: operate
  title: ''
  type: Support
  url: https://secureframe.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.secureframe.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.secureframe.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://secureframe.com/product-updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/secureframe-changelog.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://secureframe.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://secureframe.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/secureframe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/secureframe
- group: company
  title: ''
  type: Blog
  url: https://secureframe.com/blog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/secureframe-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/secureframe-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/secureframe-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/secureframe-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/secureframe-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.secureframe.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/secureframe-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/secureframe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/secureframe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/secureframe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/secureframe-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/secureframe-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/secureframe-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/secureframe-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/secureframe-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/secureframe-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/secureframe-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/secureframe-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/secureframe-public-api-overlay.yaml
- group: commercial
  title: ''
  type: FinOps
  url: finops/secureframe-finops.yml
created: '2026-05-08'
description: Secureframe automates security and privacy compliance for SOC 2, ISO 27001, HIPAA, PCI DSS, GDPR, CMMC, FedRAMP, NIST 800-171 and more. Its Public API is a 112-operation, JSON:API-shaped REST contract over the compliance record of truth — frameworks, requirements, controls, tests, evidence, policies, risks, personnel, devices, cloud resources, repositories, third-party vendors, trust center requests, and the System Security Plan and POA&M artifacts CMMC and FedRAMP assessments are conducted against. Secureframe also runs a first-party hosted MCP server that exposes all 112 operations as agent-callable tools over OAuth 2.1.
finops:
- name: Secureframe Finops
  service_category: GRC
  slug: secureframe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/secureframe.png
layout: provider
mcp_servers:
- description: Secureframe publishes a first-party hosted (remote) MCP server that exposes its compliance platform — controls, tests, evidence, frameworks, risks, vendors, personnel, SSP and POA&M records — as 112 M
  name: Secureframe MCP Server
  slug: secureframe-mcp-server
modified: '2026-08-27'
name: Secureframe
nav: Providers
network: true
overview: 'Secureframe publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include GRC, Compliance, SOC 2, ISO 27001, and Risk.


  Secureframe''s developer surface includes documentation, API reference, pricing, signup flow, support, changelog, engineering blog, and 34 more developer resources.'
plans:
- name: Secureframe Plans Pricing
  plan_count: 3
  slug: secureframe-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Secureframe Rate Limits
  slug: secureframe-rate-limits
scopes:
- name: Secureframe Scopes
  scope_count: 0
  slug: secureframe-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 21
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 6.5
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 51.8
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 49.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/secureframe/refs/heads/main/screenshots/secureframe-2026-06-20T193625.png
security:
- kind: authentication
  name: Secureframe Authentication
  slug: secureframe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Secureframe Domain Security
  slug: secureframe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Secureframe Vulnerability Disclosure
  slug: secureframe-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Secureframe Trust Center
  slug: secureframe-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: secureframe
tags:
- GRC
- Compliance
- SOC 2
- ISO 27001
- Risk
- CMMC
- FedRAMP
- Security
- Audit
- Trust
website: https://secureframe.com/
---

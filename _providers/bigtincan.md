---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Bigtincan Agentic Access
  operation_count: 69
  slug: bigtincan-agentic-access
  summary_line: 69 operations · 36 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Bigtincan Hub Public API provides programmatic access to the Bigtincan sales enablement platform, enabling management of sales content, training programs, coaching insights, buyer engagement analy
  name: Bigtincan Hub API
  slug: bigtincan-hub-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bigtincan-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bigtincan-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bigtincan-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bigtincan-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bigtincan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bigtincan.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pubapi.bigtincan.com/doc/interactive/
- group: docs
  title: ''
  type: APIReference
  url: https://pubapi.bigtincan.com/doc/interactive/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/bigtincan-hub-api-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/bigtincan-hub-api-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/bigtincan-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bigtincan-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bigtincan-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bigtincan-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bigtincan-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bigtincan-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/bigtincan-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/bigtincan-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bigtincan-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bigtincan-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bigtincan-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.bigtincan.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bigtincan.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bigtincan.com/
- group: start
  title: ''
  type: SignUp
  url: https://identity.bigtincan.com
- group: start
  title: ''
  type: Login
  url: https://identity.bigtincan.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bigtincan.com/eula/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bigtincan.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.bigtincan.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.bigtincan.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bigtincan
- group: other
  title: ''
  type: X
  url: https://x.com/bigtincan
- group: commercial
  title: ''
  type: Plans
  url: plans/bigtincan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bigtincan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bigtincan-finops.yml
created: '2026-06-13'
description: Bigtincan is an industry-leading sales enablement automation platform providing a REST API for managing sales content, training and coaching programs, buyer engagement analytics, digital sales rooms, and CRM content sync. The platform combines AI-powered content management, sales readiness tools, and buyer engagement capabilities to help revenue teams close deals faster.
finops:
- name: Bigtincan Finops
  service_category: ''
  slug: bigtincan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bigtincan.png
layout: provider
mcp_servers:
- description: Bigtincan ships NO Model Context Protocol server. A search of the provider's site, the MCP ecosystem and the public registries found no hosted endpoint and no stdio package, and no /.well-known/ai-plu
  name: Bigtincan Hub MCP Server (candidate)
  slug: bigtincan-hub-mcp-server-candidate
modified: '2026-08-14'
name: Bigtincan
nav: Providers
network: true
overview: 'Bigtincan publishes 1 API on the [APIs.io](https://apis.io/) network: Hub API. Tagged areas include Sales Enablement, Content Management, Training, Coaching, and Buyer Engagement.


  Bigtincan''s developer surface includes authentication, documentation, API reference, changelog, engineering blog, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Bigtincan Plans Pricing
  plan_count: 5
  slug: bigtincan-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Bigtincan Rate Limits
  slug: bigtincan-rate-limits
scopes:
- name: Bigtincan Scopes
  scope_count: 0
  slug: bigtincan-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.5
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 16.7
    contract_quality: 50.3
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bigtincan/refs/heads/main/screenshots/bigtincan-2026-06-20T173235.png
security:
- kind: authentication
  name: Bigtincan Authentication
  slug: bigtincan-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Bigtincan Domain Security
  slug: bigtincan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bigtincan Trust Center
  slug: bigtincan-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27701
slug: bigtincan
tags:
- Sales Enablement
- Content Management
- Training
- Coaching
- Buyer Engagement
- Analytics
- CRM Integration
- Digital Sales Rooms
website: https://www.bigtincan.com/
---

---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 11.4
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'REST API for the Allego sales enablement platform enabling programmatic access to video coaching sessions, content libraries, learning modules, certifications, rep readiness assessments, conversation '
  name: Allego API
  slug: allego-api
- description: First-party hosted Model Context Protocol server shipped with Allego 9 that exposes Allego deal intelligence, content and enablement to any MCP-compatible AI copilot. Verified live at https://mcp.alle
  name: Allego MCP API Server
  slug: allego-mcp-api-server
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/allego-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allego-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.allego.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.allego.com/platform/integrations/
- group: company
  title: ''
  type: Blog
  url: https://www.allego.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.allego.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.allego.com/support/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allego/
- group: other
  title: ''
  type: X
  url: https://twitter.com/allegosoftware
- group: commercial
  title: ''
  type: Plans
  url: plans/allego-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/allego-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/allego-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/allego-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allego-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allego-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/allego-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/allego-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/allego-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/allego-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.allego.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/allego-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/allego-problem-types.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.allego.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.allego.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/allegosoftware
- group: start
  title: ''
  type: Login
  url: https://my.allego.com/login.do
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.allego.com/
created: '2026-06-13'
description: Allego is an AI-powered sales enablement and revenue training platform providing a REST API for managing video coaching, content libraries, certifications, rep readiness assessments, conversation intelligence, and deal intelligence to help revenue teams improve performance.
finops:
- name: Allego Finops
  service_category: ''
  slug: allego-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allego.png
layout: provider
mcp_servers:
- description: Allego ships a first-party, hosted Model Context Protocol server — marketed as the "Allego MCP API Server" and shipped as part of Allego 9 — that exposes deal intelligence, content and enablement to a
  name: Allego MCP API Server
  slug: allego-mcp-api-server
modified: '2026-08-14'
name: Allego
nav: Providers
network: true
overview: 'Allego publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Enablement, Sales Training, Video Coaching, Content Management, and Conversation Intelligence.


  Allego''s developer surface includes documentation, engineering blog, pricing, support, authentication, and 22 more developer resources.'
plans:
- name: Allego Plans Pricing
  plan_count: 4
  slug: allego-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Allego Rate Limits
  slug: allego-rate-limits
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 24.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allego/refs/heads/main/screenshots/allego-2026-06-20T171529.png
security:
- kind: authentication
  name: Allego Authentication
  slug: allego-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Allego Domain Security
  slug: allego-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Allego Trust Center
  slug: allego-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR, UK Data Protection Law (UKDPL), CCPA, FINRA 17a-3 / 17a-4, FDA 21 CFR Part 11, EU AI Act
slug: allego
tags:
- Sales Enablement
- Sales Training
- Video Coaching
- Content Management
- Conversation Intelligence
- Deal Intelligence
- Revenue Enablement
- Certifications
- Artificial Intelligence
website: https://www.allego.com/
---

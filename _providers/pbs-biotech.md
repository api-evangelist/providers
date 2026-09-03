---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.1
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The agent-callable commerce surface of the PBS Biotech online store. Implemented by Shopify on the company's own shoppbsbiotech.com host and advertised by the store's own /llms.txt, /agents.md and /ro
  name: PBS Biotech Store Agent Commerce (UCP/MCP)
  slug: pbs-biotech-store-agent-commerce
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pbs-biotech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pbsbiotech.com/
- group: operate
  title: ''
  type: Support
  url: https://pbsbiotech.com/customer-support-portal
- group: operate
  title: ''
  type: HelpCenter
  url: https://pbsbiotech.com/help-center
- group: start
  title: ''
  type: Login
  url: https://pbsbiotech.com/vertical-wheel-scaling-calculator-sign-in
- group: commercial
  title: ''
  type: Pricing
  url: https://pbsbiotech.com/service-plans
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pbsbiotech.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shoppbsbiotech.com/policies/terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pbs-biotech-inc.
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pbs-biotech-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pbs-biotech-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pbs-biotech-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pbs-biotech-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pbs-biotech-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pbs-biotech-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/pbs-biotech-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pbs-biotech-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pbs-biotech-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pbs-biotech-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pbs-biotech-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pbs-biotech-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pbs-biotech-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/pbs-biotech-conformance.yml
created: '2026-08-26'
description: 'PBS Biotech, Inc. is a Camarillo, California manufacturer of single-use Vertical-Wheel bioreactor systems for cell and gene therapy manufacturing, scaling from 0.1 L benchtop vessels (PBS-Mini 0.1, PBS-Mini 0.5, MiniPRO) through 3 L, 15 L and 80 L production systems (PBS-3, PBS-15, PBS-80), together with single-use vessels, perfusion consumables, process development (CDO) services, field service and service plans. The company is a hardware and consumables business, not a software vendor: it publishes no developer program, no REST/GraphQL API and no machine-readable contract for its bioreactor control software, whose releases are documented only as versioned PDF release notes. Its one genuinely machine-callable, agent-facing surface is its own online store at shoppbsbiotech.com, a Shopify-hosted storefront that serves an llms.txt/agents.md agent instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and an anonymous MCP endpoint at /api/ucp/mcp
  exposing 13 catalog, cart, checkout and order tools for agent-driven purchase of PBS Biotech consumables.'
image: https://cdn.prod.website-files.com/62cc627d7fe73059b1484e97/6375797b9b37d215da32705e_PBS_Wing_Logo_1375C-p-500.jpg
layout: provider
mcp_servers:
- description: ''
  name: PBS Biotech Store Agent Commerce (UCP/MCP)
  slug: pbs-biotech-store-agent-commerce-ucpmcp
modified: '2026-08-26'
name: PBS Biotech
nav: Providers
network: true
overview: 'PBS Biotech publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Biotechnology, Bioprocessing, and Cell Therapy.


  PBS Biotech''s developer surface includes support, pricing, authentication, changelog, and 20 more developer resources.'
plans:
- name: Pbs Biotech Plans Pricing
  plan_count: 0
  slug: pbs-biotech-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Pbs Biotech Rate Limits
  slug: pbs-biotech-rate-limits
scopes:
- name: Pbs Biotech Scopes
  scope_count: 0
  slug: pbs-biotech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 31.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pbs-biotech/refs/heads/main/screenshots/pbs-biotech-2026-09-02T150924.png
security:
- kind: authentication
  name: Pbs Biotech Authentication
  slug: pbs-biotech-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Pbs Biotech Domain Security
  slug: pbs-biotech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pbs-biotech
tags:
- Company
- Life Sciences
- Biotechnology
- Bioprocessing
- Cell Therapy
- Laboratory Equipment
- Manufacturing
- E-Commerce
- Agent Commerce
- MCP
website: https://pbsbiotech.com/
---

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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 13.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'The agent-callable commerce surface for LinusBio''s Traced environmental exposure test, served from the traced.life storefront. It implements the Universal Commerce Protocol (UCP) 2026-04-08 over MCP: '
  name: Traced UCP Commerce (MCP)
  slug: linusbio-traced-ucp-commerce
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.linusbio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.linusbio.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.clearstrandasd.com/support/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://traced.life/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://traced.life/policies/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://traced.life/products/test
- group: docs
  title: ''
  type: Documentation
  url: https://traced.life/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://traced.life/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linusbio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/linusbio-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/linusbio-traced-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linusbio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/linusbio-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linusbio-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/linusbio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/linusbio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linusbio-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/linusbio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/linusbio-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linusbio-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/linusbio-conformance.yml
created: '2026-08-25'
description: LinusBio (Linus Biotechnology Inc.) is a New York-based precision-medicine company spun out of the Mount Sinai Institute for Exposomic Research that commercializes "temporal exposomics sequencing" — a robotics, laser-ablation and mass-spectrometry platform that reads a single strand of hair like growth rings to reconstruct hundreds of time-resolved measurements of a person's chemical and biological exposures, then runs them through an AI pipeline to produce biomarkers. Its clinical product ClearStrand-ASD (formerly StrandDx-ASD) is an FDA Breakthrough Device-designated laboratory developed test run in a CLIA-certified lab to help rule out autism spectrum disorder in children from one month to ten years of age, and its consumer product Traced is a $299 at-home environmental exposure test measuring 15 elements across a 30-day timeline. LinusBio publishes no developer program, no OpenAPI and no public REST API; its only machine-callable surface is the Shopify-hosted Universal Commerce
  Protocol (UCP) MCP endpoint on the traced.life storefront, through which an agent can search the catalog, build a cart and open a checkout for the Traced test under a buyer-approval rule.
image: https://www.linusbio.com/assets/site/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Traced UCP Commerce MCP Server
  slug: traced-ucp-commerce-mcp-server
modified: '2026-08-25'
name: LinusBio
nav: Providers
network: true
overview: 'LinusBio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Diagnostics, Precision Medicine, and Biotechnology.


  LinusBio''s developer surface includes engineering blog, support, pricing, documentation, getting-started guide, authentication, and 16 more developer resources.'
plans:
- name: Linusbio Plans Pricing
  plan_count: 0
  slug: linusbio-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Linusbio Rate Limits
  slug: linusbio-rate-limits
scopes:
- name: Linusbio Scopes
  scope_count: 0
  slug: linusbio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 34.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linusbio/refs/heads/main/screenshots/linusbio-2026-09-02T150259.png
security:
- kind: authentication
  name: Linusbio Authentication
  slug: linusbio-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Linusbio Domain Security
  slug: linusbio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: linusbio
tags:
- Company
- Health
- Diagnostics
- Precision Medicine
- Biotechnology
- Exposomics
- Life Sciences
- Autism
- Commerce
- Agents
website: https://www.linusbio.com/
---

---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: An OAuth-protected Model Context Protocol endpoint served from LiftLab's own hostname connect.liftlab.com, discovered by certificate-transparency enumeration rather than from documentation. An anonymo
  name: LiftLab Connect MCP Server
  slug: liftlab-connect-mcp
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liftlab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://liftlab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://liftlab.com/resources/
- group: start
  title: ''
  type: GettingStarted
  url: https://liftlab.com/platform/unified-marketing-measurement/
- group: operate
  title: ''
  type: Support
  url: https://liftlab.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://liftlab.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://liftlab.com/request-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://liftlab.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://liftlab.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liftlab-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/liftlab-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://liftlab-analytics-inc.trust.site/
- group: auth
  title: ''
  type: TrustCenter
  url: security/liftlab-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/liftlab-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liftlab-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/liftlab-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/liftlab-well-known.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/liftlab-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/liftlab-plans-pricing.yml
created: '2026-07-17'
description: 'LiftLab (LiftLab Analytics, Inc.) is a marketing measurement and capital allocation platform for enterprise marketing, analytics, and finance leaders. Its Two-Stage Agile Marketing Mix Model (AMM) separates ad marketplace auction dynamics — CPM/CPC volatility and competitive pressure — from true consumer demand response, producing channel response curves and marginal ROI (mROAS) that are not contaminated by marketplace noise. A geo-based Incrementality Testing Suite feeds causal results back into the model through the Trust Engine as permanent calibration inputs, PlatformSense applies live ad platform data to those stable curves for daily channel intelligence, the Scenario Planner turns model output into constraint-aware, finance-ready budget plans, and Miles AI answers natural-language questions grounded in the model. LiftLab serves D2C/ecommerce, CPG, and omnichannel retail brands including Pandora, Cinemark, Quicken, SKIMS, and Thrive Market. Headquartered in Oakland, CA;
  SOC 2 Type II and ISO 27001:2013 certified, GDPR and CCPA compliant. LiftLab publishes no developer portal, no API documentation and no OpenAPI, but it does operate one undocumented machine surface: an OAuth-protected Model Context Protocol endpoint at https://connect.liftlab.com/server/api/mcp, advertised through RFC 8414 and RFC 9728 discovery documents on its own hostname and scoped for a Claude connector. That host is a white-labeled TapClicks deployment, so the agent surface is served by LiftLab but supplied by a vendor.'
image: https://liftlab.com/assets/logo.svg
layout: provider
mcp_servers:
- description: A live, OAuth-protected Model Context Protocol server served from LiftLab's own hostname connect.liftlab.com. Discovered through certificate-transparency enumeration of *.liftlab.com, not from any Lif
  name: LiftLab Connect MCP Server
  slug: liftlab-connect-mcp-server
modified: '2026-08-13'
name: LiftLab
nav: Providers
network: true
overview: 'LiftLab publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Marketing, Marketing Measurement, and Marketing Mix Modeling.


  LiftLab''s developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, authentication, and 13 more developer resources.'
plans:
- name: Liftlab Plans Pricing
  plan_count: 0
  slug: liftlab-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Liftlab Rate Limits
  slug: liftlab-rate-limits
scopes:
- name: Liftlab Scopes
  scope_count: 1
  slug: liftlab-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 27.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liftlab/refs/heads/main/screenshots/liftlab-2026-07-25T225100.png
security:
- kind: authentication
  name: Liftlab Authentication
  slug: liftlab-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Liftlab Domain Security
  slug: liftlab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Liftlab Trust Center
  slug: liftlab-trust-center
  summary_line: SOC 2, SOC 2 Type II, ISO 27001, ISO 27001:2013, GDPR, CCPA
slug: liftlab
tags:
- Company
- Enterprise
- Marketing
- Marketing Measurement
- Marketing Mix Modeling
- Incrementality
- Analytics
- MarTech
- Attribution
- Budget Optimization
- Data Science
- Software-as-a-Service
website: https://liftlab.com/
---

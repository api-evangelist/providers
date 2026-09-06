---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.3
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/madethis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://madethis.com
- group: start
  title: ''
  type: SignUp
  url: https://madethis.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://madethis.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://madethis.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://madethis.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/madethis-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/madethis-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/madethis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/madethis-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/madethis-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/madethis-plans-pricing.yml
- group: operate
  title: ''
  type: Support
  url: https://madethis.com/support
- group: start
  title: ''
  type: Login
  url: https://madethis.com/login
coverage:
  checked: '2026-08-13'
  detail: 'MadeThis is an end-user product with no developer program at all: every OpenAPI, Swagger, GraphQL, llms.txt and agent-card path 404s on madethis.com, and its own product backend api.madethis.com answers every path with the Convex router''s "No matching routes found", so the only machine-readable documents on any MadeThis host are the OIDC/OAuth discovery files its vendor identity subdomain clerk.madethis.com serves for end-user sign-in.'
  evidence:
  - status: 404
    url: https://madethis.com/openapi.json
  - status: 404
    url: https://api.madethis.com/openapi.json
  - status: 404
    url: https://madethis.com/.well-known/agent-card.json
  - status: 404
    url: https://madethis.com/llms.txt
  - status: 200
    url: https://clerk.madethis.com/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: MadeThis (madethis.com) is a Y Combinator (Fall 2025) startup based in San Francisco, founded in 2025 by Jacob Wright, Cambree Bernkopf and Santiago Gomez Paz, that markets itself as "Your AI Co-Founder" and "the autonomous business platform" — a team of AI employees that build, market, and run a business on the founder's behalf. A user describes a business idea and MadeThis autonomously handles website and app development, Stripe-based payment and billing setup, ad-campaign creation and optimization, 24/7 AI customer support, email automation and cold outbound, market and competitor research, and code generation and deployment, iterating on founder feedback. It targets e-commerce, SaaS, agencies, online courses, coaching, and service businesses across Starter ($49/mo), Growth ($79/mo), Scale ($199/mo) and Enterprise (from $5,000/mo) tiers metered in AI-work credits, with an Enterprise line that builds a "company brain" digital twin and trains AI employees on a customer's top
  performers. MadeThis publishes no public API, developer portal, SDK, CLI or API documentation — every spec path probed on madethis.com and on its Convex product backend api.madethis.com returns 404. The only machine-readable documents any MadeThis host serves are the OIDC and RFC 8414 discovery documents on clerk.madethis.com, a vendor-run identity instance for end-user sign-in. Its Enterprise page notes that customer systems connect through MCP and ACP, which makes MadeThis an MCP consumer rather than an MCP publisher.
image: https://madethis.com/opengraph-image
layout: provider
modified: '2026-08-13'
name: MadeThis
nav: Providers
network: true
overview: 'MadeThis is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Business Automation, and Software-as-a-Service.


  MadeThis'' developer surface includes signup flow, pricing, authentication, support, and 10 more developer resources.'
plans:
- name: Madethis Plans Pricing
  plan_count: 4
  slug: madethis-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Madethis Rate Limits
  slug: madethis-rate-limits
scopes:
- name: Madethis Scopes
  scope_count: 7
  slug: madethis-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 23.8
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/madethis/refs/heads/main/screenshots/madethis-2026-07-25T225830.png
security:
- kind: authentication
  name: Madethis Authentication
  slug: madethis-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Madethis Domain Security
  slug: madethis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: madethis
tags:
- Company
- Artificial Intelligence
- AI Agents
- Business Automation
- Software-as-a-Service
- Marketing Automation
- Startup Tools
- Y Combinator
- No-Code
- Website Builder
- E-Commerce
- Small Business
- AI Employees
website: https://madethis.com
---

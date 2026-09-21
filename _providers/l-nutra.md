---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-09-20'
api_count: 3
apis:
- description: The agent-facing commerce surface of L-Nutra's direct-to-consumer ProLon storefront. An anonymous MCP endpoint at https://prolonlife.com/api/ucp/mcp implements Universal Commerce Protocol 2026-04-08 a
  name: ProLon Life Agentic Commerce (UCP/MCP)
  slug: prolon-life-agentic-commerce-ucpmcp
- description: The agent-facing commerce surface of L-Nutra Health, the employer / health-plan channel storefront. An anonymous MCP endpoint at https://l-nutrahealth.com/api/ucp/mcp implements Universal Commerce Pro
  name: L-Nutra Health Agentic Commerce (UCP/MCP)
  slug: l-nutra-health-agentic-commerce-ucpmcp
- description: 'The agent-facing commerce surface of L-Nutra Professional, the practitioner ordering storefront. An anonymous MCP endpoint at https://l-nutraprofessional.com/api/ucp/mcp implements Universal Commerce '
  name: ProLon Professional Agentic Commerce (UCP/MCP)
  slug: prolon-professional-agentic-commerce-ucpmcp
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://prolonlife.com/
- group: docs
  title: ''
  type: Documentation
  url: https://prolonlife.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://prolonlife.com/pages/faqs
- group: commercial
  title: ''
  type: Pricing
  url: https://prolonlife.com/collections/all
- group: start
  title: ''
  type: SignUp
  url: https://prolonlife.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://prolonlife.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prolonlife.com/policies/privacy-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/mcp/l-nutra-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/l-nutra-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/mcp/l-nutra-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/l-nutra-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/llms/l-nutra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/l-nutra-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/well-known/l-nutra-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/l-nutra-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/authentication/l-nutra-authentication.yml
  title: ''
  type: Authentication
  url: authentication/l-nutra-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/scopes/l-nutra-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/l-nutra-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/conformance/l-nutra-conformance.yml
  title: ''
  type: Conformance
  url: conformance/l-nutra-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/conventions/l-nutra-conventions.yml
  title: ''
  type: Conventions
  url: conventions/l-nutra-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/conventions/l-nutra-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/l-nutra-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/lifecycle/l-nutra-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/l-nutra-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/data-model/l-nutra-data-model.yml
  title: ''
  type: DataModel
  url: data-model/l-nutra-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/rate-limits/l-nutra-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/l-nutra-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/plans/l-nutra-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/l-nutra-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/packages/l-nutra-packages.yml
  title: ''
  type: Packages
  url: packages/l-nutra-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/security/l-nutra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/l-nutra-domain-security.yml
created: '2026-08-23'
description: 'L-Nutra, Inc. is a Los Angeles based nutri-technology company founded on the fasting-mimicking diet (FMD) research of Dr. Valter Longo at the USC Longevity Institute. It develops and sells clinically studied nutrition programs — the ProLon 5-Day Fasting Mimicking Diet, Fast Bar and related longevity nutrition products — direct to consumers, to healthcare providers, and through an employer and health-plan channel. L-Nutra is not a developer-platform company and publishes no developer portal, OpenAPI description or API reference of its own. Its machine-readable surface is the agentic-commerce layer of its three Shopify storefronts (prolonlife.com, l-nutrahealth.com and l-nutraprofessional.com): each serves an llms.txt / agents.md agent instruction document, a Universal Commerce Protocol (UCP) discovery profile at /.well-known/ucp, an anonymous MCP endpoint at /api/ucp/mcp exposing thirteen catalog, cart, checkout and order tools, a Shopify Storefront MCP endpoint at /api/mcp,
  and Shopify customer-account OpenID Connect discovery documents.'
image: https://prolonlife.com/cdn/shop/files/Prolon_Icon_light_green.png
layout: provider
mcp_servers:
- description: L-Nutra operates no developer platform, but all three of its storefronts expose live, anonymous, remote MCP endpoints. Each storefront serves a Universal Commerce Protocol (UCP) 2026-04-08 discovery p
  name: L-Nutra MCP Server
  slug: l-nutra-mcp-server
modified: '2026-08-23'
name: L-Nutra
nav: Providers
network: true
overview: 'L-Nutra publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nutrition, Health, Longevity, and Consumer Products.


  L-Nutra''s developer surface includes documentation, support, pricing, signup flow, authentication, and 18 more developer resources.'
plans:
- name: L Nutra Plans Pricing
  plan_count: 0
  slug: l-nutra-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: L Nutra Rate Limits
  slug: l-nutra-rate-limits
scopes:
- name: L Nutra Scopes
  scope_count: 0
  slug: l-nutra-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.0
    discoverability: 81.5
    operational_transparency: 0.0
  previous_composite: 29.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/l-nutra/refs/heads/main/screenshots/l-nutra-2026-09-02T150213.png
security:
- kind: authentication
  name: L Nutra Authentication
  slug: l-nutra-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: L Nutra Domain Security
  slug: l-nutra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: l-nutra
tags:
- Company
- Nutrition
- Health
- Longevity
- Consumer Products
- E-Commerce
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
website: https://prolonlife.com/
---

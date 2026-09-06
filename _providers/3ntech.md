---
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
    error_semantics: documented
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
  score: 25.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Universal Commerce Protocol shopping service 3N Eyecare exposes on its own storefront host. An anonymous JSON-RPC 2.0 MCP endpoint serves 13 tools for catalog search and lookup, cart create/update
  name: 3N Eyecare Agentic Commerce (UCP / MCP)
  slug: 3n-eyecare-agentic-commerce-ucp-mcp
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3ntech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.3neyecare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.3neyecare.com/agents.md
- group: company
  title: ''
  type: Blog
  url: https://www.3neyecare.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://www.3neyecare.com/pages/contact
- group: start
  title: ''
  type: SignUp
  url: https://account.3neyecare.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.3neyecare.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.3neyecare.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/3ntech-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3ntech-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/3ntech-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/3ntech-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/3ntech-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/3ntech-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/3ntech-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/3ntech-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/3ntech-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/3ntech-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/3ntech-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/3ntech-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-05'
description: '3N TECH (Suzhou 3N Biological Technology Co., Ltd.) is a Chinese eye-care medical-device maker founded in 2015 and headquartered in Suzhou Industrial Park BioBAY, with an international arm selling in Hong Kong and the United States. It develops active contact-lens care hardware built on its patented Electrophoresis-Disintegration ("Elepy") technology, and shipped the first contact-lens cleaner to hold an FDA 510(k) clearance for that mechanism. The company sells under two brands: 3N in mainland China and ReO2 internationally, through the 3N Eyecare direct-to-consumer storefront. 3N TECH publishes no developer program and no OpenAPI. Its only machine-readable, publicly callable surface is the agentic-commerce layer on its own storefront host: an anonymous UCP (Universal Commerce Protocol) merchant profile at /.well-known/ucp.json, an unauthenticated MCP endpoint at /api/ucp/mcp serving 13 cart, checkout, order and catalog tools, an llms.txt / agents.md pair of agent instructions,
  and Shopify Customer Account OAuth 2.0 / OpenID Connect discovery documents. That surface is platform-authored by Shopify and served under the company''s domain, which this profile records explicitly rather than crediting it as first-party API design.'
image: https://www.3neyecare.com/cdn/shop/files/LOGO.png?v=1683448741
layout: provider
mcp_servers:
- description: ''
  name: 3N TECH MCP Server
  slug: 3n-tech-mcp-server
modified: '2026-09-05'
name: 3N TECH
nav: Providers
network: true
overview: '3N TECH publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Eye Care, Medical Devices, Consumer Health, and Contact Lenses.


  3N TECH''s developer surface includes documentation, engineering blog, support, signup flow, authentication, and 16 more developer resources.'
plans:
- name: 3Ntech Plans Pricing
  plan_count: 0
  slug: 3ntech-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: 3Ntech Rate Limits
  slug: 3ntech-rate-limits
scopes:
- name: 3Ntech Scopes
  scope_count: 4
  slug: 3ntech-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 3Ntech Authentication
  slug: 3ntech-authentication
  summary_line: oauth2/openIdConnect/none · 3 schemes
- kind: domain-security
  name: 3Ntech Domain Security
  slug: 3ntech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 3ntech
tags:
- Company
- Eye Care
- Medical Devices
- Consumer Health
- Contact Lenses
- Ecommerce
- Agentic Commerce
- Universal Commerce Protocol
- Model Context Protocol
- Manufacturing
website: https://www.3neyecare.com/
---

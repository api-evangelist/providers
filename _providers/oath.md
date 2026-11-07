---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GraphQL API for Oath Soil Life e‑commerce platform.
  name: Oath Soil Life API
  slug: oath-soil-life-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/oath/llms/oath-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oath-llms.txt
- group: agent
  href: https://artifacts.apis.io/oath/mcp/oath-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/oath-mcp.yml
- group: agent
  href: https://artifacts.apis.io/oath/well-known/oath-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/oath-well-known.yml
- group: other
  href: https://artifacts.apis.io/oath/hosts/oath-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oath-hosts.yml
- group: other
  href: https://artifacts.apis.io/oath/vendors/oath-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oath-vendors.yml
- group: auth
  href: https://artifacts.apis.io/oath/security/oath-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oath-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oathsoillife.com
- group: company
  title: ''
  type: Blog
  url: https://www.oathsoillife.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://www.oathsoillife.com/pages/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oathsoillife.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oathsoillife.com/policies/privacy-policy
created: '2026-10-29'
description: Oath Soil Life is a US‑based company that offers products designed to replenish the soil microbiome, helping trees, lawns, and gardens thrive. Operating an e‑commerce storefront on Shopify, the brand markets soil‑health solutions and educational content to support sustainable gardening practices. The website provides a blog with gardening tips, a contact page for support, and clear terms of service and privacy policy. Oath aims to improve plant health through microbiome enrichment.
image: https://www.oathsoillife.com/cdn/shop/files/Logo.svg?v=1747370641&width=410
layout: provider
mcp_servers:
- description: Remote MCP server at www.oathsoillife.com.
  name: Oath MCP Server
  slug: oath-mcp-yml
modified: '2026-10-29'
name: Oath
nav: Providers
network: true
overview: 'Oath is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Soil Health, Gardening, and Sustainability.


  Oath''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Oath Plans Pricing
  plan_count: 0
  slug: oath-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Oath Rate Limits
  slug: oath-rate-limits
scopes:
- name: Oath Scopes
  scope_count: 0
  slug: oath-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/oath/oath-2026-11-03T140420.png
security:
- kind: authentication
  name: Oath Authentication
  slug: oath-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Oath Domain Security
  slug: oath-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oath
tags:
- Company
- Agriculture
- Soil Health
- Gardening
- Sustainability
- E-Commerce
website: https://oathsoillife.com
---

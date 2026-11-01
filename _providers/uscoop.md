---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Universal Commerce Protocol shopping service exposed over MCP by the tnuck.com Shopify storefront - catalog search, cart, checkout, fulfillment, discounts, and orders, with buyer-approved payment. Dis
  name: Storefront Agent Commerce (UCP over MCP)
  slug: storefront-agent-commerce-ucp-over-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://tnuck.com
- group: docs
  title: ''
  type: Documentation
  url: https://tnuck.com/agents.md
- group: agent
  href: https://artifacts.apis.io/uscoop/mcp/uscoop-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/uscoop-mcp.yml
- group: agent
  href: https://artifacts.apis.io/uscoop/llms/uscoop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uscoop-llms.txt
- group: agent
  href: https://artifacts.apis.io/uscoop/well-known/uscoop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uscoop-well-known.yml
- group: auth
  href: https://artifacts.apis.io/uscoop/authentication/uscoop-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uscoop-authentication.yml
- group: auth
  href: https://artifacts.apis.io/uscoop/scopes/uscoop-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/uscoop-scopes.yml
- group: design
  href: https://artifacts.apis.io/uscoop/conformance/uscoop-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uscoop-conformance.yml
- group: agent
  href: https://artifacts.apis.io/uscoop/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/uscoop/security/uscoop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uscoop-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tnuck.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tnuck.com/policies/terms-of-service
- group: start
  title: ''
  type: Login
  url: https://tnuck.com/account
- group: operate
  title: ''
  type: Support
  url: https://tnuck.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://tnuck.com/blogs/news
created: '2026-07-17'
description: uScoop appears in the 500 Global portfolio mapped to the website tnuck.com. The original uScoop was a 2010 college-student daily-deals startup (theuscoop.com, later uscoop.com); both domains are now offline or parked for sale, and the recorded website today is the Tuckernuck online retail storefront on Shopify. This profile documents the live API and agent surface of that recorded website, which publishes llms.txt and agents.md agent instructions, a Universal Commerce Protocol (UCP) merchant profile, a live MCP shopping endpoint, and OpenID Connect / OAuth 2.0 discovery documents for customer accounts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uscoop.png
layout: provider
mcp_servers:
- description: Remote MCP server at tnuck.com over HTTP; 5 tools listed.
  name: uScoop MCP Server
  slug: tnuck-ucp-shopping
modified: '2026-07-21'
name: uScoop
nav: Providers
network: true
overview: 'uScoop is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Fashion, E-Commerce, and Agentic Commerce.


  uScoop''s developer surface includes documentation, authentication, support, engineering blog, and 11 more developer resources.'
random_paper: 17
scopes:
- name: Uscoop Scopes
  scope_count: 4
  slug: uscoop-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 24.5
  provenance:
    conformance: first-party
    mcp: platform-generated
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/uscoop/uscoop-2026-09-02T165232.png
security:
- kind: authentication
  name: Uscoop Authentication
  slug: uscoop-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Uscoop Domain Security
  slug: uscoop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Shop the tnuck.com storefront as an agent (UCP/MCP)
  slug: uscoop-agent-shopping
slug: uscoop
tags:
- Company
- Retail
- Fashion
- E-Commerce
- Agentic Commerce
- Shopping
website: https://tnuck.com
---

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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Universal Commerce Protocol shopping service exposed over MCP by the tnuck.com Shopify storefront - catalog search, cart, checkout, fulfillment, discounts, and orders, with buyer-approved payment. Dis
  name: Storefront Agent Commerce (UCP over MCP)
  slug: storefront-agent-commerce-ucp-over-mcp
artifact_total: 5
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
  title: ''
  type: MCPServer
  url: mcp/uscoop-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uscoop-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uscoop-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uscoop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uscoop-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uscoop-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
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
- description: ''
  name: uScoop MCP Server
  slug: uscoop-mcp-server
modified: '2026-07-21'
name: uScoop
nav: Providers
network: true
overview: 'uScoop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Fashion, E-Commerce, and Agentic Commerce.


  uScoop''s developer surface includes documentation, authentication, support, engineering blog, and 11 more developer resources.'
random_paper: 14
scopes:
- name: Uscoop Scopes
  scope_count: 4
  slug: uscoop-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uscoop/refs/heads/main/screenshots/uscoop-2026-09-02T165232.png
security:
- kind: authentication
  name: Uscoop Authentication
  slug: uscoop-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Uscoop Domain Security
  slug: uscoop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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

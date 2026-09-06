---
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
    dynamic_client_registration: true
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
  score: 24.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: A hosted Model Context Protocol endpoint operated by Abatable at mcp.abatable.com, fronted by Cloudflare Access. It advertises itself as an OAuth protected resource under RFC 9728 and publishes RFC 84
  name: Abatable MCP Server
  slug: abatable-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://abatable.com/
- group: company
  title: ''
  type: Blog
  url: https://abatable.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://abatable.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abatable.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abatable.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.abatable.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Abatable
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abatable/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@abatable
- group: operate
  title: ''
  type: StatusPage
  url: https://status.abatable.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abatable-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/abatable-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/abatable-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abatable-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/abatable-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/abatable-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/abatable-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abatable-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/abatable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abatable-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/abatable-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abatable-domain-security.yml
created: '2026-09-05'
description: Abatable (legal entity Zero Imprint Ltd, London) operates a procurement and intelligence platform for environmental assets — principally voluntary carbon credits and CORSIA-eligible units. Buyers run structured RFPs against a network of 5,000+ project developers, commission tiered third-party due diligence, and monitor delivered portfolios from one dashboard; investors and developers buy the same market intelligence layer, built from 85,000+ transaction price points, vintage forward curves, country policy profiles and supply/demand tracking across 18,000+ projects in 23 registries. The company holds no inventory and represents no seller, and is funded by buyers rather than suppliers. The product is delivered as an authenticated SaaS application at app.abatable.com; there is no public developer program, no published API reference and no machine-readable contract, though the company does operate an undocumented, OAuth-gated Model Context Protocol server at mcp.abatable.com.
image: https://cdn.prod.website-files.com/6a21901ab9e1e5d902f470f8/6a21901ab9e1e5d902f471a6_abatable-open-graph.jpg
layout: provider
mcp_servers:
- description: A hosted Model Context Protocol server operated by Abatable at mcp.abatable.com. It is not announced anywhere on abatable.com, in the site llms.txt, or in the GitHub organisation — it was found by pro
  name: Abatable MCP Server
  slug: abatable-mcp-server
modified: '2026-09-05'
name: Abatable
nav: Providers
network: true
overview: 'Abatable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Carbon Markets, Carbon Credits, Carbon Offsets, Environmental Assets, and Voluntary Carbon Market.


  Abatable''s developer surface includes engineering blog, support, YouTube channel, authentication, and 18 more developer resources.'
plans:
- name: Abatable Plans Pricing
  plan_count: 0
  slug: abatable-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Abatable Rate Limits
  slug: abatable-rate-limits
scopes:
- name: Abatable Scopes
  scope_count: 14
  slug: abatable-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 12
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
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Abatable Authentication
  slug: abatable-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Abatable Domain Security
  slug: abatable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abatable
tags:
- Carbon Markets
- Carbon Credits
- Carbon Offsets
- Environmental Assets
- Voluntary Carbon Market
- CORSIA
- Climate
- Sustainability
- Net Zero
- Procurement
- Market Intelligence
- Due Diligence
- ESG
- MCP
website: https://abatable.com/
---

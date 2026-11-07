---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/starshipit/llms/starshipit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/starshipit-llms.txt
- group: agent
  href: https://artifacts.apis.io/starshipit/mcp/starshipit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/starshipit-mcp.yml
- group: agent
  href: https://artifacts.apis.io/starshipit/well-known/starshipit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/starshipit-well-known.yml
- group: other
  href: https://artifacts.apis.io/starshipit/hosts/starshipit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/starshipit-hosts.yml
- group: other
  href: https://artifacts.apis.io/starshipit/vendors/starshipit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/starshipit-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.starshipit.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.starshipit.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.starshipit.com/Dashboard/SignUp.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://starshipit.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.starshipit.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://support.starshipit.com/categories/getting-started
- group: auth
  href: https://artifacts.apis.io/starshipit/security/starshipit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/starshipit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://starshipit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.starshipit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.starshipit.com/
- group: company
  title: ''
  type: Blog
  url: https://starshipit.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://starshipit.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://starshipit.com/support-centre
- group: company
  title: ''
  type: About
  url: https://starshipit.com/about-us
- group: company
  title: ''
  type: Careers
  url: https://starshipit.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://starshipit.com/contact-us
- group: company
  title: ''
  type: Partner
  url: https://starshipit.com/partner
- group: other
  title: ''
  type: ReferralProgram
  url: https://starshipit.com/referral-program
coverage:
  checked: '2026-10-26'
  detail: Developer portal at https://api-docs.starshipit.com/ returns HTML with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://api-docs.starshipit.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Starshipit is a shipping and fulfilment platform that helps retailers automate label creation, manage over 60 carriers, and send shipping notifications, delivering better customer experiences across Australia and New Zealand. The service offers a free trial, integrated pricing, and extensive support resources for eCommerce businesses.
image: https://starshipit.com/photography/pages/home-seo-photo-en-nz-461c37ad.webp
layout: provider
mcp_servers:
- description: Remote MCP server at ssi-website-static-nkcp0thgo-starshipit-6076ea81.vercel.app.
  name: Starshipit MCP Server
  slug: starshipit-mcp-yml
modified: '2026-10-26'
name: Starshipit
nav: Providers
network: true
overview: 'Starshipit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Fulfilment, E-Commerce, Automation, and Australia.


  Starshipit''s developer surface includes signup flow, changelog, getting-started guide, documentation, engineering blog, pricing, support, and 16 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 58.3
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/starshipit/starshipit-2026-11-03T143743.png
security:
- kind: domain-security
  name: Starshipit Domain Security
  slug: starshipit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: starshipit
tags:
- Shipping
- Fulfilment
- E-Commerce
- Automation
- Australia
- New Zealand
website: https://starshipit.com/
---

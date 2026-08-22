---
access_model:
  confidence: high
  label: No published API · No developer onboarding
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probe
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mcgrath-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mcgrath-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mcgrath-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.mcgrath.com.au/
- group: company
  title: ''
  type: About
  url: https://www.mcgrath.com.au/about-us
- group: operate
  title: ''
  type: Contact
  url: https://www.mcgrath.com.au/contact-us
- group: other
  title: ''
  type: Offices
  url: https://www.mcgrath.com.au/offices
- group: other
  title: ''
  type: Agents
  url: https://www.mcgrath.com.au/agents
- group: company
  title: ''
  type: Careers
  url: https://www.mcgrath.com.au/join-us
- group: company
  title: ''
  type: LinkedIn
  url: https://au.linkedin.com/company/mcgrath-estate-agents
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/McGrathEstateAgents/
- group: other
  title: ''
  type: Robots
  url: https://www.mcgrath.com.au/robots.txt
- group: company
  title: ''
  type: Blog
  url: https://www.mcgrath.com.au/articles
- group: other
  title: ''
  type: Research
  url: https://www.mcgrath.com.au/mcgrath-report
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mcgrath.com.au/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mcgrath.com.au/terms
- group: other
  title: ''
  type: Sitemap
  url: https://www.mcgrath.com.au/sitemap/general.xml
- group: other
  title: ''
  type: X
  url: https://x.com/mcgrathestate
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/mcgrathestateagents/
created: '2026-07-26'
description: 'McGrath is one of Australia''s largest residential real estate brokerage networks, founded in Sydney in 1988 by John McGrath and operating a mixed company-owned and franchise network of roughly 118 offices across New South Wales, Queensland, the ACT, Victoria and Tasmania. Its business lines span residential sales, property management and rentals, projects and new-development marketing, rural and livestock, an Asia Desk for offshore buyers, and mortgage broking through Oxygen Home Loans. Listed on the ASX in 2015 as McGrath Limited (ASX:MEA), it was acquired in June 2024 by a consortium of Knight Frank Australia and New Zealand''s Bayleys for A$95.5m and delisted from the ASX on 28 June 2024. McGrath sits on the demand side of the Australian property value chain: it is a brokerage that publishes listings into the REA Group (realestate.com.au) and Domain portal duopoly, settles transactions over the PEXA electronic conveyancing network, and consumes valuation data from PropTrack
  and CoreLogic rather than producing any of those rails itself. Its API posture is honestly nil. No developer portal exists — developer., developers., api., docs., feeds., data. and portal. subdomains of mcgrath.com.au all fail to resolve (NXDOMAIN), and /developers, /api, /docs, /api-docs, /openapi.json, /swagger.json, /$metadata and /.well-known/openid-configuration all return HTTP 404. RESO — the only genuinely mandated machine-readable real estate contract anywhere in this study — is a North American standard driven by NAR and MLS membership; it has no Australian counterpart and McGrath has no RESO Web API or Data Dictionary certification, no OData surface, and no Universal Property Identifier usage. The only interoperability standards McGrath demonstrably implements are robots.txt and twelve XML sitemaps; every /.well-known/ document probed — security.txt, openid-configuration, oauth-authorization-server, api-catalog, ai-plugin.json — and /llms.txt return 404. Its robots.txt enumerates
  twenty crawler groups including GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended, CCBot and Bytespider, but under RFC 9309 group-matching rules those named AI agents are disallowed only from Google Maps JS/RPC paths — the /properties/ and /search/ disallow lands solely on User-agent: *, so the listing corpus is nominally open to the named AI crawlers and closed to generic ones, while the properties-buy/sold/rent/leased sitemaps advertise those same URLs. Reachability is the harder gate: www.mcgrath.com.au sits behind a Vercel Security Checkpoint that answers scripted clients with HTTP 429 and a browser challenge on every path, so no unattended agent can read the site regardless of robots.txt. The listing inventory is a marketing asset routed to portals under commercial agreements, not a developer surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-26'
name: McGrath
nav: Providers
network: true
overview: 'McGrath is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Australia, Property Listings, Brokerage, and Residential Real Estate.


  McGrath''s developer surface includes engineering blog and 18 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.1
  delta: -6.8
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 13.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
security:
- kind: domain-security
  name: Mcgrath Domain Security
  slug: mcgrath-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mcgrath
tags:
- Real Estate
- Australia
- Property Listings
- Brokerage
- Residential Real Estate
- Property Management
- Rentals
- Mortgage
website: https://www.mcgrath.com.au/
---

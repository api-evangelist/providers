---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.games24x7.com/
- group: operate
  title: ''
  type: Support
  url: https://www.games24x7.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.games24x7.com/resources
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.games24x7.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.games24x7.com/terms-and-conditions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/games24x7-opensource
- group: auth
  title: ''
  type: Compliance
  url: https://cdn.prod.website-files.com/651cf07e5bb9107daafa9310/67c94cbbfe72bfd56632e216_ISO27001-Play%20Games24x7.pdf
- group: build
  title: ''
  type: Packages
  url: packages/games24x7-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/games24x7-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/games24x7-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/games24x7-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/games24x7-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/games24x7-rate-limits.yml
coverage:
  checked: '2026-08-16'
  detail: Games24x7 is a business-to-consumer skill-gaming operator whose entire product surface is the RummyCircle, My11Circle and Wowzy apps; its published sitemap has no developer, API or pricing page, /developers and /api both 404, and 30 contract-discovery probes across games24x7.com, rummycircle.com and my11circle.com returned 404 on every path.
  evidence:
  - status: 200
    url: https://www.games24x7.com/sitemap.xml
  - status: 404
    url: https://www.games24x7.com/developers
  - status: 404
    url: https://www.games24x7.com/api
  - status: 404
    url: https://www.games24x7.com/openapi.json
  - status: 404
    url: https://www.games24x7.com/.well-known/agent-card.json
  - status: 404
    url: https://www.rummycircle.com/.well-known/agent-card.json
  - status: 404
    url: https://www.my11circle.com/openapi.json
  - status: 404
    url: https://www.games24x7.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-16'
description: Games24x7 is a Mumbai-headquartered Indian online skill-gaming company founded in 2006 by Bhavin Pandya and Trivikraman Thampy, operating consumer real-money and casual gaming platforms rather than a developer API business. Its portfolio spans RummyCircle (online rummy), My11Circle (fantasy cricket, football, kabaddi and ludo) and Wowzy (a three-dice ludo variant), backed by Tiger Global, The Raine Group and Malabar Investment. The company publishes engineering writing on distributed systems, Cassandra, Amazon Aurora, ksqlDB and React Native through its Resources section, runs the TechXpedite accelerator, and maintains a small public GitHub organization (games24x7-opensource) plus one first-party npm package for AI-assisted Appium test automation. As of August 2026 it publishes no developer portal, no API documentation, no machine-readable specification, and no partner or affiliate API of its own.
image: https://cdn.prod.website-files.com/651cf07e5bb9107daafa9310/651cf8a23d4234857765a701_Webclip.png
layout: provider
modified: '2026-08-16'
name: Games24x7
nav: Providers
network: true
overview: 'Games24x7 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Online Gaming, Skill Gaming, and Fantasy Sports.


  Games24x7''s developer surface includes support, engineering blog, and 11 more developer resources.'
plans:
- name: Games24X7 Plans Pricing
  plan_count: 0
  slug: games24x7-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Games24X7 Rate Limits
  slug: games24x7-rate-limits
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 14.7
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Games24X7 Domain Security
  slug: games24x7-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: games24x7
tags:
- Company
- Gaming
- Online Gaming
- Skill Gaming
- Fantasy Sports
- Real Money Gaming
- Consumer Applications
- Entertainment
- Mobile Games
- India
website: https://www.games24x7.com/
---

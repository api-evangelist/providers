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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/merlin-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://merlinlabs.com/
- group: other
  title: ''
  type: Product
  url: https://merlinlabs.com/pilot/
- group: company
  title: ''
  type: About
  url: https://merlinlabs.com/company/
- group: company
  title: ''
  type: Blog
  url: https://merlinlabs.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://investors.merlinlabs.com/rss/news-releases.xml
- group: operate
  title: ''
  type: Support
  url: https://merlinlabs.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://merlinlabs.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://merlinlabs.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/merlinlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/merlinlabs/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/MerlinAero
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@merlin_labs
- group: company
  title: ''
  type: Careers
  url: https://merlinlabs.com/careers/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.merlinlabs.com/
- group: other
  title: ''
  type: SECFilings
  url: https://investors.merlinlabs.com/financial-information/sec-filings
- group: operate
  title: ''
  type: PressReleases
  url: https://investors.merlinlabs.com/news-events/news-releases
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/merlin-labs-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/merlin-labs-plans-pricing.yml
coverage:
  checked: '2026-08-25'
  detail: Merlin sells the Merlin Pilot as embedded flight-autonomy software inside aircraft programs (USSOCOM C-130J, USAF KC-135, Northrop Grumman, Honeywell, GE Aerospace, IAI) — merlinlabs.com is a six-page marketing site whose own sitemap lists only newsroom, company, careers and legal pages, and api./docs./developer.merlinlabs.com do not resolve in DNS at all.
  evidence:
  - status: 200
    url: https://merlinlabs.com/sitemap-0.xml
  - status: 404
    url: https://merlinlabs.com/openapi.json
  - status: 404
    url: https://merlinlabs.com/llms.txt
  - status: 404
    url: https://merlinlabs.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/merlinlabs
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'Merlin (Merlin Labs, Inc., NASDAQ: MRLN) is a Boston-headquartered aerospace and defense company founded in 2018 that builds takeoff-to-touchdown flight autonomy for legacy and next-generation aircraft. Its product is the Merlin Pilot, an aircraft-agnostic, AI-powered autonomy stack that pairs machine-learning mission planning with deterministic, hardcoded fallback flight systems, and that has flown hundreds of autonomous flights from test facilities in Kerikeri (New Zealand), Quonset Point (Rhode Island) and Bedford/Hanscom (Massachusetts). Merlin is a prime contractor to USSOCOM for C-130J autonomy, works with the U.S. Air Force on KC-135 tanker autonomy, and collaborates with Northrop Grumman, Honeywell, GE Aerospace and Israel Aerospace Industries. The company holds a New Zealand Part 146 aircraft design organization designation and reached Stage of Involvement 3 (SOI 3) with the Civil Aviation Authority of New Zealand in August 2026. Merlin became publicly traded in March
  2026 through a business combination with Inflection Point Acquisition Corp IV. Merlin sells embedded flight-autonomy software to aircraft OEMs, primes and government programs; it publishes no public developer program, API, SDK or machine-readable contract.'
image: https://merlinlabs.com/share.jpg
layout: provider
modified: '2026-08-25'
name: Merlin Labs
nav: Providers
network: true
overview: 'Merlin Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Aviation, Defense, and Autonomy.


  Merlin Labs'' developer surface includes engineering blog, support, YouTube channel, and 16 more developer resources.'
plans:
- name: Merlin Labs Plans Pricing
  plan_count: 0
  slug: merlin-labs-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 11.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Merlin Labs Domain Security
  slug: merlin-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: merlin-labs
tags:
- Company
- Aerospace
- Aviation
- Defense
- Autonomy
- Artificial Intelligence
- Flight Software
- Robotics
- Public Company
website: https://merlinlabs.com/
---

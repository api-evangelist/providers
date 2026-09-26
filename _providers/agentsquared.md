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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agentsquared/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/agentsquared
coverage:
  checked: '2026-09-12'
  detail: AgentSquared's domain agentsquared.com was re-registered in February 2026 and now serves an unrelated online-casino affiliate site (the WordPress discovery document at https://agentsquared.com/wp-json/ names the site "Online Casinos"), every page of the former real estate site returns 404, the customer login host dashboard.agentsquared.com no longer resolves, and STEP 0b contract discovery against both surviving hosts — /openapi.json, /swagger.json, /api-docs, /llms.txt, /apis.json and the full /.well-known/ set including agent-card.json and agent.json — returned only 403 Cloudflare interstitials and 404s, which is consistent with the company never having published a developer portal, API reference or machine-readable contract while it operated (it was a RESO Web API consumer, not a producer).
  evidence:
  - status: 403
    url: https://www.agentsquared.com/
  - status: 200
    url: https://agentsquared.com/wp-json/
  - status: 200
    url: https://agentsquared.com/page-sitemap.xml
  - status: 404
    url: https://www.agentsquared.com/pricing/
  - status: 404
    url: https://www.agentsquared.com/support/
  - status: 404
    url: https://www.agentsquared.com/how-it-works/
  - status: 404
    url: https://www.agentsquared.com/mls-partners/
  - status: 0
    url: https://dashboard.agentsquared.com/login/auth/login
  - status: 403
    url: https://www.agentsquared.com/openapi.json
  - status: 404
    url: https://www.agentsquared.com/llms.txt
  - status: 404
    url: https://www.agentsquared.com/.well-known/agent-card.json
  - status: 404
    url: https://www.agentsquared.com/.well-known/security.txt
  - status: 404
    url: https://registry.npmjs.org/agentsquared
  - status: 404
    url: https://pypi.org/pypi/agentsquared/json
  - status: 200
    url: https://www.linkedin.com/company/agentsquared/
  - status: 200
    url: https://equityzen.com/company/agentsquared
  reason: defunct
  state: none
created: '2026-09-12'
description: 'AgentSquared was a La Jolla, California real estate marketing technology company, founded in 2013 by Albert Lopez and a team its LinkedIn page describes as "Internet pioneers who have founded, built and sold leading brand name Internet companies such as Media Temple, Miva, and Attracta." Its product was marketing automation for real estate agents and brokers: Instant IDX websites provisioned with a single click, single-property websites generated automatically for new listings, social sharing of those listings, lead capture and CRM, and Google Business Profile and Local Services Ads management. The company was notable as an API CONSUMER rather than an API producer — it was a RESO (Real Estate Standards Organization) member and one of the few vendors building on the National Association of Realtors Web API standard, using deep integrations and channel partnerships with MLS software providers to pull a broker''s identity and listing data straight out of the MLS and stand up a
  fully populated website from it. It worked with RESO to help define and document the client portion of the RESO Web API certification program. AgentSquared never published a developer program of its own: no developer portal, API reference, OpenAPI or other machine-readable contract, SDK, or public package ever appeared on its site. The company reached roughly $961K in reported revenue without raising venture capital. Its web presence is now gone — see x-status below.'
layout: provider
modified: '2026-09-12'
name: AgentSquared
nav: Providers
network: true
overview: AgentSquared is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Real Estate Technology, Marketing Automation, and MLS.
random_paper: 8
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: agentsquared
tags:
- Company
- Real Estate
- Real Estate Technology
- Marketing Automation
- MLS
- IDX
- RESO
- Lead Generation
- Website Builder
- Defunct
---

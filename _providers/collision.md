---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/collision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vancouver.websummit.com/
- group: company
  title: ''
  type: Website
  url: https://collisionconf.com/
- group: other
  title: ''
  type: Parent
  url: https://websummit.com/
- group: company
  title: ''
  type: News
  url: https://vancouver.websummit.com/blog/news/web-summit-vancouver-collision-toronto/
- group: company
  title: ''
  type: Blog
  url: https://vancouver.websummit.com/blog/
- group: company
  title: ''
  type: Newsletter
  url: https://vancouver.websummit.com/newsletter/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vancouver.websummit.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://support-vancouver.websummit.com/hc/en-us
- group: other
  title: ''
  type: X
  url: https://x.com/collisionconf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/collision/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/collisionconf/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vancouver.websummit.com/terms-and-conditions/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/collision-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/collision-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/collision-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: collisionconf.com 301s its entire path space to vancouver.websummit.com, and the successor site's only /developers/ page is an application for a discounted attendee ticket — ten hosts were probed for a spec, a GraphQL endpoint, an MCP server, an agent card or any /.well-known/ document and every one returned 404 or a redirect.
  evidence:
  - status: 200
    url: https://vancouver.websummit.com/developers/
  - status: 404
    url: https://api.websummit.com/openapi.json
  - status: 404
    url: https://attend.websummit.com/openapi.json
  - status: 404
    url: https://vancouver.websummit.com/.well-known/api-catalog
  - status: 301
    url: https://collisionconf.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-03-24'
description: Collision was the major annual North American technology conference organized by Web Summit, held in Toronto from 2019 through 2024 and widely dubbed the "Olympics of Tech." Beginning in 2025, the event was relocated to the Vancouver Convention Centre and rebranded as Web Summit Vancouver, aligning with the global Web Summit family (Lisbon, Rio, Doha, Qatar). Web Summit Vancouver is contracted through at least 2027 and was held May 27-30, 2025; Web Summit Vancouver 2026 is scheduled for May 11-14, 2026. The Collision brand is retired but this profile is preserved for historical reference. Collision/Web Summit does not publish a public developer REST API; the conference operates speaker, partner, attendee, and press portals.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/collision.png
layout: provider
modified: '2026-09-05'
name: Collision (now Web Summit Vancouver)
nav: Providers
network: true
overview: 'Collision (now Web Summit Vancouver) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Conferences, Event, Historical, Rebrand, and Startups.


  Collision (now Web Summit Vancouver)''s developer surface includes product news, engineering blog, support, and 13 more developer resources.'
plans:
- name: Collision Plans Pricing
  plan_count: 0
  slug: collision-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Collision Rate Limits
  slug: collision-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/collision/refs/heads/main/screenshots/collision-2026-06-20T174751.png
security:
- kind: domain-security
  name: Collision Domain Security
  slug: collision-domain-security
  summary_line: TLSv1.3 · DMARC
slug: collision
tags:
- Conferences
- Event
- Historical
- Rebrand
- Startups
- Technology
- Web Summit
website: https://vancouver.websummit.com/
---

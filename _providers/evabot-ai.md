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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Gift API platform for businesses to automate and personalize employee gifting.
  name: Evabot Gift APIs
  slug: evabot-gift-apis
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/evabot-ai/hosts/evabot-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evabot-ai-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://evabot.net:443/press
- group: other
  title: ''
  type: Leadership
  url: https://www.evabot.ai/profile/team/Team7908
- group: auth
  href: https://artifacts.apis.io/evabot-ai/security/evabot-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evabot-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.evabot.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://evabot.net/
- group: company
  title: ''
  type: Blog
  url: https://evabot.net/blog.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evabot.net/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evabot.net/privacy-policy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://evabot.net/drafts/pricing-old.html
coverage:
  detail: Docs site renders via JavaScript, no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://docs.evabot.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Eva, operating under the brand Evabot, provides an AI‑driven employee gifting platform that helps businesses automate and personalize gift‑giving to strengthen customer relationships and boost ROI. The solution offers a catalog of curated gifts, AI recommendations, and analytics to track engagement, serving enterprises across various industries. Founded with backing from Bloomberg‑Beta, Eva leverages machine learning to streamline gifting workflows and enhance brand loyalty.
image: https://cdn.prod.website-files.com/61254805d17b9c1e42ff76d0/62d6d22013a3505b1f4fdf6e_Corporate%20gifting%20Solutions%20Social%20Preview%20-%201200x630px.png
layout: provider
modified: '2026-10-25'
name: Eva
nav: Providers
network: true
overview: 'Eva is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, EmployeeGifting, SaaS, and Platform.


  Eva''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 60.7
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Evabot Ai Domain Security
  slug: evabot-ai-domain-security
  summary_line: TLSv1.2 · DMARC
slug: evabot-ai
tags:
- Company
- AI
- EmployeeGifting
- SaaS
- Platform
website: https://www.evabot.ai/
---

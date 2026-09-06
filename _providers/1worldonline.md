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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The first-party HTTP backend behind the 1World Online publisher portal, widget frontend and loyalty applications. Its host is declared by 1World Online's own frontend configuration (URL_SERVER_API_NEW
  name: 1World Platform API
  slug: 1worldonline-platform
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://1worldonline.com/
- group: operate
  title: ''
  type: Support
  url: https://welcome.1worldonline.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://frontend-wleu.1worldonline.com/#!/become-partner
- group: commercial
  title: ''
  type: TermsOfService
  url: https://welcome.1worldonline.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://welcome.1worldonline.com/terms/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@1WorldOnline
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1worldonline-rnd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/1world-online/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/1World_Online/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCFFAw-lm7sOEHjjKnt3OCaQ
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/1world-online/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1worldonline-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/1worldonline-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1worldonline-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/1worldonline-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/1worldonline-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: 1World Online's platform backend is live at app-wleu.1worldonline.com and its own frontend configuration names it, but the only route to it is the publisher/advertiser partner registration SPA at frontend-wleu.1worldonline.com — the formerly public Swagger UI host api.1worldonline.com no longer resolves in DNS, and the live backend returns 404 for every conventional specification path.
  evidence:
  - status: 0
    url: https://api.1worldonline.com/
  - status: 404
    url: https://app-wleu.1worldonline.com/openapi.json
  - status: 404
    url: https://app-wleu.1worldonline.com/v3/api-docs
  - status: 404
    url: https://app-wleu.1worldonline.com/swagger-ui.html
  - status: 200
    url: https://portal-wleu.1worldonline.com/
  - status: 200
    url: https://app-wleu.1worldonline.com/actuator
  reason: partner-login
  state: gated
created: '2026-09-05'
description: 1World Online is an audience-engagement and interactive-advertising company, operating since 2012, that serves media publishers, advertisers and travel brands. Its platform embeds Interactive Media Units — polls, quizzes, trivia, debates and surveys — into publisher pages in 30+ languages, turns the resulting engagement into interactive ad inventory and first-party audience insight, and rewards participants through a points-based loyalty program and Web3 collectables (TravelVerse). The company also operates a technology center offering custom development and integration services. Its platform backend is live at app-wleu.1worldonline.com and serves the publisher portal, widget frontend and loyalty applications, but 1World Online publishes no public developer portal, API reference or machine-readable contract today, and the historic public Swagger UI host api.1worldonline.com no longer resolves.
image: https://1worldonline.com/images/logo.svg
layout: provider
modified: '2026-09-05'
name: 1World Online
nav: Providers
network: true
overview: '1World Online publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Audience Engagement, Polls, Surveys, and Quizzes.


  1World Online''s developer surface includes support, signup flow, engineering blog, YouTube channel, and 12 more developer resources.'
plans:
- name: 1Worldonline Plans Pricing
  plan_count: 0
  slug: 1worldonline-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: 1Worldonline Rate Limits
  slug: 1worldonline-rate-limits
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 1Worldonline Domain Security
  slug: 1worldonline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 1worldonline
tags:
- Advertising
- Audience Engagement
- Polls
- Surveys
- Quizzes
- Loyalty
- Media
- Publishing
- Widgets
- Web3
website: https://1worldonline.com/
---

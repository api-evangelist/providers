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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coachclub-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coachclub-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/coachclub-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://coachclub.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://coachclub.com/nos-abonnements-cours-de-sport/
- group: company
  title: ''
  type: Blog
  url: https://coachclub.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://coachclub.com/feed/
- group: operate
  title: ''
  type: FAQ
  url: https://coachclub.com/faq/
- group: operate
  title: ''
  type: Support
  url: https://coachclub.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coachclub.com/conditions-generales-de-vente-cgv/
- group: start
  title: ''
  type: Login
  url: https://mon.coachclub.com/login
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/coachclubbymoveyourfit
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/coachclubbymoveyourfit/
coverage:
  checked: '2026-08-17'
  detail: CoachClub ships a consumer fitness-video subscription and nothing else — the member application at mon.coachclub.com is a hosted Kajabi tenant (CNAME endpoint.mykajabi.com) that 404s every spec and .well-known path, and the only host named api.coachclub.com is a bare nginx catch-all on EC2 that answers 200 with a zero-byte body for every path, including a nonsense control path, so it serves no contract at all.
  evidence:
  - status: 404
    url: https://coachclub.com/openapi.json
  - status: 404
    url: https://coachclub.com/.well-known/agent-card.json
  - status: 404
    url: https://mon.coachclub.com/openapi.json
  - status: 200
    url: https://api.coachclub.com/zzz-nonsense-abc
  - status: 200
    url: https://coachclub.com/llms.txt
  - status: 503
    url: https://signup.coachclub.com/
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: 'CoachClub — branded "CoachClub by Move Your Fit" — is a French direct-to-consumer online sport and wellness coaching service founded in 2010 in France by Leslie Vartabedian and backed by Serena. Subscribers answer a questionnaire covering goals, physical ability, health and availability, and receive a tailored training and nutrition programme drawn from a library of more than 1,100 on-demand coaching videos spanning over 30 disciplines — fitness, musculation, yoga, danse, cardio boxe, pilates, stretching, bien-être and prénatal/postnatal — graded across three difficulty levels and paired with twelve weeks of healthy recipes, accessible 24/7 from computer, tablet, smartphone or television. The public marketing site runs on WordPress and the member application is a hosted Kajabi tenant at mon.coachclub.com. CoachClub sells an end-user subscription only: it publishes no public API, SDK, webhook catalog, developer portal or machine-readable specification.'
image: https://coachclub.com/wp-content/uploads/2025/02/logo-coachclub-2025.webp
layout: provider
modified: '2026-08-17'
name: CoachClub
nav: Providers
network: true
overview: 'CoachClub is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Fitness, Health and Wellness, and Online Coaching.


  CoachClub''s developer surface includes pricing, engineering blog, FAQ, support, and 9 more developer resources.'
plans:
- name: Coachclub Plans Pricing
  plan_count: 3
  slug: coachclub-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 5
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Coachclub Domain Security
  slug: coachclub-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coachclub
tags:
- Company
- Consumer
- Fitness
- Health and Wellness
- Online Coaching
- Video Streaming
- Subscription
- Nutrition
- France
website: https://coachclub.com/
---

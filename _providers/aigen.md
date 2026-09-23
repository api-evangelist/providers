---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
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
  score: 2.2
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.aigen.io/
- group: company
  title: ''
  type: About
  url: https://www.aigen.io/about
- group: company
  title: ''
  type: Blog
  url: https://www.aigen.io/news
- group: operate
  title: ''
  type: Support
  url: https://www.aigen.io/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aigen.io/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aigeninc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Aigenio
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@aigen-inc
- group: company
  title: ''
  type: Careers
  url: https://jobs.lever.co/aigen/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aigen/refs/heads/main/llms/aigen-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aigen-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aigen/refs/heads/main/well-known/aigen-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/aigen-robots.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aigen/refs/heads/main/security/aigen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aigen-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aigen/refs/heads/main/plans/aigen-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aigen-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aigen/refs/heads/main/packages/aigen-packages.yml
  title: ''
  type: Packages
  url: packages/aigen-packages.yml
coverage:
  checked: '2026-09-14'
  detail: 'Aigen sells a managed robotics-as-a-service engagement, not software access: the only two calls to action on the whole site are Fillout intake forms, https://www.aigen.io/pricing returns 404, every API/docs/developer/app/portal subdomain of aigen.io fails to resolve in DNS, and Aigen''s own llms.txt names a grower app and three email aliases but no developer surface of any kind.'
  evidence:
  - status: 200
    url: https://aigen.io/llms.txt
  - status: 200
    url: https://aigen.io/sitemap.xml
  - status: 404
    url: https://aigen.io/openapi.json
  - status: 404
    url: https://www.aigen.io/pricing
  - status: 404
    url: https://aigen.io/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: 'Aigen ("AI Generated Agriculture") is a Kirkland, Washington robotics company founded in 2020 that builds fully autonomous, solar-powered farm robots for daily, chemical-free weed control. Its flagship product, the Element, uses AI vision to identify and mechanically strike weeds — including herbicide-resistant weeds — with no herbicides, running on solar power with onboard battery storage and coordinating as a crew over a mesh network. In 2026 Aigen introduced Alchemy, a generative world model for outdoor physical AI that produces self-labeling synthetic training data. Aigen sells a managed robotics-as-a-service engagement rather than a self-serve developer product: growers are onboarded through a local Aigen agent and an intake form, and Aigen operates and maintains the fleet through the growing season. As of this profile Aigen publishes no public developer portal, API reference, or machine-readable API contract.'
image: https://aigen.io/assets/brand/landscape-logo-thumbnail.png
layout: provider
modified: '2026-09-14'
name: Aigen
nav: Providers
network: true
overview: 'Aigen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Agriculture, Agriculture Technology, and Artificial Intelligence.


  Aigen''s developer surface includes engineering blog, support, YouTube channel, and 11 more developer resources.'
plans:
- name: Aigen Plans Pricing
  plan_count: 0
  slug: aigen-plans-pricing
random_paper: 10
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 0.0
  previous_composite: 9.3
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aigen Domain Security
  slug: aigen-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aigen
tags:
- Company
- Robotics
- Agriculture
- Agriculture Technology
- Artificial Intelligence
- Autonomous Systems
- Machine Vision
- Sustainability
website: https://www.aigen.io/
---

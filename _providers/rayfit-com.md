---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/rayfit-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/rayfit-com/llms/rayfit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rayfit-com-llms.txt
- group: other
  href: https://artifacts.apis.io/rayfit-com/hosts/rayfit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rayfit-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/rayfit-com/vendors/rayfit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rayfit-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rayfit.com/terms-service/
- group: operate
  title: ''
  type: Support
  url: https://www.rayfit.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rayfit.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/rayfit-com/security/rayfit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rayfit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rayfit.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rayfit.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.rayfit.com/blog/
coverage:
  checked: '2026-10-29'
  detail: No API documentation, developer portal, or machine‑readable contract was found on rayfit.com or its subdomains.
  evidence:
  - status: 404
    url: https://www.rayfit.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Ray is an AI-powered personal fitness trainer that listens to users, learns from their workouts, and adapts coaching in real time. It offers voice‑guided exercise sessions, automatic rep counting, personalized workout plans, and progress tracking. Users can start with a free first week and upgrade for advanced features. The platform integrates with wearable devices and provides nutrition guidance, aiming to make fitness accessible and engaging for everyone.
image: https://d1cuqi4e8ky1tg.cloudfront.net/ray_og_image.png
layout: provider
modified: '2026-10-29'
name: Ray
nav: Providers
network: true
overview: 'Ray is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Fitness, Health, Personal Trainer, and Wellness.


  Ray''s developer surface includes support, pricing, engineering blog, and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Rayfit Com Domain Security
  slug: rayfit-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: rayfit-com
tags:
- AI
- Fitness
- Health
- Personal Trainer
- Wellness
- Company
website: https://rayfit.com
---

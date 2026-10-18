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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/celestialai/refs/heads/main/plans/celestialai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/celestialai-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/celestialai/refs/heads/main/hosts/celestialai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/celestialai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/celestialai/refs/heads/main/vendors/celestialai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/celestialai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://celestiai.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://celestiai.co/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://celestiai.co/pricing
- group: start
  title: ''
  type: Login
  url: https://celestiai.co/login
- group: company
  title: ''
  type: Blog
  url: https://celestiai.co/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/celestialai/refs/heads/main/security/celestialai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celestialai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://celestiai.co
coverage:
  checked: '2026-10-07'
  detail: No machine‑readable API specification was found on the provider’s site or API host.
  evidence:
  - status: 200
    url: https://celestiai.co
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Celestialai provides AI-driven short-form video creation tools, enabling rapid generation of marketing content with automated scripting, voiceovers, and editing in multiple languages. The platform offers a web interface for users to input product details or media, then leverages AI to produce tailored video ads. Acquired by Marvell, Celestialai integrates into broader AI accelerator offerings, targeting enterprises seeking scalable content generation solutions.
image: https://k1r3ok.celestiai.co/api/files/5pqsx3ttp47j2h1/6tw81ej58q7awxx/celestiai_aZRAcLOae8.jpg
layout: provider
modified: '2026-10-07'
name: Celestialai
nav: Providers
network: true
overview: 'Celestialai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI content, Short-Form Video, Content Calendar, and Voice Cloning.


  Celestialai''s developer surface includes pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Celestialai Plans Pricing
  plan_count: 6
  slug: celestialai-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 13.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Celestialai Domain Security
  slug: celestialai-domain-security
  summary_line: TLSv1.3
slug: celestialai
tags:
- AI content
- Short-Form Video
- Content Calendar
- Voice Cloning
website: https://celestiai.co
---

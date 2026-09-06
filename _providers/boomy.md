---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boomy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boomy.com/
- group: start
  title: ''
  type: Signup
  url: https://boomy.com/sign-up
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.boomy.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boomy.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boomy.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://help.boomy.com/
- group: other
  title: ''
  type: Notes
  url: ''
created: '2026-05-23'
description: Boomy is a consumer-facing generative music platform that lets anyone create original AI songs in a browser or mobile app and release them to Spotify, Apple Music, Amazon Music, TikTok, YouTube, and other DSPs with Boomy collecting and paying out streaming royalties. Boomy does not publish a public, self-serve developer API; integrations and partner arrangements (DSP distribution, licensing) are handled directly by the Boomy team rather than through a documented public API surface.
finops:
- name: Boomy Finops
  service_category: API
  slug: boomy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boomy.png
layout: provider
modified: '2026-07-25'
name: Boomy
nav: Providers
network: true
overview: 'Boomy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Music, Generative, Consumer, Streaming Distribution, and Royalties.


  Boomy''s developer surface includes signup flow and 6 more developer resources.'
plans:
- name: Boomy Plans Pricing
  plan_count: 1
  slug: boomy-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Boomy Rate Limits
  slug: boomy-rate-limits
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boomy/refs/heads/main/screenshots/boomy-2026-06-20T173609.png
security:
- kind: domain-security
  name: Boomy Domain Security
  slug: boomy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: boomy
tags:
- AI Music
- Generative
- Consumer
- Streaming Distribution
- Royalties
- Web App
- Mobile App
website: https://boomy.com/
---

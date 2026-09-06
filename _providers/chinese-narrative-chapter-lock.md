---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://culturebiz-xianxia-lock.onrender.com
  baseurl_source: declared
  description: REST API for locking chapter-scoped terminology in Chinese webnovel localization. Core endpoint POST /v1/lock returns locked terms, title entities, a character bible, and a glossary CSV. Documented by
  name: cultureBiz chapter-lock
  slug: culturebiz-chapter-lock
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://culturebiz-xianxia-lock.onrender.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chinese-narrative-chapter-lock-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chinese-narrative-chapter-lock-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/chinese-narrative-chapter-lock-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chinese-narrative-chapter-lock-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://rapidapi.com/zhongzhir/api/chinese-narrative-chapter-lock/pricing
created: '2026-09-05'
description: A chapter-scoped terminology-locking REST API for CN→EN webnovel (xianxia/cultivation) localization. It locks genre conventions, honorifics, ranks, sect and character names from pasted buyer text and exports a two-column glossary CSV for downstream MT/CAT tools like DeepL or Crowdin. It is not a full novel MT engine and does not host novels; consistency is per-paste.
image: https://rapidapi-prod-apis.s3.amazonaws.com/4faa5ef5-939d-444c-bfc8-8d868e9bd6de.png
layout: provider
modified: '2026-09-05'
name: Chinese Narrative Chapter Lock
nav: Providers
network: true
overview: 'Chinese Narrative Chapter Lock publishes 1 API on the [APIs.io](https://apis.io/) network: cultureBiz chapter-lock. Tagged areas include localization, translation, NLP, terminology-management, and CAT.


  Chinese Narrative Chapter Lock''s developer surface includes pricing and 5 more developer resources.'
plans:
- name: Chinese Narrative Chapter Lock Plans Pricing
  plan_count: 2
  slug: chinese-narrative-chapter-lock-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Chinese Narrative Chapter Lock Rate Limits
  slug: chinese-narrative-chapter-lock-rate-limits
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 42.0
    catalog_earned_first_party: 8.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 34.7
    developer_ergonomics: 18.5
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: Chinese Narrative Chapter Lock Authentication
  slug: chinese-narrative-chapter-lock-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Chinese Narrative Chapter Lock Domain Security
  slug: chinese-narrative-chapter-lock-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chinese-narrative-chapter-lock
tags:
- localization
- translation
- NLP
- terminology-management
- CAT
- MT-preprocessing
- chinese-language
- webnovels
- publishing
- entertainment
website: https://culturebiz-xianxia-lock.onrender.com
---

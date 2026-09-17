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
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://culturebiz-xianxia-lock.onrender.com
  baseurl_source: declared
  description: The CultureBiz Chapter Lock API from Chinese Narrative Chapter Lock — 1 operation(s) for culturebiz chapter lock.
  name: Chinese Narrative Chapter Lock CultureBiz Chapter Lock API
  slug: chinese-narrative-chapter-lock-culturebiz-chapter-lock-api
- baseURL: https://culturebiz-xianxia-lock.onrender.com
  baseurl_source: declared
  description: The Docs API from Chinese Narrative Chapter Lock — 1 operation(s) for docs.
  name: Chinese Narrative Chapter Lock Docs API
  slug: chinese-narrative-chapter-lock-docs-api
- baseURL: https://culturebiz-xianxia-lock.onrender.com
  baseurl_source: declared
  description: The Examples API from Chinese Narrative Chapter Lock — 1 operation(s) for examples.
  name: Chinese Narrative Chapter Lock Examples API
  slug: chinese-narrative-chapter-lock-examples-api
- baseURL: https://culturebiz-xianxia-lock.onrender.com
  baseurl_source: declared
  description: The Go API from Chinese Narrative Chapter Lock — 1 operation(s) for go.
  name: Chinese Narrative Chapter Lock Go API
  slug: chinese-narrative-chapter-lock-go-api
- baseURL: https://culturebiz-xianxia-lock.onrender.com
  baseurl_source: declared
  description: The Health API from Chinese Narrative Chapter Lock — 1 operation(s) for health.
  name: Chinese Narrative Chapter Lock Health API
  slug: chinese-narrative-chapter-lock-health-api
- baseURL: https://culturebiz-xianxia-lock.onrender.com
  baseurl_source: declared
  description: The Lock API from Chinese Narrative Chapter Lock — 1 operation(s) for lock.
  name: Chinese Narrative Chapter Lock Lock API
  slug: chinese-narrative-chapter-lock-lock-api
- baseURL: https://culturebiz-xianxia-lock.onrender.com
  baseurl_source: declared
  description: The Metrics API from Chinese Narrative Chapter Lock — 1 operation(s) for metrics.
  name: Chinese Narrative Chapter Lock Metrics API
  slug: chinese-narrative-chapter-lock-metrics-api
- baseURL: https://culturebiz-xianxia-lock.onrender.com
  baseurl_source: declared
  description: The Use API from Chinese Narrative Chapter Lock — 2 operation(s) for use.
  name: Chinese Narrative Chapter Lock Use API
  slug: chinese-narrative-chapter-lock-use-api
artifact_total: 12
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chinese-narrative-chapter-lock/refs/heads/main/overlays/chinese-narrative-chapter-lock-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/chinese-narrative-chapter-lock-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chinese-narrative-chapter-lock/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://culturebiz-xianxia-lock.onrender.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chinese-narrative-chapter-lock/refs/heads/main/security/chinese-narrative-chapter-lock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chinese-narrative-chapter-lock-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/chinese-narrative-chapter-lock/refs/heads/main/llms/chinese-narrative-chapter-lock-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chinese-narrative-chapter-lock-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/chinese-narrative-chapter-lock/refs/heads/main/plans/chinese-narrative-chapter-lock-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chinese-narrative-chapter-lock-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/chinese-narrative-chapter-lock/refs/heads/main/rate-limits/chinese-narrative-chapter-lock-rate-limits.yml
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
overview: 'Chinese Narrative Chapter Lock publishes 8 APIs on the [APIs.io](https://apis.io/) network, including CultureBiz Chapter Lock API, Docs API, Examples API, and 5 more. Tagged areas include Localization, Translation, NLP, terminology-management, and Cats.


  Chinese Narrative Chapter Lock''s developer surface includes pricing and 7 more developer resources.'
plans:
- name: Chinese Narrative Chapter Lock Plans Pricing
  plan_count: 2
  slug: chinese-narrative-chapter-lock-plans-pricing
random_paper: 18
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
  delta: 0.7
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 37.8
    developer_ergonomics: 18.5
    discoverability: 70.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 25.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Localization
- Translation
- NLP
- terminology-management
- Cats
- MT-preprocessing
- chinese-language
- Web Novels
- Publishing
- Entertainment
website: https://culturebiz-xianxia-lock.onrender.com
---

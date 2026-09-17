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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.5
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://video-cn.fly4k.com/api
  baseurl_source: declared
  description: The auth-controller API from 4K Garden — 9 operation(s) for auth-controller.
  name: 4K Garden Auth Controller API
  slug: 4k-garden-auth-controller-api
- baseURL: https://video-cn.fly4k.com/api
  baseurl_source: declared
  description: The customer-controller API from 4K Garden — 22 operation(s) for customer-controller.
  name: 4K Garden Customer Controller API
  slug: 4k-garden-customer-controller-api
- baseURL: https://video-cn.fly4k.com/api
  baseurl_source: declared
  description: The enterprise-controller API from 4K Garden — 9 operation(s) for enterprise-controller.
  name: 4K Garden Enterprise Controller API
  slug: 4k-garden-enterprise-controller-api
- baseURL: https://video-cn.fly4k.com/api
  baseurl_source: declared
  description: The frontend-controller API from 4K Garden — 10 operation(s) for frontend-controller.
  name: 4K Garden Frontend Controller API
  slug: 4k-garden-frontend-controller-api
- baseURL: https://video-cn.fly4k.com/api
  baseurl_source: declared
  description: The tvc-controller API from 4K Garden — 8 operation(s) for tvc-controller.
  name: 4K Garden Tvc Controller API
  slug: 4k-garden-tvc-controller-api
artifact_total: 9
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/4k-garden/refs/heads/main/overlays/4k-garden-diebian-ai-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/4k-garden-diebian-ai-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/4k-garden/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.4kgarden.com/
- group: company
  title: ''
  type: About
  url: https://www.4kgarden.com/skabout.html
- group: company
  title: ''
  type: Blog
  url: https://www.4kgarden.com/sknews.html
- group: company
  title: ''
  type: Careers
  url: https://www.4kgarden.com/skjoin.html
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/4k-garden/refs/heads/main/packages/4k-garden-packages.yml
  title: ''
  type: Packages
  url: packages/4k-garden-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/4k-garden/refs/heads/main/llms/4k-garden-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/4k-garden-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/4k-garden/refs/heads/main/security/4k-garden-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/4k-garden-domain-security.yml
created: '2026-09-05'
description: 4K Garden (4K花园), legally Sikai Garden Network Technology (Guangzhou) Co., Ltd. (四开花园网络科技（广州）有限公司), is a Chinese ultra-high-definition video technology company founded in 2016 and headquartered in Guangzhou, Guangdong, with roughly 200 staff across Guangzhou and Beijing. It produces, aggregates and distributes 4K and 8K content, was among the first in China to run end-to-end UHD HDR live production over the public internet and 5G, operates large outdoor naked-eye 3D LED landmarks, builds 8K 3D VR capture systems and domestically-sourced UHD broadcast trucks, and sells 5G video ringtone services with the three national carriers. Its AI product, Diebian AI (蝶变 AI), is a credit-metered video super-resolution platform at fly4k.com, and is the only part of the business with a machine-readable API contract.
image: http://m.4kgarden.com/images/logo.png
layout: provider
modified: '2026-09-05'
name: 4K Garden
nav: Providers
network: true
overview: '4K Garden publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth Controller API, Customer Controller API, Enterprise Controller API, and 2 more. Tagged areas include Company, Video, Ultra High Definition, Media and Entertainment, and Content Distribution.


  4K Garden''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: 4K Garden Plans Pricing
  plan_count: 4
  slug: 4k-garden-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: 4K Garden Rate Limits
  slug: 4k-garden-rate-limits
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 42.9
    developer_ergonomics: 14.9
    discoverability: 68.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 26.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
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
  name: 4K Garden Authentication
  slug: 4k-garden-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 4K Garden Domain Security
  slug: 4k-garden-domain-security
  summary_line: TLSv1.2 · DMARC
slug: 4k-garden
tags:
- Company
- Video
- Ultra High Definition
- Media and Entertainment
- Content Distribution
- Live Streaming
- Artificial Intelligence
- Video Super Resolution
- Virtual Reality
- China
website: https://www.4kgarden.com/
---

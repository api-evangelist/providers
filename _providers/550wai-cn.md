---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 18.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public Open API for subtitle removal, watermark removal, image compression, async tasks and webhooks.
  name: 550W AI Open API
  slug: 550w-ai-open-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/550wai-cn/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/550wai-cn/conventions/550wai-cn-conventions.yml
  title: ''
  type: Conventions
  url: conventions/550wai-cn-conventions.yml
- group: auth
  href: https://artifacts.apis.io/550wai-cn/authentication/550wai-cn-authentication.yml
  title: ''
  type: Authentication
  url: authentication/550wai-cn-authentication.yml
- group: agent
  href: https://artifacts.apis.io/550wai-cn/llms/550wai-cn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/550wai-cn-llms.txt
- group: agent
  href: https://artifacts.apis.io/550wai-cn/well-known/550wai-cn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/550wai-cn-well-known.yml
- group: other
  href: https://artifacts.apis.io/550wai-cn/hosts/550wai-cn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/550wai-cn-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://qzm.550wai.cn/team
- group: auth
  href: https://artifacts.apis.io/550wai-cn/security/550wai-cn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/550wai-cn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://550wai.cn/
- group: docs
  title: ''
  type: Documentation
  url: https://qzm.550wai.cn/api-open/
- group: docs
  title: ''
  type: APIReference
  url: https://qzm.550wai.cn/api-open/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.550wai.cn/qsy.html
- group: company
  title: ''
  type: Blog
  url: https://www.550wai.cn/blog/
coverage:
  checked: '2026-10-30'
  detail: All attempted OpenAPI spec URLs on the API host returned 404, and no documentation provides a machine‑readable contract.
  evidence:
  - status: 404
    url: https://api.550wai.cn/openapi.json
  - status: 404
    url: https://api.550wai.cn/openapi.yaml
  - status: 404
    url: https://api.550wai.cn/swagger.json
  - status: 404
    url: https://api.550wai.cn/v1/openapi.json
  - status: 404
    url: https://api.550wai.cn/api-docs
  - status: 404
    url: https://api.550wai.cn/docs
  - status: 404
    url: https://api.550wai.cn/redoc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: 550W AI (550W AI实验室) provides AI‑powered tools for content creators to automatically remove subtitles from videos, erase watermarks from images and videos, compress images, and more. The platform offers a public Open API that enables developers to integrate subtitle removal, watermark removal, image compression, asynchronous task polling, and webhook callbacks into their applications. Services are accessible via web, WeChat mini‑program, and desktop clients for macOS and Windows, supporting both single‑image and batch processing with before‑after comparison and automated workflows.
image: https://www.550wai.cn/static2/og_cover.jpg
layout: provider
modified: '2026-10-29'
name: 550wai-cn
nav: Providers
network: true
overview: '550wai-cn is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, VideoProcessing, ImageProcessing, WatermarkRemoval, and SubtitleRemoval.


  550wai-cn''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, and 8 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 49.3
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 550Wai Cn Authentication
  slug: 550wai-cn-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: 550Wai Cn Domain Security
  slug: 550wai-cn-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: 550wai-cn
tags:
- AI
- VideoProcessing
- ImageProcessing
- WatermarkRemoval
- SubtitleRemoval
website: https://550wai.cn/
---

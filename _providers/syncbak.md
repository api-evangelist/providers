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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syncbak-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zeammedia.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zeam.com/about/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zeam.com/about/privacypolicy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zeammedia/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/syncbak-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/syncbak-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/syncbak-rate-limits.yml
coverage:
  checked: '2026-08-29'
  detail: Syncbak rebranded to Zeam Media in May 2024 and every syncbak.com path now 301s to zeammedia.com, whose entire navigation is About, Careers, News & Press and a Contact modal — there is no developer section, no API reference, no GitHub organization, and api./developer./ docs. subdomains on syncbak.com, zeammedia.com and zeam.com do not resolve in DNS at all.
  evidence:
  - status: 301
    url: https://www.syncbak.com/
  - status: 200
    url: https://zeammedia.com/
  - status: 500
    url: https://zeammedia.com/openapi.json
  - status: 404
    url: https://zeam.com/openapi.json
  - status: 404
    url: https://zeam.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/syncbak
  reason: no-developer-program
  state: none
created: '2026-08-29'
description: Syncbak is a Marion, Iowa media-technology company founded in 2009 by Jack Perry that built the streaming infrastructure local U.S. television broadcasters use to put their over-the-air signals online. Its SimpleSync / MediaMogul platform handles live-stream transcoding, cloud-based rights resolution and geo-location authentication, cloud DVR, device filtering, content management, stream monitoring, clipping, and dynamic ad insertion through its AdSync product, delivering station feeds to OTT destinations including Paramount+, Hulu, fuboTV, Amazon, Roku, Apple TV and the NFL across 200+ U.S. markets. The company rebranded to Zeam Media in May 2024 to match its Zeam consumer hyperlocal streaming app, and syncbak.com now redirects to zeammedia.com. Syncbak publishes no public developer program, API reference, or machine-readable contract; its platform is delivered to broadcasters and station groups under commercial agreement.
image: https://cdn.sanity.io/images/r7pd5g2i/production/5ce955d9ba99cc7e0dc069ca791c04e139bfe595-1200x630.jpg
layout: provider
modified: '2026-08-29'
name: Syncbak
nav: Providers
network: true
overview: Syncbak is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Broadcasting, Streaming, Video, and Media.
plans:
- name: Syncbak Plans Pricing
  plan_count: 0
  slug: syncbak-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Syncbak Rate Limits
  slug: syncbak-rate-limits
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Syncbak Domain Security
  slug: syncbak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: syncbak
tags:
- Company
- Broadcasting
- Streaming
- Video
- Media
- OTT
- Television
- Advertising
- Local News
website: https://zeammedia.com/
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
  score: 20.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://open.yuanqisenlin.com/
  baseurl_source: declared
  description: Partner-facing API gateway at open.yuanqisenlin.com serving a Swagger 2.0 document titled "经销商&账款管理" (Distributor & Receivables Management, service name "arthur-merchant"). The document is publicly re
  name: Genki Forest Open Platform — Distributor & Receivables Management
  slug: genki-forest-open-platform-distributor-receivables-management
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.yuanqisenlin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.yuanqisenlin.com/doc.html
- group: docs
  title: ''
  type: APIReference
  url: https://open.yuanqisenlin.com/v2/api-docs
- group: operate
  title: ''
  type: Support
  url: https://www.yuanqisenlin.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.yuanqisenlin.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chiforest
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/genki-forest-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/genki-forest-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/genki-forest-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/genki-forest-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/genki-forest-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/genki-forest-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/genki-forest-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/genki-forest-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genki-forest-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/genki-forest-open-platform-overlay.yaml
created: '2026-08-21'
description: Genki Forest (元气森林), which trades internationally as Chi Forest, is a Chinese beverage company founded in Beijing in 2016 by Tang Binsen. It makes sugar-free sparkling water, brewed and iced teas, milk tea, and electrolyte and vitamin drinks under the 元气森林, 外星人 (Alienergy), 好自在 and Chi Forest brands, produced in its own plants in Chuzhou, Tianjin, Zhaoqing, Dujiangyan, Xianning, Taicang and Jiangsu. Its products are distributed across more than 30 Chinese provinces, cities and autonomous regions and exported to more than 40 countries. It is not a software vendor and runs no public developer program; its only public machine-readable API surface is a partner-facing open platform at open.yuanqisenlin.com that serves a Swagger 2.0 document for a distributor and receivables management service, and a first-party llms.txt published for AI crawlers on its corporate site.
image: https://static1.squarespace.com/static/694a6a14c2f7be39f0b59e75/t/694a77dc8d4a240fdfd73472/1766488028229/CHIFOREST-Logo.png?format=1500w
layout: provider
modified: '2026-08-21'
name: Genki Forest
nav: Providers
network: true
overview: 'Genki Forest publishes 1 API on the [APIs.io](https://apis.io/) network: Open Platform — Distributor & Receivables Management. Tagged areas include Company, Beverages, Food and Beverage, Consumer Packaged Goods, and Manufacturing.


  Genki Forest''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 11 more developer resources.'
plans:
- name: Genki Forest Plans Pricing
  plan_count: 0
  slug: genki-forest-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Genki Forest Rate Limits
  slug: genki-forest-rate-limits
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 29.3
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 21.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genki-forest/refs/heads/main/screenshots/genki-forest-2026-09-02T145622.png
security:
- kind: authentication
  name: Genki Forest Authentication
  slug: genki-forest-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Genki Forest Domain Security
  slug: genki-forest-domain-security
  summary_line: TLSv1.2 · HSTS
slug: genki-forest
tags:
- Company
- Beverages
- Food and Beverage
- Consumer Packaged Goods
- Manufacturing
- Distribution
- Retail
- China
website: https://www.yuanqisenlin.com/
---

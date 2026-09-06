---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/treadwell-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://treadwelltx.com/
- group: company
  title: ''
  type: Blog
  url: https://treadwelltx.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://treadwelltx.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://treadwelltx.com/terms-of-use/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/treadwell-therapeutics-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/treadwell-therapeutics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/treadwell-therapeutics-rate-limits.yml
coverage:
  checked: '2026-08-30'
  detail: Treadwell Therapeutics is a privately held clinical-stage oncology drug developer whose entire web presence is an eight-page WordPress marketing site on Flywheel - the only machine-readable things it serves are an SEO-plugin llms.txt and the WordPress core wp-json CMS index, and every OpenAPI/Swagger/GraphQL/.well-known path returns the site's WordPress 404 template.
  evidence:
  - status: 404
    url: https://treadwelltx.com/openapi.json
  - status: 404
    url: https://treadwelltx.com/graphql
  - status: 404
    url: https://treadwelltx.com/.well-known/api-catalog
  - status: 404
    url: https://treadwelltx.com/.well-known/agent-card.json
  - status: 200
    url: https://treadwelltx.com/llms.txt
  - status: 200
    url: https://treadwelltx.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: Treadwell Therapeutics is a clinical-stage, multi-modality oncology company developing novel small-molecule therapeutics for highly aggressive cancers by targeting tumor-specific vulnerabilities such as aneuploidy and immunogenicity. Co-founded by Tak Wah Mak, PhD and Mark R. Bray, PhD, the company keeps drug discovery and clinical development under one roof and works out of Toronto (with a research footprint at the University Health Network), New York and Hong Kong. Its internally developed pipeline includes CFI-400945, an oral PLK4 inhibitor in Phase 1/2 studies across triple-negative breast cancer, prostate cancer and acute myeloid leukemia (FDA Fast Track designation); CFI-402257, a TTK inhibitor in Phase 1b/2; and CFI-402411, a first-in-class HPK1 inhibitor. Treadwell is a therapeutics developer, not a software vendor - it publishes no developer program, no public API, and no machine-readable API contract. Profiled by API Evangelist from its own public corporate site.
image: https://treadwelltx.com/wp-content/uploads/logo.png
layout: provider
modified: '2026-08-30'
name: Treadwell Therapeutics
nav: Providers
network: true
overview: 'Treadwell Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Life Sciences.


  Treadwell Therapeutics'' developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Treadwell Therapeutics Plans Pricing
  plan_count: 0
  slug: treadwell-therapeutics-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Treadwell Therapeutics Rate Limits
  slug: treadwell-therapeutics-rate-limits
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/treadwell-therapeutics/refs/heads/main/screenshots/treadwell-therapeutics-2026-09-02T164156.png
security:
- kind: domain-security
  name: Treadwell Therapeutics Domain Security
  slug: treadwell-therapeutics-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: treadwell-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Life Sciences
- Healthcare
- Clinical Trials
- Drug Discovery
website: https://treadwelltx.com/
---

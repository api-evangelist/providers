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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-17'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.aiclearing.com/
- group: company
  title: ''
  type: About
  url: https://www.aiclearing.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.aiclearing.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.aiclearing.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.aiclearing.com/contact
- group: other
  title: ''
  type: CaseStudies
  url: https://www.aiclearing.com/case-studies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aiclearing.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aiclearing.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AI-Clearing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ai-clearing/
- group: start
  title: ''
  type: Login
  url: https://core.aiclearing.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ai-clearing/refs/heads/main/conformance/ai-clearing-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ai-clearing-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-clearing/refs/heads/main/conformance/ai-clearing-conformance.yml
  title: ''
  type: Compliance
  url: conformance/ai-clearing-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-clearing/refs/heads/main/security/ai-clearing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-clearing-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ai-clearing/refs/heads/main/llms/ai-clearing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-clearing-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ai-clearing/refs/heads/main/plans/ai-clearing-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ai-clearing-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ai-clearing/refs/heads/main/rate-limits/ai-clearing-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ai-clearing-rate-limits.yml
coverage:
  checked: '2026-09-13'
  detail: 'AI Clearing sells CORE as an end-user SaaS web application and publishes nothing for developers: its 54-URL sitemap has no developer, API, integrations or pricing page, the CORE app host answers a Cloudflare bot challenge on every API-shaped path, and the one docs subdomain that resolves (docs.aiclearing.com) refuses public connections entirely.'
  evidence:
  - status: 200
    url: https://www.aiclearing.com/sitemap.xml
  - status: 404
    url: https://www.aiclearing.com/openapi.json
  - status: 403
    url: https://core.aiclearing.com/openapi.json
  - status: 0
    url: https://docs.aiclearing.com/
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: 'AI Clearing is an AI-native construction progress tracking and quality control company founded in 2020, headquartered in Austin, Texas with an R&D center in Warsaw, Poland. Its CORE platform ingests drone imagery, ground-level mobile capture, CAD/BIM models and project schedules (including Primavera P6) and returns automated progress, productivity and quality analytics through interactive dashboards, a 3D digital twin and an agentic assistant (Clara), serving contractors and asset owners across solar, pipelines, transmission, highways, railways and airports. As of this profiling round the company publishes no public developer program, API reference or machine-readable contract: the CORE application at core.aiclearing.com is a customer-only single-page app behind a Cloudflare bot challenge, and docs.aiclearing.com does not answer public requests.'
image: https://cdn.prod.website-files.com/679889f10197fecac457e3ac/6798dc4cfc0f75e2e6dc471c_Open%20graph%20Home.avif
layout: provider
modified: '2026-09-13'
name: AI Clearing
nav: Providers
network: true
overview: 'AI Clearing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Construction Technology, Artificial Intelligence, and Computer-Vision.


  AI Clearing''s developer surface includes engineering blog, support, and 15 more developer resources.'
plans:
- name: Ai Clearing Plans Pricing
  plan_count: 0
  slug: ai-clearing-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Ai Clearing Rate Limits
  slug: ai-clearing-rate-limits
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 32.4
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai Clearing Domain Security
  slug: ai-clearing-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ai-clearing
tags:
- Company
- Construction
- Construction Technology
- Artificial Intelligence
- Computer-Vision
- Drones
- Geospatial
- Digital Twin
- Progress Tracking
- Quality Control
- Renewable Energy
- Infrastructure
website: https://www.aiclearing.com/
---

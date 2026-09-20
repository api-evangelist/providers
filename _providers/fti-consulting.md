---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-19'
api_count: 1
apis:
- description: Placeholder entry — FTI Consulting publishes no public API. The scaffolded hosts developer.fticonsulting.com and api.fticonsulting.com do not resolve (DNS NXDOMAIN, probed 2026-09-17), so the former D
  name: FTI Consulting API
  slug: fti-consulting-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fti-consulting/refs/heads/main/security/fti-consulting-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fti-consulting-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fti-consulting
- group: company
  title: ''
  type: Website
  url: https://www.fticonsulting.com
- group: company
  title: ''
  type: Blog
  url: https://www.fticonsulting.com/insights
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fti-consulting/refs/heads/main/llms/fti-consulting-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fti-consulting-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fticonsulting.com/about/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fticonsulting.com/about/legal
coverage:
  checked: '2026-09-17'
  detail: 'FTI Consulting is a professional-services advisory firm with no developer program: the scaffolded developer.fticonsulting.com and api.fticonsulting.com hosts are DNS NXDOMAIN, www.fticonsulting.com and the Technology segment site www.ftitechnology.com 404 every spec and /.well-known/ path, the 5,382-URL sitemap and the firm''s own llms.txt list no API or developer page, and the fticonsulting GitHub org has zero public repositories.'
  evidence:
  - status: 0
    url: https://developer.fticonsulting.com/docs
  - status: 0
    url: https://api.fticonsulting.com/openapi.json
  - status: 404
    url: https://www.fticonsulting.com/openapi.json
  - status: 404
    url: https://www.fticonsulting.com/.well-known/api-catalog
  - status: 200
    url: https://www.fticonsulting.com/llms.txt
  - status: 404
    url: https://www.ftitechnology.com/developers
  reason: no-developer-program
  state: none
created: '2026-04-19'
description: 'FTI Consulting is a global business advisory firm (NYSE: FCN, Fortune 1000) working in corporate finance and restructuring, economic consulting, forensic and litigation consulting, strategic communications and technology (e-discovery and information governance). Engagements are bespoke professional services; the firm publishes no public developer program, API reference or machine-readable contract. The only agent-facing document it serves is an llms.txt site index on www.fticonsulting.com.'
finops:
- name: Fti Consulting Finops
  service_category: Professional Services
  slug: fti-consulting-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fti-consulting.png
layout: provider
modified: '2026-09-17'
name: FTI Consulting
nav: Providers
network: true
overview: 'FTI Consulting publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Consulting, Economics, Financial Advisory, Professional Services, and Restructuring.


  FTI Consulting''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Fti Consulting Plans Pricing
  plan_count: 1
  slug: fti-consulting-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Fti Consulting Rate Limits
  slug: fti-consulting-rate-limits
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.9
    operational_transparency: 5.3
  previous_composite: 15.6
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/fti-consulting/refs/heads/main/screenshots/fti-consulting-2026-06-20T181607.png
security:
- kind: domain-security
  name: Fti Consulting Domain Security
  slug: fti-consulting-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fti-consulting
tags:
- Consulting
- Economics
- Financial Advisory
- Professional Services
- Restructuring
- Forensic Accounting
website: https://www.fticonsulting.com
---

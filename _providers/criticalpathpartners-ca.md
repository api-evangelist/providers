---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/criticalpathpartners-ca/plans/criticalpathpartners-ca-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/criticalpathpartners-ca-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/criticalpathpartners-ca/hosts/criticalpathpartners-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/criticalpathpartners-ca-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://criticalpathpartners.ca/terms-of-service.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://criticalpathpartners.ca/privacy-policy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://criticalpathpartners.ca/pricing.html
- group: company
  title: ''
  type: Blog
  url: https://criticalpathpartners.ca/blog/
- group: auth
  href: https://artifacts.apis.io/criticalpathpartners-ca/security/criticalpathpartners-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/criticalpathpartners-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://criticalpathpartners.ca/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://criticalpathpartners.ca/
  reason: no-developer-program
  state: none
created: '2026-11-04'
description: Critical Path Partners (CPP) provides forensic schedule analysis and delay claim consulting services for Ontario construction projects. They offer expert forensic methodology, free claim checks, and detailed analysis of Primavera P6 schedules to defend or support delay claims. Their services include windows analysis, as-built collapse, concurrency assessment, and expert testimony preparation, ensuring admissibility in court and compliance with Daubert standards. CPP serves sectors such as nuclear, energy, municipal infrastructure, mining, and commercial projects, delivering thorough, AI‑assisted reports within days.
image: https://criticalpathpartners.ca/og-image.png
layout: provider
modified: '2026-11-04'
name: Critical Path Partners
nav: Providers
network: true
overview: 'Critical Path Partners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Consulting, Construction, ForensicAnalysis, ScheduleDelay, and Ontario.


  Critical Path Partners'' developer surface includes pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Criticalpathpartners Ca Plans Pricing
  plan_count: 3
  slug: criticalpathpartners-ca-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Criticalpathpartners Ca Domain Security
  slug: criticalpathpartners-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: criticalpathpartners-ca
tags:
- Consulting
- Construction
- ForensicAnalysis
- ScheduleDelay
- Ontario
website: https://criticalpathpartners.ca/
---

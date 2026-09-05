---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ansa-biotechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ansabio.com/
- group: company
  title: ''
  type: Blog
  url: https://ansabio.com/topic/blog/
- group: operate
  title: ''
  type: Support
  url: https://ansabio.com/customer-support/
- group: start
  title: ''
  type: Login
  url: https://portal.ansabio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ansabio.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ansabio.com/privacy-policy/
coverage:
  checked: '2026-08-06'
  detail: Ansa sells wet-lab DNA synthesis, not software — ordering runs through a Salesforce Experience Cloud customer portal (portal.ansabio.com) whose every path, real or not, returns the same login HTML, and the corporate site answers every probe including /robots.txt with a SiteGround sgcaptcha challenge; no API, spec, SDK, package or GitHub org exists on any host or registry.
  evidence:
  - status: 404
    url: https://ansabio.my.site.com/openapi.json
  - status: 404
    url: https://ansabio.my.site.com/.well-known/agent-card.json
  - status: 200
    url: https://portal.ansabio.com/openapi.json
  - status: 202
    url: https://ansabio.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/ansabio
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Ansa Biotechnologies is a synthetic DNA manufacturer headquartered in Emeryville, California, founded in 2017 as a UC Berkeley spinout. Its enzymatic DNA synthesis platform is built on TdT-dNTP conjugates — enzymatic reagents that add single bases to a growing DNA molecule — and is sold as a made-to-order laboratory service producing sequence-verified double-stranded DNA fragments up to 600 bp, clonal DNA up to 7.5 kb, and ultra-long clonal constructs up to 50 kb. Quotes and orders are placed through a Salesforce Experience Cloud customer portal at portal.ansabio.com. Ansa is a wet-lab manufacturer rather than a software company: it publishes no public API, developer portal, SDK, or machine-readable specification.'
layout: provider
modified: '2026-08-06'
name: Ansa Biotechnologies
nav: Providers
network: true
overview: 'Ansa Biotechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Synthetic Biology, DNA Synthesis, and Gene Synthesis.


  Ansa Biotechnologies'' developer surface includes engineering blog, support, and 5 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ansa-biotechnologies/refs/heads/main/screenshots/ansa-biotechnologies-2026-08-07T161422.png
security:
- kind: domain-security
  name: Ansa Biotechnologies Domain Security
  slug: ansa-biotechnologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ansa-biotechnologies
tags:
- Company
- Biotechnology
- Synthetic Biology
- DNA Synthesis
- Gene Synthesis
- Life Sciences
- Laboratory Services
website: https://ansabio.com/
---

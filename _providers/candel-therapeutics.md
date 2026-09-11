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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://candeltx.com/
- group: company
  title: ''
  type: About
  url: https://candeltx.com/about
- group: company
  title: ''
  type: Blog
  url: https://candeltx.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://candeltx.com/blog/rss.xml
- group: operate
  title: ''
  type: Support
  url: https://candeltx.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://candeltx.com/privacy-policy
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.candeltx.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/candel-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/candel-therapeutics-llms.txt
coverage:
  checked: '2026-09-09'
  detail: Candel Therapeutics is a clinical-stage biopharmaceutical developer whose only credentialed surface is a HubSpot-hosted clinical-trial investigator login; every contract-discovery path on candeltx.com returns a real 404 and the company publishes no developer portal, API reference or machine-readable specification.
  evidence:
  - status: 404
    url: https://candeltx.com/openapi.json
  - status: 404
    url: https://candeltx.com/.well-known/api-catalog
  - status: 200
    url: https://candeltx.com/sitemap.xml
  - status: 200
    url: https://candeltx.com/investigator-login
  reason: not-a-software-company
  state: none
created: '2026-09-09'
description: 'Candel Therapeutics, Inc. (Nasdaq: CADL) is a clinical-stage biopharmaceutical company headquartered in Needham, Massachusetts, developing off-the-shelf multimodal viral immunotherapies for solid tumors. Founded as Advantagene, the company advances two engineered viral platforms: aglatimagene besadenovec (CAN-2409), a replication-defective adenovirus delivered intratumorally alongside a prodrug to trigger immunogenic cell death, and linoserpaturev (CAN-3110), a replication-competent oncolytic herpes simplex virus. Its clinical programs span prostate cancer, non-small cell lung cancer, pancreatic cancer and recurrent high-grade glioma. Candel is a therapeutics developer, not a software vendor: it operates no developer program, publishes no public API, SDK or machine-readable specification, and its only credentialed surface is a clinical-trial investigator portal.'
image: https://candeltx.com/hubfs/logo-main-nav-1.svg
layout: provider
modified: '2026-09-09'
name: Candel Therapeutics
nav: Providers
network: true
overview: 'Candel Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Immunotherapy, and Oncology.


  Candel Therapeutics'' developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Candel Therapeutics Plans Pricing
  plan_count: 0
  slug: candel-therapeutics-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Candel Therapeutics Rate Limits
  slug: candel-therapeutics-rate-limits
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Candel Therapeutics Domain Security
  slug: candel-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: candel-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Immunotherapy
- Oncology
- Life Sciences
- Clinical Trials
- Healthcare
website: https://candeltx.com/
---

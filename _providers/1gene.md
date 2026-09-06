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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1gene-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: 1GENE sells non-invasive cancer early-screening lab tests to consumers and clinics and publishes no developer program in either Chinese- or English-language sources; its own www.1gene.com.cn now answers HTTP 200 with an unconfigured Nginx Proxy Manager "Default Site" placeholder and every /.well-known/ and spec path on it returns a real 404, with no api./open./developer./docs. subdomain resolving and no GitHub organization or published package anywhere.
  evidence:
  - status: 200
    url: http://www.1gene.com.cn/
  - status: 404
    url: http://www.1gene.com.cn/openapi.json
  - status: 404
    url: http://www.1gene.com.cn/.well-known/agent-card.json
  - status: 404
    url: http://www.1gene.com.cn/llms.txt
  - status: 404
    url: https://api.github.com/orgs/1gene
  - status: 404
    url: https://pypi.org/pypi/1gene/json
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '1GENE (壹基因) is the brand of Hangzhou He-Yi Gene Technology Co., Ltd., a Chinese molecular-diagnostics company founded in Hangzhou''s Binjiang district in May 2014 by chairman and chief executive Junyi Wang. It develops non-invasive early cancer screening tests built on proprietary tumour DNA methylation markers and liquid- and stool-based biopsy chemistry, sold under the mission of "letting everyone stay away from cancer earlier". Its product pipeline covers colorectal cancer screening (常壹宁), gastric pathogen screening and medication guidance (优壹宁), gastric cancer screening (卫壹宁), and liver and oesophageal cancer screening in development; company scientists co-authored a validated stool-DNA biomarker panel for colorectal neoplasms in the Journal of Cancer Research and Clinical Oncology. The company raised an angel round in 2014, a RMB 49.5M Series A in 2015 and a Series B of several tens of millions of RMB from listed pharmaceutical maker Chengda Pharmaceuticals in December
  2022, and its shares are listed for secondary-market trading on EquityZen. 1GENE sells a clinical test, not software: it publishes no developer program, no public API, no SDK and no machine-readable specification, and as of this profile its own web origin at www.1gene.com.cn is unconfigured and serves a placeholder page.'
layout: provider
modified: '2026-09-05'
name: 1GENE
nav: Providers
network: true
overview: 1GENE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Biotechnology, and Genomics.
random_paper: 2
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 1Gene Domain Security
  slug: 1gene-domain-security
  summary_line: no transport/DNS hardening detected
slug: 1gene
tags:
- Company
- Health
- Healthcare
- Biotechnology
- Genomics
- Diagnostics
- Cancer Screening
- Precision Medicine
- Life Sciences
- China
---

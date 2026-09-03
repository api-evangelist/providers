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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prognomiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://prognomiq.com/
- group: company
  title: ''
  type: Blog
  url: https://prognomiq.com/news-resources/
- group: operate
  title: ''
  type: Support
  url: https://prognomiq.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://prognomiq.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prognomiq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prognomiq-inc/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/PrognomiQ_Inc
- group: company
  title: ''
  type: Careers
  url: https://prognomiq.com/careers/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prognomiq-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/prognomiq-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/prognomiq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prognomiq-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: PrognomiQ sells a blood-based laboratory developed test (ProVue Lung) ordered through a healthcare provider, and its entire public web presence is a six-page WordPress marketing site with no developer section — every contract-discovery path probed on prognomiq.com returned 404 and no api./developer./portal./app. subdomain resolves in DNS.
  evidence:
  - status: 404
    url: https://prognomiq.com/openapi.json
  - status: 404
    url: https://prognomiq.com/.well-known/agent-card.json
  - status: 404
    url: https://prognomiq.com/llms.txt
  - status: 404
    url: https://prognomiq.com/developers
  - status: 200
    url: https://github.com/prognomiq
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'PrognomiQ Inc. is a Redwood City, California multi-omics diagnostics company, spun out of Seer (NASDAQ: SEER) in 2020, that combines proteomic, genomic, transcriptomic and metabolomic measurement with machine learning to detect cancer and other complex diseases earlier from a blood draw. Its first commercial product, ProVue Lung, is a proteomics-based laboratory developed test (LDT) intended to aid early detection of lung cancer. PrognomiQ is a clinical laboratory and life sciences business rather than a software vendor: as of this profile it publishes a six-page corporate marketing site, a public GitHub organization holding forks of open-source data-engineering tooling, and no public developer portal, API documentation or machine-readable API contract.'
image: https://prognomiq.com/wp-content/uploads/2021/01/Prognomiq_logo_2-pink-white@2x.png
layout: provider
modified: '2026-08-26'
name: PrognomiQ
nav: Providers
network: true
overview: 'PrognomiQ is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Life Sciences, Diagnostics, and Proteomics.


  PrognomiQ''s developer surface includes engineering blog, support, and 11 more developer resources.'
plans:
- name: Prognomiq Plans Pricing
  plan_count: 0
  slug: prognomiq-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Prognomiq Rate Limits
  slug: prognomiq-rate-limits
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prognomiq/refs/heads/main/screenshots/prognomiq-2026-09-02T152125.png
security:
- kind: domain-security
  name: Prognomiq Domain Security
  slug: prognomiq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: prognomiq
tags:
- Company
- Healthcare
- Life Sciences
- Diagnostics
- Proteomics
- Multiomics
- Oncology
- Clinical Laboratory
- Early Detection
- Liquid Biopsy
website: https://prognomiq.com/
---

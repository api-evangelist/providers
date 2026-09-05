---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.semmle.com'', ''status'': 301, ''note'': ''declared website redirects to https://github.blog/news-insights/company-news/github-welcomes-semmle/ — a different registrable domain (semmle.com -> github.blog), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/semmle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.semmle.com
created: '2026-07-17'
description: Semmle was a semantic code-analysis company whose engine let developers write queries (in its QL query language) to find security vulnerabilities and their variants across large codebases, and which powered the free open-source code review platform LGTM.com. Its technology was adopted by Uber, NASA, Microsoft, and Google. GitHub acquired Semmle in September 2019 and folded the QL engine into what is now CodeQL and GitHub code scanning; the standalone Semmle and LGTM.com products were retired and www.semmle.com now redirects to the GitHub acquisition announcement. This profile is retained as a historical (acquired) company lead in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/semmle.png
layout: provider
modified: '2026-07-21'
name: Semmle
nav: Providers
network: true
overview: Semmle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Code Analysis, Application Security, and Static Analysis.
random_paper: 13
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/semmle/refs/heads/main/screenshots/semmle-2026-09-02T154826.png
security:
- kind: domain-security
  name: Semmle Domain Security
  slug: semmle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: semmle
tags:
- Company
- Enterprise
- Code Analysis
- Application Security
- Static Analysis
- Developer Tools
- Acquired
website: http://www.semmle.com
---

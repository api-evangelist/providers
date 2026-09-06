---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://codesecure.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.adacore.com/codesecure — a different registrable domain (codesecure.com -> adacore.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codesecure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://codesecure.com
- group: start
  title: ''
  type: Portal
  url: https://www.adacore.com/codesecure
- group: docs
  title: ''
  type: Documentation
  url: https://www.adacore.com/documentation
- group: company
  title: ''
  type: Blog
  url: https://www.adacore.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.adacore.com/codesecure-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adacore
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codesecure-llms.txt
created: '2026-07-17'
description: CodeSecure is an application security testing company whose CodeSonar static application security testing (SAST) engine performs deep whole-program analysis of C, C++, Java, and other languages to find bugs, security vulnerabilities, and coding-standard violations, and whose CodeSentry binary software composition analysis (SCA) tool generates SBOMs and detects vulnerabilities in third-party and binary components. CodeSecure merged with AdaCore in 2025, combining SAST and SCA tooling with high-integrity software development for aerospace, automotive, defense, medical, and industrial customers. The tools support SARIF, CWE, MISRA, CERT, and OWASP as well as safety standards such as ISO 26262, IEC 61508, EN 50128, and DO-178C, and integrate with CI/CD, IDE, and issue-tracking pipelines rather than exposing a public developer REST API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codesecure.png
layout: provider
modified: '2026-07-18'
name: CodeSecure
nav: Providers
network: true
overview: 'CodeSecure is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Application Security, Static Analysis, SAST, and Software Composition Analysis.


  CodeSecure''s developer surface includes developer portal, documentation, engineering blog, support, and 4 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codesecure/refs/heads/main/screenshots/codesecure-2026-07-25T205925.png
security:
- kind: domain-security
  name: Codesecure Domain Security
  slug: codesecure-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: codesecure
tags:
- Company
- Application Security
- Static Analysis
- SAST
- Software Composition Analysis
- SBOM
- DevSecOps
- Code Quality
- Security
website: https://codesecure.com
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gilead-sciences/refs/heads/main/security/gilead-sciences-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gilead-sciences-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gilead-sciences
- group: company
  title: ''
  type: Website
  url: https://www.gilead.com
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gilead-sciences/refs/heads/main/packages/gilead-sciences-packages.yml
  title: ''
  type: Packages
  url: packages/gilead-sciences-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gilead-sciences/refs/heads/main/llms/gilead-sciences-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gilead-sciences-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Gilead-Public
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gilead.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gilead.com/privacy-statements
- group: operate
  title: ''
  type: Support
  url: https://www.gilead.com/contact-us
coverage:
  checked: '2026-09-12'
  detail: 'Gilead ships real first-party open-source software — 19 public repos under github.com/Gilead-Public, the Apache-2.0 "gsm" R suite for risk-based clinical trial monitoring — but no public API: the only host that resolves as an API surface, api.gilead.com, answers HTTP 200 with the same 321-byte "Resource not Found" page for every path including a random one that cannot exist, and developer.gilead.com / developers.gilead.com / apis.gilead.com do not resolve at all.'
  evidence:
  - status: 200
    url: https://api.gilead.com/openapi.json
  - status: 200
    url: https://api.gilead.com/.well-known/gilead-sciences-negative-control-7f3ab91c.json
  - status: 404
    url: https://www.gilead.com/.well-known/api-catalog
  - status: 404
    url: https://www.gilead.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: Gilead Sciences is a research-based biopharmaceutical company that discovers, develops, and commercializes innovative therapeutics in areas of unmet medical need including HIV, viral hepatitis, oncology, and inflammatory diseases.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gilead-sciences.png
layout: provider
modified: '2026-09-12'
name: Gilead Sciences
nav: Providers
network: true
overview: 'Gilead Sciences is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceuticals, Biotechnology, Healthcare, Life Sciences, and Clinical Trials.


  Gilead Sciences'' developer surface includes support and 8 more developer resources.'
press:
- date: ''
  title: Artificial Intelligence at Gilead Sciences - Two Use Cases
  url: https://emerj.com/artificial-intelligence-at-gilead-sciences-two-use-cases/
- date: ''
  title: Tempus Announces Strategic Collaboration with Gilead to ...
  url: https://investors.tempus.com/news-releases/news-release-details/tempus-announces-strategic-collaboration-gilead-advance-oncology
- date: ''
  title: AI Principles
  url: https://www.gilead.com/company/policies-and-procedures/ai-principles
- date: ''
  title: Cognizant and Gilead Extend Partnership with Five-Year ...
  url: https://www.prnewswire.com/news-releases/cognizant-and-gilead-extend-partnership-with-five-year-service-agreement-estimated-at-800-million-301883522.html
- date: ''
  title: Gilead and Genesis Therapeutics Announce Strategic ...
  url: https://www.gilead.com/news/news-details/2024/gilead-and-genesis-therapeutics-announce-strategic-collaboration-to-discover-and-develop-novel-therapies
random_paper: 8
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/gilead-sciences/refs/heads/main/screenshots/gilead-sciences-2026-06-20T181825.png
security:
- kind: domain-security
  name: Gilead Sciences Domain Security
  slug: gilead-sciences-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: gilead-sciences
tags:
- Pharmaceuticals
- Biotechnology
- Healthcare
- Life Sciences
- Clinical Trials
- Open Source
- Fortune 500
website: https://www.gilead.com
---

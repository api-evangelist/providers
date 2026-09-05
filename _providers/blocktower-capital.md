---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://blocktower.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.ar.ca/arca-acquires-blocktower — a different registrable domain (blocktower.com -> ar.ca), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/blocktower-capital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blocktower.com
created: '2026-07-17'
description: BlockTower Capital was an institutional digital-asset investment management firm founded in 2017, running crypto hedge fund and venture strategies and backed by investors including Andreessen Horowitz (a16z) and Union Square Ventures. As of April 30, 2025 the firm was acquired by and rebranded as Arca; blocktower.com now 301-redirects to ar.ca and BlockTower no longer operates as a standalone brand. The firm published no public API, developer portal, or SDK surface, so there is no API artifact set to enrich here beyond identity and a domain-security probe of the still-resolving legacy domain.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blocktower-capital.png
layout: provider
modified: '2026-07-18'
name: BlockTower Capital
nav: Providers
network: true
overview: BlockTower Capital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Digital Assets, Investment Management, and Blockchain.
random_paper: 15
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
screenshot: https://raw.githubusercontent.com/api-evangelist/blocktower-capital/refs/heads/main/screenshots/blocktower-capital-2026-07-25T203348.png
security:
- kind: domain-security
  name: Blocktower Capital Domain Security
  slug: blocktower-capital-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blocktower-capital
tags:
- Company
- Cryptocurrency
- Digital Assets
- Investment Management
- Blockchain
- Venture Capital
- Hedge Fund
- Acquired
website: https://blocktower.com
---

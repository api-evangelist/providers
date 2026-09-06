---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Deutsche Bank is a global financial institution that offers a wide range of banking and financial services to individuals, corporations, and institutional clients. The bank provides services such as i
  name: Deutsche Bank API Program
  slug: deutsche-bank
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deutsche-bank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deutsche-bank-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deutschebank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deutsche-bank
- group: docs
  title: ''
  type: Documentation
  url: https://developer.db.com/
- group: company
  title: ''
  type: Partners
  url: https://developer.db.com/partnernetwork
- group: company
  title: ''
  type: Website
  url: https://www.db.com/
created: '2025-02-08'
description: Deutsche Bank is a global financial institution that offers a wide range of banking services to individuals, businesses, and institutions. The bank provides services such as retail banking, investment banking, asset management, and wealth management. Deutsche Bank is known for its expertise in international markets and has a strong presence in Europe, the Americas, and Asia. The Deutsche Bank Developer Portal publishes Open Banking and Beyond-PSD2 APIs for partners and developers.
finops:
- name: Deutsche Bank Finops
  service_category: API
  slug: deutsche-bank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deutsche-bank.png
layout: provider
modified: '2026-04-28'
name: Deutsche Bank
nav: Providers
network: true
overview: 'Deutsche Bank publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Financial, Wealth Management, Open Banking, and PSD2.


  Deutsche Bank''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Deutsche Bank Plans Pricing
  plan_count: 3
  slug: deutsche-bank-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Deutsche Bank Rate Limits
  slug: deutsche-bank-rate-limits
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 10.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deutsche-bank/refs/heads/main/screenshots/deutsche-bank-2026-06-20T175943.png
security:
- kind: domain-security
  name: Deutsche Bank Domain Security
  slug: deutsche-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deutsche Bank Vulnerability Disclosure
  slug: deutsche-bank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deutsche-bank
tags:
- Banking
- Financial
- Wealth Management
- Open Banking
- PSD2
website: https://www.db.com/
---

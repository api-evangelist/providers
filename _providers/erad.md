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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/erad-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/erad-llms.txt
- group: company
  title: ''
  type: Website
  url: https://erad.co
- group: company
  title: ''
  type: Blog
  url: https://erad.co/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://erad.co/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://erad.co/en/privacy
created: '2026-07-17'
description: Erad is a licensed, Sharia-compliant fintech lender providing fast, flexible working capital to small and medium-sized businesses across Saudi Arabia and the United Arab Emirates. Founded in 2022 (Y Combinator S22) and headquartered in Riyadh, Erad offers revenue-based financing, invoice financing (advancing up to 90% of B2B/B2G invoices in as little as 48 hours), and supplier financing to revenue-generating SMEs. The company embeds working-capital products into supplier networks and business platforms, and is backed by investors including Y Combinator, 500 Global, Nuwa Capital, Khwarizmi Ventures, Aljazira Capital, VentureSouq, Oraseya Capital and Joa Capital, alongside debt facilities from Stride Ventures and a $125M asset-backed facility led by Jefferies with Channel Capital.
image: https://erad.co/favicon.png
layout: provider
modified: '2026-07-19'
name: Erad
nav: Providers
network: true
overview: 'Erad is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Financial-Services, Lending, and SME Financing.


  Erad''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/erad/refs/heads/main/screenshots/erad-2026-07-25T213556.png
security:
- kind: domain-security
  name: Erad Domain Security
  slug: erad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: erad
tags:
- Company
- Fintech
- Financial-Services
- Lending
- SME Financing
- Working Capital
- Invoice Financing
- Embedded Finance
- Revenue-Based Financing
- Saudi Arabia
- MENA
- Sharia-Compliant
website: https://erad.co
---

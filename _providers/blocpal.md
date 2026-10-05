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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.blocpal.com/security
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blocpal/refs/heads/main/hosts/blocpal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blocpal-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blocpal/refs/heads/main/vendors/blocpal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blocpal-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blocpal.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blocpal.com/privacy-policy-old
- group: company
  title: ''
  type: Newsroom
  url: https://www.blocpal.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blocpal/refs/heads/main/security/blocpal-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/blocpal-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blocpal/refs/heads/main/security/blocpal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blocpal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blocpal.com/
coverage:
  checked: '2026-09-29'
  detail: OpenAPI spec not found at standard endpoints (openapi.json, openapi.yaml) on api.blocpal.com.
  evidence:
  - status: 404
    url: https://api.blocpal.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-29'
description: BlocPal is a Canadian fintech building a next‑generation digital wealth and neo‑banking platform. It offers digital banking, digital wealth, tokenization, and API integration services, empowering individuals and businesses worldwide to access financial services easily and securely. Leveraging AI, cloud computing, and blockchain, BlocPal delivers both traditional (TradFi) and decentralized (DeFi) financial solutions through collaborative networks.
image: https://cdn.prod.website-files.com/683dc9f61e8ea0aa11eb3643/68768e5d8b712d567a97e1a7_og_logo.png
layout: provider
modified: '2026-09-29'
name: BlocPal
nav: Providers
network: true
overview: BlocPal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Digital Banking, Wealth Management, and Blockchain.
random_paper: 7
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.0
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blocpal Domain Security
  slug: blocpal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Blocpal Trust Center
  slug: blocpal-trust-center
  summary_line: SOC 2, PCI DSS
slug: blocpal
tags:
- Company
- Fintech
- Digital Banking
- Wealth Management
- Blockchain
website: https://www.blocpal.com/
---

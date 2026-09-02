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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/protego-trust-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.protegotrust.com/
coverage:
  checked: '2026-08-26'
  detail: Protego has no reachable web surface at all - protegotrust.com, www.protegotrust.com and protegotrust.co each terminate the TLS handshake with a fatal internal_error alert and present no certificate (Webflow proxy hosts with no provisioned certificate), plain HTTP 301s into that same dead origin, api/docs/developer subdomains do not resolve, and no developer portal, API reference or spec appears at any Protego URL in the public web archive going back to 2020.
  evidence:
  - status: 0
    url: https://www.protegotrust.com/
  - status: 0
    url: https://www.protegotrust.com/openapi.json
  - status: 0
    url: https://www.protegotrust.com/.well-known/agent-card.json
  - status: 0
    url: https://api.protegotrust.com/
  - status: 404
    url: https://pypi.org/pypi/protego-trust/json
  - status: 200
    url: https://api.github.com/orgs/protegotrust
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Protego Trust Bank is a Seattle, Washington digital-asset trust bank built for institutional clients, offering crypto-asset custody, trading, lending/borrowing and issuer services, with custody-related fiduciary services such as staking-as-a-service, protocol governance and voting, and fork and airdrop handling. Protego Trust Company received OCC conditional approval in February 2021 to convert into a national trust bank; that approval lapsed in February 2023 after pre-conversion requirements were not met. On 13 February 2026 the OCC granted parent Protego Holdings Corporation preliminary conditional approval (Corporate Decision #1366, control number 2025-Charter-342009) to charter National Digital Trust Company, Seattle. Protego''s marketing material has described API endpoints for trading and liquidity aggregation, but the company publishes no public developer portal, API reference or machine-readable contract, and as of this profile its own web properties do not complete
  a TLS handshake.'
layout: provider
modified: '2026-08-26'
name: Protego Trust Bank
nav: Providers
network: true
overview: Protego Trust Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Financial-Services, Digital Assets, and Cryptocurrency.
plans:
- name: Protego Trust Bank Plans Pricing
  plan_count: 0
  slug: protego-trust-bank-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Protego Trust Bank Rate Limits
  slug: protego-trust-bank-rate-limits
score:
  band: minimal
  composite: 1.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Protego Trust Bank Domain Security
  slug: protego-trust-bank-domain-security
  summary_line: DNSSEC · DMARC
slug: protego-trust-bank
tags:
- Company
- Banking
- Financial-Services
- Digital Assets
- Cryptocurrency
- Custody
- Trust Bank
- Institutional
- United States
website: https://www.protegotrust.com/
---

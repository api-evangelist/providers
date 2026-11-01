---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: BIT (formerly Matrixport) provides digital asset trading and services. Documentation is at https://www.bit.com/cryptocurrency.
  name: BIT API
  slug: bit-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://www.bit.com/security-trust
- group: agent
  href: https://artifacts.apis.io/matrixport-com/llms/matrixport-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/matrixport-com-llms.txt
- group: other
  href: https://artifacts.apis.io/matrixport-com/hosts/matrixport-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/matrixport-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/matrixport-com/vendors/matrixport-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/matrixport-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bit.com/terms-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.bit.com/security/verification
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bit.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.bit.com/login
- group: auth
  href: https://artifacts.apis.io/matrixport-com/security/matrixport-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/matrixport-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/matrixport-com/security/matrixport-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/matrixport-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bit.com
coverage:
  checked: '2026-10-30'
  detail: Provider documentation pages exist but no OpenAPI, GraphQL, AsyncAPI, gRPC or WSDL contracts were found.
  evidence:
  - status: 404
    url: https://www.bit.com/openapi.json
  - status: 500
    url: https://api.matrixport.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Matrixport, now operating as BIT (Digital Asset Group), provides institutional-grade digital asset financial services, including trading, custody, liquidity, and tokenized real‑world assets. Founded in 2019, it manages over $6 B in assets and serves professional investors worldwide. The rebrand to BIT reflects its expanded product suite and global market presence.
image: https://www.bit.com/og-image.png
layout: provider
modified: '2026-10-28'
name: Matrixport
nav: Providers
network: true
overview: Matrixport is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FinTech, DigitalAssets, Crypto, and Institutional.
random_paper: 14
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Matrixport Com Domain Security
  slug: matrixport-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Matrixport Com Trust Center
  slug: matrixport-com-trust-center
  summary_line: SOC 2, ISO 27001
slug: matrixport-com
tags:
- Company
- FinTech
- DigitalAssets
- Crypto
- Institutional
website: https://www.bit.com
---

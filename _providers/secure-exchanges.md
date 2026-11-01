---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/secure-exchanges/authentication/secure-exchanges-authentication.yml
  title: ''
  type: Authentication
  url: authentication/secure-exchanges-authentication.yml
- group: agent
  href: https://artifacts.apis.io/secure-exchanges/llms/secure-exchanges-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/secure-exchanges-llms.txt
- group: other
  href: https://artifacts.apis.io/secure-exchanges/hosts/secure-exchanges-hosts.yml
  title: ''
  type: Hosts
  url: hosts/secure-exchanges-hosts.yml
- group: other
  href: https://artifacts.apis.io/secure-exchanges/vendors/secure-exchanges-vendors.yml
  title: ''
  type: Vendors
  url: vendors/secure-exchanges-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.secure-exchanges.com/terms-of-sale
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.secure-exchanges.com/privacy-policy.aspx
- group: commercial
  title: ''
  type: Pricing
  url: https://www.secure-exchanges.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.secure-exchanges.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.secure-exchanges.com/
- group: auth
  href: https://artifacts.apis.io/secure-exchanges/security/secure-exchanges-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/secure-exchanges-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://secure-exchanges.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://secure-exchanges.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Secure Exchanges provides a Canadian‑based platform for confidential document exchange, encrypted email, and digital signatures. It enables organizations such as legal, finance, insurance, HR, healthcare, and education to send and receive messages, large files up to 25 GB, and signed documents with end‑to‑end encryption, self‑destruction, code protection, and event logs. The service complies with standards including GDPR, HIPAA, Quebec Law 25, and Adobe AATL.
image: https://www.secure-exchanges.com/images/og/home-en.jpg
layout: provider
modified: '2026-10-21'
name: Secure Exchanges
nav: Providers
network: true
overview: 'Secure Exchanges is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Secure Document Exchange, Email Encryption, Digital Signatures, Compliance, and File Transfer.


  Secure Exchanges'' developer surface includes authentication, pricing, engineering blog, documentation, and 7 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Secure Exchanges Authentication
  slug: secure-exchanges-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Secure Exchanges Domain Security
  slug: secure-exchanges-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: secure-exchanges
tags:
- Secure Document Exchange
- Email Encryption
- Digital Signatures
- Compliance
- File Transfer
website: https://secure-exchanges.com/
---

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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- baseURL: https://api.externalintegration.payex.com
  baseurl_source: declared
  description: The Psp API from Swedbank Pay — 6 operation(s) for psp.
  name: Swedbank Pay Psp API
  slug: swedbank-pay-psp-api
artifact_total: 3
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/swedbank-pay/refs/heads/main/rules/swedbank-pay-rules.yml
  title: ''
  type: Spectral
  url: rules/swedbank-pay-rules.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/swedbank-pay/refs/heads/main/sandbox/swedbank-pay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/swedbank-pay-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/swedbank-pay/refs/heads/main/conformance/swedbank-pay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/swedbank-pay-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/swedbank-pay/refs/heads/main/well-known/swedbank-pay-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/swedbank-pay-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/swedbank-pay/refs/heads/main/well-known/swedbank-pay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/swedbank-pay-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/swedbank-pay/refs/heads/main/hosts/swedbank-pay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swedbank-pay-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/swedbank-pay/refs/heads/main/vendors/swedbank-pay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/swedbank-pay-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/swedbank-pay/refs/heads/main/packages/swedbank-pay-packages.yml
  title: ''
  type: SDKs
  url: packages/swedbank-pay-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/swedbank-pay/refs/heads/main/packages/swedbank-pay-packages.yml
  title: ''
  type: Packages
  url: packages/swedbank-pay-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.swedbankpay.com/checkout-v3/features/customize-ui/tos/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.swedbankpay.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.swedbankpay.com/old-implementations/checkout-v2/technical-reference/prices/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.swedbankpay.com/release-notes/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.swedbankpay.com/checkout-v3/get-started/setup/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SwedbankPay
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/swedbank-pay/refs/heads/main/security/swedbank-pay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swedbank-pay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://swedbankpay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.swedbankpay.com/
- group: operate
  title: ''
  type: Support
  url: https://www.swedbankpay.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.swedbankpay.com/newsroom
coverage:
  checked: '2026-10-15'
  detail: Developer portal provides documentation but no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://developer.swedbankpay.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Swedbank Pay provides a comprehensive, end‑to‑end payment platform for merchants and developers across Sweden and the Nordics. It offers in‑store, online, and acquiring solutions, along with a developer portal, sandbox environment, and extensive documentation to integrate payments, recurring billing, and tokenisation into web, mobile, and POS applications.
layout: provider
modified: '2026-10-14'
name: Swedbank Pay
nav: Providers
network: true
overview: 'Swedbank Pay is listed with 1 API on the [APIs.io](https://apis.io/) network: Psp API. Tagged areas include Company, Payments, Fintech, and Nordic.


  The Swedbank Pay catalog on APIs.io includes 1 Spectral governance ruleset.


  Swedbank Pay''s developer surface includes sandbox, pricing, changelog, getting-started guide, documentation, support, engineering blog, and 13 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Swedbank Pay API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: swedbank-pay-rules
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 42.9
    discoverability: 53.6
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 13.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Swedbank Pay Domain Security
  slug: swedbank-pay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: swedbank-pay
tags:
- Company
- Payments
- Fintech
- Nordic
website: https://swedbankpay.com/
---

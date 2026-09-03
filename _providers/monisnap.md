---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monisnap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.monisnap.com/fr/
- group: design
  title: ''
  type: Conformance
  url: conformance/monisnap-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/monisnap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/monisnap-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monisnap-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://monisnap.zendesk.com/hc/fr
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assets.monisnap.com/monisnap/legal/monisnap-legal-notice.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.monisnap.com/fr/politique-de-confidentialite/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Monisnap
- group: company
  title: ''
  type: Blog
  url: https://dev.to/monisnap
- group: company
  title: ''
  type: BlogRSS
  url: https://dev.to/feed/monisnap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monisnap
coverage:
  checked: '2026-08-17'
  detail: 'MONI markets a B2B "Moni-as-a-Service" remittance-as-a-service platform that Nickel and Bnext already embed, but ships it entirely through direct sales — there is no developer portal to gate: api., docs., developer., developers. and sandbox.monisnap.com all NXDOMAIN, and every /.well-known/ discovery path on the two live hosts 404s.'
  evidence:
  - status: 0
    url: https://developer.monisnap.com/
  - status: 404
    url: https://www.monisnap.com/.well-known/api-catalog
  - status: 404
    url: https://allo.monisnap.com/.well-known/agent-card.json
  - status: 404
    url: https://www.monisnap.com/llms.txt
  - status: 403
    url: https://www.monisnap.com/gb/
  reason: sales-gate
  state: gated
created: '2026-08-17'
description: 'MONI, formerly Monisnap, is a Paris-based remittance fintech founded in 2017 by Raphaël Rivière, Jean-Baptiste Bouvier and Jonathan Brossard. It lets diaspora customers in France, Spain and the United Kingdom send money to roughly 150 countries — as cash pickup across a partner network of some 350,000 payout points, as a transfer into a mobile money wallet, as mobile airtime top-up with more than 800 operators, or as a prepaid card recharge — through a consumer app and the monisnap.com and allo.monisnap.com storefronts. Alongside the consumer product MONI runs a B2B "Moni-as-a-Service" remittance-as-a-service platform that banks and neobanks such as Nickel and Bnext embed white-label in their own applications. MONISNAP SAS is registered with the French ACPR as a payment services agent of MPS SAS, an authorised payment institution (CIB 17738). MONI publishes no public API: there is no developer portal, no API reference and no machine-readable contract on any MONI host — the
  partner platform is reached through a sales conversation.'
image: https://www.monisnap.com/logo.png
layout: provider
modified: '2026-08-17'
name: MONI (Ex-Monisnap)
nav: Providers
network: true
overview: 'MONI (Ex-Monisnap) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech Insurtech, Money Transfer, Remittances, and Payments.


  MONI (Ex-Monisnap)''s developer surface includes support, engineering blog, and 11 more developer resources.'
plans:
- name: Monisnap Plans Pricing
  plan_count: 0
  slug: monisnap-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Monisnap Rate Limits
  slug: monisnap-rate-limits
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 13.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monisnap/refs/heads/main/screenshots/monisnap-2026-09-02T150630.png
security:
- kind: domain-security
  name: Monisnap Domain Security
  slug: monisnap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: monisnap
tags:
- Company
- Fintech Insurtech
- Money Transfer
- Remittances
- Payments
- Mobile Money
- Airtime Top-Up
- Prepaid Cards
- Embedded Finance
- France
website: https://www.monisnap.com/fr/
---

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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Built platform offering real‑estate finance services.
  name: Built API
  slug: built-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/builttechnologiesinc/refs/heads/main/plans/builttechnologiesinc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/builttechnologiesinc-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.getbuilt.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/builttechnologiesinc/refs/heads/main/llms/builttechnologiesinc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/builttechnologiesinc-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/builttechnologiesinc/refs/heads/main/well-known/builttechnologiesinc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/builttechnologiesinc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/builttechnologiesinc/refs/heads/main/hosts/builttechnologiesinc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/builttechnologiesinc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/builttechnologiesinc/refs/heads/main/vendors/builttechnologiesinc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/builttechnologiesinc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getbuilt.com/legal/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://help.getbuilt.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getbuilt.com/
- group: auth
  title: ''
  type: Security
  url: https://getbuilt.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getbuilt.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://getbuilt.com/products/lien-waiver-management-payments/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://getbuilt.com/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://getbuilt.com/developers/
- group: company
  title: ''
  type: Blog
  url: https://getbuilt.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.getbuilt.com/docs/new-account-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getbuilt.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/builttechnologiesinc/refs/heads/main/security/builttechnologiesinc-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/builttechnologiesinc-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/builttechnologiesinc/refs/heads/main/security/builttechnologiesinc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/builttechnologiesinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getbuilt.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://app.getbuilt.com/mcp
  - status: 200
    url: https://getbuilt.com
  - status: 403
    url: https://equityzen.com/company/builttechnologiesinc
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Builttechnologiesinc, operating as Built, provides an AI‑first real‑estate and construction finance platform. It connects lenders, owners, and developers to automate draw management, underwriting, risk mitigation, and portfolio reporting. Powered by a dataset of over $3 trillion in real‑estate finance data, Built’s platform offers tools for loan administration, compliance tracking, lien‑waiver management, and more, helping customers reduce risk and accelerate capital flow.
image: https://getbuilt.com/wp-content/uploads/2025/07/Open-Graph-Image-Opt-02.png
layout: provider
modified: '2026-10-06'
name: Builttechnologiesinc
nav: Providers
network: true
overview: 'Builttechnologiesinc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Construction Finance, Artificial Intelligence, and Fintech.


  Builttechnologiesinc''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
plans:
- name: Builttechnologiesinc Plans Pricing
  plan_count: 1
  slug: builttechnologiesinc-plans-pricing
random_paper: 8
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Builttechnologiesinc Domain Security
  slug: builttechnologiesinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Builttechnologiesinc Trust Center
  slug: builttechnologiesinc-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: builttechnologiesinc
tags:
- Company
- Real Estate
- Construction Finance
- Artificial Intelligence
- Fintech
website: https://getbuilt.com
---

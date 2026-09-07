---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-09-06'
api_count: 1
apis:
- description: The GraphQL gateway that backs the Acin / CUBE Platform web application. It is served from Acin's own Azure API Management instance at apim-prod.acin.com and is referenced by name in the application b
  name: Acin Platform GraphQL Gateway
  slug: acin-platform-graphql-gateway
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acin.com/
- group: company
  title: ''
  type: About
  url: https://www.acin.com/company/about/
- group: docs
  title: ''
  type: Documentation
  url: https://acin-documentation-prd01.azureedge.net/docs/intro
- group: start
  title: ''
  type: Login
  url: https://app.acin.com/
- group: operate
  title: ''
  type: Support
  url: https://www.acin.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.acin.com/resources/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.acin.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acin.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acin.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acin-ltd
- group: auth
  title: ''
  type: TrustCenter
  url: security/acin-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.acin.com/release-note/acin-release-notes-and-product-updates-q2-2025/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/acin-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/acin-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acin-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/acin-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/acin-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acin-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acin-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acin-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acin-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/acin-changelog.yml
created: '2026-09-06'
description: Acin is a London-based operational and non-financial risk (NFR) data company for financial services, founded in 2018 and acquired by regulatory-intelligence firm CUBE in June 2025. Its platform ingests a bank's process, risk and control inventories, standardises them against Acin's published Data Technical Standards — a documented model of Controls, Risks, Processes, Risk Inventories, Regulations, Regulators and Penalties — and benchmarks them anonymously across a peer network of tier-one banks, turning control assessment from a qualitative exercise into a quantified one. Acin is backed by Barclays, BNP Paribas, Citi, J.P. Morgan, Lloyds Banking Group, Fitch Ventures, Notion Capital and Talis Capital, and is listed on the Microsoft Azure Marketplace. It is delivered as a tenant-gated web platform at app.acin.com backed by an Azure API Management GraphQL gateway; there is no public developer program or machine-readable contract.
image: https://www.acin.com/wp-content/uploads/2024/02/icon-1x1-1-300x300.png
layout: provider
modified: '2026-09-06'
name: Acin
nav: Providers
network: true
overview: 'Acin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Operational Risk, Risk Management, Non-Financial Risk, and Financial Services.


  Acin''s developer surface includes documentation, support, engineering blog, changelog, authentication, and 20 more developer resources.'
plans:
- name: Acin Plans Pricing
  plan_count: 0
  slug: acin-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Acin Rate Limits
  slug: acin-rate-limits
scopes:
- name: Acin Scopes
  scope_count: 0
  slug: acin-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 59.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: authentication
  name: Acin Authentication
  slug: acin-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Acin Domain Security
  slug: acin-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Acin Vulnerability Disclosure
  slug: acin-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Acin Trust Center
  slug: acin-trust-center
  summary_line: ISO/IEC 27001, Cyber Essentials
slug: acin
tags:
- Company
- Operational Risk
- Risk Management
- Non-Financial Risk
- Financial Services
- Banking
- Compliance
- Regulatory Technology
- Benchmarking
- Data Standards
website: https://www.acin.com/
---

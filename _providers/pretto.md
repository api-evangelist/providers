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
  url: security/pretto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pretto.fr/
- group: company
  title: ''
  type: About
  url: https://www.pretto.fr/notre-service/
- group: operate
  title: ''
  type: Support
  url: https://www.pretto.fr/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://faq.pretto.fr/fr
- group: company
  title: ''
  type: Blog
  url: https://www.pretto.fr/actualites/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/finspot
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pretto.fr/courtier-credit/courtier-immobilier-comment-ca-marche/prix-courtier/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pretto.fr/cgu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pretto.fr/privacy/
- group: commercial
  title: ''
  type: LegalNotices
  url: https://www.pretto.fr/mentions-legales/
- group: company
  title: ''
  type: Careers
  url: https://www.pretto.fr/nous-rejoindre/
- group: company
  title: ''
  type: Partners
  url: https://www.prettogalaxie.fr/
- group: build
  title: ''
  type: Packages
  url: packages/pretto-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pretto-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/pretto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pretto-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pretto-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.pretto.fr/mentions-legales/
coverage:
  checked: '2026-08-17'
  detail: Pretto's API reference route exists at https://api.pretto.fr/api-docs but is protected by HTTP Basic auth (401), and the developers.pretto.fr ReadMe hub 302s to /inactive and then 401s — while sibling paths on the same API host return 404, so the gate is real and the contract is issued only to Pretto Galaxie broker partners under agreement, never published.
  evidence:
  - status: 401
    url: https://api.pretto.fr/api-docs
  - status: 404
    url: https://api.pretto.fr/api-docsX
  - status: 302
    url: https://developers.pretto.fr/
  - status: 401
    url: https://developers.pretto.fr/inactive
  - status: 404
    url: https://api.pretto.fr/openapi.json
  - status: 404
    url: https://www.pretto.fr/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-08-17'
description: 'Pretto is a French online mortgage brokerage (courtier en credit immobilier) operated by FINSPOT SAS, founded in 2016 and headquartered in Paris. It runs a digital platform that lets borrowers simulate a home loan, compare rates across more than 125 partner banks, assemble a financing file and be accompanied by a human credit expert through to signature, and it publishes a transparent, non-negotiable fee schedule instead of the bank-funded commission model used by most French brokers. Pretto also operates Pretto Galaxie, a B2B network that opens the same technology stack — semi-automated file assembly, an embeddable loan simulator, a client portal, a commission dashboard and a back-office service — to independent brokers, and Pretto Search, a consumer property-search product priced against real borrowing capacity. FINSPOT is registered with ORIAS (17000916) as a banking/payment-services and insurance broker and is supervised by the ACPR. As of this pass Pretto publishes no
  public developer program: the api.pretto.fr host serves its API reference behind HTTP Basic auth and the developers.pretto.fr ReadMe hub is deactivated.'
image: https://res.cloudinary.com/pretto-fr/image/upload/c_fill,w_1200,h_630,f_auto,q_auto/website/pretto-og-default
layout: provider
modified: '2026-08-17'
name: Pretto
nav: Providers
network: true
overview: 'Pretto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech Insurtech, Mortgage, Lending, and Real-Estate.


  Pretto''s developer surface includes support, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Pretto Plans Pricing
  plan_count: 0
  slug: pretto-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Pretto Rate Limits
  slug: pretto-rate-limits
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 16.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 36.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pretto/refs/heads/main/screenshots/pretto-2026-09-02T151949.png
security:
- kind: domain-security
  name: Pretto Domain Security
  slug: pretto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pretto
tags:
- Company
- Fintech Insurtech
- Mortgage
- Lending
- Real-Estate
- Brokerage
- France
- Consumer Finance
- Financial-Services
website: https://www.pretto.fr/
---

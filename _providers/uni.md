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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uni-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uni.cards/
- group: company
  title: ''
  type: Blog
  url: https://www.uni.cards/blog
- group: operate
  title: ''
  type: Support
  url: https://www.uni.cards/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uni.cards/docs/Uni_Terms_and_Conditions_and_Privacy_Policy.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uni.cards/privacy-policy-main
- group: start
  title: ''
  type: SignUp
  url: https://www.uni.cards/apply
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Uni-Cards
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uni-llms.txt
created: '2026-07-17'
description: Uni (Uni Cards) is an Indian consumer credit fintech founded in 2020 by Nitin Gupta, Prateek Jindal, and Laxmikant Vyas that delivers clutter-breaking credit products to consumers in India, including pay-later style credit cards and flexible repayment products. Uni is backed by Lightspeed Venture Partners and General Catalyst. The company is a consumer-facing app-first business and does not currently publish a public developer portal or API surface.
image: https://webcdn.uni.club/images/favicon-48.png
layout: provider
modified: '2026-07-21'
name: Uni
nav: Providers
network: true
overview: 'Uni is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Credit, Credit Cards, and Consumer Finance.


  Uni''s developer surface includes engineering blog, support, signup flow, and 6 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Uni Domain Security
  slug: uni-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: uni
tags:
- Company
- Fintech
- Credit
- Credit Cards
- Consumer Finance
- Payments
- India
website: https://www.uni.cards/
---

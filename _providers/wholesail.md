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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.paywholesail.com
- group: company
  title: ''
  type: Blog
  url: https://www.paywholesail.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://wholesail.zendesk.com
- group: start
  title: ''
  type: Login
  url: https://app.paywholesail.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paywholesail.com/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: security/wholesail-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.paywholesail.com/security/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wholesail-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wholesail-llms.txt
created: '2026-07-17'
description: Wholesail is an all-in-one accounts receivable and B2B payments platform for food & beverage wholesalers, distributors, and service vendors. It helps vendors onboard customers, manage credit risk, automate collections, accept ACH and card payments, and drive autopay — all connected to the vendor's ERP or accounting system. Wholesail is a fintech company backed by Foundry Group. As of enrichment it publishes no public developer API; it integrates with ERP systems using their native API protocols, scheduled file exchange, and robotic process automation, and it partners with Stripe, Plaid, Modern Treasury, JP Morgan, and SVB for payment processing. This profile is maintained in the API Evangelist network.
image: https://www.paywholesail.com/static/og-facebook-190507.jpg
layout: provider
modified: '2026-07-21'
name: Wholesail
nav: Providers
network: true
overview: 'Wholesail is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Accounts Receivable, and B2B.


  Wholesail''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 23.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wholesail/refs/heads/main/screenshots/wholesail-2026-09-02T170718.png
security:
- kind: domain-security
  name: Wholesail Domain Security
  slug: wholesail-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Wholesail Trust Center
  slug: wholesail-trust-center
  summary_line: SOC 2, PCI DSS
slug: wholesail
tags:
- Company
- Fintech
- Payments
- Accounts Receivable
- B2B
- ACH
- Wholesale
- Collection
website: https://www.paywholesail.com
---

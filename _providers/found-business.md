---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Free business checking with a Mastercard business debit card, team cards with spend controls, check and cash deposits, wires, check payments, contractor payments, and sub-accounts. App feature only; n
  name: Found Banking
  slug: found-banking
- description: Automatic expense and income tracking, custom rules and tags, receipt scanning, importing external transactions, and financial reports. App feature only; no public API is documented.
  name: Found Bookkeeping
  slug: found-bookkeeping
- description: Real-time tax estimates with automatic tax savings set-aside, automatic write-offs, tax form generation, mileage tracking, and quarterly federal tax payments from the app (Schedule C filers on the Fou
  name: Found Taxes
  slug: found-taxes
- description: Create and send invoices, track their status, and get paid directly into the Found account, with invoice income flowing into bookkeeping and tax estimates. App feature only; no public API is documente
  name: Found Invoicing
  slug: found-invoicing
- description: Unlimited contractor payments with no per-contractor fees, flexible payment methods, W-9 collection, and free 1099-NEC generation and filing. App feature only; no public API is documented.
  name: Found Contractor Management
  slug: found-contractors
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Found
  slug: open-found-business
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/found-business-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/found-business-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/found-business-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/foundforbusiness
- group: company
  title: ''
  type: Website
  url: https://found.com/
- group: docs
  title: ''
  type: Documentation
  url: https://found.com/help
- group: commercial
  title: ''
  type: Plans
  url: plans/found-business-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/found-business-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/found-business-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://found.com/resources
created: '2026-06-20'
description: Found is a fintech business-banking app for the self-employed, freelancers, and sole proprietors that combines a free business checking account (banking services provided by Lead Bank, Member FDIC) with built-in bookkeeping, real-time tax estimates and payments, invoicing, and contractor management. As of the 2026-06-20 review Found exposes no public or partner developer API; the surfaces below are documented as in-app product features, not programmatic APIs.
finops:
- name: Found Business Finops
  service_category: Financial Services
  slug: found-business-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/found-business.png
layout: provider
modified: '2026-06-20'
name: Found
nav: Providers
network: true
overview: 'Found publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Banking, Bookkeeping, Taxes, and 2 more. Tagged areas include Fintech, Business Banking, Bookkeeping, Taxes, and Self-Employed.


  Found''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Found Business Plans Pricing
  plan_count: 3
  slug: found-business-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Found Business Rate Limits
  slug: found-business-rate-limits
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 47.0
    catalog_earned_first_party: 0.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 25.9
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/found-business/refs/heads/main/screenshots/found-business-2026-06-20T181457.png
security:
- kind: domain-security
  name: Found Business Domain Security
  slug: found-business-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Found Business Vulnerability Disclosure
  slug: found-business-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Found Business Trust Center
  slug: found-business-trust-center
  summary_line: SOC 2, PCI DSS
slug: found-business
tags:
- Fintech
- Business Banking
- Bookkeeping
- Taxes
- Self-Employed
website: https://found.com/
---

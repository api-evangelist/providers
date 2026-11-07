---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://dpogroup.com/compliance/
- group: build
  href: https://artifacts.apis.io/dpo-pay/errors/dpo-pay-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/dpo-pay-decline-codes.yml
- group: agent
  href: https://artifacts.apis.io/dpo-pay/llms/dpo-pay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dpo-pay-llms.txt
- group: agent
  href: https://artifacts.apis.io/dpo-pay/well-known/dpo-pay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dpo-pay-well-known.yml
- group: other
  href: https://artifacts.apis.io/dpo-pay/hosts/dpo-pay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dpo-pay-hosts.yml
- group: other
  href: https://artifacts.apis.io/dpo-pay/vendors/dpo-pay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dpo-pay-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dpogroup.com/terms-and-conditions-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dpogroup.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://dpogroup.com/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DPO-Group
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dpopay.com/api/index.html
- group: auth
  href: https://artifacts.apis.io/dpo-pay/security/dpo-pay-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dpo-pay-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dpo-pay/security/dpo-pay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dpo-pay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dpogroup.com/
- group: company
  title: ''
  type: Blog
  url: https://dpogroup.com/blog
- group: operate
  title: ''
  type: Support
  url: https://dpogroup.com/contact-us
- group: start
  title: ''
  type: GettingStarted
  url: https://dpogroup.com/get-started-2
created: '2026-10-27'
description: DPO Pay provides secure online payment solutions across Africa, offering a range of products such as mobile POS, network POS, easy‑scan, ecommerce payment links and invoicing. Operating in over 20 countries, it enables merchants to accept multiple payment methods, including cards and mobile money, with fraud protection and PCI‑DSS Level 1 compliance. The platform serves thousands of businesses, delivering fast, reliable transactions and comprehensive integration options for shopping carts and hotel management platforms.
image: https://dpogroup.com/wp-content/uploads/2025/01/Network-POS-Machines.svg?wsr
layout: provider
modified: '2026-10-27'
name: DPO Pay
nav: Providers
network: true
overview: 'DPO Pay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Africa, Fintech, and E-Commerce.


  DPO Pay''s developer surface includes engineering blog, support, getting-started guide, and 14 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 11.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dpo-pay/dpo-pay-2026-11-03T131020.png
security:
- kind: domain-security
  name: Dpo Pay Domain Security
  slug: dpo-pay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dpo Pay Trust Center
  slug: dpo-pay-trust-center
  summary_line: PCI DSS, GDPR
slug: dpo-pay
tags:
- Company
- Payments
- Africa
- Fintech
- E-Commerce
website: https://dpogroup.com/
---

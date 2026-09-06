---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://linkablenetworks.com/'', ''status'': 308, ''note'': ''declared website redirects to https://www.absolute-sway.com/ — a different registrable domain (linkablenetworks.com -> absolute-sway.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: RESTful consumer API for building applications on top of the Linkable card-linked-offer platform. Per the provider developer page it exposes consumer registration, view and opt-out (consumerapi/consum
  name: MyLinkables Consumer API
  slug: mylinkables-consumer-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linkable-networks-collinson-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://linkablenetworks.com/
- group: company
  title: ''
  type: Website
  url: https://www.collinsongroup.com/en-GB
- group: start
  title: ''
  type: DeveloperPortal
  url: https://linkablenetworks.com/appweb-developers/
- group: docs
  title: ''
  type: Documentation
  url: https://linkablenetworks.com/appweb-developers/
- group: start
  title: ''
  type: Login
  url: https://www.mylinkables.com/
- group: operate
  title: ''
  type: Support
  url: https://linkablenetworks.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://linkablenetworks.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/collinsongroup
- group: company
  title: ''
  type: Blog
  url: https://www.collinsongroup.com/en-GB/insights
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/linkables
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/pages/Linkable-Networks/300275889988840
- group: auth
  title: ''
  type: Authentication
  url: authentication/linkable-networks-collinson-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linkable-networks-collinson-group-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/linkable-networks-collinson-group-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linkable-networks-collinson-group-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/linkable-networks-collinson-group-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linkable-networks-collinson-group-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/linkable-networks-collinson-group-packages.yml
created: '2026-07-17'
description: Linkable Networks, Inc. is a Boston-based card-linked-offers (CLO) and SKU-linked-offers platform that lets consumers attach digital offers directly to the credit and debit cards already in their wallet. When a linked card is used for a qualifying purchase on the Visa, MasterCard, American Express or PayPal rails, the Linkable platform receives the transaction, optionally confirms item-level detail through the on-premises Linkable SKU Matcher, and delivers the savings back to the cardholder as a statement credit, eGift, points or miles - with no POS integration, no additional hardware or software, no punch cards and no employee training. The company sells to brands and retailers (product/SKU-level promotions funded with trade and co-op dollars), to loyalty program operators (single-purchase, multi-visit and aggregate-spend reward mechanics layered on an existing program), and to publishers and app developers, who integrate the consumer-facing MyLinkables REST API to display
  offers, link them to a cardholder, register consumers, manage linked payment accounts and track redemption. Linkable Networks is associated with the Collinson Group, the privately-owned global travel, loyalty and insurance operator behind Priority Pass, and was surfaced through the Bain Capital Ventures portfolio.
image: https://linkablenetworks.com/wp-content/themes/linkablenetworks/library/images/svg/logo-mark.svg
layout: provider
modified: '2026-07-19'
name: Linkable Networks (Collinson Group)
nav: Providers
network: true
overview: 'Linkable Networks (Collinson Group) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Card-Linked Offers, Loyalty, and Payments.


  Linkable Networks (Collinson Group)''s developer surface includes documentation, support, engineering blog, authentication, and 15 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 21.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linkable-networks-collinson-group/refs/heads/main/screenshots/linkable-networks-collinson-group-2026-07-25T225253.png
security:
- kind: authentication
  name: Linkable Networks Collinson Group Authentication
  slug: linkable-networks-collinson-group-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Linkable Networks Collinson Group Domain Security
  slug: linkable-networks-collinson-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: linkable-networks-collinson-group
tags:
- Company
- Fintech
- Card-Linked Offers
- Loyalty
- Payments
- Rewards
- Advertising
- Retail
website: https://linkablenetworks.com/
---

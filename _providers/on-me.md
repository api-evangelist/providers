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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/on-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onme.com/
- group: company
  title: ''
  type: Blog
  url: https://onme.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://onme.com/help
- group: operate
  title: ''
  type: Support
  url: mailto:support@onme.com
- group: start
  title: ''
  type: SignUp
  url: https://onme.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onme.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onme.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onmegifting
- group: commercial
  title: ''
  type: Plans
  url: plans/on-me-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/on-me-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/on-me-llms.txt
coverage:
  checked: '2026-08-26'
  detail: On Me's only API surface is a marketing page at /corporate-gift-cards/gifting-api that describes the Gifting API entirely in the future tense and offers "Talk to a specialist / Book a call" instead of a reference — there is no developer portal, no base URL, and no spec on onme.com, business.onme.com or the company GitHub org.
  evidence:
  - status: 200
    url: https://onme.com/corporate-gift-cards/gifting-api
  - status: 404
    url: https://onme.com/developers
  - status: 404
    url: https://onme.com/openapi.json
  - status: 404
    url: https://business.onme.com/openapi.json
  - status: 404
    url: https://onme.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-08-26'
description: On Me is a San Francisco digital gifting company that sells wallet-native, multi-brand eGift cards organised by hobby and interest rather than by single retailer. Founded by former Google product managers Darragh Meaney and Sitar Harel, it emerged from stealth in December 2024 with a five-year Mastercard partnership and $1.7M in pre-seed funding led by Lerer Hippeau and Focal VC. Recipients add a gift to Apple Wallet or Google Wallet and tap to pay across a curated category of brands, and senders can attach photos, video and GIFs. A business portal supports corporate gifting, campaigns and bulk sends. On Me markets a forthcoming Gifting API for programmatic rewards, incentives and webhooks, but as of this pass no public API reference, base URL, or machine-readable specification is published — access runs through a "talk to a specialist" sales conversation.
image: https://onme.com/assets/headers/onmeOpenGraphDefault.webp
layout: provider
modified: '2026-08-26'
name: On Me
nav: Providers
network: true
overview: 'On Me is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gift Cards, Digital Gifting, Corporate Gifting, and Rewards and Incentives.


  On Me''s developer surface includes engineering blog, support, signup flow, and 9 more developer resources.'
plans:
- name: On Me Plans Pricing
  plan_count: 0
  slug: on-me-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: On Me Rate Limits
  slug: on-me-rate-limits
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 6
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
    operational_transparency: 2.6
  previous_composite: 12.7
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
  name: On Me Domain Security
  slug: on-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: on-me
tags:
- Company
- Gift Cards
- Digital Gifting
- Corporate Gifting
- Rewards and Incentives
- Payments
- Mobile Wallet
- Employee Recognition
- Consumer
website: https://onme.com/
---

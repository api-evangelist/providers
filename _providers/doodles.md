---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 5
asyncapis:
- description: ''
  name: Doodles Webhooks
  slug: doodles-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doodles-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/doodles-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/doodles-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/doodles-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doodles-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/doodles-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/doodles-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doodles-llms.txt
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Doodles/webhook-example
- group: company
  title: ''
  type: Website
  url: https://www.doodles.app/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Doodles
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doodles.app/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doodles.app/legal/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/doodles-stock
created: '2026-08-12'
description: Doodles is a Web3-native entertainment and media company built around the 10,000-piece Doodles NFT collection launched on Ethereum in 2021 by artist Scott Martin (Burnt Toast) with Evan Keast and Jordan Castro. Doodles, LLC has since grown into a character-IP and animation business — it acquired the Emmy-nominated animation studio Golden Wolf, ships the Stoodio avatar app, the DOOD token, the Prism image model trained on Doodles-owned IP, and DreamNet, an onchain worldbuilding and storytelling layer. Doodles publishes no public REST API or developer portal; its machine-readable developer surface is limited to two first-party open-source npm libraries for the Flow blockchain (@doodlesteam/floo and @doodlesteam/flooks) and a signed outbound webhook integration contract published as a reference server on its GitHub organization.
image: https://avatars.githubusercontent.com/u/96498387?v=4
layout: provider
modified: '2026-08-12'
name: Doodles
nav: Providers
network: true
overview: 'Doodles is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, NFT, Web3, Blockchain, and Entertainment.


  The Doodles catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Doodles'' developer surface includes authentication and 13 more developer resources.'
plans:
- name: Doodles Plans Pricing
  plan_count: 0
  slug: doodles-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Doodles Rate Limits
  slug: doodles-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 23.2
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Doodles Authentication
  slug: doodles-authentication
  summary_line: hmac-signature · 1 scheme
- kind: domain-security
  name: Doodles Domain Security
  slug: doodles-domain-security
  summary_line: TLSv1.3 · DMARC
slug: doodles
tags:
- Company
- NFT
- Web3
- Blockchain
- Entertainment
- Media
- Digital Collectibles
- Animation
- Consumer
- Webhook
website: https://www.doodles.app/
---

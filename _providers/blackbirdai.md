---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.1
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: An API for checking the context of inputs and managing contextChecks and visionAnalyses.
  name: Compass API
  slug: compass-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackbirdai/refs/heads/main/authentication/blackbirdai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blackbirdai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blackbirdai/refs/heads/main/conformance/blackbirdai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blackbirdai-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackbirdai/refs/heads/main/overlays/blackbirdai-compass-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/blackbirdai-compass-openapi-overlay.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blackbirdai/refs/heads/main/llms/blackbirdai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blackbirdai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blackbirdai/refs/heads/main/well-known/blackbirdai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blackbirdai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackbirdai/refs/heads/main/hosts/blackbirdai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackbirdai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blackbirdai/refs/heads/main/vendors/blackbirdai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blackbirdai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blackbird.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blackbird.ai/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://blackbird.ai/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://blackbird.ai/news
- group: start
  title: ''
  type: Login
  url: https://app.blackbird.ai/login
- group: other
  title: ''
  type: Leadership
  url: https://blackbird.ai/team
- group: company
  title: ''
  type: Blog
  url: https://blackbird.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blackbird.ai/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blackbird.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blackbirdai/refs/heads/main/security/blackbirdai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackbirdai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blackbird.ai
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://app.blackbird.ai/api/graphql
  - status: 403
    url: https://api.blackbird.ai/mcp
  - status: 403
    url: https://forgeglobal.com/blackbirdai_stock/
  reason: partner-login
  state: gated
created: '2026-09-29'
description: Blackbird.AI provides a Narrative & Risk Intelligence Platform that aggregates and analyzes public data to deliver actionable insights for enterprises. Their solutions include Constellation Platform, Compass Context, RAV3N Watch, and other tools that help organizations monitor brand risk, supply chain threats, geopolitical events, and financial market manipulations. The platform serves sectors such as finance, healthcare, media, and public sector, offering APIs for real-time data access and integration.
image: https://blackbird.ai/wp-content/uploads/2024/04/social-media-default-image.jpg
layout: provider
modified: '2026-09-29'
name: Blackbird.AI
nav: Providers
network: true
overview: 'Blackbird.AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Risk Intelligence, Data Analytics, and Enterprise.


  Blackbird.AI''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, and 13 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 76.8
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blackbirdai Authentication
  slug: blackbirdai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Blackbirdai Domain Security
  slug: blackbirdai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blackbirdai
tags:
- Company
- Artificial Intelligence
- Risk Intelligence
- Data Analytics
- Enterprise
website: https://blackbird.ai
---

---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
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
    auth_clarity: served
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
  score: 9.0
  scored_at: '2026-09-12'
api_count: 3
apis:
- description: Public-facing presence of Electronic Arts. Covers EA's corporate site, consumer game services, the EA app, EA Play subscription, and EA Help support surfaces. EA does not publish a developer API porta
  name: Electronic Arts
  slug: electronic-arts
- description: 'EA''s account authorization server at accounts.ea.com — the single identity surface behind the EA app, EA''s web properties and the approved EA SPORTS FC Community API partners. EA serves a live OpenID '
  name: EA Account OpenID Connect / OAuth 2.0
  slug: ea-account-connect
- description: 'EA''s only API programme, announced 2026-07-27. A player connects their EA Account to an approved community site through EA''s OAuth login flow and grants that site permission to make specific requests '
  name: EA SPORTS FC Community API
  slug: fc-community-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/electronic-arts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/electronic-arts-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/electronic-arts
- group: company
  title: ''
  type: Website
  url: https://www.ea.com
- group: operate
  title: ''
  type: Support
  url: https://help.ea.com
- group: other
  title: ''
  type: Subscription
  url: https://www.ea.com/ea-play
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.ea.com
- group: company
  title: ''
  type: Careers
  url: https://www.ea.com/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/electronicarts
- group: company
  title: ''
  type: Blog
  url: https://www.ea.com/news
- group: agent
  title: ''
  type: WellKnown
  url: well-known/electronic-arts-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/electronic-arts-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/electronic-arts-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/electronic-arts-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/electronic-arts-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/electronic-arts-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/electronic-arts-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/electronic-arts-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/electronic-arts-llms.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://help.ea.com/en/server-status/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.ea.com/service-updates
- group: auth
  title: ''
  type: Security
  url: https://www.ea.com/security/disclosure
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ea.com/legal/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ea.com/legal/privacy-and-cookie-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ea.com/ea-play
created: '2026-03-21'
description: Electronic Arts (EA) is a global leader in digital interactive entertainment, developing and delivering games, content, and online services for internet-connected consoles, mobile devices, and personal computers. EA's portfolio includes franchises such as EA SPORTS FC, Madden NFL, Battlefield, The Sims, Apex Legends, and Need for Speed, supported by online services like the EA app, EA Play, and EA Help. EA runs no public developer portal and publishes no OpenAPI, GraphQL, AsyncAPI or gRPC contract. Its one API programme is the EA SPORTS FC Community API, announced 2026-07-27, which lets a player grant an approved community site (FUT.GG, FUTBIN, FUTWIZ) delegated read access to Ultimate Team data through EA's OAuth flow; EA states it is not accepting further partner requests. The only machine-readable documents EA serves anywhere are the OpenID Connect Discovery and RFC 8414 authorization-server metadata on accounts.ea.com, plus the JWKS they reference.
finops:
- name: Electronic Arts Finops
  service_category: Entertainment
  slug: electronic-arts-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/electronic-arts.png
layout: provider
modified: '2026-09-06'
name: Electronic Arts
nav: Providers
network: true
overview: 'Electronic Arts publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Video Games, Entertainment, Consumer, and Player Services.


  Electronic Arts'' developer surface includes support, engineering blog, authentication, pricing, and 21 more developer resources.'
plans:
- name: Electronic Arts Plans Pricing
  plan_count: 2
  slug: electronic-arts-plans-pricing
press:
- date: '2026-05-25'
  title: Sent Via email October 28, 2025 Scott Bessent Secretary of ...
  url: https://cwa-union.org/sites/default/files/2025-10/20251028_cwa_letter_to_secretary_bessent.pdf
- date: '2026-05-25'
  title: Stability AI Partners with Electronic Arts on Customizable AI
  url: https://www.linkedin.com/posts/prem-akkaraju-7b10a265_inside-video-game-giant-electronic-arts-activity-7424598337934442497-I3Ck
- date: '2026-05-25'
  title: Mr. Andrew Wilson Chief Executive Officer Electronic Arts, Inc.
  url: https://www.hsgac.senate.gov/wp-content/uploads/2025-10-14-Letter-from-Blumenthal-and-Warren-to-Electronic-Arts-CEO-Andrew-Wilson.pdf
- date: '2026-05-25'
  title: Inside the AI divide roiling video game giant Electronic Arts
  url: https://www.businessinsider.com/inside-ai-divide-roiling-video-game-giant-electronic-arts-2025-10
- date: '2026-05-25'
  title: EA and Stability AI partner to empower artists, designers, ...
  url: https://www.ea.com/news/ea-partners-with-stability-ai
random_paper: 18
rate_limits:
- limit_count: 0
  name: Electronic Arts Rate Limits
  slug: electronic-arts-rate-limits
scopes:
- name: Electronic Arts Scopes
  scope_count: 0
  slug: electronic-arts-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.0
    catalog_earned_first_party: 8.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 64.8
    operational_transparency: 39.5
  previous_composite: 30.2
  provenance:
    conformance: first-party
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/electronic-arts/refs/heads/main/screenshots/electronic-arts-2026-06-20T180553.png
security:
- kind: authentication
  name: Electronic Arts Authentication
  slug: electronic-arts-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Electronic Arts Domain Security
  slug: electronic-arts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Electronic Arts Vulnerability Disclosure
  slug: electronic-arts-vulnerability-disclosure
  summary_line: Hackerone
slug: electronic-arts
tags:
- Gaming
- Video Games
- Entertainment
- Consumer
- Player Services
- Fortune 1000
website: https://www.ea.com
---

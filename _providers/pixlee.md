---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pixlee Agentic Access
  operation_count: 4
  slug: pixlee-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 3
apis:
- baseURL: https://distillery.pixlee.co/api/v2
  baseurl_source: declared
  description: Consume approved UGC media from albums (with filters/sorts and pagination), ingest new content from a URL or file, and add or update products. API key in query plus HMAC-SHA1 signature for writes; res
  name: Pixlee Content API
  slug: pixlee-content-api
- baseURL: https://distillery.pixlee.co/api/v2
  baseurl_source: declared
  description: Create albums and add or update products
  name: Pixlee Albums API
  slug: pixlee-albums-api
- baseURL: https://distillery.pixlee.co/api/v2
  baseurl_source: declared
  description: Upload new content from a URL or a file
  name: Pixlee Media API
  slug: pixlee-media-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pixlee Content Albums API
  slug: open-pixlee-albums-api
- collection_type: open
  name: Pixlee Albums Content API
  slug: open-pixlee-content-api
- collection_type: open
  name: Pixlee Content Albums Media API
  slug: open-pixlee-media-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.pixlee.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pixlee.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.pixlee.com/reference/about-the-content-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.pixlee.com/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.pixlee.com/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/changelog/pixlee-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pixlee-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pixlee
- group: operate
  title: ''
  type: Support
  url: https://support.emplifi.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://emplifi.io/resource-type/blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://emplifi.io/pricing/
- group: start
  title: ''
  type: Login
  url: https://emplifi.io/login/
- group: start
  title: ''
  type: SignUp
  url: https://emplifi.io/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emplifi.io/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emplifi.io/legal/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://emplifi.io/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/llms/pixlee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pixlee-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/packages/pixlee-packages.yml
  title: ''
  type: Packages
  url: packages/pixlee-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/packages/pixlee-packages.yml
  title: ''
  type: SDKs
  url: packages/pixlee-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/well-known/pixlee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pixlee-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/mcp/pixlee-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/pixlee-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/conformance/pixlee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pixlee-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/errors/pixlee-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pixlee-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/lifecycle/pixlee-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pixlee-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/authentication/pixlee-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pixlee-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/security/pixlee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pixlee-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/conventions/pixlee-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pixlee-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/data-model/pixlee-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pixlee-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/components/pixlee-components.yml
  title: ''
  type: Components
  url: components/pixlee-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/agentic-access/pixlee-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pixlee-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Pixlee (Pixlee TurnTo, now part of Emplifi) is a visual and social user-generated content (UGC) marketing platform that helps brands collect, curate, moderate, and display customer photos and videos across their website, mobile apps, and email. The Pixlee Content API (v2) gives brands programmatic access to their approved media in albums with rich filtering and sorting, lets them ingest new content from a URL or an uploaded file, and add or update commerce products that media can be tagged with. Authentication is via an account API key passed as a query parameter, with HMAC-SHA1 request signing required for all writes. Pixlee also ships embeddable JavaScript display widgets, email display blocks, and native iOS/Android UI SDKs. Originally an a16z-backed startup, Pixlee was acquired by Emplifi.
image: https://files.readme.io/9160404-small-transparentLogo.png
layout: provider
modified: '2026-07-20'
name: Pixlee
nav: Providers
network: true
overview: 'Pixlee publishes 3 APIs on the [APIs.io](https://apis.io/) network: Content API, Albums API, and Media API. Tagged areas include Company, User Generated Content, Social Commerce, Visual Marketing, and Content.


  Pixlee''s developer surface includes documentation, API reference, getting-started guide, changelog, support, engineering blog, pricing, and 23 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 13.3
    developer_ergonomics: 47.0
    discoverability: 78.6
    operational_transparency: 10.5
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/pixlee/refs/heads/main/screenshots/pixlee-2026-08-17T081245.png
security:
- kind: authentication
  name: Pixlee Authentication
  slug: pixlee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pixlee Domain Security
  slug: pixlee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pixlee
tags:
- Company
- User Generated Content
- Social Commerce
- Visual Marketing
- Content
- Media
- E-Commerce
- Widgets
- Emplifi
website: https://emplifi.io/
---

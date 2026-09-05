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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-04'
api_count: 3
apis:
- baseURL: https://rest.ceros.com
  baseurl_source: declared
  description: The accounts API from Ceros — 1 operation(s) for accounts.
  name: Ceros Accounts API
  slug: ceros-accounts-api
- baseURL: https://rest.ceros.com
  baseurl_source: declared
  description: The embedCodes API from Ceros — 1 operation(s) for embedcodes.
  name: Ceros Embed Codes API
  slug: ceros-embedcodes-api
- baseURL: https://rest.ceros.com
  baseurl_source: declared
  description: The experience API from Ceros — 1 operation(s) for experience.
  name: Ceros Experience API
  slug: ceros-experience-api
- baseURL: https://rest.ceros.com
  baseurl_source: declared
  description: The experiencePage API from Ceros — 6 operation(s) for experiencepage.
  name: Ceros Experience Page API
  slug: ceros-experiencepage-api
- baseURL: https://rest.ceros.com
  baseurl_source: declared
  description: The folders API from Ceros — 1 operation(s) for folders.
  name: Ceros Folders API
  slug: ceros-folders-api
- baseURL: https://rest.ceros.com
  baseurl_source: declared
  description: The oembed API from Ceros — 1 operation(s) for oembed.
  name: Ceros Oembed API
  slug: ceros-oembed-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ceros Accounts API
  slug: open-ceros-accounts-api
- collection_type: open
  name: Ceros Embed Codes API
  slug: open-ceros-embedcodes-api
- collection_type: open
  name: Ceros Experience API
  slug: open-ceros-experience-api
- collection_type: open
  name: Ceros Public Experience Page API
  slug: open-ceros-experiencepage-api
- collection_type: open
  name: Ceros Folders API
  slug: open-ceros-folders-api
- collection_type: open
  name: Ceros Oembed API
  slug: open-ceros-oembed-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ceros-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ceros-public-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.ceros.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ceros.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.ceros.com/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.ceros.com/api/public/ceros-public-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.ceros.com/guides/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://educate.ceros.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.ceros.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.ceros.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ceros
- group: operate
  title: ''
  type: Roadmap
  url: https://portal.productboard.com/ceros/7-ceros-staging-roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ceros.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://www.ceros.com/login/
- group: start
  title: ''
  type: SignUp
  url: https://www.ceros.com/demo-request/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ceros.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ceros.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ceros.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/ceros-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/ceros-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ceros-packages.yml
- group: design
  title: ''
  type: Components
  url: components/ceros-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ceros-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ceros-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ceros-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ceros-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ceros-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ceros-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ceros-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ceros-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ceros-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ceros-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-09'
description: Ceros is an experiential content platform used by marketing, design and agency teams to build interactive, no-code web content — microsites, landing pages, interactive reports, infographics, pitch decks and embeddable experiences — in a browser design studio and publish them to a CDN. Its developer surface is three separate things. A small read-only REST Public API at rest.ceros.com walks accounts, folders, experiences and embed codes behind a bearer API key, versioned by dated snapshots selected with the x-ceros-api-version header. A browser-side Flex Experience SDK, delivered as an ES module from the Ceros CDN, scripts a published experience at runtime — setting text, controlling media and states, toggling visibility and navigating pages. And a public oEmbed 1.0 endpoint on view.ceros.com, together with first-party connectors for Adobe Experience Manager, Contentful, Optimizely and WordPress, places an experience inside another platform. Ceros also operates MarkUp, its visual
  commenting and collaboration product.
examples:
- key_count: 10
  name: Ceros Oembed Response
  slug: ceros-oembed-response
image: https://www.ceros.com/favicon.ico
layout: provider
modified: '2026-08-09'
name: Ceros
nav: Providers
network: true
overview: 'Ceros publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Embed Codes API, Experience API, and 3 more. Tagged areas include Content Management, Interactive Content, Digital Experience, Embed, and oEmbed.


  Ceros'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 56.3
    developer_ergonomics: 66.1
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 50.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 16.7
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ceros/refs/heads/main/screenshots/ceros-2026-08-17T080810.png
security:
- kind: authentication
  name: Ceros Authentication
  slug: ceros-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ceros Domain Security
  slug: ceros-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ceros Trust Center
  slug: ceros-trust-center
  summary_line: trust center published
slug: ceros
tags:
- Content Management
- Interactive Content
- Digital Experience
- Embed
- oEmbed
- CMS Integration
- Marketing
- Design
- No-Code
- Content Delivery
- Media and Publishing
- SDK
website: https://www.ceros.com/
---

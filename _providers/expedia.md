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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.expedia.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.expediagroup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.expediagroup.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://www.expedia.com/helpcenter
- group: company
  title: ''
  type: Blog
  url: https://partner.expediagroup.com/en-us/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ExpediaGroup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.expediagroup.com/terms-of-use/default.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.expediagroup.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/expediagroup
- group: other
  title: ''
  type: Canonical Catalog
  url: https://github.com/api-evangelist/expedia-group
- group: docs
  title: ''
  type: GraphQL
  url: graphql/expedia-graphql.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/expedia-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/expedia-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/expedia-security.txt
- group: auth
  title: ''
  type: Security
  url: security/expedia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/expedia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/expedia-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/expedia-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/expedia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/expedia-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/expedia-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/expedia-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/expedia-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/expedia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/expedia-rate-limits.yml
created: '2026-03-21'
description: Expedia is one of the world's leading travel platforms, helping travelers plan and book trips through a portfolio of brands including Expedia, Hotels.com, Vrbo, Orbitz, Travelocity, Hotwire, Wotif, and trivago. Developer APIs are published under the Expedia Group developer platform; this repository serves as a brand alias pointing to the canonical expedia-group catalog.
graphqls:
- description: 'generated: ''2026-09-07'''
  name: Expedia GraphQL
  slug: expedia-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/expedia.png
layout: provider
mcp_servers:
- description: An MCP server for the Expedia Travel Recommendation Service API, exposing hotel, flight, activity and car-rental recommendations to MCP clients.
  name: Expedia Travel Recommendations MCP Server
  slug: expedia-travel-recommendations-mcp-server
modified: '2026-09-07'
name: Expedia
nav: Providers
network: true
overview: 'Expedia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Flights, Hotels, Lodging, Travel, and Fortune 500.


  Expedia''s developer surface includes documentation, support, engineering blog, and 22 more developer resources.'
plans:
- name: Expedia Plans Pricing
  plan_count: 0
  slug: expedia-plans-pricing
press:
- date: '2026-05-25'
  title: Expedia introduced its AI trip-planning chatbot Roamie two ...
  url: https://www.facebook.com/Skiftnews/posts/expedia-introduced-its-ai-trip-planning-chatbot-roamie-two-years-ago-but-ceo-ari/1293646796224631/
- date: '2026-05-25'
  title: 'Expedia Group Reveals ''The AI Trust Gap'': Travelers ...'
  url: https://www.businesswire.com/news/home/20260414532485/en/Expedia-Group-Reveals-The-AI-Trust-Gap-Travelers-Embrace-AI-for-Planning-but-Rely-on-Trusted-Brands-to-Book
- date: '2026-05-25'
  title: News
  url: https://ir.expediagroup.com/news-and-events/media/
- date: '2026-05-25'
  title: 'Put Your Trip on Autopilot: Expedia Group Introduces New ...'
  url: https://www.expedia.com/newsroom/spring-product-release-2024/
- date: '2026-05-25'
  title: Expedia Group sees reward and risk in the rise of AI- ...
  url: https://www.geekwire.com/2026/expedia-group-sees-reward-and-risk-in-the-rise-of-ai-powered-travel/
random_paper: 1
rate_limits:
- limit_count: 0
  name: Expedia Rate Limits
  slug: expedia-rate-limits
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 31.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 32.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/expedia/refs/heads/main/screenshots/expedia-2026-07-25T213918.png
security:
- kind: domain-security
  name: Expedia Domain Security
  slug: expedia-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Expedia Vulnerability Disclosure
  slug: expedia-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: expedia
tags:
- Flights
- Hotels
- Lodging
- Travel
- Fortune 500
website: https://www.expedia.com
---

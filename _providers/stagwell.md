---
access_model:
  confidence: medium
  label: Contract-only API access
  onboarding: approval
  pricing: paid
  public: false
  source:
  - https://influencermarketing.ai/api/
  - https://influencermarketing.ai/pricing/
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 29.9
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: Credit-metered REST API over IMAI's creator database of 380M+ influencers across Instagram, TikTok and YouTube. Documented capabilities are keyword and filter search, AI search, influencer reports, au
  name: IMAI Discovery API
  slug: imai-discovery-api
- description: Per-request REST API returning live, unfiltered data read directly from influencer profiles — campaign post capture, mention monitoring, and brand and creator collaboration timelines in real time. Met
  name: IMAI Raw API
  slug: imai-raw-api
- description: OAuth-protected Model Context Protocol endpoint served on the IMAI / InfluencerMarketing.ai host by the Novamira WordPress plugin, advertised through RFC 9728 protected-resource metadata and an RFC 84
  name: IMAI MCP Server
  slug: imai-mcp-server
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stagwell-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stagwell-Marketing-Cloud
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stagwell
- group: company
  title: ''
  type: Website
  url: https://www.stagwellglobal.com
- group: other
  title: ''
  type: MarketingCloud
  url: https://www.stagwellglobal.com/smc/
- group: company
  title: ''
  type: Blog
  url: https://www.stagwellglobal.com/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://influencermarketing.ai/api/
- group: docs
  title: ''
  type: Documentation
  url: https://imai.co/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://imai.co/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://influencermarketing.ai/api/
- group: start
  title: ''
  type: SignUp
  url: https://imai.co/signup
- group: start
  title: ''
  type: Login
  url: https://imai.co/login
- group: operate
  title: ''
  type: Support
  url: https://influencermarketing.ai/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://influencermarketing.ai/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stagwellglobal.com/privacy-policy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stagwell-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stagwell-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stagwell-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stagwell-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/stagwell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stagwell-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stagwell-imai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/stagwell-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stagwell-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://influencermarketing.ai/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/stagwell-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://influencermarketing.ai/security/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stagwell-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stagwell-conventions.yml
- group: other
  title: ''
  type: Platform
  url: https://www.themarketingcloud.com/
created: '2026-05-04'
description: 'Stagwell (NASDAQ: STGW) is a digital-first global marketing services and technology company and a Fortune 1000 firm, operating a network of creative, media, communications and research agencies alongside the Stagwell Marketing Cloud (now branded The Marketing Cloud), a suite of proprietary SaaS and DaaS marketing-technology products built by its in-house engineering teams. Stagwell does not publish a unified public developer portal at the holding-company level and ships no OpenAPI, AsyncAPI or agent card of its own; developer access is exposed product by product. The most substantial public developer surface in the group belongs to IMAI / InfluencerMarketing.ai, acquired with LEADERS in July 2024 and folded into the PRophet Comms Tech suite, which publishes a credit-metered REST creator-data API (Discovery and Raw), an llms.txt, and an OAuth-protected Model Context Protocol endpoint on its own host.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stagwell.png
layout: provider
mcp_servers:
- description: ''
  name: Stagwell MCP Server
  slug: stagwell-mcp-server
modified: '2026-08-12'
name: Stagwell
nav: Providers
network: true
overview: 'Stagwell publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, Advertising, Media, MarTech, and Influencer Marketing.


  Stagwell''s developer surface includes engineering blog, documentation, API reference, pricing, signup flow, support, authentication, and 23 more developer resources.'
plans:
- name: Stagwell Plans Pricing
  plan_count: 8
  slug: stagwell-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Stagwell Rate Limits
  slug: stagwell-rate-limits
scopes:
- name: Stagwell Scopes
  scope_count: 0
  slug: stagwell-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 39.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stagwell/refs/heads/main/screenshots/stagwell-2026-06-20T194452.png
security:
- kind: authentication
  name: Stagwell Authentication
  slug: stagwell-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Stagwell Domain Security
  slug: stagwell-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Stagwell Vulnerability Disclosure
  slug: stagwell-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Stagwell Trust Center
  slug: stagwell-trust-center
  summary_line: SOC 2 Type II
slug: stagwell
tags:
- Marketing
- Advertising
- Media
- MarTech
- Influencer Marketing
- Market Research
- Creator Economy
- Public Relations
- Consumer Insights
- Holding Company
website: https://www.stagwellglobal.com
---

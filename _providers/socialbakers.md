---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 24.1
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: Facebook Ads content and metrics
  name: Socialbakers Ads API
  slug: socialbakers-ads-api
- description: Digital asset management — collections and assets
  name: Socialbakers Assets API
  slug: socialbakers-assets-api
- description: Customer care cases and messages
  name: Socialbakers Care API
  slug: socialbakers-care-api
- description: Community content, labeling and engagement metrics
  name: Socialbakers Community API
  slug: socialbakers-community-api
- description: Social listening content and metrics
  name: Socialbakers Listening API
  slug: socialbakers-listening-api
- description: Published content (posts / videos / tweets) per network
  name: Socialbakers Posts API
  slug: socialbakers-posts-api
- description: Time-series and aggregate metrics per social profile
  name: Socialbakers Profile Metrics API
  slug: socialbakers-profile-metrics-api
- description: Managed profiles, labels, label groups, listening queries, ad accounts
  name: Socialbakers Reference API
  slug: socialbakers-reference-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/socialbakers-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.emplifi.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emplifi.io/platform/latest/home
- group: docs
  title: ''
  type: APIReference
  url: https://api.emplifi.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emplifi.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/socialbakers-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/socialbakers-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/socialbakers-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Emplifi
- group: company
  title: ''
  type: Blog
  url: https://emplifi.io/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://emplifi.io/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emplifi.io/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emplifi.io/legal/website-terms-of-use/
created: '2026-07-17'
description: Socialbakers was a pioneering social media analytics and marketing platform (founded 2008 in Prague) that let brands and agencies benchmark, measure and optimize their presence across Facebook, Instagram, X/Twitter, YouTube, LinkedIn, Pinterest, TikTok and Snapchat. In 2021 Socialbakers was acquired by Astute and rebranded to Emplifi, a unified social customer experience platform combining social marketing, commerce and care. The former Socialbakers Public API lives on as the Emplifi Public API (v3) at api.emplifi.io, exposing profile and post metrics, published content, social listening, community engagement, Facebook Ads, digital asset management and customer care data. Authentication is HTTP Basic (API token/secret) or OAuth 2.0 authorization code, with hourly rate limits and cursor-paginated content endpoints.
image: https://base.cdn.emplifi.io/suite/main/favicon.ico
layout: provider
modified: '2026-07-21'
name: Socialbakers
nav: Providers
network: true
overview: 'Socialbakers publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Ads API, Assets API, Care API, and 5 more. Tagged areas include Company, Marketing, Social Media, Analytics, and Social Media Analytics.


  Socialbakers'' developer surface includes documentation, API reference, engineering blog, pricing, and 10 more developer resources.'
random_paper: 52
rate_limits:
- limit_count: 2
  name: Socialbakers Rate Limits
  slug: socialbakers-rate-limits
scopes:
- name: Socialbakers Scopes
  scope_count: 0
  slug: socialbakers-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.2
  delta: 0.2
  facets:
    commercial_clarity: 31.6
    contract_quality: 56.8
    developer_ergonomics: 27.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 42.1
  previous_composite: 42.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Socialbakers Authentication
  slug: socialbakers-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Socialbakers Domain Security
  slug: socialbakers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: socialbakers
tags:
- Company
- Marketing
- Social Media
- Analytics
- Social Media Analytics
- Social Listening
- Marketing Analytics
- Digital Asset Management
- Customer Care
- Emplifi
website: https://api.emplifi.io/
---

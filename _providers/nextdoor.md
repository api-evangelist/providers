---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Nextdoor Agentic Access
  operation_count: 22
  slug: nextdoor-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 6
apis:
- description: Nextdoor developer platform with Advertising, Sharing, and Content Display APIs for connecting with hyperlocal audiences.
  name: Nextdoor
  slug: nextdoor
- description: The Advertising API from Nextdoor — 7 operation(s) for advertising.
  name: Nextdoor Advertising API
  slug: nextdoor-advertising-api
- description: The Conversions API from Nextdoor — 1 operation(s) for conversions.
  name: Nextdoor Conversions API
  slug: nextdoor-conversions-api
- description: The Creatives API from Nextdoor — 4 operation(s) for creatives.
  name: Nextdoor Creatives API
  slug: nextdoor-creatives-api
- description: The Posts API from Nextdoor — 6 operation(s) for posts.
  name: Nextdoor Posts API
  slug: nextdoor-posts-api
- description: The Search API from Nextdoor — 4 operation(s) for search.
  name: Nextdoor Search API
  slug: nextdoor-search-api
artifact_total: 15
collections:
- collection_type: open
  name: Nextdoor Developer API
  slug: open-nextdoor
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nextdoor-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nextdoor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nextdoor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nextdoor-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nextdoor-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nextdoor
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nextdoor-com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nextdoor.com/docs
- group: docs
  title: ''
  type: Reference
  url: https://developer.nextdoor.com/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.nextdoor.com/changelog
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.nextdoor.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.nextdoor.com/rss.xml
created: '2025-02-09'
description: Nextdoor for Developers offers APIs to advertise on, share to, and display content from Nextdoor, the neighborhood-based social network. The developer platform groups capabilities into Advertising APIs (campaign management and measurement), Sharing APIs (Share Plugin and Publish to Nextdoor), and Displaying Content APIs (Trending Posts, Search, and Public Agency Feed).
finops:
- name: Nextdoor Finops
  service_category: API
  slug: nextdoor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nextdoor.png
layout: provider
modified: '2026-04-28'
name: Nextdoor
nav: Providers
network: true
overview: 'Nextdoor publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Advertising API, Conversions API, Creatives API, and 2 more. Tagged areas include Social, Local, Advertising, Community, and Sharing.


  Nextdoor''s developer surface includes authentication, documentation, changelog, engineering blog, and 8 more developer resources.'
plans:
- name: Nextdoor Plans Pricing
  plan_count: 3
  slug: nextdoor-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 5
  name: Nextdoor Rate Limits
  slug: nextdoor-rate-limits
scopes:
- name: Nextdoor Scopes
  scope_count: 11
  slug: nextdoor-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: thin
  composite: 39.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.2
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nextdoor/refs/heads/main/screenshots/nextdoor-2026-06-20T190257.png
security:
- kind: authentication
  name: Nextdoor Authentication
  slug: nextdoor-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nextdoor Domain Security
  slug: nextdoor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nextdoor Vulnerability Disclosure
  slug: nextdoor-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: nextdoor
tags:
- Social
- Local
- Advertising
- Community
- Sharing
---

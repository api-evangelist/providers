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
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Read-only REST API providing programmatic access to the article data behind a Muck Rack Saved Search. Sold as an add-on to Premier-tier subscriptions; authenticated with an organization API key presen
  name: Muck Rack API
  slug: muck-rack-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/muck-rack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://muckrack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.muckrack.com/en/articles/10175260-muck-rack-api
- group: commercial
  title: ''
  type: Pricing
  url: https://muckrack.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://muckrack.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.muckrack.com/en/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://muckrack.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://muckrack.com/privacy
- group: start
  title: ''
  type: Login
  url: https://muckrack.com/account/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/muckrack
- group: operate
  title: ''
  type: StatusPage
  url: https://status.muckrack.com/
- group: auth
  title: ''
  type: Security
  url: https://muckrack.com/responsible-disclosure
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.muckrack.com/
- group: auth
  title: ''
  type: Compliance
  url: conformance/muck-rack-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/muck-rack-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/muck-rack-plans-pricing.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/muck-rack-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/muck-rack-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/muck-rack-data-model.yml
created: '2026-08-26'
description: Muck Rack is a public relations and earned-media software platform that combines a journalist and media-outlet database, media monitoring across news, print, broadcast, social and generative AI engines, pitching and press-release distribution, and executive-ready earned-media reporting. The Muck Rack API is a paid add-on for Premier-tier customers that provides programmatic access to the article data behind a Saved Search, so communications teams can pipe earned coverage into internal systems such as Snowflake or business-intelligence tools such as Power BI and Tableau. API keys are issued by an account Admin under Organization Settings, and the API reference itself is published only to authenticated customers.
image: https://cdn.muckrack.com/static/images/icon_facebook_share.f9886809.jpg
layout: provider
modified: '2026-08-26'
name: Muck Rack
nav: Providers
network: true
overview: 'Muck Rack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Public Relations, Media Monitoring, Media Database, Journalists, and Communications.


  Muck Rack''s developer surface includes documentation, pricing, engineering blog, support, and 15 more developer resources.'
plans:
- name: Muck Rack Plans Pricing
  plan_count: 3
  slug: muck-rack-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Muck Rack Rate Limits
  slug: muck-rack-rate-limits
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 14
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 31.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Muck Rack Authentication
  slug: muck-rack-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Muck Rack Domain Security
  slug: muck-rack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Muck Rack Vulnerability Disclosure
  slug: muck-rack-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Muck Rack Trust Center
  slug: muck-rack-trust-center
  summary_line: SOC 2 Type II, GDPR, CCPA / CPRA, Cloud Security Alliance CAIQ v4 (under NDA)
slug: muck-rack
tags:
- Public Relations
- Media Monitoring
- Media Database
- Journalists
- Communications
- Press Releases
- Earned Media
- Social Listening
- Marketing
- News
- Analytics
- Company
website: https://muckrack.com/
---

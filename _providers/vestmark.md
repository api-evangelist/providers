---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vestmark-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vestmark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vestmark.com/
- group: operate
  title: ''
  type: Support
  url: https://www.vestmark.com/support
- group: start
  title: ''
  type: Login
  url: https://vestmark.my.site.com/Community/s/login/
- group: company
  title: ''
  type: Blog
  url: https://www.vestmark.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vestmark.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vestmark.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vestmark
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/vestmark-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vestmark-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vestmark-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vestmark-llms.txt
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/vestmark_stock/
coverage:
  checked: '2026-08-05'
  detail: Vestmark markets VestmarkONE integrations with 45+ custodian sponsors but serves no developer host at all — developer/api/docs/apis.vestmark.com are NXDOMAIN — and the integration reference lives inside the authenticated Vestmark Client Community on Salesforce Experience Cloud, which answers 401 for every unauthenticated path.
  evidence:
  - status: 200
    url: https://vestmark.my.site.com/Community/s/login/
  - status: 401
    url: https://vestmark.my.site.com/.well-known/agent-card.json
  - status: 404
    url: https://www.vestmark.com/openapi.json
  - status: 404
    url: https://www.vestmark.com/.well-known/api-catalog
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: Vestmark is a Wakefield, Massachusetts wealthtech company that builds VestmarkONE, an enterprise SaaS portfolio management, trading and rebalancing platform for broker-dealers, banks, registered investment advisors and asset managers. The platform covers unified managed accounts, model portfolio management and a model marketplace of 2,000+ strategies from 250+ asset managers, tax-aware trading and overlay, household rebalancing, advisor dashboards, proposal generation, compliance monitoring and client reporting, alongside VAST direct indexing and outsourced investment advisory services delivered by its SEC-registered subsidiary Vestmark Advisory Solutions. Vestmark states the platform supports more than $2T in assets, 5M+ investor accounts and 72K+ financial advisors, and integrates with 45+ custodian sponsors. Vestmark publishes no public developer portal, API reference or machine-readable specification; integration documentation is reachable only inside the authenticated Vestmark
  Client Community.
image: https://vestmark-two-transforms.vestmark.com/production/documents/vestmark-homepage-seo-image.webp?w=1820&h=1024&auto=compress%2Cformat&fit=crop&dm=1756934350&s=9f8d429dd942b0d19cd290bd6f97512c
layout: provider
modified: '2026-08-05'
name: Vestmark
nav: Providers
network: true
overview: 'Vestmark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth Management, WealthTech, Financial Services, and Portfolio Management.


  Vestmark''s developer surface includes support, engineering blog, and 12 more developer resources.'
random_paper: 86
score:
  band: emerging
  composite: 20.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 5.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: domain-security
  name: Vestmark Domain Security
  slug: vestmark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vestmark Vulnerability Disclosure
  slug: vestmark-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: vestmark
tags:
- Company
- Wealth Management
- WealthTech
- Financial Services
- Portfolio Management
- Trading
- Investment Management
- Asset Management
- Managed Accounts
- Direct Indexing
- SaaS
website: https://www.vestmark.com/
---

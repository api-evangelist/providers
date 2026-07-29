---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: 'insurancecouncil.com.au runs on WordPress and leaves the standard WordPress REST API reachable anonymously at /wp-json/, returning JSON for pages, media (the PDF publication corpus of media releases, '
  name: Insurance Council of Australia WordPress REST API
  slug: wordpress-rest-api
- description: A WordPress MCP adapter server route is registered on the ICA estate in the mcp namespace, alongside a wp-abilities/v1 namespace. Namespace discovery at /wp-json/mcp returns HTTP 200 and lists the ada
  name: Insurance Council of Australia WordPress MCP Adapter (gated)
  slug: mcp-adapter
- description: The ICA publishes its news, media releases, catastrophe declarations and resource updates as a standard RSS 2.0 feed at /feed/, served as application/rss+xml. This is the only first-party machine-read
  name: Insurance Council of Australia News RSS Feed
  slug: news-rss-feed
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insurance-council-australia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/insurance-council-australia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/insurance-council-australia-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/insurance-council-australia-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/insurance-council-australia-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/insurance-council-australia-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/insurance-council-australia-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/insurance-council-australia-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/insurance-council-australia-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/insurance-council-australia-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/insurance-council-australia-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/insurance-council-australia-llms.txt
- group: other
  title: ''
  type: DiscoveryDocument
  url: discovery/insurance-council-australia-wp-json-root.json
- group: company
  title: ''
  type: Website
  url: https://insurancecouncil.com.au/
- group: company
  title: ''
  type: About
  url: https://insurancecouncil.com.au/about-us/our-role/
- group: start
  title: ''
  type: Portal
  url: https://memberportal.insurancecouncil.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://insurancecouncil.com.au/industry-members/data-hub/
- group: docs
  title: ''
  type: Documentation
  url: https://insurancecouncil.com.au/code-of-practice/
- group: docs
  title: ''
  type: Documentation
  url: https://insurancecouncil.com.au/news-hub/current-catastrophes/
- group: other
  title: ''
  type: Dataset
  url: https://insurancecouncil.com.au/wp-content/uploads/2026/07/ICA-Historical-Normalised-Catastrophe-Master-Updated-2026_06.xlsx
- group: other
  title: ''
  type: Dataset
  url: https://insurancecouncil.com.au/ica-reports/
- group: company
  title: ''
  type: Blog
  url: https://insurancecouncil.com.au/news-hub/
- group: operate
  title: ''
  type: Support
  url: https://insurancecouncil.com.au/about-us/get-in-touch/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://insurancecouncil.com.au/about-us/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://insurancecouncil.com.au/about-us/disclaimer/
- group: start
  title: ''
  type: Login
  url: https://memberportal.insurancecouncil.com.au/
- group: other
  title: ''
  type: RSSFeed
  url: https://insurancecouncil.com.au/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/insurance-council-of-australia/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/icaus
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/insurancecouncil
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/InsuranceCouncilofAustralia
created: '2026-07-25'
description: 'The Insurance Council of Australia (ICA) is the representative body for Australia''s general insurance industry, whose members write approximately 90% of total premium income for private sector general insurers and reinsurers, spanning home and contents, motor, travel, liability, professional indemnity, commercial property and directors and officers lines. The ICA administers the General Insurance Code of Practice, issues catastrophe and significant event declarations, operates the member Data Hub that reports claim counts, incurred losses and closed rates for declared events, and advocates on resilience, climate risk, building standards and insurance affordability. It is a market body rather than a carrier — it sells no policies and exposes no quote, bind, issue or FNOL API. Its API posture is partner-gated with no public developer program: developer, developers, docs and api subdomains do not resolve, and /developers/, /developer/, /partners/ and /integrations/ all return
  404. The only integration surface is the member portal at memberportal.insurancecouncil.com.au, an Azure AD B2C (OpenID Connect authorization code) login wall for member insurers. Catastrophe and resilience data is published as PDF reports and a downloadable XLSX master file rather than through an API, and no ACORD, AL3 or NGDS reference appears anywhere on the site — Australia''s insurance data seam is the Consumer Data Right, which was designated for general insurance and then deferred.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: Insurance Council Australia Wp V2 Categories
  property_count: 0
  slug: insurance-council-australia-wp-v2-categories
- name: Insurance Council Australia Wp V2 Comments
  property_count: 0
  slug: insurance-council-australia-wp-v2-comments
- name: Insurance Council Australia Wp V2 Media
  property_count: 0
  slug: insurance-council-australia-wp-v2-media
- name: Insurance Council Australia Wp V2 Pages
  property_count: 0
  slug: insurance-council-australia-wp-v2-pages
- name: Insurance Council Australia Wp V2 Search
  property_count: 0
  slug: insurance-council-australia-wp-v2-search
- name: Insurance Council Australia Wp V2 Statuses
  property_count: 0
  slug: insurance-council-australia-wp-v2-statuses
- name: Insurance Council Australia Wp V2 Tags
  property_count: 0
  slug: insurance-council-australia-wp-v2-tags
- name: Insurance Council Australia Wp V2 Taxonomies
  property_count: 0
  slug: insurance-council-australia-wp-v2-taxonomies
- name: Insurance Council Australia Wp V2 Types
  property_count: 0
  slug: insurance-council-australia-wp-v2-types
layout: provider
mcp_servers:
- description: ''
  name: insurance-council-australia-mcp.yml
  slug: insurance-council-australia-mcpyml
modified: '2026-07-25'
name: Insurance Council of Australia
nav: Providers
network: true
overview: 'Insurance Council of Australia publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, General Insurance, Industry Association, and Property and Casualty.


  Insurance Council of Australia''s developer surface includes authentication, developer portal, documentation, engineering blog, support, YouTube channel, and 25 more developer resources.'
random_paper: 1
scopes:
- name: Insurance Council Australia Scopes
  scope_count: 1
  slug: insurance-council-australia-scopes
  summary_line: 1 scope · authorizationCode/implicit
score:
  band: thin
  composite: 34.4
  delta: -2.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 16.1
    developer_ergonomics: 43.5
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 37.1
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/insurance-council-australia/refs/heads/main/screenshots/insurance-council-australia-2026-07-25T222633.png
security:
- kind: authentication
  name: Insurance Council Australia Authentication
  slug: insurance-council-australia-authentication
  summary_line: none/openIdConnect · 3 schemes
- kind: domain-security
  name: Insurance Council Australia Domain Security
  slug: insurance-council-australia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: insurance-council-australia
tags:
- Insurance
- Australia
- General Insurance
- Industry Association
- Property and Casualty
- Claims
- Catastrophe
- Risk Data
- Code of Practice
website: https://insurancecouncil.com.au/
---

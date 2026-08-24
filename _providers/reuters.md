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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Reuters Agentic Access
  operation_count: 5
  slug: reuters-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 4
apis:
- description: Authenticate with Reuters Connect to obtain an authorization token. Tokens are required for all content API calls and should be cached and renewed periodically.
  name: Reuters Authentication API
  slug: reuters-authentication-api
- description: Retrieve available content channels within your subscription. Channels are organized by category including text (TXT), images (PIX), video (VID), and graphics (GFX).
  name: Reuters Channels API
  slug: reuters-channels-api
- description: Retrieve content items from specific channels. Items represent individual pieces of editorial content such as news stories, images, video clips, or graphics.
  name: Reuters Items API
  slug: reuters-items-api
- description: Search for content items across channels using keyword queries. Search supports filtering by headline, channel, date range, and other metadata fields.
  name: Reuters Search API
  slug: reuters-search-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Reuters Connect Authentication API
  slug: open-reuters-authentication-api
- collection_type: open
  name: Reuters Connect Authentication Channels API
  slug: open-reuters-channels-api
- collection_type: open
  name: Reuters Connect API
  slug: open-reuters-connect-api
- collection_type: open
  name: Reuters Connect Authentication Items API
  slug: open-reuters-items-api
- collection_type: open
  name: Reuters Connect Authentication Search API
  slug: open-reuters-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reuters-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/reuters-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reuters-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reuters-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reuters2
- group: docs
  title: ''
  type: Documentation
  url: https://developers.reutersconnect.com/docs
- group: auth
  title: ''
  type: Authentication
  url: https://developers.reutersconnect.com/authentication
- group: company
  title: ''
  type: Blog
  url: https://medium.com/tr-labs-ml-engineering-blog
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/tr-labs-ml-engineering-blog
- group: operate
  title: ''
  type: Support
  url: https://www.reuters.com/info-pages/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reuters.com/info-pages/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thomsonreuters.com/en/privacy-statement.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ReutersMedia
- group: company
  title: ''
  type: Website
  url: https://www.reuters.com
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/reuters/refs/heads/main/openapi/reuters-connect-api-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/reuters/refs/heads/main/vocabulary/reuters-vocabulary.yml
created: '2024-01-01'
description: Global news organization providing breaking news, business, financial, and multimedia content through wire services, digital platforms, and content APIs serving media organizations worldwide. Reuters Connect Web Services provides a professional REST API for searching and retrieving editorial content including text, images, video, and graphics.
examples:
- key_count: 2
  name: Reuters Authenticate Example
  slug: reuters-authenticate-example
- key_count: 2
  name: Reuters List Channels Example
  slug: reuters-list-channels-example
- key_count: 2
  name: Reuters Search Items Example
  slug: reuters-search-items-example
finops:
- name: Reuters Finops
  service_category: API
  slug: reuters-finops
graphqls:
- description: 'Conceptual GraphQL schema for the Reuters Connect API. Reuters Connect Web Services provides a professional REST API for searching and retrieving editorial content — text, images, video, and graphics '
  name: Reuters GraphQL Schema
  slug: reuters-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reuters.png
json_schemas:
- name: Reuters Connect Channel
  property_count: 4
  slug: reuters-channel
- name: Reuters Connect Content Item
  property_count: 17
  slug: reuters-item
- name: Reuters Connect Rendition
  property_count: 8
  slug: reuters-rendition
- name: Reuters Connect Search Result
  property_count: 3
  slug: reuters-search-result
json_structures:
- name: Reuters Connect Api Structure
  property_count: 0
  slug: reuters-connect-api-structure
jsonld:
- class_count: 28
  name: Reuters Context
  property_count: 20
  slug: reuters-context
layout: provider
modified: '2026-05-19'
name: Reuters
nav: Providers
network: true
overview: 'Reuters publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Channels API, Items API, and 1 more. Tagged areas include Business, Finance, Journalism, Media, and News.


  The Reuters catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Reuters'' developer surface includes authentication, documentation, engineering blog, support, and 12 more developer resources.'
plans:
- name: Reuters Plans Pricing
  plan_count: 3
  slug: reuters-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Reuters Rate Limits
  slug: reuters-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Reuters API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 4
  slug: reuters-connect-api-rules
- effective_rule_count: 6
  extends: []
  name: Reuters API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: reuters-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.4
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 69.7
    contract_quality: 75.2
    developer_ergonomics: 15.5
    discoverability: 64.8
    governance: 69.7
    operational_transparency: 10.5
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reuters/refs/heads/main/screenshots/reuters-2026-08-17T125210.png
security:
- kind: authentication
  name: Reuters Authentication
  slug: reuters-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Reuters Domain Security
  slug: reuters-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Reuters Vulnerability Disclosure
  slug: reuters-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: reuters
tags:
- Business
- Finance
- Journalism
- Media
- News
- Wire Service
website: https://www.reuters.com
---

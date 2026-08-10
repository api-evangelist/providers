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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Guardian Agentic Access
  operation_count: 5
  slug: guardian-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: 'Search and retrieve articles, news content, and multimedia from The Guardian''s archive of 2 million+ pieces of content published since 1999. Supports keyword search, section filtering, tag filtering, '
  name: The Guardian Content API
  slug: the-guardian-content-api
- description: Search and retrieve Guardian content items
  name: The Guardian Content API
  slug: guardian-content-api
- description: Browse Guardian editions (UK, US, AU, International, Europe)
  name: The Guardian Editions API
  slug: guardian-editions-api
- description: Browse Guardian sections
  name: The Guardian Sections API
  slug: guardian-sections-api
- description: Browse and search Guardian tags (keywords, series, contributors, etc.)
  name: The Guardian Tags API
  slug: guardian-tags-api
artifact_total: 28
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/guardian-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/guardian-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guardian-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/guardian-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://open-platform.theguardian.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open-platform.theguardian.com/documentation/
- group: other
  title: ''
  type: RegistrationForm
  url: https://open-platform.theguardian.com/access/
- group: operate
  title: ''
  type: Support
  url: https://groups.google.com/g/guardian-api-talk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://open-platform.theguardian.com/legal/terms/
- group: company
  title: ''
  type: Blog
  url: https://www.theguardian.com/info/series/digital-blog/rss
created: '2026-06-13'
description: The Guardian newspaper REST API providing access to 2M+ articles, news content, sections, tags, editions, and real-time breaking news from Guardian journalists worldwide. The API covers all articles published since 1999 and supports advanced search, filtering by section, tag, date range, and edition (UK, US, Australia).
examples:
- key_count: 1
  name: Content Item
  slug: content-item
- key_count: 1
  name: Search Response
  slug: search-response
- key_count: 1
  name: Sections Response
  slug: sections-response
- key_count: 1
  name: Tags Response
  slug: tags-response
finops:
- name: Guardian Finops
  service_category: News & Media Content
  slug: guardian-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/guardian.png
json_schemas:
- name: ContentItem
  property_count: 13
  slug: contentitem
- name: Edition
  property_count: 6
  slug: edition
- name: EditionsResponse
  property_count: 1
  slug: editionsresponse
- name: ErrorResponse
  property_count: 1
  slug: errorresponse
- name: ItemResponse
  property_count: 1
  slug: itemresponse
- name: SearchResponse
  property_count: 1
  slug: searchresponse
- name: Section
  property_count: 5
  slug: section
- name: SectionsResponse
  property_count: 1
  slug: sectionsresponse
- name: Tag
  property_count: 8
  slug: tag
- name: TagsResponse
  property_count: 1
  slug: tagsresponse
jsonld:
- class_count: 7
  name: Guardian Context
  property_count: 29
  slug: guardian-context
layout: provider
modified: '2026-06-13'
name: The Guardian
nav: Providers
network: true
overview: 'The Guardian publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Content API, Editions API, Sections API, and 1 more. Tagged areas include News, Media, Content, Articles, and Journalism.


  The The Guardian catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Guardian''s developer surface includes authentication, documentation, support, engineering blog, and 6 more developer resources.'
plans:
- name: Guardian Plans Pricing
  plan_count: 2
  slug: guardian-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 4
  name: Guardian Rate Limits
  slug: guardian-rate-limits
rules:
- name: The Guardian API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: guardian-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.4
    developer_ergonomics: 26.1
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/guardian/refs/heads/main/screenshots/guardian-2026-06-20T182423.png
security:
- kind: authentication
  name: Guardian Authentication
  slug: guardian-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Guardian Domain Security
  slug: guardian-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Guardian Vulnerability Disclosure
  slug: guardian-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: guardian
tags:
- News
- Media
- Content
- Articles
- Journalism
website: https://open-platform.theguardian.com/
---

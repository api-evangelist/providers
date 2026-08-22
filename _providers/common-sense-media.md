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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Common Sense Media Agentic Access
  operation_count: 4
  slug: common-sense-media-agentic-access
  summary_line: 4 operations
api_count: 2
apis:
- description: 'JSON REST API exposing Common Sense Media''s reviews and ratings catalog. Each review includes recommended age, age-rating group (littleKids/kids/tweens/teens), star rating, content grid (educational, '
  name: Common Sense Media Reviews API
  slug: common-sense-media-reviews-api
- description: System and health endpoints.
  name: Common Sense Media system API
  slug: common-sense-media-system-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Common Sense Media reviews system API
  slug: open-common-sense-media-system-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/common-sense-media-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/common-sense-media-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/common-sense-media-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/commonsense-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/common-sense-media
- group: company
  title: ''
  type: Website
  url: https://www.commonsensemedia.org/
- group: other
  title: ''
  type: DeveloperCenter
  url: https://www.commonsensemedia.org/developers
- group: other
  title: ''
  type: APIOverview
  url: https://www.commonsensemedia.org/developers/api-overview
- group: other
  title: ''
  type: APIv3
  url: https://www.commonsensemedia.org/developers/api/v3
- group: docs
  title: ''
  type: SwaggerUI
  url: https://api.commonsense.org/docs/v3/
- group: docs
  title: ''
  type: ImplementationGuide
  url: https://www.commonsensemedia.org/developers/api/implementation
- group: operate
  title: ''
  type: PartnerProgramContact
  url: https://commonsense.my.site.com/membersupport/s/contactsupport
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commonsensemedia.org/privacy-policy
- group: design
  title: ''
  type: JSONLD
  url: json-ld/common-sense-media-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/common-sense-media-review-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/common-sense-media-rules.yml
created: '2025-03-01'
description: Common Sense Media is a nonprofit organization providing independent, age-rated reviews and ratings of movies, TV shows, books, video games, apps, podcasts, websites, and YouTube channels. The Common Sense Media Reviews API (v3) exposes this catalog via a partner-keyed REST surface hosted at api.commonsense.org/api/v3, with the partnership granted through Common Sense's Business Partner Program. The API is used by parenting apps, smart-TV guides, education platforms, and family- discovery products to surface age-appropriate guidance and the Common Sense Selection award.
finops:
- name: Common Sense Media Finops
  service_category: API
  slug: common-sense-media-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/common-sense-media.png
json_schemas:
- name: Common Sense Media Review
  property_count: 15
  slug: common-sense-media-review
jsonld:
- class_count: 0
  name: Common Sense Media Context
  property_count: 8
  slug: common-sense-media-context
layout: provider
modified: '2026-05-19'
name: Common Sense Media
nav: Providers
network: true
overview: 'Common Sense Media publishes 2 APIs on the [APIs.io](https://apis.io/) network: Reviews API and system API. Tagged areas include Apps, Books, Media, Movies, and Non-Profit.


  The Common Sense Media catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Common Sense Media''s developer surface includes authentication and 15 more developer resources.'
plans:
- name: Common Sense Media Plans Pricing
  plan_count: 3
  slug: common-sense-media-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Common Sense Media Rate Limits
  slug: common-sense-media-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Common Sense Media API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: common-sense-media-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Common Sense Media API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 3
  slug: common-sense-media-rules
score:
  band: thin
  composite: 30.4
  delta: -8.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 61.9
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/common-sense-media/refs/heads/main/screenshots/common-sense-media-2026-06-20T174819.png
security:
- kind: authentication
  name: Common Sense Media Authentication
  slug: common-sense-media-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Common Sense Media Domain Security
  slug: common-sense-media-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: common-sense-media
tags:
- Apps
- Books
- Media
- Movies
- Non-Profit
- Podcasts
- Ratings
- Reviews
- Television
- Video Games
- YouTube
website: https://www.commonsensemedia.org/
---

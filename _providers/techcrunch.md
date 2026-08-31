---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Techcrunch Agentic Access
  operation_count: 15
  slug: techcrunch-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- description: TechCrunch provides RSS feeds covering its full range of technology news, startup coverage, and venture capital reporting. The main feed delivers all published articles, and category-specific feeds ar
  name: TechCrunch RSS Feed
  slug: rss-feed
- description: Author and contributor profiles
  name: TechCrunch Authors API
  slug: techcrunch-authors-api
- description: Post category taxonomy
  name: TechCrunch Categories API
  slug: techcrunch-categories-api
- description: Post comments
  name: TechCrunch Comments API
  slug: techcrunch-comments-api
- description: Media files and attachments
  name: TechCrunch Media API
  slug: techcrunch-media-api
- description: Static page content
  name: TechCrunch Pages API
  slug: techcrunch-pages-api
- description: Article and post content
  name: TechCrunch Posts API
  slug: techcrunch-posts-api
- description: Full-text search across content
  name: TechCrunch Search API
  slug: techcrunch-search-api
- description: Post tag taxonomy
  name: TechCrunch Tags API
  slug: techcrunch-tags-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TechCrunch WordPress REST Authors API
  slug: open-techcrunch-authors-api
- collection_type: open
  name: TechCrunch WordPress REST Authors Categories API
  slug: open-techcrunch-categories-api
- collection_type: open
  name: TechCrunch WordPress REST Authors Comments API
  slug: open-techcrunch-comments-api
- collection_type: open
  name: TechCrunch WordPress REST Authors Media API
  slug: open-techcrunch-media-api
- collection_type: open
  name: TechCrunch WordPress REST Authors Pages API
  slug: open-techcrunch-pages-api
- collection_type: open
  name: TechCrunch WordPress REST Authors Posts API
  slug: open-techcrunch-posts-api
- collection_type: open
  name: TechCrunch WordPress REST Authors Search API
  slug: open-techcrunch-search-api
- collection_type: open
  name: TechCrunch WordPress REST Authors Tags API
  slug: open-techcrunch-tags-api
- collection_type: open
  name: TechCrunch WordPress REST API
  slug: open-techcrunch-wordpress-rest-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/aol/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/techcrunch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/techcrunch-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/techcrunch
- group: company
  title: ''
  type: Website
  url: https://techcrunch.com/
- group: company
  title: ''
  type: About
  url: https://techcrunch.com/about-techcrunch/
- group: company
  title: ''
  type: Newsletter
  url: https://techcrunch.com/newsletters/
- group: other
  title: ''
  type: RSSFeeds
  url: https://techcrunch.com/feed/
- group: other
  title: ''
  type: Advertising
  url: https://techcrunch.com/advertise/
- group: operate
  title: ''
  type: Contact
  url: https://techcrunch.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://techcrunch.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://techcrunch.com/privacy-policy/
- group: other
  title: ''
  type: X
  url: https://x.com/TechCrunch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/techcrunch/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/techcrunch/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/techcrunch/
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/vocabulary/techcrunch-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/json-ld/techcrunch-context.jsonld
created: '2026-03-24'
description: TechCrunch (https://techcrunch.com/) is a leading technology media property dedicated to covering startups, venture capital, and innovation. Founded in 2005 and acquired by AOL in 2010 and later by Yahoo, TechCrunch delivers breaking news, in-depth analysis, and original reporting on the technology industry, emerging companies, funding rounds, and the people shaping the future of tech. The publication hosts flagship events including TechCrunch Disrupt and the Startup Battlefield competition. TechCrunch runs on WordPress and exposes the standard WordPress REST API for programmatic content access.
examples:
- key_count: 2
  name: Techcrunch List Posts Example
  slug: techcrunch-list-posts-example
- key_count: 2
  name: Techcrunch Search Example
  slug: techcrunch-search-example
finops:
- name: Techcrunch Finops
  service_category: API
  slug: techcrunch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/techcrunch.png
json_schemas:
- name: TechCrunch Category
  property_count: 8
  slug: techcrunch-category
- name: TechCrunch Post
  property_count: 21
  slug: techcrunch-post
json_structures:
- name: Techcrunch Post Structure
  property_count: 0
  slug: techcrunch-post-structure
jsonld:
- class_count: 57
  name: Techcrunch Context
  property_count: 0
  slug: techcrunch-context
layout: provider
modified: '2026-05-19'
name: TechCrunch
nav: Providers
network: true
overview: 'TechCrunch publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authors API, Categories API, Comments API, and 5 more. Tagged areas include Media, News, Startups, Technology News, and Venture Capital.


  The TechCrunch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Techcrunch Plans Pricing
  plan_count: 3
  slug: techcrunch-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Techcrunch Rate Limits
  slug: techcrunch-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TechCrunch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: techcrunch-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: TechCrunch API Rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 5
  slug: techcrunch-wordpress-rules
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 36.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 28.8
    contract_quality: 61.9
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/screenshots/techcrunch-2026-06-20T195006.png
security:
- kind: domain-security
  name: Techcrunch Domain Security
  slug: techcrunch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: techcrunch
tags:
- Media
- News
- Startups
- Technology News
- Venture Capital
website: https://techcrunch.com/
---

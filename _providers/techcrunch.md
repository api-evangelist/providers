---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.4
  scored_at: '2026-11-06'
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
- description: 'The public WordPress REST API (wp-json) of the TechCrunch website at techcrunch.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate API'
  name: TechCrunch Website (WordPress REST)
  slug: techcrunch-com-website-wordpress-rest
artifact_total: 16
collections:
- collection_type: open
  name: TechCrunch WordPress REST API
  slug: open-techcrunch-wordpress-rest-api
common:
- group: commercial
  href: https://artifacts.apis.io/techcrunch/plans/techcrunch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/techcrunch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/techcrunch/rate-limits/techcrunch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/techcrunch-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/techcrunch/finops/techcrunch-finops.yml
  title: ''
  type: FinOps
  url: finops/techcrunch-finops.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/aol/
- group: agent
  href: https://artifacts.apis.io/techcrunch/agentic-access/techcrunch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/techcrunch-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/techcrunch/security/techcrunch-domain-security.yml
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
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/json-schema/techcrunch-post-schema.json
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/techcrunch/refs/heads/main/rules/techcrunch-wordpress-rules.yml
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
- has_sources: false
  method: generated
  name: Techcrunch Finops
  primary_unit: request
  service_category: API
  slug: techcrunch-finops
  template: true
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
overview: 'TechCrunch publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Media, News, Startups, Technology News, and Venture Capital.


  The TechCrunch catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Techcrunch Plans Pricing
  plan_count: 3
  slug: techcrunch-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Techcrunch Rate Limits
  slug: techcrunch-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: TechCrunch — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: techcrunch-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: TechCrunch — wordpress rules
  rule_count: 12
  severity_counts:
    error: 5
    hint: 0
    info: 2
    warn: 5
  slug: techcrunch-wordpress-rules
score:
  band: emerging
  composite: 20.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 50.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 27.3
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 20.3
  provenance:
    agentic_access: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/techcrunch/techcrunch-2026-06-20T195006.png
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

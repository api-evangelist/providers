---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dog Ceo Agentic Access
  operation_count: 10
  slug: dog-ceo-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- baseURL: https://dog.ceo/api
  baseurl_source: declared
  description: Operations for fetching images from a specific breed
  name: Dog CEO Breed API
  slug: dog-ceo-breed-api
- baseURL: https://dog.ceo/api
  baseurl_source: declared
  description: Operations for listing all available dog breeds
  name: Dog CEO Breeds API
  slug: dog-ceo-breeds-api
- baseURL: https://dog.ceo/api
  baseurl_source: declared
  description: Operations for fetching random dog images across all breeds
  name: Dog CEO Random API
  slug: dog-ceo-random-api
- baseURL: https://dog.ceo/api
  baseurl_source: declared
  description: Operations for fetching images from a specific sub-breed
  name: Dog CEO Sub-Breed API
  slug: dog-ceo-sub-breed-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dog CEO Breed API
  slug: open-dog-ceo-breed-api
- collection_type: open
  name: Dog CEO Breed Breeds API
  slug: open-dog-ceo-breeds-api
- collection_type: open
  name: Dog CEO Breed Random API
  slug: open-dog-ceo-random-api
- collection_type: open
  name: Dog CEO Breed Sub-Breed API
  slug: open-dog-ceo-sub-breed-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ElliottLandsborough/dog-ceo-api/issues
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dog-ceo/refs/heads/main/agentic-access/dog-ceo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dog-ceo-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dog-ceo/refs/heads/main/security/dog-ceo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dog-ceo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dog.ceo/dog-api/
- group: docs
  title: ''
  type: Documentation
  url: https://dog.ceo/dog-api/documentation/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ElliottLandsborough
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/ElliottLandsborough/dog-ceo-api
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/jigsawpieces/dog-api-images
- group: company
  title: ''
  type: Blog
  url: https://dog.ceo/dog-api/about
- group: commercial
  title: ''
  type: Pricing
  url: https://dog.ceo/dog-api/about
- group: other
  title: ''
  type: X
  url: https://x.com/dog__CEO
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dog-ceo/refs/heads/main/plans/dog-ceo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dog-ceo-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dog-ceo/refs/heads/main/rate-limits/dog-ceo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dog-ceo-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dog-ceo/refs/heads/main/finops/dog-ceo-finops.yml
  title: ''
  type: FinOps
  url: finops/dog-ceo-finops.yml
created: '2026-06-13'
description: Free REST API providing random dog images organized by breed and sub-breed from 120+ breeds. Backed by the Stanford Dogs Dataset and community-contributed photos, Dog CEO is widely used for learning HTTP concepts, API integration practice, and building dog-related applications. No authentication or API key is required. All endpoints return JSON with image URLs served via Vultr CDN. Open-source under the MIT license and community-funded via voluntary donations.
examples:
- key_count: 2
  name: Breed Images
  slug: breed-images
- key_count: 2
  name: Breeds List All
  slug: breeds-list-all
- key_count: 2
  name: Random Image
  slug: random-image
- key_count: 2
  name: Random Images Multiple
  slug: random-images-multiple
- key_count: 2
  name: Sub Breeds List
  slug: sub-breeds-list
finops:
- name: Dog Ceo Finops
  service_category: ''
  slug: dog-ceo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dog-ceo.png
json_schemas:
- name: Dog CEO API Breeds List Response
  property_count: 2
  slug: breeds-list-response
- name: Dog CEO API Image Response
  property_count: 2
  slug: dog-image-response
- name: Dog CEO API Multiple Images Response
  property_count: 2
  slug: dog-images-list-response
jsonld:
- class_count: 5
  name: Dog Ceo Context
  property_count: 5
  slug: dog-ceo-context
layout: provider
modified: '2026-06-13'
name: Dog CEO
nav: Providers
network: true
overview: 'Dog CEO publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Breed API, Breeds API, Random API, and 1 more. Tagged areas include Dogs, Image, Animals, Open Source, and Free API.


  The Dog CEO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dog CEO''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Dog Ceo Plans Pricing
  plan_count: 1
  slug: dog-ceo-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Dog Ceo Rate Limits
  slug: dog-ceo-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Dog CEO API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: dog-ceo-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 65.7
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 37.4
    contract_governance: 9.8
    contract_quality: 52.7
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 24.2
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 10.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/dog-ceo/refs/heads/main/screenshots/dog-ceo-2026-06-20T180123.png
security:
- kind: domain-security
  name: Dog Ceo Domain Security
  slug: dog-ceo-domain-security
  summary_line: TLSv1.3
slug: dog-ceo
tags:
- Dogs
- Image
- Animals
- Open Source
- Free API
- Machine Learning
- Education
website: https://dog.ceo/dog-api/
---

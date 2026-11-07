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
  band: agent-aware
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Meet Agentic Access
  operation_count: 11
  slug: google-meet-agentic-access
  summary_line: 11 operations · 3 acting
api_count: 1
apis:
- baseURL: https://meet.googleapis.com
  baseurl_source: declared
  description: The Google Meet API API from Google Meet — 2 operation(s) for google meet api.
  name: Google Meet Google Meet API
  slug: google-meet-google-meet-api-api
- baseURL: https://meet.googleapis.com
  baseurl_source: declared
  description: The Spaces API from Google Meet — 1 operation(s) for spaces.
  name: Google Meet Spaces API
  slug: google-meet-spaces-api
- baseURL: https://meet.googleapis.com
  baseurl_source: declared
  description: The Conference Records API from Google Meet — 7 operation(s) for conference records.
  name: Google Meet Conference Records API
  slug: google-meet-conference-records-api
artifact_total: 16
collections:
- collection_type: open
  name: Google Meet conferenceRecords API
  slug: open-google-meet-conferencerecords-api
- collection_type: open
  name: Google Meet conferenceRecords Google Meet API API
  slug: open-google-meet-google-meet-api-api
- collection_type: open
  name: Google Meet conferenceRecords Spaces API
  slug: open-google-meet-spaces-api
- collection_type: open
  name: Google Meet API
  slug: open-openapi
common:
- group: commercial
  href: https://artifacts.apis.io/google-meet/plans/google-meet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-meet-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-meet/rate-limits/google-meet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-meet-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-meet/finops/google-meet-finops.yml
  title: ''
  type: FinOps
  url: finops/google-meet-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: agent
  href: https://artifacts.apis.io/google-meet/agentic-access/google-meet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-meet-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-meet/security/google-meet-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-meet-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-meet/security/google-meet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-meet-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/meet/api/guides/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/meet/pricing
- group: design
  href: https://artifacts.apis.io/google-meet/json-ld/json-ld.jsonld
  title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/feeds/posts/default/-/Google%20Meet
created: '2026-03-13'
description: The Google Meet API provides programmatic access to Google Meet video conferencing functionality. It enables applications to create and manage meeting spaces, retrieve conference records including participant details, access recordings and transcripts, and end active conferences. The API supports building integrations that automate meeting workflows and extract meeting data.
finops:
- has_sources: false
  method: generated
  name: Google Meet Finops
  primary_unit: request
  service_category: API
  slug: google-meet-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-meet.png
jsonld:
- class_count: 4
  name: Json Ld Context
  property_count: 6
  slug: json-ld
layout: provider
modified: '2026-09-16'
name: Google Meet
nav: Providers
network: true
overview: 'Google Meet publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Google Meet API, Spaces API, and Conference Records API. Tagged areas include Google, Google Workspace, Meetings, Recording, and Transcripts.


  The Google Meet catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Meet''s developer surface includes getting-started guide, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Google Meet Plans Pricing
  plan_count: 3
  slug: google-meet-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Google Meet Rate Limits
  slug: google-meet-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Google Meet — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-meet-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Google Meet API Rules
  rule_count: 17
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 5
  slug: google-meet-spectral-rules
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.9
    catalog_earned_first_party: 0.0
    catalog_gap: 57.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 52.4
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-meet/google-meet-2026-06-20T182215.png
security:
- kind: domain-security
  name: Google Meet Domain Security
  slug: google-meet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Meet Vulnerability Disclosure
  slug: google-meet-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-meet
tags:
- Google
- Google Workspace
- Meetings
- Recording
- Transcripts
- Video Conferencing
website: https://www.google.com/
---

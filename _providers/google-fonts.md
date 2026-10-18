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
    auth_clarity: bearer
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
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Fonts Agentic Access
  operation_count: 1
  slug: google-fonts-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://www.googleapis.com/webfonts/v1
  baseurl_source: declared
  description: Retrieve font family metadata
  name: Google Fonts Developer Fonts API
  slug: google-fonts-fonts-api
artifact_total: 14
collections:
- collection_type: postman
  name: Google Developer Fonts API
  slug: postman-google-fonts-fonts-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Developer Fonts API
  slug: open-google-fonts-fonts-api
- collection_type: open
  name: Google Fonts Developer API
  slug: open-openapi
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/google-fonts/refs/heads/main/plans/google-fonts-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-fonts-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/google-fonts/refs/heads/main/rate-limits/google-fonts-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-fonts-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/google-fonts/refs/heads/main/finops/google-fonts-finops.yml
  title: ''
  type: FinOps
  url: finops/google-fonts-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-fonts-developer/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/google-fonts/refs/heads/main/agentic-access/google-fonts-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-fonts-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-fonts/refs/heads/main/security/google-fonts-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-fonts-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/google-fonts/refs/heads/main/security/google-fonts-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-fonts-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/google-fonts
- group: start
  title: ''
  type: Portal
  url: https://fonts.google.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/fonts/docs/getting_started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/fonts
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/fonts/docs/developer_api#APIKey
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/fonts/docs/support
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/google-fonts/refs/heads/main/json-ld/google-fonts.jsonld
created: '2026-03-13'
description: The Google Fonts Developer API provides programmatic access to the metadata for all font families served by Google Fonts. Developers can query for available font families, retrieve details about variants, subsets, and categories, access font file URLs, and work with variable font axis metadata. The API supports sorting and filtering to help applications discover and integrate web fonts.
finops:
- has_sources: false
  method: generated
  name: Google Fonts Finops
  primary_unit: ''
  service_category: API
  slug: google-fonts-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-fonts.png
json_schemas:
- name: Google Fonts Developer API Schema
  property_count: 0
  slug: google-fonts
jsonld:
- class_count: 0
  name: Google Fonts Context
  property_count: 9
  slug: google-fonts
layout: provider
modified: '2026-05-19'
name: Google Fonts Developer
nav: Providers
network: true
overview: 'Google Fonts Developer publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Fonts API. Tagged areas include CSS, Design, Fonts, Google Fonts, and Typography.


  The Google Fonts Developer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Fonts Developer''s developer surface includes developer portal, getting-started guide, documentation, authentication, support, and 14 more developer resources.'
plans:
- name: Google Fonts Plans Pricing
  plan_count: 3
  slug: google-fonts-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Google Fonts Rate Limits
  slug: google-fonts-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Fonts Developer — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: google-fonts-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 56.7
    catalog_earned_first_party: 0.0
    catalog_gap: 58.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 51.8
    developer_ergonomics: 44.0
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/google-fonts/refs/heads/main/screenshots/google-fonts-2026-06-20T182204.png
security:
- kind: domain-security
  name: Google Fonts Domain Security
  slug: google-fonts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Fonts Vulnerability Disclosure
  slug: google-fonts-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-fonts
tags:
- CSS
- Design
- Fonts
- Google Fonts
- Typography
- Web Fonts
website: https://www.google.com/
---

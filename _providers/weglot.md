---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.4
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Weglot Agentic Access
  operation_count: 4
  slug: weglot-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.weglot.com
  baseurl_source: declared
  description: The Languages API from Weglot — 2 operation(s) for languages.
  name: Weglot Languages API
  slug: weglot-languages-api
- baseURL: https://api.weglot.com
  baseurl_source: declared
  description: The Status API from Weglot — 1 operation(s) for status.
  name: Weglot Status API
  slug: weglot-status-api
- baseURL: https://api.weglot.com
  baseurl_source: declared
  description: The Translate API from Weglot — 1 operation(s) for translate.
  name: Weglot Translate API
  slug: weglot-translate-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Weglot Translation Languages API
  slug: open-weglot-languages-api
- collection_type: open
  name: Weglot Translation Languages Status API
  slug: open-weglot-status-api
- collection_type: open
  name: Weglot Translation Languages Translate API
  slug: open-weglot-translate-api
- collection_type: open
  name: Weglot Translation API
  slug: open-weglot
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/weglot/refs/heads/main/agentic-access/weglot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/weglot-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/weglot/refs/heads/main/security/weglot-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/weglot-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/weglot/refs/heads/main/security/weglot-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/weglot-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/weglot/refs/heads/main/security/weglot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weglot-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/weglot/refs/heads/main/authentication/weglot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/weglot-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weglot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weglot
- group: company
  title: ''
  type: Website
  url: https://www.weglot.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.weglot.com
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/weglot/refs/heads/main/plans/weglot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/weglot-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/weglot/refs/heads/main/rate-limits/weglot-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/weglot-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/weglot/refs/heads/main/finops/weglot-finops.yml
  title: ''
  type: FinOps
  url: finops/weglot-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.weglot.com/blog
created: '2026-06-21'
description: Weglot is a website translation platform that detects, translates, and displays multilingual content with no code changes. Its REST API at https://api.weglot.com powers machine and human translation of arrays of sentences between languages, exposes the catalog of supported languages, and is the same translation service used by the Weglot JavaScript, WordPress, Shopify, and CMS integrations.
finops:
- name: Weglot Finops
  service_category: Web Services
  slug: weglot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weglot.png
layout: provider
modified: '2026-06-21'
name: Weglot
nav: Providers
network: true
overview: 'Weglot publishes 3 APIs on the [APIs.io](https://apis.io/) network: Languages API, Status API, and Translate API. Tagged areas include Translation, Localization, Internationalization, Machine Translation, and Multilingual.


  Weglot''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Weglot Plans Pricing
  plan_count: 7
  slug: weglot-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Weglot Rate Limits
  slug: weglot-rate-limits
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 61.6
    catalog_earned_first_party: 0.0
    catalog_gap: 53.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 44.2
    contract_governance: 0.0
    contract_quality: 47.3
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 31.1
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/weglot/refs/heads/main/screenshots/weglot-2026-09-02T170606.png
security:
- kind: authentication
  name: Weglot Authentication
  slug: weglot-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Weglot Domain Security
  slug: weglot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Weglot Vulnerability Disclosure
  slug: weglot-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Weglot Trust Center
  slug: weglot-trust-center
  summary_line: SOC 2, GDPR
slug: weglot
tags:
- Translation
- Localization
- Internationalization
- Machine Translation
- Multilingual
website: https://www.weglot.com
---

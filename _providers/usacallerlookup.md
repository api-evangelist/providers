---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-09-20'
api_count: 1
apis:
- baseURL: https://www.usacallerlookup.com/wp-json/ucl/v1
  baseurl_source: declared
  description: Aggregate figures for one area code
  name: USACallerLookup Area codes API
  slug: usacallerlookup-area-codes-api
- baseURL: https://www.usacallerlookup.com/wp-json/ucl/v1
  baseurl_source: declared
  description: Headline figures for the whole dataset
  name: USACallerLookup Dataset API
  slug: usacallerlookup-dataset-api
- baseURL: https://www.usacallerlookup.com/wp-json/ucl/v1
  baseurl_source: declared
  description: Per-number carrier, location and complaint profile
  name: USACallerLookup Numbers API
  slug: usacallerlookup-numbers-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.usacallerlookup.com/
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/openapi/_original/usacallerlookup-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/usacallerlookup-openapi.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/llms/usacallerlookup-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/usacallerlookup-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/packages/usacallerlookup-packages.yml
  title: ''
  type: Packages
  url: packages/usacallerlookup-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/packages/usacallerlookup-packages.yml
  title: ''
  type: SDKs
  url: packages/usacallerlookup-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/authentication/usacallerlookup-authentication.yml
  title: ''
  type: Authentication
  url: authentication/usacallerlookup-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/rate-limits/usacallerlookup-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/usacallerlookup-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/plans/usacallerlookup-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/usacallerlookup-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/errors/usacallerlookup-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/usacallerlookup-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/conventions/usacallerlookup-conventions.yml
  title: ''
  type: Conventions
  url: conventions/usacallerlookup-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/data-model/usacallerlookup-data-model.yml
  title: ''
  type: DataModel
  url: data-model/usacallerlookup-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/conformance/usacallerlookup-conformance.yml
  title: ''
  type: Conformance
  url: conformance/usacallerlookup-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/lifecycle/usacallerlookup-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/usacallerlookup-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/security/usacallerlookup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usacallerlookup-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/usacallerlookup/refs/heads/main/overlays/usacallerlookup-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/usacallerlookup-openapi-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://www.usacallerlookup.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.usacallerlookup.com/api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usacallerlookup.com/terms-conditions/
- group: company
  title: ''
  type: Blog
  url: https://www.usacallerlookup.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.usacallerlookup.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.usacallerlookup.com/faq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/usacallerlookup
created: '2026-09-14'
description: A free, read-only JSON REST API over US phone-numbering data and FTC robocall complaint records. No API key or signup required; access is throttled at 60 requests/minute per IP. Data is sourced from FTC Do Not Call complaints and the NANPA registry and dedicated to the public domain under CC0.
image: https://www.usacallerlookup.com/favicon.ico
layout: provider
modified: '2026-09-16'
name: USACallerLookup
nav: Providers
network: true
overview: 'USACallerLookup publishes 3 APIs on the [APIs.io](https://apis.io/) network: Area codes API, Dataset API, and Numbers API. Tagged areas include Phone Lookup, Caller ID, robocall, FTC, and Telecom.


  USACallerLookup''s developer surface includes authentication, documentation, API reference, engineering blog, support, and 18 more developer resources.'
plans:
- name: Usacallerlookup Plans Pricing
  plan_count: 0
  slug: usacallerlookup-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Usacallerlookup Rate Limits
  slug: usacallerlookup-rate-limits
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 44.6
    discoverability: 75.9
    operational_transparency: 23.7
  previous_composite: 36.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 29.2
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Usacallerlookup Authentication
  slug: usacallerlookup-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Usacallerlookup Domain Security
  slug: usacallerlookup-domain-security
  summary_line: TLSv1.3 · DMARC
slug: usacallerlookup
tags:
- Phone Lookup
- Caller ID
- robocall
- FTC
- Telecom
- Open Data
- Anti-Fraud
website: https://www.usacallerlookup.com/
---

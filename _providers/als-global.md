---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Als Global Agentic Access
  operation_count: 6
  slug: als-global-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- description: API layer from ALS Solutions that lets existing clients connect registration, LIMS and reporting systems to ALS to send sample registration data, retrieve results automatically and download certificat
  name: ALS Global Integration Platform
  slug: global-integration-platform
- baseURL: https://api.alstribology.com
  baseurl_source: declared
  description: The Preference API from ALS — 1 operation(s) for preference.
  name: ALS Preference API
  slug: als-global-preference-api
- baseURL: https://api.alstribology.com
  baseurl_source: declared
  description: The Sample API from ALS — 3 operation(s) for sample.
  name: ALS Sample API
  slug: als-global-sample-api
- baseURL: https://api.alstribology.com
  baseurl_source: declared
  description: The Search API from ALS — 2 operation(s) for search.
  name: ALS Search API
  slug: als-global-search-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/als-global/agentic-access/als-global-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/als-global-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/als-global/rate-limits/als-global-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/als-global-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/als-global/rules/als-global-rules.yml
  title: ''
  type: Spectral
  url: rules/als-global-rules.yml
- group: design
  href: https://artifacts.apis.io/als-global/vocabulary/als-global-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/als-global-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/als-global/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/als-global/data-model/als-global-data-model.yml
  title: ''
  type: DataModel
  url: data-model/als-global-data-model.yml
- group: design
  href: https://artifacts.apis.io/als-global/conventions/als-global-conventions.yml
  title: ''
  type: Conventions
  url: conventions/als-global-conventions.yml
- group: design
  href: https://artifacts.apis.io/als-global/lifecycle/als-global-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/als-global-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/als-global/errors/als-global-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/als-global-problem-types.yml
- group: design
  href: https://artifacts.apis.io/als-global/conformance/als-global-conformance.yml
  title: ''
  type: Conformance
  url: conformance/als-global-conformance.yml
- group: other
  href: https://artifacts.apis.io/als-global/overlays/als-global-webtrieve-export-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/als-global-webtrieve-export-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/als-global/llms/als-global-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/als-global-llms.txt
- group: other
  href: https://artifacts.apis.io/als-global/hosts/als-global-hosts.yml
  title: ''
  type: Hosts
  url: hosts/als-global-hosts.yml
- group: other
  href: https://artifacts.apis.io/als-global/vendors/als-global-vendors.yml
  title: ''
  type: Vendors
  url: vendors/als-global-vendors.yml
- group: auth
  href: https://artifacts.apis.io/als-global/authentication/als-global-authentication.yml
  title: ''
  type: Authentication
  url: authentication/als-global-authentication.yml
- group: auth
  href: https://artifacts.apis.io/als-global/security/als-global-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/als-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alsglobal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.alsglobal.com/global-integration-platform
- group: start
  title: ''
  type: SignUp
  url: https://www.alsglobal.com/portal---activate-global-integration
- group: start
  title: ''
  type: Login
  url: https://solutions.alsglobal.com/
- group: start
  title: ''
  type: Portal
  url: https://www.alsglobal.com/all-client-portals
- group: operate
  title: ''
  type: Support
  url: https://www.alsglobal.com/contact-us
- group: company
  title: ''
  type: About
  url: https://www.alsglobal.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.alsglobal.com/food-insights-blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.alsglobal.com/news-and-media-global
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.alsglobal.com/investor-relations
- group: company
  title: ''
  type: Careers
  url: https://www.alsglobal.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alsglobal.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alsglobal.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/als
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC9GTzaPtpqJYG7Gzdc7bygw
created: '2026-10-21'
description: ALS (ALS Limited, alsglobal.com) is a global provider of laboratory testing, inspection, certification and verification solutions, serving environmental, equipment reliability (oil and tribology), food and agrisciences, mining and commodities (geochemistry), beauty and personal care, and pharmaceutical and healthcare clients. It operates client data portals such as ALS Solutions and Webtrieve, and its Global Integration Platform adds a credential-gated API layer to an ALS Solutions account so client registration, LIMS and reporting systems can exchange sample registrations, results and certificates; endpoint documentation is provided by client support on activation.
image: https://edge.sitecorecloud.io/alsgroupusa347e-alsgroup8904-alsglobalpr1dd3-c9a5/media/alsglobal/header/logo.png
layout: provider
modified: '2026-10-21'
name: ALS
nav: Providers
network: true
overview: 'ALS publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Preference API, Sample API, Search API, and 1 more. Tagged areas include Company, Laboratory Testing, Environmental Testing, Inspection, and Certification.


  The ALS catalog on APIs.io includes 1 Spectral governance ruleset.


  ALS''s developer surface includes authentication, documentation, signup flow, developer portal, support, engineering blog, YouTube channel, and 24 more developer resources.'
plans:
- name: Als Global Plans Pricing
  plan_count: 0
  slug: als-global-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Als Global Rate Limits
  slug: als-global-rate-limits
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: ALS API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: als-global-rules
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 45.8
    catalog_earned_first_party: 8.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 42.0
    developer_ergonomics: 39.9
    discoverability: 58.9
    operational_transparency: 21.1
  previous_composite: 38.0
  provenance:
    agentic_access: derived
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Als Global Authentication
  slug: als-global-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Als Global Domain Security
  slug: als-global-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: export-sample-results
  slug: als-global-export-sample-results
- name: submit-oil-samples
  slug: als-global-submit-oil-samples
slug: als-global
tags:
- Company
- Laboratory Testing
- Environmental Testing
- Inspection
- Certification
- Geochemistry
- Food Testing
- LIMS Integration
website: https://www.alsglobal.com/
---

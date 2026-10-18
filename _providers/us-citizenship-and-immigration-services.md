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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Us Citizenship And Immigration Services Agentic Access
  operation_count: 3
  slug: us-citizenship-and-immigration-services-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 2
apis:
- baseURL: https://api-int.uscis.gov/case-status
  baseurl_source: declared
  description: Immigration case status retrieval by receipt number
  name: US Citizenship and Immigration Services Case Status API
  slug: us-citizenship-and-immigration-services-case-status-api
- baseURL: https://api-int.uscis.gov/case-status
  baseurl_source: declared
  description: Submit and manage FOIA and Privacy Act requests for Alien File records
  name: US Citizenship and Immigration Services FOIA Requests API
  slug: us-citizenship-and-immigration-services-foia-requests-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USCIS Case Status API
  slug: open-us-citizenship-and-immigration-services-case-status-api
- collection_type: open
  name: USCIS Case Status FOIA Requests API
  slug: open-us-citizenship-and-immigration-services-foia-requests-api
- collection_type: open
  name: USCIS Case Status API
  slug: open-uscis-case-status-api
- collection_type: open
  name: USCIS FOIA Request and Status API
  slug: open-uscis-foia-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/plans/us-citizenship-and-immigration-services-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/us-citizenship-and-immigration-services-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/rate-limits/us-citizenship-and-immigration-services-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/us-citizenship-and-immigration-services-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/finops/us-citizenship-and-immigration-services-finops.yml
  title: ''
  type: FinOps
  url: finops/us-citizenship-and-immigration-services-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/capabilities/us-citizenship-and-immigration-services-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/us-citizenship-and-immigration-services-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/agentic-access/us-citizenship-and-immigration-services-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/us-citizenship-and-immigration-services-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/security/us-citizenship-and-immigration-services-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/us-citizenship-and-immigration-services-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/authentication/us-citizenship-and-immigration-services-authentication.yml
  title: ''
  type: Authentication
  url: authentication/us-citizenship-and-immigration-services-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/scopes/us-citizenship-and-immigration-services-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/us-citizenship-and-immigration-services-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uscis
created: '2024-12-03'
description: The US Citizenship and Immigration Services (USCIS) is a government agency responsible for overseeing lawful immigration to the United States. Its primary function is to process and adjudicate applications for various immigration benefits, such as green cards, work permits, and naturalization. USCIS provides a public developer portal (developer.uscis.gov) with APIs for case status lookup and FOIA request submission. The Torch API Program enables qualified software developers to integrate USCIS services into immigration case management applications, providing OAuth 2.0 secured access to case status information and Freedom of Information Act (FOIA) request capabilities.
examples:
- key_count: 2
  name: Uscis Get Case Status Example
  slug: uscis-get-case-status-example
- key_count: 2
  name: Uscis Submit Foia Request Example
  slug: uscis-submit-foia-request-example
finops:
- has_sources: false
  method: generated
  name: Us Citizenship And Immigration Services Finops
  primary_unit: ''
  service_category: API
  slug: us-citizenship-and-immigration-services-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-citizenship-and-immigration-services.png
json_schemas:
- name: USCIS Case Status
  property_count: 8
  slug: uscis-case-status
json_structures:
- name: Uscis Case Status Structure
  property_count: 0
  slug: uscis-case-status-structure
jsonld:
- class_count: 1
  name: Us Citizenship And Immigration Services Context
  property_count: 25
  slug: us-citizenship-and-immigration-services-context
layout: provider
modified: '2026-05-19'
name: US Citizenship and Immigration Services
nav: Providers
network: true
overview: 'US Citizenship and Immigration Services publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Case Status API and FOIA Requests API. Tagged areas include Federal Government, Immigration, Citizenship, Case Status, and FOIA.


  The US Citizenship and Immigration Services catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US Citizenship and Immigration Services'' developer surface includes authentication and 8 more developer resources.'
plans:
- name: Us Citizenship And Immigration Services Plans Pricing
  plan_count: 3
  slug: us-citizenship-and-immigration-services-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Us Citizenship And Immigration Services Rate Limits
  slug: us-citizenship-and-immigration-services-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: US Citizenship and Immigration Services — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-citizenship-and-immigration-services-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 12
  extends: []
  name: US Citizenship and Immigration Services — uscis api rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 8
  slug: uscis-api-rules
scopes:
- name: Us Citizenship And Immigration Services Scopes
  scope_count: 3
  slug: us-citizenship-and-immigration-services-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.3
    catalog_earned_first_party: 0.0
    catalog_gap: 60.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 7.9
    contract_governance: 9.8
    contract_quality: 59.3
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 26.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/us-citizenship-and-immigration-services/refs/heads/main/screenshots/us-citizenship-and-immigration-services-2026-06-20T200606.png
security:
- kind: authentication
  name: Us Citizenship And Immigration Services Authentication
  slug: us-citizenship-and-immigration-services-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Us Citizenship And Immigration Services Domain Security
  slug: us-citizenship-and-immigration-services-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: us-citizenship-and-immigration-services
tags:
- Federal Government
- Immigration
- Citizenship
- Case Status
- FOIA
---

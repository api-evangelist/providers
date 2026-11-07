---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://public-api.cloverhealth.com
  baseurl_source: declared
  description: The fhir-r4-formulary-api API from Clover Health — 5 operation(s) for fhir-r4-formulary-api.
  name: Clover Health Fhir R4 Formulary API
  slug: clover-health-fhir-r4-formulary-api-api
- baseURL: https://public-api.cloverhealth.com
  baseurl_source: declared
  description: The FHIR R4 ProviderDirectory API API from Clover Health — 17 operation(s) for fhir r4 providerdirectory api.
  name: Clover Health FHIR R4 ProviderDirectory API
  slug: clover-health-fhir-r4-providerdirectory-api-api
artifact_total: 10
collections:
- collection_type: open
  name: FHIR fhir-r4-formulary-api API
  slug: open-clover-health-fhir-r4-formulary-api-api
- collection_type: open
  name: FHIR fhir-r4-formulary-api FHIR R4 ProviderDirectory API API
  slug: open-clover-health-fhir-r4-providerdirectory-api-api
common:
- group: company
  title: ''
  type: Blog
  url: https://www.cloverhealth.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cloverhealth.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://public-api.cloverhealth.com/swagger
- group: docs
  title: ''
  type: APIReference
  url: https://public-api.cloverhealth.com/swagger
- group: start
  title: ''
  type: SignUp
  url: https://docs.google.com/forms/d/1qhbMWXYYn3lpBg8026mW20rxGHE9SL2sHNLzVoyOS0g/edit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloverhealth.com/developers/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloverhealth.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:api-support@cloverhealth.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CloverHealth
- group: docs
  href: https://artifacts.apis.io/clover-health/openapi/_original/clover-health-fhir-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/clover-health-fhir-openapi-original.yml
- group: other
  href: https://artifacts.apis.io/clover-health/overlays/clover-health-fhir-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clover-health-fhir-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/clover-health/authentication/clover-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clover-health-authentication.yml
- group: design
  href: https://artifacts.apis.io/clover-health/conventions/clover-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clover-health-conventions.yml
- group: design
  href: https://artifacts.apis.io/clover-health/data-model/clover-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clover-health-data-model.yml
- group: design
  href: https://artifacts.apis.io/clover-health/conformance/clover-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clover-health-conformance.yml
- group: design
  href: https://artifacts.apis.io/clover-health/lifecycle/clover-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clover-health-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/clover-health/mcp/clover-health-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/clover-health-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clover-health/llms/clover-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clover-health-llms.txt
- group: agent
  href: https://artifacts.apis.io/clover-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/clover-health/well-known/clover-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clover-health-well-known.yml
- group: auth
  href: https://artifacts.apis.io/clover-health/well-known/clover-health-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clover-health-security.txt
- group: auth
  href: https://artifacts.apis.io/clover-health/security/clover-health-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clover-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cloverhealth.com/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/clover-health/security/clover-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clover-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloverhealth.com
created: '2026-07-17'
description: Clover Health is a Medicare Advantage health insurer that runs a public developer program built on healthcare interoperability standards. Its public FHIR R4 API exposes a Formulary service (covered drugs, tiers, and utilization management) and a Provider Directory service (practitioners, organizations, locations, healthcare services, and insurance plans), and a separate consent-based Patient Access API delivers a member's clinical and claims data in FHIR-native format via CareEvolution. The APIs implement the CMS Interoperability and Patient Access final rule (CMS-9115-F); Clover was the first payer to go live on a CMS-aligned/TEFCA network. Developers register for approved credentials and authenticate with HTTP Basic or a session cookie.
image: https://cdn.cloverhealth.com/filer_cloudrun_public/img/live-tile-large-310x310.png
layout: provider
modified: '2026-10-06'
name: Clover Health
nav: Providers
network: true
overview: 'Clover Health publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Fhir R4 Formulary API and FHIR R4 ProviderDirectory API. Tagged areas include Company, Healthcare, Health Insurance, Medicare Advantage, and FHIR.


  The Clover Health catalog on APIs.io includes 1 Spectral governance ruleset.


  Clover Health''s developer surface includes engineering blog, documentation, API reference, signup flow, support, authentication, and 19 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Clover Health API Rules
  rule_count: 46
  severity_counts:
    error: 37
    hint: 0
    info: 2
    warn: 7
  slug: clover-health-rules
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 49.7
    developer_ergonomics: 47.0
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 41.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 34.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/clover-health/clover-health-2026-07-25T205721.png
security:
- kind: authentication
  name: Clover Health Authentication
  slug: clover-health-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Clover Health Domain Security
  slug: clover-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clover Health Vulnerability Disclosure
  slug: clover-health-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: Check drug coverage in the Clover Health formulary
  slug: clover-health-formulary-lookup
- name: Find an in-network provider (Clover Health)
  slug: clover-health-provider-directory-search
slug: clover-health
tags:
- Company
- Healthcare
- Health Insurance
- Medicare Advantage
- FHIR
- Interoperability
- Provider Directory
- Formulary
- Patient Access
- Payers
website: https://www.cloverhealth.com
---

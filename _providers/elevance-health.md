---
access_model:
  confidence: high
  label: Free, registration and approval required
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - sandbox
  - https://www.anthem.com/developers
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Elevance Health Agentic Access
  operation_count: 10
  slug: elevance-health-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- description: 'The Patient Access API gives Elevance Health members, through an application they authorize, up to five years of their medical, pharmacy, dental and vision claims and clinical data. It is HL7 FHIR R4 '
  name: Elevance Health Patient Access API
  slug: patient-access
- description: The Provider Directory API exposes which practitioners and organizations are in-network for a given Elevance Health insurance plan. HL7 FHIR R4 conforming to Da Vinci PDEX Plan Net 1.1.0 and US Core S
  name: Elevance Health Provider Directory API
  slug: provider-directory
- description: The Formulary API publishes drug coverage for Elevance-affiliated Medicare, Medicaid and CHIP plans — covered drug lists, tier placement, pharmacy type and cost-sharing. HL7 FHIR R4 conforming to Da V
  name: Elevance Health Formulary API
  slug: formulary
- baseURL: https://patient360.anthem.com/P360Member/api/fhir
  baseurl_source: declared
  description: The Claims API from Elevance Health — 3 operation(s) for claims.
  name: Elevance Health Claims API
  slug: elevance-health-claims-api
- baseURL: https://patient360.anthem.com/P360Member/api/fhir
  baseurl_source: declared
  description: The Conformance API from Elevance Health — 1 operation(s) for conformance.
  name: Elevance Health Conformance API
  slug: elevance-health-conformance-api
- baseURL: https://patient360.anthem.com/P360Member/api/fhir
  baseurl_source: declared
  description: The Coverage API from Elevance Health — 2 operation(s) for coverage.
  name: Elevance Health Coverage API
  slug: elevance-health-coverage-api
- baseURL: https://patient360.anthem.com/P360Member/api/fhir
  baseurl_source: declared
  description: The Patient API from Elevance Health — 2 operation(s) for patient.
  name: Elevance Health Patient API
  slug: elevance-health-patient-api
- baseURL: https://patient360.anthem.com/P360Member/api/fhir
  baseurl_source: declared
  description: The Provider Directory API from Elevance Health — 2 operation(s) for provider directory.
  name: Elevance Health Provider Directory API
  slug: elevance-health-provider-directory-api
artifact_total: 25
collections:
- collection_type: open
  name: Elevance Health Patient Access FHIR Claims API
  slug: open-elevance-health-claims-api
- collection_type: open
  name: Elevance Health Patient Access FHIR Claims Conformance API
  slug: open-elevance-health-conformance-api
- collection_type: open
  name: Elevance Health Patient Access FHIR Claims Coverage API
  slug: open-elevance-health-coverage-api
- collection_type: open
  name: Elevance Health Access FHIR Claims Patient API
  slug: open-elevance-health-patient-api
- collection_type: open
  name: Elevance Health Patient Access FHIR Claims Provider Directory API
  slug: open-elevance-health-provider-directory-api
- collection_type: open
  name: Elevance Health Patient Access FHIR API
  slug: open-elevance-health
common:
- group: commercial
  href: https://artifacts.apis.io/elevance-health/finops/elevance-health-finops.yml
  title: ''
  type: FinOps
  url: finops/elevance-health-finops.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://www.anthem.com/developers
- group: start
  title: ''
  type: SignUp
  url: https://www.anthem.com/developers/request-anthem-io
- group: operate
  title: ''
  type: Support
  url: https://www.anthem.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.anthem.com/blog
- group: start
  title: ''
  type: Portal
  url: https://www.anthem.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openanthem
- group: other
  href: https://artifacts.apis.io/elevance-health/capabilities/elevance-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/elevance-health-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/elevance-health/agentic-access/elevance-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elevance-health-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/elevance-health/security/elevance-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elevance-health-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/elevance-health/authentication/elevance-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elevance-health-authentication.yml
- group: auth
  href: https://artifacts.apis.io/elevance-health/scopes/elevance-health-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/elevance-health-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elevance-health
- group: company
  title: ''
  type: Website
  url: https://www.elevancehealth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.anthem.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://patient360c.anthem.com/P360Member/fhir/documentation
- group: start
  title: ''
  type: Signup
  url: https://www.anthem.com/developers/request-anthem-io
- group: design
  href: https://artifacts.apis.io/elevance-health/conformance/elevance-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elevance-health-conformance.yml
- group: agent
  href: https://artifacts.apis.io/elevance-health/well-known/elevance-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elevance-health-well-known.yml
- group: design
  href: https://artifacts.apis.io/elevance-health/conventions/elevance-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elevance-health-conventions.yml
- group: design
  href: https://artifacts.apis.io/elevance-health/errors/elevance-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elevance-health-problem-types.yml
- group: design
  href: https://artifacts.apis.io/elevance-health/lifecycle/elevance-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elevance-health-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/elevance-health/changelog/elevance-health-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elevance-health-changelog.yml
- group: design
  href: https://artifacts.apis.io/elevance-health/data-model/elevance-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elevance-health-data-model.yml
- group: start
  href: https://artifacts.apis.io/elevance-health/sandbox/elevance-health-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/elevance-health-sandbox.yml
- group: build
  href: https://artifacts.apis.io/elevance-health/packages/elevance-health-packages.yml
  title: ''
  type: Packages
  url: packages/elevance-health-packages.yml
- group: commercial
  href: https://artifacts.apis.io/elevance-health/plans/elevance-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elevance-health-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/elevance-health/rate-limits/elevance-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elevance-health-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/elevance-health/llms/elevance-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elevance-health-llms.txt
- group: agent
  href: https://artifacts.apis.io/elevance-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/elevance-health/mcp/elevance-health-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/elevance-health-mcp.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.anthem.com/content/dam/digital/developers-portal/Anthem-IOProviderDirectoryAndFormulary-API-Documentation.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anthem.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elevancehealth.com/privacy-policy
created: '2026-03-21'
description: 'Elevance Health (formerly Anthem) is a Fortune 500 health benefits company serving members through Blue Cross and Blue Shield affiliated health plans across multiple states, offering medical, pharmacy, dental, vision and specialty insurance. Its entire public API surface is HL7 FHIR, published to satisfy the CMS Interoperability and Patient Access Final Rule: a member-consented Patient Access API (FHIR R4, CARIN Blue Button, SMART on FHIR), a read-only Provider Directory API (Da Vinci PDEX Plan Net) whose CapabilityStatement is readable with no credentials, a Formulary API (Da Vinci PDEX US Drug Formulary), and a legacy Patient360 FHIR DSTU2 endpoint running CareEvolution HIEBus. There is no OpenAPI, no SDK and no pricing — the contracts are the FHIR CapabilityStatements the servers publish about themselves. Elevance has committed in its own endpoint support document to shipping Payer-to-Payer, Prior Authorization and Provider Access APIs by 1 January 2027 under CMS-0057-F;
  none of the three exists today.'
finops:
- has_sources: true
  method: derived
  name: Elevance Health Finops
  primary_unit: ''
  service_category: ''
  slug: elevance-health-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elevance-health.png
layout: provider
modified: '2026-09-07'
name: Elevance Health
nav: Providers
network: true
overview: 'Elevance Health publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Claims API, Conformance API, Coverage API, and 5 more. Tagged areas include Fortune 500, Healthcare, Health Insurance, FHIR, and Interoperability.


  The Elevance Health catalog on APIs.io includes 1 Spectral governance ruleset.


  Elevance Health''s developer surface includes getting-started guide, signup flow, support, engineering blog, developer portal, authentication, documentation, and 27 more developer resources.'
plans:
- name: Elevance Health Plans Pricing
  plan_count: 0
  slug: elevance-health-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Elevance Health Rate Limits
  slug: elevance-health-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Elevance Health API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: elevance-health-rules
scopes:
- name: Elevance Health Scopes
  scope_count: 272
  slug: elevance-health-scopes
  summary_line: 272 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 22.4
    contract_governance: 31.8
    contract_quality: 51.3
    developer_ergonomics: 51.8
    discoverability: 66.1
    operational_transparency: 18.4
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: carin-blue-button
    - jurisdiction: US
      standard: da-vinci
    - jurisdiction: US
      standard: us-core
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 48.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/elevance-health/elevance-health-2026-06-20T180559.png
security:
- kind: authentication
  name: Elevance Health Authentication
  slug: elevance-health-authentication
  summary_line: oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Elevance Health Domain Security
  slug: elevance-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: elevance-health-discover-fhir-capabilities
  slug: elevance-health-discover-fhir-capabilities
- name: elevance-health-retrieve-member-claims
  slug: elevance-health-retrieve-member-claims
- name: elevance-health-search-provider-directory
  slug: elevance-health-search-provider-directory
slug: elevance-health
tags:
- Fortune 500
- Healthcare
- Health Insurance
- FHIR
- Interoperability
- CMS Interoperability
- SMART on FHIR
- Da Vinci PDEX
- CARIN Blue Button
- Payers
- Provider Directory
- Formulary
- HL7
website: https://www.elevancehealth.com
---

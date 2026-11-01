---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
  score: 25.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Moxe Health Agentic Access
  operation_count: 4
  slug: moxe-health-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 4
apis:
- baseURL: https://int-api.moxehealth.com/chart-retrieval
  baseurl_source: declared
  description: The Claims API from Moxe Health — 2 operation(s) for claims.
  name: Moxe Health Claims API
  slug: moxe-health-claims-api
- baseURL: https://int-api.moxehealth.com/chart-retrieval
  baseurl_source: declared
  description: The Patient API from Moxe Health — 2 operation(s) for patient.
  name: Moxe Health Patient API
  slug: moxe-health-patient-api
arazzos:
- description: Initiate a claim-management request to retrieve the clinical chart supporting a specific claim, then poll the status endpoint with the returned moxeRequestId.
  name: Request a claim-supporting chart and poll for status
  slug: moxe-health-request-claim-chart
- description: Initiate a release-of-information request for a patient's clinical chart, then poll the status endpoint with the returned moxeRequestId until Moxe delivers the chart via SFTP.
  name: Request a patient chart and poll for status
  slug: moxe-health-request-patient-chart
artifact_total: 19
collections:
- collection_type: open
  name: Chart Retrieval API
  slug: open-moxe-health-chart-retrieval-initiate
- collection_type: open
  name: Chart Retrieval API
  slug: open-moxe-health-chart-retrieval-status
- collection_type: open
  name: Chart Retrieval API
  slug: open-moxe-health-claim-management-initiate
- collection_type: open
  name: Chart Retrieval API
  slug: open-moxe-health-claim-management-status
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://moxehealth.com/feed/
- group: other
  href: https://artifacts.apis.io/moxe-health/capabilities/moxe-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/moxe-health-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/moxe-health/security/moxe-health-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/moxe-health-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/moxe-health/security/moxe-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moxe-health-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/moxe-health/agentic-access/moxe-health-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moxe-health-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/moxe-health/scopes/moxe-health-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/moxe-health-scopes.yml
- group: auth
  href: https://artifacts.apis.io/moxe-health/authentication/moxe-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/moxe-health-authentication.yml
- group: design
  href: https://artifacts.apis.io/moxe-health/conventions/moxe-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moxe-health-conventions.yml
- group: design
  href: https://artifacts.apis.io/moxe-health/errors/moxe-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moxe-health-problem-types.yml
- group: design
  href: https://artifacts.apis.io/moxe-health/lifecycle/moxe-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moxe-health-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/moxe-health/conformance/moxe-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moxe-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://moxehealth.com/security/
- group: design
  href: https://artifacts.apis.io/moxe-health/data-model/moxe-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moxe-health-data-model.yml
- group: agent
  href: https://artifacts.apis.io/moxe-health/mcp/moxe-health-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/moxe-health-mcp.yml
- group: build
  href: https://artifacts.apis.io/moxe-health/mcp/moxe-health-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/moxe-health-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/moxe-health/security/moxe-health-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/moxe-health-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/moxe-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/moxe-health/packages/moxe-health-packages.yml
  title: ''
  type: Packages
  url: packages/moxe-health-packages.yml
- group: commercial
  href: https://artifacts.apis.io/moxe-health/plans/moxe-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moxe-health-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/moxe-health/rate-limits/moxe-health-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/moxe-health-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/moxe-health/arazzo/moxe-health-request-patient-chart.yml
  title: ''
  type: Arazzo
  url: arazzo/moxe-health-request-patient-chart.yml
- group: design
  href: https://artifacts.apis.io/moxe-health/arazzo/moxe-health-request-claim-chart.yml
  title: ''
  type: Arazzo
  url: arazzo/moxe-health-request-claim-chart.yml
- group: other
  href: https://artifacts.apis.io/moxe-health/overlays/moxe-health-chart-retrieval-initiate-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moxe-health-chart-retrieval-initiate-overlay.yaml
- group: other
  href: https://artifacts.apis.io/moxe-health/overlays/moxe-health-chart-retrieval-status-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moxe-health-chart-retrieval-status-overlay.yaml
- group: other
  href: https://artifacts.apis.io/moxe-health/overlays/moxe-health-claim-management-initiate-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moxe-health-claim-management-initiate-overlay.yaml
- group: other
  href: https://artifacts.apis.io/moxe-health/overlays/moxe-health-claim-management-status-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moxe-health-claim-management-status-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/moxe-health/llms/moxe-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moxe-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://moxehealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.moxehealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.moxehealth.com/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.moxehealth.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.moxehealth.com/reference/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developer.moxehealth.com/docs/authentication
- group: start
  title: ''
  type: SignUp
  url: https://developer.moxehealth.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moxehealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moxe-health
- group: company
  title: ''
  type: Blog
  url: https://moxehealth.com/insights
- group: auth
  title: ''
  type: Security
  url: https://moxehealth.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moxehealth.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moxehealth.com/moxe-technology-governing-agreement/
- group: operate
  title: ''
  type: Support
  url: https://moxehealth.com/contact/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developer.moxehealth.com/llms.txt
created: '2026-07-24'
description: Moxe Health is a United States healthcare data interoperability company, headquartered in Madison, Wisconsin, that operates the Clinical Data Clearinghouse for secure clinical data exchange between health plans (payers) and health systems (providers). Moxe's API-first platform ingests release-of-information (ROI) requests, searches connected electronic health records (EHRs) to extract the minimum-necessary contextual clinical data for a specified patient and date range, and securely delivers that data to the partner's system. Its Chart Retrieval API supports risk adjustment, quality improvement, claim management, payment integrity, care management, and forecasting use cases. The public developer portal documents a REST (OpenAPI 3.0.1) Chart Retrieval API secured with OAuth2 client-credentials plus an x-api-key header; retrieved charts are returned to a predetermined location via SFTP. Moxe is HIPAA and SOC 2 Type 2 compliant and was named number 1 Best in KLAS for Payer-Provider
  Data Exchange. The documented API is REST/JSON rather than HL7 FHIR, and full access is granted through a partner onboarding agreement.
finops:
- has_sources: true
  method: derived
  name: Moxe Health Finops
  primary_unit: ''
  service_category: ''
  slug: moxe-health-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-10-06'
name: Moxe Health
nav: Providers
network: true
overview: 'Moxe Health publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Claims API and Patient API. Tagged areas include Healthcare, United States, Interoperability, Clinical Data, and Payers.


  Moxe Health''s developer surface includes authentication, documentation, getting-started guide, API reference, signup flow, engineering blog, support, and 35 more developer resources.'
plans:
- name: Moxe Health Plans Pricing
  plan_count: 0
  slug: moxe-health-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Moxe Health Rate Limits
  slug: moxe-health-rate-limits
scopes:
- name: Moxe Health Scopes
  scope_count: 4
  slug: moxe-health-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 47.8
    developer_ergonomics: 58.9
    discoverability: 78.6
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 46.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/moxe-health/moxe-health-2026-08-07T184405.png
security:
- kind: authentication
  name: Moxe Health Authentication
  slug: moxe-health-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Moxe Health Domain Security
  slug: moxe-health-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Moxe Health Vulnerability Disclosure
  slug: moxe-health-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Moxe Health Trust Center
  slug: moxe-health-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 2
skills:
- name: Request a claim-supporting chart from Moxe Health
  slug: moxe-health-request-claim-chart
- name: Request a patient chart from Moxe Health
  slug: moxe-health-request-patient-chart
slug: moxe-health
tags:
- Healthcare
- United States
- Interoperability
- Clinical Data
- Payers
- Providers
- Electronic Health Records
- Health Data Exchange
- Claims
- Risk Adjustment
website: https://moxehealth.com/
---

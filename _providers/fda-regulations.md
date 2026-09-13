---
access_model:
  confidence: high
  label: Free · Requires approval
  onboarding: approval
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fda Regulations Agentic Access
  operation_count: 4
  slug: fda-regulations-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api-datadashboard.fda.gov/v1
  baseurl_source: declared
  description: 'RESTful access to the FDA Data Dashboard datasets that record how FDA regulations are enforced: inspection classifications, inspection citations (the specific CFR references cited against a firm), com'
  name: FDA Data Dashboard API
  slug: fda-regulations-data-dashboard-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fda-regulations-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://datadashboard.fda.gov/oii/api/index.htm#section-endpoints
- group: auth
  title: ''
  type: Authentication
  url: authentication/fda-regulations-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fda-regulations-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fda-regulations-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fda-regulations-data-model.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://datadashboard.fda.gov/oii/api/index.htm
- group: docs
  title: ''
  type: Documentation
  url: https://datadashboard.fda.gov/oii/api/index.htm
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fda-regulations-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fda-regulations-error-codes.yml
- group: build
  title: ''
  type: Examples
  url: examples/fda-regulations-examples.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://datadashboard.fda.gov/oii/api/index.htm#section-usage
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FDA
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fda-regulations-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fda-regulations-llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/fda-regulations-data-dashboard-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fda-regulations-data-dashboard-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/fda-regulations-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fda-regulations-plans-pricing.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fda.gov/about-fda/about-website/website-policies
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fda-regulations-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: https://datadashboard.fda.gov/oii/api/index.htm#section-try
- group: operate
  title: ''
  type: Support
  url: mailto:FDADataDashboard@fda.hhs.gov
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fda.gov/about-fda/about-website/website-policies
- group: company
  title: ''
  type: Website
  url: https://www.fda.gov/regulatory-information/laws-enforced-fda
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fda-regulations-mcp.yml
- group: agent
  title: ''
  type: X-WellKnownProbe
  url: well-known/fda-regulations-well-known.yml
created: '2025-01-01'
description: 'FDA Regulations is the body of federal rules the U.S. Food and Drug Administration enforces over the safety, efficacy and security of food, human and animal drugs, biologics, medical devices, cosmetics and tobacco products — codified at 21 CFR and administered through the agency''s inspection, citation, import and compliance-action programs. The machine-readable surface for that regulatory activity is the FDA Data Dashboard API (DDAPI), published by the FDA Office of Inspections and Investigations (formerly the Office of Regulatory Affairs), which serves the same inspection classification, inspection citation, import refusal and compliance action datasets that power the public Data Dashboard. Access is credentialed: FDA issues an Authorization-User / Authorization-Key header pair on request, and every endpoint is a POST search over a single dataset with JSON filters, column projection, sorting and offset paging.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fda-regulations.png
layout: provider
modified: '2026-09-12'
name: FDA Regulations
nav: Providers
network: true
overview: 'FDA Regulations publishes 1 API on the [APIs.io](https://apis.io/) network: FDA Data Dashboard API. Tagged areas include Regulatory Compliance, Healthcare, Medical Devices, Pharmaceuticals, and Food Safety.


  FDA Regulations'' developer surface includes API reference, authentication, documentation, code examples, getting-started guide, sandbox, support, and 21 more developer resources.'
plans:
- name: Fda Regulations Plans Pricing
  plan_count: 0
  slug: fda-regulations-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Fda Regulations Rate Limits
  slug: fda-regulations-rate-limits
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 38.3
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 63.7
    discoverability: 68.5
    operational_transparency: 5.3
  previous_composite: 3.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/fda-regulations/refs/heads/main/screenshots/fda-regulations-2026-06-20T181102.png
security:
- kind: authentication
  name: Fda Regulations Authentication
  slug: fda-regulations-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Fda Regulations Domain Security
  slug: fda-regulations-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fda-regulations
tags:
- Regulatory Compliance
- Healthcare
- Medical Devices
- Pharmaceuticals
- Food Safety
- Inspections
- Enforcement
- Federal-Government
- Public Data
- Imports
website: https://www.fda.gov/regulatory-information/laws-enforced-fda
---

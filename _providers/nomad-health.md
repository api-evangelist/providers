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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://nomadhealth.com/api/v1
  baseurl_source: declared
  description: Default namespace
  name: Nomad Health Default API
  slug: nomad-health-default-api
artifact_total: 8
collections:
- collection_type: open
  name: Nomad Health Default API
  slug: open-nomad-health-default-api
common:
- group: other
  href: https://artifacts.apis.io/nomad-health/capabilities/nomad-health-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nomad-health-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/nomad-health/overlays/nomad-health-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nomad-health-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://nomadhealth.com
- group: docs
  title: ''
  type: APIReference
  url: https://nomadhealth.com/api
- group: company
  title: ''
  type: Blog
  url: https://nomadhealth.com/blog
- group: operate
  title: ''
  type: Support
  url: https://nomadhealth.com/faqs
- group: operate
  title: ''
  type: HelpCenter
  url: https://faq.nomadhealth.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://nomadhealth.com/auth/register
- group: start
  title: ''
  type: Login
  url: https://nomadhealth.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nomadhealth.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nomadhealth.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NomadHealth
- group: agent
  href: https://artifacts.apis.io/nomad-health/llms/nomad-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nomad-health-llms.txt
- group: agent
  href: https://artifacts.apis.io/nomad-health/well-known/nomad-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nomad-health-well-known.yml
- group: auth
  href: https://artifacts.apis.io/nomad-health/authentication/nomad-health-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nomad-health-authentication.yml
- group: design
  href: https://artifacts.apis.io/nomad-health/conventions/nomad-health-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nomad-health-conventions.yml
- group: design
  href: https://artifacts.apis.io/nomad-health/errors/nomad-health-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nomad-health-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nomad-health/conformance/nomad-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nomad-health-conformance.yml
- group: design
  href: https://artifacts.apis.io/nomad-health/data-model/nomad-health-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nomad-health-data-model.yml
- group: design
  href: https://artifacts.apis.io/nomad-health/lifecycle/nomad-health-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nomad-health-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/nomad-health/mcp/nomad-health-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nomad-health-mcp.yml
- group: build
  href: https://artifacts.apis.io/nomad-health/mcp/nomad-health-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/nomad-health-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/nomad-health/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/nomad-health/security/nomad-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nomad-health-domain-security.yml
created: '2026-08-04'
description: Nomad Health operates a digital marketplace for healthcare travel staffing, connecting travel nurses, allied health professionals and other clinicians directly with healthcare facilities across all fifty U.S. states. The two-sided platform lets clinicians search and apply for travel assignments with transparency on pay rate, shift structure and requirements, while facilities post open positions and manage hiring through a cloud-based system; Nomad Navigators support clinicians through credentialing, onboarding and on-assignment needs. Nomad Health holds the Joint Commission Gold Seal of Approval for Travel Nursing Accreditation and reports more than 400,000 registered clinicians across 50-plus specialties spanning nursing, cath lab, laboratory, occupational therapy, physical therapy, radiology, respiratory therapy, sonography, speech language pathology and surgical technology. The company runs no public developer program, but serves a live Swagger 2.0 contract and a Swagger
  UI from its production application host covering job search, applications, credentialing, placements, facilities and messaging.
image: https://marketing.nomadhealth.com/favicon/apple-icon-114x114.png
layout: provider
modified: '2026-08-04'
name: Nomad Health
nav: Providers
network: true
overview: 'Nomad Health publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Default API. Tagged areas include Company, Healthcare, Staffing, Job, and Marketplace.


  The Nomad Health catalog on APIs.io includes 1 Spectral governance ruleset.


  Nomad Health''s developer surface includes API reference, engineering blog, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: Nomad Health API Rules
  rule_count: 27
  severity_counts:
    error: 23
    hint: 0
    info: 1
    warn: 3
  slug: nomad-health-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 36.0
    developer_ergonomics: 28.0
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 33.9
  provenance:
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
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/nomad-health/nomad-health-2026-08-07T185440.png
security:
- kind: authentication
  name: Nomad Health Authentication
  slug: nomad-health-authentication
  summary_line: session-cookie · 1 scheme
- kind: domain-security
  name: Nomad Health Domain Security
  slug: nomad-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Apply to a Nomad Health assignment
  slug: nomad-health-apply-to-assignment
- name: Manage Nomad Health credentialing and timecards
  slug: nomad-health-credentialing-and-timecards
- name: Search Nomad Health travel healthcare jobs
  slug: nomad-health-search-travel-jobs
slug: nomad-health
tags:
- Company
- Healthcare
- Staffing
- Job
- Marketplace
- Travel Nursing
- Allied Health
- Credentialing
- Recruiting
- Human Resources
website: https://nomadhealth.com
---

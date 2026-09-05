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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-04'
api_count: 4
apis:
- baseURL: https://nomadhealth.com/api/v1
  baseurl_source: declared
  description: Default namespace
  name: Nomad Health Default API
  slug: nomad-health-default-api
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nomad Health Default API
  slug: open-nomad-health-default-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nomad-health-capability-edges.yml
- group: other
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
  title: ''
  type: LLMsTxt
  url: llms/nomad-health-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nomad-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nomad-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nomad-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nomad-health-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nomad-health-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nomad-health-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nomad-health-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nomad-health-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nomad-health-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
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
overview: 'Nomad Health publishes 1 API on the [APIs.io](https://apis.io/) network: Default API. Tagged areas include Company, Healthcare, Staffing, Job, and Marketplace.


  Nomad Health''s developer surface includes API reference, engineering blog, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 33.1
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 31.6
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
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nomad-health/refs/heads/main/screenshots/nomad-health-2026-08-07T185440.png
security:
- kind: authentication
  name: Nomad Health Authentication
  slug: nomad-health-authentication
  summary_line: session-cookie · 1 scheme
- kind: domain-security
  name: Nomad Health Domain Security
  slug: nomad-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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

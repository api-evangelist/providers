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
    error_semantics: verified
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
  score: 23.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Orderly Health Agentic Access
  operation_count: 1
  slug: orderly-health-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.orderlyhealth.com
  baseurl_source: declared
  description: The Look Up Practitioners API from Orderly Health — 1 operation(s) for look up practitioners.
  name: Orderly Health Look Up Practitioners API
  slug: orderly-health-look-up-practitioners-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orderly Provider Directory Look Up Practitioners API
  slug: open-orderly-health-look-up-practitioners-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/orderly-health-provider-directory-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orderly-health-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orderly-health-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orderly-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orderly-health-conventions.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/orderly-health-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orderly-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/orderly-health-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orderly-health-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orderly-health-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orderly-health-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://orderlyapi.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://orderlyapi.readme.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://orderlyapi.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://orderlyapi.readme.io/docs/setting-up-to-use-the-orderly-api
- group: operate
  title: ''
  type: ChangeLog
  url: https://orderlyapi.readme.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://orderlyhealth.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orderlyhealth
- group: start
  title: ''
  type: SignUp
  url: https://app.orderlyhealth.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orderlyhealth.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orderlyhealth.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://orderlyhealth.com
created: '2026-07-17'
description: Orderly Health is a Denver, Colorado healthcare data company that keeps provider directories accurate and usable. Founded in 2015, its API-first platform uses machine learning and AI to automatically identify and repair inaccuracies in healthcare provider data for providers, payers, and health-technology companies. Its products include the Orderly Provider Directory (6.4M+ practitioner profiles), a Roster Automation Suite that normalizes and validates rosters in seconds, and Data Updates that deliver traceable, field-level corrections. The public Orderly Provider Directory API lets developers search practitioners by NPI, name, location, specialty, care category, accepted insurance, and DEA number, returning per-field confidence scores and source attribution. Orderly Health was acquired by First Choice Health.
image: https://files.readme.io/e494480-small-Orderly_Logo_4cMrk_NavyText.png
layout: provider
modified: '2026-07-20'
name: Orderly Health
nav: Providers
network: true
overview: 'Orderly Health publishes 1 API on the [APIs.io](https://apis.io/) network: Look Up Practitioners API. Tagged areas include Company, Healthcare, Provider Data, Provider Directory, and Health Data.


  Orderly Health''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, engineering blog, and 16 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 53.1
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 37.3
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
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orderly-health/refs/heads/main/screenshots/orderly-health-2026-08-07T190912.png
security:
- kind: authentication
  name: Orderly Health Authentication
  slug: orderly-health-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Orderly Health Domain Security
  slug: orderly-health-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: orderly-health
tags:
- Company
- Healthcare
- Provider Data
- Provider Directory
- Health Data
- Machine-Learning
- Data Quality
- Interoperability
website: https://orderlyhealth.com
---

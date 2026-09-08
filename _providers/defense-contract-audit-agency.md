---
access_model:
  confidence: high
  label: Free and anonymous — no sign-up, no key, no plans
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-07'
api_count: 2
apis:
- description: The public JSON backend of DCAA's Field Audit Office Branch Locator. It resolves the DCAA field audit office cognizant over a contractor from a CAGE code (searchType 0), a SAM.gov Unique Entity Identi
  name: DCAA Field Audit Office Branch Locator API
  slug: branch-locator
- description: The portal a defense contractor uses to file, update or withdraw a certified incurred cost submission with DCAA. It is a DCAA-operated application on a DCAA host, but every path redirects unauthentica
  name: DCAA Contractor Submission Portal (CSP)
  slug: contractor-submission-portal
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-defense-contract-audit-agency
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defense-contract-audit-agency-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/defense-contract-audit-agency-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/defense-contract-audit-agency-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/defense-contract-audit-agency-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/defense-contract-audit-agency-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/defense-contract-audit-agency-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/defense-contract-audit-agency-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/defense-contract-audit-agency-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/defense-contract-audit-agency-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/defense-contract-audit-agency-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/defense-contract-audit-agency
- group: company
  title: ''
  type: Website
  url: https://www.dcaa.mil
- group: company
  title: ''
  type: About
  url: https://www.dcaa.mil/About/
- group: other
  title: ''
  type: Publications
  url: https://www.dcaa.mil/Guidance/
- group: operate
  title: ''
  type: Contact
  url: https://www.dcaa.mil/Contact/
- group: operate
  title: ''
  type: Support
  url: https://www.dcaa.mil/Contact/Contact-Form/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dcaa.mil/Privacy-and-Security/
created: '2024-12-03'
description: 'The Defense Contract Audit Agency (DCAA), under the authority, direction, and control of the Under Secretary of Defense (Comptroller), provides audit and financial advisory services to the Department of Defense and other federal entities responsible for acquisition and contract administration. DCAA runs no developer program: no API documentation, no OpenAPI, no SDK, no MCP server, no agent card and no /.well-known surface exist on any host it operates. It does serve one public, unauthenticated and undocumented JSON API — the Field Audit Office Branch Locator at https://fao.dcaa.mil/api — which resolves the cognizant DCAA audit office for a contractor by CAGE code, SAM.gov UEI or ZIP code and returns RFC 9457 problem details on validation failure. A second, gated surface, the Contractor Submission Portal at https://csp.dcaa.mil, takes certified incurred cost submissions behind an OpenID Connect sign-in federated to DoD PIEE.'
finops:
- name: Defense Contract Audit Agency Finops
  service_category: API
  slug: defense-contract-audit-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defense-contract-audit-agency.png
layout: provider
modified: '2026-09-07'
name: Defense Contract Audit Agency
nav: Providers
network: true
overview: 'Defense Contract Audit Agency publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Defense, Department of Defense, Audit, and Contract Audit.


  Defense Contract Audit Agency''s developer surface includes authentication, support, and 15 more developer resources.'
plans:
- name: Defense Contract Audit Agency Plans Pricing
  plan_count: 0
  slug: defense-contract-audit-agency-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Defense Contract Audit Agency Rate Limits
  slug: defense-contract-audit-agency-rate-limits
scopes:
- name: Defense Contract Audit Agency Scopes
  scope_count: 2
  slug: defense-contract-audit-agency-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.5
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 11.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/defense-contract-audit-agency/refs/heads/main/screenshots/defense-contract-audit-agency-2026-06-20T175820.png
security:
- kind: authentication
  name: Defense Contract Audit Agency Authentication
  slug: defense-contract-audit-agency-authentication
  summary_line: none/openIdConnect · 2 schemes
- kind: domain-security
  name: Defense Contract Audit Agency Domain Security
  slug: defense-contract-audit-agency-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: defense-contract-audit-agency
tags:
- Federal-Government
- Defense
- Department of Defense
- Audit
- Contract Audit
- Financial
- Government Contracting
- CAGE Code
- Unique Entity Identifier
- Locator
website: https://www.dcaa.mil
---

---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Devoted Agentic Access
  operation_count: 6
  slug: devoted-agentic-access
  summary_line: 6 operations
api_count: 7
apis:
- description: Public FHIR R4 API for in-network providers, facilities, and pharmacies, based on the Da Vinci PDEX Plan-Net reference implementation.
  name: Provider & Pharmacy Directory API
  slug: provider-pharmacy-directory-api
- description: Public FHIR R4 API for drug formulary information, based on the Da Vinci PDEX US Drug Formulary implementation guide.
  name: Plan Coverage & Formularies API
  slug: plan-coverage-formularies-api
- description: The Condition API from Devoted Health — 1 operation(s) for condition.
  name: Devoted Health Condition API
  slug: devoted-condition-api
- description: The Encounter API from Devoted Health — 1 operation(s) for encounter.
  name: Devoted Health Encounter API
  slug: devoted-encounter-api
- description: The ExplanationOfBenefit API from Devoted Health — 1 operation(s) for explanationofbenefit.
  name: Devoted Health ExplanationOfBenefit API
  slug: devoted-explanationofbenefit-api
- description: The Medication API from Devoted Health — 1 operation(s) for medication.
  name: Devoted Health Medication API
  slug: devoted-medication-api
- description: The Patient API from Devoted Health — 2 operation(s) for patient.
  name: Devoted Health Patient API
  slug: devoted-patient-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://devoted.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.devoted.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.devoted.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://devoted.com/developers/fhir/swagger/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.devoted.com/developers/
- group: start
  title: ''
  type: SignUp
  url: https://forms.gle/UFYvckiAeEjWP49K9
- group: operate
  title: ''
  type: Support
  url: mailto:interop@devoted.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DevotedHealth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.devoted.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.devoted.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/devoted-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/devoted-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/devoted-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/devoted-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/devoted-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/devoted-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/devoted-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/devoted-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/devoted-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/devoted-patient-access-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/devoted-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/devoted-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/devoted-agentic-access.yml
created: '2026-07-17'
description: 'Devoted Health is a technology-enabled Medicare Advantage payer founded in 2017 and headquartered in Waltham, Massachusetts, backed by General Catalyst and Obvious Ventures. It publishes CMS-required interoperability APIs built on HL7 FHIR R4: a member-facing Patient Access API exposing claims (ExplanationOfBenefit), encounters, conditions, and medications; a public Provider & Pharmacy Directory API (Da Vinci PDEX Plan-Net); and a public Plan Coverage & Formularies API (PDEX US Drug Formulary). Member data access uses OAuth 2.0 / OpenID Connect with member consent under the 21st Century Cures Act, and third-party applications register with the interoperability team to receive credentials.'
image: https://www.devoted.com/static/og-image-47c9150444c012fc8cbb61768089657c.png
layout: provider
mcp_servers:
- description: ''
  name: devoted-mcp.yml
  slug: devoted-mcpyml
modified: '2026-07-18'
name: Devoted Health
nav: Providers
network: true
overview: 'Devoted Health publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Condition API, Encounter API, ExplanationOfBenefit API, and 2 more. Tagged areas include Company, Healthcare, Medicare Advantage, Health Insurance, and FHIR.


  Devoted Health''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, and 18 more developer resources.'
random_paper: 69
scopes:
- name: Devoted Scopes
  scope_count: 14
  slug: devoted-scopes
  summary_line: 14 scopes
score:
  band: developing
  composite: 43.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 41.5
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/devoted/refs/heads/main/screenshots/devoted-2026-07-25T211821.png
security:
- kind: authentication
  name: Devoted Authentication
  slug: devoted-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Devoted Domain Security
  slug: devoted-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: devoted
tags:
- Company
- Healthcare
- Medicare Advantage
- Health Insurance
- FHIR
- Interoperability
- CMS Patient Access
- Payer
website: https://devoted.com
---

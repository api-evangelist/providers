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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Metriport Agentic Access
  operation_count: 30
  slug: metriport-agentic-access
  summary_line: 30 operations · 13 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Medical API consolidated FHIR data.
  name: Metriport Consolidated API
  slug: metriport-consolidated-api
- description: Devices API normalized health data.
  name: Metriport Devices Data API
  slug: metriport-devices-data-api
- description: Medical API clinical document query and retrieval.
  name: Metriport Document API
  slug: metriport-document-api
- description: Medical API facility management.
  name: Metriport Facility API
  slug: metriport-facility-api
- description: Medical API patient management.
  name: Metriport Patient API
  slug: metriport-patient-api
- description: Account settings and webhooks.
  name: Metriport Settings API
  slug: metriport-settings-api
- description: Devices API user and connect management.
  name: Metriport User API
  slug: metriport-user-api
arazzos:
- description: Register a patient, start a consolidated FHIR R4 query for the requested resources, poll until conversion completes, then count the consolidated data.
  name: Metriport Consolidated FHIR Query
  slug: metriport-consolidated-fhir-query-workflow
- description: Register a patient, trigger an IHE document query across the networks, poll until retrieval completes, list the resulting documents, and obtain a signed download URL.
  name: Metriport Patient Document Retrieval
  slug: metriport-patient-document-retrieval-workflow
- description: Create a facility, register a patient under it, then run an MPI demographic match to resolve an existing patient record.
  name: Metriport Patient Matching
  slug: metriport-patient-matching-workflow
- description: Create a devices user, mint a Connect Widget session token, then pull the user's activity and biometrics data from connected wearables.
  name: Metriport Wearables Connect
  slug: metriport-wearables-connect-workflow
artifact_total: 30
asyncapis:
- description: ''
  name: Metriport Webhooks
  slug: metriport-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Metriport Consolidated API
  slug: open-metriport-consolidated-api
- collection_type: open
  name: Metriport Consolidated Devices Data API
  slug: open-metriport-devices-data-api
- collection_type: open
  name: Metriport Consolidated Document API
  slug: open-metriport-document-api
- collection_type: open
  name: Metriport Consolidated Facility API
  slug: open-metriport-facility-api
- collection_type: open
  name: Metriport Consolidated Patient API
  slug: open-metriport-patient-api
- collection_type: open
  name: Metriport Consolidated Settings API
  slug: open-metriport-settings-api
- collection_type: open
  name: Metriport Consolidated User API
  slug: open-metriport-user-api
- collection_type: open
  name: Metriport API
  slug: open-metriport
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/metriport-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metriport-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metriport-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metriport-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metriport
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/metriport
- group: company
  title: ''
  type: Website
  url: https://www.metriport.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metriport.com
- group: commercial
  title: ''
  type: Plans
  url: plans/metriport-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/metriport-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/metriport-finops.yml
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
- group: company
  title: ''
  type: Blog
  url: https://www.metriport.com/blog
- group: build
  title: ''
  type: Packages
  url: packages/metriport-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/metriport-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/metriport-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/metriport-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/metriport-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/metriport-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metriport-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/metriport-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/metriport-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/metriport-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/metriport-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/metriport-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metriport-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metriport-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metriport-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/metriport-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/metriport-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/metriport-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/metriport-webhooks.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.metriport.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dash.metriport.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.metriport.com/medical-api/getting-started/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.metriport.com/medical-api/api-reference/patient/create-patient
- group: operate
  title: ''
  type: Support
  url: https://www.metriport.com/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.metriport.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dash.metriport.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.metriport.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.metriport.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/metriport/metriport-api/folder/7zl228v/medical
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/metriport/metriport
created: '2026-06-21'
description: Metriport is an open-source, universal API for healthcare data. The Medical API exchanges patient medical records across the CommonWell and Carequality networks and returns consolidated FHIR R4 data, while the Devices API hydrates activity, biometrics, nutrition, and sleep data from consumer wearables and mHealth apps. Companies can use the hosted Metriport cloud or self-host the open-source code to avoid vendor lock-in.
finops:
- name: Metriport Finops
  service_category: Healthcare and Life Sciences
  slug: metriport-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metriport.png
layout: provider
mcp_servers:
- description: Metriport serves a remote MCP endpoint from its documentation host. A tools/list POST returns HTTP 200 anonymously with three real tools and their inputSchemas — captured verbatim in metriport-mcp-too
  name: Metriport MCP Server
  slug: metriport-mcp-server
modified: '2026-08-14'
name: Metriport
nav: Providers
network: true
overview: 'Metriport publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Consolidated API, Devices Data API, Document API, and 4 more. Tagged areas include Healthcare, Medical Records, FHIR, Health Data, and Wearables.


  The Metriport catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Metriport''s developer surface includes authentication, documentation, engineering blog, sandbox, getting-started guide, API reference, support, and 36 more developer resources.'
plans:
- name: Metriport Plans Pricing
  plan_count: 4
  slug: metriport-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 10
  name: Metriport Rate Limits
  slug: metriport-rate-limits
score:
  band: strong
  composite: 65.9
  coverage:
    artifact_dirs: 27
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 61.6
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 51.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metriport/refs/heads/main/screenshots/metriport-2026-08-07T172739.png
security:
- kind: authentication
  name: Metriport Authentication
  slug: metriport-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Metriport Domain Security
  slug: metriport-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Metriport Vulnerability Disclosure
  slug: metriport-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Metriport Trust Center
  slug: metriport-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: metriport
tags:
- Healthcare
- Medical Records
- FHIR
- Health Data
- Wearables
- Open-Source
website: https://www.metriport.com
---

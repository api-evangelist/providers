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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: provides endpoints to access to commands sent to the submission API
  name: Interhyp commands API
  slug: interhyp-commands-api
- description: access to submission documents
  name: Interhyp documents API
  slug: interhyp-documents-api
- description: provides endpoints for financing application resources not associate to a specific financing partner
  name: Interhyp financing-application API
  slug: interhyp-financing-application-api
- description: provides basic info about service status and version of the submission API specs used
  name: Interhyp info API
  slug: interhyp-info-api
- description: provides endpoints to access submission logbook
  name: Interhyp logbook API
  slug: interhyp-logbook-api
- description: provides endpoints for pre-submission resources associated with a specific financing partner
  name: Interhyp pre-submission-checks API
  slug: interhyp-pre-submission-checks-api
- description: access to submission protocol
  name: Interhyp protocol API
  slug: interhyp-protocol-api
- description: provides endpoints for submission resources associated with a specific financing partner
  name: Interhyp submissions API
  slug: interhyp-submissions-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Interhyp Submission commands API
  slug: open-interhyp-commands-api
- collection_type: open
  name: Interhyp Submission commands documents API
  slug: open-interhyp-documents-api
- collection_type: open
  name: Interhyp Submission commands financing-application API
  slug: open-interhyp-financing-application-api
- collection_type: open
  name: Interhyp Submission commands info API
  slug: open-interhyp-info-api
- collection_type: open
  name: Interhyp Submission commands logbook API
  slug: open-interhyp-logbook-api
- collection_type: open
  name: Interhyp Submission commands pre-submission-checks API
  slug: open-interhyp-pre-submission-checks-api
- collection_type: open
  name: Interhyp Submission commands protocol API
  slug: open-interhyp-protocol-api
- collection_type: open
  name: Interhyp Submission commands submissions API
  slug: open-interhyp-submissions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/interhyp-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/interhyp-submission-documents-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ehyphome.de/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ehyphome.de/products
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ehyphome.de/first-steps
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.ehyphome.de/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.ehyphome.de/assets/AGB.pdf
- group: start
  title: ''
  type: SignUp
  url: https://www.prohyp.de/partner-werden/
- group: operate
  title: ''
  type: Support
  url: mailto:am@prohyp.de
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Interhyp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.interhyp.de/datenschutz.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/interhyp-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/interhyp-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/interhyp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/interhyp-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/interhyp-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/interhyp-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/interhyp-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/interhyp-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/interhyp-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/interhyp-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/interhyp-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/interhyp-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/interhyp-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Interhyp AG is Germany's leading platform for residential mortgage financing (Baufinanzierung), connecting homebuyers and partners with the best financing options by comparing offers from more than 500 loan partners. Through its Developer Studio (developer.ehyphome.de) Interhyp publishes a partner-facing REST API surface — most notably the Submission API — that lets brokers, referrers and platforms integrate mortgage submission workflows, financing applications, documents, logbooks and pre-submission checks directly into their own applications. The API is designed "API First" and "Mobile First", secured with OAuth 2.0 JWT bearer tokens plus an Api-Key header, uses cursor-based pagination, RFC 7807 problem+json error responses and traceId request tracing. Interhyp is part of the ING Group and operates the broker brand Prohyp.
image: https://developer.ehyphome.de/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Interhyp MCP Server
  slug: interhyp-mcp-server
modified: '2026-07-19'
name: Interhyp
nav: Providers
network: true
overview: 'Interhyp publishes 8 APIs on the [APIs.io](https://apis.io/) network, including commands API, documents API, financing-application API, and 5 more. Tagged areas include Company, Fintech, Mortgage, Lending, and Baufinanzierung.


  Interhyp''s developer surface includes documentation, getting-started guide, changelog, signup flow, support, authentication, sandbox, and 18 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 58.1
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 44.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/interhyp/refs/heads/main/screenshots/interhyp-2026-07-25T222702.png
security:
- kind: authentication
  name: Interhyp Authentication
  slug: interhyp-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Interhyp Domain Security
  slug: interhyp-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: interhyp
tags:
- Company
- Fintech
- Mortgage
- Lending
- Baufinanzierung
- Real-Estate
- Banking
- Germany
- API-First
website: https://developer.ehyphome.de/
---

---
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
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Qbe Agentic Access
  operation_count: 17
  slug: qbe-agentic-access
  summary_line: 17 operations · 15 acting
api_count: 2
apis:
- description: QBE Australia's broker-facing policy lifecycle API, published in the QBE Australia API Hub as the "ANZO Digital Brokers" product. QBE describes it as providing "access to the insurance policy lifecycl
  name: QBE Australia ANZO Digital Brokers Experience API
  slug: qbe-anzo-digital-brokers-api
- description: A small QBE Australia service published in the same API Hub as the "ANZO CTP Service" product, supporting the compulsory third party (CTP) motor insurance switching flow. Two documented operations app
  name: QBE Australia CTP Switch Service
  slug: qbe-ctp-switch-service-api
arazzos:
- description: Cancel an in-force QBE policy with a published cancellation reason code, confirm it, and attach the cancellation schedule.
  name: QBE policy cancellation
  slug: qbe-cancel-policy
- description: Open a mid-term endorsement on an in-force QBE policy, confirm it with a bind, and attach the endorsement schedule.
  name: QBE mid-term endorsement, confirmed
  slug: qbe-endorse-and-bind
- description: Create a commercial quote with QBE Australia, amend it, then convert it into a bound policy.
  name: QBE quote to bound policy
  slug: qbe-quote-to-bind
artifact_total: 12
collections:
- collection_type: open
  name: ANZO Digital Brokers Experience API
  slug: open-qbe-anzo-digital-brokers
- collection_type: open
  name: CTP Switch Service
  slug: open-qbe-ctp-switch-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qbe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qbe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qbe-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.qbe.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://connect.api-au.qbe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://connect.api-au.qbe.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://connect.api-au.qbe.com/apis
- group: start
  title: ''
  type: PartnerPortal
  url: https://partnerportal-api.qbena.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://connect.api-au.qbe.com/getting-started
- group: start
  title: ''
  type: Login
  url: https://connect.api-au.qbe.com/signin
- group: operate
  title: ''
  type: Support
  url: https://www.qbe.com/au/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qbe.com/au/about/governance/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qbe.com/us/legal/api-terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qbegroup
- group: auth
  title: ''
  type: Security
  url: https://www.qbe.com/responsible-disclosure-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qbe-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qbe-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qbe-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qbe-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qbe-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/qbe-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qbe-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/qbe-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/qbe-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qbe-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/qbe-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qbe-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/qbe-quote-to-bind.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/qbe-endorse-and-bind.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/qbe-cancel-policy.yml
created: '2026-07-25'
description: 'QBE Insurance Group Limited is a Sydney-headquartered, ASX-listed global general insurance and reinsurance group, tracing back to 1886 in Townsville, Queensland, and operating today across Australia Pacific, North America and International divisions including a Lloyd''s of London syndicate. QBE writes commercial and personal property and casualty lines — property, liability, motor and compulsory third party (CTP), workers compensation, marine, aviation, trade credit, crop and specialty — distributed overwhelmingly through brokers and agents rather than direct to consumers. Its API posture reflects that distribution model and is partner-gated by design: QBE Australia runs a real, publicly browsable Azure API Management developer portal at connect.api-au.qbe.com whose catalogue, operations, schemas and examples can be read anonymously, but every product requires an approved subscription (approvalRequired true) and the broker API is keyed to named partner platforms. The portal
  exposes genuine quote, bind, endorse, renew, cancel and refer operations for the commercial policy lifecycle — the four real insurance verbs, minus claims/FNOL, which QBE does not expose publicly. A separate QBE North America partner API hub at partnerportal-api.qbena.com serves an empty Azure APIM catalogue to anonymous callers but does publish seven named API products in its own content pages — Quote, Bind, Master Liability, Property Inquiry, Zip Code Validate and Reconciliation and Cancellation for Renters, plus Quote for Homeowners — behind a documented client-id/secret to JWT token exchange; no endpoints or specs are exposed. QBE Hong Kong documents a partner API behind qbe.com pages that are bot-blocked to anonymous fetchers. Australia is the home market; the Consumer Data Right was designated for general insurance and then deferred, so nothing here is compelled by regulation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Candidate MCP manifest (no hosted server published)
  slug: candidate-mcp-manifest-no-hosted-server-published
modified: '2026-07-25'
name: QBE Insurance
nav: Providers
network: true
overview: 'QBE Insurance publishes 2 APIs on the [APIs.io](https://apis.io/) network: QBE Australia ANZO Digital Brokers Experience API and QBE Australia CTP Switch Service. Tagged areas include Insurance, Australia, Property and Casualty, Commercial Insurance, and Underwriting.


  QBE Insurance''s developer surface includes authentication, documentation, API reference, getting-started guide, support, sandbox, and 25 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 36.3
  delta: 0.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 20.5
    contract_quality: 13.4
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 20.5
    operational_transparency: 13.2
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Qbe Authentication
  slug: qbe-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Qbe Domain Security
  slug: qbe-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qbe Vulnerability Disclosure
  slug: qbe-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: qbe
tags:
- Insurance
- Australia
- Property and Casualty
- Commercial Insurance
- Underwriting
- Policy Administration
- Quote
- Broker
- Reinsurance
- Carrier
- Partner API
website: https://www.qbe.com/
---

---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Solera Agentic Access
  operation_count: 26
  slug: solera-agentic-access
  summary_line: 26 operations · 8 acting
api_count: 10
apis:
- description: The Assignment API from Solera — 3 operation(s) for assignment.
  name: Solera Assignment API
  slug: solera-assignment-api
- description: The EstimateReturn API from Solera — 1 operation(s) for estimatereturn.
  name: Solera Estimate Return API
  slug: solera-estimatereturn-api
- description: The GetClaimImageResponse API from Solera — 1 operation(s) for getclaimimageresponse.
  name: Solera Get Claim Image Response API
  slug: solera-getclaimimageresponse-api
- description: The GetDocument API from Solera — 2 operation(s) for getdocument.
  name: Solera Get Document API
  slug: solera-getdocument-api
- description: The GetDocuments API from Solera — 2 operation(s) for getdocuments.
  name: Solera Get Documents API
  slug: solera-getdocuments-api
- description: The GetImage API from Solera — 4 operation(s) for getimage.
  name: Solera Get Image API
  slug: solera-getimage-api
- description: The GetValuation API from Solera — 1 operation(s) for getvaluation.
  name: Solera Get Valuation API
  slug: solera-getvaluation-api
- description: The GetValuationResponse API from Solera — 1 operation(s) for getvaluationresponse.
  name: Solera Get Valuation Response API
  slug: solera-getvaluationresponse-api
- description: The GICIntegration API from Solera — 2 operation(s) for gicintegration.
  name: Solera GIC Integration API
  slug: solera-gicintegration-api
- description: The ValuationReturn API from Solera — 2 operation(s) for valuationreturn.
  name: Solera Valuation Return API
  slug: solera-valuationreturn-api
- description: The Version API from Solera — 2 operation(s) for version.
  name: Solera Version API
  slug: solera-version-api
artifact_total: 28
asyncapis:
- description: 'Audatex Integrations (EAPI) pushes claim lifecycle events to a CLIENT-hosted HTTPS endpoint. The client registers its callback endpoints and the credentials Audatex should use, per assignment, in the '
  name: Solera / Audatex EAPI Event Callbacks
  slug: solera-eapi-asyncapi
- description: ''
  name: Solera Webhooks
  slug: solera-webhooks
collections:
- collection_type: open
  name: ClaimImages API
  slug: open-solera-claim-images-prod-swagger
- collection_type: open
  name: ClaimImages API
  slug: open-solera-claim-images
- collection_type: open
  name: Solera Dashboard Assignment API
  slug: open-solera-dashboard-assignment
- collection_type: open
  name: EAPI Get Document API
  slug: open-solera-eapi-getdocument
- collection_type: open
  name: Solera Enterprise API
  slug: open-solera-enterprise-assignment-prod-swagger
- collection_type: open
  name: Audatex GetDocuments API
  slug: open-solera-getdocuments-v1
- collection_type: open
  name: Audatex GetDocuments API
  slug: open-solera-getdocuments-v2
- collection_type: open
  name: Audatex Assignment Get Document API
  slug: open-solera-getimage-v1
- collection_type: open
  name: Audatex Assignment Get Document API
  slug: open-solera-getimage-v2
- collection_type: open
  name: EAPI GIC Integration API
  slug: open-solera-gic-integration
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/solera-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/solera-dashboard-assignment-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/solera-enterprise-assignment-prod-swagger-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/solera-claim-images-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/solera-claim-images-prod-swagger-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/solera-gic-integration-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/solera-getdocuments-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/solera-getdocuments-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/solera-getimage-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/solera-getimage-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/solera-eapi-getdocument-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/solera-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solera-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/solera-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/solera-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.solera.com/
- group: other
  title: ''
  type: Company
  url: https://www.solera.com/company/
- group: company
  title: ''
  type: Blog
  url: https://www.solera.com/blog/
- group: start
  title: ''
  type: PartnerPortal
  url: https://na.api.solera.com/
- group: auth
  title: ''
  type: Authentication
  url: https://dispatch-login-demo.audatex.com/.well-known/openid-configuration
- group: other
  title: ''
  type: Standards
  url: https://www.cieca.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-prod.audatex.com/TestAssignmentapi/docs/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://na.api.solera.com/files/Estimate%20Return%20API.pdf
- group: docs
  title: ''
  type: Documentation
  url: https://na.api.solera.com/files/ClaimImage%20Return%20API.pdf
- group: docs
  title: ''
  type: Documentation
  url: https://na.api.solera.com/files/GIC%20-%20Image%20Capture%20API.docx
- group: agent
  title: ''
  type: WellKnown
  url: well-known/solera-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/solera-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/solera-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/solera-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/solera-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/solera-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/solera-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/solera-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/solera-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/solera-eapi-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/solera-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/solera-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solera-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.solera.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.mysupportgarage.com
- group: start
  title: ''
  type: GettingStarted
  url: https://na.api.solera.com/files/Estimate%20Return%20API.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solera.com/us-canada-master-services-agreement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.solera.com/product-specific-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.solera.com/privacy-policy/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.solera.com/privacy-center/
- group: commercial
  title: ''
  type: Legal
  url: https://www.solera.com/legal/
- group: other
  title: ''
  type: Policies
  url: https://www.solera.com/policies-downloads/
- group: company
  title: ''
  type: News
  url: https://www.solera.com/news/
- group: company
  title: ''
  type: Careers
  url: https://www.solera.com/careers/
created: '2026-07-25'
description: Solera is a Westlake, Texas headquartered vehicle lifecycle management software, data, and services company operating in more than 100 countries, and one of the claims-technology intermediaries that sits between property and casualty insurers and the repair, salvage, and fleet economy rather than underwriting risk itself. Its insurance-facing business is automobile physical damage claims — first notice of loss intake, photo and AI damage assessment, repair cost estimating, total loss valuation, parts sourcing, and claims workflow — delivered through the Audatex and Qapter brands alongside Vehicle Repair (Identifix, Autodata, Hollander), Dealer Solutions (DealerSocket, cap hpi), and Fleet Solutions (Omnitracs, SmartDrive, eDriving) divisions. Its API posture is characteristic of the United States insurance market seam — there is no self-serve developer portal on solera.com, no signup, and no public API key. The Solera Integrations portal at na.api.solera.com returns HTTP 200
  to an Audatex user ID and password login wall, and onboarding is a provisioned B2B integration run through a Solera account representative with a kickoff meeting and UAT. What is genuinely public is a set of anonymously readable Swagger UI reference pages and machine readable OpenAPI 3.0.1 documents on the Audatex demo API host, plus PDF integration guides on na.api.solera.com/files, covering assignment dispatch and first notice of loss, claim image retrieval, and GIC integration. Authentication is OAuth 2.0 against an IdentityServer discovery document at dispatch-login-demo.audatex.com with resource scopes including b2b.fnol.api, gofnol.api, estimatics.api, and hqclaims.api. Solera does not reference ACORD anywhere in its public integration documentation. Its published standards alignment is CIECA instead — Audatex is documented as a Corporate Technology member of the Collision Industry Electronic Commerce Association and licensed to use CIECA standards, with the BMS 5.7 schema as the
  data mapping baseline for estimate return, which is the auto physical damage sector's analogue to ACORD rather than ACORD itself.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: No MCP server is published by Solera. This is a candidate tool list derived from the 26 harvested OpenAPI operations; any real deployment would be an in-tenant server, since credentials are provisione
  name: Candidate MCP tool surface
  slug: candidate-mcp-tool-surface
modified: '2026-07-25'
name: Solera
nav: Providers
network: true
overview: 'Solera publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Assignment API, Estimate Return API, Get Claim Image Response API, and 8 more. Tagged areas include Insurance, United States, Property and Casualty, Claims, and Claims Technology.


  The Solera catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Solera''s developer surface includes authentication, engineering blog, API reference, documentation, sandbox, changelog, support, and 43 more developer resources.'
random_paper: 16
scopes:
- name: Solera Scopes
  scope_count: 4
  slug: solera-scopes
  summary_line: 4 scopes · password
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 22
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 63.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/solera/refs/heads/main/screenshots/solera-2026-08-17T081956.png
security:
- kind: authentication
  name: Solera Authentication
  slug: solera-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Solera Domain Security
  slug: solera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: solera
tags:
- Insurance
- United States
- Property and Casualty
- Claims
- Claims Technology
- Automotive Claims
- FNOL
- Vehicle Damage Assessment
- Risk Data
- CIECA
- Insurtech
website: https://www.solera.com/
---

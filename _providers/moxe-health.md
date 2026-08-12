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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Moxe Health Agentic Access
  operation_count: 4
  slug: moxe-health-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 2
apis:
- description: Initiate a patient chart request and check its status. The API ingests a release-of-information request with member and demographic identifiers, searches connected EHRs for the specified patient and d
  name: Moxe Health Chart Retrieval API
  slug: moxe-health-chart-retrieval-api
- description: 'Initiate a claim management request and check its status. Retrieves the clinical chart supporting a specific claim by member and claim identifiers, then delivers the extracted data to a predetermined '
  name: Moxe Health Claim Management API
  slug: moxe-health-claim-management-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Initiate a claim-management request to retrieve the clinical chart supporting a specific claim, then poll the status endpoint with the returned moxeRequestId.
  name: Request a claim-supporting chart and poll for status
  slug: moxe-health-request-claim-chart
- description: Initiate a release-of-information request for a patient's clinical chart, then poll the status endpoint with the returned moxeRequestId until Moxe delivers the chart via SFTP.
  name: Request a patient chart and poll for status
  slug: moxe-health-request-patient-chart
artifact_total: 12
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/moxe-health-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moxe-health-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moxe-health-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/moxe-health-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moxe-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moxe-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moxe-health-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moxe-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moxe-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://moxehealth.com/security/
- group: design
  title: ''
  type: DataModel
  url: data-model/moxe-health-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moxe-health-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/moxe-health-tool-crosswalk.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moxe-health-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moxe-health-request-patient-chart.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/moxe-health-request-claim-chart.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/moxe-health-chart-retrieval-initiate-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moxe-health-chart-retrieval-status-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moxe-health-claim-management-initiate-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/moxe-health-claim-management-status-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moxe-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://moxehealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.moxehealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.moxehealth.com/docs/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.moxehealth.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.moxehealth.com/reference/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developer.moxehealth.com/docs/authentication
- group: start
  title: ''
  type: SignUp
  url: https://developer.moxehealth.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moxehealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moxe-health
- group: company
  title: ''
  type: Blog
  url: https://moxehealth.com/insights
- group: auth
  title: ''
  type: Security
  url: https://moxehealth.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moxehealth.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moxehealth.com/moxe-technology-governing-agreement/
- group: operate
  title: ''
  type: Support
  url: https://moxehealth.com/contact/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developer.moxehealth.com/llms.txt
created: '2026-07-24'
description: Moxe Health is a United States healthcare data interoperability company, headquartered in Madison, Wisconsin, that operates the Clinical Data Clearinghouse for secure clinical data exchange between health plans (payers) and health systems (providers). Moxe's API-first platform ingests release-of-information (ROI) requests, searches connected electronic health records (EHRs) to extract the minimum-necessary contextual clinical data for a specified patient and date range, and securely delivers that data to the partner's system. Its Chart Retrieval API supports risk adjustment, quality improvement, claim management, payment integrity, care management, and forecasting use cases. The public developer portal documents a REST (OpenAPI 3.0.1) Chart Retrieval API secured with OAuth2 client-credentials plus an x-api-key header; retrieved charts are returned to a predetermined location via SFTP. Moxe is HIPAA and SOC 2 Type 2 compliant and was named number 1 Best in KLAS for Payer-Provider
  Data Exchange. The documented API is REST/JSON rather than HL7 FHIR, and full access is granted through a partner onboarding agreement.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: moxe-health-mcp.yml
  slug: moxe-health-mcpyml
modified: '2026-07-24T12:00:00Z'
name: Moxe Health
nav: Providers
network: true
overview: 'Moxe Health publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chart Retrieval API and Claim Management API. Tagged areas include Healthcare, United States, Interoperability, Clinical Data, and Payer.


  Moxe Health''s developer surface includes authentication, documentation, getting-started guide, API reference, signup flow, engineering blog, support, and 30 more developer resources.'
random_paper: 72
scopes:
- name: Moxe Health Scopes
  scope_count: 4
  slug: moxe-health-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 50.7
  delta: -2.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.2
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 15.8
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moxe-health/refs/heads/main/screenshots/moxe-health-2026-08-07T184405.png
security:
- kind: authentication
  name: Moxe Health Authentication
  slug: moxe-health-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Moxe Health Domain Security
  slug: moxe-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Moxe Health Vulnerability Disclosure
  slug: moxe-health-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
- kind: trust-center
  name: Moxe Health Trust Center
  slug: moxe-health-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: moxe-health
tags:
- Healthcare
- United States
- Interoperability
- Clinical Data
- Payer
- Provider
- EHR
- Health Data Exchange
- Claims
- Risk Adjustment
website: https://moxehealth.com/
---

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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Kno2 Agentic Access
  operation_count: 12
  slug: kno2-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- description: HL7 FHIR (DSTU3/R4) resource query and retrieval at scale, including USCDI data classes and patient demographic search, brokered through Kno2's gateway to Carequality and national FHIR endpoints. MODE
  name: Kno2 FHIR API
  slug: kno2-fhir-api
- description: On-demand patient record location and retrieval across national networks - Kno2's private network, Carequality, eHealth Exchange, and TEFCA (Kno2 is a designated QHIN). Find a patient, query participa
  name: Kno2 Patient Record Query API
  slug: kno2-record-query-api
- baseURL: https://{subscription}.kno2fy.com
  baseurl_source: declared
  description: Upload, retrieve, and mark clinical document attachments.
  name: Kno2 Attachments API
  slug: kno2-attachments-api
- baseURL: https://{subscription}.kno2fy.com
  baseurl_source: declared
  description: OAuth2 client-credentials token issuance.
  name: Kno2 Authentication API
  slug: kno2-authentication-api
- baseURL: https://{subscription}.kno2fy.com
  baseurl_source: declared
  description: Validate Direct addresses and list document types.
  name: Kno2 Directory API
  slug: kno2-directory-api
- baseURL: https://{subscription}.kno2fy.com
  baseurl_source: declared
  description: RECEIVE surface - search, retrieve, and process inbound messages.
  name: Kno2 Intake API
  slug: kno2-intake-api
- baseURL: https://{subscription}.kno2fy.com
  baseurl_source: declared
  description: SEND surface - draft, populate, attach, and send messages.
  name: Kno2 Messaging API
  slug: kno2-messaging-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kno2 Communication Attachments API
  slug: open-kno2-attachments-api
- collection_type: open
  name: Kno2 Communication Attachments Authentication API
  slug: open-kno2-authentication-api
- collection_type: open
  name: Kno2 Communication Attachments Directory API
  slug: open-kno2-directory-api
- collection_type: open
  name: Kno2 Communication Attachments Intake API
  slug: open-kno2-intake-api
- collection_type: open
  name: Kno2 Communication Attachments Messaging API
  slug: open-kno2-messaging-api
- collection_type: open
  name: Kno2 Communication API
  slug: open-kno2
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kno2-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Kno2/Kno2.ApiTestClient/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/Kno2/Kno2.ApiTestClient/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kno2-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kno2-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kno2-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kno2
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kno2
- group: company
  title: ''
  type: Website
  url: https://kno2.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kno2.com
- group: commercial
  title: ''
  type: Plans
  url: plans/kno2-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kno2-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kno2-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kno2.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.kno2.com
- group: operate
  title: ''
  type: Support
  url: https://kno2.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://kno2.com/resources/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kno2.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kno2.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://kno2.com/request-a-demo/
- group: build
  title: ''
  type: Packages
  url: packages/kno2-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kno2-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kno2-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/kno2-attachments-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kno2-authentication-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kno2-directory-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kno2-intake-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kno2-messaging-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/kno2-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kno2-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kno2-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kno2.com
- group: design
  title: ''
  type: Conventions
  url: conventions/kno2-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kno2-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/kno2-send-a-message.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/kno2-process-inbound-message.md
created: '2026-07-12'
description: Kno2 provides Interoperability as a Service for healthcare - a single Communication API to SEND, RECEIVE, and FIND patient information across the healthcare ecosystem. One connection reaches Direct Secure Messaging, clinical document exchange, HL7 FHIR resources, HL7 V2.x, cloud fax, and national record location and retrieval through Kno2's private network, Carequality, eHealth Exchange, and TEFCA (Kno2 is a federally designated QHIN). API access is partner/enterprise gated - integrators are provisioned a per-subscription tenant host with OAuth2 client-credentials keys and an IP allowlist; a staging sandbox is available through the Kno2 Developer Program.
finops:
- name: Kno2 Finops
  service_category: Healthcare Interoperability
  slug: kno2-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kno2.png
layout: provider
mcp_servers:
- description: ''
  name: Kno2 MCP Server
  slug: kno2-mcp-server
modified: '2026-08-14'
name: Kno2
nav: Providers
network: true
overview: 'Kno2 publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Attachments API, Authentication API, Directory API, and 2 more. Tagged areas include Healthcare Interoperability, Clinical Records, Health Information Exchange, Direct Secure Messaging, and FHIR.


  Kno2''s developer surface includes authentication, documentation, API reference, support, engineering blog, signup flow, and 30 more developer resources.'
plans:
- name: Kno2 Plans Pricing
  plan_count: 2
  slug: kno2-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Kno2 Rate Limits
  slug: kno2-rate-limits
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 22
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 30.3
    commercial_clarity: 30.3
    contract_governance: 4.5
    contract_quality: 56.5
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kno2/refs/heads/main/screenshots/kno2-2026-07-25T224009.png
security:
- kind: authentication
  name: Kno2 Authentication
  slug: kno2-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Kno2 Domain Security
  slug: kno2-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kno2
tags:
- Healthcare Interoperability
- Clinical Records
- Health Information Exchange
- Direct Secure Messaging
- FHIR
- Clinical Documents
- Patient Records
- Healthcare
- HIE
- Care Coordination
- QHIN
- TEFCA
- Carequality
website: https://kno2.com
---

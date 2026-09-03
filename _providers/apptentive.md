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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apptentive Agentic Access
  operation_count: 36
  slug: apptentive-agentic-access
  summary_line: 36 operations · 1 acting
api_count: 1
apis:
- baseURL: https://data.apptentive.com
  baseurl_source: declared
  description: experimental data endpoints
  name: Apptentive experimental API
  slug: apptentive-experimental-api
- baseURL: https://data.apptentive.com
  baseurl_source: declared
  description: info endpoints
  name: Apptentive info API
  slug: apptentive-info-api
- baseURL: https://data.apptentive.com
  baseurl_source: declared
  description: metrics data endpoints
  name: Apptentive metrics API
  slug: apptentive-metrics-api
- baseURL: https://data.apptentive.com
  baseurl_source: declared
  description: raw data endpoints
  name: Apptentive raw API
  slug: apptentive-raw-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: public-api-service experimental API
  slug: open-apptentive-experimental-api
- collection_type: open
  name: public-api-service experimental info API
  slug: open-apptentive-info-api
- collection_type: open
  name: public-api-service experimental metrics API
  slug: open-apptentive-metrics-api
- collection_type: open
  name: public-api-service experimental raw API
  slug: open-apptentive-raw-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/apptentive-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apptentive-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apptentive-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apptentive-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/apptentive-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/apptentive-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/apptentive-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apptentive-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/apptentive-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apptentive-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.alchemer.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/apptentive-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apptentive-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.apptentive.com
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.alchemer.com/help/alchemer-digital-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apptentive
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alchemer.com/apptentive-master-service-agreement/
- group: operate
  title: ''
  type: Support
  url: https://help.alchemer.com/
- group: company
  title: ''
  type: Blog
  url: https://www.alchemer.com/resources/blog/
- group: company
  title: ''
  type: Website
  url: http://apptentive.com
created: '2026-07-17'
description: Apptentive, now Alchemer Mobile / Alchemer Digital, is a mobile customer engagement and in-app feedback platform used to run surveys, message prompts (Notes), ratings/review prompts, and Fan Signals inside iOS, Android, React Native, and web apps. Its public Data API at data.apptentive.com gives customers read-only export and analytics access to app metrics (active users, retention, Love Percent, Net Fan Score, ratings, reviews), survey and note reporting, and raw people, device, conversation, and message records, plus a GDPR/CCPA data-request endpoint. Authentication is an X-API-KEY header issued and scoped from the Alchemer Digital dashboard; the service is SOC 2 Type 2 and ISO 27001 certified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apptentive.png
layout: provider
modified: '2026-07-18'
name: Apptentive
nav: Providers
network: true
overview: 'Apptentive publishes 4 APIs on the [APIs.io](https://apis.io/) network, including experimental API, info API, metrics API, and 1 more. Tagged areas include Company, Enterprise, Mobile, Customer Feedback, and Surveys.


  Apptentive''s developer surface includes authentication, documentation, support, engineering blog, and 17 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Apptentive Rate Limits
  slug: apptentive-rate-limits
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 52.4
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 40.8
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apptentive/refs/heads/main/screenshots/apptentive-2026-07-25T200848.png
security:
- kind: authentication
  name: Apptentive Authentication
  slug: apptentive-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apptentive Domain Security
  slug: apptentive-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Apptentive Trust Center
  slug: apptentive-trust-center
  summary_line: AICPA SOC 2 Type 2, ISO 27001, GDPR, CCPA, HIPAA, FERPA
slug: apptentive
tags:
- Company
- Enterprise
- Mobile
- Customer Feedback
- Surveys
- Analytics
- Customer Engagement
- Voice of Customer
website: http://apptentive.com
---

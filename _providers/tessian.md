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
  - '{''url'': ''https://www.tessian.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.proofpoint.com/us/tessian-is-now-proofpoint — a different registrable domain (tessian.com -> proofpoint.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Tessian Agentic Access
  operation_count: 13
  slug: tessian-agentic-access
  summary_line: 13 operations · 5 acting
api_count: 1
apis:
- baseURL: https://your-domain.tessian-platform.com
  baseurl_source: declared
  description: The Beta Endpoints API from Tessian — 1 operation(s) for beta endpoints.
  name: Tessian Beta Endpoints API
  slug: tessian-beta-endpoints-api
- baseURL: https://your-domain.tessian-platform.com
  baseurl_source: declared
  description: The Endpoints API from Tessian — 9 operation(s) for endpoints.
  name: Tessian Endpoints API
  slug: tessian-endpoints-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tessian Anomalies API
  slug: open-tessian-anomalies-api
- collection_type: open
  name: Tessian Anomalies Audits API
  slug: open-tessian-audits-api
- collection_type: open
  name: Tessian Anomalies Beta Endpoints API
  slug: open-tessian-beta-endpoints-api
- collection_type: open
  name: Tessian Anomalies Deprecated API
  slug: open-tessian-deprecated-api
- collection_type: open
  name: Tessian Anomalies Endpoints API
  slug: open-tessian-endpoints-api
- collection_type: open
  name: Tessian Anomalies Events API
  slug: open-tessian-events-api
- collection_type: open
  name: Tessian Anomalies Groups API
  slug: open-tessian-groups-api
- collection_type: open
  name: Tessian Anomalies Monitoring API
  slug: open-tessian-monitoring-api
- collection_type: open
  name: Tessian Anomalies Risk API
  slug: open-tessian-risk-api
- collection_type: open
  name: Tessian Anomalies Triggers API
  slug: open-tessian-triggers-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tessian.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tessian.com/documentation/api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.tessian.com/documentation/api/index.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/tessian-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tessian-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tessian-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tessian-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tessian-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tessian-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/tessian-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tessian-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/tessian-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tessian-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tessian-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tessian
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.proofpoint.com/us/legal/api-terms-of-use
- group: operate
  title: ''
  type: Support
  url: mailto:support@tessian.com
- group: company
  title: ''
  type: Website
  url: https://www.tessian.com
created: '2026-07-17'
description: Tessian, now part of Proofpoint, is an AI-powered email security platform that protects against inbound threats (phishing and impersonation), accidental data loss, and deliberate data exfiltration across its Defender, Guardian, Enforcer, Architect, and Constructor modules. The Tessian API is a RESTful, JSON, read-oriented interface that exports security-event, anomaly, company-risk, user-monitoring, audit-log, and trigger data into SIEMs and other data-management tools. It authenticates with a static API token, paginates by checkpoint, and returns ISO 8601 UTC timestamps.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tessian.png
layout: provider
modified: '2026-07-21'
name: Tessian
nav: Providers
network: true
overview: 'Tessian publishes 2 APIs on the [APIs.io](https://apis.io/) network: Beta Endpoints API and Endpoints API. Tagged areas include Company, Enterprise, Email Security, Cybersecurity, and Data Loss Prevention.


  Tessian''s developer surface includes documentation, API reference, authentication, support, and 15 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 51.8
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tessian/refs/heads/main/screenshots/tessian-2026-09-02T163217.png
security:
- kind: authentication
  name: Tessian Authentication
  slug: tessian-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tessian Domain Security
  slug: tessian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tessian
tags:
- Company
- Enterprise
- Email Security
- Cybersecurity
- Data Loss Prevention
- SIEM
- Security
- Phishing
website: https://www.tessian.com
---

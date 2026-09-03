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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Taskcall Agentic Access
  operation_count: 24
  slug: taskcall-agentic-access
  summary_line: 24 operations · 23 acting
api_count: 1
apis:
- description: 'REST API for creating, updating, and managing incidents in TaskCall. Authentication uses API keys passed in the Authorization header as "Authorization: token <api_key>", with optional IP allowlisting '
  name: TaskCall Incidents API
  slug: incidents-api
- baseURL: https://incidents-api.taskcallapp.com
  baseurl_source: declared
  description: The Components API from TaskCall — 1 operation(s) for components.
  name: TaskCall Components API
  slug: taskcall-components-api
- baseURL: https://incidents-api.taskcallapp.com
  baseurl_source: declared
  description: The Incidents API from TaskCall — 23 operation(s) for incidents.
  name: TaskCall Incidents API
  slug: taskcall-incidents-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TaskCall Incidents Components API
  slug: open-taskcall-components-api
- collection_type: open
  name: TaskCall Components Incidents API
  slug: open-taskcall-incidents-api
- collection_type: open
  name: TaskCall Incidents API
  slug: open-taskcall
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/taskcall-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/taskcall-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taskcall-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/taskcall-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taskcallapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/taskcall
- group: company
  title: ''
  type: Website
  url: https://taskcallapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.taskcallapp.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://taskcallapp.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.us.taskcallapp.com/signup
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.taskcallapp.com/llms.txt
created: '2026-05-11'
description: TaskCall is an incident management and on-call alerting platform for DevOps, SRE, and IT teams that centralizes alerts from monitoring tools, manages on-call schedules, escalation policies, status pages, and post-incident analysis. The platform provides automated incident triggers, integrations with monitoring and ITSM tools, and IP-restricted API key access. TaskCall exposes a REST API for managing incidents and related resources using token-based authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taskcall.png
layout: provider
modified: '2026-05-11'
name: TaskCall
nav: Providers
network: true
overview: 'TaskCall publishes 2 APIs on the [APIs.io](https://apis.io/) network: Components API and Incidents API. Tagged areas include Incident Management, On-Call, Alerting, DevOps, and SRE.


  TaskCall''s developer surface includes authentication, documentation, pricing, signup flow, and 7 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/taskcall/refs/heads/main/screenshots/taskcall-2026-06-20T194924.png
security:
- kind: authentication
  name: Taskcall Authentication
  slug: taskcall-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Taskcall Domain Security
  slug: taskcall-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Taskcall Trust Center
  slug: taskcall-trust-center
  summary_line: SOC 2, HIPAA
slug: taskcall
tags:
- Incident Management
- On-Call
- Alerting
- DevOps
- SRE
- ITSM
website: https://taskcallapp.com/
---

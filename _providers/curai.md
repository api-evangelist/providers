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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Curai Agentic Access
  operation_count: 2
  slug: curai-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://gateway.curaihealth.com/partner
  baseurl_source: declared
  description: The Partner API from Curai — 2 operation(s) for partner.
  name: Curai Partner API
  slug: curai-partner-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Curai Partner API
  slug: open-curai-partner-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/curai-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/curai-partner-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.curaihealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gateway.curaihealth.com/partner/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.curaihealth.com/sdk-quickstart-guide
- group: start
  title: ''
  type: GettingStarted
  url: https://www.curaihealth.com/sdk-quickstart-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/curai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curaihealth.com/terms-of-use
- group: build
  title: ''
  type: Packages
  url: packages/curai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/curai-packages.yml
- group: design
  title: ''
  type: Components
  url: components/curai-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/curai-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/curai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/curai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/curai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/curai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/curai-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/curai-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curai-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/curai-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/curai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/curai-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/curai-agentic-access.yml
created: '2026-07-17'
description: Curai Health is a virtual-first primary care company offering 24/7 text-based telemedicine to patients across all 50 U.S. states, connecting them with board-certified clinicians for urgent care, chronic disease management, wellness, and preventive screenings, with orders for labs and prescriptions and referrals to specialists. For organizations, health systems, TPAs, and benefits administrators, Curai exposes a Partner API and an embeddable Web SDK (curai-js) that let partners register patients and drop the Curai patient experience into their own web and mobile apps, plus integration via standards-based APIs, Health Information Exchanges (HIE), and webhooks. The Partner API is a small, key-authenticated surface used to onboard patients and obtain session access tokens for the embedded experience.
image: https://cdn.prod.website-files.com/619acca858666ac6759d6e31/61d79c66ae46600b755a13be_logo_webclip.png
layout: provider
modified: '2026-07-18'
name: Curai
nav: Providers
network: true
overview: 'Curai publishes 1 API on the [APIs.io](https://apis.io/) network: Partner API. Tagged areas include Company, Health, Healthcare, Telemedicine, and Telehealth.


  Curai''s developer surface includes documentation, getting-started guide, authentication, sandbox, and 20 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 49.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/curai/refs/heads/main/screenshots/curai-2026-07-25T210929.png
security:
- kind: authentication
  name: Curai Authentication
  slug: curai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Curai Domain Security
  slug: curai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curai
tags:
- Company
- Health
- Healthcare
- Telemedicine
- Telehealth
- Primary Care
- Digital Health
- Patient Engagement
- Partner API
- SDK
website: https://www.curaihealth.com/
---

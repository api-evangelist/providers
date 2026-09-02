---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 21.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Mytomorrows Agentic Access
  operation_count: 42
  slug: mytomorrows-agentic-access
  summary_line: 42 operations · 33 acting
api_count: 1
apis:
- description: The Legacy GraphQL Proxy API from myTomorrows — 1 operation(s) for legacy graphql proxy.
  name: myTomorrows Legacy GraphQL Proxy API
  slug: mytomorrows-legacy-graphql-proxy-api
- description: The Public API from myTomorrows — 1 operation(s) for public.
  name: myTomorrows Public API
  slug: mytomorrows-public-api
- description: The System API from myTomorrows — 2 operation(s) for system.
  name: myTomorrows System API
  slug: mytomorrows-system-api
- description: The V1 API from myTomorrows — 38 operation(s) for v1.
  name: myTomorrows V1 API
  slug: mytomorrows-v1-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Enterprise Search Legacy GraphQL Proxy API
  slug: open-mytomorrows-legacy-graphql-proxy-api
- collection_type: open
  name: Enterprise Search Legacy GraphQL Proxy Public API
  slug: open-mytomorrows-public-api
- collection_type: open
  name: Enterprise Search Legacy GraphQL Proxy System API
  slug: open-mytomorrows-system-api
- collection_type: open
  name: Enterprise Search Legacy GraphQL Proxy V1 API
  slug: open-mytomorrows-v1-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/mytomorrows-enterprise-search-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://mytomorrows.com/en/
- group: company
  title: ''
  type: Blog
  url: https://mytomorrows.com/en/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mytomorrows.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mytomorrows.com/en/privacy-statement
- group: auth
  title: ''
  type: TrustCenter
  url: security/mytomorrows-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mytomorrows.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mytomorrows-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mytomorrows-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mytomorrows-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mytomorrows-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mytomorrows-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mytomorrows-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mytomorrows-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mytomorrows-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mytomorrows-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/mytomorrows-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mytomorrows-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/myTomorrows
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mytomorrows.com/enterprise/api-beta-program/
- group: start
  title: ''
  type: SignUp
  url: https://mytomorrows.com/enterprise/api-beta-program/
created: '2026-07-17'
description: myTomorrows is a healthcare technology platform that helps patients and healthcare professionals discover and access clinical trials and expanded-access (pre-approval) treatment options, and helps biopharma companies run and manage expanded-access programs (EAPs), collect real-world data, and recruit trial patients. Founded in 2012 by Dr. Ronald Brus, the company operates in roughly 50 countries. Its Trial Search AI product is backed by a FastAPI "Enterprise Search API" that generates Trial Search Reports (TSR), resolves conditions, and searches studies. This profile was surfaced as a portfolio company of Balderton Capital and enriched by the API Evangelist pipeline from a harvested OpenAPI and public trust surface.
image: https://mytomorrows.com/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: myTomorrows MCP Server
  slug: mytomorrows-mcp-server
modified: '2026-07-20'
name: myTomorrows
nav: Providers
network: true
overview: 'myTomorrows publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Legacy GraphQL Proxy API, Public API, System API, and 1 more. Tagged areas include Company, Healthcare, Clinical Trials, Expanded Access, and Pharmaceuticals.


  myTomorrows'' developer surface includes engineering blog, signup flow, and 20 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 46.3
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mytomorrows/refs/heads/main/screenshots/mytomorrows-2026-08-07T184546.png
security:
- kind: domain-security
  name: Mytomorrows Domain Security
  slug: mytomorrows-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mytomorrows Trust Center
  slug: mytomorrows-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR
slug: mytomorrows
tags:
- Company
- Healthcare
- Clinical Trials
- Expanded Access
- Pharmaceuticals
- Patient Access
- Life Sciences
- Search
- Artificial Intelligence
website: https://mytomorrows.com/en/
---

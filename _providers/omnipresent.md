---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/omnipresent-stock
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OmnipresentGroup
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/omnipresent-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omnipresent-domain-security.yml
coverage:
  checked: '2026-08-26'
  detail: Omnipresent was acquired by Deel in October 2025 and its entire web presence has been switched off — omnipresent.com keeps its Route 53 delegation and Google Workspace mail records but publishes no A record, so all 45 discovery probes across omnipresent.com, www.omnipresent.com and omnipresent.group (well-known, agent-card, openapi, swagger, graphql, mcp, llms.txt) failed at DNS resolution rather than returning any HTTP status.
  evidence:
  - status: 0
    url: https://omnipresent.com/
  - status: 0
    url: https://omnipresent.com/openapi.json
  - status: 0
    url: https://omnipresent.com/.well-known/agent-card.json
  - status: 0
    url: https://www.omnipresent.com/.well-known/security.txt
  - status: 0
    url: https://omnipresent.group/openapi.json
  - status: 200
    url: https://github.com/OmnipresentGroup
  - status: 200
    url: https://www.hiive.com/securities/omnipresent-stock
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Omnipresent was a London-headquartered global employment company, founded in 2019 by Matthew Wilson and Guenther Eisinger, that acted as an Employer of Record so companies could hire, onboard, pay and manage employees and contractors in countries where they had no legal entity. Its platform handled local employment contracts, payroll, benefits, expenses and tax and labour compliance across more than 160 countries, and it sold packaged integrations with HR and payroll systems alongside an account-scoped REST API for custom integration work. The company raised roughly $138M, including a $120M Series B in March 2022 led by Kinnevik and Tencent, and was acquired by its competitor Deel in October 2025, after which clients, employees and contractors were migrated onto the Deel platform. Omnipresent never published a public developer portal, API reference or machine-readable specification, and its web presence has since been decommissioned: omnipresent.com now publishes only NS and
  Google Workspace MX records with no A record, www.omnipresent.com is NXDOMAIN, and the original omnipresent.group domain SERVFAILs at the registry. The company''s GitHub organization is still public but holds four forks and one archived internal tech-radar CSV, with no API contract of any kind. This profile is retained as a historical record; there is no API surface left to enrich.'
image: https://avatars.githubusercontent.com/u/61059189?v=4
layout: provider
modified: '2026-08-26'
name: Omnipresent
nav: Providers
network: true
overview: Omnipresent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, Employment, Payroll, and Employer of Record.
random_paper: 7
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omnipresent/refs/heads/main/screenshots/omnipresent-2026-09-02T150843.png
security:
- kind: domain-security
  name: Omnipresent Domain Security
  slug: omnipresent-domain-security
  summary_line: no transport/DNS hardening detected
slug: omnipresent
tags:
- Company
- Human Resources
- Employment
- Payroll
- Employer of Record
- Global Employment
- Remote Work
- Compliance
- Benefits
- Acquired
- Defunct
---

---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tydo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tydo.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tydo
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tydo-llms.txt
created: '2026-07-17'
description: 'Tydo delivers autonomous audits for Shopify stores inside Claude. A single integration runs hundreds of audits - retention, shipping, email and SMS, and more - scoring a store against similar brands in its network, re-running on a cadence in the background, and routing every finding to a next step: fix it yourself, turn on an agent, or get matched to a vetted partner via dtcmvp. A Greylock portfolio company, currently waitlist-only with no public developer portal, API documentation, or published MCP endpoint.'
image: https://tydo.com/icon.svg
layout: provider
modified: '2026-07-21'
name: Tydo
nav: Providers
network: true
overview: Tydo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Application, Shopify, E-Commerce, and Audits.
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
  previous_composite: 5.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tydo/refs/heads/main/screenshots/tydo-2026-09-02T164647.png
security:
- kind: domain-security
  name: Tydo Domain Security
  slug: tydo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tydo
tags:
- Company
- Application
- Shopify
- E-Commerce
- Audits
- AI Agents
- Analytics
website: https://tydo.com/
---

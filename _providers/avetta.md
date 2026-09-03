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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 10.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'Avetta''s Open API surface, documented through the Avetta Developer Portal, lets client organizations select contractor and supplier endpoints and customize data synchronization between the Avetta One '
  name: Avetta Developer API
  slug: avetta-developer-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/avetta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avetta.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.avetta.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.avetta.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.avetta.com
- group: company
  title: ''
  type: Blog
  url: https://www.avetta.com/blog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.avetta.com
- group: start
  title: ''
  type: Login
  url: https://app.avetta.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.avetta.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.avetta.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.avetta.com/legal/master-subscription-agreement
- group: agent
  title: ''
  type: WellKnown
  url: well-known/avetta-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/avetta-llms.txt
created: '2026-07-17'
description: Avetta operates a cloud-based supply chain risk management (SCRM) and contractor compliance platform, Avetta One, used by more than 360,000 businesses across 120+ countries to prequalify, audit, and continuously monitor contractors and suppliers. The platform spans health and safety compliance, prequalification, worker management, sustainability and ESG (GHG reporting, supplier diversity, supplier ESG due diligence), and business risk (financial, cybersecurity, and insurance verification). Avetta exposes an Open API and ERP connectors through a developer portal (docs.api.avetta.com) so client organizations can synchronize contractor and supplier data into Salesforce, Oracle, Workday, ServiceNow, and internal systems. Avetta is a portfolio company of Norwest Venture Partners.
image: https://cdn.prod.website-files.com/696fddc24f2e82c416e23640/697ba15528499b3ced513224_hero-opg.png
layout: provider
modified: '2026-07-18'
name: Avetta
nav: Providers
network: true
overview: 'Avetta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain, Risk Management, Compliance, and Contractor Management.


  Avetta''s developer surface includes documentation, engineering blog, support, and 10 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/avetta/refs/heads/main/screenshots/avetta-2026-07-25T201923.png
security:
- kind: domain-security
  name: Avetta Domain Security
  slug: avetta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avetta
tags:
- Company
- Supply Chain
- Risk Management
- Compliance
- Contractor Management
- Safety
- ESG
- Supplier Management
website: https://avetta.com
---

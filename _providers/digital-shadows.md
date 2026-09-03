---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: 'The Digital Shadows SearchLight Portal API — the REST surface behind the SearchLight / GreyMatter DRP portal. Exposes incidents, intelligence incidents, intelligence threats, data breaches and breach '
  name: SearchLight Portal API
  slug: searchlight-portal-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digital-shadows-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://reliaquest.com/solutions/digital-risk-protection/
- group: start
  title: ''
  type: Portal
  url: https://portal-digitalshadows.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digitalshadows
- group: company
  title: ''
  type: Blog
  url: https://reliaquest.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reliaquest.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.digitalshadows.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/digital-shadows-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/digital-shadows-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/digital-shadows-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/digital-shadows-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/digital-shadows-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/digital-shadows-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/digital-shadows-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/digital-shadows-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/digital-shadows-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/digital-shadows-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/digital-shadows-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/digital-shadows-rate-limits.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/digital-shadows_stock/
created: '2026-08-12'
description: Digital Shadows is a London-founded digital risk protection (DRP) company whose SearchLight platform monitors the open, deep and dark web for data leakage, exposed credentials, brand impersonation, exposed infrastructure and threat-actor activity affecting a customer's organization. ReliaQuest acquired Digital Shadows in July 2022 and the entity now trades as ReliaQuest UK Limited, with SearchLight folded into ReliaQuest GreyMatter Digital Risk Protection. The SearchLight Portal API remains live at portal-digitalshadows.com/api/ and is consumed by first-party tooling (the shadowline Python CLI and the Splunk SOAR connector) and by a wide third-party integration surface (Cortex XSOAR, ThreatConnect, Splunk, Sekoia, Axonius, TheHive, Atlassian Marketplace). The API reference itself is published only inside the authenticated customer portal.
image: https://avatars.githubusercontent.com/u/11042971?v=4
layout: provider
modified: '2026-08-12'
name: Digital Shadows
nav: Providers
network: true
overview: 'Digital Shadows publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Threat Intelligence, Digital Risk Protection, and Dark Web Monitoring.


  Digital Shadows'' developer surface includes developer portal, engineering blog, CLI, authentication, and 16 more developer resources.'
plans:
- name: Digital Shadows Plans Pricing
  plan_count: 0
  slug: digital-shadows-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Digital Shadows Rate Limits
  slug: digital-shadows-rate-limits
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 19.5
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digital-shadows/refs/heads/main/screenshots/digital-shadows-2026-09-02T145238.png
security:
- kind: authentication
  name: Digital Shadows Authentication
  slug: digital-shadows-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Digital Shadows Domain Security
  slug: digital-shadows-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digital-shadows
tags:
- Company
- Cybersecurity
- Threat Intelligence
- Digital Risk Protection
- Dark Web Monitoring
- Data Breach
- Brand Protection
- Security Operations
- Vulnerability Intelligence
website: https://reliaquest.com/solutions/digital-risk-protection/
---

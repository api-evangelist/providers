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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: Submit customers, designs and pricing into Palmetto's transparent, auditable clean-energy fulfillment pipeline.
  name: Palmetto Energy Platform API
  slug: palmetto-energy-platform-api
- description: Finance solar, storage and other clean-energy projects; includes contracts, documents, organizations, users and a webhook event surface.
  name: Palmetto Finance (LightReach) API
  slug: palmetto-finance-lightreach-api
- baseURL: https://ei.palmetto.com
  baseurl_source: declared
  description: The Bem API from Palmetto — 1 operation(s) for bem.
  name: Palmetto Bem API
  slug: palmetto-bem-api
- baseURL: https://ei.palmetto.com
  baseurl_source: declared
  description: The Health API from Palmetto — 1 operation(s) for health.
  name: Palmetto Health API
  slug: palmetto-health-api
artifact_total: 10
asyncapis:
- description: ''
  name: Palmetto Finance Webhooks
  slug: palmetto-finance-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Palmetto Energy Intelligence Bem API
  slug: open-palmetto-bem-api
- collection_type: open
  name: Palmetto Energy Intelligence Bem Health API
  slug: open-palmetto-health-api
common:
- group: company
  title: ''
  type: Website
  url: https://palmetto.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.palmetto.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.palmetto.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.palmetto.com/energy/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://help.palmetto.com
- group: company
  title: ''
  type: Blog
  url: https://palmetto.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/palmetto
- group: operate
  title: ''
  type: StatusPage
  url: https://status.palmetto.com
- group: commercial
  title: ''
  type: Pricing
  url: https://palmetto.com/business/energy-intelligence-api
- group: start
  title: ''
  type: SignUp
  url: https://ei.docs.palmetto.com/docs/getting-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://palmetto.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://palmetto.com/legal/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/authentication/palmetto-authentication.yml
  title: ''
  type: Authentication
  url: authentication/palmetto-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/security/palmetto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/palmetto-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/packages/palmetto-packages.yml
  title: ''
  type: Packages
  url: packages/palmetto-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/components/palmetto-components.yml
  title: ''
  type: Components
  url: components/palmetto-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/well-known/palmetto-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/palmetto-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/mcp/palmetto-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/palmetto-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/llms/palmetto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/palmetto-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/overlays/palmetto-energy-intelligence-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/palmetto-energy-intelligence-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/conformance/palmetto-conformance.yml
  title: ''
  type: Conformance
  url: conformance/palmetto-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/errors/palmetto-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/palmetto-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/lifecycle/palmetto-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/palmetto-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/sandbox/palmetto-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/palmetto-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/conventions/palmetto-conventions.yml
  title: ''
  type: Conventions
  url: conventions/palmetto-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/data-model/palmetto-data-model.yml
  title: ''
  type: DataModel
  url: data-model/palmetto-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/asyncapi/palmetto-finance-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/palmetto-finance-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/skills/palmetto-model-home-energy.md
  title: ''
  type: AgentSkill
  url: skills/palmetto-model-home-energy.md
created: '2026-07-17'
description: 'Palmetto is a clean-energy technology company that helps homeowners and partners adopt solar, HVAC, battery storage, water heaters and financing. For developers and technology partners it publishes three API products under docs.palmetto.com: the Energy Intelligence API (physics-based building energy modeling and solar simulation for any US home, down to hourly granularity and disaggregated to end use), the Energy Platform API (submit customers, designs and pricing into Palmetto''s fulfillment pipeline), and the Finance (LightReach) API for financing clean-energy projects, complete with webhooks. Backed by Social Capital.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/palmetto.png
layout: provider
modified: '2026-07-20'
name: Palmetto
nav: Providers
network: true
overview: 'Palmetto publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Bem API, Health API, and 2 more. Tagged areas include Company, Clean Energy, Solar, Energy, and Building Energy Modeling.


  The Palmetto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Palmetto''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, authentication, and 21 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 56.4
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 50.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/palmetto/refs/heads/main/screenshots/palmetto-2026-08-07T191322.png
security:
- kind: authentication
  name: Palmetto Authentication
  slug: palmetto-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Palmetto Domain Security
  slug: palmetto-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: palmetto
tags:
- Company
- Clean Energy
- Solar
- Energy
- Building Energy Modeling
- Home Energy
- Financing
- Sustainability
website: https://palmetto.com
---

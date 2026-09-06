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
  score: 18.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 2
  name: Brainbase Agentic Access
  operation_count: 4
  slug: brainbase-agentic-access
  summary_line: 4 operations · 2 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.brainbase.com
  baseurl_source: declared
  description: ApiContractController endpoints
  name: Brainbase ApiContract API
  slug: brainbase-apicontract-api
- baseURL: https://api.brainbase.com
  baseurl_source: declared
  description: GeneralController endpoints
  name: Brainbase General API
  slug: brainbase-general-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API v1 ApiContract API
  slug: open-brainbase-apicontract-api
- collection_type: open
  name: API v1 ApiContract General API
  slug: open-brainbase-general-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brainbase-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brainbase-conventions.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/brainbase-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brainbase-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/brainbase-openapi-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/brainbase-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brainbase-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brainbase-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brainbase-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.brainbase.com/
- group: start
  title: ''
  type: Login
  url: https://app.brainbase.com/
created: '2026-07-17'
description: Brainbase is a modern, end-to-end brand-licensing and intellectual-property management platform used by global licensing businesses to run their licensing, partnership and sponsorship programs from a single system of record. The product covers the full IP lifecycle — trademarks, patents, copyrights, licences, products and royalties — consolidating contract management, royalty calculation, sales-data reporting and contract-compliance workflows for brand owners, licensors and their partners. Founded in 2016 in Los Angeles by Nate Cavanaugh, Brainbase raised an $8M Series A in 2020 led by Bessemer Venture Partners and Nosara Capital, and was acquired by PYXiS Software Group (a division of Jonas Software) in 2022. The public marketing apex (www.brainbase.com) no longer resolves post-acquisition; the SaaS application remains live at app.brainbase.com and exposes a small public REST API (bearer/JWT) at api.brainbase.com with an auto-generated OpenAPI document at api.brainbase.com/docs.
  This profile was surfaced from the Bessemer Venture Partners portfolio and enriched by the API Evangelist pipeline from the live API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brainbase.png
layout: provider
modified: '2026-07-18'
name: Brainbase
nav: Providers
network: true
overview: 'Brainbase publishes 2 APIs on the [APIs.io](https://apis.io/) network: ApiContract API and General API. Tagged areas include Company, Cloud, Intellectual Property, Brand Licensing, and Licensing Management.


  Brainbase''s developer surface includes authentication and 11 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 45.2
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 24.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Brainbase Authentication
  slug: brainbase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Brainbase Domain Security
  slug: brainbase-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brainbase
tags:
- Company
- Cloud
- Intellectual Property
- Brand Licensing
- Licensing Management
- Royalties
- Contracts
- Trademarks
- Software-as-a-Service
website: https://www.brainbase.com/
---

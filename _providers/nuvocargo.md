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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuvocargo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nuvocargo.com
- group: company
  title: ''
  type: Blog
  url: https://www.nuvocargo.com/knowledge-hub
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.nuvocargo.com/product-updates
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nuvocargo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nuvocargo.com/privacy-policy
created: '2026-07-17'
description: Nuvocargo is an AI-powered freight-management platform for North American truckload logistics, focused on the US-Mexico-Canada cross-border corridor. Its "Nuvo AI" system coordinates a network of specialized agents (quoting, negotiation, booking, dispatch, tracking, exception handling, audit, and payment) to automate the freight load lifecycle, and it pairs that software with licensed freight brokerage, managed transportation, and customs-brokerage services. The company was surfaced through the API Evangelist network as a portfolio company of Homebrew and QED Investors. As of this enrichment pass Nuvocargo publishes no public developer API, OpenAPI specification, or developer portal; onboarding is contact-gated ("zero-integration" pilots), so this profile captures the company identity, legal/resource surface, and domain-security posture rather than API artifacts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nuvocargo.png
layout: provider
modified: '2026-07-20'
name: Nuvocargo
nav: Providers
network: true
overview: 'Nuvocargo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Freight, Supply Chain, and Cross-Border.


  Nuvocargo''s developer surface includes engineering blog, changelog, and 4 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 11.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuvocargo/refs/heads/main/screenshots/nuvocargo-2026-08-07T185806.png
security:
- kind: domain-security
  name: Nuvocargo Domain Security
  slug: nuvocargo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nuvocargo
tags:
- Company
- Logistics
- Freight
- Supply Chain
- Cross-Border
- Trucking
- Transportation
- Customs
- Artificial Intelligence
website: https://www.nuvocargo.com
---

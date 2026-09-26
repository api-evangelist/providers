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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nova/refs/heads/main/security/nova-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nova-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.novaintelligence.com/
- group: company
  title: ''
  type: Blog
  url: https://www.novaintelligence.com/blog
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.vanta.com/novasoftware.ai/trust/p83comjtnonkkjycksuelo
created: '2026-07-17'
description: Nova (Nova Intelligence) is an agentic AI platform for SAP teams, used in production across documentation, functional design, development, and production issue resolution. Its capabilities include code intelligence and system visibility, fit-to-standard analysis mapping custom code to SAP standard, development acceleration for ABAP Cloud and BTP CAP, S/4HANA and Clean Core transformation support, and security vulnerability identification, with claims of a 3x productivity boost at 50% lower cost. Nova is an enterprise, demo-led product with no public API, developer portal, or SDKs at this time; it is backed by Accel and Battery Ventures. This profile was enriched by the API Evangelist pipeline, which probed the company's public surface and found a domain-security posture and a Vanta trust center but no developer or API artifacts to harvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nova.png
layout: provider
modified: '2026-07-20'
name: Nova
nav: Providers
network: true
overview: 'Nova is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, SAP, AI Agents, and Enterprise Software.


  Nova''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 5.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nova Domain Security
  slug: nova-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nova
tags:
- Company
- Artificial Intelligence
- SAP
- AI Agents
- Enterprise Software
- Developer Productivity
- Code Intelligence
website: https://www.novaintelligence.com/
---

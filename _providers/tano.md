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
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Tano Agentic Access
  operation_count: 17
  slug: tano-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 1
apis:
- baseURL: https://tano.ai
  baseurl_source: spec
  description: Brand signups for product offerings (Creator Partnership Ads, Content Analysis Framework, Creator Discovery Guide, USA waitlist).
  name: Tano Brand Signups API
  slug: tano-brand-signups-api
- baseURL: https://tano.ai
  baseurl_source: spec
  description: Contact form submissions and updates.
  name: Tano Contact API
  slug: tano-contact-api
- baseURL: https://tano.ai
  baseurl_source: spec
  description: Creator-side signups.
  name: Tano Creator Signups API
  slug: tano-creator-signups-api
- baseURL: https://tano.ai
  baseurl_source: spec
  description: Static discovery files for AI agents (llms.txt, manifests, sitemap).
  name: Tano Discovery API
  slug: tano-discovery-api
- baseURL: https://tano.ai
  baseurl_source: spec
  description: Webinar and event registrations.
  name: Tano Events API
  slug: tano-events-api
artifact_total: 16
collections:
- collection_type: open
  name: Tano Public Brand Signups API
  slug: open-tano-brand-signups-api
- collection_type: open
  name: Tano Public Brand Signups Contact API
  slug: open-tano-contact-api
- collection_type: open
  name: Tano Public Brand Signups Creator Signups API
  slug: open-tano-creator-signups-api
- collection_type: open
  name: Tano Public Brand Signups Discovery API
  slug: open-tano-discovery-api
- collection_type: open
  name: Tano Public Brand Signups Events API
  slug: open-tano-events-api
common:
- group: company
  title: ''
  type: Blog
  url: https://www.tano.ai/blog/
- group: other
  href: https://artifacts.apis.io/tano/capabilities/tano-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tano-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/tano/skills/tano-agents.md
  title: ''
  type: AgentSkill
  url: skills/tano-agents.md
- group: agent
  href: https://artifacts.apis.io/tano/mcp/tano-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tano-mcp.yml
- group: other
  href: https://artifacts.apis.io/tano/overlays/tano-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tano-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/tano/a2a/tano-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tano-a2a.yml
- group: company
  title: ''
  type: Website
  url: http://tano.ai
- group: operate
  title: ''
  type: Support
  url: https://tano.ai/contact
created: '2026-07-17'
description: Tano is a company surfaced as a portfolio company of seedcamp and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: Remote MCP server at tano.ai over streamable HTTP; 4 tools listed.
  name: Tano
  slug: tano
modified: '2026-10-06'
name: Tano
nav: Providers
network: true
overview: 'Tano publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Brand Signups API, Contact API, Creator Signups API, and 2 more. Tagged areas include Company and A2A.


  Tano''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 15.0
    catalog_earned_first_party: 0.0
    catalog_gap: 100.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 46.6
    developer_ergonomics: 8.9
    discoverability: 28.3
    operational_transparency: 0.0
  previous_composite: 14.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tano/tano-2026-09-02T162520.png
security:
- kind: authentication
  name: Tano Authentication
  slug: tano-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Tano Domain Security
  slug: tano-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Sign up for a Tano playbook or product
  slug: tano-playbook-signup
- name: Submit a brand enquiry to Tano
  slug: tano-submit-brand-enquiry
slug: tano
tags:
- Company
- A2A
website: http://tano.ai
---

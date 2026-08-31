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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://nomadhomes.co/
- group: company
  title: ''
  type: Website
  url: https://www.getremy.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nomadhomes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getremy.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getremy.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@getremy.ai
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nomad-homes-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nomad-homes-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nomad-homes-domain-security.yml
created: '2026-07-17'
description: Nomad Homes is a Partech-backed proptech company originally launched as a real-estate marketplace. It has since rebranded and pivoted to RemyAI (getremy.ai) — "the 24/7 intelligent assistant for real estate agents." RemyAI listens to agents' calls and texts, transcribes and summarizes them, auto-creates follow-up tasks and reminders, organizes buyer/seller contacts, and manages voicemail across iOS, Android, and desktop. The company's original domain nomadhomes.co now 301-redirects to getremy.ai. RemyAI publishes a public /.well-known/ai-plugin.json and an llms.txt describing the product, but it exposes NO public developer API, SDK, OpenAPI, or developer portal (its ai-plugin manifest explicitly declares api.type=none and auth.type=none).
image: https://www.getremy.ai/remy_logo.png
layout: provider
modified: '2026-07-20'
name: Nomad Homes
nav: Providers
network: true
overview: 'Nomad Homes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Real-Estate, PropTech, and Artificial Intelligence.


  Nomad Homes'' developer surface includes support and 8 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 11.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nomad-homes/refs/heads/main/screenshots/nomad-homes-2026-08-07T185443.png
security:
- kind: domain-security
  name: Nomad Homes Domain Security
  slug: nomad-homes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nomad-homes
tags:
- Company
- Marketplace
- Real-Estate
- PropTech
- Artificial Intelligence
- AI Assistant
- Productivity
website: https://nomadhomes.co/
---

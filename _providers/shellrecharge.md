---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - '{''url'': ''https://shellrecharge.com'', ''status'': 307, ''note'': ''declared website redirects to https://www.shell.nl/elektrisch-opladen.html — a different registrable domain (shellrecharge.com -> shell.nl), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 2
  human_in_the_loop: 1
  name: Shellrecharge Agentic Access
  operation_count: 8
  slug: shellrecharge-agentic-access
  summary_line: 8 operations · 2 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.shell.com
  baseurl_source: declared
  description: The Locations API from ShellRecharge — 4 operation(s) for locations.
  name: ShellRecharge Locations API
  slug: shellrecharge-locations-api
- baseURL: https://api.shell.com
  baseurl_source: declared
  description: The Sessions API from ShellRecharge — 4 operation(s) for sessions.
  name: ShellRecharge Sessions API
  slug: shellrecharge-sessions-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ShellRecharge EV Platform Locations API
  slug: open-shellrecharge-locations-api
- collection_type: open
  name: ShellRecharge EV Platform Locations Sessions API
  slug: open-shellrecharge-sessions-api
- collection_type: open
  name: ShellRecharge EV Platform API
  slug: open-shellrecharge
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shellrecharge/refs/heads/main/capabilities/shellrecharge-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/shellrecharge-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shellrecharge/refs/heads/main/agentic-access/shellrecharge-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shellrecharge-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shellrecharge/refs/heads/main/security/shellrecharge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shellrecharge-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shellrecharge/refs/heads/main/authentication/shellrecharge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shellrecharge-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shellrecharge/refs/heads/main/scopes/shellrecharge-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/shellrecharge-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shellrecharge
- group: company
  title: ''
  type: Website
  url: https://shellrecharge.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shell.com/api-catalog
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/shellrecharge/refs/heads/main/plans/shellrecharge-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shellrecharge-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/shellrecharge/refs/heads/main/rate-limits/shellrecharge-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shellrecharge-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/shellrecharge/refs/heads/main/finops/shellrecharge-finops.yml
  title: ''
  type: FinOps
  url: finops/shellrecharge-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://developer.shell.com/latest-updates
created: '2026-06-21'
description: ShellRecharge (formerly NewMotion) is Shell's EV charging network and operator platform. Its EV-Platform / Shell Developer APIs let partners and charge point operators manage public charging - retrieving charging locations, starting, stopping, and tracking charge sessions, and exchanging locations, sessions, tariffs, tokens, and CDRs over the OCPI 2.2.1 standard. The APIs are partner-gated and secured with OAuth 2.0 client credentials.
finops:
- name: Shellrecharge Finops
  service_category: Mobility and EV Charging
  slug: shellrecharge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shellrecharge.png
layout: provider
modified: '2026-06-21'
name: ShellRecharge
nav: Providers
network: true
overview: 'ShellRecharge publishes 2 APIs on the [APIs.io](https://apis.io/) network: Locations API and Sessions API. Tagged areas include EV Charging, Electric Vehicles, Mobility, Charge Points, and OCPI.


  ShellRecharge''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Shellrecharge Plans Pricing
  plan_count: 1
  slug: shellrecharge-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Shellrecharge Rate Limits
  slug: shellrecharge-rate-limits
scopes:
- name: Shellrecharge Scopes
  scope_count: 0
  slug: shellrecharge-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 54.4
    catalog_earned_first_party: 0.0
    catalog_gap: 60.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 26.8
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 18.9
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/shellrecharge/refs/heads/main/screenshots/shellrecharge-2026-09-02T155127.png
security:
- kind: authentication
  name: Shellrecharge Authentication
  slug: shellrecharge-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Shellrecharge Domain Security
  slug: shellrecharge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: shellrecharge
tags:
- EV Charging
- Electric Vehicles
- Mobility
- Charge Points
- OCPI
- Energy
website: https://shellrecharge.com
---

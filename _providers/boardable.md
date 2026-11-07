---
access_model:
  confidence: low
  gated: private
  gated_source:
  - tag:No Public API
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://boardable.com/feed/
- group: auth
  href: https://artifacts.apis.io/boardable/security/boardable-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/boardable-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/boardable/security/boardable-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/boardable-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/boardable/security/boardable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boardable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boardable.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boardable
- group: docs
  title: ''
  type: Documentation
  url: https://docs.boardable.com/knowledge/getting-started-with-boardable
- group: commercial
  href: https://artifacts.apis.io/boardable/plans/boardable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boardable-plans-pricing.yml
created: '2026-07-05'
description: 'Boardable is board management software for nonprofits, associations, foundations, and other mission-driven organizations, covering meeting scheduling, agenda building, a document center, minutes and AI-generated meeting summaries, e-voting, task assignments, groups/committees, member directories, and built-in video conferencing. As of this review Boardable does NOT publish a documented public developer API: there is no developer portal, no published API reference, no OpenAPI, no self-serve API keys, and no documented webhooks. A private, authentication-gated backend API exists at https://api.boardable.com (for example, GET https://api.boardable.com/accounts returns HTTP 401 Unauthorized) that powers the Boardable web and mobile apps, but it is undocumented and not offered as a public/partner integration surface. Third-party listings occasionally describe Boardable as having an "open API," but Boardable provides no public developer documentation to substantiate that. Integrations
  are delivered through pre-built connectors (Salesforce, Microsoft 365 / Teams / Outlook / SharePoint / OneDrive, Google Drive & Calendar, Zoom, Dropbox, LinkedIn) rather than a documented API. This entry is therefore an honest stub: no APIs are listed because none are publicly documented.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boardable.png
layout: provider
modified: '2026-10-06'
name: Boardable
nav: Providers
network: true
overview: 'Boardable is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Board Management, Governance, Non-Profit, Meetings, and Collaboration.


  Boardable''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Boardable Plans Pricing
  plan_count: 4
  slug: boardable-plans-pricing
random_paper: 12
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/boardable/boardable-2026-07-25T203519.png
security:
- kind: domain-security
  name: Boardable Domain Security
  slug: boardable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Boardable Vulnerability Disclosure
  slug: boardable-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Boardable Trust Center
  slug: boardable-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: boardable
tags:
- Board Management
- Governance
- Non-Profit
- Meetings
- Collaboration
website: https://boardable.com
---

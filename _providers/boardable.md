---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/boardable-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/boardable-vulnerability-disclosure.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/boardable-plans-pricing.yml
created: '2026-07-05'
description: 'Boardable is board management software for nonprofits, associations, foundations, and other mission-driven organizations, covering meeting scheduling, agenda building, a document center, minutes and AI-generated meeting summaries, e-voting, task assignments, groups/committees, member directories, and built-in video conferencing. As of this review Boardable does NOT publish a documented public developer API: there is no developer portal, no published API reference, no OpenAPI, no self-serve API keys, and no documented webhooks. A private, authentication-gated backend API exists at https://api.boardable.com (for example, GET https://api.boardable.com/accounts returns HTTP 401 Unauthorized) that powers the Boardable web and mobile apps, but it is undocumented and not offered as a public/partner integration surface. Third-party listings occasionally describe Boardable as having an "open API," but Boardable provides no public developer documentation to substantiate that. Integrations
  are delivered through pre-built connectors (Salesforce, Microsoft 365 / Teams / Outlook / SharePoint / OneDrive, Google Drive & Calendar, Zoom, Dropbox, LinkedIn) rather than a documented API. This entry is therefore an honest stub: no APIs are listed because none are publicly documented.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boardable.png
layout: provider
modified: '2026-07-05'
name: Boardable
nav: Providers
network: true
overview: 'Boardable is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Board Management, Governance, Non-Profit, Meetings, and Board Portal.


  Boardable''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Boardable Plans Pricing
  plan_count: 4
  slug: boardable-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boardable/refs/heads/main/screenshots/boardable-2026-07-25T203519.png
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
- Board Portal
- Collaboration
- No Public API
website: https://boardable.com
---

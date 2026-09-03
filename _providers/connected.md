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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/connected-domain-security.yml
created: '2026-07-17'
description: Connected (Connected HQ, Inc.) was a social CRM and contact-management startup that pulled a user's address book, email and social accounts together into a single continuously-updated relationship manager. Backed by 500 Global, it was acquired by LinkedIn in October 2011 and folded into the LinkedIn-branded "Connected" product, after which the standalone service was retired. Connected never shipped a public developer program, API, SDK or documentation. The connectedhq.com domain is still defensively held by the acquirer (MarkMonitor registrar, Azure DNS and NS1 nameservers, SPF and DMARC p=reject, RFC 7505 null MX) but publishes no A record and serves no content. This profile is retained as a historical record; there is no API surface to enrich.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/connected.png
layout: provider
modified: '2026-07-20'
name: Connected
nav: Providers
network: true
overview: Connected is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Acquired, CRM, and Contacts.
random_paper: 2
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 5.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Connected Domain Security
  slug: connected-domain-security
  summary_line: DMARC
slug: connected
tags:
- Company
- Defunct
- Acquired
- CRM
- Contacts
- Address Book
- Relationship Management
- Social
---

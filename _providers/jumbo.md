---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.jumboprivacy.com'', ''status'': 303, ''note'': ''declared website redirects to https://blog.withjumbo.com/ — a different registrable domain (jumboprivacy.com -> withjumbo.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/coalition-inc/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jumbo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jumboprivacy.com
- group: company
  title: ''
  type: Blog
  url: https://blog.withjumbo.com/
created: '2026-07-17'
description: Jumbo (Jumbo Privacy) was a consumer privacy and security assistant for iOS and Android, founded in 2018 and headquartered in New York, that helped people manage the privacy settings across their social media and online accounts, clean up old posts, and monitor for data breaches. By design the app processed everything on-device and did not rely on server-side APIs to control user accounts, so it never exposed a public developer platform, OpenAPI specification, or SDK. Jumbo was acquired by Coalition, the B2B cyber insurer, in July 2023 and the consumer app has since been shut down. This API Evangelist profile is retained as a portfolio-company record for index-ventures; no API surface exists to enrich.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jumbo.png
layout: provider
modified: '2026-07-19'
name: Jumbo
nav: Providers
network: true
overview: 'Jumbo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Privacy, Consumer, and Mobile.


  Jumbo''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jumbo/refs/heads/main/screenshots/jumbo-2026-07-25T223309.png
security:
- kind: domain-security
  name: Jumbo Domain Security
  slug: jumbo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: jumbo
tags:
- Company
- Security
- Privacy
- Consumer
- Mobile
- Identity
- Data Protection
website: https://www.jumboprivacy.com
---

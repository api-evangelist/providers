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
api_count: 1
apis:
- description: Secure and modern passwordless authentication platform
  name: MojoAuth
  slug: mojoauth
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mojoauth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mojoauth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mojoauth.com
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://mojoauth.com/blog/feed/
created: '2026-05-28'
description: Secure and modern passwordless authentication platform
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mojoauth.png
layout: provider
modified: '2026-05-28'
name: MojoAuth
nav: Providers
network: true
overview: 'MojoAuth publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication And Authorization and Public APIs.


  MojoAuth''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.1
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
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mojoauth/refs/heads/main/screenshots/mojoauth-2026-06-20T185708.png
security:
- kind: domain-security
  name: Mojoauth Domain Security
  slug: mojoauth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mojoauth Vulnerability Disclosure
  slug: mojoauth-vulnerability-disclosure
  summary_line: disclosure policy published
slug: mojoauth
tags:
- Authentication And Authorization
- Public APIs
website: https://mojoauth.com
---

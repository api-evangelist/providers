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
api_count: 1
apis:
- description: Managed User Authentication Service
  name: LoginRadius
  slug: loginradius
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/loginradius-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loginradius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.loginradius.com/docs/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.loginradius.com/blog/rss.xml
created: '2026-05-28'
description: Managed User Authentication Service
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loginradius.png
layout: provider
modified: '2026-05-28'
name: LoginRadius
nav: Providers
network: true
overview: 'LoginRadius publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security and Public APIs.


  LoginRadius'' developer surface includes engineering blog and 4 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loginradius/refs/heads/main/screenshots/loginradius-2026-06-20T184655.png
security:
- kind: domain-security
  name: Loginradius Domain Security
  slug: loginradius-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Loginradius Trust Center
  slug: loginradius-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: loginradius
tags:
- Security
- Public APIs
website: https://www.loginradius.com/docs/
---

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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Bugcrowd API for interacting and tracking the reported issues programmatically
  name: Bugcrowd
  slug: bugcrowd
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/bugcrowd-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bugcrowd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bugcrowd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.bugcrowd.com/api/getting-started/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.bugcrowd.com/blog/
created: '2026-05-28'
description: Bugcrowd API for interacting and tracking the reported issues programmatically
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bugcrowd.png
layout: provider
modified: '2026-05-28'
name: Bugcrowd
nav: Providers
network: true
overview: 'Bugcrowd publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security and Public APIs.


  Bugcrowd''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 0
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
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bugcrowd/refs/heads/main/screenshots/bugcrowd-2026-06-20T173740.png
security:
- kind: domain-security
  name: Bugcrowd Domain Security
  slug: bugcrowd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bugcrowd Vulnerability Disclosure
  slug: bugcrowd-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Bugcrowd Trust Center
  slug: bugcrowd-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27018, FedRAMP, CSA STAR
slug: bugcrowd
tags:
- Security
- Public APIs
website: https://docs.bugcrowd.com/api/getting-started/
---

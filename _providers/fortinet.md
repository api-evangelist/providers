---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The Fortinet API provides access to platform services and data for enterprise integration and automation.
  name: Fortinet API
  slug: fortinet-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/fortinet-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fortinet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fortinet-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fortinet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fortinet
- group: company
  title: ''
  type: Website
  url: https://www.fortinet.com
- group: company
  title: ''
  type: Blog
  url: https://feeds.fortinet.com/fortinet/blogs
created: '2026-04-19'
description: Fortinet is a major US corporation and Fortune 1000 company. The Fortinet API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Fortinet Finops
  service_category: Cybersecurity / Networking
  slug: fortinet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fortinet.png
layout: provider
modified: '2026-04-19'
name: Fortinet
nav: Providers
network: true
overview: 'Fortinet publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity and Networking.


  Fortinet''s developer surface includes engineering blog and 6 more developer resources.'
plans:
- name: Fortinet Plans Pricing
  plan_count: 3
  slug: fortinet-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Fortinet Rate Limits
  slug: fortinet-rate-limits
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fortinet/refs/heads/main/screenshots/fortinet-2026-06-20T181441.png
security:
- kind: domain-security
  name: Fortinet Domain Security
  slug: fortinet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fortinet Vulnerability Disclosure
  slug: fortinet-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Fortinet Trust Center
  slug: fortinet-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: fortinet
tags:
- Cybersecurity
- Networking
website: https://www.fortinet.com
---

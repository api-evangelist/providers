---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
api_count: 1
apis:
- description: API for Dental Monitoring integration (no machine-readable spec found)
  name: Dental Monitoring API
  slug: dental-monitoring-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: Compliance
  url: https://dentalmonitoring.com/security/
- group: auth
  href: https://artifacts.apis.io/dental-monitoring/well-known/dental-monitoring-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dental-monitoring-security.txt
- group: agent
  href: https://artifacts.apis.io/dental-monitoring/well-known/dental-monitoring-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dental-monitoring-well-known.yml
- group: other
  href: https://artifacts.apis.io/dental-monitoring/hosts/dental-monitoring-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dental-monitoring-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dentalmonitoring.com/terms-of-use/
- group: auth
  title: ''
  type: Security
  url: https://dentalmonitoring.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dentalmonitoring.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://dentalmonitoring.com/doctor/login
- group: company
  title: ''
  type: Blog
  url: https://dentalmonitoring.com/blog/
- group: auth
  href: https://artifacts.apis.io/dental-monitoring/security/dental-monitoring-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dental-monitoring-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dental-monitoring/security/dental-monitoring-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dental-monitoring-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dental-monitoring/security/dental-monitoring-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dental-monitoring-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dentalmonitoring.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dentalmonitoring.com/integration/
- group: company
  title: ''
  type: AboutUs
  url: https://dentalmonitoring.com/about-us/
coverage:
  checked: '2026-10-23'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts were found despite accessible documentation.
  evidence:
  - status: 200
    url: https://dentalmonitoring.com/integration/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Dental Monitoring provides AI-powered dental monitoring solutions that enable remote orthodontic care, allowing clinicians to track patient progress through a patented scanning device and cloud platform. The company offers a suite of tools for dentists and orthodontists to monitor treatment, engage patients, and integrate data into practice workflows, supporting multiple languages and regulatory compliance.
image: https://dentalmonitoring.com/wp-content/uploads/2021/05/icon-patients.svg
layout: provider
modified: '2026-10-22'
name: Dental Monitoring
nav: Providers
network: true
overview: 'Dental Monitoring is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Dental, Artificial Intelligence, Healthcare, and Orthodontics.


  Dental Monitoring''s developer surface includes engineering blog, documentation, and 13 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 20.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dental-monitoring/dental-monitoring-2026-11-03T130530.png
security:
- kind: domain-security
  name: Dental Monitoring Domain Security
  slug: dental-monitoring-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dental Monitoring Vulnerability Disclosure
  slug: dental-monitoring-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dental Monitoring Trust Center
  slug: dental-monitoring-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: dental-monitoring
tags:
- Company
- Dental
- Artificial Intelligence
- Healthcare
- Orthodontics
website: https://dentalmonitoring.com/
---

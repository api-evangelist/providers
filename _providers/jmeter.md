---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Apache JMeter is a load testing and performance measurement tool for web applications, databases, FTP servers, JMS, mail protocols, and more. Provides extensible samplers, listeners, and a CLI mode fo
  name: Apache JMeter
  slug: jmeter
artifact_total: 6
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/jmeter/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/jmeter/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/jmeter/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/jmeter/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/jmeter/blob/master/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jmeter-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jmeter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jmeter.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://jmeter.apache.org/usermanual/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/jmeter
- group: operate
  title: ''
  type: Issues
  url: https://github.com/apache/jmeter/issues
- group: other
  title: ''
  type: Mailing List
  url: https://jmeter.apache.org/mail2.html
created: '2025-01-01'
description: Apache JMeter is an open-source Java application designed to load test functional behavior and measure performance of web applications and services. It can simulate heavy loads on servers, networks, and objects to test performance under different load types, supporting HTTP/HTTPS, SOAP/REST, databases, LDAP, JMS, and mail protocols.
finops:
- name: Jmeter Finops
  service_category: API
  slug: jmeter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jmeter.png
layout: provider
modified: '2026-04-28'
name: Apache JMeter
nav: Providers
network: true
overview: 'Apache JMeter publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Java, Load Testing, Open-Source, Performance Testing, and Testing.


  Apache JMeter''s developer surface includes documentation and 11 more developer resources.'
plans:
- name: Jmeter Plans Pricing
  plan_count: 3
  slug: jmeter-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Jmeter Rate Limits
  slug: jmeter-rate-limits
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 26.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jmeter/refs/heads/main/screenshots/jmeter-2026-06-20T183738.png
security:
- kind: domain-security
  name: Jmeter Domain Security
  slug: jmeter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jmeter Vulnerability Disclosure
  slug: jmeter-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jmeter
tags:
- Java
- Load Testing
- Open-Source
- Performance Testing
- Testing
website: https://jmeter.apache.org/
---

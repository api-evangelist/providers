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
api_count: 2
apis:
- description: The logging facade providing a feature-rich Java interface for application logging. Applications code against this stable API while delegating to a backing implementation such as Log4j Core.
  name: Log4j API
  slug: log4j-api
- description: The reference implementation of the Log4j API providing appenders, layouts, filters, lookups and configuration that route log events to consoles, files, databases, network endpoints and more.
  name: Log4j Core
  slug: log4j-core
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/logging-log4j2/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/logging-log4j2/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/log4j-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/log4j-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://logging.apache.org/log4j/2.x/
- group: docs
  title: ''
  type: Documentation
  url: https://logging.apache.org/log4j/2.x/manual/
- group: start
  title: ''
  type: GettingStarted
  url: https://logging.apache.org/log4j/2.x/manual/getting-started.html
- group: auth
  title: ''
  type: Security
  url: https://logging.apache.org/security.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://logging.apache.org/log4j/2.x/release-notes.html
- group: other
  title: ''
  type: Performance
  url: https://logging.apache.org/log4j/2.x/performance.html
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/apache/logging-log4j2
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
created: '2024-01-15'
description: Apache Log4j is a versatile, industrial-grade Java logging framework composed of an API, its implementation, and components to assist deployment for various use cases. It is part of the Apache Logging Services project. Log4j is a Java library distributed as Maven artifacts and is consumed via its Java API rather than over the network; no public HTTP/REST surface is published.
finops:
- name: Log4J Finops
  service_category: API
  slug: log4j-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/log4j.png
layout: provider
modified: '2026-04-28'
name: Apache Log4j
nav: Providers
network: true
overview: 'Apache Log4j publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Apache, Debugging, Java, Library, and Logging.


  Apache Log4j''s developer surface includes documentation, getting-started guide, release notes, and 10 more developer resources.'
plans:
- name: Log4J Plans Pricing
  plan_count: 3
  slug: log4j-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Log4J Rate Limits
  slug: log4j-rate-limits
score:
  band: emerging
  composite: 19.1
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
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 19.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/log4j/refs/heads/main/screenshots/log4j-2026-06-20T184648.png
security:
- kind: domain-security
  name: Log4J Domain Security
  slug: log4j-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Log4J Vulnerability Disclosure
  slug: log4j-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: log4j
tags:
- Apache
- Debugging
- Java
- Library
- Logging
- Monitoring
- Open-Source
website: https://logging.apache.org/log4j/2.x/
---

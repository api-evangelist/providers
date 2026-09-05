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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Apache Thrift is a lightweight, language-independent software stack for point-to-point RPC implementation. It provides abstractions for data transport, serialization, and application-level processing '
  name: Apache Thrift
  slug: thrift
artifact_total: 12
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/thrift-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thrift-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thrift.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://thrift.apache.org/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/thrift
- group: other
  title: ''
  type: Mailing List
  url: https://thrift.apache.org/mailing
- group: operate
  title: ''
  type: Issue Tracker
  url: https://issues.apache.org/jira/projects/THRIFT
- group: other
  title: ''
  type: Download
  url: https://thrift.apache.org/download
- group: build
  title: ''
  type: npm
  url: https://www.npmjs.com/package/thrift
- group: other
  title: ''
  type: Maven
  url: https://mvnrepository.com/artifact/org.apache.thrift/libthrift
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/thrift/
- group: other
  title: ''
  type: Packagist
  url: https://packagist.org/packages/apache/thrift
created: '2026-03-27'
description: Apache Thrift is a cross-language RPC framework originally developed at Facebook for scalable cross-language services development. It provides a lightweight, language-independent software stack for point-to-point RPC implementation with clean abstractions for data transport, serialization, and application-level processing. The framework includes an Interface Definition Language (IDL) compiler that generates client and server code for 28+ programming languages including C++, Java, Python, Go, Ruby, PHP, Node.js, C#, and many others, enabling seamless cross-language service communication.
examples:
- key_count: 11
  name: Thrift Calculator Service Example
  slug: thrift-calculator-service-example
- key_count: 7
  name: Thrift Client Server Example
  slug: thrift-client-server-example
finops:
- name: Thrift Finops
  service_category: API
  slug: thrift-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thrift.png
json_schemas:
- name: Apache Thrift IDL Definition
  property_count: 9
  slug: thrift-idl
json_structures:
- name: Thrift Idl Structure
  property_count: 0
  slug: thrift-idl-structure
jsonld:
- class_count: 42
  name: Thrift Context
  property_count: 15
  slug: thrift-context
layout: provider
modified: '2026-05-03'
name: Apache Thrift
nav: Providers
network: true
overview: 'Apache Thrift publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Apache, Code Generation, Cross-Language, Open-Source, and RPC.


  The Apache Thrift catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apache Thrift''s developer surface includes documentation and 11 more developer resources.'
plans:
- name: Thrift Plans Pricing
  plan_count: 3
  slug: thrift-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Thrift Rate Limits
  slug: thrift-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Apache Thrift API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: thrift-jsonschema-spectral-rules
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 71.3
    catalog_earned_first_party: 0.0
    catalog_gap: 43.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 22.7
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 26.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thrift/refs/heads/main/screenshots/thrift-2026-06-20T195317.png
security:
- kind: domain-security
  name: Thrift Domain Security
  slug: thrift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Thrift Vulnerability Disclosure
  slug: thrift-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: thrift
tags:
- Apache
- Code Generation
- Cross-Language
- Open-Source
- RPC
- SDK
- Serialization
- Thrift
website: https://thrift.apache.org/
---

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
api_count: 4
apis:
- description: The in-toto specification defines the metadata format for recording software supply chain steps. It includes layout metadata that defines the expected steps and their authorized functionaries, and lin
  name: in-toto Attestation Specification
  slug: in-toto-spec
- description: 'The in-toto Attestation Framework provides a specification for generating verifiable claims about any aspect of how a piece of software is produced. It defines a fixed lightweight Statement structure '
  name: in-toto Attestation Framework
  slug: in-toto-attestation-framework
- description: The Python reference implementation of in-toto provides tools and libraries for creating and verifying in-toto metadata. It includes the in-toto-run command for wrapping supply chain steps, in-toto-re
  name: in-toto Python Reference Implementation
  slug: in-toto-python
- description: A Go implementation of the in-toto specification that enables supply chain integrity verification in Go-based build and deployment pipelines. It provides the same core functionality as the Python refe
  name: in-toto Go Implementation
  slug: in-toto-golang
artifact_total: 14
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/in-toto/attestation/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/in-toto/attestation/releases
- group: auth
  title: ''
  type: DomainSecurity
  url: security/in-toto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://in-toto.io
- group: docs
  title: ''
  type: Documentation
  url: https://in-toto.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://in-toto.io/docs/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://in-toto.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://in-toto.io/community/
- group: operate
  title: ''
  type: FAQ
  url: https://in-toto.io/docs/faq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/in-toto
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/in-toto-layout-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/in-toto-link-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/in-toto-attestation-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/in-toto-context.jsonld
- group: design
  title: ''
  type: Rules
  url: rules/in-toto-rules.yml
created: '2026-03-16'
description: in-toto is a CNCF graduated framework for securing the integrity of software supply chains. It provides a specification for generating and verifying metadata about each step in a software supply chain, from source code to deployment. in-toto ensures that each step is performed by the authorized party and that materials and products are not tampered with between steps.
finops:
- name: In Toto Finops
  service_category: API
  slug: in-toto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/in-toto.png
json_schemas:
- name: in-toto Attestation Statement
  property_count: 4
  slug: in-toto-attestation
- name: in-toto Layout
  property_count: 6
  slug: in-toto-layout
- name: in-toto Link
  property_count: 7
  slug: in-toto-link
jsonld:
- class_count: 9
  name: In Toto Context
  property_count: 41
  slug: in-toto-context
layout: provider
modified: '2026-04-28'
name: In-Toto
nav: Providers
network: true
overview: 'In-Toto publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Native, Graduated, Security, Software Integrity, and Supply Chain Security.


  The In-Toto catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  In-Toto''s developer surface includes documentation, getting-started guide, engineering blog, FAQ, and 11 more developer resources.'
plans:
- name: In Toto Plans Pricing
  plan_count: 3
  slug: in-toto-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: In Toto Rate Limits
  slug: in-toto-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: In-Toto API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: in-toto-jsonschema-spectral-rules
- effective_rule_count: 0
  extends: []
  name: In-Toto API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: in-toto-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 68.3
    catalog_earned_first_party: 0.0
    catalog_gap: 46.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 28.0
    developer_ergonomics: 33.3
    discoverability: 72.2
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 28.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/in-toto/refs/heads/main/screenshots/in-toto-2026-06-20T183303.png
security:
- kind: domain-security
  name: In Toto Domain Security
  slug: in-toto-domain-security
  summary_line: TLSv1.3 · HSTS
slug: in-toto
tags:
- Cloud-Native
- Graduated
- Security
- Software Integrity
- Supply Chain Security
- Verification
website: https://in-toto.io
---

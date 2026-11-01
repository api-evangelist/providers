---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for creating, retrieving, and submitting fillable PDF and web forms as documented in the Guides section.
  name: Fillable Document API
  slug: fillable-document-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/jivrus/lifecycle/jivrus-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jivrus-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/jivrus/conformance/jivrus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jivrus-conformance.yml
- group: other
  href: https://artifacts.apis.io/jivrus/hosts/jivrus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jivrus-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jivrus.com/legal/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.jivrus.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jivrus.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jivrus.com/resources/guides/pricing-faq
- group: other
  title: ''
  type: Leadership
  url: https://www.jivrus.com/about/team
- group: docs
  title: ''
  type: Documentation
  url: https://www.jivrus.com/resources/guides
- group: company
  title: ''
  type: Blog
  url: https://blog.jivrus.com
- group: auth
  href: https://artifacts.apis.io/jivrus/security/jivrus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jivrus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jivrus.com/
coverage:
  checked: '2026-10-20'
  detail: Documentation pages exist but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://www.jivrus.com/resources/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Fillable Document provides a platform for creating, managing, and processing fillable PDF and web forms. Their service enables businesses to design interactive documents, collect data securely, and integrate submissions via webhooks or API calls. The company focuses on compliance, data privacy, and customizable workflows, supporting industries such as legal, finance, and healthcare. With a user-friendly editor and robust API, developers can automate form generation, retrieval, and submission handling, enhancing digital transformation initiatives.
image: https://lh7-us.googleusercontent.com/sitesv-images-rt/AMxu72vc3Vr1b8K9KAqjJ4DKlzlqpHpnoTDTz9laeeUei-n3CPVvU-YMzJJUqV1S9BcNDumSBZRy7zA5qh4RMiHjLFiWcaCa6het32bVIE3zlqkjmIiPGhrcSzXZ-kaazsGkNWAUPQlZrZBb6Cz2B_4dNjjci2k6D4uNGwc2lcoUcsf0VT74K7fZ05Kn=w16383
layout: provider
modified: '2026-10-20'
name: Fillable Document
nav: Providers
network: true
overview: 'Fillable Document is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Forms, PDF, Automation, and Compliance.


  Fillable Document''s developer surface includes support, pricing, documentation, engineering blog, and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Jivrus Domain Security
  slug: jivrus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jivrus
tags:
- Company
- Forms
- PDF
- Automation
- Compliance
website: https://jivrus.com/
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/invitae-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/invitae-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/invitae-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.invitae.com/us/provider-faqs/tech-and-quality
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/invitae-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/invitae-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/invitae-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/invitae-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.invitae.com/
- group: other
  title: ''
  type: Products
  url: https://www.invitae.com/us/providers
- group: operate
  title: ''
  type: Support
  url: https://www.invitae.com/us/provider-faqs
- group: company
  title: ''
  type: Blog
  url: https://blog.invitae.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.invitae.com/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/invitae
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.invitae.com/us/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.invitae.com/us/terms-of-use
coverage:
  checked: '2026-08-15'
  detail: Invitae ships genetic testing as a clinician-ordered laboratory service with no programmatic product of any kind — its one API-shaped host, api.invitae.com, is a private backend that answers a blanket nginx 403 on every path including the root, and the live site markets no API, no partner integration programme and no "request API access" form to gate one behind.
  evidence:
  - status: 403
    url: https://api.invitae.com/openapi.json
  - status: 404
    url: https://www.invitae.com/developers
  - status: 404
    url: https://www.invitae.com/llms.txt
  - status: 404
    url: https://www.invitae.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-24'
description: 'Invitae — operated as Labcorp Invitae / Labcorp Genetics since Labcorp acquired select Invitae assets out of the company''s 2024 Chapter 11 — is a United States medical genetics and healthcare-technology company providing clinical-grade hereditary and somatic genetic testing across oncology, women''s health, cardiology, neurology, pediatrics, and rare disease. Its laboratory is CLIA-certified and CAP-accredited, and it publishes a HIPAA Notice of Privacy Practices and state laboratory licensure. Clinicians order tests and receive results through a web portal with licensed genetic counseling and the Gia digital assistant. Invitae publishes no API: contract discovery across every Invitae host found no developer portal, no OpenAPI, no GraphQL endpoint, no MCP server, no A2A agent card, no FHIR CapabilityStatement, no SMART-on-FHIR configuration, no webhooks, no client SDK and no /.well-known document. api.invitae.com resolves but returns a blanket nginx 403 for every path, and
  the developer, docs and fhir subdomains do not resolve at all. The company''s public GitHub organization is genuine but consists of forks of upstream bioinformatics projects, not first-party specifications or libraries.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-08-15'
name: Invitae
nav: Providers
network: true
overview: 'Invitae is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, United States, Genomics, Genetic Testing, and Precision Medicine.


  Invitae''s developer surface includes support, engineering blog, and 14 more developer resources.'
plans:
- name: Invitae Plans Pricing
  plan_count: 0
  slug: invitae-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Invitae Rate Limits
  slug: invitae-rate-limits
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 18.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/invitae/refs/heads/main/screenshots/invitae-2026-07-25T222754.png
security:
- kind: domain-security
  name: Invitae Domain Security
  slug: invitae-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: invitae
tags:
- Healthcare
- United States
- Genomics
- Genetic Testing
- Precision Medicine
- Life Sciences
- Diagnostics
- Clinical Laboratory
- Oncology
- Rare Disease
website: https://www.invitae.com/
---
